
# Just Travel 

Construir uma API de uma calculadora.


## Stack utilizada

**Back-end:** Python, FastApi, SQLAlchemy, alembic, pydantic, uvicorn, psycopg2


## Design Patterns

- Repositories - persistencia de dados
- Arquitetura de 3 camadas - persistencia de dados
- ORM - facilidade de manipulacao de queries
- Models - facilidade de uso com os outros design patterns



## Instalação

- Clone o repositorio

```bash
  git clone git@github.com:Syngon/just_travel.git
  cd just_travel
```
- Faca a build do docker

```bash
  docker-compose build
```

- Faca as migrations dentro do container

```bash
  docker-compose run web alembic revision --autogenerate -m "migration1"
```

- Execute o container

```bash
  docker-compose up
```


## Documentação da API

### AUTH

#### Registra usuario

```http
  POST /auth/signup
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `username` | `string` | **Obrigatório**. Nome do usuario |
| `password` | `string` | **Obrigatório**. Senha do usuario |

#### Retorn token

```http
  POST /auth/token
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `username` | `string` | **Obrigatório**. Nome do usuario |
| `password` | `string` | **Obrigatório**. Senha do usuario |



### User 

#### Lista travels do usuario

```http
  GET /user/{user_id}/travels
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `user_id` | `int` | **Obrigatório**. ID do usuario |

#### Retorn usuario

```http
  GET /user/{user_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `user_id` | `int` | **Obrigatório**. ID do usuario |



### Travels 

#### Registra travel

```http
  POST /travel
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `user_id` | `int` | **Obrigatório**. ID do usuario |
| `name` | `string` | **Obrigatório**. Nome da travel |
| `place` | `string` | **Obrigatório**. Lugar da travel |
| `price` | `float` | **Obrigatório**. Preco inicial |

#### Retorn travel

```http
  GET /travel/{travel_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `travel_id` | `int` | **Obrigatório**. ID da travel |


#### Registra travel

```http
  PUT /travel/{travel_id}
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `action` | `string` | **Obrigatório**. Acao do calculo |
| `price` | `float` | **Obrigatório**. Preco para usar no calculo |


#### Delete travel

```http
  DELETE /travel/{travel_id}
```

| Parâmetro   | Tipo       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `travel_id` | `int` | **Obrigatório**. ID da travel |