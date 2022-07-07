# L09E02: Password generator
Vytvořte modul `passwords` obsahující funkci `password_generator(length)`. Funkce přijímá jediný argument a tím je délka hesla. Funkce vrací iterátor generující všechny možné hesela složená z písmen (pouze malá) a čísel (0-9).

K získání kolekce všech písmen a čísel použijte modul `string`.

```python
import string

string.ascii_lowercase
# 'abcdefghijklmnopqrstuvwxyz'

string.digits
# '0123456789'
```

Příklad použití:

```python
from passwords import password_generator

assert len(list(password_generator(4))) == 1679616
assert len(list(password_generator(5))) == 60466176
```

V řešení použíjte pouze modul `itertools` a `string`. Nepoužívejte cykly, seznamy ani jiné datové struktury.

