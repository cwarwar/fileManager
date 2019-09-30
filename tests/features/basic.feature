Feature: Cenários de teste

  Scenario: Cenário de sucesso, copiar o arquivo para um diretório existente
     Given Um arquivo existente no filesystem
      Then Copie para um diretório existente com sucesso

  Scenario: Cenário de sucesso, copiar o arquivo para um diretório inexistente
    Given Um arquivo existente no filesystem 1
    Then Copie para um diretório inexistente com sucesso

  Scenario: Cenário de sucesso, apagar o arquivo de um diretório
    Given Pegue o arquivo copiado do primeiro passo
    Then Apague-o

  Scenario: Cenário de sucesso, gerar o checksum de um arquivo
    Given Pegue um arquivo qualquer no filesystem
    Then Gere o checksum

  Scenario: Cenário de sucesso, mover o arquivo para um diretório existente
    Given Gerando um arquivo no filesystem
    Then Mova para um diretório existente com sucesso


  Scenario: Cenário de sucesso, mover o arquivo um diretório inexistente
    Given Gerando um arquivo (2.txt) no filesystem
    Then Mova para um diretório inexistente com sucesso


  Scenario: Cenário de sucesso, copiar o arquivo via FTP
    Given Um arquivo existente no filesystem 2
    Then Envie via FTP com sucesso