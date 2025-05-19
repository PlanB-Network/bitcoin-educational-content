---
name: Neutrino
description: Instrukcja instalacji LND Neutrino
---

# Konfiguracja Raspberry Pi z LND


#### 1. Pobierz Raspberry Pi OS Lite

Instrukcje pobierania i instalowania obrazu na karcie micro SD w systemach Windows, Mac i Linux można znaleźć na [tej stronie](https://www.raspberrypi.org/software/operating-systems/).


#### 2. Formatowanie karty SD

użyj Raspberry Pi Imager lub balenaEtcher.


**Uwaga:** Symbol `$` jest używany jako znak zachęty i pozwala użytkownikowi na wprowadzanie komend do komputera, komendy te będą interpretowane przez bash w Linuksie. Symbol `#` na początku linii wskazuje, że poniższy tekst jest komentarzem.


#### 3. Włącz SSH


Przed uruchomieniem Raspberry Pi ze sformatowaną pamięcią, musimy włożyć ją do komputera i utworzyć dwa pliki, które pozwolą nam na zdalne połączenie. Za pomocą polecenia `touch` tworzymy pusty plik na partycji /boot, umożliwiając połączenie SSH przy pierwszym uruchomieniu świeżo sformatowanej karty SD.


```
# NOTE: If the microSD card has been mounted at /media/microSD, the command
# should be $ sudo touch /media/microSD/boot/ssh
$ touch /boot/ssh
```

#### 4. Utwórz plik dla połączenia Wi-Fi

Za pomocą polecenia nano tworzymy plik `wpa_supplicant.conf` i bezpośrednio rozpoczynamy jego edycję. W tym pliku musimy skopiować konfigurację wifi, kopiując tekst między START i END oraz modyfikując SSID i hasło wifi, z którym chcemy się połączyć.


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


#### 5. Połączenie

Następnie wkładamy kartę SD do Raspberry Pi i podłączamy Pi do źródła zasilania, aby uruchomić system operacyjny. Musimy zidentyfikować go w sieci, a protokół mDNS prawdopodobnie przypisze mu nazwę raspberrypi.local. Spróbujmy połączyć się przez SSH.

```
$ ssh pi@raspberrypi.local
password: raspberry
```

Jeśli to nie zadziała, musimy znaleźć sieć. Sprawdźmy IP Address, z którym jesteśmy połączeni.


```
$ ifconfig
```


Na przykład, jeśli jest to 192.168.0.0, użyj nmap, aby znaleźć Pi.


```
nmap -v 192.168.0.0/24
```


Zakładając, że znajdziemy nowy adres IP w naszej sieci, wejdźmy przez SSH.


```
$ ssh pi@192.168.0.30
password: raspberry
```


#### 6. Konfiguracja Pi

```
$ sudo raspi-config
```


- Wybierz opcję (1) i zmień hasło użytkownika pi.
- Wybieramy opcję (8), aby zaktualizować narzędzie konfiguracyjne do najnowszej wersji
- Wybieramy opcję (4), aby wybrać naszą strefę czasową
- Wybieramy opcję (7), a następnie Rozwiń system plików
- Zakończenie


#### 7. Teraz zaktualizuj system operacyjny

```
$ sudo apt update && sudo apt upgrade -y
$ sudo apt install htop git curl bash-completion jq qrencode dphys-swapfile vim --install-recommends -y
```


#### 8. Dodaj użytkownika Bitcoin

```
$ sudo adduser bitcoin
```


#### 9. Zabezpiecz rpi


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


#### 10. Zainstaluj Go

Jeśli nie używasz raspberry pi, pobierz go dla swojej architektury [tutaj](https://golang.org/dl/)


```
$ wget https://golang.org/dl/go1.15.linux-armv6l.tar.gz
$ sudo tar -C /usr/local -xzf go1.15.linux-armv6l.tar.gz
$ echo "export PATH=$PATH:/usr/local/go/bin" >> ~/.bashrc
$ echo "export GOPATH=$HOME/go" >> ~/.bashrc
$ echo "export PATH=$PATH:$GOPATH/bin" >> ~/.bashrc
$ source ~/.bashrc
$ go version # should display the following message 'go version go1.13.5 linux/arm'
```


#### 11. Kompilacja i instalacja LND


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


#### 12. Tworzenie pliku LND conf

Utwórz plik konfiguracyjny LND, należy to zrobić za pomocą użytkownika "Bitcoin"


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


#### 13. LND usługa autostartu

Aby LND uruchomił się po starcie rpi, musimy utworzyć plik .service w systemd. Jeśli jesteśmy zalogowani jako użytkownik Bitcoin i chcemy przełączyć się z powrotem na użytkownika pi, po prostu wpisujemy "exit


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


Możemy wyświetlić dzienniki, uruchamiając polecenie journalctl


```
$ sudo journalctl -f -u lnd
```


#### 14. Teraz zaczynamy LND


```
$ sudo su - bitcoin
$ lncli create
```


#### 15. Dodaj środki do węzła


```
$ lncli newaddress p2wkh
```

Możesz teraz wysłać btc do Address zwróconego przez LND.


za pomocą tego polecenia można sprawdzić saldo:


```
$ lncli walletbalance
{
"total_balance": "500000",
"confirmed_balance": "0",
"unconfirmed_balance": "500000"
}
```


Po potwierdzeniu transakcji możemy otworzyć kanał. Jeśli nie wiesz, w którym węźle otworzyć kanał, możesz przejść do 1ml.com i wybrać węzeł.


Otwarcie połączenia z węzłem:

```
$ lncli connect 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0@212.129.58.219:9735
```


Następnie otwórz kanał:

```
$ lncli openchannel 031015a7839468a3c266d662d5bb21ea4cea24226936e2864a7ca4f2c3939836e0 1000000 0
```


Sprawdź nasze fundusze:

```
$ lncli walletbalance
$ lncli channelbalance
```


Możemy przeglądać oczekujące i aktywne kanały:

```
$ lncli pendingchannels
$ lncli listchannels
```


Aby zapłacić błyskawicę Invoice:

```
$ lncli payinvoice lnbc1p0kkhgwpp5sn9y6xe9hx7swrjj4057674vh73nwk6rxg8j8zedztkn3vdzgjafacqmud86h
```


Aby otrzymać płatność, utwórz Invoice na określoną kwotę:

```
$ lncli addinvoice --memo 'my first payment on LN' --amt 100
```


Aby wyświetlić informacje o moim węźle:

```
$ lncli getinfo
```


Pełną listę poleceń można zobaczyć po prostu uruchamiając polecenie lncli:

```
$ lncli
```


Wreszcie, aby wykonywać połączenia z interfejsem API LND:

```
$ MACAROON_HEADER="Grpc-Metadata-macaroon: $(xxd -ps -u -c 1000 .lnd/data/chain/bitcoin/mainnet/admin.macaroon)"
$ curl -X GET --cacert .lnd/tls.cert --header "$MACAROON_HEADER" https://localhost:8080/v1/getinfo |jq
```


KONIEC przewodnika!