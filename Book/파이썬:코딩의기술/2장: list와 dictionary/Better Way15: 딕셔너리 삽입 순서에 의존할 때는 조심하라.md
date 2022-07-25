## 💡 Better Way15: 딕셔너리 삽입 순서에 의존할 때는 조심하라

파이썬 3.5 이전에는 딕셔너리에 대해 이터레이션을 수행하면 키를 임의의 순서로 돌려줬으며, 이터레이션 순서는 원소가 삽입된 순서와 일치하지 않았다.

그 이유는 예전의 딕셔너리 구현이 내장 hash 함수와 파이썬 인터프리터가 시작할 때 초기화되는 난수 씨앗값(seed)을 사용하는 해시 테이블 알고리즘으로 만들어졌기 때문이다.

3.6부터는 딕셔너리가 삽입 순서를 보존하도록 동작이 개선됐고, 파이썬 3.7부터는 아예 파이썬 언어 명세에 이 내용이 포함됐다.

---

우리가 딕셔너리를 처리할 때 앞에서 설명한 삽입 순서 관련 동작이 항상 성립한다고 가정해서는 안 된다. 파이썬에서 프로그래머가 list, dict 등의 표준 프로토콜을 흉내 내는 커스텀 컨테이너 타입을 쉽게 정의할 수 있다. 파이썬은 정적 타입 지정 언어가 아니기 때문에 대부분의 경우 코드는 엄격한 클래스 계층보다는 개체 동작이 객체의 실질적인 타입을 결정하는 **덕 타이핑**에 의존하며, 이로 인해 가끔 어려운 함정에 빠질 수 있다.

> '덕타이핑' 이란?
<br> 
동적 타입 지정의 일종으로, 객체가 실행 시점에 어떻게 행동하는지를 기준으로 객체의 타입을 판단하는 타입 지정 방식이다. 실질적으로 아무런 타이핑을 하지 않고 런타임에 객체가 제공하는 애트리뷰트와 메서드가 없는 경우에는 그냥 오류를 내겠다는 말과 같다.

귀여운 동물 콘테스트 프로그램을 작성한다고 하자.

```
votes = {
    'panda' : 1001,
    'tiger' : 550,
    'dog' : 381900
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks):
    return next(iter(ranks))
```

콘테스트에서 어떤 동물이 우승했는지 보여주는 함수이다. 이 함수는 populate_ranks가 ranks 딕셔너리에 내용을 등수 오름차순으로 등록한다고 가정하고 동작한다.

```
ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(rnaks)
print(winner)

>>>
{'dog': 1, 'panda': 2, 'tiger': 3}
dog
```

여기서 요구사항이 변경됐다고 가정해보자. UI 요소에서 보여줄 때 순위가 아닌 알파뱃순으로 표시해야 한다. 이 경우에는 collections.abc 모듈을 사용해 딕셔너리와 비슷하지만 내용을 알파뱃 순서대로 이터레이션해주는 클래스를 새로 정의할 수 있다.

```
from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.date = {}

    def __getitem__(self, key):
        return self.data[key]

    def __setitem__(self, key, value):
        self.date[key] = value

    def __delitem__(self, key):
        del self.date[key]

    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key

    def __len__(self):
        return len(self.data)
```

SortedDict는 표준 딕셔너리의 포로토콜을 지키므로, 앞에서 정의한 함수를 호출하면서 사용해도 오류가 발생하지 않는다. 하지만 실행 결과는 요구 사항에 맞지 않는다.

여기서 문제는 get_winner의 구현이 populate_ranks의 삽입 순서에 맞게 딕셔너리를 이터레이션한다고 가정했다는 데 있다. 따라서 우승 동물로는 득표수가 1등이 아닌 알파벳 순서로 동물이 반환된다.

이러한 문제 해결 방법으로는 세 가지가 있다.

첫 번째 방법은 ranks 딕셔너리가 특정 순서로 이터레이션된다고 가정하지 않고 get_winner 함수는 구현하는 것이다. 가장 보수적이고 튼튼한 해법이다.

```
def get_winner(ranks):
    for name, rank in ranks.items():
        if rank == 1:
            return name
```

두 번째는 함수 맨 앞에 ranks의 타입이 내가 원하는 타입인지 검사하는 코드를 추가하는 것이다. 원하는 타입이 아니면 예외를 던지는 것이고, 첫 번째 방법보다 싱행 성능이 더 좋을 것이다.

```
def get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError('dict 인스턴스가 필요합니다')
    return next(iter(ranks))
```

세 번째는 타입 어노테이션을 사용해서 get_winner에 전달되는 값이 딕셔너리와 비슷한 동작을 하는 MutableMapping 인스턴스가 아니라 dict 인스턴스가 되도록 강제하는 것이다. 다음 코드는 앞의 코드에 타입 어노테이션을 붙이고 mypy 도구를 엄격한 모드로 사용한다.

```
from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int],
                   ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.sort, reverse=True)
    for i, name in enumerate(names, 1)
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))
```

dict와 MutableMapping 타입의 차이를 올바로 감지해서 적절할 타입의 객체를 사용하지 않았을 때 오류를 발생시킨다. 이 해법은 정적 타입 안정성과 런타임 가능성을 가장 잘 조합해준다.