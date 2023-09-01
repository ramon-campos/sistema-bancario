# Sistema Bancário

## Descrição

### Versão 1

A primeira versão deste projeto consiste em criar um Sistema Bancário em Python. A meta é implementar três operações essenciais: depósito, saque e extrato. O sistema será desenvolvido para um banco que busca monetizar suas operações. A intenção é aplicar os conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias.

### Versão 2

A segunda versão deste projeto consiste em otimizar o Sistema Bancário previamente desenvolvido com o uso de funções Python. O propósito é aprimorar a estrutura e a eficiência do sistema, implementando as operações de depósito, saque e extrato em funções específicas. Nossa intenção é refatorar o código existente, dividindo-o em funções reutilizáveis, facilitando a manutenção e o entendimento do sistema como um todo.

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

## Operações

### Operação de Depósito

* [x] Deve ser possível depositar valores positivos para a minha conta bancária.
* [x] Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Saque

* [x] O sistema deve permitir realizar 3 saques diários, com limite máximo de R$ 500,00 por saque.
* [x] Caso o usuário não tenha saldo suficiente em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
* [x] Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

## Operação de Extrato

* [x] Essa operação deve listar todos os depósitos e saques realizados na conta.
* [x] No fim da listagem, deve ser exibido o saldo atual da conta.
* [x] Se o extrato estiver em branco, exibir a mensagem: "Não foram realizadas movimentações.".
* [x] Os valores devem ser exibidos utilizando o formato "R$ XXX,XX".
