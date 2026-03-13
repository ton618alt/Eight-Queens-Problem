"""
八皇后问题求解器（回溯法）。

函数 solve(n) 接收棋盘大小 n，返回所有解的列表，
每个解是长度为 n 的列表，表示每一行皇后所在的列索引（0 到 n-1）。
"""
from typing import List


def solve(n: int) -> List[List[int]]:
    """
    使用回溯法求解 n 皇后问题的所有解。

    Args:
        n: 棋盘大小（n×n），也是皇后数量。

    Returns:
        所有解的列表。每个解是一个长度为 n 的列表，
        解[i] 表示第 i 行皇后所在的列索引（0 到 n-1）。
    """
    if n <0:
        return []

    result: List[List[int]] = []
    # 当前尝试的解：board[i] 表示第 i 行皇后所在的列
    board: List[int] = []

    def is_safe(row: int, col: int) -> bool:
        """检查在 (row, col) 放皇后是否与已有皇后冲突。"""
        for r in range(row):
            c = board[r]
            # 同列
            if c == col:
                return False
            # 同一主对角线：行差 == 列差
            if row - r == col - c:
                return False
            # 同一副对角线：行差 == -列差
            if row - r == c  -  col:
                return False
        return True

    def backtrack(row: int) -> None:
        if row == n:
            result.append(board[:])
            return
        for col in range(n):
            if is_safe(row, col):
                board.append(col)
                backtrack(row + 1)
                board.pop()

    backtrack(0)
    return result
