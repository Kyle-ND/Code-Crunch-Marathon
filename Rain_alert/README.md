
# 🌧️ Rain Alert - README

Welcome to **Rain Alert**! This project leverages the **OpenWeather API** to detect whether rain is expected in a user's area and notifies the user via **SMS using Twilio**.

---

## 📋 Table of Contents  
- [Features](#features)  
- [Prerequisites](#prerequisites)  
- [Installation](#installation)  
- [Configuration](#configuration)  
- [Usage](#usage)  
- [To-Do](#to-do)  
- [Contributing](#contributing)  
- [License](#license)

---

## ⚡ Features  
- Detect rain forecast using the **OpenWeather API**.  
- Retrieve and use the user's **current location**.  
- Send real-time SMS alerts using **Twilio**.  
- Clean and simple code structure for easy maintenance.

---

## ✅ Prerequisites  
Before you begin, ensure you have the following installed:

1. **Python 3.x**  
2. **pip** (Python package manager)  
3. **Twilio account** – [Sign up here](https://www.twilio.com/try-twilio)  
4. **OpenWeather API Key** – [Generate your key here](https://openweathermap.org/api)

---

## ⚙️ Installation  

1. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**  
   - On **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Install required packages**  
   ```bash
   python -m pip install requests
   pip install python-dotenv twilio
   ```

4. **Configuration**  
   - Open the `check_for_rain` function in the code and update `to="..."` with the phone number where you wish to receive SMS alerts.

---

You’re all set! 🎉 You can now run the program.
