---
name: Ashigaru - Stonewall
description: Compreender e utilizar as transacções Stonewall em Ashigaru
---
![cover stonewall](assets/cover.webp)



> *Quebre os pressupostos da análise da cadeia de blocos com dúvidas matematicamente comprováveis entre o remetente e o destinatário das suas transacções

## O que é uma transação Stonewall?



A Stonewall é uma forma específica de transação Bitcoin concebida para aumentar a confidencialidade dos utilizadores quando efectuam despesas, imitando uma união de moedas entre duas pessoas, sem o serem na realidade. De facto, esta transação não é colaborativa. Um utilizador pode construí-la sozinho, usando apenas os UTXOs que possui como entrada. Assim, é possível criar uma transação Stonewall para qualquer ocasião, sem ter de sincronizar com outro utilizador.



A transação Stonewall funciona da seguinte forma: como entrada para a transação, o emitente utiliza 2 UTXO que lhe pertencem. Do lado das saídas, a transação produz 4 saídas, 2 das quais são exatamente do mesmo montante. Os outros 2 serão moeda estrangeira. Das duas saídas do mesmo montante, apenas uma irá efetivamente para o beneficiário.



Assim, existem apenas 2 papéis numa transação Stonewall:




- O emitente, que efectua o pagamento efetivo ;
- O destinatário, que pode não ter conhecimento da natureza específica da transação e espera simplesmente o pagamento do remetente.



Vejamos um exemplo para compreender esta estrutura de transação. Alice está na padaria para comprar a sua baguete, que custa `4.000 sats`. Ela quer pagar em bitcoins, mantendo alguma forma de confidencialidade sobre o seu pagamento. Por isso, decide criar uma transação Stonewall para o pagamento.



![image](assets/fr/01.webp)



Analisando esta transação, podemos ver que o padeiro recebeu efetivamente `4 000 sats` em pagamento da baguete. O Alice utilizou 2 UTXO como inputs: um de `10.000 sats` e outro de `15.000 sats`. Do lado da produção, recuperou 3 UTXO: um de `4 000 sats`, um de `6 000 sats` e um de `11 000 sats`. Por conseguinte, o Alice tem um saldo líquido de 4 000 sats nesta transação, o que corresponde ao preço da baguete.



Neste exemplo, negligenciei intencionalmente as comissões do mining para facilitar a compreensão. Na realidade, os custos de transação são inteiramente suportados pelo emitente.



## Qual é a diferença entre Stonewall e Stonewall x2?



A transação Stonewall funciona de forma idêntica à transação StonewallX2, exceto que esta última requer colaboração, ao contrário da transação Stonewall clássica, daí o nome "x2". Isto porque a transação Stonewall é executada sem necessidade de cooperação externa: o remetente pode executá-la sem a ajuda de outra pessoa. Em contrapartida, para uma transação Stonewall x2, um participante adicional, conhecido como "colaborador", junta-se ao processo. Ele ou ela contribui com os seus próprios bitcoins para a transação, juntamente com os do remetente, e recebe o montante total no final (modulo dos custos mining).



Voltemos ao nosso exemplo com Alice na padaria. Se ela quisesse fazer uma transação Stonewall x2, Alice teria de colaborar com Bob (um terceiro) ao preparar a transação. Cada um deles teria trazido um UTXO. O Bob teria então recebido toda a sua contribuição de volta. O padeiro teria recebido o pagamento pela sua baguete da mesma forma que na transação de Stonewall, enquanto o Alice teria recuperado o seu saldo inicial, menos o custo da baguete.



![image](assets/fr/02.webp)



De um ponto de vista externo, a transação teria permanecido exatamente a mesma.



![image](assets/fr/03.webp)



Em suma, as transacções Stonewall e Stonewall x2 partilham uma estrutura idêntica. A distinção entre as duas reside no seu carácter colaborativo ou não colaborativo. A transação Stonewall é desenvolvida individualmente, sem necessidade de colaboração. A transação Stonewall x2, por outro lado, depende da cooperação entre dois indivíduos para a sua realização.



[**-> Saiba mais sobre as transacções de Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Qual é o objetivo de uma transação Stonewall?



A estrutura de Stonewall acrescenta uma enorme quantidade de entropia à transação, esbatendo as linhas de análise da cadeia. Vista de fora, esta transação pode ser interpretada como uma pequena união de moedas entre duas pessoas. Mas, na realidade, tal como a transação Stonewall x2, trata-se de um pagamento. Por conseguinte, este método gera incertezas na análise da cadeia, ou mesmo conduz a falsas pistas.



Vejamos o exemplo do Alice na padaria. A transação na cadeia de blocos teria o seguinte aspeto:



![image](assets/fr/04.webp)



Um observador externo que se baseie na heurística de análise de cadeia comum pode concluir erradamente que "**duas pessoas fizeram uma pequena junção de moedas, com um UTXO cada como entrada e dois UTXOs cada como saída**".



![image](assets/fr/05.webp)



Esta interpretação é incorrecta, porque, como sabem, um UTXO foi enviado ao padeiro, os 2 UTXOs de entrada vieram de Alices, e ela recuperou 3 outputs de taxas de câmbio.



![image](assets/fr/01.webp)



Mesmo que o observador externo consiga identificar a paterna da transação Stonewall, não terá toda a informação. Não poderá determinar qual das duas UTXOs de montantes iguais corresponde ao pagamento. Além disso, não poderá determinar se as duas UTXO registadas são de duas pessoas diferentes ou se pertencem a uma única pessoa que as fundiu. Este último ponto deve-se ao facto de as transacções Stonewall x2, acima mencionadas, seguirem exatamente o mesmo padrão das transacções Stonewall. Visto de fora, e sem informação contextual adicional, é impossível distinguir entre uma transação Stonewall e uma transação Stonewall x2. As primeiras não são transacções de colaboração, enquanto as segundas o são. Este facto acrescenta ainda mais dúvidas à despesa.



![image](assets/fr/03.webp)



## Como é que faço uma transação Stonewall em Ashigaru?



Originalmente desenvolvidas pela equipa Samourai Wallet, as transacções Stonewall foram assumidas pela aplicação Ashigaru, um fork do wallet original criado após a detenção dos criadores Samourai. É necessário instalar a Ashigaru e criar um wallet:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Ao contrário das transacções Stowaway ou Stonewall x2 (*cahoots*), as transacções Stonewall não requerem a utilização do Paynyms. Podem ser executadas diretamente, sem preparação prévia ou colaboração com outro utilizador.



Na verdade, não é preciso um tutorial para fazer transacções de Stonewall, uma vez que Ashigaru as gera automaticamente de cada vez que gastas, assim que o teu wallet contém UTXOs suficientes.



Clique no botão `+` no canto inferior direito do ecrã e, em seguida, selecione `Enviar`.



![Image](assets/fr/06.webp)



Selecione a conta a partir da qual pretende efetuar a despesa.



![Image](assets/fr/07.webp)



Em seguida, introduza os dados da transação: o endereço do destinatário e o montante a enviar, e prima a seta para confirmar.



![Image](assets/fr/08.webp)



Aqui, pode, obviamente, ajustar as taxas de transação predefinidas de acordo com as condições de mercado. No entanto, o elemento mais interessante desta página é o tipo de transação. Verá que a Ashigaru selecionou automaticamente `STONEWALL`. Clique no botão `PREVIEW` para saber mais.



![Image](assets/fr/09.webp)



Pode ver que a transação é de facto do tipo Stonewall: inclui 2 entradas do mesmo montante, 2 saídas do mesmo montante, bem como as saídas de troca e, no meu caso, uma entrada adicional para satisfazer a soma do pagamento.



![Image](assets/fr/10.webp)



Se não desejar efetuar uma transação Stonewall, mas preferir um pagamento convencional, clique no ícone do lápis no canto superior direito do ecrã e selecione `Simples` em vez de `STONEWALL`.



![Image](assets/fr/11.webp)



Depois de ter verificado todos os detalhes, arraste a seta verde na parte inferior do ecrã para assinar e libertar a transação.



![Image](assets/fr/12.webp)



Agora já sabe como efetuar uma transação Stonewall e, mais importante, como funciona. Se quiseres saber mais, dá uma vista de olhos no meu tutorial sobre o Terminal Ashigaru, que explica como fazer coinjoins através do Whirlpool.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add