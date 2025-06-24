
import sys
import traceback
from fastmcp import FastMCP

from lib import read_readme_from_github

# Add debug logging
print("Starting MCP server...", file=sys.stderr)
print(f"Python version: {sys.version}", file=sys.stderr)

try:
    mcp = FastMCP("mcp-readme", "0.1.0", "A simple MCP server for listing GitHub files")
    print("FastMCP instance created successfully", file=sys.stderr)
except Exception as e:
    print(f"Error creating FastMCP instance: {e}", file=sys.stderr)
    traceback.print_exc(file=sys.stderr)
    sys.exit(1)


@mcp.tool
def read_the_readme_file(repo:str) -> int:
    """List public GitHub repository files"""
    print(f"read_readme_from_github called with repo={repo}", file=sys.stderr)
    print("Calling read_readme_from_github...", read_readme_from_github(repo), file=sys.stderr)
    return read_readme_from_github(repo)


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