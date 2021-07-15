DESCRIPTION:
This a service alow us to know top committer, how many commits in a month of a github repository

REQUIREMENT:
- docker

DEPLOY:
- add your personal github token to docker-compose.yml at line 45
- docker-compose build
- docker-compose up -d
- docker exec -it grab_api_1 bash
- cd round1
- npm start
- access localhost:3000
