---
term: STONEWALL X2

---
Uma forma específica de transação Bitcoin destinada a aumentar a privacidade do utilizador durante uma despesa, através da colaboração com um terceiro não envolvido na despesa. Este método simula uma mini-coinjoin entre dois participantes, ao mesmo tempo que efectua um pagamento a um terceiro. As transacções Stonewall x2 estão disponíveis tanto na aplicação Samourai Wallet como no software Sparrow Wallet (ambos são interoperáveis).

O seu funcionamento é relativamente simples: utiliza um UTXO na nossa posse para efetuar o pagamento e procura a ajuda de um terceiro que também contribui com um UTXO que possui. A transação termina com quatro saídas: duas delas de montantes iguais, uma destinada ao endereço do destinatário do pagamento, a outra a um endereço pertencente ao colaborador. Um terceiro UTXO é enviado de volta para outro endereço do colaborador, permitindo-lhe recuperar o montante inicial (uma ação neutra para ele, menos as taxas de mineração), e um último UTXO retorna a um endereço que possuímos, o que constitui o troco do pagamento. Assim, são definidos três papéis diferentes nas transacções Stonewall x2:


- O remetente, que efectua o pagamento efetivo;
- O colaborador, que fornece bitcoins para melhorar o anonimato geral da transação, ao mesmo tempo que recupera totalmente os seus fundos no final;
- O destinatário, que pode não ter conhecimento da natureza específica da transação e que se limita a aguardar um pagamento do remetente.

![](../../dictionnaire/assets/3.webp)

A estrutura x2 de Stonewall acrescenta muita entropia à transação e baralha as pistas da análise da cadeia. De fora, uma transação deste tipo pode ser interpretada como uma pequena união de moedas entre duas pessoas. Mas, na realidade, trata-se de um pagamento. Este método gera, assim, incertezas na análise da cadeia, ou mesmo pistas falsas. Mesmo que um observador externo consiga identificar o padrão da transação Stonewall x2, não disporá de toda a informação. Não será capaz de determinar qual dos dois UTXOs de montantes iguais corresponde ao pagamento. Além disso, não poderão saber quem efectuou o pagamento. Por último, não poderão determinar se as duas UTXO de entrada provêm de duas pessoas diferentes ou se pertencem a uma única pessoa que as fundiu. Este último ponto deve-se ao facto de as transacções Stonewall clássicas seguirem exatamente o mesmo padrão que as transacções Stonewall x2. Do exterior e sem informação adicional sobre o contexto, é impossível diferenciar uma transação Stonewall de uma transação Stonewall x2. No entanto, as primeiras não são transacções de colaboração, enquanto as segundas o são. Este facto aumenta ainda mais as dúvidas sobre as despesas.