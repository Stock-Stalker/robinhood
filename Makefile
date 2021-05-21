-include secrets.mk

build :
				docker-compose build --force-rm --no-cache

start:
				docker-compose up

stop :
				docker-compose down

debug :
				docker-compose --verbose up

reload:
				docker-compose down && docker-composes up

test :
				docker-compose -f docker-compose.test.yml up --abort-on-container-exit

test-security:
				snyk config set api=$(snyk_auth_token) && snyk test --fail-on=upgradable

test-image-security:
				snyk config set api=$(snyk_auth_token) && snyk container test python:3.9 --file=Dockerfile --fail-on=upgradable

reload-test :
				docker-compose down && docker-compose -f docker-compose.test.yml up --abort-on-container-exit

hard-reload-test :
				docker-compose down && docker rmi robinhood_robinhood && docker-compose -f docker-compose.test.yml up --abort-on-container-exit

lint:
				flake8 .

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