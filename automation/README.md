# Selenium Pytest POM Framework - Automation

This folder contains the automated test suite for the Selenium Practice website.

## Directory Structure
- `automation/configs/`: Configuration management (`config.py`).
- `automation/pages/`: Page Object Model classes.
- `automation/tests/`: Test scripts.
- `automation/conftest.py`: Pytest fixtures and command-line options.

## Environments
The framework supports three environments: `dev`, `qa`, and `prod`.
Each environment has its own `.env` file:
- `.env.dev`
- `.env.qa`
- `.env.prod`

### How to Run Tests
By default, tests run against the **production** environment.

#### Run in Production (Default)
```bash
pytest
```

#### Run in Dev Environment
```bash
pytest --env dev
```

#### Run in QA Environment
```bash
pytest --env qa
```

#### Run with Reporting
```bash
pytest --html=reports/report.html
```

## Configuration Settings
You can modify the following in the `.env.*` files:
- `BASE_URL`: The URL of the environment.
- `BROWSER`: `chrome` or `firefox`.
- `HEADLESS`: `true` or `false`.
- `IMPLICIT_WAIT`: Time in seconds.
- `EXPLICIT_WAIT`: Timeout for element waits.
