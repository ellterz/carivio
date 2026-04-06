#!/bin/bash
gunicorn carivio.wsgi:application --bind 0.0.0.0:8000