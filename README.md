# 🌳 Parcial Final - Estructuras de Datos

## Árboles (Grafos Especiales)

**Universidad:** Uniremington
**Asignatura:** Estructuras de Datos
**Tema:** Árboles
**Estudiantes:** Kevin Ramirez, jonathan ballesteros, eustorgio chirimia

---

# 📚 1. Introducción

En este proyecto se analiza y representa un árbol correspondiente a una estructura jerárquica de cuatro niveles.

El objetivo es identificar los componentes principales de un árbol, representar su estructura mediante código y realizar los recorridos fundamentales:

* Preorden.
* Inorden.
* Postorden.

También se presenta una aplicación de los árboles en un contexto real y se responden preguntas relacionadas con los grafos acíclicos y los árboles.

---

# 🌳 2. Árbol asignado

El árbol proporcionado en el parcial tiene la siguiente estructura:

```text
                    1
                  /   \
                 2     3
                / \   / \
               4   5 6   7
              /   / \ |   |
             8   9  10 11  12
```

El árbol contiene 12 nodos distribuidos en cuatro niveles.

---

# 🔎 3. Identificación de los componentes del árbol

## 3.1. Raíz

La raíz es el nodo **1**, porque es el nodo principal desde el cual comienza la estructura del árbol.

## 3.2. Nodos

Los nodos son los elementos que conforman el árbol. En este caso, están identificados con los números del 1 al 12.

## 3.3. Aristas o conexiones

Las aristas son las líneas que conectan dos nodos. Representan las relaciones entre un nodo padre y sus hijos.

Las conexiones del árbol son:

* Nodo 1 → Nodo 2.
* Nodo 1 → Nodo 3.
* Nodo 2 → Nodo 4.
* Nodo 2 → Nodo 5.
* Nodo 3 → Nodo 6.
* Nodo 3 → Nodo 7.
* Nodo 4 → Nodo 8.
* Nodo 5 → Nodo 9.
* Nodo 5 → Nodo 10.
* Nodo 6 → Nodo 11.
* Nodo 7 → Nodo 12.

**Total: 12 nodos y 11 conexiones.**

## 3.4. Padres e hijos

| Nodo padre | Nodos hijos |
| ---------- | ----------- |
| 1          | 2 y 3       |
| 2          | 4 y 5       |
| 3          | 6 y 7       |
| 4          | 8           |
| 5          | 9 y 10      |
| 6          | 11          |
| 7          | 12          |

## 3.5. Hojas

Las hojas son los nodos que no tienen hijos.

En este árbol, las hojas son:

**8, 9, 10, 11 y 12.**

## 3.6. Niveles del árbol

| Nivel   | Nodos             |
| ------- | ----------------- |
| Nivel 1 | 1                 |
| Nivel 2 | 2 y 3             |
| Nivel 3 | 4, 5, 6 y 7       |
| Nivel 4 | 8, 9, 10, 11 y 12 |

## 3.7. Altura del árbol

El árbol tiene cuatro niveles. Su altura es de tres aristas, contando el camino más largo desde la raíz hasta una hoja.

---

## 🎯 4. Parte 2: Aplicación a un caso de la vida real — Evaluación de crédito

### 4.1. Descripción del problema

En una entidad financiera, es necesario evaluar las solicitudes de crédito de los clientes para determinar si cumplen con los requisitos establecidos para recibir un préstamo.

Para solucionar este problema, se utiliza un **árbol binario de decisión**, que representa las preguntas y las posibles respuestas durante el proceso de evaluación.

El árbol está compuesto por **12 nodos distribuidos en 4 niveles**. Cada conexión representa una decisión lógica, donde:

* **Sí:** indica que se cumple la condición evaluada.
* **No:** indica que no se cumple la condición evaluada.
* **Aprobado:** representa un resultado favorable para el solicitante.
* **Rechazado:** representa un resultado desfavorable según las condiciones del ejemplo.

El programa utiliza Python, `NetworkX` para construir el grafo y `Matplotlib` para dibujar la estructura de forma visual.

### 4.2. Identificación de los 12 nodos

Cada nodo representa una pregunta, una evaluación o una decisión final dentro del proceso de aprobación del crédito.

| Nodo | Descripción                              | Tipo             |
| ---: | ---------------------------------------- | ---------------- |
|    1 | ¿Ingresos mayores a $3.000 USD?          | Pregunta inicial |
|    2 | ¿Buen historial crediticio?              | Pregunta         |
|    3 | ¿Cuenta con codeudor?                    | Pregunta         |
|    4 | ¿Antigüedad laboral mayor a 2 años?      | Pregunta         |
|    5 | ¿Capacidad de pago mayor al 40 %?        | Pregunta         |
|    6 | ¿El codeudor posee una propiedad?        | Pregunta         |
|    7 | Rechazado por falta de respaldo          | Decisión final   |
|    8 | Aprobado por monto máximo                | Decisión final   |
|    9 | Aprobado por monto medio                 | Decisión final   |
|   10 | Aprobado con seguros                     | Decisión final   |
|   11 | Rechazado por falta de capacidad de pago | Decisión final   |
|   12 | Aprobado con codeudor                    | Decisión final   |

### 4.3. Funcionamiento del árbol de decisión

La evaluación comienza en el nodo 1 y continúa por las conexiones según las respuestas a las preguntas.

**Nivel 0 — Pregunta inicial**

* Nodo 1: ¿Los ingresos son mayores a $3.000 USD?
* Si la respuesta es **Sí**, se continúa al nodo 2.
* Si la respuesta es **No**, se continúa al nodo 3.

**Nivel 1 — Evaluación del historial crediticio o del codeudor**

* Nodo 2: ¿Tiene buen historial crediticio?

  * Sí: pasa al nodo 4.
  * No: pasa al nodo 5.
* Nodo 3: ¿Cuenta con codeudor?

  * Sí: pasa al nodo 6.
  * No: pasa al nodo 7, donde se rechaza la solicitud por falta de respaldo.

**Nivel 2 — Evaluaciones adicionales**

* Nodo 4: ¿Tiene más de 2 años de antigüedad laboral?

  * Sí: pasa al nodo 8, aprobado por monto máximo.
  * No: pasa al nodo 9, aprobado por monto medio.
* Nodo 5: ¿Su capacidad de pago es mayor al 40 %?

  * Sí: pasa al nodo 10, aprobado con seguros.
  * No: pasa al nodo 11, rechazado por falta de capacidad de pago.
* Nodo 6: ¿El codeudor posee una propiedad?

  * Sí: pasa al nodo 12, aprobado con codeudor.

**Nivel 3 — Decisiones finales**

En este nivel se encuentran los resultados de las evaluaciones: aprobación del crédito bajo distintas condiciones o rechazo de la solicitud.

### 4.4. Conexiones entre los nodos

Las conexiones del árbol están definidas en el código mediante una lista de tuplas. Cada tupla contiene el nodo de origen, el nodo de destino y la respuesta que representa la conexión.

| Origen | Destino | Respuesta |
| -----: | ------: | --------- |
|      1 |       2 | Sí        |
|      1 |       3 | No        |
|      2 |       4 | Sí        |
|      2 |       5 | No        |
|      3 |       6 | Sí        |
|      3 |       7 | No        |
|      4 |       8 | Sí        |
|      4 |       9 | No        |
|      5 |      10 | Sí        |
|      5 |      11 | No        |
|      6 |      12 | Sí        |

El árbol tiene **12 nodos y 11 conexiones dirigidas**. Como se trata de un árbol binario de decisión, cada nodo de pregunta puede tener como máximo dos hijos. En este caso, el nodo 6 solo tiene una conexión definida: la respuesta «Sí» conduce al nodo 12.

### 4.5. Representación gráfica con Python

El código utiliza las siguientes bibliotecas:

* **NetworkX:** permite crear el grafo dirigido, registrar los nodos y definir las conexiones.
* **Matplotlib:** permite dibujar el árbol y mostrarlo en pantalla.
* **Colores:** facilitan la interpretación de los resultados.

La representación gráfica utiliza tres colores:

* **Azul:** preguntas y evaluaciones.
* **Verde:** decisiones de crédito aprobado.
* **Rojo:** decisiones de crédito rechazado.

Las flechas indican la dirección del proceso de evaluación, y sus etiquetas muestran las respuestas «Sí» o «No».

Para ejecutar el programa, guarda el código en el archivo `p2_credito.py` y utiliza el siguiente comando en la terminal:

```bash
python p2_credito.py
```

Si todavía no tienes instaladas las bibliotecas necesarias, ejecuta:

```bash
python -m pip install matplotlib networkx
```

### 4.6. Importancia de utilizar árboles de decisión

Los árboles de decisión permiten organizar un proceso complejo en preguntas y respuestas fáciles de seguir. En el caso de una entidad financiera, ayudan a representar visualmente las condiciones que se evalúan antes de tomar una decisión sobre una solicitud de crédito.

Entre sus principales ventajas se encuentran:

1. **Organización:** divide el proceso en etapas claramente identificadas.
2. **Comprensión:** permite visualizar las decisiones y sus posibles resultados.
3. **Seguimiento:** facilita identificar el camino recorrido durante una evaluación.
4. **Mantenimiento:** permite modificar preguntas o condiciones cuando cambian las políticas de evaluación.
5. **Aplicación práctica:** puede servir como modelo inicial para desarrollar un sistema informático de evaluación de solicitudes.

**Nota:** este programa es una simulación académica. Los requisitos y resultados son ilustrativos y no constituyen una política financiera real. Antes de utilizar un sistema de este tipo en producción, deben definirse y validarse las reglas de negocio y las conexiones que falten.

## 🧠 5. Conclusión

El desarrollo de este ejercicio permite comprender cómo se aplican los árboles binarios a un problema de la vida real. En este caso, los nodos representan las preguntas y decisiones necesarias para evaluar una solicitud de crédito, mientras que las conexiones representan las respuestas que determinan el siguiente paso.

La implementación con Python, NetworkX y Matplotlib permite construir y visualizar el proceso, relacionando los conceptos teóricos de estructuras de datos con una situación práctica del ámbito financiero.

# Recorrido adecuado para el árbol de decisión de crédito

## Recorrido elegido: preorden

El recorrido **preorden** es el más adecuado para representar la evaluación de una solicitud de crédito. En este recorrido se procesa primero el nodo actual y luego sus hijos. Aplicado al árbol, significa comenzar por la pregunta inicial y continuar según las respuestas hasta llegar a una decisión final.

## Justificación

### Orden de procesamiento

La evaluación comienza en el nodo 1: «¿Los ingresos son mayores a $3.000 USD?». Después de responder, se continúa por la rama correspondiente:

- Si la respuesta es **Sí**, se evalúa el nodo 2.
- Si la respuesta es **No**, se evalúa el nodo 3.

El mismo procedimiento se repite en cada pregunta hasta alcanzar un nodo de aprobación o rechazo. El preorden representa este procesamiento secuencial: primero se considera la pregunta actual y, a continuación, se avanza al siguiente nodo del recorrido.

### Necesidad del problema

El objetivo es evaluar cada solicitud de forma progresiva para tomar una decisión de crédito. No es necesario revisar todas las preguntas del árbol: la respuesta a una pregunta determina qué condición debe evaluarse después.

El preorden refleja esta necesidad porque permite iniciar en la raíz del árbol y seguir el camino que corresponde a las respuestas del solicitante, hasta obtener el resultado aplicable.

### Flujo de información

La información fluye desde la pregunta inicial hacia las preguntas posteriores y, finalmente, hacia una decisión. Cada respuesta determina el siguiente paso:

1. Se formula una pregunta.
2. Se recibe una respuesta afirmativa o negativa.
3. Se sigue la conexión correspondiente.
4. Se continúa hasta llegar a una decisión final.

Por ejemplo, si los ingresos superan los $3.000 USD, hay buen historial crediticio y la antigüedad laboral es mayor a dos años, el recorrido sería:

**Nodo 1 → Nodo 2 → Nodo 4 → Nodo 8**

El resultado sería «Aprobado por monto máximo». Este camino muestra cómo la información guía la evaluación desde la raíz hasta una hoja del árbol.

## Comparación con otros recorridos

- **Inorden:** procesa primero el subárbol izquierdo, luego el nodo y después el subárbol derecho. Este orden no representa de manera natural la evaluación, porque las preguntas posteriores dependen de las respuestas a las preguntas anteriores.
- **Postorden:** procesa primero los descendientes y después el nodo actual. No resulta apropiado para este caso, ya que se debe conocer la respuesta a una pregunta antes de decidir qué condición evaluar a continuación.
- **Preorden:** procesa primero el nodo actual y luego avanza por la rama correspondiente. Por ello, se ajusta al flujo de evaluación de una solicitud.
