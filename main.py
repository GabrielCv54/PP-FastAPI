from fastapi import FastAPI 
from routers.transactionRoutes import transaction_router
from routers.accountRoutes import account_router
from routers.userRoutes import user_router
from erros.errors import FinanceException
from fastapi import Request
from fastapi.responses import JSONResponse
from database.models import Base
from database.db import engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title='Finance API',
              description='API de gestão de finanças pessoais',
              version='1.0')


origins = [
    'http://localhost',
    'http://localhost:5500',
    'http://127.0.0.1:8000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(transaction_router)
app.include_router(account_router)
app.include_router(user_router)


@app.exception_handler(FinanceException)
async def finance_exception_handler(request: Request, exc: FinanceException):
    return JSONResponse(status_code=exc.status_code,
                        content={
                            "error_type": exc.__class__.__name__,
                            "message":exc.message_error,
                            "path":  request.url.path
                        })
@app.get('/')
async def request_home():
    return{"Mensagem":'Olá , api Finance está no Ar'}

Base.metadata.create_all(bind=engine)
