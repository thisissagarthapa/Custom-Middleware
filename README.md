# Django Middleware Project

This project demonstrates how to create and implement custom middleware in Django, including template response handling, exception handling, and process view hooks. The project also includes basic views and URL configurations for handling requests.

## Features

- **Custom Middleware Implementation**: Includes examples of custom middleware with hooks like `__call__` and `process_view`.
- **Template Response Middleware**: Intercepts the template response and modifies the context data.
- **Exception Handling Middleware**: Catches exceptions during request processing and returns custom responses.
- **Basic Views and Templates**: Shows how to create basic views and templates using Django's `TemplateResponse`.

## Project Setup

### Prerequisites

Make sure you have Django 5.1.4 or above installed. You can install Django via pip:

```bash
pip install django
