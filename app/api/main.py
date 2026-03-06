from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI BI Copilot running"}

@app.get("/predict")
def predict(price: int, quantity: int):
    return {"predicted_revenue": price * quantity}

@app.get("/summary")
def summary():
    return {
        "total_revenue": 20000,
        "best_product": "Laptop",
        "transactions": 15
    }