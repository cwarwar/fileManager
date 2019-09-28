Feature: Cenários de teste

  Scenario: Cenário de sucesso, mover o arquivo para um diretório existente
     Given Um arquivo existente no filesystem
      Then Copie para um diretório existente com sucesso

  Scenario: Cenário de sucesso, mover o arquivo para um diretório inexistente
    Given Um arquivo existente no filesystem 1
    Then Copie para um diretório inexistente com sucesso
