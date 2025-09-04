---
name: JoinMarket

description: Guia e tutorial sobre como utilizar o JoinMarket para efetuar CoinJoin sobre Bitcoin através da linha de comandos
---

![cover](assets/cover.webp)



---

Se encontrou esta página através de uma pesquisa online por "JoinTmarket", tem o meu sincero agradecimento. No entanto, tropeçou num guia que trata de um tópico completamente diferente, mas extremamente interessante! 🚬🍁



O objetivo deste tutorial é ilustrar o funcionamento teórico e prático do JoinMarket, através da linha de comandos. 🐢 💚



## Definição teórica da JoinMarket



Podemos definir o JoinMarket como uma ferramenta, ou um Wallet, que permite o CoinJoin com outros utilizadores de uma forma totalmente Trustless e sem qualquer coordenador central.



Uma vez que toda a parte teórica desta ferramenta é extremamente vasta, decidi fazer um Address num episódio específico do meu podcast. Para quem percebe italiano, recomendo vivamente que continue a ler depois de ouvir o episódio, de modo a assimilar melhor os conceitos básicos para utilizar corretamente este programa.



Pode acompanhar o episódio nestas ligações diretas:




- [Spotify] (https://open.spotify.com/episode/1UaeQxpNq9capLE3KwArbo)
- [Google podcast](https://podcasts.google.com/feed/aHR0cHM6Ly9hbmNob3IuZm0vcy9iZDVkNWIyMC9wb2RjYXN0L3Jzcw/episode/N2Y1NmRlZDAtZTc4Mi00MDJmLTk3ODktODIyYzgwODBjODYx?sa=X&ved=0CAUQkfYCahcKEwjohMaiv6n8AhUAAAAAHQAAAAAQEw)
- [Amazon music](https://music.amazon.it/podcasts/b1b27a88-c1c9-48de-a301-20f31d29c676/episodes/54dec992-5b03-463a-bb98-f653b72ccb63/il-priorato-del-Bitcoin-joinmarket-dalla-teoria-alla-pratica---turtlecute)
- [Anchor](https://Anchor.fm/turtle-cute5/episodes/Joinmarket-dalla-Teoria-alla-Pratica---Turtlecute-e1t0bep) (aqui pode ouvir diretamente a partir do browser).
- o [Antenna pod](https://antennapod.org/) é um gestor de podcasts gratuito e de código aberto que não requer registo. Para encontrar o episódio, descarregue a aplicação, adicione manualmente o meu podcast colando [this link](https://Anchor.fm/s/bd5d5b20/podcast/rss) na secção _feed rss_ e, em seguida, procure o episódio dedicado ao JoinMarket.



## Instalação



Sistemas operativos:





- Raspiblitz
- Guarda-chuva
- MeuNó
- Raspibolt



## Ficheiros de configuração



O JoinMarket é um software personalizável com um número infinito de configurações; estas configurações são especificadas num ficheiro de configuração localizado no diretório principal do programa chamado `Joinmarket.cfg`.



Nesta secção, vamos abordar alguns campos que pode achar interessante explorar e/ou modificar, dependendo das suas necessidades. Gostaria de sublinhar que todas as alterações listadas abaixo são úteis para adaptar o funcionamento do software às necessidades pessoais, mas não são obrigatórias.



Primeiro vamos para a pasta `joinmarket/scripts` e executamos o comando:



```bash
python wallet-tool.py generate
```


Neste ponto, deveríamos receber um erro, mas ao fazê-lo, o software irá fazer com que o generate crie um ficheiro de definições pré-definido para nós. Podemos ir e editar o ficheiro de definições a partir do terminal com:



```bash
nano joinmarket.cfg
```



ou:



```bash
vim joinmarket.cfg
```



uma vez aberto, notaremos numerosas linhas com várias definições e a sua explicação em inglês. Analisaremos de seguida as variáveis mais interessantes:





- `merge_algorithm` no caso de fazermos como um criador este campo ajusta a agressividade com que o software irá consolidar as saídas não gastas. No caso de termos muitos UTXOs para consolidar, pode fazer sentido mudar de _gradual_ para _greedy_
- o `tx_fees` ajusta como tomador as taxas com que se paga a transação, é muito útil alterar esta configuração no caso de utilizar o tumbler com frequência (falaremos disto mais à frente) pois se houver um pico nas taxas durante a execução desta última, se não configurarmos este campo corretamente, corremos o risco de gastar muito Sats para CoinJoin. Ao definir valores em milhares (como 2000), isso equivalerá a 2 Sats/vBytes, 3500 a 3,5 Sats/vBytes, e assim por diante. Eu recomendaria um número entre 1500 e 6000, dependendo das suas necessidades.
- `max_cj_fee_abs` é usado para especificar quanto estamos dispostos a pagar em termos absolutos para os criadores que escolhemos durante a CoinJoin. Por padrão este campo para criadores é 200 Sats, uma boa opção pode ser um número entre 200 e 1000 Sats por contraparte (isto é baseado em quanto você quer gastar e quanto anon-set você procura para seus CoinJoins)
- `max_cj_fee_rel` tem a mesma função que o campo acima, mas especifica as taxas relativas (percentagens) que estamos dispostos a pagar a cada contraparte. Uma vez que este é um valor `percentual`, tenha cuidado para não definir valores altos para evitar custos elevados em CoinJoins com grandes quantidades. O valor por defeito para os makers é _0.00002_, recomendo um valor semelhante ou ligeiramente superior.
- o `minimum_makers` é o campo que especifica com quantas outras contrapartes fazemos CoinJoin, por defeito o joinMarket escolhe sempre entre 4 e 9 contrapartes, se quisermos, para maior privacidade, podemos aumentar este valor para 5 ou 6 (no entanto, tornará as transacções mais caras).
- o `cjfee_a` especifica, no caso de actuarmos como maker, quantos Sats em termos absolutos queremos cobrar pelo aluguer da nossa liquidez. Este campo é totalmente subjetivo, o valor por defeito já é muito bom (teremos assim melhor privacidade como maker), podemos considerar levá-lo para 0 se quisermos ganhar mais CoinJoin em menos tempo.
- `cjfee_r` igual ao campo anterior, mas em termos percentuais e não absolutos. Mais uma vez, recomendo deixar o valor predefinido ou baixá-lo para atrair mais utilizadores.
- `ordertype` com este campo escolhemos do maker se queremos cobrar absolutamente (absoffer) ou percentagem (reloffer). Normalmente os compradores preferem ofertas absolutas para questões económicas.
- `minsize` se, como criador, não quisermos que o UTXO seja demasiado pequeno, podemos especificar o CoinJoin mínimo para participar. Este campo é expresso em Satoshi e é totalmente subjetivo. Podemos deixar este campo em 0 ou aumentar para 500000 (Sats), 1000000 (Sats), e assim por diante.



Tenha muito cuidado para não editar os campos errados, algumas das variáveis no ficheiro joinmarket.cfg, se definidas incorretamente, podem comprometer a funcionalidade do software ou aniquilar completamente a sua privacidade



## Configuração do ambiente de trabalho



Alguns nós definem automaticamente os valores corretos para estes campos no ficheiro joinmarket.cfg. Recomendo que volte a verificar manualmente:





- `rpc_user = seu-nome-de-usuário-como-no-Bitcoin.conf`
- `rpc_password = yourpassword-as-in-Bitcoin.conf`
- `rpc_host = localhost #default normalmente correto`
- `rpc_port = 8332 # padrão para Mainnet`



Nesta altura, podemos prosseguir com a criação do nosso Wallet no JoinMarket:



```bash
python wallet-tool.py generate
```



Este comando permite-nos introduzir uma palavra-passe para encriptar o Wallet e o nome que lhe queremos dar. Quando lhe perguntar se quer ou não suportar obrigações de fidelidade, recomendo que utilize a opção _yes_:



```bash
(jmvenv)$ python wallet-tool.py generate
Write down this wallet recovery mnemonic on paper:

matter aim multiply december stove march wolf nuclear yard boost worth supreme

Enter wallet encryption passphrase:
Reenter wallet encryption passphrase:
Input wallet file name (default: wallet.jmdat):
saved to wallet.jmdat
```


se aparecer um erro, é muito provável que tenhamos definido incorretamente os 4 campos RPC especificados acima. Neste caso, poderá ser útil seguir [este guia] (https://github.com/JoinMarket-Org/joinmarket-clientserver/blob/master/docs/USAGE.md#configure) que se encontra na documentação original do JoinMarket.



Nós completamos a configuração do nosso ambiente de trabalho e podemos começar a explorar os comandos que serão mais úteis para nós. Todos os scripts que discutiremos podem ser iniciados no console seguido de `--help` para uma explicação detalhada.



Podemos agora tentar lançar:



```bash
python wallet-tool.py *nome del wallet prima creato*
esempio: python wallet-tool.py wallet.jmdat
```



este comando mostrar-lhe-á todos os vários Wallet mixdepths com os vários endereços categorizados como:




- Novo (Address nunca utilizado)
- Mudança (remanescente de uma transação anterior)
- Cj-out (saída de um CoinJoin)



eis um exemplo prático do resultado:



```bash
JM wallet
mixdepth	0	xpub6CMAJ67vZWVXuzjzYXUoJgWrmuvFRiqiUG4dwoXNFmJtpTH3WgviANNxGyZYo27zxbMuqhDDym6fnBxmGaYoxr6LHgNDo1eEghkXHTX4Jnx
external addresses	m/84'/0'/0'/0	xpub6FFUn4AxdqFbnTH2fyPrkLreEkStNnMFb6R1PyAykZ4fzN3LzvkRB4VF8zWrks4WhJroMYeFbCcfeooEVM6n2YRy1EAYUvUxZe6JET6XYaW
m/84'/0'/0'/0/0     	bc1qt493axn3wl4gzjxvfg03vkacre0m6f2gzfhv5t	0.00000000	new
m/84'/0'/0'/0/1     	bc1q2av9emer8k2j567yzv6ey6muqkuew4nh4rl85q	0.00000000	new
m/84'/0'/0'/0/2     	bc1qggpg0q7cn4mpe98t29wte2rfn2rzjtn3zdmqye	0.00000000	new
m/84'/0'/0'/0/3     	bc1qnnkqz8vcdjan7ztcpr68tyec7dw2yk8gjnr9ze	0.00000000	new
m/84'/0'/0'/0/4     	bc1qud5s2ln88ktg83hkr6gv9s576zvt249qn2lepx	0.00000000	new
m/84'/0'/0'/0/5     	bc1qw0lhq7xlhj7ww2jdaknv23vcyhnz6qxg23uthy	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/0'/1
Balance:	0.00000000
Balance for mixdepth 0:	0.00000000
mixdepth	1	xpub6CMAJ67vZWVXyTJEaZndxZy9ACUufsmNuJwp9k5dHHKa22zQdsgALxXvMRFSwtvB8BRJzsd8h17pKqoAyHtkBrAoSqC9AUcXB1cPrSYATsZ
external addresses	m/84'/0'/1'/0	xpub6FNSLcHuGnoUbaiKgwXuKpfcbR63ybrjaqHCudrma13NDqMfKgBtZRiPZaHjSbCY3P3cgEEcdzZCwrLKXeT5jeuk8erdSmBuRgJJzfNnVjj
m/84'/0'/1'/0/0     	bc1qhrvm7kd9hxv3vxs8mw2arcrsl9w37a7d6ccwe4	0.00000000	new
m/84'/0'/1'/0/1     	bc1q0sccdfrsnjtgfytul5zulst46wxgahtcf44tcw	0.00000000	new
m/84'/0'/1'/0/2     	bc1qst6p8hr8yg280zcpvvkxahv42ecvdzq63t75su	0.00000000	new
m/84'/0'/1'/0/3     	bc1q0gkarwg8y3nc2mcusuaw9zsn3gvzwe8mp3ac9h	0.00000000	new
m/84'/0'/1'/0/4     	bc1qkf5wlcla2qlg5g5sym9gk6q4l4k5c98vvyj33u	0.00000000	new
m/84'/0'/1'/0/5     	bc1qz6zptlh3cqty2tqyspjk6ksqelnvrrrvmyqa5v	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/1'/1
Balance:	0.00000000
Balance for mixdepth 1:	0.00000000
mixdepth	2	xpub6CMAJ67vZWVY2cq5fmVxXw92fcgTchphGNFxweSiupYH1xYfjBiK6dj5wEEVAQeA4JcGDQGm2xcuz2UsMnDkzVmi2ESZ3xey63mQMY4x2w2
external addresses	m/84'/0'/2'/0	xpub6DqkbMG3tj2oixGYniEQTFamLCHTZx9CeAbUdBttiGuYwgfGZbrLMor8LWeJBUqTpsa81JcJqAUXuDxhXdLpKDxJAEqKMqPgJyXstj5dp3o
m/84'/0'/2'/0/0     	bc1qwtdgg928wma8jz32upkje7e4cegtef7yrv233l	0.00000000	new
m/84'/0'/2'/0/1     	bc1qhkuk2gny4gumrxcaw999uq3jm3fjrjvcwz7lz3	0.00000000	new
m/84'/0'/2'/0/2     	bc1qvu753lkltc8akfasclnq89tdv8yylu2alyg76y	0.00000000	new
m/84'/0'/2'/0/3     	bc1qal3r040k26cw2f08337huzcf00hrnws5rhfrz3	0.00000000	new
m/84'/0'/2'/0/4     	bc1qpv4nm7wwtxesgwsr0g0slxls33u0w02gqx2euk	0.00000000	new
m/84'/0'/2'/0/5     	bc1qk3ekjzlvw3uythw738z7nvwe2sg93w2rtuy6ml	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/2'/1
Balance:	0.00000000
Balance for mixdepth 2:	0.00000000
mixdepth	3	xpub6CMAJ67vZWVY3uty61M6jeGheGU5ni5mQmqMW2QLQbEa8ZQXuBw1K2umKFZsmU8EMEafJZKQkGS1trtWE5dtz4XmDbvLvUccAPn26ZC5i2o
external addresses	m/84'/0'/3'/0	xpub6EvT4QFPRdkt2sji3QdLLZjkJQmk7G2y3umT99ceomKTXGYvZ5S9TLaGos6cEugXEuxS6s9kvSUj1Xvpiu65dn5yzK7CgdZLzXawpKC9Mpe
m/84'/0'/3'/0/0     	bc1q9ph5l2gknjezcmzv84rnhu4df566jgputzef7l	0.00000000	new
m/84'/0'/3'/0/1     	bc1qrlvmmxfuryr3mfhssjv45h0fl6s43g3vzrkwca	0.00000000	new
m/84'/0'/3'/0/2     	bc1q40xkajgv9q42ve92zstwjc9v4jgauxme9su6uc	0.00000000	new
m/84'/0'/3'/0/3     	bc1q38pfk8yfnu97v4mckkuk2dhk9u8geuyzu9c0hc	0.00000000	new
m/84'/0'/3'/0/4     	bc1q2qzxyw56em9qdxc5z5s5xjz3j6s2qlzn3juvtu	0.00000000	new
m/84'/0'/3'/0/5     	bc1qd2f8f3dau5pfjqu7dpuvt6fahj36w4rgl3xevr	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/3'/1
Balance:	0.00000000
Balance for mixdepth 3:	0.00000000
mixdepth	4	xpub6CMAJ67vZWVY7gT4oJQBMc1fhbausT57yNVLCLCMwaGed5spHKaQY1EMQxvL2vTgDfhEimuAy7bzBE1qx5uY6D7cpUjQtXPHpyJzFuUtQPN
external addresses	m/84'/0'/4'/0	xpub6EQWpKsBTG3N9TFU4v6WtCcBJuLAeTZTcUwVJTxYUAsHeVPFdey4qT1dg4G7MqvnFFgHZDxqTo37S81UWUA2BqKKoTff1pcHTcSFzxyp5JG
m/84'/0'/4'/0/0     	bc1qdpjh3ewm367jm5eazqdf8wfrm09py50wn47urs	0.00000000	new
m/84'/0'/4'/0/1     	bc1q2x0fmtms5nr3wz3x3660c8wampg7t22e6m30t8	0.00000000	new
m/84'/0'/4'/0/2     	bc1q23595yg3dkj8gd3jrgup0hyzslhzf9skrg50r5	0.00000000	new
m/84'/0'/4'/0/3     	bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl	0.00000000	new
m/84'/0'/4'/0/4     	bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes	0.00000000	new
m/84'/0'/4'/0/5     	bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa	0.00000000	new
Balance:	0.00000000
internal addresses	m/84'/0'/4'/1
Balance:	0.00000000
Balance for mixdepth 4:	0.00000000
Total balance:	0.00000000
```


Agora podemos continuar a depositar os nossos primeiros Satoshis num ou mais endereços, lembrando que, independentemente do fabricante ou do comprador, o software nunca irá consolidar diretamente o UTXO em diferentes mixdepths, desta forma podemos manter os Satoshis com diferentes níveis de privacidade separados dentro do Wallet.



## Envio de Bitcoin com CoinJoin Single



Podemos agora mover os nossos Satoshis. Um dos principais comandos deste software é o script:



```bash
pyhton sendpayment.py
```


que nos permitirá enviar transacções para outros endereços com ou sem CoinJoin. Vamos ver como funciona e alguns exemplos práticos. Por padrão, a formatação do comando é (lembre-se de substituir o texto entre os símbolos < e >):



```bash
python sendpayment.py <option that can be viewed with --help> <wallet name> <satoshis amount> <destination address>
```



um exemplo básico de utilização pode ser:



```bash
python sendpayment.py wallet.jmdat 5000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


neste caso, vamos enviar para o Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c 0.05 Btc i.e. 5000000 Satoshi da nossa mixdepth 0 (a predefinição) escolhendo entre 4 e 9 contrapartes para o CoinJoin (opção predefinida).



Para ter mais controlo sobre como e quais os UTXOs a gastar, podemos ver as opções adicionais deste comando:



```bash
python sendpayment.py -N 5 -m 1 wallet.jmdat 100000000 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```


neste exemplo, acrescentámos duas especificações: -N indica com quantas contrapartes nos vamos misturar, -m a profundidade da mistura da qual vamos retirar fundos. De facto, enviámos 100.000.000 Sats (1 btc) para o Address 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c com os fundos em mixdepth 1 e misturando com 5 contrapartes.



Se colocarmos 0 como valor de envio, especificando um mixdepth, o joinMarket realizará um chamado `sweep`, ou seja, enviará todos os fundos nesse mixdepth consolidando-os uns com os outros:



```bash
python sendpayment.py -N 7 -m 0 wallet.jmdat 0 1mprGzBA9rQk82Ly41TsmpQGa8UPpZb2w8c
```



aqui enviámos todos os fundos da profundidade de mistura 0 (podíamos não a ter especificado porque é a predefinição) misturando-os com 7 contrapartes.



O comando sendpayment é usado para mover fundos do joinMarket para Wallet externos ou para enviar Satoshi a uma pessoa, adicionando um Layer de privacidade entre nós e ela. Para obter um nível suficiente de privacidade nos nossos UTXOs, é mais apropriado usar o comando tumbler.py, que explicaremos mais adiante neste guia.



## Ser um Criador



O script que vamos abordar nesta secção é:



```bash
yg-privacyenhanced.py
```



Este programa é utilizado para atuar como um maker no joinMarket. O software ligar-se-á ao nosso nó Bitcoin e ao mercado interno da plataforma, no qual os makers se apresentam como licitadores de liquidez e os takers procuram contrapartes. Caso pretenda utilizar um título de fidelidade, pode criá-lo com esta formatação:



```bash
python3 wallet-tool.py <wallet name> gettimelockaddress <block date, written in YYYY-MM format>
```



por exemplo:



```bash
python3 wallet-tool.py testwallet.jmdat gettimelockaddress 2025-11
```



a saída que nos será devolvida será um Bitcoin Address (ou seja, aquele em que terá de depositar os fundos que pretende afetar à fidelidade).



**Cuidado**: Há duas coisas a que deve prestar muita atenção se quiser criar uma Fidelity Bond (também conhecida como FB);





- uma vez depositados os fundos, não podem ser movimentados novamente até à sua expiração. Presta atenção ao número de Satss que envias para o Address e à forma como formatas a data. Não são permitidos erros!
- O título de fidelidade é facilmente reconhecível na cadeia, por isso é aconselhável depositar fundos através de um CoinJoin e com uma origem não relacionada com a sua identidade. A mesma coisa também é aconselhável fazer quando quiser mover o título de fidelidade expirado para fora do JoinMarket.



É importante recordar que é possível recarregar a obrigação de fidelidade com apenas uma transação; no caso de múltiplos UTXO, apenas o maior será considerado válido para o FB.



Vamos agora tratar do script mencionado no início deste parágrafo, uma vez criado o título de fidelidade (que lembramos ser opcional), estamos prontos para executar o executável para atuar como um maker na joinMarket. Uma vez que os Satss tenham sido depositados nos vários endereços e mixdepth, podemos executar o comando:



```bash
python yg-privacyenhanced.py <wallet name>
```



A partir deste momento (após alguns minutos de ligação à rede) e até pararmos o script, o nosso cliente JoinMarket aparecerá na lista de makers activos no protocolo e oferecerá a nossa liquidez a várias contrapartes para fazer CoinJoin. Não espere dezenas de CoinJoins por dia (a menos que tenha uma enorme fidúcia e grande liquidez depositada no Wallet), lembre-se também que factores como as taxas exigidas e os Satoshis depositados afectam a frequência com que será um maker.



Ao executar o comando abaixo, poderá ver o histórico de todas as transacções feitas no Wallet e qualquer ganho (se for um criador) ou despesa de taxa (se for um comprador) que tenha tido durante o tempo de vida do Wallet.



```bash
python wallet-tool.py <wallet name> history
```



Quando as tuas Satoshis fizerem CoinJoins, passarão de mixdepth para mixdepth até chegarem ao último. Depois de passarem o quarto, voltam para o mixdepth 0. Cabe-te a ti decidir quanta privacidade queres ter antes de os transferires para um Cold Wallet, sendo aconselhável terminar um ciclo completo do Wallet.



## Copo



Aqui estamos finalmente na parte mais sumarenta do JoinMarket, o tumblr! Se ouviram o podcast, já sabem do que se trata. Uma recomendação antes de começarmos: **Lembre-se de definir os limites no ficheiro joinmarket.cfg (como explicado no início) e considere executar o programa apenas quando as taxas onchain são relativamente baixas (menos de 10 Sats/vB).



Para lançar o tumblr é necessário ter parado o script do maker (se estava ativo), depois disso podemos executar o comando:



```bash
python tumbler.py <wallet name> <receiving address (1)> <receiving address (2)> <receiving address (3)>
```



É essencial introduzir **pelo menos** 3 endereços de saída para o tumbler: isto é para assegurar uma boa privacidade e para não criar ligações óbvias entre UTXOs ao longo do processo. Como de costume, adicionando`--help` ao comando, pode ver todos os detalhes adicionais. Vamos ver um exemplo mais complexo com regras avançadas:



```bash
pyhton tumbler.py TestWallet.jmdat -N 7 2 -c 3 1 bc1qz3f80rtv0ux85d7rc06ldtvmpqyfx6ly48c9pa bc1qf3wljw44utyv7qd0z57zvdkfl20y470mva0nes bc1qw48asjpkwm3k2w8cketqhrre0uwq9f7ypwzmxl
```



Neste caso, lançámos um script de tumbling que não utilizará o número predefinido de contrapartes (o parâmetro -N indica que necessitamos de 7 contrapartes com uma variância máxima de 2, ou seja, um número aleatório de fabricantes de 5 a 9) e com um número maior de CoinJoin por profundidade de mistura (por predefinição, este script cria um número aleatório de CoinJoin por secção de Wallet que varia de 1 a 3, utilizando o comando -c 3 1, em vez disso, será de 2 a 4). Desta forma, gastaremos mais Sats em taxas mas teremos um conjunto de anonimato maior.



Também pode adicionar tantos endereços de saída quantos quiser (mínimo 3, não há máximo para além do senso comum). No entanto, não é possível, por questões de privacidade, decidir como o Satoshi será distribuído entre os endereços especificados como saída.



O Tumbler é um processo deliberadamente longo, ocasionalmente pode acontecer que algo deixe de funcionar, na maioria dos casos isto resolve-se em poucas horas. No caso de uma falha total, podemos tentar reiniciá-lo com o comando:



```bash
python tumbler.py --restart
```



Ou simplesmente reiniciar um novo comando de tombamento. Isso não iniciará o agendamento do tombador anterior, mas iniciará um novo ciclo de mistura. No caso de fechar o terminal SSH do seu nó também parar o script, pode tirar partido do programa `TMUX` que pode ser instalado com o comando:



```bash
sudo apt install tmux
```



Ao iniciá-lo a partir da shell, digitando `tmux`, abrirá um terminal que permanecerá ativo em segundo plano mesmo que feche a ligação remota. Quando você se conectar novamente ao seu nó com o comando: `tmux attach` você abrirá novamente o shell que permaneceu ativo em segundo plano.



## Conclusão



O JoinMarket é um software ilimitado e personalizável. Neste guia descobrimos as principais funções para que seja possível a qualquer pessoa (ou pelo menos eu tentei, sei que usar este software não é fácil) usá-lo. Um dos maiores problemas do JoinMarket é exatamente esse: o número de pessoas que o utilizam e que são criadores. Se poucos utilizadores tirarem partido deste software, a privacidade geral (anon-set) é reduzida. É por isso que espero que este guia incentive a utilização e o convença a descarregar e instalar o meu software favorito para fazer CoinJoin. No caso de quereres aprofundar alguns aspectos, recomendo-te que leias os vários documentos detalhados no github, estão muito bem feitos e podes encontrá-los aqui.



Feliz mistura de tartarugas!🐢 💚



[Aqui] (https://btcpay.priorato.org/api/v1/invoices?storeId=2B1STLH5REvhHZBRQuyJNieRTexpeuJ4Usjn4ziEfEfd&currency=EUR) pode apoiar o Turtlecute