---
name: Coin Control
description: Inicie-se no Coin Control, uma ferramenta essencial para proteger a sua privacidade no Bitcoin
---
![cover](assets/cover.webp)


*Este tutorial foi importado de [uma lição da Officine Bitcoin](https://officinebitcoin.it/lezioni/coinco/).*



## Introdução



A solidez do protocolo Bitcoin é garantida por conceitos fundamentais simples. Entre eles, destaca-se a transparência: todas as transações de Bitcoin são públicas e facilmente verificáveis por qualquer pessoa. Embora essa característica seja um marco do protocolo, pois previne fraudes e garante a autenticidade dos fundos, também pode representar um desafio para a confidencialidade. **Você já se perguntou se tanta transparência pode comprometer sua privacidade?**



É melhor fazê-lo. Embora a acumulação de Satoshi não-kyc seja bastante fácil, a sua privacidade está mais em risco logo na fase de despesa.



### O que acontece quando se gasta um UTXO



Gastar Bitcoin não é simplesmente a transferência de valor para outra pessoa.



Ao consumir um dos seus UTXO, deve, de facto, cumprir as condições impostas pela transparência do protocolo, pois tem a obrigação de provar que é proprietário desses fundos. Torna-se assim responsável por :




- expor a sua chave pública;
- produzir uma assinatura digital.



O momento de gastar é, portanto, o mais crítico: **gastar Bitcoin é um ato que deve ser feito conscientemente e com o máximo de controlo possível**.



## Controlo Coin



No protocolo Bitcoin, itens como _conta_ ou _unidades monetárias_ não existem. O conceito de UTXO é explicado de forma excelente no seguinte curso, que recomendo vivamente:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

Com o Bitcoin o que se acumula e mais tarde se gasta são pequenas ou grandes unidades de conta medidas em Satoshi, representadas por "outputs de transacções não gastas", o **UTXO**, também chamadas "moedas". Quando se utilizam UTXOs para criar uma transação, estes são completamente destruídos e outros UTXOs são criados no seu lugar.



As carteiras de software são desenvolvidas para fazer esta escolha automaticamente, utilizando moedas selecionadas "aleatoriamente", adoptando determinados algoritmos fornecidos pelo protocolo. O único critério que estes algoritmos cumprem é o de cobrir o montante necessário para as despesas.



Podem misturar UTXOs de diferentes idades, ou favorecer o gasto dos mais recentes ou dos mais "antigos", dependendo do algoritmo escolhido pelos programadores. As melhores Carteiras de Software, também planeiam deixar o utilizador com uma escolha importante.



O `Controlo Coin`, que também pode ser referido como `Seleção Coin`, é uma caraterística de algumas Carteiras de Software que lhe permite **selecionar manualmente UTXOs para gastar quando constrói a sua transação**.



Suponhamos que temos um Wallet com 3 UTXOs de 21.000, 42.000 e 63.000 Satoshi, respetivamente.



![img](assets/en/01.webp)



Se tiver de gastar 24.000 Sats e deixar que um algoritmo faça a seleção automática, um bom Software Wallet pode optar por combinar UTXO 1 + UTXO 2 para pagar as taxas de 24k Sats e Miner, criando um remanescente que volta para um Address interno do Wallet inicial.



![img](assets/en/02.webp)



Após a transação, a nova situação no Wallet, contando apenas com os UTXO, pode ser resumida da seguinte forma.



![img](assets/en/03.webp)



No entanto, com o software certo e o seu conhecimento, poderia ter feito uma escolha diferente e, de certa forma, mais correta. Por exemplo, selecionando apenas o UTXO2 (de 42.000 Sats).



![img](assets/en/04.webp)



Com uma situação final no seu Wallet, ao nível do UTXO, isso parece diferente de antes.



![img](assets/en/05.webp)



## Por que o coin control manual?



![img](assets/en/06.webp)



Nos dois exemplos acima, o saldo é efetivamente o mesmo `108.280 Sats`. Depois de gastar 24.000 Sats, sem seleção manual teríamos 2 UTXO no Wallet; com o controlo manual do Coin temos 3 no total.



A pergunta que poderíamos nos fazer é a seguinte: **por que fazer tudo isso?** Existem, ou poderiam existir, várias razões pelas quais não usamos `UTXO1` **e todas elas estão na base do porquê — na fase de gasto — ativar o coin control manual é uma das boas práticas a seguir**.



A seleção de UTXOs permite-lhe favorecer alguns aspectos em detrimento de outros. A escolha depende realmente dos objectivos que pretende alcançar.



### Privacidade



Uma das principais vantagens do controlo manual do Coin é uma **maior privacidade para o gastador**. Tomemos sempre o nosso exemplo: a despesa de 24.000 Satoshi _sem seleção manual de Coin_. Uma vez que o Blockchain do Bitcoin é um registo público, um observador externo pode declarar, sem sombra de dúvida, que as entradas `UTXO1 de 21.000 Sats` e `UTXO2 de 42.000 Sats`, bem como o resto, o `UTXO5 de 38.280 Sats` **pertencem todos ao mesmo utilizador**.



Ao selecionar manualmente o `UTXO2`, por outro lado, o `UTXO1` permanece completamente reservado, permanecendo no conjunto UTXO à espera de ser utilizado num momento mais apropriado.



O `UTXO1` pode ser proveniente de uma fonte KYC, como um pagamento recebido no Exchange por bens e serviços, enquanto os outros UTXOs não. A mistura de um UTXO-kyc com outros mais confidenciais compromete o conjunto de anonimato dos fundos não-kyc.



**Os fundos KYC inevitavelmente levariam a rastrear a identidade do pagador. Se fosse a tua wallet, gostarias que um observador externo pudesse rastrear a tua identidade com uma certeza tão absoluta?**



Tente então considerar que as Carteiras que implementam a seleção manual de UTXOs, por exemplo, permitem a **segregação de um ou mais UTXOs**, uma função a ser utilizada quando tais situações surgem.



Embora eu esteja convencido de que os fundos KYC devem ser mantidos num Wallet separado do Bitcoin comprado sem kyc, se este for o seu caso, a segregação de alguns dos seus endereços é uma ajuda fundamental, da qual poderá tirar partido aprendendo a selecionar manualmente as suas entradas de despesas.



### Poupar nas taxas



Selecionar o UTXO correto para fazer uma despesa, **permite a otimização da taxa**. Partindo novamente do nosso exemplo inicial, o Software Wallet selecionou dois UTXOs para cobrir a despesa a efetuar. Dois UTXOs implicam duas assinaturas a serem mostradas à rede. Daqui resulta que a transação tem um maior "peso" em termos de vBytes.



Por outro lado, com o controlo manual Coin, pode selecionar apenas um que seja suficiente para cobrir o montante, poupando taxas ao diminuir o "peso" da transação.



Numa altura em que as taxas são elevadas, mas é obrigado a gastar Bitcoin On-Chain (por exemplo, para abrir um canal Lightning Network), é nessa altura que o controlo Coin se revela o incentivo económico mais adequado.



### Agregação dos restos mortais



Quando se faz um pagamento e se usa Bitcoin On-Chain, a possibilidade de receber troco torna-se quase sempre uma certeza. Cada resto é em si mesmo uma pequena perda de privacidade, pois revela à rede (e especialmente ao destinatário do pagamento) um Address seu que pode ser associado à sua entrada de origem.



Considerando que os melhores Wallet HDs generate endereços especiais para os restos, pode facilmente reconhecê-los e "segregar" todos os restos das várias transacções efectuadas; quando atingirem um determinado montante, pode seleccioná-los manualmente e consolidá-los, ou mudar para Lightning Network (o meu método preferido) e processá-los de modo a recuperar a privacidade perdida nas despesas.



### Despesas de um Cold Wallet



O Cold Wallet é um instrumento com o qual se pode obter razoavelmente um bom grau de segurança, para armazenar qualquer montante de fundos a manter de lado durante um longo período de tempo. No entanto, podem ocorrer imprevistos, pelo que surge a necessidade de deitar mão às poupanças e fazer face a algumas despesas inesperadas.



Não sei quantos podem partilhar a minha abordagem, mas o meu conselho é que **nunca faça a despesa diretamente a partir do Cold Wallet, para evitar receber a mudança entre os endereços do mesmo**. Aprenda a selecionar manualmente os UTXO necessários para cobrir a despesa, transfira-os para um Wallet Hot e prepare a sua transação a partir deste último. Qualquer troco, então, poderá devolvê-lo a um Cold Wallet Address (se o montante for adequado), utilizá-lo para outras despesas, ou ainda segregá-lo como acabámos de ver.



## Apresentação prática


Após a introdução técnica do "porquê", vamos ver como pôr em prática o controlo manual Coin com diferentes softwares, desktop e mobile. Utilizaremos sempre o mesmo Wallet BIP39, importado para cada uma das ferramentas escolhidas, de modo a mostrar as pequenas diferenças entre elas.



## Wallet Ambiente de trabalho



### Sparrow



Se utilizar o Sparrow, abra o Wallet e selecione _UTXOs_ no menu da esquerda. Verá uma lista de todos os UTXOs associados ao seu Wallet.



Basta clicar com o rato sobre um deles e escolher _Enviar seleccionado_. O Sparrow também lhe mostra o total disponível para gastar após a seleção, mesmo ao lado do comando. Graficamente, o Sparrow mostra-lhe o UTXO selecionado, destacando-o a azul.



![img](assets/en/07.webp)



Também pode selecionar mais do que um. Utilize a tecla _CTRL_ para selecionar UTXOs não adjacentes na lista.



![img](assets/en/08.webp)



Depois de selecionar manualmente o UTXO, pode começar a construir a transação, e o Sparrow mostrar-lhe-á bem, graficamente, como é constituída.



![img](assets/en/09.webp)



#### Segregação do UTXO



Segregar fundos significa "bloqueá-los" no Wallet para que não possam ser utilizados como entrada numa transação. O Sparrow permite esta funcionalidade, a que se acede sempre a partir do menu _UTXOs_: coloca-se o rato sobre o UTXO a "bloquear" e clica-se com o botão direito do rato. Entre as funcionalidades deste procedimento aparecerá _Freeze UTXO_. É assim que poderá separar as moedas com as carteiras Sparrow.



![img](assets/en/29.webp)



### Electrum



Se o seu ambiente de trabalho Wallet é Electrum, deve saber que pode selecionar manualmente UTXOs no menu _Addresses_ ou no menu _Coins_. Em ambos os menus, a seleção é feita apontando o rato para o UTXO desejado e escolhendo _Adicionar ao controlo Coin_ depois de clicar com o botão direito do rato.



![img](assets/en/10.webp)



Mesmo com este software pode selecionar mais do que um UTXO, ajudando com a tecla _CTRL_ no seu teclado se não estiverem adjacentes um ao outro.



![img](assets/en/11.webp)



Graficamente, a Electrum mostra-lhe a seleção destacando os UTXOs selecionados em Green, enquanto uma barra aparece na parte inferior, destacada na mesma cor, mostrando o saldo disponível após o controlo Coin.



![img](assets/en/12.webp)



Uma vez selecionada a saída, ou saídas, pode construir a sua transação como faz habitualmente no menu _Send_.



#### Segregação do UTXO



Electrum fornece esta funcionalidade indo ao menu _Coins_, onde seleciona um determinado UTXO e depois escolhe _Freeze_ com um clique no botão direito. Pode "congelar" o Address mesmo sem fundos no menu _Addresses_, ou o "Coin" para não o gastar.



![img](assets/en/28.webp)



### Matraca



O Nunchuk permite-te selecionar manualmente UTXOs a partir do menu principal quando este estiver aberto. Abre o Nunchuk e clica em _Ver moedas_.



![img](assets/en/13.webp)



Isto abre a janela que contém todos os UTXOs no seu Wallet, onde pode selecionar um ou mais activando a marca de verificação junto a cada montante. Depois de fazer a sua seleção, continue com _Criar transacção_.



![img](assets/en/14.webp)



Em seguida, pode introduzir o Address de destino e definir o montante e as taxas.



![img](assets/en/15.webp)



#### Segregação do UTXO



Por uma questão de exaustividade, o Nunchuk também permite, entre as suas caraterísticas, segregar um (ou mais) UTXOs e fá-lo de duas formas diferentes. Acede ao menu _Ver moedas_ e escolhe manualmente a partir da lista de moedas. Depois, clica no menu _Mais_ no canto inferior direito: aparecerá uma lista de opções, a partir da qual podes escolher _Bloquear moedas_.



![img](assets/en/39.webp)



![img](assets/en/40.webp)



Também pode clicar no espaço reservado ao UTXO para aceder à janela _Detalhes da moeda_. Aqui, o comando para bloquear/desbloquear a UTXO em questão aparece no canto superior direito.



![img](assets/en/41.webp)



### Aplicação Blockstream



O ambiente de trabalho da Blockstream App, anteriormente conhecido como Green, permite-lhe fazer a seleção do Coin quando já tiver começado a construir a transação. Portanto, abra o seu Wallet e clique em _Send_.



![img](assets/en/16.webp)



Colar o Address de destino no campo adequado e, em seguida, selecionar _Selecção manual do Coin_.



![img](assets/en/17.webp)



Isto abre a janela onde pode selecionar uma ou mais moedas UTXO. No exemplo abaixo, selecionámos duas moedas. Em seguida, confirme a sua escolha clicando em _Confirmar seleção Coin_.



![img](assets/en/18.webp)



Defina o montante e as taxas e, em seguida, prossiga normalmente com a sua transação.



![img](assets/en/19.webp)



⚠️ N.B. No menu _Coins_ do Green existem itens _Lock_/_Unlock_ que prenunciam a possibilidade de segregar o UTXO. Este recurso é ativado apenas nas chamadas contas Multisig; também é ativado apenas selecionando UTXO de valor muito pequeno, próximo ao limite de `Dust`.



## Wallet móvel



As carteiras também podem ser escolhidas a partir do telemóvel, o que permite que os UTXOs sejam selecionados manualmente. Vejamos a Blue Wallet como primeiro exemplo.



### Azul Wallet



Se é utilizador deste Wallet, abra-o e clique para entrar nos ecrãs de controlo relativos a uma das suas Carteiras. Para aceder ao manual de controlo do Coin, é necessário entrar na fase de despesas e clicar em _Enviar_.



![img](assets/en/21.webp)



No ecrã seguinte, selecionar os menus indicados pelos três pontos no canto superior direito. Abre-se uma janela suspensa com uma série de comandos. Escolha o último: _Controlo de moedas_.



![img](assets/en/22.webp)



Nesta altura, o Blue Wallet mostra todos os seus UTXOs. Para além das quantidades, são diferenciados graficamente por cores diferentes.



![img](assets/en/27.webp)



Escolha o UTXO a selecionar e depois selecione _Use Coin_.



![img](assets/en/23.webp)



O Blue Wallet leva-o de volta à janela _Enviar_ para continuar a construir a transação. Ajustar o montante e as taxas e, em seguida, selecionar _Next_.



![img](assets/en/24.webp)



Nesta altura, pode terminar a transação, como normalmente faz.



#### Segregação de um UTXO



O Wallet azul também permite segregar os UTXOs, tornando-os indisponíveis para serem gastos, o que não é uma má função para um Wallet a partir de um dispositivo móvel. Acede-se ao controlo Coin com o procedimento que acabámos de explicar e, depois de selecionar o UTXO, escolhe-se _Freeze_ em vez de _Use Coin_.



![img](assets/en/26.webp)



### Matraca



A versão móvel do Nunchuk também permite ao utilizador controlar o Coin. Se utilizares esta aplicação a partir do telemóvel, abre-a e vai ao menu _Carteira_. A partir daí, escolhe _Ver moedas_.



![img](assets/en/30.webp)



Na janela onde aparece a lista de UTXOs, clique em _Select_.



![img](assets/en/38.webp)



Uma função de seleção aparece ao lado de cada UTXO. Tal como na versão para computador, a seleção manual no Nunchuk mobile faz-se assinalando o quadradinho ao lado do montante. O ecrã mostra o número de UTXOs selecionados e o montante total disponível. Quando terminar, clique no símbolo ₿ no canto inferior esquerdo, que é o comando para começar a construir a transação.



![img](assets/en/31.webp)



Agora pode concluir a transação, escolhendo o montante e clicando em _Continuar_.



![img](assets/en/32.webp)



Continue como sempre faz, colando um destino Address, uma descrição e personalizando as definições de taxas.



#### Segregação do UTXO



Também podes separar UTXOs com o Nunchuk móvel. Acede à janela da lista de moedas dedicadas e seleciona a seta junto ao UTXO que pretendes separar.



![img](assets/en/42.webp)



Verá o espaço reservado a _Detalhes da moeda_, onde pode selecionar _Bloquear esta moeda_.



![img](assets/en/43.webp)



### Bitcoin Keeper



O Bitcoin Keeper é o último Wallet que veremos neste guia. Vemos a sua funcionalidade aplicada ao controlo do Coin com um Wallet single-sig, embora essa utilização não seja o objetivo desta aplicação específica. Depois de configurar o Keeper no seu telemóvel, inicie-o e abra um Wallet que contenha alguns fundos. No centro do ecrã principal, clique em _Ver todas as moedas_.



![img](assets/en/34.webp)



O Keeper mostra uma visão geral dos UTXOs. Para aceder ao ecrã de seleção, clique em _Seleccionar para enviar_.



![img](assets/en/35.webp)



Pode selecionar moedas marcando-as clicando no comando adequado. Quando terminar, clique em _Enviar_.



![img](assets/en/36.webp)



O Bitcoin Keeper leva-o diretamente para o menu _Send_, onde pode construir a transação com os UTXOs selecionados.



![img](assets/en/37.webp)



## Hardware Wallet



Cada uma das Carteiras de Software vistas neste guia pode ser o Interface apenas de vigilância para uma das suas Carteiras de Hardware. Isto significa que o controlo do Coin para o dispositivo de assinatura offline é realizado com os passos vistos até agora.



### Recomendações gerais



O controlo Coin é uma prática muito eficaz para selecionar os inputs das suas transacções. A seleção manual é ainda mais eficaz se, ao comprar/receber os seus fundos, tiver identificado bem a origem dos seus Satoshis. Se quiser aprender bem esta técnica, recomendo o seguinte tutorial:



https://planb.network/tutorials/privacy/on-chain/utxo-labelling-d997f80f-8a96-45b5-8a4e-a3e1b7788c52

Já falámos anteriormente da `segregação dos restos`. Se você quiser bloquear os restos para processamento posterior e recuperar a privacidade (troca no Layer 2), você deve ter o cuidado de `rotulá-los` cada vez que receber um. Das carteiras de software vistas até agora, apenas a Electrum colore graficamente os restos de UTXO para torná-los visíveis num relance. Outras, como a Sparrow, mostram a cadeia no caminho de derivação do UTXO individual (`m/84'/0'/0'/1/11`).



Para aplicar esta técnica de forma eficaz, lembre-se de acrescentar sempre uma descrição ao troco que recebe: a pessoa a quem enviou os seus fundos (um pagamento, um tutorial ou outro) conhece o Address associado ao troco e sabe que lhe pertence, uma vez que provém da transação que fizeram juntos!