---
name: Joinstr
description: CoinJoins descentralizados através da rede Nostr para confidencialidade soberana do Bitcoin
---

![cover](assets/cover.webp)



A transparência da cadeia de blocos Bitcoin torna possível rastrear o histórico das transacções. Os CoinJoins quebram estas ligações misturando múltiplas transacções simultâneas, restaurando um nível de confidencialidade comparável ao dinheiro.



No entanto, as soluções tradicionais dependem de um coordenador central como ponto único de falha. A Wasabi e a Samourai cessaram as suas actividades em 2024 sob pressão regulamentar.



*o *Joinstr** elimina essa fraqueza usando a rede descentralizada Nostr para coordenação. Esta aplicação de código aberto permite CoinJoins verdadeiramente soberanos, onde nenhuma autoridade central pode censurar, monitorizar ou interromper o serviço.



## O que é o Joinstr?



O Joinstr é uma ferramenta de código aberto que revoluciona a abordagem do CoinJoins, aproveitando o protocolo Nostr como uma infraestrutura de coordenação. Ao contrário das soluções centralizadas que requerem um servidor dedicado, o Joinstr depende de uma rede distribuída de relés Nostr para permitir que os participantes coordenem diretamente entre pares.



**Arquitetura descentralizada** : A rede Nostr substitui o coordenador central. Os participantes criam ou juntam-se a "pools" colocando anúncios encriptados através dos relés Nostr. Esta informação (quantidades, participantes, endereços) permanece ininteligível para os retransmissores, garantindo que nenhuma entidade central possa monitorizar, censurar ou filtrar CoinJoins.



*mecanismo *SIGHASH_ALL|ANYONECANPAY**: O Joinstr explora esta bandeira de assinatura Bitcoin, permitindo que cada participante assine apenas a sua entrada enquanto valida todas as saídas. Cada utilizador gera o seu PSBT localmente e depois distribui-o via Nostr. Cada utilizador gera o seu PSBT localmente, assina-o e depois distribui-o via Nostr. Os seus bitcoins permanecem sob o seu controlo exclusivo até à assinatura final.



**Filosofia**: O Joinstr segue o ethos cypherpunk do Bitcoin, visando três objectivos: **resistência à censura** (nenhuma autoridade pode parar o serviço), **não-custodialidade total** (você mantém as suas chaves privadas), e **tratamento igual** (nenhum UTXO pode ser discriminado).



### Principais caraterísticas



**Pools flexíveis**: Ao contrário das denominações fixas, qualquer utilizador pode criar um pool com o montante exato desejado e o número pretendido de participantes, optimizando a utilização do UTXO sem divisão artificial.



**Taxas transparentes**: Não há taxas de coordenação. Apenas as taxas de transação Bitcoin são partilhadas igualmente entre os participantes (alguns milhares de satoshis por pessoa).



**Efemeridade**: Nenhum dado do utilizador é retido. A informação transita através de mensagens Nostr efémeras encriptadas, imediatamente esquecidas após a transação.



### Plataformas disponíveis



Este tutorial centra-se na aplicação **Android**, a única solução atualmente estável e recomendada. Existe um plugin Electrum, mas tem problemas de compatibilidade que o tornam instável. Está a ser desenvolvida uma interface Web.



## Configuração do núcleo Bitcoin



O Joinstr Android requer uma ligação a um nó Bitcoin através do RPC. Deve primeiro configurar o Bitcoin Core no seu computador para aceitar ligações a partir do seu telemóvel.



**Nota**: Para mais pormenores sobre a configuração completa do Bitcoin Core, consulte os nossos tutoriais dedicados:



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Requisitos de rede



#### Localize o seu endereço IP local



O seu telemóvel Android deve poder aceder ao seu nó Bitcoin na rede local. Encontre o endereço IP do seu computador:



**No macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Alternativa simples:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**No Linux** :



```bash
hostname -I | awk '{print $1}'
```



**No Windows** :



```cmd
ipconfig
```



Localizar o endereço IPv4 (formato `192.168.x.x` ou `10.0.x.x`)



### Configuração do RPC



#### Editar bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Localize o seu ficheiro `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Biblioteca/Suporte a Aplicações/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Abra o ficheiro com o seu editor de texto favorito e adicione esta configuração para ativar o servidor RPC.



**Configuração recomendada para começar (marcador)** :



```conf
# Enable signet (test network)
signet=1
prune=550

# Enable the RPC server
server=1
rpcbind=0.0.0.0

# Allow connections from your local network
# Adjust according to your network (192.168.x.0/24 or 10.0.x.0/24)
rpcallowip=192.168.1.0/24

# RPC Credentials (CHANGE THESE VALUES!)
rpcuser=your_username
rpcpassword=your_strong_password

# Specific signet configuration
[signet]
rpcport=38332
```



**Configuração do mainnet** (para utilização na produção) :



```conf
# RPC Server
server=1
rpcbind=0.0.0.0
rpcallowip=192.168.1.0/24

# RPC Credentials
rpcuser=your_username
rpcpassword=your_strong_password

# Mainnet Port
rpcport=8332
```



**Importante** :




- Signet é altamente recomendado** para os seus primeiros testes: a aplicação ainda está em desenvolvimento (beta) e podem existir erros. Signet permite-lhe testar gratuitamente, sem arriscar fundos reais
- Substitua `192.168.1.0/24` pela sua sub-rede de rede (por exemplo, se o seu IP for `192.168.68.57`, utilize `192.168.68.0/24`)



**Segurança**: Gerar uma palavra-passe forte :



```bash
openssl rand -base64 32
```



### Inicialização



#### Reiniciar e verificar



1. Desligar completamente o núcleo do Bitcoin


2. Reinicie-o para aplicar a configuração




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Quando o Bitcoin Core é iniciado pela primeira vez, ele descarrega e sincroniza a cadeia de blocos de favoritos. Esta operação é muito mais rápida do que no mainnet (apenas alguns minutos). Por favor, aguarde até que a sincronização esteja completa antes de prosseguir.



![CRÉATION DE WALLET](assets/fr/04.webp)



Uma vez sincronizado, crie um novo portefólio clicando em "Criar um novo wallet". Dê-lhe um nome explícito como `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



O seu wallet está agora criado e pronto para receber bitcoins marcados para teste.



#### Obter bitcoins marcados (teste)



Para testar o Joinstr no marcador, precisa de bitcoins de teste gratuitos :



![SIGNET FAUCET](assets/fr/06.webp)



Utilize um marcador público como :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



No Bitcoin Core, generate um novo endereço de receção (separador "Receive"), copie-o e cole-o no formulário da torneira. Resolve o captcha se necessário. Receberás bitcoins grátis com marcadores em segundos.



## Aplicação Android



### Instalação



![APPLICATION ANDROID](assets/fr/07.webp)



Aceda a [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases) para transferir a versão mais recente do APK. No browser do Android, transfira o ficheiro e, em seguida, abra-o para iniciar a instalação. Terá de permitir a instalação a partir de fontes desconhecidas nas definições de segurança do seu telemóvel, se necessário.



### Configuração da aplicação



![PERMISSIONS VPN](assets/fr/08.webp)



No primeiro lançamento, a aplicação Joinstr pedirá permissões para controlar a VPN incorporada. Aceite ambos os pedidos de permissão: Controlo OpenVPN e ligação VPN. Estas permissões são necessárias para a integração da VPN, que protege a privacidade da sua rede.



![INTERFACE APPLICATION](assets/fr/09.webp)



A aplicação Joinstr está organizada em três separadores principais:




- Início**: Ecrã inicial
- Pools**: Criando e gerenciando pools CoinJoin
- Definições**: Configuração da aplicação



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Configurar as definições no separador "Definições":



**1. Nostr Relay**: Endereço de retransmissão do Nostr para coordenação do grupo




- Exemplo: `wss://relay.damus.io`
- Outros retransmissores recomendados: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Importante**: Todos os participantes devem usar o **mesmo retransmissor Nostr** para ver e participar dos mesmos pools. Se você usar um relé diferente, você não verá os pools criados em outros relés



**2. URL do nó**: Endereço IP do seu nó Bitcoin (sem porta)




- Formato: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. Nome de utilizador do RPC** : O nome de utilizador configurado em `rpcuser=` no seu bitcoin.conf




- Exemplo: `satoshi



**4. Palavra-passe RPC** : A palavra-passe definida em `rpcpassword=` no seu bitcoin.conf



**5. Porta RPC** : Porta RPC consoante a rede




- Mainnet** : `8332`
- Marcador**: `38332`



**6. Wallet**: Selecionar a carteira principal Bitcoin que contém os UTXOs a misturar




- Exemplo: `tuto_joinstr_signet`



**7. Gateway VPN**: Selecionar um servidor VPN Riseup




- Exemplo: `(Paris) vpn07-par.riseup.net`
- Outros disponíveis: Amesterdão, Seattle, etc.
- ⚠️ **Importante**: Todos os participantes da mesma pool devem usar o **mesmo Gateway VPN** para participar no CoinJoin. Durante a ronda de mistura, todos os participantes devem aparecer com o mesmo endereço IP de saída para evitar que a análise de rede correlacione os participantes



A aplicação Joinstr **integra nativamente** o Riseup VPN, simplificando a coordenação entre os participantes.



**Importante** :




- Certifique-se de que o telemóvel e o computador estão na mesma rede WiFi local
- A ligação VPN será activada automaticamente quando participar num grupo
- Clicar em **"Guardar "** depois de ter definido todos os parâmetros



## Utilização prática



### Criar ou juntar-se a um grupo



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Tem duas opções para participar num CoinJoin:



**Opção 1: Criar uma nova piscina



Clique em "Criar novo grupo" no separador "Grupos". Especifique a denominação em BTC (por exemplo, 0,002 BTC) e o número desejado de participantes (mínimo 2, recomendado 3-5 para maior anonimato). A aplicação aguarda então que outros utilizadores se juntem à sua pool. Uma vez atingido o número necessário, o processo de registo de saída começa automaticamente, e terá de selecionar o seu UTXO para misturar e clicar em "Registar".



**⏱️ Importante**: As piscinas expiram após **10 minutos** de inatividade. Se o número necessário de participantes não for atingido, a piscina será automaticamente encerrada.



**Opção 2: juntar-se a um grupo existente



No separador "Ver outros agrupamentos", procure os agrupamentos disponíveis criados por outros utilizadores. Selecione a pool que corresponde à sua quantidade e junte-se a ela. Certifique-se de que configurou o mesmo Nostr relay e VPN Gateway que os outros participantes (ver secção Configuração).



**Regra de seleção do UTXO**: O seu UTXO tem de ser ligeiramente superior à denominação da lotaria (entre +500 e +5000 sats excedente).



**Exemplo**: Para um conjunto de 0,002 BTC (200.000 sats), utilize um UTXO entre 200.500 e 205.000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



O processo é então **totalmente automático**: uma vez registada a sua entrada, a aplicação aguarda que todos os participantes registem as suas entradas. Uma vez registadas todas as entradas, o PSBT é criado, assinado automaticamente com as suas chaves e depois combinado com as assinaturas dos outros participantes. Finalmente, a transação completa é transmitida na rede Bitcoin. O utilizador recebe o TXID (identificador da transação) assim que a difusão estiver concluída. Não é necessária qualquer manipulação manual do PSBT no Android.



### Verificação on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Assim que a transação for transmitida, receberá o TXID (identificador de transação). Veja-o em [mempool.space](https://mempool.space) ou no seu navegador favorito. Para testar num bookmark, utilize [mempool.space/signet](https://mempool.space/signet).



Pode observar :





- N entradas**: Uma por participante (no nosso exemplo, 2 entradas)
- N saídas idênticas**: montante exato da denominação (neste caso, 2 saídas de 0,00199800 BTC cada)
- Fluxograma**: mempool.space apresenta visualmente a mistura de entradas e saídas
- Caraterísticas** : A transação pode ser identificada como SegWit, Taproot, RBF, etc.



Como todas as saídas principais têm a mesma quantidade, é **impossível determinar qual pertence a quem**. Este é o princípio fundamental do CoinJoin: a indistinguibilidade das saídas.



**Exemplo de transação assinada** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Atenção**: Se as suas UTXOs forem maiores do que a denominação do pool, terá saídas de divisas (excedentes). Estas UTXOs de divisas permanecem rastreáveis e devem ser geridas separadamente das suas saídas anónimas. Nunca os combine com as suas saídas mistas.



## Pacotes de qualidade e anonimato CoinJoin



A eficiência de um CoinJoin é medida pelo seu **anonimato**: o número de outputs de valor idêntico produzidos pela transação. Quanto mais elevado for este número, mais difícil é determinar que entrada corresponde a que saída.



Atualmente, o Joinstr gera pools de **2 a 5 participantes** em média. Estes números são inferiores aos dos coordenadores centralizados tradicionais como Wasabi (50-100 participantes) ou Whirlpool (5-10 participantes), mas esse é o preço da descentralização.



💡 **Para compreender os conjuntos de anonimato e o seu cálculo em pormenor**, consulte o nosso curso completo: [Conjuntos de anonimato](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. outros CoinJoins



| Aspect | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Participants par pool** | 50-100 | 5-10 | Variable (P2P) | **2-5** |
| **Coordinateur** | Centralisé (fermé 2024) | Centralisé (actif) | P2P maker/taker | **Aucun (Nostr)** |
| **Résistance à la censure** | Faible | Moyenne | Très élevée | **Très élevée** |
| **Frais de coordination** | Pourcentage | Frais d'entrée | Payés aux makers | **Aucun** |
| **Discrimination UTXO** | Oui (blacklists) | Non | Non | **Non** |

💡 **Outras soluções activas de CoinJoin** :




- Ashigaru**: Implementação de código aberto do protocolo Whirlpool com coordenador centralizado, mas implementável de forma descentralizada. Continua a funcionar após a tomada do Samourai Wallet em 2024.
- JoinMarket**: Solução P2P descentralizada, sem coordenador central, baseada num modelo de negócio maker/taker em que os "makers" fornecem liquidez e são remunerados pelos "takers".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**O compromisso fundamental**: O Joinstr e o JoinMarket são as duas únicas soluções sem um coordenador central. O JoinMarket usa um modelo de negócio P2P com incentivos financeiros, enquanto o Joinstr usa o Nostr para uma coordenação sem custos. O Joinstr sacrifica o anonimato imediato em larga escala em favor da simplicidade (sem gestão de maker/taker) e da ausência total de taxas de coordenação.



**Recomendação prática**: Para compensar os grupos mais pequenos, faça várias rondas sucessivas de CoinJoin com diferentes participantes. Espaçar as rondas e mudar as estafetas Nostr entre cada ronda para maximizar a confidencialidade.



Não hesite em consultar o nosso curso completo sobre a privacidade da bitcoin para obter mais informações sobre este tema:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Vantagens e limitações



### Destaques



**Privacidade aprimorada**: A combinação da encriptação das comunicações Nostr, a VPN partilhada entre os participantes e a utilização recomendada do Tor cria uma proteção multi-camadas difícil de contornar.



**Custos mínimos e transparentes**: Sem custos de coordenação, apenas os custos mining são partilhados equitativamente entre os participantes. Nenhuma percentagem cobrada por qualquer operador.



### Restrições a considerar





- Liquidez variável**: Conjuntos mais pequenos, podem esperar que os participantes se juntem
- Projeto em curso**: Aplicação em fase beta, possíveis bugs. Teste primeiro com pequenas quantidades no marcador
- Ataques de Sybil**: Possibilidade de um adversário controlar vários participantes na piscina



## Melhores práticas



**Isolamento do UTXO**: Nunca combine um UTXO misturado com um não misturado. Utilize uma carteira separada para os seus resultados anónimos.



**É essencial efetuar várias rondas**: Efetuar um mínimo de 3 rondas sucessivas com participantes diferentes. Variar as quantidades e os tempos para evitar padrões. As rondas devem ter um intervalo de várias horas.



**Proteção de rede**: Utilizar sistematicamente o Tor para além da VPN incorporada. Gerar chaves Nostr efémeras para cada sessão importante.



**Progresso cauteloso**: Começar a marcar com pequenas quantidades.



## Conclusão



O Joinstr representa uma solução de privacidade Bitcoin verdadeiramente descentralizada. Ao utilizar o Nostr para a coordenação, elimina a dependência de coordenadores centrais, preservando a soberania do utilizador.



**Para utilizadores que valorizam a resistência à censura e estão preparados para realizar várias rondas de CoinJoin para compensar piscinas mais pequenas.



Num contexto de crescente escrutínio financeiro, as ferramentas descentralizadas para proteger a privacidade estão a tornar-se essenciais.



## Recursos



### Documentação oficial




- [Sítio Web oficial da Joinstr](https://joinstr.xyz)
- [Documentação do utilizador](https://docs.joinstr.xyz/users/using-joinstr)
- [Documentação técnica](https://docs.joinstr.xyz/overview/how-does-it-work)
- [Código fonte do GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [Aplicação Android](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Tutoriais




- [Tutorial do plugin Electrum](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Guia completo por Uncensored Tech



### Comunidade e apoio




- [Telegram Joinstr Group](https://t.me/joinstr) - Apoio comunitário e cantos de favoritos
- [Discussão técnica sobre DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Ferramentas adicionais




- [Bookmark Faucet](https://signetfaucet.com) - Teste grátis de Bitcoins
- [Alt Signet Faucet](https://alt.signetfaucet.com) - Alternativa ao Faucet
- [Mempool.space](https://mempool.space) - Block explorer com análise da privacidade