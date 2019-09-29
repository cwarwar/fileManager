from behave import *
import requests
import json
from random import randint
import constants

@given('Um arquivo inexistente (nao_existe.txt) no filesystem')
def step_impl(context):
    context.file = 'nao_existe.txt'

@then('Tente copiar para um diretório e receba um erro')
def step_impl(context):
    payload = {'source' : context.file, 'destination' : '/primeiro/segundo/terceiro'}
    response = requests.post(constants.ENDPOINT+'file/copy', data=payload)
    assert response.json()['success'] is False

@given('Um arquivo inexistente (nao_existe_2.txt) no filesystem')
def step_impl(context):
    context.file = 'nao_existe_2.txt'

@then('Tente apagar e receba um erro')
def step_impl(context):
    payload = {'source' : context.file}
    response = requests.post(constants.ENDPOINT+'file/delete', data=payload)
    assert response.json()['success'] is False

@given('Um arquivo inexistente (nao_existe_3.txt) no filesystem')
def step_impl(context):
    context.file = 'nao_existe_3.txt'

@then('Tente gerar o checksum e receba um erro')
def step_impl(context):
    payload = {'source' : context.file}
    response = requests.post(constants.ENDPOINT+'file/checksum', data=payload)
    assert response.json()['success'] is False