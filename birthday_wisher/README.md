
# 🎉 Birthday Wisher - README

**Birthday Wisher** automates the process of checking for upcoming birthdays and sending personalized emails. This project integrates with **Google Sheets API** to fetch birthdays and uses **smtplib** to send birthday wishes via email.

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
- Fetch birthdays from **Google Sheets**.  
- Check if today is anyone’s birthday from the database.  
- Send **personalized email wishes** using **smtplib**.  
- Simple configuration through environment variables.

---

## ✅ Prerequisites  

1. **Python 3.x** installed  
2. **Google Account** with access to a Google Sheet  
3. **Google Cloud Console Project** with Sheets API enabled  
4. **Service Account** credentials for Google Sheets (JSON format)  
5. Email account with **SMTP access** (e.g., Gmail)

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
   - On **Unix-based systems** (e.g., BSD):
     ```bash
     source venv/bin/activate
     ```

3. **Install required packages**  
   ```bash
   python -m pip install requests
   pip install python-dotenv
   ```

4. **Access the Google Sheet**  
   Open [this Google Sheet](https://docs.google.com/spreadsheets/d/1Appa2HmW7PlRevDMxxSCuAeG7ov18jpHbNm2r_O6QE0/edit?usp=sharing) and add an upcoming birthday.

---

You’re all set! 🎉 You can now run the program.
