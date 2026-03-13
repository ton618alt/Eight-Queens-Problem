"""示例测试：验证项目结构与运行环境。"""
import pytest


def test_import_src_package():
    """确保 src 包可被导入。"""
    import src
    assert src is not None


def test_placeholder():
    """占位测试，确保 pytest 能正常执行。"""
    assert 1 + 1 == 2
