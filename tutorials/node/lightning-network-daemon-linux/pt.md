---
name: Lightning Network Daemon (Linux)
description: Instalando e executando o Lightning Network Daemon no Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



O Lightning Network é um segundo Layer do Bitcoin, que lhe permite assumir dimensões relâmpago, graças, nomeadamente, à rapidez e ao baixo custo das transacções que oferece.



Neste tutorial, vamos instalar a implementação do Lightning Network Daemon na nossa máquina Linux (distribuição Ubuntu 24.04).



## O que é o Lightning Network Daemon?



Lightning Network Daemon é uma implementação completa em Go do Lightning Network. Foi criado pela Lightning Labs e permite-lhe executar uma instância completa de um nó Lightning na sua máquina.


Por outras palavras, com esta implementação, é possível :





- Interagir com o Lightning Network**: Pode utilizar linhas de comando para criar carteiras Lightning, gerir canais e rotas de pagamento, e muito mais, diretamente a partir do terminal da sua máquina.
- Vinculação de um nó Bitcoin remoto ou sua própria instância Bitcoin Core**: O LND permite que você vincule uma instância do Bitcoin e use-a como seu backend. Para usar esta implementação, não é necessário executar uma instância do Bitcoin Core na sua máquina.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Porquê ter o seu próprio nó Lightning?


O Lightning é uma sobreposição Bitcoin que optimiza o processo de transferência e reduz os custos de transação.



Ao rodar o seu Lightning node, ganha soberania e autonomia. Está no controlo dos seus fundos, por isso, tenha em mente:



"Nem as vossas chaves, nem os vossos bitcoins."



Nesse sentido, a execução de um nó Lightning aumenta a segurança e a integridade dos seus dados das seguintes maneiras:





- Controlo total**: Gerir os seus próprios canais de pagamento, tornar-se o seu próprio banco e ser dono dos seus activos.
- Confidencialidade**: Efectue transacções sem depender de terceiros para proteger a sua privacidade.
- Aprendizagem e autonomia**: Graças aos comandos `lncli`, você pode entender melhor os processos subjacentes do Lightning aplicando-se a partir do seu terminal.
- Descentralização**: Desempenhar um papel ativo no reforço e descentralização do Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Há duas opções para executar uma instância da implementação do LND em nossa máquina. Podemos configurar o ambiente em nossa própria máquina para ser executado localmente ou instalar o LND a partir de um contêiner Docker. Aqui, vamos nos concentrar na primeira opção, e veremos como proceder com o Docker em um tutorial posterior.


## Instalar o LND a partir do código fonte



### Pré-requisitos


Como o LND é escrito em Go, é necessário certificar-se de que tem o ambiente GoLang e as dependências necessárias na sua máquina Linux.





- Requisitos de hardware:**


Para uma experiência suave e sem interrupções, a sua máquina terá de ter a capacidade necessária para executar o nó LND Lightning.



Necessita de :


1. **8 GB de RAM** para uma fluidez óptima,


2. **Um processador multi-core (quad-core ou mais)** para gerir eficientemente as acções do seu nó,


3. **Pelo menos 5 GB de espaço em disco** para o modo de nó podado e 1 TB para executar o Bitcoin Core (opcional se estiver usando um nó remoto)





- Instalar dependências úteis:**


O comando abaixo permitirá que você instale em sua máquina as ferramentas necessárias para executar o LND. Entre outras coisas, será necessário instalar o `Git`, uma ferramenta de versionamento, e o `make`, que pode executar e construir a implementação do LND a partir do código fonte.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Instalar o GoLang na sua máquina Linux**



A partir da data deste tutorial, o LND requer a versão 1.23.6 do Go*** para instalação.



Se já tinha uma versão anterior instalada, remova-a para a instalação do novo Go.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Configuração do ambiente Go**


No seu arquivo `~/.bashrc`, inicialize as seguintes variáveis de ambiente para adicionar o Go ao seu sistema Linux.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Verificação da instalação** (em francês)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Clonar o repositório GitHub do LND



Utilize o git para obter uma cópia do código fonte do LND localmente na sua máquina


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Construir e instalar



A ferramenta `make`, previamente instalada, permitirá construir um executável a partir do código fonte do LND e prosseguir com a instalação.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Instalar o LND no seu computador



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Verificar a sua instalação** (em francês)



Para ter a certeza de que tudo correu bem, correr este comando deve dar-lhe a versão do LND que está a correr atualmente.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Manutenção e actualizações



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **IMPORTANTE**: As actualizações do LND podem exigir versões mais recentes do Go, por isso certifique-se de que actualiza o seu sistema para evitar problemas de dependência durante a instalação.


### Configuração do Lightning Network Daemon



A configuração de um nó Lightning LND é semelhante à do Bitcoin, e é realizada em um arquivo de configuração contendo todos os parâmetros do seu nó. Para isso, na raiz da sua máquina você pode criar uma pasta oculta `.LND` e então criar seu arquivo de configuração `LND.conf` nesta pasta.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





No ficheiro de configuração, é possível configurar o nó LND.



```
noseedbackup=0
debuglevel=debug

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=bitcoind

[Bitcoind]
bitcoind.rpcuser=<UTILISATEUR_BITCOIN>
bitcoind.rpcpassword=<MOT_DE_PASSE_BITCOIN>
bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332
bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333

```



## Compreender a sua configuração



É importante que compreenda a configuração mínima necessária para uma instalação correta e completa do seu nó LND.



Com base no conteúdo do ficheiro `~/.LND/LND.conf`, eis os detalhes dos campos:





- noseedbackup**: Permite-lhe escolher se quer que o LND faça backups automáticos dos seus portfólios.  Definir esta propriedade como `0` permite-lhe guardar manualmente as informações de restauração num local seguro escolhido pessoalmente.





- debuglevel**: Permite definir o nível de detalhe dos erros e dos registos no caso de ocorrerem erros durante uma ação.





- Bitcoin.active**: Instrui o LND a funcionar como um nó Bitcoin e a interagir com a rede Bitcoin.





- Bitcoin.Mainnet**: Especifica o LND para se ligar à rede principal do Bitcoin (Mainnet), pode definir os valores `bitcoind.signet` e `bitcoind.regtest` respetivamente para as redes Bitcoin Signet e Bitcoin Regtest





- Bitcoin.node**: Especifica o tipo de nó Bitcoin ao qual o LND se deve ligar.





- Bitcoin.rpcuser** e **Bitcoin.rpcpassword** : Representar.


respetivamente os logins (utilizador, palavra-passe) para ligar ao seu nó Bitcoin





- bitcoind.zmqpubrawblock** e **bitcoind.zmqpubrawtx**: definem, respetivamente, pontos finais ZeroMQ para receber notificações sobre novos blocos e transacções na rede Bitcoin.




## Verificar a sua instalação com o LND



É provável que queira certificar-se de que o processo foi bem sucedido e que está a sincronizar com o Lightning Network para manter a informação do nó actualizada.



Para iniciar a implementação do LND e obter informações sobre o seu nó, basta digitar o comando :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Realização de acções no LND



Quando a instalação estiver concluída e verificada, pode começar a utilizá-la.


Aqui estão os comandos essenciais para começar.



### Criar um portefólio


A sua carteira Lightning é a primeira etapa de qualquer ação de gestão dos seus fundos.



⚠️ **IMPORTANTE**: Tome nota da sua frase de 24 palavras **seed**. Precisará dela para recuperar os seus fundos em caso de problemas.



Salve também sua senha do Wallet para que possa desbloqueá-lo com o comando `lncli unlock` quando reiniciar seu nó LND.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Verificar o seu saldo



Consulte as suas contas diretamente a partir do seu terminal:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informações sobre o seu nó



Utilize o comando abaixo para saber quais os canais que estão activos no seu nó.



```bash
lncli listchannels
```



Pode também obter uma lista dos nós aos quais está ligado.



```bash
lncli listpeers
```



### Gestão de canais



Um canal Lightning permite-lhe ter uma ligação **direta, par a par, com outro nó no Lightning Network**. Neste canal, pode utilizar livremente Satoshis Exchange até à capacidade do canal.



### Ligar a um nó



A ligação a outros nós Lightning é uma ação fundamental se quiser participar ativamente e beneficiar do poder do Lightning.



Para se ligar a um par (Lightning node), são necessárias três informações:




- A chave pública do nó**: Este é o identificador único do nó na rede Bitcoin;
- IP** : O IP da máquina em que o nó está instalado;
- PORT** :  A porta aberta na máquina que permite a comunicação com este nó.



Pode encontrar nós aos quais se ligar em [amboss](https://amboss.space/), uma plataforma que lista informação sobre nós Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Certifique-se de que se liga a **nós fiáveis** para preservar a integridade do seu próprio sistema. Aqui estão algumas recomendações para escolher as ligações corretas.





- Diversificação geográfica**: Ligação a nós em diferentes regiões.





- Reputação**: Escolher nós com boa disponibilidade.





- Capacidade**: Escolher nós com boa liquidez.





- Encargos**: Encargos de encaminhamento de cheques.


### Abrir um canal de pagamento


Para abrir um canal de pagamento, certifique-se de que está **conectado** ao nó par e, em seguida, defina a **capacidade** (a quantidade de satoshis) que pretende bloquear neste canal.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Criar um relâmpago Invoice



Um Lightning Invoice representa uma sequência de caracteres que expressa o seu desejo de receber satoshis no seu Lightning Wallet.


Criar facturas Lightning com o seu próprio nó permite-lhe proteger os seus dados (geográficos e pessoais) e dá-lhe 100% de autonomia sobre a gestão dos seus fundos.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Pagamento de um Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Fechar um canal



Existem duas formas de fechar um canal ativo no seu nó atual.





- Encerramento cooperativo**: Este procedimento assinala o desejo do nó de se retirar do canal de pagamento, garantindo que as tarefas em curso são concluídas e que é feita uma cópia de segurança dos dados para evitar a perda de fundos.


```
lncli closechannel <ID_CANAL>
```




- Encerramento forçado**: ⚠️ A evitar se possível, esta ação interrompe os processos em curso no seu canal de pagamento e aumenta o risco de perda de fundos.


```
lncli closechannel --force <ID_CANAL>
```


## Melhores práticas e segurança para o seu nó LND.


A segurança é fundamental quando se utiliza um nó Bitcoin/ Lightning. Aqui estão alguns pontos para reforçar a segurança da sua instalação:





- Guarde a sua "frase seed" num local seguro e fora de linha.





- Faça backups regulares do arquivo `~/.LND/channel.backup`: Este arquivo salva os estados dos seus canais toda vez que um novo canal é aberto (ou um canal antigo é fechado) no seu node.


⚠️ Permite-lhe restaurar canais e recuperar fundos bloqueados em canais de pagamento em caso de perda de dados ou falha do nó



Pode restaurar os seus fundos com o comando abaixo, especificando o caminho da cópia de segurança deste ficheiro:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Certifique-se de que guardou as palavras de restauro e a palavra-passe do Lightning Wallet.
- Mantenha o seu sistema atualizado.



## Resolução de problemas actuais


### Problemas frequentes




- Erro de ligação do bitcoind** : Verifique os seus dados de início de sessão do RPC
- Sincronização bloqueada** : Verifique a sua ligação à Internet
- Erro de permissão**: Verificar os direitos da pasta `~/.LND`




Então você chegou ao final deste tutorial. Se quiser saber mais sobre o Lightning, oferecemos este curso introdutório para que você entenda melhor os conceitos e as práticas por trás do Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb