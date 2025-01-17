---
name: Stonewall
description: Entendendo e utilizando transações Stonewall
---
![cover stonewall](assets/cover.webp)

***ATENÇÃO:** Após a prisão dos fundadores da Samourai Wallet e a apreensão dos seus servidores em 24 de abril, o uso do aplicativo Samourai Wallet agora requer uma conexão com o seu próprio Dojo para funcionar corretamente. Além disso, as transações Stonewall não são afetadas e podem continuar sendo realizadas sem problemas. De fato, esses tipos de transações são realizados autonomamente, sem a necessidade de colaboração externa ou conexão via Soroban.*

_Estamos acompanhando de perto a evolução deste caso, bem como os desenvolvimentos relacionados às ferramentas associadas. Fique assegurado de que atualizaremos este tutorial à medida que novas informações estiverem disponíveis._

_Este tutorial é fornecido apenas para fins educativos e informativos. Não endossamos nem encorajamos o uso dessas ferramentas para fins criminosos. É responsabilidade de cada usuário cumprir as leis em sua jurisdição._

---

> *"Quebre as suposições da análise de blockchain com dúvida matematicamente comprovável entre remetente e destinatário de suas transações."*

## O que é uma transação Stonewall?
Stonewall é uma forma específica de transação Bitcoin visando aumentar a privacidade do usuário durante uma transação, imitando um coinjoin entre duas partes, sem de fato ser um. Na verdade, esta transação não é colaborativa. Um usuário pode construí-la sozinho, envolvendo apenas seus próprios UTXOs como entradas. Portanto, você pode criar uma transação Stonewall para qualquer ocasião sem precisar coordenar com outro usuário.

O funcionamento de uma transação Stonewall é o seguinte: como entrada, o remetente usa 2 UTXOs que lhe pertencem. Como saída, a transação produz 4 saídas, incluindo 2 que serão exatamente do mesmo valor. As outras 2 serão de troco. Entre as 2 saídas do mesmo valor, apenas uma irá de fato para o destinatário do pagamento.

Existem apenas 2 papéis em uma transação Stonewall:
- O remetente, que faz o pagamento real;
- O destinatário, que pode estar alheio à natureza específica da transação e simplesmente espera um pagamento do remetente.

Vamos pegar um exemplo para entender essa estrutura de transação. Alice está na padaria para comprar sua baguete, que custa `4.000 sats`. Ela quer pagar em bitcoins mantendo um certo nível de privacidade em seu pagamento. Portanto, ela decide criar uma transação Stonewall para o pagamento.
![transaction stonewall bakery](assets/pt/1.webp)
Analisando esta transação, podemos ver que o padeiro de fato recebeu `4.000 sats` como pagamento pela baguete. Alice usou 2 UTXOs como entradas: um de `10.000 sats` e um de `15.000 sats`. Como saída, ela recebeu 3 UTXOs: um de `4.000 sats`, um de `6.000 sats` e um de `11.000 sats`. Alice tem um saldo líquido de `-4.000 sats` nesta transação, que corresponde ao preço da baguete.

Neste exemplo, omiti intencionalmente as taxas de mineração para facilitar o entendimento. Na realidade, as taxas de transação são totalmente cobertas pelo remetente.

## Qual é a diferença entre Stonewall e Stonewall x2?
A transação Stonewall opera da mesma maneira que a transação StonewallX2, com a única diferença sendo que a última requer colaboração, ao contrário da transação Stonewall clássica, daí a designação "x2". De fato, a transação Stonewall pode ser executada sem requerer cooperação externa: o remetente pode realizá-la sem a assistência de outra pessoa. No entanto, para uma transação Stonewall x2, um participante adicional, chamado de "colaborador", junta-se ao processo. O colaborador contribui com seus próprios bitcoins como entrada, ao lado dos do remetente, e recebe a soma total como saída (menos as taxas de mineração).

Vamos revisitar nosso exemplo com Alice na padaria. Se ela quisesse fazer uma transação Stonewall x2, Alice teria que colaborar com Bob (um terceiro) ao criar a transação. Eles teriam fornecido cada um um UTXO de entrada. Bob então teria recebido o valor total de sua entrada como saída. O padeiro teria recebido o pagamento por sua baguete da mesma forma que na transação Stonewall, enquanto Alice teria recebido seu saldo inicial de volta, menos o custo da baguete.
![transaction stonewall x2](assets/pt/2.webp)
De uma perspectiva externa, o padrão da transação teria permanecido exatamente o mesmo.
![Stonewall ou Stonewall x2?](assets/pt/3.webp)

Em resumo, as transações Stonewall e Stonewall x2 compartilham uma estrutura idêntica. A distinção entre as duas reside na sua natureza colaborativa. A transação Stonewall é desenvolvida individualmente, sem a necessidade de colaboração. Em contraste, a transação Stonewall x2 depende da cooperação entre duas pessoas para sua implementação.

[**-> Saiba mais sobre transações Stonewall x2**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)

## Qual é o propósito de uma transação Stonewall?
A estrutura Stonewall adiciona uma quantidade significativa de entropia à transação e obscurece a análise da cadeia. De uma perspectiva externa, tal transação pode ser interpretada como um pequeno coinjoin entre duas pessoas. Mas, na realidade, assim como a transação Stonewall x2, é um pagamento. Este método, portanto, cria incertezas na análise da cadeia e pode até levar a pistas falsas.

Vamos revisitar o exemplo de Alice na padaria. A transação na blockchain apareceria da seguinte forma:
![Stonewall ou Stonewall x2?](assets/pt/4.webp)
Um observador externo, confiando nas heurísticas comuns de análise de cadeia, poderia concluir erroneamente que "*duas pessoas realizaram um pequeno coinjoin, com um UTXO cada como entrada e dois UTXOs cada como saída*".
![Stonewall ou Stonewall x2?](assets/pt/5.webp)
Esta interpretação é incorreta porque, como você sabe, um UTXO foi enviado ao padeiro, os 2 UTXOs na entrada vêm de Alice, e ela recebeu 3 saídas de troco.

![transaction stonewall baker](assets/pt/1.webp)
Mesmo que um observador externo consiga identificar o padrão da transação Stonewall, ele não terá todas as informações. Eles não serão capazes de determinar qual dos dois UTXOs de mesmos valores corresponde ao pagamento. Além disso, eles não serão capazes de determinar se os dois UTXOs na entrada vêm de duas pessoas diferentes ou se pertencem a uma única pessoa que os uniu. Este último ponto deve-se ao fato de que as transações Stonewall x2, sobre as quais falamos acima, seguem exatamente o mesmo padrão das transações Stonewall. Do exterior e sem informações adicionais sobre o contexto, é impossível diferenciar uma transação Stonewall de uma transação Stonewall x2. No entanto, as primeiras não são transações colaborativas, enquanto as últimas são. Isso adiciona ainda mais dúvidas sobre este gasto.
![Stonewall ou Stonewall x2?](assets/pt/3.webp)
## Como fazer uma transação Stonewall no Samourai Wallet?
Ao contrário das transações Stowaway ou Stonewall x2 (cahoots), a transação Stonewall não requer o uso de Paynyms. Ela pode ser feita diretamente, sem etapas de preparação. Para fazer isso, siga nosso tutorial em vídeo no Samourai Wallet: 
![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)

## Como fazer uma transação Stonewall no Sparrow Wallet?
Ao contrário das transações Stowaway ou Stonewall x2 (cahoots), a transação Stonewall não requer o uso de Paynyms. Ela pode ser feita diretamente, sem etapas de preparação. Para fazer isso, siga nosso tutorial em vídeo no Sparrow Wallet:
![Tutorial Stonewall - Carteira Sparrow](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)

**Recursos Externos:**
- https://docs.samourai.io/en/spend-tools#stonewall.
