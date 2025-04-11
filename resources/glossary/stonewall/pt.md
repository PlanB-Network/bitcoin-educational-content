---
term: STONEWALL

---
Uma forma específica de transação Bitcoin destinada a aumentar a privacidade do utilizador durante um gasto, imitando uma junção de moedas entre duas pessoas, sem que na realidade o sejam. De facto, esta transação não é colaborativa. Um utilizador pode construí-la sozinho, envolvendo apenas os seus próprios UTXOs como entradas. Assim, é possível criar uma transação Stonewall para qualquer ocasião, sem necessidade de sincronização com outro utilizador.

O funcionamento da transação Stonewall é o seguinte: na entrada da transação, o emissor utiliza 2 UTXOs que lhe pertencem. A transação produz então 4 outputs, 2 dos quais serão exatamente o mesmo montante. Os outros 2 constituirão o troco. Entre as 2 saídas do mesmo montante, apenas uma irá efetivamente para o destinatário do pagamento.

Assim, existem apenas 2 papéis numa transação Stonewall:


- O remetente, que efectua o pagamento efetivo;
- O destinatário, que pode não ter conhecimento da natureza específica da transação e que se limita a aguardar um pagamento do remetente.

![](../../dictionnaire/assets/33.webp)

As transacções Stonewall estão disponíveis tanto na aplicação Samourai Wallet como no software Sparrow Wallet.

A estrutura Stonewall acrescenta muita entropia à transação e obscurece o rasto para a análise da cadeia. Do exterior, esta transação pode ser interpretada como uma pequena união de moedas entre duas pessoas. Mas, na realidade, tal como a transação Stonewall x2, trata-se de um pagamento. Este método gera, portanto, incertezas na análise da cadeia, ou mesmo leva a falsas pistas. Mesmo que um observador externo consiga identificar o padrão da transação Stonewall, não disporá de toda a informação. Não será capaz de determinar qual dos dois UTXOs de montantes iguais corresponde ao pagamento. Para além disso, não poderão determinar se os dois UTXOs na entrada provêm de duas pessoas diferentes ou se pertencem a uma única pessoa que os fundiu. Este último ponto deve-se ao facto de as transacções Stonewall x2 seguirem exatamente o mesmo padrão que as transacções Stonewall. Do exterior e sem informação de contexto adicional, é impossível diferenciar uma transação Stonewall de uma transação Stonewall x2. No entanto, as primeiras não são transacções de colaboração, enquanto as segundas o são. Este facto acrescenta ainda mais dúvidas sobre esta despesa.