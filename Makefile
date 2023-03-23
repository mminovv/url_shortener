all:
	@echo "make up			- Create & setup development"
	@echo "make lint		- Format code"
	@echo "make exec		- Connect web container"
	@echo "make migrations		- Create migrations files"
	@echo "make migrate		- Migrate migrations files"
	@echo "make restart		- Restart web container"
	@echo "make static		- Collect static"
	@exit 0
up:
	docker-compose up -d --no-deps --build
logs:
	docker logs --follow --tail 20 --timestamps shortener_web
exec:
	docker exec -it shortener_web bash
migrations:
	docker exec -it shortener_web python manage.py makemigrations
migrate:
	docker exec -it shortener_web python manage.py migrate
restart:
	docker restart shortener_web
lint:
	black shortener/ && flake8 --ignore=E501 --exclude=venv,docs .
static:
	docker exec -it shortener_web python manage.py collectstatic