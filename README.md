# MCP FastAPI Proxy

Hacking on a way to automatically create an Anthropic MCP server from an existing FastAPI server. NOT FOR PRODUCTION USE, this uses exec() which could be very bad if you pointed it at untrusted servers.

## How to run

Start FastAPI server
```
uv run fastapi dev fastapi_server.py
```

Run the MCP server
```
uv run fastmcp dev mcp_server.py
```

Now you can go to http://localhost:5173/#tools, hit "List Tools", and you should be able to see the get_weather tool and run it with "Run Tool". 