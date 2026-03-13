"""
八皇后求解器 solve(n) 的单元测试。

覆盖：n=1/4/8 的解个数、解的合法性，以及 n<=0、n=2/n=3 无解等边界。
"""
import pytest
from src.queens import solve


def _is_valid_solution(solution: list[int], n: int) -> bool:
    """
    检查一个解是否合法：任意两皇后不共列、不共对角线。
    解的形式为 [c0, c1, ...]，解[i] 为第 i 行皇后的列下标。
    """
    if len(solution) != n:
        return False 
    for i in range(n):
        if not (0 <= solution[i] < n):
            return False
        for j in range(i + 1, n):
            if solution[i] == solution[j]:
                return False  # 同列
            if j - i == solution[j] - solution[i]:
                return False  # 同一主对角线
            if j - i == solution[i] - solution[j]:
                return False  # 同一副对角线
    return True


# ---------- 解个数 ----------


def test_solve_n1_one_solution():
    """n=1 时有 1 个解。"""
    got = solve(1)
    assert len(got) == 1
    assert got[0] == [0]


def test_solve_n4_two_solutions():
    """n=4 时有 2 个解。"""
    got = solve(4)
    assert len(got) == 2


def test_solve_n8_ninety_two_solutions():
    """n=8 时有 92 个解。"""
    got = solve(8)
    assert len(got) == 92


def test_solve_n2_no_solution():
    """n=2 时无解。"""
    assert solve(2) == []


def test_solve_n3_no_solution():
    """n=3 时无解。"""
    assert solve(3) == []


def test_solve_zero_empty():
    """n=0 时返回空列表。"""
    assert solve(0) == []


def test_solve_negative_empty():
    """n<0 时返回空列表。"""
    assert solve(-1) == []


# ---------- 解的合法性 ----------


def test_solve_n4_all_solutions_valid():
    """n=4 的每个解都合法。"""
    solutions = solve(4)
    for sol in solutions:
        assert _is_valid_solution(sol, 4), f"invalid solution: {sol}"


def test_solve_n8_all_solutions_valid():
    """n=8 的每个解都合法。"""
    solutions = solve(8)
    for sol in solutions:
        assert _is_valid_solution(sol, 8), f"invalid solution: {sol}"


def test_solve_n1_solution_valid():
    """n=1 的唯一定义解合法。"""
    solutions = solve(1)
    assert len(solutions) == 1
    assert _is_valid_solution(solutions[0], 1)


# ---------- 解的形式 ----------


def test_solve_each_solution_length_n():
    """每个解的长度等于 n。"""
    for n in [1, 4, 8]:
        for sol in solve(n):
            assert len(sol) == n
            assert all(0 <= c < n for c in sol)
