import sys
import logging

sys.path.insert(0, "/var/www/flask-app")
sys.path.insert(0, "/var/www/flask-app/venv/lib/python3.11/site-packages/")

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

from app import app as applcation
