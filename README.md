# File Manager

Sistema de genrenciamento de arquivos

## Como rodar o projeto

Baster ter o docker instalado, acessar o diretório /docker na raiz do projeto e digitar o seguinte comando

```bash
docker-compose up
```

## Serviços

Copiar arquivo

```bash
[POST]
source
destination
http://localhost:8888/file/copy
```

Mover arquivo

```bash
[POST]
source
destination
http://localhost:8888/file/copy
```

Deletar arquivo

```bash
[DELETE]
source
http://localhost:8888/file/delete
```

Gerar checksum

```bash
[POST]
source
http://localhost:8888/file/checksum
```

Movendo arquivo para o FTP

```bash
[POST]
http://localhost:8888/file/serve2Ftp
```


## Testes
Existe uma bateria de testes de dos serviços implementados com behave, para rodar os testes basta entrar no container, ir ao diretório onde os testes se encontram e executá-los

Acessando o container:
```bash
docker exec -it ID_DO_CONTAINER /bin/sh
```

Executando os testes:
```bash
cd tests/features/steps
behave
```



## Licença
Toda, pode passar :)