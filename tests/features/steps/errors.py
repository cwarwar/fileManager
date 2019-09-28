from behave import *
import requests
import json
from random import randint
import constants

@given('Um arquivo inexistente no filesystem')
def step_impl(context):
    context.file = 'nao_existe.txt'

@then('Tente copiar para um diretório e receba um erro')
def step_impl(context):
    payload = {'source' : context.file, 'destination' : '/primeiro/segundo/terceiro'}
    response = requests.post(constants.ENDPOINT+'file/copy', data=payload)
    print(response)
    assert response.json()['success'] is False