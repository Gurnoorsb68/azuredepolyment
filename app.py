from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
async def read_root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple HTML Page</title>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>This is a simple HTML page served by FastAPI.</p>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
