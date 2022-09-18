from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
#from src.routers import travel_route, action_route, user_route, auth_route
from src.services.write_notification import write_notification

app = FastAPI()
# uvicorn src.server:app --reload --reload-dir=src

# CORS
origins = ['http://localhost:3000',
           'https://myapp.host.com']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)


# Rotas Travels
#app.include_router(travel_route.router)

# Rotas Users
#app.include_router(user_route.router)

# Rotas SEGURANÇA: Autenticação e Autorização
#app.include_router(auth_route.router, prefix="/auth")

# Rotas Actions
#app.include_router(action_route.router)


@app.post('/log/')
def log(user_id: int, travel_id: int, action: str, value: float, background: BackgroundTasks):
    background.add_task(write_notification,
                        msg, 'Olá tudo bem?!')
    return {'OK': 'Mensagem enviada'}



# Middlewares
@app.middleware('http')
async def validate_sql_injection(request: Request, next):
    # TODO - Implementar validação de SQL Injection
    return await next(request)
