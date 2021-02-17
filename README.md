﻿# Sistemas Distribuidos
 Aqui estão reunidos os projetos realizados dentro da disciplina de Sistemas Distribuídos do curso de Engenharia de Computação (Universidade Federal do Ceará - UFC). Os projetos foram feitos via linguagem Python. Esses projetos foram realizados pelo time composto por:
 - Iury Lima Rosal
 - Luís Gustavo de Castro
 - Vinicius Almeida de Castro
 
Projetos:
- Calculadora_UDP: consiste em, utilizando UDP, implementar uma calculadora remota que execute as 4 operações básicas (+, -, x, /) de números decimais. Descreva o formato para cada tipo das mensagens (Request e Response)
- Chat_TCP: consiste em implementar um Chat usando TCP. O Chat deve suportar múltiplos clientes e um servidor. Todos os clientes devem estar na mesma sala do chat (as mensagens enviadas por um cliente devem ser recebidas por todos os clientes). Comandos que o usuário (cliente) pode enviar: 
  - /ENTRAR: ao usar esse comando, ele é requisitado a digitar IP, porta do servidor e nickname que deseja usar no chat (não precisa tratar nicknames repetidos);
  - Uma vez conectado, o cliente pode enviar mensagens para a sala do chat;
  - /USUARIOS: ao enviar esse comando, o cliente recebe a lista de usuários atualmente conectados ao chat; 
  - /SAIR: ao enviar esse comando, uma mensagem é enviada à sala do chat informando que o usuário está saindo e encerra a participação no chat.
