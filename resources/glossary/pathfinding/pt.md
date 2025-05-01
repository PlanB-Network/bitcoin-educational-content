---
term: ENCONTRO DE CAMINHO
---

Processo utilizado por um nó para determinar o caminho ótimo para encaminhar um pagamento através da rede de canais Lightning. A determinação do caminho é efectuada pelo nó pagador, que deve selecionar os nós intermédios mais adequados para chegar ao destinatário. Esta escolha é baseada em vários critérios, tais como taxas, capacidade do canal e timelocks.


Os algoritmos de determinação do caminho constroem um gráfico da topologia da rede a partir dos dados dos boatos e avaliam as várias rotas possíveis entre o nó pagador e o nó recetor. Estas rotas são classificadas da melhor para a pior de acordo com vários critérios. O nó testa então estas rotas até conseguir efetuar o pagamento numa delas.