from pydantic import BaseModel, Field, field_validator,ConfigDict
from typing import Optional,List
from datetime import datetime,date
from decimal import Decimal
from enum import Enum
from random import randint
from erros.errors import InvalidPassword
from fastapi import Form


# Classes Base de Transação
class TransactionBase(BaseModel):
    value: Decimal 

class TransactionStatus(str, Enum):
    APPROVED = "aprovada"
    CANCELED = "cancelada"
    PENDING = "pendente"

class TransactionType(str, Enum):
    CARD = 'cartão'
    MONEY = 'dinheiro em espécie'
    PIX = 'pix'

class NewTransactionBase(TransactionBase):
    date_transaction: datetime
    description: str 
    type_transaction: TransactionType
    status: Optional[TransactionStatus] = None
    value: float
    user_id: int
    category_id: int
    account_id: int
    @field_validator('date_transaction')
    @classmethod
    def future_date_invalid(cls, fut: datetime):
        if fut and fut > datetime.now():
            raise ValueError('A data da transação deve ser atual!!')
        return fut

class TransactionResponse(TransactionBase):
    id: int
    model_config = {
        "from_attributes": True
    }



# Classes Base de Usuário
class UserBase(BaseModel):
    name: str = Field(min_length=2)
    date_nasc: date
    email : str = Field(...,max_length=50)
    cpf: str = Field(None,max_length=11)
    password: str = Field(...,min_length=8,max_length=72)
    is_delete: Optional[bool]  

class NewUserBase(UserBase):
    cpf: str = Field(...,min_length=11,max_length=11)
    transactions: List[TransactionResponse] = []

class UserLogin(UserBase):
    email: str = Form(...,max_length=50)
    password: str = Form(...,min_length=8)
    @field_validator('password')
    @classmethod
    def validate_passw(cls, passw):
        if len(passw) > 8:
            return passw
        raise InvalidPassword

class UserUpdate(UserBase):
    name: Optional[str] = Field(None)
    date_nasc: Optional[date] = Field(None)
    email: Optional[str] = Field(None)
    cpf: Optional[str] = Field(None, max_length=11)
    password : Optional[str] = Field(None,min_length=8,max_length=72)

class UserResponse(UserBase):
    id : int 
    active: bool
    model_config = ConfigDict(from_attributes=True)
    @field_validator('id')
    @classmethod
    def validate_id(cls, id):
        if not id:
            raise ValueError("Esse id de usuário não está cadastrado no sistema!!")
        return id



#  Classes Base de Conta
class AccountType(str, Enum):
    CHECKING = "corrente"
    SAVINGS = "poupança"
    INVESTIMENT = "investimento"

class AccountStatus(str, Enum):
    ACTIVE = "ativa"
    INACTIVE = "inativa"
    BLOCKED = 'bloqueada'

class AccountBase(BaseModel):
    balance: Decimal = Field(le=10000)
    type: AccountType
    bank: str = Field(...,min_length=2)
    status: AccountStatus
    client_id: int

class AccountResponse(AccountBase):
    id: int
    model_config = {
        "from_attributes": True
    }

class NewAccountBase(AccountBase):
    balance: Decimal = Field(...)
    agency_number : int = Field(randint(0,500))
    bank: str = Field(...,min_length=2)



# Classes Base de Categoria
class CategoryStatus(str,Enum):
    INPUT = 'entrada'
    OUTPUT = 'saída'

class CategoryBase(BaseModel):
    type: str  = Field(...,min_length=5,max_length=50)
    limit_value: float
    description: str = Field(...,max_length=50)
    status: CategoryStatus

class NewCategoryBase(CategoryBase):
    pass