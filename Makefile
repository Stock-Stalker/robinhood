-include secrets.mk

build :
				export DOCKER_CONTENT_TRUST=1 && docker compose -f docker-compose.dev.yml build --force-rm --no-cache

start:
				export DOCKER_CONTENT_TRUST=1 && docker compose -f docker-compose.dev.yml up

stop :
				docker compose -f docker-compose.dev.yml down

debug :
				docker compose -f docker-compose.dev.yml --verbose up

reload:
				docker compose -f docker-compose.dev.yml down && docker compose -f docker-compose.dev.yml up

hard-reload:
				docker compose -f docker-compose.dev.yml down && docker rmi robinhood_robinhood && docker compose -f docker-compose.dev.yml up

test :
				docker compose -f docker-compose.test.yml up --abort-on-container-exit

test-security:
				snyk config set api=$(snyk_auth_token) && snyk test --fail-on=upgradable

test-image-security:
				snyk config set api=$(snyk_auth_token) && snyk container test python:3.9 --file=Dockerfile --fail-on=upgradable

reload-test :
				docker compose -f docker-compose.test.yml down && docker compose -f docker-compose.test.yml up --abort-on-container-exit

hard-reload-test :
				docker compose -f docker-compose.test.yml down && docker rmi robinhood_robinhood && docker compose -f docker-compose.test.yml up --abort-on-container-exit

lint:
				flake8 . --extend-exclude env

rm :
				docker container prune -f
				
rm-all:
				docker stop $$(docker ps -aq) && docker rm $$(docker ps -aq)

rmi :
				docker rmi robinhood_robinhood

rmi-all:
				docker rmi $$(docker images -q)
	
purge:
				docker system prune --volumes --all -f