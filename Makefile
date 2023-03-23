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
	docker-compose up --build -d
logs:
	docker logs --follow --timestamps shortener_web
exec:
	docker exec -it shortener_web bash
migrations:
	docker exec -it shortener_web python manage.py makemigrations
migrate:
	docker exec -it shortener_web python manage.py migrate
restart:
	docker restart shortener_web
lint:
	docker exec -it shortener_web black .
static:
	docker exec -it shortener_web python manage.py collectstatic