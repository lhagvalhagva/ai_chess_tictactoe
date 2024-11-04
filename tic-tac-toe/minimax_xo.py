import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.human = -1  # O
        self.ai = 1      # X
        
    def available_moves(self):
        # Хоосон байрлалуудыг олох
        moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    moves.append((i, j))
        return moves
    
    def make_move(self, position, player):
        # Хөдөлгөөн хийх
        if self.board[position[0]][position[1]] == 0:
            self.board[position[0]][position[1]] = player
            return True
        return False
    
    def check_winner(self):
        # Хөндлөн шалгах
        for i in range(3):
            if abs(sum(self.board[i])) == 3:
                return self.board[i][0]
                
        # Босоо шалгах
        for i in range(3):
            if abs(sum(self.board[:, i])) == 3:
                return self.board[0][i]
                
        # Диагональ шалгах
        if abs(sum(np.diag(self.board))) == 3:
            return self.board[0][0]
        if abs(sum(np.diag(np.fliplr(self.board)))) == 3:
            return self.board[0][2]
            
        # Тэнцсэн эсвэл үргэлжилж байгаа
        if len(self.available_moves()) == 0:
            return 0  # Тэнцсэн
        return None  # Тоглоом үргэлжилж байна
    
    def minimax(self, depth, is_maximizing):
        result = self.check_winner()
        
        # Base cases
        if result is not None:
            return result
            
        if is_maximizing:
            best_score = float('-inf')
            for move in self.available_moves():
                self.board[move[0]][move[1]] = self.ai
                score = self.minimax(depth + 1, False)
                self.board[move[0]][move[1]] = 0
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.available_moves():
                self.board[move[0]][move[1]] = self.human
                score = self.minimax(depth + 1, True)
                self.board[move[0]][move[1]] = 0
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self):
        best_score = float('-inf')
        best_move = None
        
        for move in self.available_moves():
            self.board[move[0]][move[1]] = self.ai
            score = self.minimax(0, False)
            self.board[move[0]][move[1]] = 0
            
            if score > best_score:
                best_score = score
                best_move = move
                
        return best_move
    
    def print_board(self):
        symbols = {1: 'X', -1: 'O', 0: ' '}
        print("\nОдоогийн самбар:")
        for i in range(3):
            print('-------------')
            row = '|'
            for j in range(3):
                row += f' {symbols[self.board[i][j]]} |'
            print(row)
        print('-------------')

def play_game():
    game = TicTacToe()
    
    print("Байрлалын дугаарлалт:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    
    # Хэн эхлэхийг сонгох
    while True:
        try:
            choice = input("\nХэн эхлэх вэ? (1: Та, 2: AI): ")
            if choice in ['1', '2']:
                ai_starts = (choice == '2')
                break
            print("1 эсвэл 2 сонголтоос сонгоно уу!")
        except ValueError:
            print("1 эсвэл 2 сонголтоос сонгоно уу!")
    
    while True:
        game.print_board()
        
        # AI эхэлж байгаа бол
        if ai_starts:
            # AI ээлж
            ai_move = game.get_best_move()
            game.make_move(ai_move, game.ai)
            
            # Ялагч шалгах
            winner = game.check_winner()
            if winner is not None:
                game.print_board()
                if winner == 0:
                    print("Тэнцлээ!")
                elif winner == game.ai:
                    print("AI яллаа!")
                break
            
            game.print_board()
        
        ai_starts = False  # Дараагийн ээлжүүдэд хэвийн дарааллаар явна
        
        # Хүний ээлж
        available = game.available_moves()
        while True:
            try:
                move = int(input("Таны ээлж (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("1-9 хооронд тоо оруулна уу!")
                    continue
                row, col = move // 3, move % 3
                if (row, col) in available:
                    game.make_move((row, col), game.human)
                    break
                else:
                    print("Буруу байрлал! Дахин оролдоно уу.")
            except ValueError:
                print("1-9 хооронд тоо оруулна уу!")
        
        # Ялагч шалгах
        winner = game.check_winner()
        if winner is not None:
            game.print_board()
            if winner == 0:
                print("Тэнцлээ!")
            elif winner == game.human:
                print("Та яллаа!")
            break
            
        # AI ээлж
        ai_move = game.get_best_move()
        game.make_move(ai_move, game.ai)
        
        # Ялагч шалгах
        winner = game.check_winner()
        if winner is not None:
            game.print_board()
            if winner == 0:
                print("Тэнцлээ!")
            elif winner == game.ai:
                print("AI яллаа!")
            break

if __name__ == "__main__":
    while True:
        play_game()
        if input("\nДахин тоглох уу? (y/n): ").lower() != 'y':
            break