---
name: Koordynator Coinjoin - WabiSabi
description: Jak skonfigurować i uruchomić koordynatora coinjoin zgodnie z protokołem WabiSabi (używanym w Wasabi Wallet 2.0)
---

![cover](assets/cover.webp)


---

## Wprowadzenie 👋


W tym przewodniku eksperckim pomożemy ci skonfigurować koordynatora coinjoin, czyli serwer, który łączy ludzi, którzy chcą zaoszczędzić na opłatach transakcyjnych lub zwiększyć swoją prywatność onchain w transakcjach opartych na współpracy. Ponieważ nie ma już koordynatora prowadzonego przez firmę w pakiecie z Wasabi Wallet, użytkownicy muszą znaleźć i wybrać własny preferowany serwer koordynatora. Pojawiło się tylko kilku koordynatorów żądających 0% opłaty za koordynację, więc twórcy Wasabi Wallet ciężko pracowali, aby maksymalnie ułatwić uruchomienie własnego koordynatora społeczności (na sprzęcie tak małym jak Raspberry Pi5!). Obecnie aktywnych koordynatorów, którzy żądają 0% opłaty koordynacyjnej, można znaleźć na [LiquiSabi](https://liquisabi.com) i, co ważniejsze, na [nostr](https://github.com/Kukks/WasabiNostr).


## Wymagania 🫴



- VPS (węzeł hostowany) lub komputer/serwer (węzeł hostowany samodzielnie)
- Przycięty/pełny węzeł Bitcoin Core (testowany z wersją 29.0)


Opcjonalnie:


- (pod)Domena przekazująca ruch do węzła (np. coinjoin.[yourdomain].io)


Zaleca się posiadanie pewnego doświadczenia z wierszami poleceń i bash, ponieważ nie wszystkie kroki można zautomatyzować.


Pod względem sprzętowym zaleca się posiadanie systemu z:


- 4 rdzenie
- 16 GB RAM
- 2 TB SSD lub NVMe (dla pełnego węzła) / 128 GB SSD (dla węzła pruned)


Takie wymagania może spełnić Raspberry Pi 5 za jedyne 120 USD, nie licząc pamięci masowej, która kosztuje około 100 USD za 2 TB pamięci NVMe.


Tanie serwery VPS są zazwyczaj wyposażone w tylko 1 rdzeń i 4 GB pamięci RAM, co według mnie jest zbyt mało, aby zsynchronizować i zweryfikować cały bitcoin blockchain przy blockheight 911817.


Pod względem pamięci masowej pełny węzeł będzie wymagał co najmniej 2 TB pamięci dyskowej, najlepiej SSD lub NVMe. Podczas przycinania blockchain dopuszczalny jest znacznie mniejszy dysk (np. 128 GB SSD).


Jeśli zamierzasz uruchomić koordynator dla dużych (ponad 300 wejściowych) coinjoinów, zaleca się wybranie systemu z szybszymi/nowszymi rdzeniami o wyższej wydajności dla wszystkich weryfikacji podpisów.


## Instalacja 🛠️


Na węźle chcemy pobrać i zainstalować najnowszą wydaną wersję Wasabi Wallet, która zawiera backend i koordynator jako samodzielne pliki wykonywalne obok wallet.


Znajdź najnowszą wersję: [Wasabi Wallet](https://github.com/WalletWasabi/WalletWasabi/releases) i zweryfikuj podpis PGP wydania za pomocą kluczy: [PGP.txt](https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt)


Szczegóły wdrożenia różnią się w zależności od sprzętu (architektury procesora) i wyboru systemu operacyjnego, poniżej podano różne szczegóły dla Raspberry Pi (ARM-64) z Debian opartym na RaspiBlitz jako punkcie wyjścia. Przejdź do wdrożenia systemu operacyjnego Ubuntu (X86-64) przy użyciu Nix.


Instrukcje instalacji można znaleźć tutaj: [Wasabi Docs](https://docs.wasabiwallet.io/using-wasabi/InstallPackage.html)


### Wdrożenie RaspiBlitz/Debian


W przypadku węzłów RaspiBlitz (testowanych z wersją v1.11) można użyć wdrożenia script budowanego z kodu źródłowego: [home.admin/config.scripts/bonus.wasabi.sh](https://github.com/kravens/raspiblitz/blob/dev/home.admin/config.scripts/bonus.wasabi.sh)



### Łatwe wdrażanie


W przypadku minimalnego wdrożenia wystarczy wyodrębnić pliki wykonywalne dla danej platformy w folderze.

Przykładowe kody wiersza poleceń dla Debian/Ubuntu:


```
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb
wget https://github.com/WalletWasabi/WalletWasabi/releases/download/v2.7.2/Wasabi-2.7.2.deb.asc
wget https://raw.githubusercontent.com/WalletWasabi/WalletWasabi/refs/heads/master/PGP.txt
gpg --import PGP.txt
gpg --verify Wasabi-2.7.2.deb.asc Wasabi-2.7.2.deb
```


Powinno to skutkować następującą prawidłową wiadomością podpisu:


```
gpg: Signature made Mon Nov 17 01:33:09 2025 CET
gpg:                using RSA key 6FB3872B5D42292F59920797856348328949861E
gpg: Good signature from "zkSNACKs <zksnacks@gmail.com>" [unknown]
gpg: WARNING: This key is not certified with a trusted signature!
gpg:          There is no indication that the signature belongs to the owner.
Primary key fingerprint: 6FB3 872B 5D42 292F 5992  0797 8563 4832 8949 861E
```


Następnie można przystąpić do instalacji pobranego pakietu:


```
sudo apt install ./Wasabi-2.7.2.deb
```



## Konfiguracja 🧾


Przed uruchomieniem koordynatora należy edytować plik Config.json za pomocą swojego pliku:


- Poświadczenia Bitcoin RPC
- Preferowane parametry rundy
- Rozszerzony klucz publiczny koordynatora (utwórz nowy SegWit wallet do odbierania zebranego pyłu)

**Ostrzeżenie**: Taproot wallet spowoduje niewydanie UTXO! Użyj tutaj natywnego Segwit wallet.


- Dozwolone typy adresów wejściowych i wyjściowych
- Konfiguracja komunikatora do publikowania przez nostr (nazwa, opis, Uri, minimalne wejścia, przekaźnik nostr, klucz prywatny nostr)


Możesz uruchomić koordynatora dostępnego tylko za pośrednictwem adresu .onion lub użyć własnej domeny clearnet.


Znajdź lub utwórz plik konfiguracyjny w tej ścieżce:


`~/.walletwasabi/coordinator/Config.json`


Edytuj za pomocą polecenia:


```
sudo nano ~/.walletwasabi/coordinator/Config.json
```


Zobacz ten przykład Config.json:


```
{
"Network": "Main",
"MainNetBitcoinRpcUri": "http://localhost:8332",
"TestNetBitcoinRpcUri": "http://localhost:48332",
"RegTestBitcoinRpcUri": "http://localhost:18443",
"BitcoinRpcConnectionString": "your_bitcoin_rpcuser:your_bitcoin_rpcpassword",
"ConfirmationTarget": 21,
"DoSSeverity": "0.02",
"DoSMinTimeForFailedToVerify": "1d 21h 0m 0s",
"DoSMinTimeForCheating": "1d 0h 0m 0s",
"DoSPenaltyFactorForDisruptingConfirmation": 0.2,
"DoSPenaltyFactorForDisruptingSignalReadyToSign": 1.0,
"DoSPenaltyFactorForDisruptingSigning": 1.0,
"DoSPenaltyFactorForDisruptingByDoubleSpending": 3.0,
"DoSMinTimeInPrison": "0d 0h 20m 0s",
"MinRegistrableAmount": "0.000021",
"MaxRegistrableAmount": "1000.00",
"AllowNotedInputRegistration": true,
"StandardInputRegistrationTimeout": "0d 0h 21m 0s",
"BlameInputRegistrationTimeout": "0d 0h 3m 0s",
"ConnectionConfirmationTimeout": "0d 0h 1m 0s",
"OutputRegistrationTimeout": "0d 0h 1m 0s",
"TransactionSigningTimeout": "0d 0h 1m 0s",
"FailFastOutputRegistrationTimeout": "0d 0h 3m 0s",
"FailFastTransactionSigningTimeout": "0d 0h 1m 0s",
"RoundExpiryTimeout": "0d 0h 5m 0s",
"MaxInputCountByRound": 100,
"MinInputCountByRoundMultiplier": 0.21,
"MinInputCountByBlameRoundMultiplier": 0.21,
"RoundDestroyerThreshold": 375,
"CoordinatorExtPubKey": "xpub_fill_in_your_new_wallet_here",
"CoordinatorExtPubKeyCurrentDepth": 0,
"MaxSuggestedAmountBase": "100.00",
"RoundParallelization": 1,
"CoordinatorIdentifier": "CoinJoinCoordinatorIdentifier",
"AllowP2wpkhInputs": true,
"AllowP2trInputs": true,
"AllowP2wpkhOutputs": true,
"AllowP2trOutputs": true,
"AllowP2pkhOutputs": true,
"AllowP2shOutputs": true,
"AllowP2wshOutputs": true,
"DelayTransactionSigning": false,
"AnnouncerConfig": {
"CoordinatorName": "Your Coordinator Name",
"IsEnabled": true,
"CoordinatorDescription": "Privacy is a human right!",
"CoordinatorUri": "https://coinjoin.yourdomain/",
"AbsoluteMinInputCount": 21,
"ReadMoreUri": "https://coinjoin.yourdomain/",
"RelayUris": [
"wss://relay.primal.net"
],
"Key": "nsec_your_coordinator_nostr_privatekey"
},
"PublishAsOnionService": true,
"OnionServicePrivateKey": your_onion_service_private_key
}
```

### Konfiguracja toru 🧅


Aby wypełnić klucz OnionServicePrivateKey, należy go najpierw wygenerować.


Wasabi Wallet wygeneruje dla ciebie klucz prywatny, jeśli uruchomisz go za pierwszym razem z ``"PublishAsOnionService": true,``` ustawionym w pliku Config.json.


Uruchom koordynator raz za pomocą polecenia:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Aby zobaczyć adres ukrytej usługi Onion, sprawdź dzienniki koordynatora za pomocą:


```
cat ~/.walletwasabi/coordinator/Logs.txt | grep .onion
```


i znajdziesz coś takiego:


```
2026-01-09 21:21:21.210 [14] INFO       TorProcessManagerService.StartAsync (50)        Coordinator server listening on http://acoo3vgmo4rawaeujh6wckurymm2fp4ojauoag6zwov3pryyopis47qd.onion
```


Długi adres URL kończący się na .onion to ukryty adres usługi lub CoordinatorUri.


Lub sprawdź ponownie plik konfiguracyjny koordynatora za pomocą:


```
cat ~/.walletwasabi/coordinator/Config.json | grep CoordinatorUri
```


Który powinien być teraz automatycznie wypełniony.


## Bieganie ⚡


Po ustawieniu wszystkich parametrów konfiguracyjnych można uruchomić usługę koordynatora i rozpocząć ogłaszanie pierwszej rundy 🕶️


Wystarczy uruchomić koordynator za pomocą polecenia:


```
ASPNETCORE_URLS="http://localhost:5001" wcoordinator
```


Możesz monitorować bieżącą rundę i liczbę zarejestrowanych UTXO/coinów, sprawdzając (w przeglądarce Tor dla .onion):


```
http://coinjoin.yourdomain/wabisabi/human-monitor/
```


![detected](assets/en/01.webp)


### Opcjonalnie: debugowanie serwera koordynatora


Możesz monitorować wszelkie problemy lub błędy w pliku dziennika pod adresem ``~/.walletwasabi/backend/Logs.txt```


Typowe problemy obejmują problemy z połączeniem RPC, należy to włączyć w ``~/.bitcoin/bitcoin.conf`` za pomocą:


```
[main] # or [test] for testnet
rpcbind=127.0.0.1
rpcuser=your_bitcoin_rpcuser
rpcpassword=your_bitcoin_rpcpassword
```


### Opcjonalnie: Uruchomienie serwera zaplecza


Wraz z koordynatorem można również zapewnić serwer zaplecza dla użytkowników, którzy nie mają własnego węzła Bitcoin, z którym mogą się połączyć w celu oszacowania opłat i filtrów bloków.


Uruchom tę usługę za pomocą polecenia:


```
wbackend
```


## Zapraszanie użytkowników Wasabi do swojego koordynatora 🫂


Aby inni użytkownicy mogli znaleźć twoją usługę, możesz polegać na spikerze nostr lub udostępnić magiczny link z twoją domeną (clearnet) lub ukrytą usługą (link .onion) i okrągłymi parametrami, takimi jak ten:


```
name=Your%20Coordinator%20Name&network=main&coordinatorUri=https://coinjoin.yourdomain&coordinationFeeRate=0&readMore=https://coinjoin.yourdomain/&absoluteMinInputCount=21
```


Gdy użytkownik skopiuje magiczny link i otworzy Wasabi Wallet, oprogramowanie automatycznie wyświetli okno dialogowe koordynatora z domeną i parametrami.


![detected](assets/en/02.webp)


💚🍣 Gratulujemy decentralizacji prywatności bitcoinów 🕶️


Pamiętaj o treningu [wasabika](https://docs.wasabiwallet.io/FAQ/FAQ-Contribution.html#you-can-become-a-wasabika), Wasabi Wallet służy tylko do obrony 🛡️