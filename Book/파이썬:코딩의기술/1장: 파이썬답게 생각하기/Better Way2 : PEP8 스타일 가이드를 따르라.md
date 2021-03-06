# 1장 파이썬답게 생각하기

## 💡 Better Way2 : PEP8 스타일 가이드를 따르라

### 공백
- 탭 대신 스페이스를 사용한 들여쓰기

- 라인 길이는 79개 문자 이하(한글은 영문 두 글자로 계산)

- 파일 안에서 각 함수와 클래스 사이에는 두 줄, 클래스 안에서 메서드와 메서드 사이에는 한 줄의 빈 줄을 넣어라.

- 변수 대입에서 = 전후에는 스페이스를 하나씩 넣는다.

- 타입 표기를 덧붙이는 경우에는 변수 이름과 콜론 사이에 공백을 넣지 말고, 클론과 타입 정보 사이에는 스페이스를 하나 넣어라.

### 명명규약
- 함수, 변수, 애트리뷰트는 소문자와 밑줄을 사용한다.(snake_case)

- 보호돼야 하는 인스턴스 애트리뷰트는 일반적인 규칙을 따르되, 밑줄로 시작한다.

- 비공개(Private) 인스턴스 애트리뷰트는 일반적인 규칙을 따르되, 밑줄 두 개로 시작한다.

- 클래스는 여러 단어를 이어 붙이되, 각 단어의 첫 글자를 대문자로 시작한다.(Pascal Case)

- 모듈 수준의 상수는 모든 글자를 대문자로 하고 단어 사이를 밑줄로 연결한 형태를 사용한다.

- 클래스에 들어 있는 인스턴스 메서드는 호출 대상 객체를 가리키는 첫 번째 인자의 이름으로 반드시 self를 사용해야 한다.

- 클래스 메서드는 클래스를 가리키는 첫 번째 인자의 이름으로 반드시 cls를 사용해야 한다.

### 식과 문
- 긍정식을 부정하지 말고(if not a is b) 부정을 내부에 넣어라.if a is not b)

- 빈 컨테이너나 시퀀스([], ‘’ 등)를 검사할 때는 길이를 0과 비교하지 말라.(len(a) == 0) 빈 컨테이너와 시퀀스는 암묵적으로 False 취급된다는 사실을 이용해 if not 컨테이너를 써라.

- 마찬가지로 비어 있지 않은 컨테이너나 시퀀스([1], ‘hi’ 등)를 검사할 때도 길이와 비교하지 말고, 대신 if 컨테이너가 비어 있지 않은 경우 암묵적으로 True인 점을 활용하라.

- 한 줄짜리 if 문이나 for, while 루프, except 복합문을 사용하지 말라. 명확성을 위해 여러 줄에 나눠 배치하라.

- 식을 한 줄 안에 다 쓸 수 없는 경우, 식을 괄호로 둘러싸고 줄바꿈과 들여쓰기를 추가해서 읽기 쉽게 만들어라. (여러 줄에 걸쳐 쓸 때는 \ 문자보다는 괄호를 사용하라)

### 임포트
PEP8은 모듈을 임포트해 코드에 사용하는 방법에 대해서도 가이드 라인을 제시한다.

- 모듈을 임포트할 때는 절대적인 이름을 사용하고, 현 모듈의 경로에 상대적인 이름은 사용하지 말라. 예를 들어 bar 패키지로부터 foo 모듈을 임포트한다면 from bar import foo라고 해야 하며, import foo라고 하면 안 된다.(반드시 상대경로 해야할 경우, from . Import foo처럼 명시적인 구문을 사용)

- 임포트를 적을 때는 표준 라이브러리 모듈, 서드 파티 모듈, 개인이 만든 모듈 순서로 섹션을 나눠라. 각 섹션에서는 알파벳 순서로 임포트하라.

### 📒 Note
파이린트(Pylint) 도구는 파이썬 소스 코드를 분석하는 정적 분석이다. 파이린트는 PEP8 스타일 가이드를 자동으로 실행해주고, 파이썬 프로그램에서 저지르기 쉬운 다양한 오류를 감지해준다. 여러 IDE와 에디터로 자체 린트 도구나 린트와 비슷한 기능을 제공하는 플러그인을 제공한다.