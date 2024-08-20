---
termo: STONEWALL
---

Uma forma específica de transação Bitcoin visando aumentar a privacidade do usuário durante um gasto, imitando um coinjoin entre duas pessoas, sem de fato ser um. De fato, esta transação não é colaborativa. Um usuário pode construí-la sozinho, envolvendo apenas seus próprios UTXOs como entradas. Portanto, você pode criar uma transação Stonewall para qualquer ocasião, sem precisar sincronizar com outro usuário.

O funcionamento da transação Stonewall é o seguinte: na entrada da transação, o remetente usa 2 UTXOs que lhe pertencem. A transação então produz 4 saídas, 2 das quais serão exatamente do mesmo valor. As outras 2 constituirão o troco. Entre as 2 saídas do mesmo valor, apenas uma irá de fato para o destinatário do pagamento.

Assim, existem apenas 2 papéis em uma transação Stonewall:
* O remetente, que faz o pagamento real;
* O destinatário, que pode estar alheio à natureza específica da transação e simplesmente aguarda um pagamento do remetente.

![](../../dictionnaire/assets/33.png)
Transações Stonewall estão disponíveis tanto no aplicativo Samourai Wallet quanto no software Sparrow Wallet.

A estrutura Stonewall adiciona muita entropia à transação e obscurece o rastro para análise de cadeia. De fora, tal transação pode ser interpretada como um pequeno coinjoin entre duas pessoas. Mas, na realidade, assim como a transação Stonewall x2, é um pagamento. Este método gera incertezas na análise de cadeia, ou até leva a pistas falsas. Mesmo que um observador externo consiga identificar o padrão da transação Stonewall, ele não terá todas as informações. Ele não será capaz de determinar qual dos dois UTXOs de mesmos valores corresponde ao pagamento. Além disso, ele não será capaz de determinar se os dois UTXOs na entrada vêm de duas pessoas diferentes ou se pertencem a uma única pessoa que os uniu. Este último ponto deve-se ao fato de que as transações Stonewall x2 seguem exatamente o mesmo padrão que as transações Stonewall. De fora e sem informações contextuais adicionais, é impossível diferenciar uma transação Stonewall de uma transação Stonewall x2. No entanto, as primeiras não são transações colaborativas, enquanto as últimas são. Isso adiciona ainda mais dúvida sobre este gasto.