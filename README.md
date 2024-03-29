# File Manager

Sistema de genrenciamento de arquivos

## Como rodar o projeto

Baster ter o docker instalado, acessar o diretório 'docker' na raiz do projeto e digitar o seguinte comando:

```bash
docker-compose up
```

O projeto será servido na porta 80, então certifique-se de que esta esteja disponível.

## Estrutura do projeto

O projeto consiste em três containers: um é o servidor HTTP, outro que hospeda a aplicação e o outro é um servidor de FTP hospeda arquivos enviados pelo serviço ecarregado de fazer essa ação.

## Detalhes

- O log fica no arquivo log.log na raiz do projeto
- Em caso de erro de algum serviço um email será disparado para suportetecnico.globo@gmail.com
- Possui lock de arquivos para evitar resultados inesperados



## Filesystem

O diretório raiz onde os arquivos são gerenciados ficam no diretório 'filesystem' na raiz do projeto
O diretório /docker/data/ftpuser/kev é mapeado com a raiz do FTP, todo arquivo que é servido via FTP pode ser visto dentro desse diretório

## Serviços

### Copiar arquivo

```bash
curl -X POST \
  http://localhost/file/copy \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F source=1.txt \
  -F destination=/primeiro/segundo/terceiro
```
Resposta exitosa

```json
{
    "response": "23e7ae9746b31e2f559eca880b2a0b9a",
    "success": true
}
```

### Mover arquivo

```bash
curl -X POST \
  http://localhost/file/move \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F source=1.txt \
  -F destination=/diretorio/destino
```

Resposta exitosa

```json
{
    "response": "23e7ae9746b31e2f559eca880b2a0b9a",
    "success": true
}
```

### Deletar arquivo

```bash
curl -X DELETE \
  http://localhost/file/delete \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F source=1.txt
```

Resposta exitosa

```json
{
    "response": "23e7ae9746b31e2f559eca880b2a0b9a",
    "success": true
}
```

### Gerar checksum

```bash
curl -X POST \
  http://localhost/file/checksum \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F source=1.txt
```

Resposta exitosa

```json
{
    "response": "23e7ae9746b31e2f559eca880b2a0b9a",
    "success": true
}
```

### Copiando arquivo para o FTP

```bash
curl -X POST \
  http://localhost/file/serve2Ftp \
  -H 'cache-control: no-cache' \
  -H 'content-type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' \
  -F source=1.txt
```

Resposta exitosa

```json
{
    "response": "/app/filesystem/santa_monica.jpg",
    "success": true
}
```


## Testes
Existe uma bateria de testes de dos serviços implementados com behave, para rodar os testes basta entrar no container, ir ao diretório onde os testes se encontram e executá-los

### Acessando o container
```bash
docker exec -it ID_DO_CONTAINER /bin/sh
```

### Executando os testes
```bash
cd tests/features/steps
behave
```

## Mais testes
Na raiz do projeto existe algns testes com das classes modelo do sistema, para executá-los basta ir na raiz do projeto e executar o comando:
```bash
python testes.py
```
## Licença
Toda, pode passar :)