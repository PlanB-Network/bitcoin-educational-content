---
name: Lightning Network Daemon (Linux)
description: Instalacja i uruchomienie Lightning Network Daemon w systemie Linux
---

![cover-lightning-network-daemon](assets/cover.webp)



Lightning Network jest drugim Layer z Bitcoin, dzięki czemu może przybrać błyskawiczne rozmiary, w szczególności dzięki szybkości i niskim kosztom transakcji, które oferuje.



W tym samouczku zainstalujemy implementację Lightning Network Daemon na naszym komputerze z systemem Linux (dystrybucja Ubuntu 24.04).



## Co to jest Lightning Network Daemon?



Lightning Network Daemon jest kompletną implementacją Lightning Network w języku Go. Został stworzony przez Lightning Labs i pozwala uruchomić pełną instancję węzła Lightning na komputerze.


Innymi słowy, dzięki tej implementacji można :





- Interakcja z Lightning Network**: Możesz używać wierszy poleceń do tworzenia portfeli Lightning, zarządzania kanałami płatności i trasami oraz wielu innych czynności bezpośrednio z terminala urządzenia.
- Łączenie zdalnego węzła Bitcoin lub własnej instancji Bitcoin Core**: LND pozwala połączyć instancję Bitcoin i używać jej jako backendu. Aby korzystać z tej implementacji, nie trzeba uruchamiać instancji Bitcoin Core na swoim komputerze.




https://planb.network/fr/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

## Dlaczego warto mieć własny węzeł Lightning?


Lightning to nakładka Bitcoin, która optymalizuje proces transferu i zmniejsza koszty transakcji.



Obracając swój węzeł Lightning, zyskujesz suwerenność i autonomię. Masz kontrolę nad swoimi środkami, więc pamiętaj:



"Nie klucze, nie bitcoiny"



W tym sensie uruchomienie węzła Lightning zwiększa bezpieczeństwo i integralność danych w następujący sposób:





- Pełna kontrola**: Zarządzaj własnymi kanałami płatności, stań się swoim własnym bankiem i bądź panem swoich aktywów.
- Poufność**: Dokonuj transakcji bez polegania na osobach trzecich w celu ochrony swojej prywatności.
- Nauka i autonomia**: Dzięki poleceniom `lncli` można lepiej zrozumieć procesy leżące u podstaw Lightning, stosując je samodzielnie z poziomu terminala.
- Decentralizacja**: Odgrywanie aktywnej roli we wzmacnianiu i decentralizacji Bitcoin / Lightning Network.



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c


Istnieją dwie opcje uruchomienia instancji implementacji LND na naszej maszynie. Możemy albo skonfigurować środowisko na własnej maszynie, aby działało lokalnie, albo zainstalować LND z kontenera Docker. Tutaj skoncentrujemy się na pierwszej opcji i zobaczymy, jak postępować z Dockerem w późniejszym samouczku.


## Instalacja LND z kodu źródłowego



### Wymagania wstępne


Ponieważ LND jest napisany w języku Go, musisz upewnić się, że masz środowisko GoLang i niezbędne zależności na swoim komputerze z systemem Linux.





- Wymagania sprzętowe:**


Aby zapewnić płynne i bezproblemowe działanie, komputer musi mieć odpowiednią wydajność do uruchomienia węzła LND Lightning.



Potrzebne będą :


1. **8 GB pamięci RAM** dla optymalnej płynności,


2. ** Wielordzeniowy procesor (co najmniej czterordzeniowy)** do wydajnego zarządzania działaniami węzła,


3. **Co najmniej 5 GB miejsca na dysku** dla trybu przyciętego węzła i 1 TB do uruchomienia Bitcoin Core (opcjonalnie, jeśli używany jest węzeł zdalny)





- Zainstaluj przydatne zależności:**


Poniższe polecenie pozwoli ci zainstalować na twoim komputerze narzędzia potrzebne do uruchomienia LND. Między innymi będziesz musiał zainstalować `Git`, narzędzie do wersjonowania, oraz `make`, które może wykonać i zbudować implementację LND z kodu źródłowego.



```bash
sudo apt install -y build-essential git make
```



![installation-dependances](assets/fr/01.webp)





- Zainstaluj GoLang na komputerze z systemem Linux**



Na dzień publikacji tego poradnika LND wymaga do instalacji Go*** w wersji 1.23.6.



Jeśli masz już zainstalowaną poprzednią wersję, usuń ją na potrzeby nowej instalacji Go.


```bash
# Suppression d'une ancienne version de Go
sudo rm -rf /usr/local/go

# Installation de la version 1.23.6 de Go
wget https://golang.org/dl/go1.23.6.linux-amd64.tar.gz

# Decompression du package

sudo tar -C /usr/local -xzf go1.23.6.linux-amd64.tar.gz

```



![go-install](assets/fr/02.webp)





- Konfiguracja środowiska Go**


W pliku `~/.bashrc` zainicjuj następujące zmienne środowiskowe, aby dodać Go do systemu Linux.



```bash
# Configuration de l'environnement Go
export GOROOT=/usr/local/go
export GOPATH=~/gocode
export PATH=$PATH:$GOROOT/bin

# Appliquer les modifications

source ~/.bashrc
```





- Sprawdzanie instalacji** (w języku francuskim)


```bash
go version
```



![go-version](assets/fr/03.webp)


### Klonowanie repozytorium LND GitHub



Użyj git, aby uzyskać kopię kodu źródłowego LND lokalnie na swoim komputerze


```bash
git clone https://github.com/lightningnetwork/lnd.git
```


![clone-lnd](assets/fr/04.webp)


### Budowa i instalacja



Zainstalowane wcześniej narzędzie `make` pozwoli ci zbudować plik wykonywalny z kodu źródłowego LND i kontynuować instalację.



```bash
# Acceder au repertoire clonné
cd lnd

# construire LND
make
```



Zainstaluj LND na swoim komputerze



```bash
# installer LND
make install
```



![make-lnd](assets/fr/06.webp)




- Sprawdzanie instalacji** (w języku francuskim)



Aby upewnić się, że wszystko poszło gładko, uruchomienie tego polecenia powinno dać ci wersję LND, którą aktualnie używasz.



```bash
# Version de LND
lnd --version

# Version  de LNCLI
lncli --version
```


![lnd-version](assets/fr/05.webp)




- Konserwacja i aktualizacje



```bash
cd lnd
git pull
make clean && make && make install
```


⚠️ **WAŻNE**: Aktualizacje LND mogą wymagać nowszych wersji Go, więc upewnij się, że zaktualizowałeś swój system, aby uniknąć problemów z zależnościami podczas instalacji.


### Konfiguracja Lightning Network Daemon



Konfiguracja węzła Lightning LND jest podobna do konfiguracji Bitcoin i jest przeprowadzana w pliku konfiguracyjnym zawierającym wszystkie parametry węzła. Aby to zrobić, w katalogu głównym komputera można utworzyć ukryty folder `.LND`, a następnie utworzyć plik konfiguracyjny `LND.conf` w tym folderze.



```bash
# Création du ficher
mkdir -p ~/.lnd

cd ~/.lnd

# Fichier de configuration
touch lnd.conf
```





W pliku konfiguracyjnym można skonfigurować węzeł LND.



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



## Zrozumienie konfiguracji



Ważne jest, aby zrozumieć minimalną konfigurację potrzebną do prawidłowej i kompletnej instalacji węzła LND.



W oparciu o zawartość pliku `~/.LND/LND.conf`, poniżej znajdują się szczegóły pól:





- noseedbackup**: Pozwala wybrać, czy LND ma wykonywać automatyczne kopie zapasowe portfeli.  Ustawienie tej właściwości na `0` pozwala na ręczne zapisywanie informacji o przywracaniu w osobiście wybranej bezpiecznej lokalizacji.





- debuglevel**: Umożliwia określenie poziomu szczegółowości błędów i dzienników w przypadku wystąpienia błędów podczas działania.





- Bitcoin.active**: Nakazuje LND działanie jako węzeł Bitcoin i interakcję z siecią Bitcoin.





- Bitcoin.Mainnet**: Określa LND do połączenia z główną siecią Bitcoin (Mainnet), można ustawić wartości `bitcoind.signet` i `bitcoind.regtest` odpowiednio dla sieci Bitcoin Signet i Bitcoin Regtest





- Bitcoin.node**: Określa typ węzła Bitcoin, z którym powinien połączyć się LND.





- Bitcoin.rpcuser** i **Bitcoin.rpcpassword** : Reprezentują.


odpowiednio loginy (użytkownik, hasło), aby połączyć się z węzłem Bitcoin





- bitcoind.zmqpubrawblock** i **bitcoind.zmqpubrawtx**: odpowiednio definiują punkty końcowe ZeroMQ do otrzymywania powiadomień o nowych blokach i transakcjach w sieci Bitcoin.




## Sprawdzanie instalacji za pomocą LND



Prawdopodobnie będziesz chciał upewnić się, że proces zakończył się powodzeniem i że synchronizujesz się z Lightning Network, aby informacje o węźle były aktualne.



Aby uruchomić implementację LND i uzyskać informacje o węźle, wystarczy wpisać polecenie :


```bash
lnd getinfo
```


![lnd-getinfo](assets/fr/07.webp)


## Wykonywanie działań na LND



Po zakończeniu i sprawdzeniu instalacji można rozpocząć korzystanie z aplikacji.


Oto najważniejsze polecenia, które pomogą Ci zacząć.



### Tworzenie portfolio


Portfel Lightning jest pierwszym krokiem w każdym działaniu mającym na celu zarządzanie funduszami.



⚠️ **WAŻNE**: Należy uważnie zanotować 24-wyrazową frazę **seed**. Będzie ona potrzebna do odzyskania środków w przypadku problemów.



Zapisz również hasło Wallet, aby móc go odblokować za pomocą polecenia `lncli unlock` po ponownym uruchomieniu węzła LND.



```bash
lncli create
```


![créer-portefeuille](assets/fr/08.webp)


### Sprawdź saldo



Sprawdzaj swoje konta bezpośrednio z terminala:



```bash
lncli walletbalance
```


![solde](assets/fr/09.webp)


### Informacje o węźle



Użyj poniższego polecenia, aby dowiedzieć się, które kanały są aktywne w węźle.



```bash
lncli listchannels
```



Możesz także uzyskać listę węzłów, z którymi jesteś połączony.



```bash
lncli listpeers
```



### Zarządzanie kanałami



Kanał Lightning umożliwia **bezpośrednie połączenie para po parze z innym węzłem na Lightning Network**. W tym kanale można swobodnie korzystać z Exchange Satoshis do pojemności kanału.



### Połączenie z węzłem



Łączenie się z innymi węzłami Lightning jest podstawową czynnością, jeśli chcesz aktywnie uczestniczyć i korzystać z mocy Lightning.



Aby połączyć się z peerem (węzłem Lightning), potrzebne będą trzy informacje:




- Klucz publiczny węzła**: Jest to unikatowy identyfikator węzła w sieci Bitcoin;
- IP** : Adres IP komputera, na którym zainstalowany jest węzeł;
- PORT** :  Port otwarty na komputerze, który umożliwia komunikację z tym węzłem.



Węzły, z którymi można się połączyć, można znaleźć na [amboss](https://amboss.space/), platformie zawierającej informacje o węzłach Lightning.



```bash
# Se connecter à un noeud
lncli connect <ID_PUBKEY>@<IP>:<PORT>

# Un exemple  : Connexion au noeud de Wallet of Satoshi
lncli connect 035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226@170.75.163.209:9735
```




Upewnij się, że łączysz się z **niezawodnymi węzłami**, aby zachować integralność własnego systemu. Oto kilka zaleceń dotyczących wyboru odpowiednich połączeń.





- Dywersyfikacja geograficzna**: Łączenie się z węzłami w różnych regionach.





- Reputacja**: Wybierz węzły o dobrej dostępności.





- Pojemność**: Wybieraj węzły o dobrej płynności.





- Opłaty**: Opłaty za przekierowanie czeku.


### Otwórz kanał płatności


Aby otworzyć kanał płatności, upewnij się, że jesteś **połączony** z węzłem równorzędnym, a następnie zdefiniuj **pojemność** (ilość satoshi), którą chcesz zablokować w tym kanale.



```bash
lncli openchannel --node_key=<ID_PUBKEY> --local_amt=<AMOUNT_SATOSHIS>
```


### Utwórz piorun Invoice



Lightning Invoice reprezentuje ciąg znaków wyrażający chęć otrzymania satoshis w Lightning Wallet.


Tworzenie faktur Lightning z własnym węzłem pozwala chronić dane (geograficzne i osobiste) i daje 100% autonomii w zarządzaniu środkami.



```bash
# Générer une facture de 1000 sats

lncli addinvoice --amt=1000 --memo="Facture de 1000 sats"
```



### Płacenie za Lightning Invoice



```bash
lncli payinvoice <FACTURE>
```


### Zamykanie kanału



Istnieją dwa sposoby zamknięcia aktywnego kanału w bieżącym węźle.





- Zamknięcie współpracy**: Sygnalizuje to chęć węzła do wycofania się z kanału płatności, zapewniając, że trwające zadania zostaną zakończone, a dane zostaną zarchiwizowane, aby uniknąć utraty środków.


```
lncli closechannel <ID_CANAL>
```




- Wymuszone zamknięcie**: ⚠️ Należy unikać, jeśli to możliwe, działanie to przerywa trwające procesy w kanale płatności i zwiększa ryzyko utraty środków.


```
lncli closechannel --force <ID_CANAL>
```


## Najlepsze praktyki i bezpieczeństwo węzła LND.


Bezpieczeństwo jest najważniejsze podczas korzystania z węzła Bitcoin/ Lightning. Oto kilka punktów, które zwiększą bezpieczeństwo instalacji:





- Przechowuj `seed phrase` w bezpiecznym miejscu, poza siecią.





- Regularnie twórz kopie zapasowe pliku `~/.LND/channel.backup`: Ten plik zapisuje stany kanałów za każdym razem, gdy nowy kanał jest otwierany (lub stary kanał jest zamykany) na węźle.


⚠️ Umożliwia przywracanie kanałów i odzyskiwanie środków zablokowanych w kanałach płatności w przypadku utraty danych lub awarii węzła



Możesz przywrócić swoje środki za pomocą poniższego polecenia, określając ścieżkę kopii zapasowej tego pliku:


```
lncli restorechanbackup <CHEMIN_DU_FICHIER>
```




- Upewnij się, że zapisałeś słowa i hasło przywracania Lightning Wallet.
- Aktualizuj swój system na bieżąco.



## Bieżące rozwiązywanie problemów


### Częste problemy




- Błąd połączenia bitcoind** : Sprawdź dane logowania do RPC
- Synchronizacja zablokowana** : Sprawdź połączenie internetowe
- Błąd uprawnień**: Sprawdź uprawnienia folderu `~/.LND`




Dotarłeś do końca tego samouczka. Jeśli chcesz dowiedzieć się więcej o Lightning, oferujemy ten kurs wprowadzający, aby lepiej zrozumieć koncepcje i praktyki stojące za Lightning Network.




https://planb.network/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb