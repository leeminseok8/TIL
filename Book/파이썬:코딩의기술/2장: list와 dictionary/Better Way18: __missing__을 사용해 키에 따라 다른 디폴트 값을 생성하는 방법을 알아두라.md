## 💡 Better Way18: __missing__을 사용해 키에 따라 다른 디폴트 값을 생성하는 방법을 알아두라

내장 dict 타입의 setdefault와 collections 내장 모듈에 있는 defaultdict은 키가 없는 경우 짧은 코드로 처리할 수 있게 해준다. 하지만 모두 사용하기 적당하지 않은 경우도 있다.

예를 들어 파일 시스템에 있는 SNS 프로필 사진을 관리하는 프로그램을 작성한다고 가정해보자. 필요할 때 파일을 읽고 쓰기 위해 프로필 사진의 경로와 열린 파일 핸들을 연관시켜주는 딕셔너리가 필요하다. 다음 코드에서는 일반 dict 인스턴스를 사용하고 get 메서드와 대입식을 통해 키가 딕셔너리에 있는지 검사한다.

```
pictures = {}
path = 'profile_123.png'

if (handle := pictures.get(path)) is None:
    try:
        handle := pictures.get(path, a+b)
    except OSError:
        print(f'경로를 열 수 없습니다: {path}')
        raise
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()
```

read 메소드를 호출하는 부분은 open을 호출하고 예외를 처리하는 코드와 잘 분리돼 있으며 로지대로 잘 처리한 코드다.

이와 같은 로직을 구현하기 위해 in 식이나 KeyError를 사용한 접근 방법을 택할 수 도 있지만, 오히려 딕셔너리를 더 많이 읽고 내포되는 블록 깊이가 깊어지는 담점이 있다. 위의 방법이 잘 동작한다는 사실을 알면 setdefault도 잘 동작할 것이라 생각하기 쉽다.

```
try:
    handle = pictures.setdefault(path, open(path, 'a+b'))
except OSError:
    print(f'경로를 알 수 없습니다: {path}')
    raise
else:
    handle.seek(0)
    image_data = handle.read()
```

이 코드는 open이 딕셔너리에 경로가 있는지 여부와 관계없이 항상 호출되는 문제가 있다. 이로 인해 기존 파일과 혼동될 수 있는 새로운 파일이 생성될 수 있다. 그래서 open이 예외를 처리할 수 있으므로 예외를 처리해야 한다. 하지만 한 줄에 있는 setdefault로 인해 던지는 예외를 구분하지 못할 수도 있다.(딕셔너리와 비슷한 구현을 사용하면 이런 예외가 발생할 수 있다.)

이전 예제를 도우미 함수와 defaultdict 클래스를 사용해 작성할 수도 있다.

```
from collections import defaultdict

def open_picture(profile_path):
    try:
        return open(profile_path, 'a+b')
    except OSError:
        print(f'경로를 열 수 없습니다: {path}')
        raise

pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()

>>>
Traceback ...
TypeError: open_picture() missing 1 required positional
argument: 'profile_path'
```

문제는 defaultdict 생성자에 전달한 함수는 인자를 받을 수 없다는 데 있다. 호출하는 도우미 함수가 처리 중인 키를 알 수 없다는 의미다. 이로 인해 open을 호출할 방법이 없다.

이러한 상황을 해결하기 위해 파이썬ㄴ은 다른 해법을 내장해 제공한다. dict 타입의 하위클래스를 만들고 __missing__ 특별메소드를 구현하면 키가 없는 경우를 처리하는 로직을 커스텀화할 수 있다.

```
class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value

pictures = defaultdict(open_picture)
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
```

딕셔너리에 접근해서 키가 없으면 __missing__ 메서드가 호출된다. 이 메서드는 키에 해당하는 디폴트 값을 생성해 딕셔너리에 넣어준 다음 호출한 쪽에 그 값을 반환해야 한다. 이후 같은 경로에 접근하면 원소가 존재하므로 __missing__ 이 호출되지 않는다.