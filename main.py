from fastapi import FastAPI, Request, HTTPException
from src.schemas.schemas import SpecialtyChoices, Company
from src.routes import UserRouter, AuthRouter, CompanyRouter, BusinessRouter
from src.middlewares.BaseMiddleware import CustomHeaderMiddleware

app = FastAPI()

# @app.middleware('http')
# def middleware(request: Request, call_next):
#   # print(request.get('headers'))
#   response = call_next(request)
#   return response

app.include_router(UserRouter)
app.include_router(AuthRouter)
# app.include_router(CompanyRouter)
app.include_router(BusinessRouter)
app.add_middleware(CustomHeaderMiddleware)

@app.get('/')
async def index() -> dict[str, str]:
  return {'hello':'world'}