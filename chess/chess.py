from collections import deque

class Node:
    def __init__(self, state, parent=None):
        self.state = state  # Хатан хаадын байрлал
        self.parent = parent  # Эцэг зангилаа
        self.children = []    # Дэд зангилаанууд

    def add_child(self, child):
        self.children.append(child)

class NQueensProblem:
    def __init__(self, n=8):
        self.n = n  # Хөлгийн хэмжээ (8x8)
        self.solutions = []  # Олдсон бүх шийдүүд

    def is_safe(self, state, row, col):
        # Хатан хаан аюулгүй байрлаж байгаа эсэхийг шалгах
        for i in range(len(state)):
            if state[i] == col or \
               abs(state[i] - col) == abs(i - row):
                return False
        return True

    def breadth_first_search(self):
        queue = deque([(Node([]), 0)])  # deque ашиглан BFS хийх
        
        while queue:
            node, row = queue.popleft()
            
            if row == self.n:  # Бүх мөрөнд хатан тавигдсан бол
                self.solutions.append(node.state)
                continue
                
            for col in range(self.n):
                if self.is_safe(node.state, row, col):
                    new_state = node.state.copy()
                    new_state.append(col)
                    child = Node(new_state, node)
                    node.add_child(child)
                    queue.append((child, row + 1))

    def print_solution(self, solution):
        # Шийдийг хэвлэх
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if solution[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()

# Жишээ ашиглалт
if __name__ == "__main__":
    queens = NQueensProblem(8)
    
    # BFS ашиглан бодох
    queens.breadth_first_search()
    print(f"BFS олсон шийдийн тоо: {len(queens.solutions)}")
    print("BFS-ээр олсон бүх шийдүүд:")
    for i, solution in enumerate(queens.solutions, 1):
        print(f"\nШийд #{i}:")
        queens.print_solution(solution)
