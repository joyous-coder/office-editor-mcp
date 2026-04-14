"""
Office Editor MCP Package

This package provides a unified MCP server for Office document processing,
integrating Word, Excel, PowerPoint and advanced document processing features.

Usage:
    from office_editor_mcp.server import mcp
    mcp.run()

Or via command line:
    uvx office-editor-mcp
"""

# 导入各个模块，触发 @mcp.tool() 装饰器的注册
# 这些导入语句确保所有工具函数被注册到全局 mcp 实例

from office_editor_mcp import excel
from office_editor_mcp import word
from office_editor_mcp import powerpoint
from office_editor_mcp import general

# 导出 server 模块中的 mcp 实例和 main 函数
from office_editor_mcp.server import mcp, main

__all__ = [
    "mcp",
    "main",
    "excel",
    "word",
    "powerpoint",
    "general",
]
