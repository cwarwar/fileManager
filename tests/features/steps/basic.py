from behave import *
import requests
import json
from random import randint
import constants

@given('Um arquivo existente no filesystem')
def step_impl(context):
    context.file = '1.txt'

@then('Copie para um diretório existente com sucesso')
def step_impl(context):
    payload = {'source' : context.file, 'destination' : '/primeiro/segundo/terceiro'}
    response = requests.post(constants.ENDPOINT+'file/copy', data=payload)
    assert response.json()['success'] is True

@given('Um arquivo existente no filesystem 1')
def step_impl(context):
    context.file = '1.txt'

@then('Copie para um diretório inexistente com sucesso')
def step_impl(context):
    context.randDirectory = randint(0,1000)
    payload = {'source' : context.file, 'destination' : '/'+str(context.randDirectory)}
    response = requests.post(constants.ENDPOINT+'file/copy', data=payload)
    assert response.json()['success'] is True

@given('Pegue o arquivo copiado do primeiro passo')
def step_impl(context):
    context.file = '/primeiro/segundo/terceiro/1.txt'

@then('Apague-o')
def step_impl(context):
    payload = {'source' : context.file}
    response = requests.post(constants.ENDPOINT+'file/delete', data=payload)
    assert response.json()['success'] is True

@given('Pegue um arquivo qualquer no filesystem')
def step_impl(context):
    context.file = '1.txt'

@then('Gere o checksum')
def step_impl(context):
    payload = {'source' : context.file}
    response = requests.post(constants.ENDPOINT+'file/checksum', data=payload)
    assert response.json()['success'] is True