#!/bin/sh
exec gunicorn --bind :5000 --workers 1 --threads 4 --timeout 0 app:app