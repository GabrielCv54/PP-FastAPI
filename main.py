from fastapi import FastAPI 
from routers.transactionRoutes import transaction_router
from routers.accountRoutes import account_router
from routers.userRoutes import user_router
from erros.errors import FinanceException
from fastapi import Request
from fastapi.responses import JSONResponse

app = FastAPI(title='Finance API',
              description='API de gestão de finanças pessoais',
              version='1.0')

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
    return 'Olá , api Finance está no Ar'

