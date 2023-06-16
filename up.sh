(sleep 0.1; echo yes; ) | python manage.py collectstatic
python manage.py runserver