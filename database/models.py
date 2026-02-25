from .db import Base
from sqlalchemy import Column,Integer,String,Date,ForeignKey,Float,DateTime,ARRAY
from sqlalchemy.orm import mapped_column,Mapped,relationship


class User(Base):
    __tablename__  = 'user'
    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String)
    cpf = Column('cpf',String)
    data_nasc = Column('date_nasc',Date)
    email = Column("email",String)
    password = Column('password',String)
    transactions_id = mapped_column('transactions_id',ForeignKey('transaction.id'))
    
    def __init__(self,name,cpf,data_nasc,email,password):
        self.name = name
        self.cpf = cpf
        self.data_nasc = data_nasc
        self.email = email
        self.password = password

    def dici(self):
        return {"name":self.name,"cpf":self.cpf,"data_nasc":self.data_nasc,"email":self.email,'password':self.password}


class Account(Base):
    __tablename__ = 'account'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    type = Column('type',String)
    balance = Column("balance",Float,nullable=False)
    bank = Column('bank',String)
    status = Column('status',String)
    client_id : Mapped[int] = mapped_column(ForeignKey('user.id'))
    agency_number = Column('num_agency',Integer)

    def __init__(self,type,balance,status,client_id,agency_number):
        self.type = type
        self.balance = balance
        self.status = status
        self.client_id = client_id
        self.agency_number = agency_number

    def dici(self):
        return {"type":self.type,"balance":self.balance,"bank":self.bank,"status":self.status,"client_id":self.client_id,"agency_number":self.agency_number}


class Category(Base):
    __tablename__ = 'category'
    id = Column('id',primary_key=True,autoincrement=True)
    description = Column('descricao',nullable=False)
    #transactions_id = Column('transactions',ARRAY)


class Transaction(Base):
    __tablename__  = 'transaction'
    id = Column('id',primary_key=True,autoincrement=True)
    description =Column('descricao',String)
    value = Column('valor',Float,nullable=False)
    date_value = Column('data_transacao',DateTime)
    type_transac = Column('tipo_transacao',String,nullable=False)
    account_id = mapped_column('id_conta',ForeignKey('account.id'))