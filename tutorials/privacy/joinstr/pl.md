---
name: Joinstr
description: Zdecentralizowane CoinJoins za pośrednictwem sieci Nostr dla suwerennej poufności Bitcoin
---

![cover](assets/cover.webp)



Przejrzystość łańcucha bloków Bitcoin umożliwia śledzenie historii transakcji. CoinJoins przerywa te powiązania poprzez mieszanie wielu jednoczesnych transakcji, przywracając poziom poufności porównywalny z gotówką.



Tradycyjne rozwiązania opierają się jednak na centralnym koordynatorze jako pojedynczym punkcie awarii. Wasabi i Samourai zaprzestały działalności w 2024 r. pod presją regulacyjną.



**Joinstr** eliminuje tę słabość, wykorzystując zdecentralizowaną sieć Nostr do koordynacji. Ta aplikacja typu open source umożliwia prawdziwie suwerenne CoinJoins, w których żaden organ centralny nie może cenzurować, monitorować ani przerywać usługi.



## Czym jest Joinstr?



Joinstr to narzędzie typu open source, które rewolucjonizuje podejście CoinJoins, wykorzystując protokół Nostr jako infrastrukturę koordynacyjną. W przeciwieństwie do scentralizowanych rozwiązań wymagających dedykowanego serwera, Joinstr opiera się na rozproszonej sieci przekaźników Nostr, aby umożliwić uczestnikom bezpośrednią koordynację między rówieśnikami.



**Architektura zdecentralizowana** : Sieć Nostr zastępuje centralnego koordynatora. Uczestnicy tworzą lub dołączają do "pul", publikując zaszyfrowane ogłoszenia za pośrednictwem przekaźników Nostr. Informacje te (kwoty, uczestnicy, adresy) pozostają niezrozumiałe dla przekaźników, zapewniając, że żaden centralny podmiot nie może monitorować, cenzurować ani filtrować CoinJoins.



**Mechanizm SIGHASH_ALL|ANYONECANPAY**: Joinstr wykorzystuje tę flagę podpisu Bitcoin, pozwalając każdemu uczestnikowi podpisać tylko swoje dane wejściowe, jednocześnie weryfikując wszystkie dane wyjściowe. Każdy użytkownik generuje swój PSBT lokalnie, a następnie dystrybuuje go za pośrednictwem Nostr. Każdy użytkownik generuje swój PSBT lokalnie, podpisuje go, a następnie dystrybuuje za pośrednictwem Nostr. Bitcoiny pozostają pod wyłączną kontrolą użytkownika aż do ostatecznego podpisania.



**Filozofia**: Joinstr podąża za cypherpunkowym etosem Bitcoin, dążąc do trzech celów: **odporność na cenzurę** (żadna władza nie może zatrzymać usługi), **całkowita bezcenzuralność** (zachowujesz swoje klucze prywatne) i **równe traktowanie** (żaden UTXO nie może być dyskryminowany).



### Główne cechy



**Elastyczne pule**: W przeciwieństwie do stałych nominałów, każdy użytkownik może utworzyć pulę z dokładną żądaną kwotą i docelową liczbą uczestników, optymalizując wykorzystanie UTXO bez sztucznego podziału.



** Przejrzyste opłaty**: Brak opłat koordynacyjnych. Jedynie opłaty transakcyjne Bitcoin są dzielone równo między uczestników (kilka tysięcy satoshi na osobę).



**Efemeryczność**: Żadne dane użytkownika nie są przechowywane. Informacje są przesyłane za pośrednictwem zaszyfrowanych efemerycznych wiadomości Nostr, natychmiast zapomnianych po transakcji.



### Dostępne platformy



Niniejszy poradnik skupia się na aplikacji **Android**, jedynym obecnie stabilnym i zalecanym rozwiązaniu. Wtyczka Electrum istnieje, ale ma problemy z kompatybilnością, które czynią ją niestabilną. Interfejs sieciowy jest w trakcie opracowywania.



## Konfiguracja rdzenia Bitcoin



Joinstr Android wymaga połączenia z węzłem Bitcoin poprzez RPC. Należy najpierw skonfigurować Bitcoin Core na komputerze, aby akceptował połączenia z telefonu.



**Uwaga**: Aby uzyskać więcej informacji na temat pełnej konfiguracji Bitcoin Core, zobacz nasze dedykowane samouczki :



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-core-mac-windows-9684ab02-e0af-41c9-8102-86ac7c7727f3


### Wymagania sieciowe



#### Zlokalizuj swój lokalny adres IP



Telefon z systemem Android musi mieć możliwość połączenia się z węzłem Bitcoin w sieci lokalnej. Znajdź adres IP komputera:



**Na macOS** :



```bash
ifconfig | grep "inet " | grep -v "127.0.0.1" | awk '{print $2}' | head -n 1
```



Prosta alternatywa:



```bash
ipconfig getifaddr en0
# or for WiFi: ipconfig getifaddr en1
```



**W systemie Linux** :



```bash
hostname -I | awk '{print $1}'
```



**W systemie Windows** :



```cmd
ipconfig
```



Znajdź adres IPv4 (format `192.168.x.x` lub `10.0.x.x`)



### Konfiguracja RPC



#### Edytuj bitcoin.conf



![LOCALISATION BITCOIN.CONF](assets/fr/01.webp)



Zlokalizuj plik `bitcoin.conf`:




- Linux**: `~/.bitcoin/bitcoin.conf
- macOS**: `~/Library/Application Support/Bitcoin/bitcoin.conf
- Windows**: `%APPDATA%\Bitcoin\bitcoin.conf`



![CONTENU BITCOIN.CONF](assets/fr/02.webp)



Otwórz plik za pomocą ulubionego edytora tekstu i dodaj tę konfigurację, aby aktywować serwer RPC.



**Zalecana konfiguracja na początek (zakładka)** :



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



*konfiguracja *mainnet** (do użytku produkcyjnego) :



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



**Ważne** :




- Signet jest wysoce zalecany** do pierwszych testów: aplikacja jest wciąż w fazie rozwoju (beta) i nadal mogą występować błędy. Signet pozwala testować bezpłatnie, bez ryzykowania prawdziwych funduszy
- Zastąp `192.168.1.0/24` swoją podsiecią (np. jeśli twój adres IP to `192.168.68.57`, użyj `192.168.68.0/24`)



**Bezpieczeństwo**: Generowanie silnego hasła :



```bash
openssl rand -base64 32
```



### Inicjalizacja



#### Uruchom ponownie i sprawdź



1. Całkowite wyłączenie Bitcoin Core


2. Uruchom go ponownie, aby zastosować konfigurację




![SYNCHRONISATION BITCOIN CORE](assets/fr/03.webp)



Gdy Bitcoin Core uruchomi się po raz pierwszy, pobierze i zsynchronizuje blockchain zakładki. Ta operacja jest znacznie szybsza niż na mainnet (tylko kilka minut). Przed kontynuowaniem należy poczekać na zakończenie synchronizacji.



![CRÉATION DE WALLET](assets/fr/04.webp)



Po synchronizacji utwórz nowy portfel, klikając "Utwórz nowy wallet". Nadaj mu wyraźną nazwę, taką jak `tuto_joinstr_signet`.



![WALLET CRÉÉ](assets/fr/05.webp)



Twój wallet jest teraz utworzony i gotowy do przyjmowania bitcoinów z zakładek do testowania.



#### Pobierz bitcoiny z zakładek (test)



Aby przetestować Joinstr w zakładce, potrzebujesz darmowych bitcoinów testowych:



![SIGNET FAUCET](assets/fr/06.webp)



Użyj publicznej zakładki, takiej jak :




- [signetfaucet.com](https://signetfaucet.com)
- [alt.signetfaucet.com](https://alt.signetfaucet.com)
- [bookmark257.bublina.eu.org](https://signet257.bublina.eu.org)



W Bitcoin Core, generate nowy adres odbioru (zakładka "Odbiór"), skopiuj go i wklej do formularza kranu. W razie potrzeby rozwiąż captcha. Otrzymasz darmowe bitcoiny w zakładkach w ciągu kilku sekund.



## Aplikacja na Androida



### Instalacja



![APPLICATION ANDROID](assets/fr/07.webp)



Przejdź na stronę [gitlab.com/invincible-privacy/joinstr-kmp/-/releases](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases), aby pobrać najnowszą wersję APK. W przeglądarce systemu Android pobierz plik, a następnie otwórz go, aby rozpocząć instalację. W razie potrzeby należy zezwolić na instalację z nieznanych źródeł w ustawieniach zabezpieczeń telefonu.



### Konfiguracja aplikacji



![PERMISSIONS VPN](assets/fr/08.webp)



Przy pierwszym uruchomieniu aplikacja Joinstr poprosi o uprawnienia do sterowania wbudowaną siecią VPN. Zaakceptuj oba żądania uprawnień: Kontrola OpenVPN i Połączenie VPN. Uprawnienia te są wymagane do integracji VPN, która chroni prywatność sieci.



![INTERFACE APPLICATION](assets/fr/09.webp)



Aplikacja Joinstr podzielona jest na trzy główne zakładki:




- Strona główna**: Ekran główny
- Pule**: Tworzenie pul CoinJoin i zarządzanie nimi
- Ustawienia**: Konfiguracja aplikacji



![CONFIGURATION SETTINGS](assets/fr/13.webp)



Skonfiguruj ustawienia w zakładce "Ustawienia":



**1. Przekaźnik Nostr**: Adres przekaźnika Nostr dla koordynacji puli




- Przykład: `wss://relay.damus.io`
- Inne zalecane przekaźniki: `wss://nos.lol`, `wss://relay.nostr.band`, `wss://nostr.fmt.wiz.biz`
- ⚠️ **Ważne**: Wszyscy uczestnicy muszą korzystać z **tego samego przekaźnika Nostr**, aby widzieć i dołączać do tych samych pul. Jeśli korzystasz z innego przekaźnika, nie zobaczysz pul utworzonych w innych przekaźnikach



**2. Adres URL węzła**: Adres IP węzła Bitcoin (bez portu)




- Format: `http://VOTRE_IP_LOCALE`
- Example: `http://192.168.68.57`



**3. Nazwa użytkownika RPC** : Nazwa użytkownika skonfigurowana w `rpcuser=` na bitcoin.conf




- Przykład: `satoshi



**4. Hasło RPC** : Hasło ustawione w `rpcpassword=` na bitcoin.conf



**5. Port RPC** : Port RPC w zależności od sieci




- Mainnet** : `8332`
- Zakładka**: `38332`



**6. Wallet**: Wybierz portfel Bitcoin Core zawierający UTXO, które mają być mieszane




- Przykład: `tuto_joinstr_signet`



**7. VPN Gateway**: Wybierz serwer Riseup VPN




- Przykład: `(Paris) vpn07-par.riseup.net`
- Inne dostępne: Amsterdam, Seattle itp.
- ⚠️ **Ważne**: Wszyscy uczestnicy z tej samej puli muszą korzystać z **tej samej bramy VPN**, aby wziąć udział w CoinJoin. Podczas rundy miksowania wszyscy uczestnicy muszą pojawić się z tym samym wyjściowym adresem IP, aby zapobiec korelacji uczestników przez analizę sieci



Aplikacja Joinstr **integruje natywnie** Riseup VPN, upraszczając koordynację między uczestnikami.



**Ważne** :




- Upewnij się, że telefon i komputer znajdują się w tej samej lokalnej sieci Wi-Fi
- Połączenie VPN zostanie aktywowane automatycznie podczas uczestnictwa w puli
- Po ustawieniu wszystkich parametrów kliknij **"Zapisz "**



## Praktyczne zastosowanie



### Tworzenie puli lub dołączanie do niej



![CRÉATION POOL ANDROID](assets/fr/10.webp)



Masz dwie możliwości uczestnictwa w CoinJoin:



**Opcja 1: Utwórz nową pulę**



Kliknij "Utwórz nową pulę" w zakładce "Pule". Określ nominał w BTC (np. 0,002 BTC) i żądaną liczbę uczestników (minimum 2, zalecane 3-5 dla większej anonimowości). Następnie aplikacja czeka, aż inni użytkownicy dołączą do puli. Po osiągnięciu wymaganej liczby, proces rejestracji wyjściowej rozpocznie się automatycznie, a ty będziesz musiał wybrać swój UTXO do mieszania i kliknąć "Zarejestruj się".



**⏱️ Ważne**: Pule wygasają po **10 minutach** braku aktywności. Jeśli wymagana liczba uczestników nie zostanie osiągnięta, pula zostanie automatycznie zamknięta.



**Opcja 2: Dołączenie do istniejącej puli**



W zakładce "Wyświetl inne pule" przejrzyj dostępne pule utworzone przez innych użytkowników. Wybierz pulę odpowiadającą Twojej kwocie i dołącz do niej. Upewnij się, że skonfigurowałeś ten sam przekaźnik Nostr i bramę VPN, co inni uczestnicy (patrz sekcja Konfiguracja).



**Reguła wyboru UTXO**: Twój UTXO musi być nieco wyższy niż nominał puli (między +500 a +5000 nadwyżki sats).



**Przykład**: W przypadku puli 0,002 BTC (200 000 sats) należy użyć UTXO między 200 500 a 205 000 sats.



![PROCESSUS COINJOIN](assets/fr/11.webp)



Proces jest następnie **w pełni automatyczny**: po zarejestrowaniu danych wejściowych aplikacja czeka, aż wszyscy uczestnicy zarejestrują swoje dane wejściowe. Po zarejestrowaniu wszystkich danych wejściowych tworzony jest PSBT, automatycznie podpisywany kluczami użytkownika, a następnie łączony z podpisami innych uczestników. Na koniec cała transakcja jest transmitowana w sieci Bitcoin. Po zakończeniu transmisji użytkownik otrzymuje TXID (identyfikator transakcji). W systemie Android nie jest wymagana ręczna manipulacja PSBT.



### Weryfikacja on-chain



![TRANSACTION MEMPOOL](assets/fr/12.webp)



Gdy transakcja zostanie wyemitowana, otrzymasz TXID (identyfikator transakcji). Można go wyświetlić na stronie [mempool.space](https://mempool.space) lub w ulubionej przeglądarce. Aby przetestować zakładkę, użyj [mempool.space/signet](https://mempool.space/signet).



Można obserwować :





- N zgłoszeń**: Jedno na uczestnika (w naszym przykładzie 2 zgłoszenia)
- N identycznych wyjść**: dokładna kwota nominału (tutaj 2 wyjścia po 0,00199800 BTC każde)
- Wykres przepływu**: mempool.space wizualnie wyświetla połączenie wejść i wyjść
- Cechy** : Transakcję można zidentyfikować jako SegWit, Taproot, RBF itp.



Ponieważ wszystkie główne wyjścia mają taką samą ilość, **niemożliwe jest określenie, które należy do kogo**. Jest to podstawowa zasada CoinJoin: nierozróżnialność wyjść.



**Przykład sygnetu transakcji** : [404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c](https://mempool.space/signet/tx/404a6a58a1682341c1197655fa492fa160bf63fca8c3b29be125e7360dbec44c)



**Uwaga**: Jeśli Twoje UTXO były większe niż nominał puli, będziesz mieć wyjścia walutowe (nadwyżki). Te walutowe UTXO pozostają identyfikowalne i muszą być zarządzane oddzielnie od zanonimizowanych wyjść. Nigdy nie należy ich łączyć z wyjściami mieszanymi.



## Pakiety jakości i anonimowości CoinJoin



Wydajność CoinJoin jest mierzona przez jego **anonset**: liczbę wyjść o identycznej wartości wyprodukowanych przez transakcję. Im wyższa jest ta liczba, tym trudniej jest określić, który wkład odpowiada któremu wyjściu.



Joinstr generuje obecnie pule średnio od **2 do 5 uczestników**. Liczby te są niższe niż w przypadku tradycyjnych scentralizowanych koordynatorów, takich jak Wasabi (50-100 uczestników) lub Whirlpool (5-10 uczestników), ale taka jest cena decentralizacji.



💡 **Aby szczegółowo zrozumieć zestawy anonimowości i ich obliczenia**, zapoznaj się z naszym pełnym kursem: [Zestawy anonimowości](https://planb.academy/fr/courses/65c138b0-4161-4958-bbe3-c12916bc959c/les-ensembles-danonymat-be1093dc-1a74-40e5-9545-2b97a7d7d431).



### Joinstr vs. inne CoinJoins




| Aspekt | Wasabi | Whirlpool/Ashigaru | JoinMarket | **Joinstr** |
|--------|--------|--------------------|------------|-------------|
| **Uczestnicy na pulę** | 50-100 | 5-10 | Zmienny (P2P) | **2-5** |
| **Koordynator** | Scentralizowany (zamknięty 2024) | Scentralizowany (aktywny) | P2P maker/taker | **Brak (Nostr)** |
| **Odporność na cenzurę** | Słaba | Średnia | Bardzo wysoka | **Bardzo wysoka** |
| **Opłaty koordynacyjne** | Procent | Opłata wejściowa | Zapłacone twórcom | **Brak** |
| **Dyskryminacja UTXO** | Tak (czarne listy) | Nie | Nie | **Nie** |

**Inne aktywne rozwiązania CoinJoin** :




- Ashigaru**: Open-source'owa implementacja protokołu Whirlpool ze scentralizowanym koordynatorem, ale możliwa do wdrożenia w sposób zdecentralizowany. Nadal działa po przejęciu Samourai Wallet w 2024 roku.
- JoinMarket**: Zdecentralizowane rozwiązanie P2P bez centralnego koordynatora, oparte na modelu biznesowym maker/taker, w którym "makerzy" zapewniają płynność i są wynagradzani przez "takerów".



https://planb.academy/tutorials/privacy/on-chain/ashigaru-terminal-9a0d46d3-33b9-4c64-84c5-bfa25b3a0add

**Podstawowy kompromis**: Joinstr i JoinMarket to jedyne dwa rozwiązania bez centralnego koordynatora. JoinMarket wykorzystuje model biznesowy P2P z zachętami finansowymi, podczas gdy Joinstr wykorzystuje Nostr do bezkosztowej koordynacji. Joinstr poświęca natychmiastową anonimowość na dużą skalę na rzecz prostoty (brak zarządzania twórcą/producentem) i całkowitego braku opłat za koordynację.



**Zalecenie praktyczne**: Aby zrekompensować mniejsze pule, przeprowadź kilka kolejnych rund CoinJoin z różnymi uczestnikami. Rozmieść rundy i zmień przekaźniki Nostr między każdą rundą, aby zmaksymalizować poufność.



Zachęcamy do zapoznania się z naszym kompletnym kursem na temat prywatności bitcoinów, aby uzyskać więcej informacji na ten temat:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Zalety i ograniczenia



### Najważniejsze wydarzenia



**Zwiększona prywatność**: Połączenie szyfrowania komunikacji Nostr, współdzielonej sieci VPN między uczestnikami i zalecanego korzystania z sieci Tor tworzy wielowarstwową ochronę, którą trudno obejść.



**Przejrzyste, minimalne koszty**: Brak kosztów koordynacji, tylko koszty mining są dzielone sprawiedliwie między uczestników. Żaden operator nie pobiera procentu.



### Ograniczenia do rozważenia





- Zmienna płynność**: Mniejsze pule, mogą czekać na zebranie się uczestników
- Projekt w toku**: Aplikacja w wersji beta, możliwe błędy. Przetestuj najpierw z małymi ilościami w zakładce
- Ataki Sybil**: Możliwość kontrolowania kilku uczestników puli przez jednego przeciwnika



## Najlepsze praktyki



**Izolacja UTXO**: Nigdy nie należy łączyć zmieszanego UTXO z niezmieszanym. Użyj oddzielnego portfela dla zanonimizowanych wyników.



**Konieczne jest wykonanie wielu rund**: Wykonaj co najmniej 3 kolejne rundy z różnymi uczestnikami. Różne ilości i czasy, aby uniknąć schematów. Rozmieść rundy w odstępie kilku godzin.



**Ochrona sieci**: Systematycznie korzystaj z sieci Tor oprócz wbudowanej sieci VPN. Generowanie efemerycznych kluczy Nostr dla każdej ważnej sesji.



**Ostrożny postęp**: Rozpocznij tworzenie zakładek od małych ilości.



## Wnioski



Joinstr reprezentuje prawdziwie zdecentralizowane rozwiązanie prywatności Bitcoin. Wykorzystując Nostr do koordynacji, eliminuje zależność od centralnych koordynatorów przy jednoczesnym zachowaniu suwerenności użytkownika.



**Dla użytkowników, którzy cenią sobie odporność na cenzurę i są gotowi wykonać kilka rund CoinJoin, aby zrekompensować mniejsze pule.



W kontekście rosnącej kontroli finansowej, zdecentralizowane narzędzia do ochrony prywatności stają się niezbędne.



## Zasoby



### Oficjalna dokumentacja




- [Oficjalna strona Joinstr](https://joinstr.xyz)
- [Dokumentacja użytkownika](https://docs.joinstr.xyz/users/using-joinstr)
- [Dokumentacja techniczna](https://docs.joinstr.xyz/overview/how-does-it-work)
- [kod źródłowy GitLab](https://gitlab.com/invincible-privacy/joinstr)
- [aplikacja na Androida](https://gitlab.com/invincible-privacy/joinstr-kmp/-/releases)



### Samouczki




- [Samouczek wtyczki Electrum](https://uncensoredtech.substack.com/p/tutorial-electrum-plugin-for-joinstr) - Kompletny przewodnik autorstwa Uncensored Tech



### Społeczność i wsparcie




- [Telegram Joinstr Group](https://t.me/joinstr) - Wsparcie społeczności i kąciki zakładek
- [Dyskusja techniczna na temat DelvingBitcoin](https://delvingbitcoin.org/t/who-will-run-the-coinjoin-coordinators/934)



### Dodatkowe narzędzia




- [Zakładka Faucet](https://signetfaucet.com) - Darmowe Bitcoiny testowe
- [Alt Signet Faucet](https://alt.signetfaucet.com) - alternatywa dla Faucet
- [Mempool.space](https://mempool.space) - Block explorer z analizą prywatności