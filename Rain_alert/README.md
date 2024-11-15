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

## 📥 Installation
To install the program and run the program
- Go to the shell 
    ```shell
    $ git clone https://github.com/sakhileln/Code-Crunch-Marathon.git
    ```
- Change directory to the project
    ```shell
    $ cd Code-Crunch-Marathon/Rain_alert/
    ```
- Install the required packages
    ```shell
    $ pip install -r requirements.txt
    ```
- Run the project
    ```shell
    $ python3 main.py
    ```
---

## 🛠️ Usage
If you are interested to know if there is expected rain in your vicinity.
1. Create a .env file at the root of the project.
2. Get your OpenWeather API Key and Twilio Authorasation Token and Account SID, and a Twilio Number.
3. Get the number you like to receive the SMS forecast on.
4. Add the items mentioned above to .env file you just created.
5. Use .env.sample file as a guide for adding items on .env file
6. Run the project and you will receive a SMS message with the forecast.

---

## 👨‍💻 Contributing
Contributions are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request.
1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add some feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/YourFeature
   ```
5. Open a pull request.

---