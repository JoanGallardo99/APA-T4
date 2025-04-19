"""
Nombre: Joan Gallardo Caparrós

Implementa un genereador de números pseudoaleatorios usando el algoritmo lineal congruente (LGC), tanto como clase iterable como generador"

Pruebas para la clase Aleat:
>>> rand = Aleat(m=32, a=9, c=13, x0=11)
>>> for _ in range(4):
...     print(next(rand))
...
16
29
18
15

>>> rand(29)
>>> for _ in range(4):
...     print(next(rand))
...
18
15
20
1

Pruebas para la función generadora aleat():
>>> rand = aleat(m=64, a=5, c=46, x0=36)
>>> for _ in range(4):
...     print(next(rand))
...
34
24
38
44

>>> rand.send(24)
38
>>> for _ in range(4):
...     print(next(rand))
...
44
10
32
14
"""

class Aleat:
    """
    Generador de números pseudoaleatorios mediante el algoritmo LGC
    """

    def __init__(self, m = 2**48, a=25214903917, c = 11, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.seed = x0
        self.state = x0

    def __iter__(self):
        return self
    
    def __next__(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state
    
    def __call__(self, x0):
        """
        Cambia el estado inicial del generador
        """
        self.seed = x0
        self.state = x0
        return self.state
    
def aleat(m = 2**48, a=25214903917, c = 11, x0 = 1212121):
    """
    Función generadora de números pseudoaleatorios mediante el algoritmo LGC.
    Puede reiniciarse usando send() con una nueva semilla.
    """

    state = x0
    while True:
        nuevo = (yield state)
        if nuevo is not None:
            state = nuevo
        state = (a * state + c) % m