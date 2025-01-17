---
name: Whirlpool Stats Tools - Anonsets
description: Entenda o conceito de anonset e como calculá-lo com o WST
---
![cover](assets/cover.webp)

***ATENÇÃO:** Após a prisão dos fundadores da Samourai Wallet e a apreensão dos seus servidores em 24 de abril, a ferramenta Whirlpool Stats Tool não está mais disponível para download, pois estava hospedada no Gitlab da Samourai. Mesmo que você tenha baixado esta ferramenta localmente em sua máquina ou estivesse instalada em seu nó RoninDojo, o WST não funcionará no momento. Ele dependia dos dados fornecidos pelo OXT.me para operar, e esse site não está mais acessível. Atualmente, o WST não é particularmente útil, pois o protocolo Whirlpool está inativo. No entanto, é possível que esses softwares sejam reativados nas próximas semanas. Além disso, a parte teórica deste artigo permanece relevante para entender os princípios e objetivos dos coinjoins em geral (não apenas Whirlpool), bem como para compreender a eficácia do modelo Whirlpool. Você também pode aprender a quantificar a privacidade proporcionada pelos ciclos de coinjoin.*

_Estamos acompanhando de perto a evolução deste caso, bem como os desenvolvimentos relacionados às ferramentas associadas. Fique assegurado de que atualizaremos este tutorial à medida que novas informações estiverem disponíveis._

_Este tutorial é fornecido apenas para fins educativos e informativos. Não endossamos nem encorajamos o uso dessas ferramentas para fins criminosos. É responsabilidade de cada usuário cumprir as leis em sua jurisdição._

---

*"Quebre o rastro que suas moedas deixam para trás"*

Neste tutorial, estudaremos o conceito de anonsets, indicadores que nos permitem estimar a qualidade de um processo de coinjoin no Whirlpool. Cobriremos o método de cálculo e interpretação desses indicadores. Após a parte teórica, passaremos à prática, aprendendo a calcular os anonsets de uma transação específica usando a ferramenta Python *Whirlpool Stats Tools* (WST).

## O que é um coinjoin no Bitcoin?
**Coinjoin é uma técnica que quebra a rastreabilidade dos bitcoins na blockchain**. Ela se baseia em uma transação colaborativa com uma estrutura específica de mesmo name: a transação coinjoin.

As transações coinjoin aumentam a privacidade dos usuários do Bitcoin ao complicar a análise de cadeia para observadores externos. Sua estrutura permite mesclar várias moedas de diferentes usuários em uma única transação, assim obscurecendo os rastros e dificultando a determinação dos vínculos entre endereços de entrada e saída.

O princípio do coinjoin é baseado em uma abordagem colaborativa: vários usuários que desejam misturar seus bitcoins depositam quantias idênticas como entradas da mesma transação. Essas quantias são então redistribuídas em saídas de valor equivalente. Ao final da transação, torna-se impossível associar uma saída específica a um determinado usuário. Não existe um vínculo direto entre as entradas e saídas, quebrando assim a associação entre os usuários e seus UTXO, bem como o histórico de cada moeda.

![coinjoin](assets/notext/1.webp)

Exemplo de uma transação coinjoin:
[323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2](https://mempool.space/tx/323df21f0b0756f98336437aa3d2fb87e02b59f1946b714a7b09df04d429dec2)

Para realizar um coinjoin garantindo que cada usuário mantenha controle sobre seus fundos o tempo todo, o processo começa com a construção da transação por um coordenador, que então a transmite a cada participante. Cada usuário então assina a transação após verificar que ela lhes convém. Todas as assinaturas coletadas são finalmente integradas à transação. Se uma tentativa de desviar fundos for feita por um usuário ou pelo coordenador, modificando as saídas da transação coinjoin, as assinaturas se provarão inválidas, levando à rejeição da transação pelos nós.

Existem várias implementações de coinjoin, como Whirlpool, JoinMarket ou Wabisabi, cada uma visando gerenciar a coordenação entre os participantes e aumentar a eficiência das transações coinjoin.
Neste tutorial, focaremos na minha implementação favorita: Whirlpool, que está disponível no Samourai Wallet e Sparrow Wallet. Na minha opinião, é a implementação mais eficiente para coinjoins no Bitcoin.
## Qual é a utilidade do coinjoin no Bitcoin?
A utilidade do coinjoin reside em sua capacidade de produzir negação plausível, afogando sua moeda dentro de um grupo de moedas indistinguíveis. O objetivo dessa ação é quebrar os vínculos de rastreabilidade, tanto do passado para o presente quanto do presente para o passado.

Em outras palavras, um analista que conheça sua transação inicial na entrada dos ciclos de coinjoin não deve ser capaz de identificar com certeza seu UTXO na saída dos ciclos de remixagem (análise da entrada do ciclo até a saída do ciclo).

![coinjoin](assets/pt/2.webp)

Por outro lado, um analista que conhece seu UTXO na saída dos ciclos de coinjoin deve ser incapaz de determinar a transação original na entrada dos ciclos (análise da saída do ciclo para a entrada do ciclo). 
![coinjoin](assets/pt/3.webp)

Para avaliar a dificuldade de um analista em vincular o passado ao presente e vice-versa, é necessário quantificar o tamanho dos grupos nos quais sua moeda está oculta. Essa medida nos diz o número de análises com uma probabilidade idêntica. Assim, se a análise correta está perdida entre 3 outras análises de igual probabilidade, seu nível de ocultação é muito baixo. Por outro lado, se a análise correta está dentro de um conjunto de 20.000 análises todas igualmente prováveis, sua moeda está muito bem escondida.

E precisamente, o tamanho desses grupos representa indicadores que são chamados de "anonsets".

## Entendendo anonsets
Anonsets servem como indicadores para avaliar o grau de privacidade de um UTXO específico. Mais especificamente, eles medem o número de UTXOs indistinguíveis dentro do conjunto que inclui a moeda estudada. A exigência de um conjunto de UTXO homogêneo significa que os anonsets são geralmente calculados sobre ciclos de coinjoin. O uso desses indicadores é particularmente relevante para coinjoins Whirlpool devido à sua uniformidade.

Anonsets permitem, quando apropriado, julgar a qualidade dos coinjoins. Um grande tamanho de anonset significa um nível aumentado de anonimato, pois se torna difícil distinguir um UTXO específico dentro do conjunto.

Existem dois tipos de anonsets:
- **O conjunto de anonimato prospectivo;**
- **O conjunto de anonimato retrospectivo.**
O primeiro indicador mostra o tamanho do grupo entre o qual o UTXO estudado está oculto no final do ciclo, conhecendo o UTXO na entrada, ou seja, o número de moedas indistinguíveis presentes dentro deste grupo. Este indicador permite medir a resistência da confidencialidade da moeda contra uma análise do passado para o presente (entrada para saída). Em inglês, o nome deste indicador é "*forward anonset*", ou "*forward-looking metrics*". 
![coinjoin](assets/pt/4.webp)

Esta métrica estima a extensão em que seu UTXO está protegido contra tentativas de reconstruir sua história desde seu ponto de entrada até seu ponto de saída no processo de coinjoin.

Por exemplo, se sua transação participou de seu primeiro ciclo de coinjoin e dois outros ciclos descendentes foram completados, o anonset prospectivo de sua moeda seria `13`:

![coinjoin](assets/pt/5.webp)

O segundo indicador mostra o número de possíveis fontes para uma dada moeda, conhecendo o UTXO no final do ciclo. Este indicador mede a resistência da confidencialidade da moeda contra uma análise do presente para o passado (saída para entrada), ou seja, quão difícil é para um analista rastrear até a origem de sua moeda, antes dos ciclos de coinjoin. Em inglês, o nome deste indicador é "*backward anonset*", ou "*backward-looking metrics*".

![coinjoin](assets/pt/6.webp)

Conhecendo seu UTXO na saída dos ciclos, o anonset retrospectivo determina o número de possíveis transações Tx0 que poderiam ter constituído sua entrada nos ciclos de coinjoin. No diagrama abaixo, isso corresponde à soma de todas as bolhas laranjas.

![coinjoin](assets/pt/7.webp)

## Calculando anonsets com Whirlpool Stats Tools (WST)
Para calcular esses indicadores em suas próprias moedas que passaram por ciclos de coinjoin, você pode usar uma ferramenta especialmente desenvolvida pela Samourai Wallet: *Whirlpool Stats Tools*.
Se você possui um RoninDojo, o WST já está pré-instalado no seu nó. Portanto, você pode pular as etapas de instalação e seguir diretamente para as etapas de uso. Para aqueles que não possuem um nó RoninDojo, vamos ver como proceder com a instalação desta ferramenta em um computador.
Você precisará de: Tor Browser (ou Tor), Python 3.4.4 ou superior, git e pip. Abra um terminal. Para verificar a presença e a versão desses softwares no seu sistema, insira os seguintes comandos:
```plaintext
python --version
git --version
pip --version
```

Se necessário, você pode baixá-los de seus respectivos sites:
- https://www.python.org/downloads/ (pip vem diretamente com o Python desde a versão 3.4);
- https://www.torproject.org/download/;
- https://git-scm.com/downloads.
Uma vez que todos esses softwares estejam instalados, a partir de um terminal, clone o repositório WST:
```plaintext
git clone https://code.samourai.io/whirlpool/whirlpool_stats.git
```

![WST](assets/notext/8.webp)

Navegue até o diretório WST:
```plaintext
cd whirlpool_stats
```

Instale as dependências:
```plaintext
pip3 install -r ./requirements.txt
```

![WST](assets/notext/9.webp)

Você também pode instalá-las manualmente (opcional):
```plaintext
pip install PySocks
pip install requests[socks]
pip install plotly
pip install datasketch
pip install numpy
pip install python-bitcoinrpc
```

Navegue até a subpasta `/whirlpool_stats`:
```plaintext
cd whirlpool_stats
```

Inicie o WST:
```plaintext
python3 wst.py
```

![WST](assets/notext/10.webp)

Inicie o Tor ou o Tor Browser em segundo plano.

**-> Para usuários do RoninDojo, você pode retomar o tutorial diretamente aqui.**

Defina o proxy para Tor (RoninDojo),
```plaintext
socks5 127.0.0.1:9050
```

ou para o Tor Browser, dependendo do que você está usando:
```plaintext
socks5 127.0.0.1:9150
```

Esta manipulação permitirá que você baixe dados no OXT via Tor, para não vazar informações sobre suas transações. Se você é um novato e esta etapa parece complexa, saiba que ela simplesmente envolve direcionar seu tráfego de internet através do Tor. O método mais simples consiste em iniciar o Tor Browser em segundo plano no seu computador e, em seguida, executar apenas o segundo comando para se conectar através deste navegador (`socks5 127.0.0.1:9150`).

![WST](assets/notext/11.webp)

Em seguida, navegue até o diretório de trabalho a partir do qual você pretende baixar os dados do WST usando o comando `workdir`. Esta pasta servirá para armazenar os dados transacionais que você irá recuperar do OXT em forma de arquivos `.csv`. Esta informação é essencial para calcular os indicadores que você está procurando obter. Você é livre para escolher a localização deste diretório. Pode ser sábio criar uma pasta especificamente para os dados do WST. Como exemplo, vamos optar pela pasta de downloads. Se você está usando RoninDojo, esta etapa não é necessária:
```plaintext
workdir caminho/para/seu/diretório
```

O prompt de comando deve então ter mudado para indicar seu diretório de trabalho.

![WST](assets/notext/12.webp)

Então, baixe os dados do pool contendo sua transação. Por exemplo, se eu estou no pool de `100,000 sats`, o comando é:
```plaintext
download 0001
```

![WST](assets/notext/13.webp)

Os códigos de denominação no WST são os seguintes:
- Pool de 0.5 bitcoins: `05`
- Pool de 0.05 bitcoins: `005`
- Pool de 0.01 bitcoins: `001`
- Pool de 0.001 bitcoins: `0001`
Uma vez que os dados são baixados, carregue-os. Por exemplo, se eu estiver no pool de `100,000 sats`, o comando é:
```plaintext
load 0001
```

Este passo leva alguns minutos dependendo do seu computador. Agora é um bom momento para fazer um café! :)

![WST](assets/notext/14.webp)

Após carregar os dados, digite o comando `score` seguido pelo seu TXID (identificador de transação) para obter seus anonsets:
```plaintext
score TXID
```

**Atenção**, a escolha do TXID a usar varia dependendo do anonset que deseja calcular. Para avaliar o anonset prospectivo de uma moeda, é necessário inserir, via o comando `score`, o TXID correspondente ao seu primeiro coinjoin, que é a mistura inicial realizada com este UTXO. Por outro lado, para determinar o anonset retrospectivo, você deve inserir o TXID do último coinjoin realizado. Resumindo, o anonset prospectivo é calculado a partir do TXID da primeira mistura, enquanto o anonset retrospectivo é calculado a partir do TXID da última mistura.

O WST então exibe o escore retrospectivo (*Métricas olhando para trás*) e o escore prospectivo (*Métricas olhando para frente*). Por exemplo, eu peguei o TXID de uma moeda aleatória no Whirlpool que não me pertence.

![WST](assets/notext/15.webp)

A transação em questão: [7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be](https://mempool.space/tx/7fe6081fa4f4382be629fb2ef59029d058a22b6fd59cb31d1511fe9e0e7f32be)

Se considerarmos esta transação como o primeiro coinjoin realizado para a moeda em questão, então ela se beneficia de um anonset prospectivo de `86,871`. Isso significa que está escondida entre `86,871` moedas indistinguíveis. Para um observador externo que conhece esta moeda no início dos ciclos de coinjoin e tenta rastrear sua saída, ele será confrontado com `86,871` possíveis UTXOs, cada um com uma probabilidade idêntica de ser a moeda procurada.

Se considerarmos esta transação como o último coinjoin da moeda, ela então possui um anonset retrospectivo de `42,185`. Isso significa que existem `42,185` fontes potenciais para este UTXO. Se um observador externo identifica esta moeda no final dos ciclos e busca rastrear sua origem, ele será confrontado com `42,185` possíveis fontes, todas com uma probabilidade igual de ser a origem procurada.
Além dos scores de anonset, o WST também fornece a você a taxa de difusão da sua saída dentro do pool baseada no anonset. Esse outro indicador simplesmente permite avaliar o potencial de melhoria da sua peça. Essa taxa é particularmente útil para o anonset prospectivo. De fato, se a sua peça tem uma taxa de difusão de 15%, significa que ela pode ser confundida com 15% das peças no pool. Isso é bom, mas você ainda tem uma margem muito grande para melhoria ao continuar remixando. Por outro lado, se a sua peça tem uma taxa de difusão de 95%, então você está se aproximando dos limites do pool. Você pode continuar a remixar, mas o seu anonset não aumentará muito.

É importante notar que os anonsets calculados pelo WST não são perfeitamente precisos. Dado o enorme volume de dados a ser processado, o WST usa o algoritmo *HyperLogLogPlusPlus* para reduzir significativamente o ônus associado ao processamento de dados locais e à memória necessária. Este é um algoritmo que permite estimar o número de valores distintos em conjuntos de dados muito grandes, mantendo alta precisão no resultado. Portanto, os scores fornecidos são bons o suficiente para serem usados em suas análises, pois são estimativas muito próximas da realidade, mas não devem ser interpretados como valores exatos até a unidade.

Em conclusão, tenha em mente que não é imperativo calcular sistematicamente os anonsets para cada uma das suas peças em coinjoins. O próprio design do Whirlpool já oferece garantias. De fato, o anonset retrospectivo raramente é uma preocupação. A partir do seu mix inicial, você obtém um score retrospectivo particularmente alto graças ao legado dos mixes anteriores desde o coinjoin Gênesis. Quanto ao anonset prospectivo, basta manter a sua peça na conta pós-mix por um período suficientemente longo.

É por isso que considero o uso do Whirlpool como particularmente relevante em uma estratégia de *Hodl -> Mix -> Spend -> Replace*. Na minha opinião, a abordagem mais lógica é manter a maior parte das economias em bitcoin em uma carteira fria, enquanto mantém continuamente um certo número de peças em coinjoins no Samourai para cobrir despesas diárias. Uma vez que os bitcoins dos coinjoins são gastos, eles são substituídos por novos, a fim de retornar ao limiar definido de peças misturadas. Este método permite libertar-se da preocupação com nossos anonsets de UTXO, ao mesmo tempo que torna o tempo necessário para a eficácia dos coinjoins muito menos constrangedor.

**Recursos Externos:**

- [Podcast em Francês sobre análise de cadeia](https://fountain.fm/episode/6nNoQEUHBCQR8hAXAkEx)
- [Artigo da Wikipedia sobre HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog)
- Repositório do Samourai para Estatísticas do Whirlpool
- Site do Whirlpool pelo Samourai
- [Artigo no Medium em Inglês sobre privacidade e Bitcoin pelo Samourai](https://medium.com/oxt-research/understanding-bitcoin-privacy-with-oxt-part-1-4-8177a40a5923)
- [Artigo no Medium em Inglês sobre o conceito de conjunto de anonimato pelo Samourai](https://medium.com/samourai-wallet/diving-head-first-into-whirlpool-anonymity-sets-4156a54b0bc7)