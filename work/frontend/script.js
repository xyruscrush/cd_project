let charts = {};
let allData = [];

// ---------- LABEL ----------
function getLabel(value) {
    const map = ["Low", "Medium-Low", "Medium", "High"];
    return map[value];
}

// ---------- COUNT ----------
function countValues(data, key) {
    let counts = [0, 0, 0, 0];
    data.forEach(item => counts[item[key]]++);
    return counts;
}

// ---------- BAR CHART ----------
function createBarChart(id, label, data) {

    if (charts[id]) charts[id].destroy();

    const ctx = document.getElementById(id).getContext("2d");

    charts[id] = new Chart(ctx, {
        type: "bar",
        data: {
            labels: ["Low", "Medium-Low", "Medium", "High"],
            datasets: [{
                label: label,
                data: data,
                borderRadius: 8,
                barThickness: 30
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: {
                        color: "white"
                    }
                }
            },
            scales: {
                x: {
                    ticks: { color: "white" }
                },
                y: {
                    beginAtZero: true,
                    ticks: { color: "white" }
                }
            }
        }
    });
}

// ---------- ANALYZE ----------
function analyze() {

    const url = document.getElementById("repoUrl").value;
    const resultsDiv = document.getElementById("results");
    const loading = document.getElementById("loading");

    resultsDiv.innerHTML = "";
    loading.classList.remove("hidden");
    loading.innerText = "Analyzing...";

    fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ url: url })
    })
        .then(res => res.json())
        .then(data => {

            loading.classList.add("hidden");

            if (data.error) {
                alert("❌ " + data.error);
                return;
            }

            allData = data;

            // ---------- SUMMARY ----------
            document.getElementById("summary").classList.remove("hidden");
            document.getElementById("totalFiles").innerText = data.length;
            document.getElementById("highRisk").innerText =
                data.filter(x => x.importance == 3).length;
            document.getElementById("sensitive").innerText =
                data.filter(x => x.sensitivity == 3).length;

            // ---------- CARDS ----------
            data.forEach(item => {
                const card = document.createElement("div");
                card.className = "card";

                card.innerHTML = `
                <h3>${item.file}</h3>
                <p>Usage: ${getLabel(item.usage)}</p>
                <p>Activity: ${getLabel(item.activity)}</p>
                <p>Importance: ${getLabel(item.importance)}</p>
                <p>Sensitivity: ${getLabel(item.sensitivity)}</p>
            `;

                resultsDiv.appendChild(card);
            });

            // ---------- CHARTS ----------
            createBarChart("usageChart", "Usage Distribution", countValues(data, "usage"));
            createBarChart("activityChart", "Activity Distribution", countValues(data, "activity"));
            createBarChart("importanceChart", "Importance Distribution", countValues(data, "importance"));
            createBarChart("sensitivityChart", "Sensitivity Distribution", countValues(data, "sensitivity"));
        })
        .catch(err => {
            loading.classList.add("hidden");
            alert("❌ Backend not reachable!");
            console.error(err);
        });
}