include .env
export

.PHONY: run-service
run-service:
	poetry run gunicorn homepp.__main__:app --reload --bind 0.0.0.0:8000 \
	--worker-class uvicorn.workers.UvicornWorker \
	--workers 1
