# HW01 基于 AI 协作的八皇后工程实践交互日志（prompt_log.md）

> 课程：《人工智能导论/人工智能通识课》  
> 作业：HW01 基于AI协作的八皇后问题工程化实践  
> 工具：Cursor AI（内置助手）
本日志用于记录在完成 hw01 作业过程中，与 AI 编程工具的**典型交互**与**关键决策**，包括需求澄清、工程初始化、算法实现、单元测试设计以及后续 Bug 调试与重构等，便于老师从工程化过程而非最终代码来进行评价。
---
## 1. 交互会话索引（Cursor 会话）

本项目主要依托 Cursor 进行 AI 协作，较完整的两次会话如下：

- **会话 A：项目初始化与开发规划**  
  对应记录：\[HW01 初始化与开发](02353d00-33ee-4867-bf18-713a1f13e368)  
  主要内容：在 Cursor 中打开 `hw01` 仓库后，请求 AI 拆解作业要求，规划初始化标准 Python 工程（含 `src/` 与 `tests/`）、设计八皇后求解器接口以及单元测试策略。

- **会话 B：进度检查与作业对照**  
  对应记录：\[HW01 进度与总结](df876452-5a99-42e4-9da0-6600066c1309)  
  主要内容：在实现求解器与测试后，请求 AI 对当前仓库进行检查，确认与作业 4 项核心任务和提交要求的符合程度，并根据评分标准给出后续需要补齐的部分（尤其是交互日志与 Bug 实验）。

---

## 2. 需求澄清与作业理解（节选）

### 2.1 用户给 AI 的作业描述（节选自会话 B）

> 这是《人工智能导论》面向人工智能本硕的课程作业，主题为基于AI协作的八皇后问题工程化实践，提交截止2026年3月12日12:00，核心考察AI编程工具的运用与工程项目构建能力，而非算法背诵，具体内容如下：  
> 1. 核心任务：在GitHub的hw01目录下，借助Claude Code、Cursor等AI工具完成4项工作，包括初始化含src/和tests/的标准Python工程、实现八皇后问题求解器、编写单元测试验证算法、故意引入Bug并观察AI的定位修复过程。  
> 2. 提交要求：仓库hw01目录需包含src/和tests/工程代码、记录AI交互过程（需求描述、Bug处理、代码重构）的prompt_log.md/session.log交互日志、说明实现思路及运行/测试方式的README.md，最终提交仓库链接给助教。  
> 3. 评价标准：总分由三部分构成，工具熟练度（40%，考察AI工具在项目全流程的高效运用）、交互质量（40%，考察Prompt有效性和代码重构引导能力）、完整性（20%，考察项目结构规范性和测试边界覆盖度），评价侧重工程化过程而非最终代码。

### 2.2 AI 对作业的拆解与建议（摘要）

AI 在阅读作业要求和当前仓库结构后，给出了以下关键拆解（会话 A 与 B 综合）：

- **核心任务拆解为 4 步**：  
  1）初始化含 `src/` 与 `tests/` 的标准 Python 工程；  
  2）在 `src/` 中实现八皇后求解器 `solve(n)`；  
  3）在 `tests/` 中使用 `pytest` 编写单元测试验证算法；  
  4）故意引入 Bug，并通过 AI 协作完成定位与修复。
- **提交物与目录结构建议**：  
  建议在 `hw01/` 目录下统一放置 `README.md`、`prompt_log.md`、`requirements.txt`，并以 `src/` 与 `tests/` 存放业务代码与测试代码，保证结构清晰、可读性强。
- **评分标准对应策略**：  
  - 工具熟练度：在“建工程 → 写代码 → 写测试 → 修 Bug → 写 README”全流程中都通过 AI 完成或协助完成，并在日志中记录关键 Prompt 与响应。  
  - 交互质量：Prompt 要描述清楚需求、上下文和约束条件；出现错误时，通过错误信息与失败用例引导 AI 定位问题，而不是直接给出答案。  
  - 完整性：保证有边界测试（如 `n=1,2,3,4,8`）、规范工程结构和完整运行说明。

---

## 3. 工程初始化与求解器实现（基于 Cursor 的协作）

### 3.1 使用 AI 规划并创建标准工程结构

- 用户在 Cursor 中打开 `HW01` 文件夹后，向 AI 描述目标：  
  > “现在我已经用 Cursor 打开了 HW01 的文件夹，现在我要初始化标准 Python 工程（含 src 源码目录与 tests 测试目录），生成一个干净可直接运行的项目结构。”
- AI 将作业的工程要求拆解为：  
  - 在根目录创建 `src/`（含 `__init__.py`）；  
  - 创建 `tests/`（并建议添加一个示例测试文件，验证 pytest 能正常运行）；  
  - 提供 `requirements.txt` 示例（如包含 `pytest>=7.0.0`）；  
  - 建议 README 中记录运行与测试命令。
- 在 AI 的引导下，完成了上述目录与基础文件的搭建，形成了一个可以直接运行 `pytest` 的空项目骨架。

### 3.2 八皇后求解器接口约定与实现

- 用户随后给出更具体的实现需求（节选）：  
  > “在 Cursor 里新建 src/queens.py，在 src/queens.py 里实现八皇后求解：函数 solve(n) 接收棋盘大小 n，返回所有解的列表，每个解是长度为 n 的列表，表示每一行皇后所在的列索引（0 到 n-1）。用回溯实现。”
- AI 基于此约定提出了以下设计要点：  
  - 函数签名：`solve(n: int) -> List[List[int]]`；  
  - 使用回溯（`backtrack(row)`）逐行放置皇后；  
  - 使用 `is_safe(row, col)` 函数检查是否与已放置的皇后在同列或同一主/副对角线；  
  - 用一个一维列表 `board` 表示当前尝试的解，其中 `board[i]` 为第 `i` 行皇后的列索引。
- 在实现过程中，AI 还建议：  
  - 当 `n <= 0` 时直接返回空列表，作为边界情况处理；  
  - 在 `src/__init__.py` 中导出 `solve` 函数，方便 `from src import solve` 或 `from src.queens import solve` 的统一使用。

最终形成了当前版本的 `solve(n)` 求解器代码，并通过后续测试验证了正确性。

---

## 4. 单元测试设计与边界覆盖（基于 pytest）

### 4.1 测试需求描述与 AI 建议

在完成求解器后，用户向 AI 说明需要在 `tests/` 下新增 `test_queens.py`，并要求测试以下内容：

- `n=1,4,8` 的解个数是否与已知结果一致；  
- `n=2,3` 等情况无解；  
- 各解是否满足：任意两皇后不在同一列、不在同一主对角线、不在同一副对角线；  
- 每个解的长度是否为 `n`，并且列索引范围在 \[0, n-1]。

AI 建议使用 pytest，并设计了一个内部辅助函数 `_is_valid_solution(solution, n)` 来复用合法性检查逻辑，从而保持测试代码简洁清晰。

### 4.2 测试实现要点（当前 `tests/test_queens.py` 概要）

在 AI 的引导下，测试文件涵盖了以下几类用例：

- **解个数测试**：  
  - `n=1` 应当有 1 个解，且唯一解为 `[0]`；  
  - `n=4` 应当有 2 个解；  
  - `n=8` 应当有 92 个解；  
  - `n=2`、`n=3` 均无解（返回空列表）；  
  - `n=0` 或负数返回空列表，作为边界情况。
- **解合法性测试**：  
  - 对 `n=4` 和 `n=8` 的每一个返回解，使用 `_is_valid_solution` 检查是否满足“不同行、不共列、不共对角线”的约束。  
  - 对 `n=1` 的解进行合法性校验。
- **解的格式测试**：  
  - 对多个 `n` 值，检查每个解的长度均为 `n`，并且所有列索引都处于合法范围。

通过这些测试，既验证了解的正确性，又体现了对**典型用例 + 边界情况**的覆盖，有利于在评分标准中的“完整性”部分得分。

---

## 5. Bug 实验与 AI 调试过程

本节记录一次**真实的 Bug 引入 → pytest 暴露问题 → 借助 Cursor AI 分析与修复 → 回归测试通过**的完整过程，对应作业中“故意引入 Bug 并观察 AI 的定位修复过程”的要求。

### 5.1 Bug 引入：n=0 边界条件处理错误

在最初版本中，`solve` 对 \(n \le 0\) 的边界进行了正确处理：

```python
def solve(n: int) -> List[List[int]]:
    ...
    if n <= 0:
        return []
```

为刻意制造 Bug，用于后续实验，我将条件修改为只在 \(n < 0\) 时返回空列表：

```python
def solve(n: int) -> List[List[int]]:
    ...
    if n < 0:  # 故意漏掉 n == 0 的情况
        return []
```

此时，当 `n == 0` 时不会触发提前返回，代码会继续执行回溯逻辑。

### 5.2 触发测试并观察失败

在项目根目录执行仅针对八皇后测试的命令：

```bash
python -m pytest tests/test_queens.py -v
```

pytest 输出中，只有一个用例失败，其余 10 个用例全部通过：

```text
tests/test_queens.py::test_solve_n1_one_solution PASSED
tests/test_queens.py::test_solve_n4_two_solutions PASSED
tests/test_queens.py::test_solve_n8_ninety_two_solutions PASSED
tests/test_queens.py::test_solve_n2_no_solution PASSED
tests/test_queens.py::test_solve_n3_no_solution PASSED
tests/test_queens.py::test_solve_zero_empty FAILED
...
```

失败用例 `test_solve_zero_empty` 的关键信息为：

```text
E       assert [[]] == []
E         
E         Left contains one more item: []
E         
E         Full diff:
E         - []
E         + [
E         +     [],
E         + ]
```

这表明当前实现中 `solve(0)` 返回的是 `[[]]`，而测试期望的是空列表 `[]`。

### 5.3 与 Cursor AI 的调试对话（摘要）

在看到上述失败后，我把命令、失败信息以及当前的 `solve` 代码片段发给 Cursor 内置 AI，请它帮助分析原因和给出修复建议。对话的关键节点如下：

- **用户描述问题**  
  - 说明执行了 `python -m pytest tests/test_queens.py -v`；  
  - 指出只有 `test_solve_zero_empty` 失败，并贴出 `assert [[]] == []` 的断言信息；  
  - 补充当前 `solve` 开头的实现已经改成 `if n < 0: return []`。

- **AI 分析 Bug 成因**  
  - 对 `n == 0` 的执行路径做了推理：  
    1. `n == 0` 时，`if n < 0:` 条件不满足，因此不会提前返回；  
    2. 随后调用 `backtrack(0)`；  
    3. 在 `backtrack` 中，一开始就满足 `row == n`（0 == 0），于是把当前的 `board[:]`（此时是空列表 `[]`）追加到 `result`；  
    4. 最终函数返回 `[[]]`。  
  - 指出这与测试期望的“对于 n=0 应直接返回空列表 []”不符，是一个典型的边界条件 Bug。

- **AI 给出的修复建议**  
  - 将 `if n < 0:` 改回 `if n <= 0:`，在进入回溯逻辑之前统一处理 `n <= 0` 的情况；  
  - 建议修改后重新运行同一组 pytest 测试，确认所有用例都能通过。

此外，AI 在检查 `queens.py` 时，还顺带将 `is_safe` 中副对角线的条件书写格式规范为：

```python
if row - r == c - col:
    return False
```

（仅调整了空格和顺序，使主、副对角线条件更清晰，对本次 Bug 无实质影响。）

### 5.4 修复代码并回归测试

根据 AI 的建议，我在 `src/queens.py` 中将 `solve` 的开头逻辑改为：

```python
def solve(n: int) -> List[List[int]]:
    ...
    if n <= 0:
        return []
```

同时确认 `is_safe` 中主、副对角线的判断分别为：

```python
# 同一主对角线：行差 == 列差
if row - r == col - c:
    return False
# 同一副对角线：行差 == -列差
if row - r == c - col:
    return False
```

保存后，再次在项目根目录运行：

```bash
python -m pytest tests/test_queens.py -v
```

这一次的测试结果为：

```text
tests/test_queens.py::test_solve_n1_one_solution PASSED
tests/test_queens.py::test_solve_n4_two_solutions PASSED
tests/test_queens.py::test_solve_n8_ninety_two_solutions PASSED
tests/test_queens.py::test_solve_n2_no_solution PASSED
tests/test_queens.py::test_solve_n3_no_solution PASSED
tests/test_queens.py::test_solve_zero_empty PASSED
tests/test_queens.py::test_solve_negative_empty PASSED
tests/test_queens.py::test_solve_n4_all_solutions_valid PASSED
tests/test_queens.py::test_solve_n8_all_solutions_valid PASSED
tests/test_queens.py::test_solve_n1_solution_valid PASSED
tests/test_queens.py::test_solve_each_solution_length_n PASSED
============================= 11 passed in 0.04s ==============================
```

至此，这次围绕 `n=0` 边界条件的 Bug 实验完成：  
**通过单元测试暴露问题 → 将失败日志与代码发给 AI → AI 分析出是边界条件漏判 → 根据建议修复 → 回归测试全部通过。**

---

## 6. 对 AI 编程工具使用的简要反思

结合目前的协作过程，可以做出如下初步总结：

- **工具熟练度方面**：  
  已能利用 Cursor 在项目全流程中提供帮助，从工程初始化（目录、依赖、基本文件）到算法接口设计、单元测试用例规划以及最终的进度核对与作业对照，显著降低了样板代码与结构设计的负担。

- **交互质量方面**：  
  在后期的会话中，逐渐学会用自然语言清晰地描述需求与约束（例如精确说明 `solve(n)` 的输入输出语义、测试覆盖的边界情况），并在询问“现在进行到哪一步”时，让 AI 从工程视角进行阶段性总结，而不仅仅关注单个函数的正确性。

- **工程完整性方面**：  
  在 AI 的建议下，目前项目已经具备：规范的 `src/` + `tests/` 结构、类型标注较完善的求解器实现、覆盖典型与边界用例的单元测试，以及记录 AI 协作过程的本日志文件。

