## π‘ Better Way14: λ³΅μ‘ν κΈ°μ€μ μ¬μ©ν΄ μ λ ¬ν  λλ key νλΌλ―Έν°λ₯Ό μ¬μ©νλΌ

list λ΄μ₯ νμμλ λ¦¬μ€νΈμ μμλ₯Ό κΈ°μ€μ λ°λΌ μ λ ¬ν  μ μλ sort λ©μλκ° λ€μ΄ μλ€. κΈ°λ³Έμ μΌλ‘ sortλ λ¦¬μ€νΈμ λ΄μ©μ μμ νμμ λ°λ₯Έ μμ°μ€λ¬μ΄ μμλ₯Ό μ¬μ©ν΄ μ€λ₯Έμ°¨μμΌλ‘ μ λ ¬νλ€.

sort λ©μλλ μμ°μ€λ½κ² μμλ₯Ό μ ν  μ μλ λλΆλΆμ λ΄μ₯ νμ(λ¬Έμμ΄, λΆλμμμ  μ λ±)μ λν΄ μ λμνλ€. νμ§λ§ κ°μ²΄λ μ΄λ»κ² μ²λ¦¬ν κΉ?

```
class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return (f'Tool({self.name!r}, {self.weight})')

tools = [
    Tool('μ°¨λ¨κΈ°', 3.5),
    Tool('ν΄λ¨Έ', 2.5),
    Tool('κΉ½νΌ', 10),
    Tool('ν¬λ μΈ', 10)
]
```

sort λ©μλκ° νΈμΆνλ κ°μ²΄ λΉκ΅ νΉλ³ λ©μλκ° μ μλΌ μμ§ μμΌλ―λ‘ μ΄λ° νμμ κ°μ²΄λ μ λ ¬ν  μ μλ€.

> μ λ ¬μ μ¬μ©νκ³  μΆμ μ νΈλ¦¬λ·°νΈκ° κ°μ²΄μ λ€μ΄ μλ κ²½μ°κ° λ§λ€. μ΄λ° μν©μ μ§μνκΈ° μν΄ sortμλ keyλΌλ νλΌλ―Έν°κ° μλ€. keyλ ν¨μμ¬μΌ νκ³ , key ν¨μμλ μ λ ¬ μ€μΈ λ¦¬μ€νΈμ μμκ° μ λ¬λλ€. key ν¨μκ° λ°ννλ κ°μ μμ λμ  μ λ ¬ κΈ°μ€μΌλ‘ μ¬μ©ν , λΉκ΅ κ°λ₯ν(μ¦, μμ°μ€λ¬μ΄ μμκ° μ μλ) κ°μ΄μ΄μΌλ§ νλ€.

λ€μ μμ μλ lambda ν€μλλ‘ ν¨μλ₯Ό μ μνλ€.

```
print('λ―Έμ λ ¬', repr(tools))
tools.sort(key=lambda x:x.name)
print('/nμ λ ¬', tools)
```

μ΄ ν¨μλ₯Ό keyλ‘ μ¬μ©νλ©΄ Tool κ°μ²΄λ‘ μ΄λ€μ§ λ¦¬μ€νΈλ₯Ό μ΄λ¦(name)μ λ°λΌ μνλ±μμΌλ‘ μ λ ¬νλ€. μμ μ΄νΈλ¦¬λ·°νΈμ μ κ·Όνκ±°λ μΈλ±μ€λ₯Ό μ¨μ κ°μ μ»κ±°λ(μμκ° μνμ€, νν, λμλλ¦¬μΈ κ²½μ°) λ€λ₯Έ λͺ¨λ  μμ μ¬μ©ν  μ μλ€.

### μ¬λ¬ κΈ°μ€
λλ‘λ μ¬λ¬ κΈ°μ€μ μ¬μ©ν΄ μ λ ¬ν΄μΌ ν  μλ μλ€. μλ₯Ό λ€μ΄, weightλ‘ λ¨Όμ  μ λ ¬ν λ€μμ nameμΌλ‘ μ λ ¬νκ³  μΆλ€λ©΄ μ΄λ»κ² ν΄μΌ ν κΉ?

κ°μ₯ μ¬μ΄ λ°©λ²μ νν νμμ μ°λ κ²μ΄λ€. ννμ κΈ°λ³Έμ μΌλ‘ λΉκ΅ κ°λ₯νλ©° μμ°μ€λ¬μ΄ μμκ° μ ν΄μ Έ μλ€. λΉκ΅νλ λ ννμ μ²« λ²μ§Έ μμΉμ κ°μ΄ κ°μλ©΄ λ λ²μ§Έ, μΈ λ²μ§Έ κ³μ λΉκ΅λ₯Ό λ°λ³΅νλ€.

```
tools.sort(key=lambda x:(x.weight, x.name))

>>>
[Tool('ν΄λ¨Έ', 2.5), Tool('μ°¨λ¨κΈ°', 3.5), Tool('κΉ½νΌ', 10)], Tool('ν¬λ μΈ', 10)
```

μμ μ½λμ²λΌ μ΄νΈλ¦¬λ·°νΈμ μ°μ μμμ λ°λΌ ννμ λ£μ΄ λ°ννλ key ν¨μμ΄λ€. (μμλΆν° μμ μ‘΄μ¬ : weight -> name) sort λ©μλμ reverse νλΌλ―Έν°λ₯Ό Trueλ‘ μ μ©νλ©΄ λ κΈ°μ€μ μ λ ¬ μμκ° λκ°μ΄ μν₯μ λ°κ³ , λ¨ν­ λΆνΈ λ°μ (-) μ°μ°μλ₯Ό μ¬μ©ν΄ μ λ ¬ λ°©ν₯μ νΌν©ν  μλ μλ€. (μ΄ κ²½μ°, λͺ¨λ  νμμλ μ¬μ©ν  μ μλ€.)

```
tools.sort(key=lambda x:(x.weight, -x.name))

>>>
TypeError: bad operand type for unary -: 'str'
```

νμ΄μ¬μμλ μ΄λ° μν©μ μν΄ μμ μ μΈ μ λ ¬ μκ³ λ¦¬μ¦μ μ κ³΅νλ€. sort λ©μλλ key ν¨μκ° λ°ννλ κ°μ΄ μλ‘ κ°μ κ²½μ° λ¦¬μ€νΈμ λ€μ΄ μλ μλ μμλ₯Ό κ·Έλλ‘ μ μ§ν΄μ€λ€. μ¦ κ°μ λ¦¬μ€νΈμμ λ€λ₯Έ κΈ°μ€μΌλ‘ sortλ₯Ό μ¬λ¬ λ² νΈμΆν΄λ λλ€λ μλ―Έμ΄λ€.

```
tools.sort(key=lambda x:x.name)

tools.sort(key=lambda x:x.weight, reverse=True)

>>>
[Tool('κΉ½νΌ', 10), Tool('ν¬λ μΈ', 10), Tool('μ°¨λ¨κΈ°', 3.5), Tool('ν΄λ¨Έ', 2.5)]
```

μμ κ°μ μ κ·Ό λ°©λ²μ μ¬μ©νλ©΄ μ¬λ¬ λ€λ₯Έ νμμ μ λ ¬ κΈ°μ€μ μνλ λ°©ν₯μΌλ‘ μλ‘ μ‘°ν©ν  μ μλ€. **λ€λ§, μ»κ³  μΆμ μ λ ¬ κΈ°μ€ μ°μ μμμ μ­μμΌλ‘ μ λ ¬ν΄μΌ νλ€.**

κΌ­ νμν κ²½μ°κ° μλλΌλ©΄ λ¨ν­ λΆνΈ λ°μ  μ°μ°μλ₯Ό νμ©νλ κ²μ΄ μ’κ³ , κΌ­ νμν  λλ§ sortλ₯Ό μ¬λ¬ λ² νΈμΆνλ λ°©λ²μ μ¬μ©νλ κ²μ΄ μ’λ€.