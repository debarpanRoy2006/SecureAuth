#!/usr/bin/env bash
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files for production
python manage.py collectstatic --noinput

# Run database migrations
python manage.py migrate --noinput

# Optional: Create superuser if env variable is set
if [ "$CREATE_SUPERUSER" = "true" ]; then
    echo "Creating superuser..."
    python manage.py createsuperuser --noinput || true
fi
