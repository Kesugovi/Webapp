let currentUnit = "metric"; // default Celsius
const toggleBtn = document.getElementById("toggleUnit");

async function getWeather() {
    const city = document.getElementById("cityInput").value;
    if (!city) {
        alert("Please enter a city");
        return;
    }

    const response = await fetch("/weather", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ city: city, unit: currentUnit })
    });

    const data = await response.json();
    if (data.error) {
        document.getElementById("weatherResult").innerHTML = `<p>${data.error}</p>`;
        return;
    }

    document.getElementById("weatherResult").innerHTML = `
        <h3>${data.city}</h3>
        <p>${data.temperature} ${currentUnit === "metric" ? "°C" : "°F"}</p>
        <p>${data.description}</p>
    `;

    if (data.bg_url) {
        document.getElementById("background").style.backgroundImage = `url(${data.bg_url})`;
    }
}

toggleBtn.addEventListener("click", () => {
    if (currentUnit === "metric") {
        currentUnit = "imperial"; // Fahrenheit
        toggleBtn.textContent = "°F";
        toggleBtn.classList.add("fahrenheit");
    } else {
        currentUnit = "metric"; // Celsius
        toggleBtn.textContent = "°C";
        toggleBtn.classList.remove("fahrenheit");
    }
});
