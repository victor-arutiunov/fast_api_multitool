from fastapi import APIRouter, Body

router = APIRouter(prefix='/listener')


@router.post('/console_log')
def console_log_print(body=Body(...)):
    print(body)
