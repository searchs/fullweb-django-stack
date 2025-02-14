.PHONY: run_migration run_makemigrations run_collectstatic run_backend run_frontend 

run_migration:
	@echo "Running migration"
	python manage.py migrate

run_makemigrations:
	@echo "Running makemigrations"
	python manage.py makemigrations

run_collectstatic:
	@echo "Running collectstatic"
	python manage.py collectstatic --noinput

run_backend:
	@echo "Running backend"
	python manage.py runserver

run_frontend:
	@echo "Running frontend"
	cd frontend && npm start
