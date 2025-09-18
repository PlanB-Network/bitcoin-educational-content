---
name: Neutrino
description: Průvodce instalací LND Neutrino
---
![image](assets/cover.webp)


## Konfigurace Raspberry Pi s LND


### 1. Stáhnout Raspberry Pi OS Lite


Pokyny pro stažení a instalaci obrazu na kartu micro SD v systémech Windows, Mac a Linux naleznete na [této stránce](https://www.raspberrypi.org/software/operating-systems/).


### 2. Formátování karty SD


Použijte Raspberry Pi Imager nebo balenaEtcher.


**Poznámka:** Symbol `$` se používá jako výzva a umožňuje uživateli zadávat příkazy do počítače, které budou interpretovány bashem v Linuxu. Symbol `#` na začátku řádku označuje, že následující text je komentář.


### 3. Povolení SSH


Před spuštěním počítače Raspberry Pi s naformátovanou pamětí jej musíme vložit do počítače a vytvořit dva soubory, které nám umožní vzdálené připojení. Pomocí příkazu `touch` vytvoříme v oddílu /boot prázdný soubor, který umožní připojení SSH při prvním spuštění čerstvě naformátované karty SD.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```


### 4. Vytvoření souboru pro připojení Wi-Fi


Pomocí příkazu nano vytvoříme soubor `wpa_supplicant.conf` a začneme jej přímo upravovat. V tomto souboru musíme zkopírovat konfiguraci wifi, zkopírovat text mezi START a END a upravit SSID a heslo wifi, ke které se chceme připojit.


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


### 5. Připojení


Poté vložíme kartu SD do počítače Raspberry Pi, připojíme jej ke zdroji napájení a spustíme operační systém. Musíme jej identifikovat v síti a protokol mDNS mu pravděpodobně přiřadí název raspberrypi.local. Zkusíme se připojit přes SSH.


```
$ ssh pi@raspberrypi.local
password: raspberry
```


Pokud to nefunguje, musíme zjistit síť. Zjistíme IP adresu Address, ke které jsme připojeni.


```
$ ifconfig
```


Pokud je to například 192.168.0.0, použijte nmap k nalezení počítače Pi.


```
nmap -v 192.168.0.0/24
```


Za předpokladu, že jsme našli novou IP adresu v naší síti, vstoupíme do ní přes SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


### 6. Konfigurace počítače Pi


```
$ sudo raspi-config
```


- Vyberte možnost (1) a změňte heslo uživatele pi.
- Výběrem možnosti (8) aktualizujeme konfigurační nástroj na nejnovější verzi
- Výběrem možnosti (4) vybereme naše časové pásmo
- Vybereme možnost (7) a poté Rozbalit souborový systém
- Dokončení


### 7. Nyní aktualizujte operační systém


```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


### 8. Přidání uživatele Bitcoin


```
$ sudo adduser bitcoin
```


### 9. Zabezpečení rpi


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


### 10. Instalace aplikace Go


Pokud nepoužíváte raspberry pi, stáhněte si go pro svou architekturu [zde](https://golang.org/dl/).


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


### 11. Zkompilujte a nainstalujte LND


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


### 12. Vytvoření konfiguračního souboru LND


Vytvoření konfiguračního souboru LND, to by mělo být provedeno s uživatelem "Bitcoin"


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


### 13. Služba LND autostart


Aby se LND spustil po spuštění rpi, musíme v systemd vytvořit soubor .service. Pokud jsme přihlášeni jako uživatel Bitcoin a chceme se přepnout zpět na uživatele pi, jednoduše zadáme 'exit'


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


Protokoly můžeme zobrazit spuštěním příkazu journalctl


```
$ sudo journalctl -f -u lnd
```


### 14. Nyní začínáme LND


```
$ sudo su - bitcoin
$ lncli create
```


### 15. Přidání prostředků do uzlu


```
$ lncli newaddress p2wkh
```

Nyní můžete poslat btc na účet Address vrácený LND.


pomocí tohoto příkazu můžete zkontrolovat zůstatek:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Po potvrzení transakce můžeme otevřít kanál. Pokud nevíte, ve kterém uzlu kanál otevřít, můžete přejít na stránku 1ml.com a uzel si vybrat.


Otevření připojení k uzlu:


```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Pak otevřete kanál:


```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Podívejte se na naše fondy:


```
$ lncli walletbalance
$ lncli channelbalance
```


Můžeme zobrazit čekající a aktivní kanály:


```
$ lncli pendingchannels
$ lncli listchannels
```


Zaplatit blesk Invoice:


```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Chcete-li obdržet platbu, vytvořte účet Invoice na určitou částku:


```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Zobrazení informací o mém uzlu:


```
$ lncli getinfo
```


Úplný seznam příkazů lze zobrazit jednoduchým spuštěním příkazu lncli:


```
$ lncli
```


A konečně volání rozhraní API LND:


```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


KONEC průvodce!