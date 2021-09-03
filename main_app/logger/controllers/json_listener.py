from fastapi import APIRouter, Body
import json

router = APIRouter(prefix='/listener',)


@router.post('/get_json')
def json_maker(body=Body(...)):
    with open('../logger/jsons/data.json', 'w', encoding='utf-8') as f:
        if type(body) == 'bytes':
            body = body.decode('utf-8')
        json.dump(json.loads(body), f, ensure_ascii=False, indent=4)
    return {'message': 'Create json file'}
