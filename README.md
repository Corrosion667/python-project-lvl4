# Task manager

[![Maintainability](https://api.codeclimate.com/v1/badges/d980190b8c72057a5ed0/maintainability)](https://codeclimate.com/github/Corrosion667/python-project-lvl4/maintainability)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![linter-and-test-check](https://github.com/Corrosion667/python-project-lvl4/actions/workflows/linter-and-test-check.yml/badge.svg)](https://github.com/Corrosion667/python-project-lvl4/actions/workflows/linter-and-test-check.yml)
[![Test Coverage](https://api.codeclimate.com/v1/badges/d980190b8c72057a5ed0/test_coverage)](https://codeclimate.com/github/Corrosion667/python-project-lvl4/test_coverage)

---

## Basic information

**Task manager** allows setting tasks, assigning performers and changing their statuses. Registration and authentication are required to work with the system.

## Deployment

**Task manager** is also deployed on **Heroku**, so feel free to register and make experiments with it:

[![Heroku](https://pyheroku-badge.herokuapp.com/?app=task-manager-artem&style=flat)](https://task-manager-artem.herokuapp.com)

All possible errors and bugs will be sent to **Rollbar** automatically and fixed as soon as possible.

## Running

The easiest way to run this bot is to use official ***Docker image***.  
You only need to specify **django secret key** (the one you like) and **port** *(e.g. 8000)*. Run task manager with the following command:
```bash
docker run -d --env DJANGO_SECRET_KEY=<YOUR_KEY> -p 8000:8000 corrosion667/task-manager
```
**Task manager** will be available in browser at `http://0.0.0.0:8000/`  
You may encounter some problems with *Safari*, so use another browser or open `http://localhost:8000`