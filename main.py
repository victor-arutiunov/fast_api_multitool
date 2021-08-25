from fastapi import FastAPI


app = FastAPI()


def test_function(param: str):
    '''
    Функция для страдания фигней.
    Для запуска функции напишите следующий код:
        test_function('Страдаем фигней')
    '''
    return param
