# ==============================================================================
# PARTE 2 CASO DE VIDA REAL
# BUSCAR CREDITO
# ==============================================================================
import matplotlib.pyplot as plt
import networkx as nx

# ==============================================================================
# PARTE 1: Definición de los 12 Nodos (Flujo Real de Crédito)
# ==============================================================================
G = nx.DiGraph()

# Nivel 0: Raíz (Nodo 1)
# Nivel 1: Preguntas intermedias (Nodos 2 y 3)
# Nivel 2: Preguntas y Hoja directa (Nodos 4, 5, 6 y 7)
# Nivel 3: Hojas / Decisiones finales (Nodos 8, 9, 10, 11 y 12)

nodos_info = {
    # Nivel 0
    1: ("1. ¿Ingresos > $3,000 USD?", "pregunta"),
    # Nivel 1
    2: ("2. ¿Buen historial crediticio?", "pregunta"),
    3: ("3. ¿Cuenta con codeudor?", "pregunta"),
    # Nivel 2
    4: ("4. ¿Antigüedad laboral > 2 años?", "pregunta"),
    5: ("5. ¿Capacidad de pago > 40%?", "pregunta"),
    6: ("6. ¿Codeudor posee propiedad?", "pregunta"),
    7: ("7. Rechazado (Sin respaldo)", "rechazado"),
    # Nivel 3 (Hojas finales)
    8: ("8. Aprobado (Monto Máximo)", "aprobado"),
    9: ("9. Aprobado (Monto Medio)", "aprobado"),
    10: ("10. Aprobado (Con Seguros)", "aprobado"),
    11: ("11. Rechazado (Sin capacidad)", "rechazado"),
    12: ("12. Aprobado con Codeudor", "aprobado"),
}

for nodo, (label, tipo) in nodos_info.items():
    G.add_node(nodo, label=label, tipo=tipo)


# ==============================================================================
# PARTE 2: Conexiones Lógicas (Sí = Izquierda / No = Derecha)
# ==============================================================================
conexiones = [
    # Del Nivel 0 al Nivel 1
    (1, 2, "Sí"),
    (1, 3, "No"),
    # Del Nivel 1 al Nivel 2
    (2, 4, "Sí"),
    (2, 5, "No"),
    (3, 6, "Sí"),
    (3, 7, "No"),
    # Del Nivel 2 al Nivel 3
    (4, 8, "Sí"),
    (4, 9, "No"),
    (5, 10, "Sí"),
    (5, 11, "No"),
    (6, 12, "Sí"),
]

for origen, destino, respuesta in conexiones:
    G.add_edge(origen, destino, label=respuesta)


# ==============================================================================
# PARTE 3: Coordenadas de los 4 Niveles (Nivel 0 al 3)
# ==============================================================================
pos = {
    # Nivel 0 (y = 3)
    1: (0, 3),
    # Nivel 1 (y = 2)
    2: (-4, 2),
    3: (4, 2),
    # Nivel 2 (y = 1)
    4: (-6, 1),
    5: (-2, 1),
    6: (2, 1),
    7: (6, 1),
    # Nivel 3 (y = 0)
    8: (-7, 0),
    9: (-5, 0),
    10: (-3, 0),
    11: (-1, 0),
    12: (2, 0),
}


# ==============================================================================
# PARTE 4: Dibujo y Renderizado Visual con Matplotlib
# ==============================================================================
fig, ax = plt.subplots(figsize=(16, 8))
ax.set_title(
    "Árbol Binario de Decisión - Evaluación de Crédito (12 Nodos / 4 Niveles)",
    fontsize=14,
    fontweight="bold",
    pad=20,
    color="#2c3e50",
)

# Colores según la categoría del nodo
colores = {
    "pregunta": "#3498db",  # Azul: Pregunta / Evaluación
    "aprobado": "#2ecc71",  # Verde: Crédito Aprobado
    "rechazado": "#e74c3c",  # Rojo: Crédito Rechazado
}

# 1. Flechas dirigidas
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=G.edges(),
    arrowstyle="->",
    arrowsize=20,
    edge_color="#7f8c8d",
    width=2,
    ax=ax,
)

# 2. Etiquetas en las flechas (Sí / No)
etiquetas_aristas = nx.get_edge_attributes(G, "label")
nx.draw_networkx_edge_labels(
    G,
    pos,
    edge_labels=etiquetas_aristas,
    font_size=10,
    font_color="#1a252f",
    font_weight="bold",
    bbox=dict(
        boxstyle="round,pad=0.2", facecolor="white", edgecolor="#cbd5e1", lw=1
    ),
    ax=ax,
)

# 3. Dibujar nodos numerados del 1 al 12
for nodo, (x, y) in pos.items():
    texto_label = G.nodes[nodo]["label"]
    tipo_nodo = G.nodes[nodo]["tipo"]
    color_fondo = colores[tipo_nodo]

    ax.text(
        x,
        y,
        texto_label,
        ha="center",
        va="center",
        fontsize=8.5,
        fontweight="bold",
        color="white",
        bbox=dict(
            boxstyle="round,pad=0.6",
            facecolor=color_fondo,
            edgecolor="#2c3e50",
            linewidth=1.5,
        ),
    )

plt.axis("off")
plt.tight_layout()
plt.show()