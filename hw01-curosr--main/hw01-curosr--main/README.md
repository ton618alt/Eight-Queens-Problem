# hw01
基于AI协作的八皇后问题工程化实践（HW01）
八皇后问题求解器 (Eight Queens Solver)
一个基于回溯算法实现的八皇后问题求解工具，可计算并返回 n皇后在n×n棋盘上的所有合法摆放方案。本项目使用CursorAI辅助开发，并托管于GitHub。
一、实现思路
核心采用回溯算法，逐行放置皇后并校验位置合法性，核心逻辑如下：
1. 回溯 (backtrack)：递归尝试在当前行的每一列放置皇后，若放置后与已放置的皇后无冲突（不同行、不同列、不同对角线），则继续递归下一行；若递归至最后一行（所有皇后放置完成），则记录该合法方案。
2. solve(n)：核心入口函数，接收正整数n（表示棋盘大小与皇后数量），调用回溯算法计算所有合法摆放方案，最终返回方案列表（每个方案为一维数组，下标代表行号，数组值代表对应行皇后所在的列号）。
二、开发与设计工具
本项目使用 CursorAI 作为主要开发工具，借助其 AI 辅助功能进行代码设计、重构与调试，提升开发效率与代码质量。
三、如何运行
在项目根目录下，通过 Python 命令直接调用核心函数，示例如下：
bash
# 求解 4 皇后问题并打印所有方案
python -c "from src.queens import solve; print(solve(4))"
# 求解 8 皇后问题并打印所有方案
python -c "from src.queens import solve; print(solve(8))"
四、如何测试
1. 首先安装测试依赖包：
bash  
pip install -r requirements.txt  
2. 执行测试用例，查看详细测试结果： 
bash 
pytest tests/ -v
五、项目结构
plaintext
├── src/
│   └── queens.py      # 核心求解代码
├── tests/
│   └── test_queens.py # 测试用例
├── README.md          # 项目说明
└── requirements.txt   # 依赖声明     
