async function analyzeCode() {
    const code = document.getElementById("code").value;

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML =
        "<p>Score: " + data.score + "</p>" +
        "<p>Issues: " + data.issues.join(", ") + "</p>";
}