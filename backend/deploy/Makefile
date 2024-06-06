DOCKER = docker
AWS = aws
TRFM = terraform

CONTAINER_NAME = legal-lab

all: tag-login-push

create-ecr-repo:
	aws ecr create-repository --repository-name $(CONTAINER_NAME) --image-scanning-configuration scanOnPush=true

tag-login-push:
	$(DOCKER) tag $(CONTAINER_NAME):latest 981982666546.dkr.ecr.eu-central-1.amazonaws.com/$(CONTAINER_NAME):latest
	$(AWS) ecr get-login-password | $(DOCKER) login --username AWS --password-stdin 981982666546.dkr.ecr.eu-central-1.amazonaws.com
	$(DOCKER) push 981982666546.dkr.ecr.eu-central-1.amazonaws.com/$(CONTAINER_NAME):latest

push-image-ecr:
	$(DOCKER) push 981982666546.dkr.ecr.eu-central-1.amazonaws.com/$(CONTAINER_NAME):latest
