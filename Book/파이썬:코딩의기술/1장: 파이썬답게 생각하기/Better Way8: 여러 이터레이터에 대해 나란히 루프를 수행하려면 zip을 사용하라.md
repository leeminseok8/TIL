## ๐ก Better Way8: ์ฌ๋ฌ ์ดํฐ๋ ์ดํฐ์ ๋ํด ๋๋ํ ๋ฃจํ๋ฅผ ์ํํ๋ ค๋ฉด zip์ ์ฌ์ฉํ๋ผ

ํ์ด์ฌ์์๋ ๊ด๋ จ๋ ๊ฐ์ฒด๊ฐ ๋ค์ด ์๋ ๋ฆฌ์คํธ๋ฅผ ๋ค์ ๋ค๋ฃจ๋ ๊ฒฝ์ฐ๊ฐ ์์ฃผ ์๋ค. ๋ฆฌ์คํธ ์ปดํ๋ฆฌํจ์์ ์ฌ์ฉํ์ฌ ์์ค list์์ ์๋ก์ด list๋ฅผ ํ์์ํค๊ธฐ ์ฝ๊ณ , ๋ ๋ฆฌ์คํธ๋ฅผ ๋์์ ์ดํฐ๋ ์ด์ํ  ๊ฒฝ์ฐ ์์ค ๋ฆฌ์คํธ์ ๊ธธ์ด๋ฅผ ์ฌ์ฉํด ์ดํฐ๋ ์ด์ํ  ์ ์๋ค.

```
names = ['minxi', 'minseok', '์ด๋ฏผ์']

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

์ ๋ฐฉ์์ ํ ๋์ ๋ณด๊ธฐ์๋ ์ก์์ด ๋ง์ผ๋ฏ๋ก ๊ฐ์ ์ด ํ์ํด ๋ณด์ธ๋ค. enumerate๋ฅผ ์ฌ์ฉํ๋ฉด ์ฝ๊ฐ ๋์์ง์ง๋ง ์ถฉ๋ถํ์ง์๋ค.


### zip
์ด๋ฐ ์ฝ๋๋ฅผ ๋ ๊น๋ํ๊ฒ ๋ง๋ค ์ ์๋๋ก ํ์ด์ฌ์ zip ๋ด์ฅ ํจ์๋ฅผ ์ ๊ณตํ๋ค. zip ์ ๋๋ ์ดํฐ๋ ๋ ์ด์์ ์ดํฐ๋ ์ดํฐ์ ๋ค์ ๊ฐ์ด ๋ค์ด ์๋ ํํ์ ๋ฐํํ๋ค. ์ด ํํ์ for ๋ฌธ์์ ๋ฐ๋ก ์ธํจํนํ  ์ ์๋ค. 

```
for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

names.append('๋ฆฌ๋ฏผ์')
for name, count in zip(names, counts):
    print(name)

>>>
minxi
minseok
์ด๋ฏผ์
```

zip์ ์์ ์ด ๊ฐ์ผ ์ดํฐ๋ ์ดํฐ์ ๊ธธ์ด๊ฐ ๊ฐ์ ๊ฒฝ์ฐ ์ค๋จ๋๋ ์ํ ์์ด ์ฒ๋ฆฌํ๋ค. ํ์ง๋ง ์๋ ฅ ์ดํฐ๋ ์ดํฐ์ ๊ธธ์ด๊ฐ ์๋ก ๋ค๋ฅผ ๋๋ zip ๋์์ ์ฃผ์ํด์ผ ํ๋ค. ์๋ฅผ ๋ค์ด, names๋ฅผ ์ถ๊ฐํ๊ณ  count๋ฅผ ๊ฐฑ์ ํ์ง ๋ชปํ๋ค๋ฉด ์์ ๊ฐ์ด ๋์ํ๋ค.

zip์ ๊ฐ์ผ ์ดํฐ๋ ์ดํฐ ์ค ์ด๋ ํ๋๊ฐ ๋๋  ๋๊น์ง ํํ์ ์์ฑํ๋ค. ์ฆ, ์ถ๋ ฅ์ ๊ฐ์ฅ ์งง์ ์๋ ฅ์ ๊ธธ์ด์ ๊ฐ๋ค.

ํ์ง๋ง ๋ฆฌ์คํธ์ ๊ธธ์ด๊ฐ ๊ฐ์ง ์์ ๊ฒ์ ์์ํ๊ณ  ๋ท๋ถ๋ถ์ ์ถ๋ ฅํ๊ณ  ์ถ๋ค๋ฉด itertools ๋ด์ฅ ๋ชจ๋์ ๋ค์ด ์๋ zip_longest๋ฅผ ์ฌ์ฉํ  ์ ์๋ค.

```
import itertools

for name, count in itertools.zip_longest(name, count):
    print(f'{name}: {count}')

>>>
minxi: 5
minseok: 7
์ด๋ฏผ์: 3
๋ฆฌ๋ฏผ์: None
```

zip_longest๋ ์กด์ฌํ์ง ์๋ ๊ฐ์ ์์ ์๊ฒ ์ ๋ฌ๋ fillvalue๋ก ๋์ ํ๋ค. ๋ํดํธ fillvalue๋ None์ด๋ค.