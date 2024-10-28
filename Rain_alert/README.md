# 🌧️ Rain Alert

Welcome to **Rain Alert**! This project utilizes the **OpenWeather API** to detect rain conditions in a user’s location and promptly sends an SMS alert using **Twilio**.

---

## 📋 Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [To-Do](#to-do)
- [Contributing](#contributing)

---

## ⚡ Features

- **Real-Time Weather Detection**: Fetches current weather data using **OpenWeather API** based on user’s GPS coordinates.
- **Location Awareness**: Uses IP-based geolocation to find and use the user’s current location.
- **Instant Notifications**: Sends an SMS alert with weather information using **Twilio**.
- **Clean Code Structure**: Simple, modular functions for easy understanding and maintenance.

---

## ✅ Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.x**
2. **pip** (Python package manager)
3. **Twilio account** – [Sign up here](https://www.twilio.com/try-twilio)
4. **OpenWeather API Key** – [Generate your key here](https://openweathermap.org/api)
5. **Environment Variables** – Store sensitive data like API keys securely using **dotenv**.

---

## 🚀 Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/rain-alert.git
   cd Rain_alert
   ```

2. **Install Required Packages**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Environment Variables**:
   Create a `.env` file in the project root and add your credentials:
   ```plaintext
   API_KEY=your_openweather_api_key
   TWILIO_ACCOUNT_SID=your_twilio_account_sid
   TWILIO_AUTH_TOKEN=your_twilio_auth_token
   ```

---

## ⚙️ Configuration

- **Twilio Number**: Update `from_="+12562865821"` in the `send_sms` function with your Twilio number.
- **Recipient Number**: Update `to="+27785703745"` in the `send_sms` function with the number where you want to receive alerts.
- **API Key**: Ensure your **OpenWeather API Key** is correctly added to your `.env` file.

---

## 🖥️ Usage

1. **Run the Script**:
   ```bash
   python main.py
   ```
2. **Expected Output**: The program fetches the current GPS coordinates, retrieves weather data, and sends an SMS with the current weather condition to the specified phone number.

---

## 📝 To-Do

- **Weather Forecasting**: Add functionality to alert for specific weather conditions (e.g., rain expected in the next 6 hours).
- **Multiple Recipients**: Allow the SMS to be sent to multiple recipients.
- **Enhanced Notifications**: Customize SMS messages based on weather severity or type.
- **User Interface**: Add a simple web or mobile interface for easier configuration and real-time monitoring.

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit a Pull Request or open an issue to propose any changes or improvements.

---
