## 💡 Better Way17: 내부 상태에서 원소가 없는 경우를 처리할 때는 setdefault보다 defaultdict를 사용하라

get 메소드를 사용하는 것이 in과 KeyError를 사용하는 방법보다 낫지만, 경우에 따라 setdefault가 나을 수도 있다.

```
visits = {
    '미국' : {'뉴욕', '워싱턴'},
    '스페인' : {'세비야', '론도', '바르셀로나'}
}

visits.setdefault('영국', set()).add('브라이튼')
```

딕셔너리 안에 나라 이름이 들어 있는지 여부와 상관없이 각 집합에 새 도시를 추가할 때 setdefault를 사용할 수 있다.

직접 딕셔너리 생성을 제어할 수 있다면 어떨까? 예를 들어 클래스 내부에서 상태를 유지하기 위해 딕셔너리 인스턴스를 사용할 때가 이런 경우에 해당한다.

```
class Visits:
    def __init__(self):
        self.data = {}

    def add(self, country, city):
        city_set = self.data.setdefault(country, set())
        city_set.add(city)

visits = Visits()
visits.add('프랑스', '니스')
print(visits.data)

>>>
{'프랑스' : {'니스'}}
```

하지만 visits.add 메서드는 이상적이지 않다. 메서드 이름이 여전히 헷갈리고 처음 읽는 사람이 동작을 바로 이해하기 어렵다. 그리고 키의 존재 유무에 상관없이 매 호출마다 set 인스턴스를 만들기 때문에 효육적이지도 않다.

---

<br>

### **defaultdict**

다행히 collections 내장 모듈에 있는 defaultdict라는 클래스는 키가 없을 때 자동으로 디폴트 값을 저장해서 간단히 처리할 수 있게 해준다. 내가 해야할 일은 키가 없을 때 디폴트 값을 만들기 위해 호출할 함수를 제공하는 것뿐이다. defaultdict를 사용해서 다시 작성한 것이다.

```
from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)

    def add(self, country, city):
        self.data[country].add(city)

visits = Visits()
visits.add('독일', '알차이')

>>>
defaultdict<class 'set'>, {'독일' : '알차이'}
```

add 구현이 더 짧고 간단해졌다. data 딕셔너리에 있는 키에 접근하면 기존 set 인스턴스가 반환된다고 가정한다. 이 구현에서 불필요한 set이 만들어지는 경우는 없다. 이와 유사한 경우에는 setdefault보다 defaultdict를 사용하는 편이 낫다.