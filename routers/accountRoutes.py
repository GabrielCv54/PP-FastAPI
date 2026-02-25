from fastapi import APIRouter, Request
from schemas.schemas import AccountBase,AccountResponse
from database.models import Account
from database.db import session

account_router = APIRouter(
    prefix='/finance/accounts',
    tags=['conta']
)

@account_router.get("/")
async def request_return_accounts():
    accounts = session.query(Account).all()
    return [accou.dici() for accou in accounts]

@account_router.get("/{id}")
async def request_returnId_accounts():
    pass

@account_router.post('/')
async def request_create_accounts():
    pass
