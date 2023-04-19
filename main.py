class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # додавання ребра до графа
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # пошук представника множини
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # злиття двох множин
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # алгоритм Крускала
    def kruskal(self):
        result = []
        i = 0
        e = 0

        # сортування ребер за зростанням ваги
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # ініціалізація батьківського списку та списку рангів
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # перевірка, чи ребро не створює цикл
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        return result


# зчитування графа з файлу
filename = "graph.txt"
with open(filename) as f:
    content = f.readlines()
content = [x.strip() for x in content]

# конвертування рядка у список цілих чисел
graph = []
for line in content:
    graph.append(list(map(int, line.split())))

# створення графа та додавання ребер
g = Graph(len(graph))
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] != 0:
            g.add_edge(i, j, graph[i][j])

# запуск алгоритму Крускала та вивід результату
result = g.kruskal()
print("Мінімальне остовне дерево за алгоритмом Крускала: ")
for u, v, weight in result:
    print("%d - %d: %d" % (u, v, weight))

