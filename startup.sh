#!/bin/bash
python -m gunicorn --bind=0.0.0.0 --timeout 600 --workers=4 uvicorn.workers.UvicornWorker app.server.app:app