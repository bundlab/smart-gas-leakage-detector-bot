# 🚨 Smart Gas Leakage Detector Bot

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Production-green)
![ESP32](https://img.shields.io/badge/ESP32-IoT-orange)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![License](https://img.shields.io/badge/License-MIT-success)
![Status](https://img.shields.io/badge/Status-Deployment%20Ready-brightgreen)

> A **production‑ready IoT gas leakage detection system** using **ESP32, MQ gas sensor, FastAPI backend, PostgreSQL, Telegram Bot alerts, Web Dashboard, and Docker deployment**.

This project is designed for **real‑world deployment** in smart homes, laboratories, kitchens, and industrial environments.

---

## ✨ Key Features

* 🔥 Real‑time gas leakage detection (LPG, Methane, Propane)
* 📡 ESP32 Wi‑Fi based sensor communication
* 🚨 Automatic buzzer & LED alerts
* 🤖 Telegram Bot instant notifications
* 📊 Web dashboard for live monitoring
* 🗄️ PostgreSQL database logging
* 🐳 Docker‑based deployment
* 🔐 Environment‑based configuration

---

## 🧠 System Architecture

```
MQ Gas Sensor → ESP32 → FastAPI Backend → PostgreSQL
                                 ↓
                        Web Dashboard + Telegram Bot
```

---

## 🧰 Technology Stack

| Layer    | Technology             |
| -------- | ---------------------- |
| Hardware | ESP32, MQ‑2 / MQ‑5     |
| Firmware | Arduino (C++)          |
| Backend  | Python, FastAPI        |
| Database | PostgreSQL             |
| Alerts   | Telegram Bot API       |
| Frontend | HTML                   |
| DevOps   | Docker, Docker Compose |

---

## 📁 Project Structure

```
Smart-Gas-Leakage-Bot/
│── README.md
│── docker-compose.yml
│── requirements.txt
│── .env.example
│
├── firmware/
│   └── esp32_gas_detector.ino
│
├── backend/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models.py
│   └── telegram_bot.py
│
├── dashboard/
│   └── index.html
│
└── docs/
    └── system_architecture.png
```

---

## 🔌 Hardware Requirements

* ESP32 Development Board
* MQ‑2 or MQ‑5 Gas Sensor
* Active Buzzer
* LED (optional)
* 5V Power Supply

---

## 🔧 ESP32 Firmware Setup

1. Open `firmware/esp32_gas_detector.ino`
2. Update Wi‑Fi credentials
3. Set backend server IP
4. Upload to ESP32 using Arduino IDE

The ESP32 continuously reads gas levels and sends data to the backend every few seconds.

---

## ⚙️ Backend Setup (Local / Server)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Gas-Leakage-Bot.git
cd Smart-Gas-Leakage-Bot
```

### 2️⃣ Configure Environment

```bash
cp .env.example .env
```

Edit `.env`:

```
DATABASE_URL=postgresql://gasuser:gaspass@db/gasdb
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
```

### 3️⃣ Run with Docker

```bash
docker-compose up --build
```

Backend will be available at:

```
http://localhost:8800
```

---

## 🤖 Telegram Bot Alerts

* Create a bot via **@BotFather**
* Copy the bot token
* Get your chat ID
* Add both to `.env`

🚨 When gas exceeds the safe threshold, an **instant Telegram alert** is sent.

---

## 🌐 Web Dashboard

A lightweight web dashboard displays system status and confirms live monitoring.

Access:

```
http://localhost:8800
```

---

## 🐳 Docker Services

* FastAPI backend
* PostgreSQL database

Fully containerized for easy deployment on:

* VPS
* Local server
* Raspberry Pi

---

## 🚀 Deployment Checklist

* [ ] Flash ESP32 firmware
* [ ] Configure `.env`
* [ ] Start Docker containers
* [ ] Verify Telegram alerts
* [ ] Test gas sensor response

---

## 🔮 Future Enhancements

* 📱 Android mobile app
* ☁️ MQTT cloud integration
* 🧠 AI‑based leak prediction
* 📞 SMS & voice call alerts
* 🏭 Industrial multi‑sensor support

---

## 🛡️ License

MIT License

---

## 👨‍💻 Author

**Abdullahi Bundi**

IoT • Embedded Systems • AI • Python • C++

---

⭐ If this project helps you, please **star the repository** and share it!

