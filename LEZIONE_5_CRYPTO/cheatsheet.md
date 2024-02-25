# Cheatsheet per crypto


## Calcolare inverso modulare

### Utilizzando gmpy2
```py
from gmpy2 import invert
mod = 1337
num = 2
print(invert(num, mod)) # Output: mpz(669)
```

### Utilizzando python (>= 3.8)
```py
mod = 1337
num = 2
print(pow(num, -1, mod)) # Output: 669
```


## Calcolare gcd (+ extended gcd)

### Utilizzando funzioni builtin
```py
from math import gcd
mod = 1337
num = 2
print(gcd(num, mod)) # Output: 1
```

### Extended gcd
```py
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

mod = 1337
num = 2
print(extended_gcd(num, mod)) # Output: (1, -668, 1)

```

## Robe che si trovano spesso

### Dati a, b, n trovare x in a = b*x (mod n)

```py
from gmpy2 import invert
x = (invert(b, n)*a) % n

# Esempio:

b = 1024
x = 1337 # Bisogna trovare questo 
n = 2047
a = (x*b) % n
_x = (invert(b, n)*a) % n

assert _x == x # ok
```

### Radice n-esima modulo n

```py
# Su sagemath oppure su https://sagecell.sagemath.org/
mod = 2**32 - 1
K = Integers(mod)
num = 16
K(num).nth_root(3) # Output: 4096
```

### Risolvere equazione
```py
# Su sagemath oppure su https://sagecell.sagemath.org/

x = var("x")
equazione = x^2 + 2*x + 1 == 0
solve(equazione, x) # Output: [x == -1]
```

### Risolvere sistema di equazioni

```py
x,y = var("x,y")
eq1 = x^2 + y == 1024
eq2 = y - 1 == 24
solve([eq1,eq2], [x,y])
```

### Risolvere equazione/sistema di equazioni modulo n

```py
x,y = var("x,y")
eq1 = x^2 + y == 1024
eq2 = y - 1 == 24
mod = 2^16 - 1
solve_mod([eq1,eq2], mod)
```
