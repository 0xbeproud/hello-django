#!/usr/bin/env bash

celery -A djangoapi beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler