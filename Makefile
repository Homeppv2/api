include .env
export

.PHONY: run-service
run-service:
	poetry run python -m homepp