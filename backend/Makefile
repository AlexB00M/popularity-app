DC = docker compose
STORAGES_FILE = docker_compose/storages.yaml
EXEC = docker exec -it
DB_CONTAINER = postgres_container
REDIS_CONTAINER = redis_container
LOGS = docker logs
ENV = --env-file .env
APP_FILE = docker_compose/app.yaml
APP_CONTAINER = main-app
MANAGE_PY = python manage.py
MONITORING_FILE = docker_compose/monitoring.yaml
WORKERS_FILE = docker_compose/workers.yaml

.PHONY: storages
storages:
	${DC} -f ${STORAGES_FILE} ${ENV} up -d

.PHONY: storages-down
storages-down:
	${DC} -f ${STORAGES_FILE} down

.PHONY: postgres
postgres:
	${EXEC} ${DB_CONTAINER} psql -U ${POSTGRES_USER}

.PHONY: storage-logs
storage-logs:
	${LOGS} ${DB_CONTAINER} -f

.PHONY: redis-logs
redis-logs:
	${LOGS} ${REDIS_CONTAINER} -f

.PHONY: app
app:
	${DC} -f ${APP_FILE} -f ${STORAGES_FILE} -f ${WORKERS_FILE} ${ENV} up --build -d

.PHONY: workers
workers:
	${DC} -f ${WORKERS_FILE} ${ENV} up --build -d

.PHONY: workers-down
workers-down:
	${DC} -f ${WORKERS_FILE} ${ENV} down

.PHONY: worker-1-logs
worker-1-logs:
	${LOGS} -f worker-1 -f

.PHONY: worker-2-logs
worker-2-logs:
	${LOGS} -f worker-2 -f

.PHONY: monitoring
monitoring:
	${DC} -f ${MONITORING_FILE} ${ENV} up --build -d


.PHONY: monitoring-logs
monitoring-logs:
	${DC} -f ${MONITORING_FILE} ${ENV} logs -f


.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f

.PHONY: db-logs
db-logs:
	${DC} ${ENV} -f ${STORAGES_FILE} logs -f

.PHONY: app-down
app-down:
	${DC} ${ENV} -f ${APP_FILE} -f ${STORAGES_FILE} down

.PHONY: migrate
migrate:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} migrate $(app-name)

.PHONY: migrations
migrations:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} makemigrations $(app-name)

.PHONY: superuser
superuser:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} createsuperuser

.PHONY: collectstatic
collectstatic:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} collectstatic


.PHONY: run-test
run-test:
	${EXEC} ${APP_CONTAINER} pytest

.PHONY: django-console
django-console:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} shell

.PHONY: pip-install
pip-install:
	${EXEC} ${APP_CONTAINER} pip install $(name)

.PHONY: test
test:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} test ${name}

.PHONY: flush
flush:
	${EXEC} ${APP_CONTAINER} ${MANAGE_PY} flush 