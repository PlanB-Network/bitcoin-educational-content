---
name: Explorador Blockstream
description: Explorar a camada principal do Bitcoin e do Liquid Network
---

![cover](assets/cover.webp)



O Blockstream Explorer é um projeto que facilita a exploração das transacções e do estado global do protocolo Bitcoin, bem como do [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid desenvolvido pela empresa Blockstream.



Iniciado em 2014 pela Blockstream, uma empresa fundada por Adam Back, o explorador [blockstream.info](https://blockstream.info) tem como objetivo fornecer uma infraestrutura robusta para o Bitcoin, garantindo a interoperabilidade e o rastreio de transacções entre camadas (on-chain e Liquid), reforçando simultaneamente a segurança e a privacidade dos utilizadores.



Neste tutorial, veremos o que o distingue, os seus serviços e como oferece uma monitorização contínua das operações e do estado das camadas on-chain e Liquid do Bitcoin.



## Introdução ao Blockstream explorer



### Navegar no canal principal



Quando acede ao explorador Blockstream.info, no "**Dashboard**", a cadeia principal do protocolo Bitcoin é selecionada por defeito. A partir desta interface, tem uma visão geral do :





- Tamanho da cadeia principal: Blocos recentemente extraídos.



![blocks](assets/fr/01.webp)



Esta secção fornece informações sobre os últimos blocos minerados, o carimbo de data/hora, o número de transacções incluídas em cada bloco, o tamanho em kilobytes (kB) e a medida de cada bloco em unidades de peso (**WU** = *Weight Units*). Esta última medida é de interesse, pois permite-nos avaliar a otimização do bloco, dado que cada bloco da cadeia principal está limitado a `4.000.000 WU`, ou `4.000 kWU`.





- Transacções recentes.



![transactions](assets/fr/02.webp)



A secção de transação fornece informações sobre o identificador único da transação, o valor de bitcoin envolvido, o tamanho em bytes virtuais (vB) - que representa a soma de todos os dados (entrada e saída) - e a taxa de comissão associada. Por exemplo, uma transação com um tamanho de `153 vB` a uma taxa de `2 sat/vB` incorrerá numa taxa de `306 satoshis`.



### Exploração de fluidos



A partir do menu "**Blocos**", pode seguir a história de toda a cadeia principal até ao último bloco extraído.



![blocs](assets/fr/03.webp)



Ao clicar num bloco específico, pode obter mais detalhes sobre as informações e transacções nele incluídas. Por exemplo, para o bloco 919330: verá o hash do bloco. Também pode navegar para o bloco anterior, uma vez que cada bloco extraído (exceto o Genesis) está ligado ao anterior, mantendo o hash do seu antecessor.



![metadata](assets/fr/04.webp)



Ao clicar no botão **"Detalhes "**, pode obter mais informações sobre este bloco, como o seu estado, que confirma que foi adicionado à cadeia principal retida e propagada. Tem também a dificuldade com que este bloco é extraído: esta dificuldade representa o poder de computação necessário para resolver o problema criptográfico do mining e é ajustada a cada 2016 blocos (cerca de 2 semanas).



![details](assets/fr/05.webp)



Abaixo desta secção de detalhes, encontram-se todas as transacções incluídas neste bloco.



A primeira transação do bloco é designada por **transaction coinbase**. É utilizada para atribuir a recompensa mining do mineiro (todas as taxas associadas às transacções incluídas no bloco e a concessão do bloco). Os bitcoins criados por esta transação só podem ser gastos depois de terem sido extraídos mais 100 blocos consecutivos. Por outras palavras, para os poder utilizar, o mineiro terá de esperar pela produção do bloco **919430**. Este período é conhecido como [*"maturity period "*](https://planb.academy/fr/resources/glossary/maturity-period).



A coinbase é uma transação especial: é a única que não tem qualquer entrada real, uma vez que não gasta quaisquer bitcoins de uma transação anterior.




![coinbase](assets/fr/06.webp)



Todas as outras transacções estão divididas em duas secções: entradas e saídas.



Para que as bitcoins sejam utilizadas como entradas numa nova transação, o iniciador da transação deve provar a sua posse fornecendo uma assinatura que corresponda a um script específico. Cada bitcoin (UTXO) contém um script que geralmente requer uma assinatura específica que só a chave privada do detentor pode fornecer. Estes scripts são ***scriptSig*** (em ASM), escritos em Bitcoin Script, e podem ser de vários tipos. Neste exemplo, podemos ver que os UTXOs utilizados eram do tipo P2SH para uma saída do tipo P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



É possível seguir o historial de um UTXO específico utilizando heurísticas. Convidamo-lo a descobrir as diferentes heurísticas do Bitcoin e as formas de reforçar a confidencialidade das suas transacções no Bitcoin :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Vejamos o exemplo da despesa de saída desta transação. Ao clicar no identificador da transação, somos redireccionados para a secção **Transacções** na página de detalhes da transação.



![transaction](assets/fr/08.webp)



A partir desta página, é possível saber em que bloco a transação foi incluída. Dependendo do tipo de endereço utilizado, a transação pode otimizar os seus dados (*bytes virtuais*) e, por conseguinte, pagar menos taxas de transação. Esta transação, por exemplo, economizou 53% em taxas ao usar um formato de endereço nativo SegWit Bech32 começando com `bc1q`.



![trx_details](assets/fr/09.webp)



## Camada Liquid



O Liquid Network é um [*sidechain*] (https://planb.academy/en/resources/glossary/sidechain) e uma solução de código aberto de nível 2 para o protocolo Bitcoin. Em particular, permite transacções de bitcoin mais rápidas e mais confidenciais.



No explorador Blockstream.info, clique no botão **"Liquid"** para mudar para a rede Liquid.



![liquid](assets/fr/10.webp)



Clicando em uma das transações que queremos acompanhar, vemos que os valores dos pedaços de bitcoin são substituídos pelas palavras "**Confidential**". Nesta rede, as transacções podem ser confidenciais, pelo que não podemos ver os montantes de cada UTXO, dentro ou fora da transação.



![liquid_trx](assets/fr/11.webp)



No entanto, constatamos que os princípios e mecanismos presentes na camada principal do protocolo Bitcoin são os mesmos: scripts de bloqueio de bitcoin e rastreabilidade UTXO.



![liquid_details](assets/fr/12.webp)



O Liquid Network também disponibiliza activos digitais não depositados que podem ser utilizados pelas organizações. No menu **"Activos "**, encontrará uma lista dos activos registados, o seu total e o domínio a que dizem respeito.



![assets](assets/fr/13.webp)



Para cada ativo, é possível rastrear o histórico das transacções de emissão e de queima (eliminando o total em circulação).



![assets_trxs](assets/fr/14.webp)




## Mais opções



O explorador Blockstream.info também inclui visualizações e acompanhamento de transacções em Testnet, Bitcoin, on-chain e Liquid Network.



![testnet](assets/fr/15.webp)



Quando se vai para a rede Testnet, não se utilizam bitcoins reais, mas têm-se todas as caraterísticas descritas acima.



![liquid_testnet](assets/fr/16.webp)



Esta rede possui um comprimento de corrente diferente, ao qual se pode ligar e testar o funcionamento dos mecanismos Bitcoin e Liquid.





- A secção API é dedicada a qualquer pessoa que pretenda integrar certas funções do Explorer na sua própria aplicação. Através deste API é possível interrogar a cadeia principal das diferentes camadas (on-chain e Liquid), acompanhar as transacções e conhecer as taxas médias das transacções de um bloco, por exemplo.



![api](assets/fr/17.webp)



Agora você está pronto para explorar todo o potencial do Blockstream Explorer para consultar blockchains nas camadas on-chain e Liquid. Esperamos que tenha achado este tutorial informativo e recomendamos nosso tutorial sobre outro explorador Bitcoin:



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f