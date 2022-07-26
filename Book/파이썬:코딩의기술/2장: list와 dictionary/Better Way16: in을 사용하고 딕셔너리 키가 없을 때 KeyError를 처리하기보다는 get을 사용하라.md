## 💡 Better Way16: in을 사용하고 딕셔너리 키가 없을 때 KeyError를 처리하기보다는 get을 사용하라

딕셔너리와 상호작용하는 연산은 키나 키에 연관된 값에 접근하고, 대입하고, 삭제하는 것이다. 딕셔너리의 내용은 동적이므로 어떤 키에 접근하거나 키를 삭제할 때 그 키가 딕셔너리에 없을 수도 있다.

예를 들어 투표를 진행했다고 하자.

```
try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1

---

count = counters.get(key, 0)
counters[key] = count + 1
```

위 두 코드는 같은 결과를 나타내지만 get을 사용한 코드가 짧고 가독성이 뛰어나다. 따라서 간단한 타입의 값이 들어 있는 딕셔너리의 경우 get 메소드를 사용하는 방법이 가장 코드가 짧고 깔끔하다.

> 이 예제처럼 카운터로 이루어진 딕셔너리를 유지해야 하는 경우에는 collections 내장 모듈에 있는 Counter클래스를 고려해보자. 카운터를 쓸 때 필요한 대부분의 기능을 제공한다.

딕셔너리에 들어있는 값이 리스트처럼 복잡한 경우는 어떻게 해야 할까? 예를 들어 득표수만이 아닌 투표한 사람의 이름도 알고싶다면 value값으로 리스트를 연관시킬 수 있다.

```
votes = {
    '영웅이' = ['덕칠', '준빈'],
    '민석이' = ['상훈']
}
key = '치'
who = '킨'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

>>>
{'영웅이' = ['덕칠', '준빈'], '민석이' = ['상훈'], '치': [킨]}
```

위의 방식도 동작하지만 in을 사용하면 키를 두 번 읽어야 하고, 값을 한 번 대입해야 한다. votes[key] = names = []을 사용한 이중 대입문으로 한 줄에 처리 가능하다.

```
if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)
```

위의 코드를 사용하면 한 번의 읽기와 대입만으로 사용 가능하다. 또한 if문 안에 대입식을 사용하면 더 짧게 쓸 수 있어서 가독성이 좋아진다.

---

### setdefault

dict 타입은 이 패턴을 더 간단히 사용할 수 있게 해주는 setdefault 메서드를 제공한다. get과 setdefault의 차이는 dict에 접근하여 값을 불러올지 대입할지이다.

```
names = votes.setdefault(key, [])
names.append(who)
```

get을 사용했을 때보다 한 줄이 더 짧다. 존재하지 않는 key에 접근했을 때 빈 리스트를 dict에 바로 대입한다.

setdefault에는 아쉬운 점이 몇 가지 있다. 첫 번째는 메소드만 보면 가독성이 떨어진다는 점이다. 성능을 보면 get_or_set이 적절한데 이름은 그렇지 않다.

두 번째는 **존재하지 않는 키에 접근하면 복사하지 않고 바로 딕셔너리에 대입한다는 것**이다. 즉, 호출할 때마다 리스트를 만들어야 하므로 성능이 크게 떨어질 수 있다.

다시 돌아가서 투표 예제로 돌아가보자. 왜 setdefault를 사용하지 않았을까?

```
count = counters.setdefault(key, 0)
counters[key] = count + 1
```

여기서 문제점은 setdefault는 키가 존재하지 않으면 바로 대입한다는 것이다. get을 이용한 투표는 존재하지 않으면 0을 변수에 저장하고 dict에 대입하는 것은 +1 한 번이다. 하지만 setdefault는 0과 +1 두 번 대입하기 때문에 성능이 떨어진다.

setdefault를 사용하는 것이 딕셔너리 키를 처리하는 지름길인 경우는 드물다. 디폴트 값을 만들어내기 쉽거나, 변경 가능한 값이거나, 리스트 인스턴스처럼 값을 만들어낼 때 예외가 발생할 가능성이 없는 경우에 사용할 수 있다. 이렇게 구체적인 경우에는 get보다 setdfault를 사용하는 편이 낫다.