---
name: Neutrino
description: Guia de Instalação do LND Neutrino
---

# Configuração do Raspberry Pi com LND

1. Baixar o Raspberry Pi OS Lite

Baixe o Raspberry Pi OS Lite, as [instruções para download e instalação da imagem em um cartão micro SD](https://www.raspberrypi.org/software/operating-systems/) estão nesta página, para Windows, Mac e Linux.

2. Formatar o Cartão SD

Formate o cartão SD com o Raspberry Pi Imager ou com o balenaEtcher.

> NOTA: O símbolo `$` é usado como prompt e permite que o usuário insira comandos no computador, os comandos serão interpretados pelo bash no Linux. O símbolo `#` no início de uma linha indica que o texto a seguir é um comentário.

3. Habilitar o SSH

Antes de iniciar o Raspberry Pi com o cartão formatado, devemos inseri-lo em um computador e criar dois arquivos que nos permitirão conectar remotamente. Com o comando `touch`, criamos um arquivo vazio na partição /boot, habilitando assim a conexão SSH na primeira inicialização do cartão SD recém-formatado.

```
# NOTA: Se o microSD estiver montado em /media/microSD, o comando
# deve ser $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4.- Com o comando nano, criamos o arquivo wpa_supplicant.conf e começamos a editá-lo diretamente. Neste arquivo, devemos copiar a configuração do Wi-Fi, copie o texto entre INÍCIO e FIM e altere o SSID e a senha do Wi-Fi ao qual deseja se conectar.

```
$ nano /boot/wpa_supplicant.conf

------ INÍCIO -------
country=ar
update_config=1
ctrl_interface=/var/run/wpa_supplicant

network={
 ssid="MyNetworkSSID"
 psk="password"
}
------ FIM -------
```

5.- Em seguida, inserimos o cartão SD no Raspberry Pi e conectamos o RPi à fonte de alimentação para iniciar o sistema operacional. Precisaremos identificá-lo na rede, provavelmente o protocolo mDNS atribuirá a ele um nome na rede raspberrypi.local, vamos tentar nos conectar via SSH.

```
$ ssh pi@raspberrypi.local
senha: raspberry
```

Se não funcionar, precisamos descobrir o endereço de rede, vamos descobrir o endereço IP ao qual estamos conectados.

```
$ ifconfig
```

Se, por exemplo, for 192.168.0.0, faça um nmap para encontrar o RPi.

```
nmap -v 192.168.0.0/24
```

Supondo que encontramos um novo IP em nossa rede, 192.168.0.30

Conecte-se via SSH.

```
$ ssh pi@192.168.0.30
senha: raspberry
```

6.- Configuramos o RPi

```
$ sudo raspi-config
```

- Selecione a opção (1) e altere a senha do usuário pi.
- Selecionamos a opção (8) para atualizar a ferramenta de configuração para a versão mais recente
- Selecionamos a opção (4) para selecionar o nosso fuso horário
- Selecionamos a opção (7) e depois Expand filesystem
- Finish

  7.- Atualizamos o SO

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Adicionamos o usuário bitcoin

```
$ sudo adduser bitcoin
```

9.- Garantimos a segurança do rpi

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

10.- Instalamos o go: se não estiver usando um raspberry pi, baixe o go para sua arquitetura aqui (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # deve mostrar a seguinte mensagem 'go version go1.13.5 linux/arm'
```

11.- Compilamos e instalamos o lnd

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

12.- Criamos o arquivo de configuração do lnd, isso deve ser feito com o usuário 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# permite pagamentos espontâneos
accept-keysend=1

# Nome público do nó
alias=TU_ALIAS
# Cor pública em hexadecimal
color=#000000
debuglevel=info
maxpendingchannels=5
listen=localhost
# soquete gRPC
rpclisten=0.0.0.0:10009

[Bitcoin]
bitcoin.active=1
bitcoin.mainnet=1
bitcoin.node=neutrino

[neutrino]
neutrino.connect=bb2.breez.technology
```

13.- Para que o LND seja iniciado após a inicialização do rpi, devemos criar o arquivo .service no systemd.
'Se estamos como usuário bitcoin e queremos voltar a utilizar o usuário pi, basta digitar "exit"

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Execução do serviço
###################

ExecStart=/usr/local/bin/lnd


# Gerenciamento de processos
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Criação de diretórios e permissões
####################################

# Executar como bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Medidas de fortalecimento
####################

# Fornecer um /tmp e /var/tmp privados.
PrivateTmp=true

# Montar /usr, /boot/ e /etc como somente leitura para o processo.
ProtectSystem=full

# Impedir que o processo e todos os seus filhos obtenham
# novos privilégios através do execve().
NoNewPrivileges=true

# Usar um novo namespace /dev apenas populado com dispositivos pseudo API
# como /dev/null, /dev/zero e /dev/random.
PrivateDevices=true

# Negar a criação de mapeamentos de memória graváveis e executáveis.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Podemos ver os logs executando o comando journalctl

```
$ sudo journalctl -f -u lnd
```

14. Agora iniciamos o lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Adicionar fundos ao nosso nó

```
$ lncli newaddress p2wkh
```

Enviar btc para o endereço fornecido pelo lnd

Para verificar o saldo

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Após a confirmação da transação, podemos abrir um canal. Se você ainda não sabe com qual nó abrir o canal, você pode ir para 1ml.com e escolher um nó.

Abrir uma conexão com um nó:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Em seguida, abrir um canal

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Verificar nossos fundos

```
$ lncli walletbalance
$ lncli channelbalance
```

Podemos ver os canais pendentes e ativos

```
$ lncli pendingchannels
$ lncli listchannels
```

Para pagar uma fatura lightning

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Para receber um pagamento, crio uma fatura com um valor específico

````
$ lncli addinvoice --memo 'mi primer pagamento em LN' --amt 100```
````

Para ver informações sobre o meu nó

```
$ lncli getinfo
```

A lista completa de comandos pode ser vista apenas executando lncli

```
$ lncli
```

Finalmente, para fazer chamadas à API do lnd

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> FIM
