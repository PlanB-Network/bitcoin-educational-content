---
name: Neutrino
description: Guia de instalação do LND Neutrino
---
![image](assets/cover.webp)


## Configuração do Raspberry Pi com o LND


### 1. Descarregar o Raspberry Pi OS Lite


As instruções para descarregar e instalar a imagem num cartão micro SD no Windows, Mac e Linux podem ser encontradas em [esta página](https://www.raspberrypi.org/software/operating-systems/).


### 2. Formatar o cartão SD


Utilizar o Raspberry Pi Imager ou o balenaEtcher.


**Nota:** O símbolo `$` é usado como um prompt e permite ao utilizador introduzir comandos no computador, os comandos serão interpretados pelo bash no Linux. O símbolo `#` no início de uma linha indica que o texto seguinte é um comentário.


### 3. Ativar SSH


Antes de iniciar a Raspberry Pi com a memória formatada, devemos inseri-la num computador e criar dois ficheiros que nos permitirão ligar remotamente. Usando o comando `touch`, criamos um ficheiro vazio na partição /boot, permitindo a ligação SSH no primeiro arranque do cartão SD acabado de formatar.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Criar ficheiro para ligação Wi-Fi


Utilizando o comando nano criamos o ficheiro `wpa_supplicant.conf` e começamos diretamente a editá-lo. Neste ficheiro, precisamos de copiar a configuração do wifi, copiando o texto entre START e END, e modificando o SSID e a password do wifi a que nos queremos ligar.


```
$ nano /boot/wpa_supplicant.conf

------ START -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
ssid="MyNetworkSSID"
psk="password"
}
------ END -------
```


### 5. Ligação


Depois, inserimos o cartão SD no Raspberry Pi e ligamos o Pi à fonte de alimentação para iniciar o sistema operativo. Precisamos de o identificar na rede, e o protocolo mDNS irá provavelmente atribuir-lhe o nome raspberrypi.local. Vamos tentar ligar-nos via SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Se não funcionar, temos de descobrir a rede. Vamos descobrir o IP Address ao qual estamos ligados.


```
$ ifconfig
```


Por exemplo, se for 192.168.0.0, use o nmap para encontrar o Pi.


```
nmap -v 192.168.0.0/24
```


Assumindo que encontramos um novo IP na nossa rede, vamos entrar via SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Configurar o Pi


```
$ sudo raspi-config
```


- Selecione a opção (1) e altere a palavra-passe do utilizador pi.
- Seleccionamos a opção (8) para atualizar a ferramenta de configuração para a versão mais recente
- Seleccionamos a opção (4) para selecionar o nosso fuso horário
- Seleccionamos a opção (7) e, em seguida, Expandir sistema de ficheiros
- Acabamento


### 7. Agora actualize o SO


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Adicionar o utilizador Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Proteger a rpi


```
$ sudo apt install ufw
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'allow SSH from LAN'
$ sudo ufw allow 9735 comment 'allow Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```


### 10. Instalar o Go


Se não estiver a utilizar um raspberry pi, descarregue o go for your architecture [aqui](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Compilar e instalar o LND


```
$ git clone https://github.com/lightningnetwork/lnd.git
$ cd lnd
$ make
$ make install tags="autopilotrpc chainrpc experimental invoicesrpc routerrpc signrpc walletrpc watchtowerrpc wtclientrpc"
$ sudo cp $GOPATH/bin/lnd /usr/local/bin/
$ sudo cp $GOPATH/bin/lncli /usr/local/bin/
$ lncli --version
lncli version 0.11.0-beta commit=v0.11.0-beta-61-g6055b00dbbcedf45cd60f12e57dc5c1a7b97746f
```


### 12. Criar ficheiro conf LND


Criar o ficheiro de configuração do LND, o que deve ser feito com o utilizador "Bitcoin


```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```


```
[Application Options]
# enable spontaneous payments
accept-keysend=1

# Public name of the node
alias=YOUR_ALIAS
# Public color in hexadecimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# gRPC socket
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```


### 13. LND serviço de arranque automático


Para fazer o LND iniciar após o boot do rpi, devemos criar o arquivo .service no systemd. Se nós estivermos logados como um usuário Bitcoin e quisermos voltar para o usuário pi, nós simplesmente digitamos 'exit'


```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```


```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Service execution
###################

ExecStart=/usr/local/bin/lnd


# Process management
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Directory creation and permissions
####################################

# Run as bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Hardening measures
####################

# Provide a private /tmp and /var/tmp.
PrivateTmp=true

# Mount /usr, /boot/ and /etc read-only for the process.
ProtectSystem=full

# Disallow the process and all of its children to gain
# new privileges through execve().
NoNewPrivileges=true

# Use a new /dev namespace only populated with API pseudo devices
# such as /dev/null, /dev/zero and /dev/random.
PrivateDevices=true

# Deny the creation of writable and executable memory mappings.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```


```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```


Podemos ver os registos executando o comando journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Agora começamos o LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Adicionar fundos ao nó


```
$ lncli newaddress p2wkh
```

Pode agora enviar btc para o Address devolvido pelo LND.


com este comando, pode verificar o saldo:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Assim que a transação for confirmada, podemos abrir um canal. Se não souberes com que nó abrir o canal, podes ir a 1ml.com e escolher um nó.


Abrir uma ligação a um nó:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Depois abre um canal:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Verificar os nossos fundos:


```
$ lncli walletbalance
$ lncli channelbalance
```


Podemos ver os canais pendentes e activos:


```
$ lncli pendingchannels
$ lncli listchannels
```


Para pagar um relâmpago Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Para receber um pagamento, criar um Invoice para um determinado montante:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Para ver informações sobre o meu nó:


```
$ lncli getinfo
```


A lista completa de comandos pode ser vista simplesmente executando o comando lncli:


```
$ lncli
```


Por último, para efetuar chamadas à API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


FIM do guia!