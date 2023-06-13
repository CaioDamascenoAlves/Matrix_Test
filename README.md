# Testes de Unidade com PyUnit

Os testes de unidade são uma parte essencial do desenvolvimento de software, permitindo verificar a funcionalidade correta das diferentes partes de um programa. O PyUnit é um framework de teste de unidade para Python que fornece uma estrutura conveniente para escrever e executar testes automatizados.

Este projeto utiliza o PyUnit para executar testes de unidade em um programa de multiplicação de matrizes.

## Instalação

Para instalar o PyUnit, siga as etapas abaixo:

1. Certifique-se de ter o Python instalado em seu sistema. Você pode fazer o download e instalar a versão mais recente do Python em [python.org](https://www.python.org).

2. Abra um terminal ou prompt de comando e execute o seguinte comando para instalar o PyUnit usando o gerenciador de pacotes pip:
  ```
  pip install pyunit
  ```
Isso instalará o PyUnit juntamente com suas dependências necessárias.

## Configuração

Antes de executar os testes de unidade, certifique-se de ter o arquivo `matrix.py` contendo a implementação da multiplicação de matrizes. Certifique-se também de que o arquivo `matrix_test.py`, que contém os testes de unidade, esteja no mesmo diretório do arquivo `matrix.py`.

## Execução dos Testes

Para executar os testes de unidade, siga as etapas abaixo:

1. Abra um terminal ou prompt de comando e navegue até o diretório onde estão localizados os arquivos `matrix.py` e `matrix_test.py`.

2. Execute o seguinte comando para iniciar a execução dos testes:
  ```
  python -m unittest matrix_test
  ```

Isso iniciará a execução dos testes definidos na classe `MatrixMultiplicationTestCase` do arquivo `matrix_test.py`.

3. Após a execução dos testes, você verá uma saída no terminal indicando se os testes passaram ou falharam. Cada teste será exibido como um "." se passou ou "F" se falhou. No final, você verá um resumo com o número total de testes executados e os resultados.

## Personalização dos Testes

Se desejar adicionar ou modificar os testes existentes, abra o arquivo `matrix_test.py` em um editor de texto e faça as alterações necessárias. Certifique-se de seguir as convenções do PyUnit ao escrever os testes.

## Conclusão

Os testes de unidade são uma parte importante do processo de desenvolvimento de software, permitindo verificar a corretude do código e identificar possíveis erros e problemas. Com o PyUnit, você pode escrever testes automatizados para suas funções e classes Python, garantindo que elas funcionem conforme o esperado.

Espero que este guia tenha sido útil para você executar os testes de unidade usando o PyUnit. Se você tiver mais dúvidas ou precisar de assistência adicional, não hesite em entrar em contato.

