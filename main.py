
# Return/Exchange Cycle Detector using Graph Cycle Detection (DFS)

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def is_cyclic_util(self, node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True

        for neighbour in self.graph.get(node, []):
            if not visited.get(neighbour, False):
                if self.is_cyclic_util(neighbour, visited, rec_stack):
                    return True
            elif rec_stack.get(neighbour, False):
                return True

        rec_stack[node] = False
        return False

    def is_cyclic(self):
        visited = {}
        rec_stack = {}

        for node in self.graph:
            if not visited.get(node, False):
                if self.is_cyclic_util(node, visited, rec_stack):
                    return True
        return False


def main():
    g = Graph()

    print("Enter number of transactions (return/exchange records):")
    n = int(input())

    print("Enter each transaction in the format 'ProductA ProductB' (ProductA returned for ProductB):")
    for _ in range(n):
        u, v = input().split()
        g.add_edge(u, v)

    if g.is_cyclic():
        print("Cycle detected! Potential fraud in return/exchange patterns.")
    else:
        print("No cycles detected. Return/exchange patterns look safe.")

if __name__ == "__main__":
    main()
