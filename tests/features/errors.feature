Feature: Cenários de erro

  Scenario: Cenário de erro, copiando um arquivo não existente
    Given Um arquivo inexistente (nao_existe.txt) no filesystem
    Then Tente copiar para um diretório e receba um erro

  Scenario: Cenário de erro, apagando um arquivo inexistente
    Given Um arquivo inexistente (nao_existe_2.txt) no filesystem
    Then Tente apagar e receba um erro

  Scenario: Cenário de erro, gerando o checksum de um arquivo inexistente
    Given Um arquivo inexistente (nao_existe_3.txt) no filesystem
    Then Tente gerar o checksum e receba um erro