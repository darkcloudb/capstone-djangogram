web: gunicorn config.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinuput
manage.py migrate