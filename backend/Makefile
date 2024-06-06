include .env
export

ENV_FILE = .env
PIP = pip3
PYTHON = python3
DOCKER = docker

CONTAINER_NAME = $(SERVICE_NAME)
LAMBDA_URL = http://localhost:9000/2015-03-31/functions/function/invocations
PAYLOAD_COMPLETION = { "resource":"completion", "payload": { "context":"Sou Brasileiro.", "question":"Quanto imposto tenho que pagar sobre rendimentos de renda fixa?" }}
PAYLOAD_TEMPLATE = { "resource":"template", "payload": { "template":"contrato de compra e venda", "context":"Imovel em Belo Horizonte, Valor: 1.000.000,00 reais" }}
PAYLOAD_COMPARE = { "resource":"compare", "payload":{ "text1":"Imovel em Belo Horizonte, MG. Valor: 4.000.000,00 euros. E mais alguma coisa.", "text2":"Imovel em Belo Horizonte, Valor: 1.000.000,00 reais" }}

all: docker-build

docker-build:
	echo "--- building docker image"
	$(DOCKER) build -t $(CONTAINER_NAME) .

docker-rm:
	echo "--- stopping/removing docker container"
	if [ "$$($(DOCKER) ps -q -f name=$(CONTAINER_NAME))" ]; then $(DOCKER) stop $(CONTAINER_NAME); fi
	if [ "$$($(DOCKER) ps -a -q -f name=$(CONTAINER_NAME))" ]; then $(DOCKER) rm $(CONTAINER_NAME); fi

docker-run: docker-build docker-rm
	echo "--- running docker image"
	$(DOCKER) run -d -p 9000:8080 --env-file $(ENV_FILE) --name=$(CONTAINER_NAME) $(CONTAINER_NAME)

call-completion:
	echo "--- calling lambda function"
	curl -v '$(LAMBDA_URL)' --json '$(PAYLOAD_COMPLETION)'

call-template:
	echo "--- calling lambda function"
	curl -v '$(LAMBDA_URL)' --json '$(PAYLOAD_TEMPLATE)'

call-compare:
	echo "--- calling lambda function"
	curl -v '$(LAMBDA_URL)' --json '$(PAYLOAD_COMPARE)'
