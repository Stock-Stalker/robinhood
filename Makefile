-include secrets.mk

build :
				docker-compose -f docker-compose.dev.yml build --force-rm --no-cache

start:
				docker-compose -f docker-compose.dev.yml up

stop :
				docker-compose down

debug :
				docker-compose -f docker-compose.dev.yml --verbose up

reload:
				docker-compose down && docker-compose -f docker-compose.dev.yml up

test :
				docker-compose -f docker-compose.test.yml up --abort-on-container-exit

test-security:
				snyk config set api=$(snyk_auth_token) && snyk test

reload-test :
				docker-compose down && docker-compose -f docker-compose.test.yml up --abort-on-container-exit

hard-reload-test :
				docker-compose down && docker rmi robinhood_robinhood && docker-compose -f docker-compose.test.yml up --abort-on-container-exit

start-prod :
				docker-compose up -d

debug-prod:
				docker-compose --verbose up

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