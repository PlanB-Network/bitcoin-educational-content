---
name: Neutrino
description: Instalační příručka pro LND Neutrino
---

# Konfigurace Raspberry Pi s LND

1. Stáhněte si Raspberry Pi OS Lite

Stáhněte si Raspberry Pi OS Lite, návod na stahování a instalaci obrazu na micro SD kartu pro Windows, Mac a Linux najdete na [této stránce](https://www.raspberrypi.org/software/operating-systems/).

2. Formátujte SD kartu

Formátujte SD kartu pomocí Raspberry Pi Imager nebo balenaEtcher.

> POZNÁMKA: Symbol `$` se používá jako výzva a umožňuje uživateli zadávat příkazy do počítače, které budou interpretovány bashem v Linuxu. Symbol `#` na začátku řádku označuje, že následující text je komentář.

3. Povolte SSH

Před spuštěním Raspberry Pi s naformátovanou pamětí musíme vložit kartu do počítače a vytvořit dva soubory, které nám umožní vzdálené připojení. Pomocí příkazu `touch` vytvoříme prázdný soubor v oddílu /boot, čímž povolíme připojení přes SSH při prvním spuštění čerstvě naformátované SD karty.

```
# POZNÁMKA: Pokud byla microSD karta připojena na /media/microSD, příkaz
# by měl být $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

4. Použitím příkazu nano

vytvoříme soubor wpa_supplicant.conf a přímo ho začneme editovat. Do tohoto souboru potřebujeme zkopírovat konfiguraci wifi, kopírovat text mezi START a END a upravit SSID a heslo wifi, ke kterému se chcete připojit.

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

5. Připojení

Poté vložíme SD kartu do Raspberry Pi a připojíme Pi k zdroji napájení, aby se spustil operační systém. Potřebujeme ho identifikovat v síti, a protokol mDNS pravděpodobně přiřadí jméno raspberrypi.local. Zkusme se připojit přes SSH.

```
$ ssh pi@raspberrypi.local
heslo: raspberry
```

Pokud to nefunguje, potřebujeme zjistit síť. Zjistíme IP adresu, ke které jsme připojeni.

```
$ ifconfig
```

Například, pokud je to 192.168.0.0, použijeme nmap k nalezení Pi.

```
nmap -v 192.168.0.0/24
```

Předpokládáme, že najdeme novou IP v naší síti, připojíme se přes SSH.

```
$ ssh pi@192.168.0.30
heslo: raspberry
```

1. Konfigurujte Pi

```
$ sudo raspi-config
```

- Vyberte možnost (1) a změňte heslo pro uživatele pi.
- Vyberte možnost (8) pro aktualizaci nástroje konfigurace na nejnovější verzi
- Vyberte možnost (4) pro výběr časové zóny
- Vyberte možnost (7) a poté Rozšířit souborový systém
- Dokončete

  7.- Aktualizujeme OS

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```

8.- Přidáme uživatele bitcoin

```
$ sudo adduser bitcoin
```

9.- Zabezpečíme rpi

```
$ sudo apt install ufw
```
$ sudo ufw default deny incoming
$ sudo ufw default allow outgoing
$ sudo ufw allow 22 comment 'povolit SSH z LAN'
$ sudo ufw allow 9735 comment 'povolit Lightning'
$ sudo ufw allow 10009 comment 'Lightning gRPC'
$ sudo ufw enable
$ sudo systemctl enable ufw
$ sudo ufw status
$ sudo apt install fail2ban
```

```
10.- Instalujeme go: pokud nepoužíváte raspberry pi, stáhněte si go pro vaši architekturu zde (https://golang.org/dl/)

```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # mělo by zobrazit následující zprávu 'go version go1.13.5 linux/arm'
```

11.- Kompilujeme a instalujeme lnd

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

12.- Vytvoříme konfigurační soubor lnd, toto by mělo být provedeno s uživatelem 'bitcoin'

```
$ sudo su - bitcoin
$ mkdir .lnd
$ nano .lnd/lnd.conf
```

```
[Application Options]
# povolit spontánní platby
accept-keysend=1

# Veřejný název uzlu
alias=VÁŠ_ALIAS
# Veřejná barva v hexadecimálním formátu
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

13.- Aby se LND spustilo po startu rpi, musíme vytvořit .service soubor v systemd.
Pokud jsme přihlášeni jako uživatel bitcoin a chceme se přepnout zpět na uživatele pi, jednoduše napíšeme 'exit'

```
$ exit
$ sudo nano /etc/systemd/system/lnd.service
```

```
[Unit]
Description=LND Lightning Network Daemon
After=network.target

[Service]

# Spuštění služby
###################

ExecStart=/usr/local/bin/lnd


# Správa procesu
####################

Type=simple
Restart=always
RestartSec=30
TimeoutSec=240
LimitNOFILE=128000

# Vytvoření adresáře a nastavení oprávnění
####################################

# Spustit jako bitcoin:bitcoin
User=bitcoin
Group=bitcoin

# /run/lightningd
RuntimeDirectory=lightningd
RuntimeDirectoryMode=0710

# Opatření pro zvýšení bezpečnosti
####################

# Poskytnout soukromý /tmp a /var/tmp.
```
```
PrivateTmp=true
# Připojí /usr, /boot/ a /etc pouze pro čtení pro proces.
ProtectSystem=full

# Zabrání procesu a všem jeho potomkům získat
# nová oprávnění prostřednictvím execve().
NoNewPrivileges=true

# Použije nový /dev namespace, který obsahuje pouze API pseudo zařízení
# jako jsou /dev/null, /dev/zero a /dev/random.
PrivateDevices=true

# Zakáže vytváření zapisovatelných a spustitelných paměťových mapování.
MemoryDenyWriteExecute=true

[Install]
WantedBy=multi-user.target
```

```
$ sudo systemctl enable lnd
$ sudo systemctl start lnd
$ systemctl status lnd
```

Logy můžeme zobrazit spuštěním příkazu journalctl

```
$ sudo journalctl -f -u lnd
```

14. Nyní spustíme lnd

```
$ sudo su - bitcoin
$ lncli create
```

15. Přidáme prostředky na náš uzel

```
$ lncli newaddress p2wkh
```

Pošlete btc na adresu vrácenou lnd

Pro kontrolu zůstatku

```
$ lncli walletbalance
{
    "total_balance": "500000",
    "confirmed_balance": "0",
    "unconfirmed_balance": "500000"
}
```

Jakmile bude transakce potvrzena, můžeme otevřít kanál. Pokud nevíte, s kterým uzlem otevřít kanál, můžete jít na 1ml.com a vybrat uzel.

Otevřete spojení s uzlem:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```

Poté otevřete kanál

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```

Zkontrolujeme naše prostředky

```
$ lncli walletbalance
$ lncli channelbalance
```

Můžeme zobrazit čekající a aktivní kanály

```
$ lncli pendingchannels
$ lncli listchannels
```

Pro zaplacení lightning faktury

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```

Pro přijetí platby vytvořte fakturu na konkrétní částku

```
$ lncli addinvoice --memo 'moje první platba na LN' --amt 100
```

Pro zobrazení informací o mém uzlu

```
$ lncli getinfo
```

Kompletní seznam příkazů lze zobrazit jednoduše spuštěním lncli

```
$ lncli
```

Nakonec, pro volání lnd API

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```

> KONEC