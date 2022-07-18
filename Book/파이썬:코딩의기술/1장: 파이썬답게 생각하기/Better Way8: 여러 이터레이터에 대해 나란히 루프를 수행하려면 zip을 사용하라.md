## 💡 Better Way8: 여러 이터레이터에 대해 나란히 루프를 수행하려면 zip을 사용하라

파이썬에서는 관련된 객체가 들어 있는 리스트를 다수 다루는 경우가 자주 있다. 리스트 컴프리헨션을 사용하여 소스 list에서 새로운 list를 파생시키기 쉽고, 두 리스트를 동시에 이터레이션할 경우 소스 리스트의 길이를 사용해 이터레이션할 수 있다.

```
names = ['minxi', 'minseok', '이민석']

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_count)

>>>
minseok
```

위 방식은 한 눈에 보기에도 잡음이 많으므로 개선이 필요해 보인다. enumerate를 사용하면 약간 나아지지만 충분하지않다.


### zip
이런 코드를 더 깔끔하게 만들 수 있도록 파이썬은 zip 내장 함수를 제공한다. zip 제너레이터는 둘 이상의 이터레이터의 다음 값이 들어 있는 튜플을 반환한다. 이 튜플을 for 문에서 바로 언패킹할 수 있다. 

```
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

names.append('리민시')
for name, count in zip(names, counts):
    print(name)

>>>
minxi
minseok
이민석
```

zip은 자신이 감싼 이터레이터의 길이가 같을 경우 중단되는 위험 없이 처리한다. 하지만 입력 이터레이터의 길이가 서로 다를 때는 zip 동작에 주의해야 한다. 예를 들어, names를 추가하고 count를 갱신하지 못했다면 위와 같이 동작한다.

zip은 감싼 이터레이터 중 어느 하나가 끝날 때까지 튜플을 생성한다. 즉, 출력은 가장 짧은 입력의 길이와 같다.

하지만 리스트의 길이가 같지 않을 것을 예상하고 뒷부분을 출력하고 싶다면 itertools 내장 모듈에 들어 있는 zip_longest를 사용할 수 있다.

```
import itertools

for name, count in itertools.zip_longest(name, count):
    print(f'{name}: {count}')

>>>
minxi: 5
minseok: 7
이민석: 3
리민시: None
```

zip_longest는 존재하지 않는 값을 자신에게 전달된 fillvalue로 대신한다. 디폴트 fillvalue는 None이다.