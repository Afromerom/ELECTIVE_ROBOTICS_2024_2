function getCaseStatus() {
    const caseNumber = document.getElementById("caseNumber").value;
    const serial = document.getElementById("serialOrAccount").value;

    if (caseNumber === "225964" && serial === "CBH123456") {
        document.getElementById("caseResult").textContent = "Case 225964 is currently Open and pending review.";
    } else {
        document.getElementById("caseResult").textContent = "Case not found or invalid details.";
    }
}

function sendEmailUpdates() {
    document.getElementById("emailResult").textContent = "Updates have been sent to your registered email address.";
}

function getTrackingNumber() {
    const caseNumber = document.getElementById("trackCaseNumber").value;
    const systemNumber = document.getElementById("systemNumber").value;

    if (caseNumber && systemNumber) {
        const trackingNum = "882677670333";
        document.getElementById("trackingResult").innerHTML =
            `Tracking Number: ${trackingNum} <br> 
             <a href="https://www.fedex.com/fedextrack/?tracknumbers=${trackingNum}" target="_blank">Check delivery status on FedEx</a>`;
    } else {
        document.getElementById("trackingResult").textContent = "Please enter both Case and System numbers.";
    }
}

function openChat() {
    window.location.href = "/chat";  // Ruta que lleva al chatbot
}
