# Sistema Bancário

## Objetivo Geral

Este projeto tem como objetivo criar um sistema bancário, utilizando a linguagem Python, com as operações: sacar, depositar e visualizar extrato.

## Desafio

* Fomos contratados por um grande banco para desenvolver o seu novo sistema.
* Esse banco deseja modernizar suas operações e, para isso, escolheu a linguagem Python.
* Para a primeira versão do sistema, devemos implementar apenas 3 operações: depósito, saque e extrato.
* A primeira versão do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária.

### Operação de Depósito

* [x] Deve ser possível depositar valores positivos para a minha conta bancária.
* [x] Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Saque

* [x] O sistema deve permitir realizar 3 saques diários, com limite máximo de R$ 500,00 por saque.
* [x] Caso o usuário não tenha saldo suficiente em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
* [x] Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Extrato

* [x] Essa operação deve listar todos os depósitos e saques realizados na conta.
* [x] No fim da listagem, deve ser exibido o saldo atual da conta.
* [x] Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações.".
* [x] Os valores devem ser exibidos utilizando o formato "R$ XXX,XX".
