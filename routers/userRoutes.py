from schemas.schemas import UserResponse,NewUserBase,UserUpdate
from database.models import User
from database.db import session
from fastapi import Request,APIRouter
from erros.errors import IdNonExists

user_router = APIRouter(
      prefix='/finance/users',
      tags=['usuário']
)

@user_router.get('/')
async def request_users():
      users = session.query().all(User)
      return [user.dici for user in users] 

@user_router.get('/{id_user}',response_model=UserResponse)
async def request_user_id(id_user:int):
        try:
            user = session.get(id_user)
            return [user.dici()]
        except:
            raise IdNonExists

@user_router.post('/')
async def request_post_user(request: NewUserBase):
        session.add(request)
        session.commit()
        return {"Sucesso":"Usuário criado com sucesso!!"}

@user_router.put("/{user_id}")
async def request_update_user(request_upd:UserUpdate):
        data_update = session.get(request_upd.id)
        data_update.name = request_upd['name']
        data_update.cpf = request_upd['cpf']
        data_update.data_nasc = request_upd['data_nasc']
        data_update.email = request_upd['email']
        data_update.password = request_upd['password']
        data_update.finances = request_upd['transactions_id']
        session.commit()

@user_router.post('')
async def request_sack_user(id):
      user = session.get(id)