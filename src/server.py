from fastapi import FastAPI, BackgroundTasks
from src.schemas.schemas import LogData

from src.routers import travel_route, user_route, auth_route
from src.services.write_notification import write_notification

app = FastAPI()


#
#
# RUN SERVER python -m uvicorn src.server:app --reload
# TODO README
# RUN TESTS python -m pytest tests
#
#


# Rotas Travels
app.include_router(travel_route.router)

# Rotas Users
app.include_router(user_route.router)

# Rotas SEGURANÇA: Autenticação e Autorização
app.include_router(auth_route.router, prefix="/auth")

# Rotas Actions
# app.include_router(action_route.router)


@app.post("/log/")
def log(json_log: LogData, background: BackgroundTasks):

    data_is_correct = check_data_types(json_log)

    if not data_is_correct:
        return {"Error": "Data is incorrect"}

    background.add_task(
        write_notification,
        user_id=json_log.user_id,
        travel_id=json_log.travel_id,
        action=json_log.action,
        value=json_log.value,
    )
    return {"OK": "Mensagem enviada"}


def check_data_types(json_log: LogData):
    if not isinstance(json_log.user_id, int):
        return False
    if not isinstance(json_log.travel_id, int):
        return False
    if not isinstance(json_log.action, str):
        return False
    if not isinstance(json_log.value, int):
        return False
    return True


# Middlewares
# @app.middleware('http')
# async def validate_sql_injection(request: Request, next):
#    # TODO - Implementar validação de SQL Injection
#    return await next(request)
