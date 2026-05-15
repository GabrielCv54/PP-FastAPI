from schemas.schemas import UserResponse,NewUserBase,UserUpdate,UserLogin
from database.models import User
from database.db import session
from fastapi import Request,APIRouter,status,HTTPException
from erros.errors import IdNonExists, InvalidPassword, InvalidEmailLogin, UserNotFound
from sqlalchemy import select
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from security.core import verify_password_hash, define_password_hash
from typing import List

user_router = APIRouter(
      prefix='/finance/users',
      tags=['users']
)

@user_router.get('/')
async def request_users():
      users = session.execute(select(User)).scalars().all()
      return [user.dici() for user in users] 

@user_router.get('/users')
async def read_user_profile(request: List[UserResponse]):
      request = session.query(User).all()
      return request

@user_router.post('/register')
async def request_register(request: NewUserBase):
            try:
                  passw = define_password_hash(request.password)
                  user = User(name=request.name,cpf=request.cpf,email=request.email,date_nasc=request.date_nasc,password=passw,is_delete=request.is_delete)
                  session.add(user)
                  session.commit()
                  return {"Sucesso":"Usuário registrado com sucesso"}
            except Exception as erro:
                   raise HTTPException(status_code=erro.status_code,detail=f'Erro durante a requisição:{erro}')

@user_router.post('/login',status_code=status.HTTP_200_OK)
async def request_login(request : UserLogin):
            email = request.email
            password = request.password     
            userDb = session.query(User).filter_by(email=email).first()
            if not userDb:
                  raise InvalidEmailLogin
            if not verify_password_hash(password,userDb.password):
                  raise InvalidPassword
            session.commit()
            return {'sucesso':'login realizado com sucesso'}

@user_router.get('/{id_user}',response_model=UserResponse)
async def request_user_id(id_user:int):
        try:
            user = session.query(User).get(id_user)
            return [user.dici()]
        except:
            raise IdNonExists

@user_router.post('/',status_code=status.HTTP_201_CREATED)
async def request_post_user(request: NewUserBase):
        try:
            passw = define_password_hash(request.password)
            user = User(name=request.name, email=request.email, date_nasc=request.date_nasc, password=passw,cpf=request.cpf)      
            session.add(user)
            session.commit()
            return {"Sucesso":"Usuário criado com sucesso!!"}
        except Exception as erro:
              raise HTTPException(status_code=500,detail=f'Erro no servidor:{erro}')

@user_router.put("/{user_id}",status_code=status.HTTP_201_CREATED)
async def request_update_user(user_id, request_upd: UserUpdate):
        try:
            data_update = session.query(User).get(user_id)
            data_update.name = request_upd.name
            data_update.cpf = request_upd.cpf
            data_update.date_nasc = request_upd.date_nasc
            data_update.email = request_upd.email
            passw = define_password_hash(request_upd.password)
            data_update.password = passw
            #data_update.transactions = request_upd['transactions']
            session.commit()
            return {'sucesso':'Dados atualizados com sucesso!!'}
        except IdNonExists:
            raise HTTPException(status_code=404)

@user_router.delete('/{user_id}',status_code=status.HTTP_204_NO_CONTENT)
async def request_exclude_user(user_id):
      try:
       data_user = session.query(User).get(user_id)
       session.delete(data_user)
       return {'Sucesso':f'Usuário deletado com sucesso'}
      except IdNonExists:
            raise HTTPException(status_code=404,detail=f'Não se pode achar o usuário com id')