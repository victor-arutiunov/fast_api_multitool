from fastapi import APIRouter

router = APIRouter(prefix='/getJSON')


@router.middleware('/')
def index():
    print('Incoming transmission')
