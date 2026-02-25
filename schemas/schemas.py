from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Optional
from datetime import datetime
from decimal import Decimal
from enum import Enum
from random import randint


# Classes Base de Transação
class TransactionBase(BaseModel):
    total: Decimal = Field(...)

class TransactionStatus(str, Enum):
    APPROVED = "Aprovada"
    CANCELED = "Cancelada"
    PENDING = "Pendente"

class NewTransactionBase(TransactionBase):
    date_transaction: Optional[datetime] = None
    type__trans: str = Field()
    status: TransactionStatus

    @field_validator('date_transaction')
    @classmethod
    def future_date_invalid(cls, fut: datetime):
        if fut > datetime.now():
            return 'A data da transação deve ser atual!!'

class TransactionResponse(TransactionBase):
    id: int
    model_config = {
        "from_attributes": True
    }

# Classes Base de Usuário
class UserBase(BaseModel):
    name: str = Field(min_length=4)
    data_nasc: Optional[datetime] = None
    email : str = Field(...,max_length=20)
    transactions_id: list[TransactionResponse] = []

    @field_validator("transactions_id")
    @classmethod
    def validate_transactions_id(cls, transact_id):
        if not transact_id:
            raise ValueError("Transação não foi feita ou o id dela não foi encontrado!!")
        return transact_id
        
class NewUserBase(UserBase):
    cpf: str = Field(...,min_length=11,max_length=11)
    password: str = Field(...,min_length=8)

    @field_validator('cpf')
    @classmethod
    def validate_cpf(cls,cpf):
        if cpf:
             return f"CPF {cpf} válido! "
        raise "CPF com tamanho inválido! O CPF precisa ter 11 caracteres!"

class UserUpdate(UserBase):
    name: Optional[str] = Field(None)
    data_nasc: Optional[datetime] = Field(None)
    email: Optional[str] = Field(None)
    cpf: Optional[str] = Field(None, max_length=11)
    password : Optional[str] = Field(None,min_length=8)

class UserResponse(UserBase):
    id : int 
    active: bool
    model_config = {
        'from_attributes': True
    }

    
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
    balance: Decimal = Field()
    type: AccountType
    bank: str = Field(...,min_length=2)
    status: AccountStatus

class AccountResponse(AccountBase):
    id: int
    model_config = {
        "from_attributes": True
    }


# Classes Base de Categoria
class CategoryBase(BaseModel):
    pass

class CategoryStatus(CategoryBase):
    pass