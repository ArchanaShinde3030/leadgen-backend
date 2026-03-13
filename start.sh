#!/bin/bash
# Apply migrations first
python manage.py migrate

# Start server
python manage.py runserver 0.0.0.0:7860