#!/bin/bash

# Optional: Wait for postgres to be ready
echo "Waiting for postgres..."
sleep 3 

# Initialize and run migrations
flask db init || true  # '|| true' ignores error if already initialized
flask db migrate -m "Initial migration"
flask db upgrade

# Start the Flask app

exec gunicorn --bind 0.0.0.0:80 "app:create_app()"