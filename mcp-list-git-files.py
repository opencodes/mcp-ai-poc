
import sys
import traceback
from fastmcp import FastMCP

from lib import list_files_from_github_url

# Add debug logging
print("Starting MCP server...", file=sys.stderr)
print(f"Python version: {sys.version}", file=sys.stderr)

try:
    mcp = FastMCP("mcp-poc", "0.1.0", "A simple MCP server for listing GitHub files")
    print("FastMCP instance created successfully", file=sys.stderr)
except Exception as e:
    print(f"Error creating FastMCP instance: {e}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)


@mcp.tool
def list_files_in_git_repo(repo:str) -> int:
    """List public GitHub repository files"""
    print(f"list_files_in_git_repo called with repo={repo}", file=sys.stderr)
    print("Calling list_files_from_github_url...", list_files_from_github_url(repo), file=sys.stderr)
    return list_files_from_github_url(repo)


print("Tool registered successfully", file=sys.stderr)

if __name__ == "__main__":
    try:
        print("About to start mcp.run()", file=sys.stderr)
        mcp.run()
        print("mcp.run() completed", file=sys.stderr)
    except KeyboardInterrupt:
        print("Server interrupted by user", file=sys.stderr)
    except Exception as e:
        print(f"Error running MCP server: {e}", file=sys.stderr)
        traceback.print_exc(file=sys.stderr)
        sys.exit(1)