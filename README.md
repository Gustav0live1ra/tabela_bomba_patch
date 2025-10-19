# tabela_bomba_patch
Projeto criado com o intuito de simular uma tabela de futebol com sistema de pontos corridos.

  __CODE DESCRIPTION__

  
    - O código utiliza das bibliotecas pandas, para criar a database e permitir a altereção das informações contidas na mesma a partir de resultados entre os jogadores, e tabulate, para possibilitar a organização dessa base de dados em formato de tabela.
    - O código também conta com uma validação de dados razoável e funcionalidades, como o "for" que permite a digitação de todas as informações de uma vez (impedindo assim a necessidade de ficar fechando e reexecutando o programa toda hora), que otimizam o uso.
    - A lógica consiste na possibilitade de 3 fatores: caso dê empate, derrota ou vitória pro time da casa. Em cada um desses casos são atribuidas informações particulares que, conforme o fator ocorrido, vão ser somadas ao dataframe. E por fim será exibida a tabela_final, organizada inicialmente por pontos, depois vitórias, saldo de gols, etc; e posta em formato de tabela.
