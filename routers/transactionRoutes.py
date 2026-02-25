from fastapi import APIRouter,Request
from erros.errors import InsufficientFunds

transaction_router = APIRouter(
    prefix='/finance/expenses',
    tags=['transação']
)

@transaction_router.get('/')
async def request_return_expenses():
    pass

@transaction_router.post('/create_expense')
async def request_create_new_Expense(value:float, balance_value:float):
    if value > balance_value:
        raise InsufficientFunds(balance_ammout=balance_value,withdrawal_amount=value)
    return {"Sucesso":"Despesa criada com sucesso!!"}