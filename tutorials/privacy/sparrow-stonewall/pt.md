---
name: Sparrow Wallet - Stonewall
description: Compreender e utilizar as transacções Stonewall no Sparrow
---

![cover](assets/cover.webp)




> *Quebre os pressupostos da análise da cadeia de blocos com dúvidas matematicamente comprováveis entre o remetente e o destinatário das suas transacções

## O que é uma transação Stonewall?



Stonewall é uma forma específica de transação Bitcoin concebida para aumentar a confidencialidade dos utilizadores quando efectuam despesas, imitando uma união de moedas entre duas pessoas, sem o serem na realidade. De facto, esta transação não é colaborativa. Um utilizador pode construí-la sozinho, usando apenas os UTXOs que lhe pertencem como entrada. Assim, é possível criar uma transação Stonewall para qualquer ocasião, sem ter de sincronizar com outro utilizador.



A transação Stonewall funciona da seguinte forma: como entrada para a transação, o emitente utiliza 2 UTXO que lhe pertencem. Do lado da saída, a transação produz 4 saídas, 2 das quais são exatamente do mesmo montante. Os outros 2 serão moeda estrangeira. Das duas saídas do mesmo montante, apenas uma irá efetivamente para o beneficiário.



Assim, existem apenas 2 papéis numa transação Stonewall:




- O emitente, que efectua o pagamento efetivo ;
- O destinatário, que pode não ter conhecimento da natureza específica da transação e espera simplesmente o pagamento do remetente.



Vejamos um exemplo para compreender esta estrutura de transação. Alice está na padaria para comprar a sua baguete, que custa `4.000 sats`. Ela quer pagar em bitcoins, mantendo alguma forma de confidencialidade sobre o seu pagamento. Por isso, decide criar uma transação Stonewall para o pagamento.



![image](assets/fr/01.webp)



Analisando esta transação, podemos ver que o padeiro recebeu efetivamente `4.000 sats` em pagamento pela baguete. O Alice utilizou 2 UTXOs como entradas: um de `10.000 sats` e outro de `15.000 sats`. Na saída, recuperou 3 UTXO: um de `4 000 sats`, um de `6 000 sats` e um de `11 000 sats`. Por conseguinte, o Alice tem um saldo líquido de 4 000 sats nesta transação, o que corresponde ao preço da baguete.



Neste exemplo, negligenciei intencionalmente as comissões do mining para facilitar a sua compreensão. Na realidade, os custos de transação são inteiramente suportados pelo emitente.



## Qual é a diferença entre Stonewall e Stonewall x2?



A transação Stonewall funciona de forma idêntica à transação StonewallX2, exceto que esta última requer colaboração, ao contrário da transação Stonewall clássica, daí o nome "x2". Isto porque a transação Stonewall é executada sem necessidade de cooperação externa: o remetente pode executá-la sem a ajuda de outra pessoa. Em contrapartida, para uma transação Stonewall x2, um participante adicional, conhecido como "colaborador", junta-se ao processo. Ele ou ela contribui com os seus próprios bitcoins para a transação, juntamente com os do remetente, e recebe o montante total no final (menos os custos mining).



Voltemos ao nosso exemplo com Alice na padaria. Se ela quisesse fazer uma transação Stonewall x2, Alice teria de colaborar com Bob (um terceiro) ao preparar a transação. Cada um deles teria trazido um UTXO. O Bob teria então recebido o montante total da sua contribuição à saída. O padeiro teria recebido o pagamento pela sua baguete da mesma forma que na transação Stonewall, enquanto o Alice teria recuperado o seu saldo inicial, menos o custo da baguete.



![image](assets/fr/02.webp)



De um ponto de vista externo, a transação teria permanecido exatamente a mesma.



![image](assets/fr/03.webp)



Em suma, as transacções Stonewall e Stonewall x2 partilham uma estrutura idêntica. A distinção entre as duas reside no seu carácter colaborativo ou não colaborativo. A transação Stonewall é desenvolvida individualmente, sem necessidade de colaboração. A transação Stonewall x2, por outro lado, depende da cooperação entre dois indivíduos para a sua realização.



[**-> Saiba mais sobre as transacções de Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Qual é o objetivo de uma transação Stonewall?



A estrutura de Stonewall acrescenta uma enorme quantidade de entropia à transação, esbatendo as linhas de análise da cadeia. Vista de fora, esta transação pode ser interpretada como uma pequena união de moedas entre duas pessoas. Mas, na realidade, tal como a transação Stonewall x2, trata-se de um pagamento. Por conseguinte, este método gera incertezas na análise em cadeia, ou mesmo conduz a falsas pistas.



Vejamos o exemplo do Alice na padaria. A transação na cadeia de blocos teria o seguinte aspeto:



![image](assets/fr/04.webp)



Um observador externo que se baseie na heurística comum de análise de cadeias pode concluir erradamente que "*duas pessoas fizeram uma pequena junção de moedas, com um UTXO cada como entrada e dois UTXOs cada como saída*".



![image](assets/fr/05.webp)



Esta interpretação é incorrecta, porque, como sabem, um UTXO foi enviado ao padeiro, os 2 UTXOs de entrada vieram de Alices e ela recuperou 3 saídas de troca.



![image](assets/fr/01.webp)



Mesmo que o observador externo consiga identificar a paterna da transação Stonewall, não terá toda a informação. Não poderá determinar qual dos dois UTXOs de montantes iguais corresponde ao pagamento. Além disso, não poderá determinar se os dois registos UTXO provêm de duas pessoas diferentes ou se pertencem a uma única pessoa que os fundiu. Este último ponto deve-se ao facto de as transacções Stonewall x2, acima mencionadas, seguirem exatamente o mesmo padrão das transacções Stonewall. Visto de fora e sem informação contextual adicional, é impossível distinguir entre uma transação Stonewall e uma transação Stonewall x2. As primeiras não são transacções de colaboração, enquanto as segundas o são. Este facto acrescenta ainda mais dúvidas à despesa.



![image](assets/fr/03.webp)



## Como é que faço uma transação Stonewall no Sparrow?



Originalmente desenvolvidas pela equipa Samurai Wallet, as transacções de Stonewall foram assumidas pela aplicação Ashigaru, um fork do portfólio original criado após a detenção dos criadores de Samurai, e também no Sparrow Wallet.



Será necessário instalar o Sparrow e criar um arquivo :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

Ao contrário das transacções Stowaway ou Stonewall x2 (*cahoots*), as transacções Stonewall não requerem a utilização do Paynyms. Podem ser efectuadas diretamente, sem qualquer preparação especial ou colaboração com outro utilizador.



Para efetuar uma transação Stonewall no Sparrow, o procedimento é muito simples: comece por criar uma transação como habitualmente, quer através do menu `Send`, quer a partir do menu `UTXOs` se desejar fazer *Coin Control*.



![Image](assets/fr/06.webp)



Em seguida, introduza os dados da transação: o endereço do destinatário, uma etiqueta, o montante a enviar e o montante ou a taxa dos encargos, em função das condições do mercado.



![Image](assets/fr/07.webp)



Antes de confirmar, é aqui que pode selecionar a estrutura Stonewall. Na parte inferior da interface, substitua `Eficiência` por `Privacidade`. Se esta opção não aparecer, isso significa que a sua carteira não tem um número suficiente de UTXOs para construir este tipo de transação.



![Image](assets/fr/08.webp)



Depois de selecionar a opção `Privacidade`, notará que a estrutura da transação é completamente modificada: torna-se uma transação Stonewall, consumindo vários dos seus UTXOs como inputs e produzindo dois outputs de montantes idênticos, um dos quais corresponde ao pagamento efetivo de `100.000 sats`, para além dos outputs de troca.



![Image](assets/fr/09.webp)



Se tudo estiver correto, clique em `Criar transação`.



Pode então verificar os detalhes da transação uma última vez e clicar em `Finalizar transação para assinatura`.



![Image](assets/fr/10.webp)



Em seguida, assine a transação de acordo com o método específico da sua carteira, e clique em "Transmitir Transação" para a transmitir na rede Bitcoin, aguardando confirmação.



![Image](assets/fr/11.webp)



Agora você sabe como funciona uma transação Stonewall no Sparrow Wallet e como criar uma. Para aprofundar o seu domínio destas ferramentas concebidas para reforçar a sua confidencialidade onchain, convido-o a seguir a minha formação BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c