from js import Response
from server import app

# async def on_fetch(request, env):
#     return Response.new("Hello World!")

async def on_fetch(request, env, ctx):
    # Extract path and method from request
    url = request.url
    path = url.split('/', 3)[3] if len(url.split('/', 3)) > 3 else ""
    method = request.method
    
    # Handle CORS preflight requests
    if method == "OPTIONS":
        return Response("", 
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            }
        )
    
    # Process the request based on path
    if path == "process":
        # Get the request body
        body = request.text()
        # Call your processing function from server.py
        result = app.process_excel_data(body)
        return Response(result, 
            headers={
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            }
        )
    
    # Default response for root path or unknown paths
    return Response("Remote Excel MCP Server", 
        headers={
            "Content-Type": "text/plain",
            "Access-Control-Allow-Origin": "*"
        }
    )
