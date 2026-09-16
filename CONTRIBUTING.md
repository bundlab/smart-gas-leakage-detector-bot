# Contributing to Smart Gas Leakage Detector Bot

Thank you for your interest in contributing to **Smart Gas Leakage Detector Bot**.

This project is an open-source IoT system designed to detect potentially dangerous gas levels using an ESP32 and gas sensors, send readings to a FastAPI backend, store sensor data in PostgreSQL, and provide alerts through Telegram.

Contributions of all kinds are welcome, including bug fixes, documentation improvements, testing, backend improvements, dashboard enhancements, firmware improvements, and new features.

## Table of Contents

* [Code of Conduct](#code-of-conduct)
* [Getting Started](#getting-started)
* [Project Structure](#project-structure)
* [Development Environment](#development-environment)
* [Making Changes](#making-changes)
* [Testing](#testing)
* [Docker Development](#docker-development)
* [Commit Guidelines](#commit-guidelines)
* [Pull Requests](#pull-requests)
* [Issue Guidelines](#issue-guidelines)
* [Security](#security)
* [Questions and Discussions](#questions-and-discussions)
* [License](#license)

## Code of Conduct

Please be respectful, constructive, and professional when participating in this project.

Contributors are expected to:

* Treat other contributors with respect.
* Provide constructive feedback.
* Keep discussions focused on the project.
* Avoid harassment, discrimination, or personal attacks.
* Help maintain an inclusive and welcoming community.

## Getting Started

### 1. Fork the repository

Create your own fork of the repository on GitHub.

### 2. Clone your fork

```bash
git clone https://github.com/bundlab/smart-gas-leakage-detector-bot.git
cd smart-gas-leakage-detector-bot
```

### 3. Add the upstream repository

```bash
git remote add upstream https://github.com/bundlab/smart-gas-leakage-detector-bot.git
```

Verify your remotes:

```bash
git remote -v
```

### 4. Create a feature branch

Avoid making changes directly on `main`.

```bash
git checkout -b feature/your-feature-name
```

Examples:

```bash
git checkout -b feature/gas-alert-cooldown
git checkout -b fix/database-connection
git checkout -b docs/improve-setup-guide
```

## Project Structure

The main project components are organized as follows:

```text
smart-gas-leakage-detector-bot/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── cd.yml
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── telegram_bot.py
├── dashboard/
│   └── index.html
├── docs/
│   └── sys_architecture.png
├── firmware/
│   └── esp32_gas_detector.ino
├── .dockerignore
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

## Development Environment

The backend uses:

* Python 3.10+
* FastAPI
* Uvicorn
* SQLAlchemy
* PostgreSQL
* Requests

The hardware component uses:

* ESP32
* MQ-series gas sensor
* Arduino-compatible firmware

The project also uses:

* Docker
* Docker Compose
* GitHub Actions
* GitHub Container Registry
* Telegram Bot API

## Environment Variables

Create a local `.env` file based on `.env.example`.

Example:

```env
DATABASE_URL=postgresql://gasuser:gaspass@db:5432/gasdb
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID
```

### Important

Never commit `.env` or real credentials to GitHub.

Use `.env.example` when documenting required environment variables.

## Making Changes

Before starting development, make sure your branch is up to date:

```bash
git checkout main
git pull upstream main
```

Create a new branch:

```bash
git checkout -b feature/your-feature-name
```

Make your changes and review them:

```bash
git status
git diff
```

Check for whitespace errors:

```bash
git diff --check
```

## Testing

### Python syntax check

Run:

```bash
python -m compileall backend
```

A successful compilation should complete without syntax errors.

### Run the backend locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI:

```bash
uvicorn backend.main:app --reload --port 8000
```

The API should be available at:

```text
http://localhost:8000
```

FastAPI's interactive API documentation is available at:

```text
http://localhost:8000/docs
```

### Docker testing

Build the image:

```bash
docker build -t smart-gas-leakage-detector-bot .
```

Start the services:

```bash
docker compose up --build
```

The API is exposed on:

```text
http://localhost:8800
```

Stop the services with:

```bash
docker compose down
```

## Docker Development

The Docker Compose environment contains:

```text
ESP32 / Client
      │
      ▼
FastAPI API :8800
      │
      ▼
PostgreSQL
```

The PostgreSQL service is accessible to the API through the Docker network using the service name:

```text
db
```

Contributors should avoid adding unnecessary host port mappings for PostgreSQL unless there is a specific development requirement.

## Commit Guidelines

Use clear, concise, and descriptive commit messages.

Recommended format:

```text
<type>: <short description>
```

Examples:

```text
feat: add gas alert cooldown
fix: handle database connection errors
docs: improve Docker setup instructions
test: add gas reading endpoint tests
refactor: improve Telegram notification handling
ci: update GitHub Actions workflow
```

Common commit types include:

| Type       | Purpose                     |
| ---------- | --------------------------- |
| `feat`     | New functionality           |
| `fix`      | Bug fix                     |
| `docs`     | Documentation               |
| `test`     | Tests                       |
| `refactor` | Code restructuring          |
| `ci`       | CI/CD changes               |
| `build`    | Build or dependency changes |
| `chore`    | Maintenance                 |

## Pull Requests

Before opening a pull request:

1. Make sure your branch contains only the changes relevant to your contribution.
2. Run the available tests and validation checks.
3. Review your changes with `git diff`.
4. Make sure no secrets or `.env` files are included.
5. Update documentation when necessary.
6. Use a clear pull request title.
7. Explain what changed and why.

Push your branch:

```bash
git push origin feature/your-feature-name
```

Then open a pull request against:

```text
bundlab/smart-gas-leakage-detector-bot:main
```

### Pull Request Description

A useful pull request should explain:

```text
## What changed?

Describe the implementation.

## Why?

Explain the problem or feature being addressed.

## Testing

Explain how the changes were tested.

## Additional notes

Include anything reviewers should know.
```

GitHub Actions CI will automatically validate pull requests targeting `main`.

## Issue Guidelines

Before opening a new issue, search existing issues to avoid duplicates.

### Bug Reports

Include:

* A clear description of the problem.
* Steps to reproduce it.
* Expected behavior.
* Actual behavior.
* Relevant logs or error messages.
* Operating system and environment information.
* Docker/Python version when relevant.

Example:

```text
### Description

The API returns an error when submitting a gas reading.

### Steps to reproduce

1. Start the Docker services.
2. Send a POST request to `/api/gas`.
3. Observe the response.

### Expected behavior

The gas reading should be stored successfully.

### Actual behavior

The API returns an error.

### Environment

Ubuntu 24.04
Docker
Python 3.10+
```

### Feature Requests

Explain:

* What you would like to add.
* Why the feature would be useful.
* How you expect it to work.
* Any possible implementation considerations.

## Hardware Contributions

Hardware and firmware contributions should be tested carefully.

When modifying the ESP32 firmware:

* Clearly document hardware requirements.
* Identify sensor pins and GPIO assignments.
* Avoid hard-coding credentials.
* Do not commit Wi-Fi passwords, API credentials, or Telegram tokens.
* Explain any changes to sensor thresholds.
* Consider the effect of repeated network requests.
* Test changes with appropriate hardware before submitting a pull request.

### Safety

This project is intended as a technical and educational IoT project.

Gas detection hardware can involve real safety risks. Software changes should not be presented as a substitute for certified gas detection equipment, professional installation, or applicable safety standards.

Contributors should avoid making claims that the project provides certified life-safety protection.

## Security

Please do not publicly disclose sensitive credentials or security vulnerabilities through regular issues.

Never commit:

```text
.env
API tokens
Telegram bot tokens
Passwords
Private keys
Database credentials
Wi-Fi credentials
```

For security-related concerns, contact the project maintainer through the appropriate private communication channel before publicly disclosing sensitive details.

## Questions and Discussions

For general questions, improvements, ideas, and development discussions, use GitHub Issues or Discussions when available.

When asking for help, provide enough technical context for others to reproduce or understand the problem.

## License

By contributing to this project, you agree that your contributions will be licensed under the same license as the project.

See the repository's `LICENSE` file for the complete license terms.

---

Thank you for contributing to **Smart Gas Leakage Detector Bot**! 🚨
