from fastapi import FastAPI
from src.routers import travel_route, user_route, auth_route, log_route

app = FastAPI()


#
#
# RUN SERVER python -m uvicorn src.server:app --reload
# RUN TESTS python -m pytest tests
#
#


# Rotas
app.include_router(travel_route.router)
app.include_router(user_route.router)
app.include_router(log_route.router)
app.include_router(auth_route.router, prefix="/auth")
