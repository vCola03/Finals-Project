from pyscript import document
from pyodide.ffi import create_proxy

def welcome_message(event):
    document.getElementById("welcome-message").innerText = (
        "Welcome to AROMA! We are happy to serve you!"
    )

def calculate_order(event):
    event.preventDefault()

    name = document.getElementById("customer").value.strip()
    price = float(document.getElementById("product").value)
    quantity_text = document.getElementById("quantity").value

    if not name:
        document.getElementById("result").innerText = (
            "Please enter your name."
        )
        return

    try:
        quantity = int(quantity_text)
        if quantity < 1 or quantity > 100:
            raise ValueError
    except (ValueError, TypeError):
        document.getElementById("result").innerText = (
            "Please enter a quantity from 1 to 100."
        )
        return

    total = price * quantity

    document.getElementById("result").innerHTML = (
        f"<h3>Order Summary</h3>"
        f"<p>Thank you, {name.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')}!</p>"
        f"<p>Quantity: {quantity}</p>"
        f"<p>Total: ₱{total:,.2f}</p>"
        f"<p>Your sample order has been calculated.</p>"
    )

document.getElementById("welcome-btn").addEventListener(
    "click", create_proxy(welcome_message)
)

document.getElementById("order-form").addEventListener(
    "submit", create_proxy(calculate_order)
)