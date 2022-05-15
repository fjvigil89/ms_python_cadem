from fastapi import FastAPI
from app.routes.b2b_routes import item_routes, move_routes
from starlette.responses import RedirectResponse

app = FastAPI()
app.include_router(item_routes)
app.include_router(move_routes)

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")
