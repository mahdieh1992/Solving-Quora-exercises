#بمب‌بازی
n , m = map(int, input().split())
def check_pos(x,y,board):
    position__increase = [[x - 1, y], [x + 1, y], [x, y + 1],[x - 1, y + 1],
                          [x , y - 1], [x - 1 , y - 1], [x + 1, y + 1] ,
                          [x + 1 , y - 1]]
    for pos in position__increase:
        if pos[0] == -1 or pos[0] >= n or pos[1] >= m or pos[1] == -1:
            continue
        else:
            i = pos[0]
            j = pos[1]
            if board[i][j] != "*":
               board[i][j] += 1
    return board

board = [[0 for j in range(m)] for i in range(n)]
k = int(input())
for i in range(k):
    x,y = map(int,input().split())
    x, y = x - 1 , y - 1
    board[x][y] = '*'
    result = check_pos(x,y,board)
for r in result:
    print(*r)
    
