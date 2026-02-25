import random

# Simulate daily sensor data (replace this with actual sensor data from NodeMCU)
def fetch_sensor_data(day):
    # Simulated values for soil parameters
    soil_data = {
        "day": day,
        "pH": random.uniform(5.5, 7.5),         # Soil pH (acidic to neutral)
        "moisture": random.randint(30, 80),     # Soil moisture percentage
        "temperature": random.randint(20, 35),  # Temperature in Celsius
    }
    return soil_data

# Wheat growing procedure based on day and conditions
def daily_procedure(day, pH, moisture, temperature):
    print(f"Day {day}:")
    print(f"  - Soil pH: {pH:.2f}")
    print(f"  - Soil Moisture: {moisture}%")
    print(f"  - Temperature: {temperature}°C")

    # Stage-specific procedures
    if day == 1:
        print("  - Add lime to neutralize the soil." if pH < 6.0 else "  - pH is optimal; no lime needed.")
        print("  - Water the crop to maintain optimal moisture levels." if moisture < 40 else "  - Moisture level is sufficient.")
        print("  - Prepare the soil and sow the wheat seeds.")
    elif 2 <= day <= 7:
        print("  - Maintain consistent soil moisture; water lightly if moisture drops below 40%.")
        print("  - Ensure temperature stays between 20–25°C; provide shade if it exceeds 30°C.")
        print("  - Remove early weeds to prevent competition for nutrients.")
    elif 8 <= day <= 14:
        print("  - Water every 3–4 days to keep the topsoil moist.")
        print("  - Apply nitrogen-based fertilizer to promote root and leaf development.")
        print("  - Check for pests like aphids and use organic repellents if needed.")
    elif 15 <= day <= 21:
        print("  - Increase watering slightly as tillering requires more moisture.")
        print("  - Apply a second round of nitrogen fertilizer to support shoot formation.")
        print("  - Monitor for healthy green leaves and remove yellowed ones.")
    elif 22 <= day <= 30:
        print("  - Continue irrigation to maintain optimal soil moisture.")
        print("  - Add potassium fertilizer to strengthen stems if required.")
        print("  - Remove weeds and check for fungal diseases, treating with organic fungicides if needed.")
    else:
        print("  - Monitor crop health and follow standard care practices.")

    print("-" * 50)

# Main loop for 30 days of wheat growth
def simulate_wheat_growth():
    for day in range(1, 31):
        sensor_data = fetch_sensor_data(day)  # Fetch daily sensor data
        daily_procedure(
            day=day,
            pH=sensor_data["pH"],
            moisture=sensor_data["moisture"],
            temperature=sensor_data["temperature"],
        )

# Run the simulation
simulate_wheat_growth()
