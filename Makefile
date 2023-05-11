ALEMBIC:=homepp_api/homepp/config/alembic.ini

include .env
export

.PHONY: run-service
run-service:
	poetry run python -m homepp

.PHONY: migrate-up
migrate-up:
	poetry run alembic -c $(ALEMBIC) upgrade head

.PHONY: migrate-down
migrate-down:
	poetry run alembic -c $(ALEMBIC) downgrade $(revision)

.PHONY: migrate-create
migrate-create:
	poetry run alembic -c $(ALEMBIC) revision --autogenerate -m $(name)

.PHONY: migrate-history
migrate-history:
	poetry run alembic -c $(ALEMBIC) history

.PHONY: migrate-stamp
migrate-stamp:
	poetry run alembic -c $(ALEMBIC) stamp $(revision)