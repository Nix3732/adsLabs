import networkx as nx
import matplotlib.pyplot as plt


def graph_coloring(network, colors_count):
    nodes = sorted(network.keys(), key=lambda n: -len(network[n]))      # сортировка по убыванию степени
    coloring = {}

    def backtrack(current_pos):             # перебираем все цвета для вершины
        if current_pos == len(nodes):
            return coloring.copy()

        current_node = nodes[current_pos]
        for color in range(1, colors_count + 1):
            if all(coloring.get(neighbor) != color for neighbor in network[current_node]):  # проверяем что цвета разные
                coloring[current_node] = color
                result = backtrack(current_pos + 1)         # рекурсивно переходим к следующей вершине
                if result is not None:
                    return result
                coloring.pop(current_node)
        return None

    return backtrack(0)


def find_min_colors(network):           # вычисляем минимальное количество нужных цветов
    max_degree = max(len(edges) for edges in network.values())
    for k in range(1, max_degree + 2):      # раскрашиваем граф
        coloring = graph_coloring(network, k)
        if coloring is not None:
            return k, coloring
    return len(network), {node: i + 1 for i, node in enumerate(network)}


def visualize_graph(network, coloring, title):
    G = nx.Graph()

    for node, edges in network.items():
        G.add_node(node)
        for edge in edges:
            if edge > node:
                G.add_edge(node, edge)

    color_palette = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8',
                     '#F06292', '#7986CB', '#9575CD', '#64B5F6', '#4DB6AC']

    node_colors = [color_palette[coloring[node] - 1] for node in G.nodes()]

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G, seed=42)

    nx.draw_networkx_nodes(G, pos, node_size=800, node_color=node_colors, edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.5)
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')

    unique_colors = sorted(set(coloring.values()))
    legend_elements = [plt.Line2D([0], [0], marker='o', color='w',
                                  markerfacecolor=color_palette[color - 1],
                                  markersize=10,
                                  label=f'Цвет {color}')
                       for color in unique_colors]

    plt.legend(handles=legend_elements, loc='upper right')
    plt.title(title, fontsize=14)
    plt.axis('off')
    plt.tight_layout()
    plt.show()


graphs = [
    {
        "name": "Циклический граф (4 вершины)",
        "graph": {
            0: [1, 3],
            1: [0, 2],
            2: [1, 3],
            3: [0, 2]
        }
    },
    {
        "name": "Почти полный граф",
        "graph": {
            0: [1, 2],
            1: [0, 2, 3],
            2: [0, 1, 3],
            3: [1, 2]
        }
    },
    {
        "name": "Сложный граф (8 вершин)",
        "graph": {
            0: [1, 4, 5],
            1: [0, 2, 3, 7],
            2: [1, 3, 7],
            3: [1, 2, 4, 6],
            4: [0, 3, 5, 6],
            5: [0, 4, 6],
            6: [3, 4, 5, 7],
            7: [1, 2, 6]
        }
    }
]

for graph_data in graphs:
    min_colors, coloring = find_min_colors(graph_data['graph'])
    print(f"Минимальное количество цветов: {min_colors}")
    print("Раскраска вершин:", coloring)

    # Визуализация
    visualize_graph(
        graph_data['graph'],
        coloring,
        f"Минимальная раскраска: {min_colors} цветов")
