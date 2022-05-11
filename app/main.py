from fastapi import FastAPI
from app.routes import b2b_routes
from starlette.responses import RedirectResponse

app = FastAPI()
app.include_router(b2b_routes)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")
