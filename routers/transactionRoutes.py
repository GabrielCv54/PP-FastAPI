from fastapi import APIRouter,Request,status
from erros.errors import InsufficientFunds,NegativeBalance,IdNonExists
from database.models import Transaction,Account
from database.db import session
from schemas.schemas import NewTransactionBase
from datetime import datetime

transaction_router = APIRouter(
    prefix='/finance',
    tags=['transactions']
)

@transaction_router.get('/transactions')
async def request_transactions_dashboard():
    transactions = session.query(Transaction).all()
    return [transac.dici() for transac in transactions]

@transaction_router.get('/transactions/{user_id}',status_code=status.HTTP_200_OK)
async def request_transactions_userId():
    pass 

@transaction_router.post('/transactions/perform_transac',status_code=status.HTTP_201_CREATED)
async def request_create_new_Expense(request: NewTransactionBase):
    date = request.date_transaction.date()
    transac = Transaction(value=request.value,description=request.description,date_transaction=date,type_transaction=(request.type_transaction),account_id=request.account_id,user_id=request.user_id)
    account_balance = session.query(Account).filter_by(id=request.account_id).first()
    if not account_balance:
        raise IdNonExists
    if account_balance.balance < request.value:
        raise InsufficientFunds(balance_ammout=account_balance.balance,withdrawal_amount=request.value)
    elif account_balance.balance < 0:
        request.status = 'cancelada'
        raise NegativeBalance
    else:
        account_balance.balance -= request.value
        session.commit()
    session.add(transac)
    session.commit()
    return {"Sucesso":"Transação finalizada com sucesso!!"}