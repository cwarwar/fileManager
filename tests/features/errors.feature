Feature: Cenários de erro

  Scenario: Cenário de erro, arquivo não existente
    Given Um arquivo inexistente no filesystem
    Then Tente copiar para um diretório e receba um erro