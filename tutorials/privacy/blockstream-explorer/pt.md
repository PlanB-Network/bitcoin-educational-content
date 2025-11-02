---
name: Explorador BLOCKSTREAM
description: Explorar os principais Layer dos Bitcoin e Liquid Network
---

![cover](assets/cover.webp)



O BLOCKSTREAM Explorer é um projeto que facilita a exploração das transacções e do Global State do protocolo Bitcoin, bem como do [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid desenvolvido pela empresa BLOCKSTREAM.



Iniciado em 2014 pela BLOCKSTREAM, uma empresa fundada por Adam Back, o explorador [BLOCKSTREAM.info](https://BLOCKSTREAM.info) tem por objetivo fornecer uma infraestrutura robusta para a Bitcoin, garantindo a interoperabilidade e o rastreio de transacções entre camadas (On-Chain e Liquid), reforçando simultaneamente a segurança e a privacidade dos utilizadores.



Neste tutorial, apresentamos o que o torna diferente, os seus serviços e como oferece uma monitorização contínua das operações e do estado das camadas On-Chain e Liquid do Bitcoin.



## Introdução ao BLOCKSTREAM



### Navegar no canal principal



Quando acede ao explorador do BLOCKSTREAM.info, no "**Dashboard**", o canal principal do protocolo Bitcoin é selecionado por defeito. A partir deste Interface, tem uma visão geral do :





- Tamanho da cadeia principal: Blocos recentemente extraídos.



![blocks](assets/fr/01.webp)



Esta secção fornece informações sobre os blocos recentemente minerados, o Timestamp, o número de transacções incluídas em cada BLOCK, o tamanho em kilobytes (kB) e a medida de cada BLOCK em unidades de peso (**WU** = *Weight Units*). Esta última medida é de interesse, pois permite avaliar a otimização do BLOCK, dado que cada BLOCK da cadeia principal está limitado a `4.000.000 WU`, ou `4.000 kWU`.





- Transacções recentes.



![transactions](assets/fr/02.webp)



A secção da transação fornece informações sobre o identificador único da transação, o valor Bitcoin envolvido, o tamanho em bytes virtuais (vB) - que representa a soma de todos os dados (entrada e saída) - e a taxa de débito associada. Por exemplo, uma transação com um tamanho de `153 vB` a uma taxa de `2 sat/vB` terá um custo de `306 satoshis`.



### Exploração de fluidos



A partir do menu "**Blocos**", é possível rastrear a história de toda a cadeia principal até ao último BLOCK extraído.



![blocs](assets/fr/03.webp)



Ao clicar num BLOCK específico, pode obter mais pormenores sobre as informações e transacções nele incluídas. Por exemplo, para o BLOCK 919330: tem o Hash do BLOCK. Também pode navegar para o BLOCK anterior, uma vez que cada BLOCK extraído (exceto o Genesis) está ligado ao anterior, mantendo o Hash do seu antecessor.



![metadata](assets/fr/04.webp)



Ao clicar no botão **"Detalhes "**, pode obter mais informações sobre este BLOCK, como o seu estado, que confirma que foi adicionado à cadeia principal retida e propagada. Também tem a dificuldade com que este BLOCK é extraído: esta dificuldade representa o poder de computação necessário para resolver o problema criptográfico do Mining e é ajustada a cada 2016 blocos (cerca de 2 semanas).



![details](assets/fr/05.webp)



Abaixo desta secção de detalhes, encontram-se todas as transacções incluídas neste BLOCK.



A primeira transação no BLOCK é designada por **transaction coinbase**. É utilizada para atribuir a recompensa Mining do Miner (todas as taxas associadas às transacções incluídas no BLOCK e o subsídio BLOCK). Os bitcoins criados por esta transação só podem ser gastos depois de terem sido extraídos mais 100 blocos consecutivos. Por outras palavras, para os poder utilizar, o Miner terá de esperar pela produção do BLOCK **919430**. Este período é conhecido como [*"maturity period "*](https://planb.network/fr/resources/glossary/maturity-period).



A coinbase é uma transação especial: é a única que não tem qualquer entrada real, uma vez que não gasta quaisquer bitcoins de uma transação anterior.




![coinbase](assets/fr/06.webp)



Todas as outras transacções estão divididas em duas secções: entradas e saídas.



Para que as bitcoins sejam utilizadas como entradas numa nova transação, o iniciador da transação deve provar a sua posse fornecendo uma assinatura que corresponda a um script específico. Cada unidade de bitcoins (UTXO) contém um script que geralmente requer uma assinatura específica que só a chave privada do detentor pode fornecer. Estes scripts são ***scriptSig*** (em ASM), escritos em Bitcoin Script, e podem ser de vários tipos. Neste exemplo, podemos ver que os UTXOs utilizados eram do tipo P2SH para uma saída do tipo P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



É possível seguir o historial de um UTXO específico utilizando heurísticas. Convidamo-lo a descobrir as diferentes heurísticas do Bitcoin e como reforçar a confidencialidade das suas transacções Bitcoin:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Vejamos o exemplo da despesa de saída desta transação. Ao clicar no identificador da transação, somos redireccionados para a secção **Transacções** na página de detalhes da transação.



![transaction](assets/fr/08.webp)



Nesta página, é possível saber em que BLOCK a transação foi incluída. Dependendo do tipo de Address utilizado, a transação pode otimizar os seus dados (*bytes virtuais*) e, por conseguinte, pagar menos taxas de transação. Esta transação, por exemplo, economizou 53% em taxas ao usar um formato nativo SegWit BECH32 Address começando com `bc1q`.



![trx_details](assets/fr/09.webp)



## Revestimento Liquid



O Liquid Network é um [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) e uma solução de fonte aberta de nível 2 para o protocolo Bitcoin. Em particular, permite transacções Bitcoin mais rápidas e mais confidenciais.



No explorador BLOCKSTREAM.info, clique no botão **"Liquid"** para mudar para o Liquid Network.



![liquid](assets/fr/10.webp)



Ao clicar numa das transacções que queremos seguir, vemos que os montantes das peças Bitcoin são substituídos pelas palavras "**Confidencial**". Nesta rede, as transacções podem ser confidenciais, pelo que não podemos ver os montantes de cada UTXO, dentro ou fora da transação.



![liquid_trx](assets/fr/11.webp)



No entanto, notamos que os princípios e mecanismos presentes nos principais Layer do protocolo Bitcoin são os mesmos: scripts de bloqueio Bitcoin e rastreabilidade UTXO.



![liquid_details](assets/fr/12.webp)



O Liquid Network também disponibiliza activos digitais não depositados que podem ser utilizados pelas organizações. No menu **"Activos "**, encontrará uma lista dos activos registados, o seu total e o domínio a que se referem.



![assets](assets/fr/13.webp)



Para cada ativo, é possível rastrear o histórico das transacções de emissão e de queima (eliminando o total em circulação).



![assets_trxs](assets/fr/14.webp)




## Mais opções



O explorador BLOCKSTREAM.info também inclui visualizações e acompanhamento de transacções em Testnet, Bitcoin, On-Chain e Liquid Network.



![testnet](assets/fr/15.webp)



Quando se utiliza a rede Testnet, não se usam bitcoins reais, mas têm-se todas as caraterísticas descritas acima.



![liquid_testnet](assets/fr/16.webp)



Esta rede possui um comprimento de corrente diferente, ao qual se pode ligar e testar o funcionamento dos mecanismos Bitcoin e Liquid.





- A secção API é dedicada a qualquer pessoa que pretenda integrar determinadas funções do Explorer na sua própria aplicação. Através deste API é possível interrogar a cadeia principal dos diferentes níveis (On-Chain e Liquid), acompanhar as transacções e conhecer as taxas médias das transacções num BLOCK, por exemplo.



![api](assets/fr/17.webp)



Agora você está pronto para explorar todo o potencial do BLOCKSTREAM Explorer para consultar blockchains nas camadas On-Chain e Liquid. Esperamos que tenha achado este tutorial informativo e recomendamos nosso tutorial sobre outro Bitcoin Explorer:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f