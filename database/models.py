from .db import Base
from sqlalchemy import Column,Integer,String,Date,ForeignKey,Float,DateTime,Boolean
from sqlalchemy.orm import relationship
from datetime import date

class User(Base):
    __tablename__  = 'user'
    id = Column('id',Integer, primary_key=True,autoincrement=True)
    name = Column('name',String)
    cpf = Column('cpf',String,unique=True)
    date_nasc = Column('date_nasc',Date)
    email = Column("email",String,unique=True)
    password = Column('password',String)
    transactions = relationship('Transaction',back_populates=('transac_user'))
    is_delete = Column('is_delete',Boolean,default=False)
    
    def __init__(self,name,cpf,date_nasc,email,password,is_delete):
        self.name = name
        self.cpf = cpf
        self.date_nasc = date_nasc
        self.email = email
        self.password = password
        self.is_delete = is_delete
        
    def dici(self):
        return {"id":self.id,"name":self.name,"cpf":self.cpf,"date_nasc":self.date_nasc,"email":self.email,"password":self.password,"transactions_id":[transac.id for transac in self.transactions]}


class Account(Base):
    __tablename__ = 'account'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    type = Column('type',String)
    balance = Column("balance",Float,nullable=False)
    bank = Column('bank',String)
    status = Column('status',String,default='ativa')
    client_id = Column(ForeignKey('user.id'))
    agency_number = Column('num_agency',Integer)
    is_delete = Column('is_delete',Boolean,default=False)

    def __init__(self,type,balance,bank,status,client_id,agency_number,is_delete):
        self.type = type
        self.balance = balance
        self.bank = bank
        self.status = status
        self.client_id = client_id
        self.agency_number = agency_number
        self.is_delete = is_delete

    def dici(self):
        return {"id":self.id,"type":self.type,"balance":self.balance,"bank":self.bank,"status":self.status,"client_id":self.client_id,"agency_number":self.agency_number,'is_delete':self.is_delete}


class Category(Base):
    __tablename__ = 'category'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    type = Column('type',String,nullable=False,unique=True)
    description = Column('description',String,nullable=False)
    limit_value = Column('limit_value',Float,nullable=False)
    status = Column('status',String,nullable=False)
    transactions_list = relationship('Transaction',back_populates="category")
    is_delete = Column('is_delete',Boolean,default=False)

    def __init__(self,type,description,limit_value,status,is_delete):
        self.type = type
        self.description = description
        self.limit_value = limit_value
        self.status = status
        self.is_delete = is_delete

    def dici(self):
        return {'id':self.id,'type':self.type,'description':self.description,'limit_value':self.limit_value,'status':self.status,'is_delete':self.is_delete,'transactions_list':[transac for transac in self.transactions_list]}


class Transaction(Base):
    __tablename__  = 'transaction'
    id = Column('id',Integer,primary_key=True,autoincrement=True)
    description =Column('description',String)
    value = Column('value',Float,nullable=False)
    date_transaction = Column('date_transaction',Date,nullable=False,default=date.today())
    type_transaction = Column('type_transaction',String,nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))
    category_id = Column(Integer,ForeignKey("category.id"),nullable=False)
    transac_user = relationship('User',back_populates='transactions')
    category = relationship("Category",back_populates="transactions_list")
    account_id = Column('account_id',Integer,ForeignKey('account.id'))
    is_delete = Column("is_delete",Boolean,default=False)

    def __init__(self,description, value, date_transaction, user_id,account_id,type_transaction,category_id,is_delete):
        self.description = description
        self.value = value
        self.date_transaction = date_transaction
        self.user_id = user_id
        self.account_id = account_id
        self.type_transaction = type_transaction
        self.category_id = category_id
        self.is_delete = is_delete

    def dici(self):
        return {"description":self.description,"value":self.value,
                "date_transaction":self.date_transaction,'type_transaction':self.type_transaction,"account_id":self.account_id,"user_id":self.user_id,'category_id':self.category_id}