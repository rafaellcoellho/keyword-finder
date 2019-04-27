# Keyword Finder 

Uma api que recebe uma palavra e uma lista de urls e retorna o número de ocorrencias daquela palavra em cada url.

## Tecnologias 

* python 3.6
* [aiohttp](https://aiohttp.readthedocs.io/en/stable/index.html)
* [aiohttp-devtools](https://github.com/aio-libs/aiohttp-devtools)
* [aiohttp-swagger](https://github.com/cr0hn/aiohttp-swagger)
* [aioredis](https://github.com/aio-libs/aioredis/)

## Pré-requisitos

* pipenv - [como instalar](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)
* redis - [como instalar no fedora](https://computingforgeeks.com/how-to-install-redis-on-fedora-29-fedora-28/), [como instalar usando source code](https://redis.io/download)
 
## Como usar

Após clonar o repositório, instalar as dependências:

```bash
$ pipenv install --dev
```

Para rodar em desenvolvimento basta dar um: 

```bash
$ pipenv run dev
```

Em modo de desenvolvimento é possível ver a documentação indo em __localhost:8000/docs__. 

<p align="center">
	<a href="">
		<img alt="docs" src="docs/imgs/01.png" width="600px">
	</a>
</p>

## Autor 

* **Rafael Coelho** - [rafaellcoellho](https://github.com/rafaellcoellho)
