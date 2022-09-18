from fastapi import FastAPI, Request, BackgroundTasks
#from src.routers import travel_route, action_route, user_route, auth_route
from src.routers import auth_route
from src.services.write_notification import write_notification

app = FastAPI()
# uvicorn src.server:app --reload 
# --reload-dir=src




# Rotas Travels
#app.include_router(travel_route.router)

# Rotas Users
#app.include_router(user_route.router)

# Rotas SEGURANÇA: Autenticação e Autorização
app.include_router(auth_route.router, prefix="/auth")

# Rotas Actions
#app.include_router(action_route.router)


@app.post('/log/')
def log(user_id: int, travel_id: int, action: str, value: float, background: BackgroundTasks):
    background.add_task(write_notification,
                        user_id=user_id, travel_id=travel_id, action=action, value=value)
    return {'OK': 'Mensagem enviada'}



# Middlewares
#@app.middleware('http')
#async def validate_sql_injection(request: Request, next):
#    # TODO - Implementar validação de SQL Injection
#    return await next(request)
