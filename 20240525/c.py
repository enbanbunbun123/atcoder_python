def bingo_turn(N, T, A):
    #盤面の初期化
    board = [[(i * N + j + 1) for j in range(N)] for i in range(N)]

    #マークの初期化
    marks = [[False] * N for _ in range(N)]

    def check_bingo():
        #横列のチェック
        for row in marks:
            if all(row):
                return True
            
        #縦列のチェック
        for col in range(N):
            if all(marks[row][col] for row in range(N)):
                return True
            
        #斜めのチェック 
        if all(marks[i][i] for i in range(N)):
            return True
        if all(marks[i][N - 1 - i] for i in range(N)):
            return True 
        
        return False
    
    for turn in range(T):
        #数字A[turn]に対応するマスに印をつける
        num = A[turn]
        for i in range(N):
            for j in range(N):
                if board[i][j] == num:
                    marks[i][j] = True
                    
        if check_bingo():
            return turn + 1
        
    return -1

N, T = map(int, input().split())
A = list(map(int, input().split()))

result = bingo_turn(N, T, A)
print(result)