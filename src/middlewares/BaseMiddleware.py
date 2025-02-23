from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.base import BaseHTTPMiddleware


# @app.middleware('http')
# def middleware(request: Request, call_next):
#   # print(request.get('headers'))
#   response = call_next(request)
#   return response

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers['Custom'] = 'Example'
        return response
