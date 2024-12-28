from fastapi import FastAPI, Request, HTTPException
from schemas import SpecialtyChoices, Company
from src.routes import UserRouter, AuthRouter
from src.middlewares.BaseMiddleware import CustomHeaderMiddleware

app = FastAPI()

# @app.middleware('http')
# def middleware(request: Request, call_next):
#   # print(request.get('headers'))
#   response = call_next(request)
#   return response

app.include_router(UserRouter)
app.include_router(AuthRouter)
app.add_middleware(CustomHeaderMiddleware)

COMPANIES = [
  {'id':1 , 'name':'Julies', 'specialty':'Pastries'},
  {'id':2 , 'name':'DOMAIN', 'specialty':'Netcafe'},
  {'id':3 , 'name':'TNC', 'specialty':'Netcafe', 
    'branches':[{ 'address':'11 Pelaez St, Cebu City, 6000 Cebu', 'contactNo':'(032) 266 1810'}]
  },
  {'id':4 , 'name':'Grafik9', 'specialty':'Printing'},
]

@app.get('/')
async def index() -> dict[str, str]:
  return {'hello':'world'}

@app.get('/companies')
async def companies() -> list[Company]:
  return [
    Company(**c) for c in COMPANIES
  ]

@app.get('/companies/{id}')
async def company(id: int) -> Company:
  company = next((Company(**c) for c in COMPANIES if c['id'] == id), None)
  if company == None:
    raise HTTPException(status_code=404, detail='company not found')
  return company

@app.get('/companies/specialty/{specialty}')
async def companies_in_specialty(specialty: SpecialtyChoices) -> list[dict]:
  return[
    c for c in COMPANIES if c['specialty'].lower() == specialty.value
  ]