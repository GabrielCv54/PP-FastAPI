from fastapi import APIRouter, Request,status
from schemas.schemas import AccountBase,AccountResponse,NewAccountBase
from database.models import Account
from database.db import session
from erros.errors import AccountNotFound

account_router = APIRouter(
    prefix='/finance/accounts',
    tags=['accounts']
)

@account_router.get("/")
async def request_return_accounts():
    accounts = session.query(Account).all()
    return [accou.dici() for accou in accounts]

@account_router.get("/{bank}")
async def request_returnBank_accounts(request: AccountBase):
    acc = session.query(Account).filter_by(bank=request.bank)
    return list(acc)

@account_router.post('/',status_code=status.HTTP_201_CREATED)
async def request_create_accounts(request: NewAccountBase):
    try:
        account = Account(type=request.type, balance=request.balance, status=request.status, agency_number=request.agency_number, client_id=request.client_id,bank=request.bank)
        session.add(account)
        session.commit()
        return {'Sucesso':'A conta foi criada com sucesso!!'}
    except:
        raise {"Erro": AccountNotFound}