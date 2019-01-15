## queen problem with recurison 八皇后问题（循环递归法）
BOARD_SIZE = 8

def under_attack(col，queens)：
    left = right = col
    for r,c in reversed(queens): #左右有冲突的位置的列号
        left,right = left -1, right + 1
        if c in (left ,col, right):
            return True
        return False
def solve(n):
    if n == 0:
        return [[]]
    smaller_solution = solve(n -1)
    return [solution+[n,i+1]]
    