from behave import *
import requests
from shutil import copyfile, move
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

@given('Gerando um arquivo no filesystem')
def step_impl(context):
    copyfile('/app/filesystem/1.txt', '/app/filesystem/2.txt')
    context.file = '2.txt'

@then('Mova para um diretório existente com sucesso')
def step_impl(context):
    payload = {'source' : context.file, 'destination' : '/primeiro/segundo/terceiro'}
    response = requests.post(constants.ENDPOINT+'file/move', data=payload)
    assert response.json()['success'] is True

@given('Gerando um arquivo (2.txt) no filesystem')
def step_impl(context):
    copyfile('/app/filesystem/1.txt', '/app/filesystem/2.txt')
    context.file = '2.txt'

@then('Mova para um diretório inexistente com sucesso')
def step_impl(context):
    context.randDirectory = randint(0,1000)
    payload = {'source' : context.file, 'destination' : '/'+str(context.randDirectory)}
    response = requests.post(constants.ENDPOINT+'file/move', data=payload)
    assert response.json()['success'] is True

@given('Um arquivo existente no filesystem 2')
def step_impl(context):
    context.file = '1.txt'

@then('Envie via FTP com sucesso')
def step_impl(context):
    payload = {'source' : context.file}
    response = requests.post(constants.ENDPOINT+'file/serve2Ftp', data=payload)
    assert response.json()['success'] is True