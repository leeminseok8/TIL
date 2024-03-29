# Better Way 11~13

## 💡 Better Way11: 시퀀스를 슬라이싱하는 방법을 익혀라

슬라이싱할 때 인덱스 범위를 넘어가는 시작과 끝 인덱스는 조용히 무시된다. 반면 같은 인덱스에 직접 접근하면 예외가 발생한다.

```
a = [1,2,3,4,5,6,7,8,9,10]

first_item = a[:20]
second_item = a[20:]

a[20]

>>>IndexError: list index out of range
```

> somelist[-n:]에서 n이 0보다 클 경우 잘 동작하지만, n이 0이면 somelist[:]와 같기 때문에 원래 리스트를 복사한다.

언패킹 대입과 달리 슬라이스 대입은 슬라이스와 대입된 리스트의 길이가 같을 필요가 없다. 그래서 지정 슬라이스 길이보다 대입되는 별열의 길이가 짧거나 길면 따라간다.

```
print(a)
a[2:4] = [6]
print(a)

>>>
[1,2,3,4,5]
[1,2,6,5]
```

길어도 마찬가지로 동작한다. 인덱스가 없는 슬라이스에 대입하면(새 리스트 대신) 슬라이스가 참조하는 리스트의 내용을 대입하는 리스트의 복사본으로 덮어 쓴다.

```
b = a
print(a, b)
a[:] = [10,11,12]
print(a, b)

>>>
[1,2,3,4,5]
[10,11,12]
```

---

## 💡 Better Way12: 스트라이드와 슬라이스를 한 식에 함께 사용하지 말라

파이썬은 일정한 간격을 두고 슬라이싱하는 구문을 제공하는데, 이를 스트라이드라고 한다.

```
x = ['빨강', '주황', '노랑', '초록']
odds = x[::2]
evens = x[1::2]
print(odds, evens)

>>>
['빨강','노랑'] ['주황','초록']
```

> 유니코드 데이터를 UTF-8로 인코딩한 문자열에서는 역으로 뒤집는 코드가 동작하지 않는다. UTF-8 인코딩의 바이트 순서를 뒤집으면 원래 인코딩 바이트 문자열 코드에서 2바이트 이상으로 이뤄졌던 문자들은 코드개 깨지기 때문이다. 단, 모든 문자가 아스키 코드 범위에 들어가는 문자라면 문제없을 수도 있다.(아스키 코드 문자열은 인코딩시 아스키 코드와 같은 1바이트로 인코딩 된다.)

```
w = 'abcZYX123'
x = w.encode('utf-8')
y = x[::-1]
z = y.decode('utf-8')
print(z)

>>>
'321XYZcba'
```

슬라이싱 구문에 스트라이딩까지 들어가면 가독성이 떨어진다. 그러므로 각각 나누어 진행하는 것을 권장한다.

```
y = x[::2]  # [1,3,5,7]
z = y[1:-1] # [3,5]
```

리스트는 O(N)의 시간복잡도를 가지므로 스트라이딩 후 슬라이싱 하면 시간복잡도를 줄일 수 있다. 그러므로 첫 번째 연산은 결과 슬라이스의 크기를 가능한 한 줄일 수 있어야 한다.

---

## 💡 Better Way13: 슬라이싱보다는 나머지 모두 잡아내는 언패킹을 사용하라

기본 언패킹의 한 가지 한계점은 언패킹할 시퀀스의 길이를 알고 있어야 한다는 점이다. 또한 인덱스와 슬라이싱을 사용하면 직관성이 떨어지고, 시퀀스 원소를 하위 집합으로 나누면 1차이 나는 인덱스로 인한 오류를 만들기 쉽다.

```
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(oldest, second_oldest, others)

>>>
20 19 [18, ... ,1]
```

이런 상황을 잘 다룰 수 있도록 파이썬은 **별표 식**을 사용해 모든 값을 언패킹할 수 있게 지원한다. 다음은 인덱스나 슬라이싱없이 언패킹을 사용하는 코드다.

```
oldest, second_oldest, *others = car_ages_descending
print(oldest, second_oldest, others)

>>>
20 19 [18, ... ,1]
```

이 코드가 더 짧고, 직관적이고, 인덱스 경계 값이 어긋나서 오류가 발생할 여지도 없다.

언패킹 변수 위치에 따라 인덱스 위치를 선정할 수 있지만, 별표 식이 포함된 언패킹을 대입 처리하려면 최소 하나의 필수 대입이 필요하다. 그렇지 않으면 SyntaxError가 발생한다. (별표 식만으로 언패킹할 수 없다)

또한, 한 수준(같은 리스트)의 언패킹 패턴에 별표 식을 두 개 이상 쓸 수도 없다.