// Función para consultar estado del pedido
function checkOrder() {
    const orderId = document.getElementById("orderId").value;

    fetch("/check-order", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ order_id: orderId })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("orderResult").textContent = data.message;
    });
}

// Función para predecir la mejor acción
function predictAction() {
    const issueType = document.getElementById("issueType").value;

    fetch("/predict-next-action", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ issue_type: issueType })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("actionResult").textContent = data.next_best_action;
    });
}
