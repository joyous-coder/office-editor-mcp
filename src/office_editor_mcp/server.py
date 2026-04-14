"""
Office Editor MCP Server - 统一的 MCP 服务器入口

整合了 Word、Excel、PowerPoint 和高级文档处理功能。
"""

import logging
from mcp.server.fastmcp import FastMCP

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("OfficeEditorMCP")

# 创建统一的 MCP 服务器
mcp = FastMCP("office-editor-mcp")


def main():
    """主入口函数"""
    logger.info("启动 Office Editor MCP Server...")
    mcp.run()


if __name__ == "__main__":
    main()
