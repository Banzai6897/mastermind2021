mastermind 2021
========

$**mastermind2021** é um jogo de computador desenvolvido em **python**, baseado no jogo de tabuleiro "Senha",
respeitando as regras da versão de tabuleiro e extendendo-se por mais níveis de dificuldade.
--------
--------

Objetivo do Jogo e como jogar:
------------------------------

        7 pinos de cores diferentes e aleatórias (exceto preto e branco), entre estes pinos, o usuário deve optar pelas cores em seus respectivos lugares no tabuleiro para acertar a combinação proposta pelo adversário(computador).

        O usuário tem diferentes quantidades de chances para acertar a senha proposta pelo adversário, sendo 8 tentativas para o nível  1, 10 tentativas para o nível 2 e 12 tentativas para o nível 3. 

        Quando o usuário recebe o feedback de sua jogada, a seguinte interpretação deve ser considerada para realizar a próxima jogada: 

            - "X" nas casas em que o dígito escolhido pelo usuário na última jogada não está presente na senha atual.

            - "?" nas casas em que o dígito escolhido pelo usuário na última jogada está presente na senha atual mas em outra casa.

            - "dígito" para as casas que o usuário tiver acertado o próprio dígito em questão e sua posição em jogadas anteriores. 
-------------------------------

Módulos e Bibliotecas
-------
- **main.py** -> Módulo de acesso que controla a execução da aplicação e contém as chamadas das funções que iniciam e/ou finalizam a partida. 

- **partida.py** -> Módulo que contém a definição das funções que controlam o funcionamento das partidas. Recebe informações do usuário para obter o nível de dificuldade. 

  - test_partida.py -> Contém os casos de teste para a função que gera a senha do computador e para a função que recebe o nível em que o usuário deseja jogar.  

- **jogada.py** -> Módulo que contém a definição da função responsável por receber a senha ecolhida pelo usuário a cada tentativa.

- **feedback.py** -> Módulo contendo a definição das funções que recebem e/ou operam dados dos módulos partida.py e jogada.py, comparando o valor de retorno das funções destes 2 módulos para  avaliar a jogada mais recente do usuário e então, interromper ou prosseguir a execução da aplicação (dependendo do número de tentativas ou do acerto de todas as casas na jogada, a execução é interrompida).

  - test_feedback.py ->  Contém casos de teste para a função que checa a quantidade de dígitos na jogada do usuário e para a função que retorna o feedback da jogada do usuário.
  
- **unittest** : Biblioteca utilizada para realizar os testes automatizados, a documentação encontra-se em: [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
-------

Funcionalidades
--------

- O jogo pode ser iniciado em 3 dificuldades, 
representando a senha em 4, 5 ou 6 dígitos (cores) respectivamente.  

- A estrutura do código é responsiva quanto à entradas incompatíveis do usuário. 
--------
Instalação
------------

Para instalar e executar o projeto $mastermind2021 basta seguir os seguintes passos:

    - fazer o download da pasta mastermind2021V2_3.zip 

    - extrair os arquivos da pasta mastermind2021V2_3.zip para uma 
      pasta na máquina em que o jogo será executado

    - abrir a pasta na qual o projeto foi extraído e executar o arquivo 
      main.py através de uma IDE ou através de uma prompt de comando:

      $cd mastermind2021V2_3


      $python main.py --python
                ou
      $python3 main.py --python3
     
------------
Versionamento
----------

- Página contendo as versões do código-fonte e os recursos do projeto: https://github.com/Banzai6897/mastermind2021.git
----------
Apoio e objetivo
-------
    Esta é uma atividade proposta pela PUC-Rio (Rio de Janeiro, Brasil) 
    durante o curso da disciplina de Programação Modular (2021.1 - 3WB),
    sob orientação e supervisão do professor Fl*v*o Be*i*ac*u*,
    destinada exclusivamente apenas à fins acadêmicos. 
    
    O projeto está sendo desenvolvido pela equipe de graduandos:

        - David Wolff Salles de Oliveira
        - João Gabriel Cavalcanti D Nielsen 
        - Laís Corbellini Fagundes 
        - Matheus Amaral Mendes Freitas
--------