from fastapi import FastAPI
import requests

app = FastAPI()

@app.post("/order")
def create_order():
    # Simulasi bikin order
    print("Order created")

    # Panggil payment service
    payment_response = requests.post("http://localhost:8001/pay")
    if payment_response.status_code != 200:
        return {"error": "Payment failed, canceling order"}

    return {"message": "Order placed and paid"}
