from lecture_2.hw.shop_api.controllers import cart, item
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="Shop API")

@app.get(
    path="/ping"
)
async def pong():
    return {"message": "pong"}

app.include_router(cart.router)
app.include_router(item.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)