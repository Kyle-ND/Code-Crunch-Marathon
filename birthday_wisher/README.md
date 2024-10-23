# Birthday Wisher

A Python script to automatically send birthday wishes via email. The program fetches birthday data from a Google Sheet API using Sheety, compares the current date with stored birthdays, and sends an email if a match is found.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)

## Features

- Automatically fetches birthday data from a Google Sheet.
- Compares birthdays to the current date.
- Sends personalized birthday emails using an SMTP server.
- Utilizes environment variables for secure email credentials.
- Lightweight and easy to set up.

## Requirements

- Python 3.8+
- An active Gmail account for sending emails.
- API endpoint containing the birthday data (uses Sheety API).
- A `.env` file for storing sensitive credentials.

### Python Libraries:

- `requests`
- `smtplib` (Standard Library)
- `email.mime` (Standard Library)
- `python-dotenv`

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/birthday-wisher.git
   cd birthday_wisher
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the project directory with the following content:

   ```plaintext
   APPS_PASSWORD=your_apps_password
   EMAIL=your_email@example.com
   ```

   - `APPS_PASSWORD`: Your Gmail App password (you need to enable 2FA on your Gmail and generate an app-specific password).
   - `EMAIL`: Your Gmail address that will be used to send the birthday wishes.

4. **Configure the Sheety API:**

   - Create a Google Sheet with columns for `name`, `email`, and `birthday`.
   - Use [Sheety](https://sheety.co/) to turn your Google Sheet into an API.
   - Replace the `URL` in the code with your Sheety API URL.

## Configuration

- In the script, replace the `URL` variable with your specific Sheety API URL.
- The script expects the Google Sheet to have the following columns:
  - **name**: The name of the person.
  - **email**: The email address of the person.
  - **birthday**: The birthday of the person in the format `YYYY-MM-DD`.

## Usage

1. **Run the script manually** to check for birthdays and send emails:

   ```bash
   python birthday_wisher.py
   ```

2. **Automate the script** using a task scheduler:
   - For **Linux/Mac**, use `cron`.
   - For **Windows**, use Task Scheduler.

## Project Structure

```
birthday-wisher/
├── .env                # Environment variables file
├── README.md           # This README file
├── requirements.txt    # Python dependencies
└── birthday_wisher.py  # Main script file
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the project.
2. Create a feature branch (`git checkout -b feature/new-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/new-feature`).
5. Open a pull request.
