gunicorn -w 4 -k --bind=0.0.0.0 --timeout 600 uvicorn.workers.UvicornWorker 
app.server.app:app