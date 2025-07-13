# hello-world-mcp

## Description
A simple Python project that prints a hello message.

## Requirements
- Python 3.11 or higher

## Setup

Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies

If you need to install the `mcp[cli]` extra, use quotes to avoid shell errors:

```bash
uv add 'mcp[cli]'
```

> **Note:** The quotes are required in zsh to prevent bracket expansion errors.

## How to Run

### Run the client
`client.py` connects to the `weather.py` server using stdio, lists available tools, and calls the `get_weather` tool with a sample location.

```bash
python client.py
```

#### Or run the client with uv
Running with `uv` ensures all dependencies are managed by uv:

```bash
uv run client.py
```

## Using the MCP CLI

To run the `weather.py` server in development mode with live reloading and the MCP Inspector UI, use:

```bash
mcp dev weather.py
```

This will start your MCP server locally and open the Inspector at http://localhost:6274 for testing and debugging your tools.

## Example Host Configuration

If you need to configure your host/server entry (e.g., for Claude Desktop or a similar tool), use the following example:

```json
"weather": {
  "command": "uv",
  "args": [
    "--directory",
    "/path",
    "run",
    "weather.py"
  ]
}
```

This configuration tells the host to use `uv` to run `weather.py` from your project directory, ensuring all dependencies are available.

## Troubleshooting

### MCP Inspector Connection Error
If you see a connection error in MCP Inspector asking for a proxy session token, make sure you start the Inspector with the server URL including your token, like this:

```
http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=YOUR_TOKEN_HERE#resources
```

**Example:**
```
http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=1f874aa0441c94cb870f4b4a14c3f5b76e5a814e422ba86687a98396b7fb5846#resources
```

Replace `YOUR_TOKEN_HERE` with your actual session token.
