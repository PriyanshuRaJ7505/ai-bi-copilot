from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return FileResponse("index.html")


@app.get("/predict")
def predict(price: int, quantity: int):
    revenue = price * quantity
    return {
        "price": price,
        "quantity": quantity,
        "predicted_revenue": revenue
    }


@app.get("/summary")
def summary():
    return {
        "total_revenue": 20000,
        "best_product": "Laptop",
        "transactions": 15
    }