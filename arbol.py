# ============================================================
# ARBOL BINARIO
# 12 NODOS
# 4 NIVELES DE JERARQUIA
# PREORDEN, INORDEN Y POSTORDEN
# ============================================================

import matplotlib.pyplot as plt


# 1. CLASE NODO
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


# 2. CREAR LOS NODOS
nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)
nodo7 = Nodo(7)
nodo8 = Nodo(8)
nodo9 = Nodo(9)
nodo10 = Nodo(10)
nodo11 = Nodo(11)
nodo12 = Nodo(12)


# 3. CONSTRUIR EL ARBOL
nodo1.izquierdo = nodo2
nodo1.derecho = nodo3

nodo2.izquierdo = nodo4
nodo2.derecho = nodo5
nodo3.izquierdo = nodo6
nodo3.derecho = nodo7

nodo4.izquierdo = nodo8
nodo5.izquierdo = nodo9
nodo5.derecho = nodo10
nodo6.izquierdo = nodo11
nodo7.derecho = nodo12


# 4. RECORRIDOS
def preorden(nodo):
    if nodo is not None:
        print(nodo.valor, end=" ")
        preorden(nodo.izquierdo)
        preorden(nodo.derecho)


def inorden(nodo):
    if nodo is not None:
        inorden(nodo.izquierdo)
        print(nodo.valor, end=" ")
        inorden(nodo.derecho)


def postorden(nodo):
    if nodo is not None:
        postorden(nodo.izquierdo)
        postorden(nodo.derecho)
        print(nodo.valor, end=" ")


# 5. MOSTRAR LOS RECORRIDOS
print("==============================================")
print("             RECORRIDOS DEL ARBOL")
print("==============================================")

print("\nPREORDEN")
print("Raiz - Izquierda - Derecha")
preorden(nodo1)

print("\n\nINORDEN")
print("Izquierda - Raiz - Derecha")
inorden(nodo1)

print("\n\nPOSTORDEN")
print("Izquierda - Derecha - Raiz")
postorden(nodo1)

print("\n\n==============================================")
print("             FIN DEL PROGRAMA")
print("==============================================")


# 6. POSICIONES PARA DIBUJAR LOS NODOS
posiciones = {
    1: (0, 4),
    2: (-3, 3),
    3: (3, 3),
    4: (-4.5, 2),
    5: (-1.5, 2),
    6: (1.5, 2),
    7: (4.5, 2),
    8: (-5, 1),
    9: (-2.5, 1),
    10: (-0.5, 1),
    11: (1, 1),
    12: (5, 1),
}


def dibujar_conexiones(nodo):
    if nodo is None:
        return

    x, y = posiciones[nodo.valor]
    for hijo in (nodo.izquierdo, nodo.derecho):
        if hijo is not None:
            x_hijo, y_hijo = posiciones[hijo.valor]
            plt.plot([x, x_hijo], [y, y_hijo], color="black", zorder=1)
            dibujar_conexiones(hijo)


# 7. DIBUJAR EL ARBOL
plt.figure(figsize=(12, 8))
dibujar_conexiones(nodo1)

for valor, (x, y) in posiciones.items():
    plt.scatter(
        x,
        y,
        s=1800,
        color="lightblue",
        edgecolors="black",
        zorder=2,
    )
    plt.text(
        x,
        y,
        str(valor),
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        zorder=3,
    )

plt.title("ARBOL BINARIO - 12 NODOS - 4 NIVELES", fontsize=20)
plt.xlim(-6, 6)
plt.ylim(0, 5)
plt.axis("off")
plt.show()
