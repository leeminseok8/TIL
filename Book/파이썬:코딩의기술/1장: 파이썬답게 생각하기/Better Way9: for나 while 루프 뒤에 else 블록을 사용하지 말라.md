## 💡 Better Way9: for나 while 루프 뒤에 else 블록을 사용하지 말라

파이썬에서는 루프가 반복 수행하는 내부 블록 바로 다음에 else 블록을 추가할 수 있다. 우리는 if / else 문에서 else는 '앞의 블록이 실행되지 않으면 이 블록을 실행하라'는 뜻으로 알고있다. try / except / else도 같은 의미로 동작한다.

파이썬에서 else, except, finally를 배운 프로그래머는 for / else의 else 부분을 **'루프가 정상적으로 완료되지 않으면 이 블록을 실행하라'는 뜻으로 가정하기 쉽다. 하지만 실제 else 블록은 완전히 반대로 동작한다.** 실제로 루프 안에서 break 문을 사용하면 else 블록이 동작하지 않는다.

또한 빈 시퀀스에 대한 루프를 실행하면 else 블록이 바로 실행된다.

```
for x in []:
    print('이 줄은 실행되지 않는다.')
else:
    print('else 동작')

>>>
else 동작



while False:
    print('이 줄은 실행되지 않는다.')
else:
    print('else 동작')

>>>
else 동작
```

이런 식으로 동작하는 이유는 루프를 사용해 검색을 수행할 경우, 루프 바로 뒤에 있는 else 블록이 그와 같이 동작해야 유용하기 때문이다. 예를 들어 두 수가 서로소인지 알아보고 싶을 때를 보자.

```
a = 4
b = 9

for i in range(2, min(a, b) + 1):
    print('검사 중', i)
    if a % i == 0 and b % i == 0:
        print('서로소 아님')
        break
else:
    print('서로소')

>>>
검사 중 2
검사 중 3
검사 중 4
서로소
```

하지만 else 블록을 사용함으로써 처음 코드를 보는 사람 입장에서는 직관적이지 못할 수 있다. 그러므로 도우미 함수를 작성하면 좋다.

```
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)
```

위의 방식이 코드를 처음 보는 사람들에게 훨씬 더 명확해 보일 것이다. 상호아에 따라 둘 다 좋은 선택이 될 수 있지만, else 블록을 사용함으로써 얻을 수 있는 표현력보다는 미래에 이 코드를 이해하려는 사람들이 느끼게 될 부담감이 더 크다. 파이썬에서 루프와 같은 간단한 구성요소는 그 자체로 의미가 명확해야 한다.