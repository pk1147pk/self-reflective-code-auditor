let chart;

async function analyzeCode() {
let code = document.getElementById("code").value;

```
let response = await fetch("/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({code: code})
});

let result = await response.json();

// Output show
document.getElementById("output").innerHTML =
    "<b>Score:</b> " + result.score +
    "<br><b>Issues:</b> " + result.issues.join(", ");

// Graph Update
if(chart) {
    chart.destroy();
}

chart = new Chart(document.getElementById("scoreChart"), {
    type: "bar",
    data: {
        labels: ["Your Code Score"],
        datasets: [{
            label: "Quality Score",
            data: [result.score]
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true,
                max: 100
            }
        }
    }
});
```

}
