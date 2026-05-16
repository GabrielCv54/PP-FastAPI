from fastapi import APIRouter,status,HTTPException
from database.db import session
from database.models import Category
from schemas.schemas import CategoryBase

category_router = APIRouter(
    prefix='/finance/category',
    tags=['categories'] 
          )

@category_router.get('/')
def request_return_categories():
    categories = session.query(Category).all()
    return [cat.dici() for cat in categories]

@category_router.post('/')
def request_register_category(request: CategoryBase):
     try:
        new_category = Category(type=request.type,description=request.description,limit_value=request.limit_value,status=request.status)
        session.add(new_category)
        session.commit()
     except Exception as err:
         return HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=f'Erro no servidor:{err}')

@category_router.put('/{id}')
def request_update_cateogry_infos(request: CategoryBase):
     pass