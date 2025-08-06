from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simulación de base de datos (normalmente sería Salesforce)
orders = {
    "1001": {"status": "Shipped", "delivery_date": "2025-08-08"},
    "1002": {"status": "Processing", "delivery_date": "2025-08-10"},
}

@app.route("/")
def home():
    """Carga la página principal del portal SmartServe Lite"""
    return render_template("index.html")

@app.route("/check-order", methods=["POST"])
def check_order():
    """Simula un endpoint que Einstein Bot usaría para responder estado del pedido"""
    data = request.get_json()
    order_id = data.get("order_id")

    if order_id in orders:
        response = {
            "message": f"Your order {order_id} is {orders[order_id]['status']} "
                       f"and will be delivered on {orders[order_id]['delivery_date']}."
        }
    else:
        response = {"message": "Order not found. Please check the ID."}

    return jsonify(response)

@app.route("/predict-next-action", methods=["POST"])
def predict_next_action():
    """Simula Einstein Next Best Action con una lógica sencilla"""
    data = request.get_json()
    issue_type = data.get("issue_type", "").lower()

    actions = {
        "invoice": "Download your latest invoice here.",
        "delivery": "You can reschedule your delivery or track your package.",
        "support": "We recommend contacting a live agent for complex issues."
    }

    recommendation = actions.get(issue_type, "Please select a valid option.")
    
    return jsonify({"next_best_action": recommendation})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
