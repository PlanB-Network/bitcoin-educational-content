---
name: Bitfeed
description: Explorar a principal cadeia de protocolos Bitcoin.
---

![cover](assets/cover.webp)



Bitfeed é uma plataforma para visualizar a camada onchain do protocolo Bitcoin. Foi iniciada por um dos colaboradores do projeto Mempool.space e destaca-se principalmente pela sua aparência minimalista e facilidade de utilização.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

Neste tutorial, vamos dar uma vista de olhos a esta ferramenta, que permite explorar todas as transacções e blocos na rede.



## Começar a utilizar o Bitfeed



A Bitfeed é uma plataforma que se centra em três pontos principais:





- Consulta Blockchain**,
- Pesquisa de transacções**,
- Visualizar o mempool**.



### Consultar a cadeia de blocos



Na página inicial do Bitfeed, encontrará principalmente :





- A barra de pesquisa: Esta secção é o ponto de entrada para as consultas da cadeia de blocos. Aqui pode procurar um bloco específico pelo seu número ou hash. Também pode pesquisar transacções específicas e endereços Bitcoin para verificar determinadas informações de transação na rede.



![searchBar](assets/fr/01.webp)



No canto superior esquerdo, pode ver o preço atual do bitcoin, estimado em dólares americanos (USD).



![price](assets/fr/02.webp)



Na barra lateral direita encontra-se o menu da plataforma. A partir deste menu, pode personalizar a interface da plataforma a seu gosto, adicionar ou remover itens e personalizar os filtros de visualização. Por exemplo, visualizar o tamanho de cada bloco por valor ou por peso em bytes virtuais (vBytes).



![menu](assets/fr/03.webp)



No centro da página está o último bloco extraído, com uma vista de todas as transacções incluídas nesse bloco. Esta secção fornece informações sobre o carimbo de data/hora, o número total de bitcoins envolvidos no bloco, o tamanho do bloco em bytes, o número de transacções e o rácio médio do custo da transação por byte virtual no bloco.



![block](assets/fr/04.webp)



Pode voltar atrás no histórico do canal, procurando um bloco específico na barra de pesquisa, e visualizá-lo de acordo com os seus critérios.



Por exemplo, queremos ver as transacções no bloco `879488`.



![bloc](assets/fr/05.webp)



A primeira transação deste bloco representa a transação **coinbase** que permite ao mineiro deste bloco ganhar a recompensa mining, que só pode ser gasta depois de 100 blocos terem sido minerados, composta pelas taxas de transação incluídas e pelo subsídio do bloco. Esta transação é a que permite a emissão de novos bitcoins no sistema.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Por defeito, as transacções num bloco são representadas de acordo com dois critérios:




- O tamanho, que pode variar entre o valor e o peso (vBytes) ;
- A cor pode variar consoante a idade e o rácio das taxas de transação por byte virtual.



![options](assets/fr/07.webp)



Podemos, portanto, concluir que todas as transacções incluídas no mesmo bloco têm o mesmo número de confirmações na cadeia de blocos. Os cubos maiores representam as transacções que contêm a maior quantidade de bitcoins.



Esta interpretação é ainda confirmada pela opção de menu **"Info "**, que nos informa da tradução da cor e do tamanho das transacções do bloco.



![infos](assets/fr/08.webp)



Também é possível visualizar as transacções de um bloco por bytes virtuais e rácio de taxas. Esta visualização pode ser diferente da anterior, uma vez que o valor de bitcoin incluído numa transação não define o seu tamanho.



![visualisation](assets/fr/09.webp)



### Visualizar transacções



Pode procurar uma transação utilizando o seu identificador através da barra de pesquisa. Também pode clicar num cubo para ver as informações relacionadas com essa transação.



No nosso caso, vamos considerar a transação que ocupa o maior espaço no bloco `879488`.



![biggest](assets/fr/10.webp)



Verá que esta transação tem `42,989`, que representa a diferença entre o último bloco a ser extraído e o nosso bloco escolhido. Estas confirmações ajudam a reforçar a segurança da rede Bitcoin, porque para modificar esta transação de forma maliciosa, os atacantes teriam de possuir o poder de computação equivalente para reescrever toda a cadeia de blocos principal.



O tamanho dessa transação é de `57.088 vBytes`, principalmente devido ao grande número de UTXOs usados em sua construção (842 entradas). Surpreendentemente, o rácio da taxa aplicada permanece relativamente baixo (apenas 4 sats/vByte) em comparação com a média global do bloco de 5,82 sats/vByte.



A transação que ocupa mais espaço não é, portanto, necessariamente a transação com o rácio de custo de transação mais elevado.



![transaction](assets/fr/11.webp)



Se seguir a escala no menu **Info**, a transação com o rácio de custo de transação mais elevado é a roxa. Esta é a transação [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) com um rácio de custo de transação de `147.49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Visualização do Mempool



O mempool é o local virtual onde se agrupam as transacções Bitcoin à espera de serem incluídas num bloco. Bitfeed permite a consulta do [mempool](https://planb.academy/resources/glossary/mempool) de vários mineiros Bitcoin, oferecendo uma ampla gama de rastreamento de transações.



![mempool](assets/fr/13.webp)



Nesta secção, pode acompanhar todas as transacções válidas e ainda não confirmadas na cadeia principal da rede Bitcoin.



![unconfirmed](assets/fr/14.webp)



Tem agora um guia para utilizar a plataforma Bitfeed para analisar blocos e transacções de forma a visualizar a informação disponível na cadeia principal da rede Bitcoin, beneficiando de uma interface minimalista e fácil de utilizar. Se gostou deste tutorial, recomendamos que dê o próximo passo: descubra o Lightning Network através do projeto Amboss.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017