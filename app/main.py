from fastapi import FastAPI
# from app.routes.category_routes import router as category_routes
from routes.produto_routes import router as produto_router
from routes.user_routes import router as user_router
from routes.sector_routes import router as sector_router

app = FastAPI()
@app.get('/health-check')
def health_check():
    return True

app.include_router(produto_router)
app.include_router(user_router)
app.include_router(sector_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8003, reload=True)