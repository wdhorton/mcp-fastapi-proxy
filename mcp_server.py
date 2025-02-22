import os

from fastmcp import FastMCP
import requests

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://127.0.0.1:8000")

mcp = FastMCP("Demo 🚀")

resp = requests.get(f"{FASTAPI_URL}/openapi.json")
openapi = resp.json()

print(openapi)

fn_template = """
def fn({args_str}):
    resp = requests.get("{fastapi_url}{path}", params={params_str})
    return resp.json()
"""

def create_args_and_params_str(parameters):
    args = []
    params = []
    for param in parameters:
        name = param["name"]
        args.append(name)
        params.append(f'"{name}": {name}')
    return ", ".join(args), "{" + ", ".join(params) + "}"


for path, spec in openapi["paths"].items():
    args_str, params_str = create_args_and_params_str(spec["get"]["parameters"])
    fn_str = fn_template.format(args_str=args_str, params_str=params_str, path=path, fastapi_url=FASTAPI_URL)
    exec(fn_str)
    mcp.add_tool(
        name=path[1:],
        description=spec["get"]["description"],
        fn=fn
    )