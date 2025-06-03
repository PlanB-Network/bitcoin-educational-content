---
name: LNbits

description: Platforma księgowa dla sprzedawców
---

![presentation](assets/lnbits-intro.webp)

# System księgowy


LNbits jest wyposażony w wiele narzędzi do kontrolowania i kierowania przychodzących i wychodzących środków, podłączania sklepu internetowego, a nawet urządzeń takich jak Hardware Wallet lub bankomat, który sam zbudowałeś. Typy użytkowników obejmują:


- Właściciele Wallet, którzy chcą używać LNbits jako Interface do zarządzania swoimi środkami, a także jego dodatkowymi funkcjami.
- Sprzedawcy online i offline lub dostawcy usług, którzy chcą akceptować płatności Bitcoin onchain i Lightning Network.
- Programiści, którzy chcą tworzyć aplikacje Lightning Network.
- Operatorzy węzłów, którzy chcą zintegrować swój węzeł z systemem LNbits do celów księgowych.
- Każdy z nich ma inne potrzeby. Budujemy LNbits w sposób modułowy, aby każdy użytkownik mógł korzystać z naszych funkcji w sposób, który najbardziej mu odpowiada.


# Menedżer Wallet


LNbits to darmowy system księgowy o otwartym kodzie źródłowym, a nie menedżer węzłów. Zarządzanie kanałami jest domeną węzła Lightning, który jest podłączony do LNbits jako źródło finansowania, takie jak LND lub c-lightning. Użytkownicy Superuser lub Admin w systemie LNbits są odpowiedzialni za zarządzanie ogólną dostępnością i konfiguracją funkcji księgowych i wewnętrznych rozszerzeń.


LNbits działa jako Interface między użytkownikiem a węzłem Lightning, zapewniając prosty, przyjazny dla użytkownika sposób zarządzania i interakcji z siecią płatności.


Pomyśl o LNbits jak o "modułowym frameworku Wordpressa" dla Twojego węzła. Łatwa w zarządzaniu platforma, oparta na rozszerzeniach, które można łączyć w wielu przypadkach użycia.


Pomyśl o LNbits jak o własnym oprogramowaniu do zarządzania finansami bankowymi. Twój węzeł oferuje kanały płatności, a LNbits rozszerza Twój węzeł, aby móc uruchomić więcej niż jeden piorun Wallet, z którym jest dostarczany. Portfele te niekoniecznie muszą należeć do ciebie. Załóżmy, że jako operator węzła LN masz już wystarczającą płynność kanału i fundusze, a teraz chcesz zaoferować niektóre usługi bankowe Bitcoin swoim znajomym, rodzinie, własnemu sklepowi lub innym zwykłym sprzedawcom.


Zaoferujesz im prosty sposób na otwarcie "konta bankowego" na swoim węźle bez dostępu do innych portfeli na węźle i do całej płynności węzła, ale tylko do ich części. Twój węzeł (bank) działa tylko jako dostawca transportu dla ich płatności (przychodzących / wychodzących).


UWAGA: wszystkie środki, które Twoi "klienci" wpłacą na swoje konta bankowe LNbits w Twoim węźle, trafią bezpośrednio do kanałów LN Twojego węzła. Oznacza to, że TY jesteś prawdziwym właścicielem tych środków. Będziesz ponosić dużą odpowiedzialność za ich fundusze. Nie bądź zły i nie uciekaj z funduszami, nie bądź zły i nie pobieraj wysokich opłat. Chcemy pieprzyć bankierów fiat, a nie pieprzyć siebie nawzajem (użytkowników Bitcoin).


# Platforma demonstracyjna


Demo można znaleźć pod adresem [https://legend.lnbits.com](https://legend.lnbits.com). Jest w pełni funkcjonalny i może być używany do zapoznania się z Lightning Network i funkcjami LNbits i LNURL w ogóle. Chociaż nie możemy ci tego zabronić, chcielibyśmy poprosić, abyś nie używał go do konfiguracji produkcyjnej. Nie tylko często pracujemy nad serwerami, aby przetestować nowe funkcje, ale także chcielibyśmy zachęcić do uruchomienia własnego węzła i LNbits w suwerenny sposób. Jeśli uważasz, że prowadzenie węzła jest zbyt wymagające w tej chwili, możesz podłączyć LNbits do usługi finansowania powierniczego w chmurze, takiej jak Opennode, Luna lub Votage, lub do Lightning Tipbot na Telegramie, by wymienić tylko niektóre.


# Ulotka LNbits


Chcesz przekazać podstawowe informacje handlowcowi lub znajomemu z branży budowlanej? Z przyjemnością ogłaszamy naszą pierwszą ulotkę dla wszystkich. Rozmiar to typowy format ulotki z 6 stronami (2 zagięcia) o szerokości 3508 i wysokości 2480 pikseli.


LNbits dla handlowców: [EN](/assets/lnbits-merchants-en.pdf) | [DE](/assets/lnbits-merchants-de.pdf) | [ES](/assets/lnbits-merchants-es.pdf) | [IT](/assets/lnbits-merchants-it.pdf) | [PL](/assets/lnbits-merchants-pl.pdf)


LNbits dla konstruktorów: [EN](/assets/lnbits-builders-pl.pdf) | [DE](/assets/lnbits-builders-de.pdf) | [ES](/assets/lnbits-builders-es.pdf) | [IT](/assets/lnbits-builders-it.pdf) | [PL](/assets/lnbits-builders-pl.pdf)


# Kilka podstaw


LNbits działa w oparciu o protokół LNURL, co oznacza, że żądania są ważne w dwóch formach: jako łącze https:// clearnet (bez certyfikatów z podpisem własnym) lub jako łącze http:// v2/v3 onion. Aby oferować usługi LNbits, takie jak kody QR LNURLp/w lub karty NFC, które mogą być używane na wolności, należy otworzyć LNbits na clearnet (https).


Przed zainstalowaniem LNbits upewnij się, że przeczytałeś i zrozumiałeś poniższe ogólne wskazówki dotyczące tego, czym jest LNbits i jakie możliwości otwiera przed Tobą.



- [LND Guide](https://docs.lightning.engineering/) | Instalacja LND
- [Przykład konfiguracji LND](https://github.com/lightningnetwork/LND/blob/master/sample-LND.conf) | Ustawienia LND
- [Przewodnik CLN](https://docs.corelightning.org/docs/installation) | Instalowanie CLN
- [LUDs](https://github.com/lnurl/luds) LNURL Spec | [NIPs](https://github.com/nostr-protocol/nips) Nostr Spec
- [Uruchom Watchtower](https://docs.lightning.engineering/lightning-network-tools/LND/Watchtower) | Bardzo ważne!


Bardziej szczegółowe przewodniki dotyczące korzystania z LNbits w określonych scenariuszach przypadków użycia można znaleźć tutaj:



- [Getting Started with LNbits](https://darthcoin.substack.com/p/getting-started-lnbits) | Przewodnik Substack
- [ToDos dla twojego bezpieczeństwa z LNbits](https://youtu.be/i5FQf96e6zg) | Youtube Video
- [Prywatne banki na Lightning Network](https://darthcoin.substack.com/p/Bitcoin-private-banks-over-lightning) | Przewodnik po podpakowaniach
- [Uruchom portfele powiernicze dla znajomych i rodziny] (https://darthcoin.substack.com/p/the-bank-of-lnbits) | Przewodnik po Substack
- [LNbits dla małej restauracji / hotelu](https://darthcoin.substack.com/p/lnbits-for-small-merchants) | Przewodnik Substack
- [Korzystanie z pilota LNbits Streamer](https://darthcoin.substack.com/p/lnbits-streamer-copilot) | Przewodnik po Substack
- [Rozpocznij swój NOSTR Market z LNbits](https://darthcoin.substack.com/p/lnbits-nostr-market) | Przewodnik po Substack
- [Wykorzystanie LNbits w projektach szkolnych lub wydarzeniach festiwalowych](https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools) Przewodnik Substack



# Zainstaluj LNbits


## Podstawowa instrukcja instalacji


LNbits można zainstalować na dowolnym komputerze z systemem operacyjnym Linux. Nie wymaga potężnej maszyny ani serwera, wystarczy wystarczająca ilość pamięci RAM i trochę miejsca na dysku na bazę danych. Może być uruchamiany oddzielnie od węzła BTC/LN (lokalny komputer PC lub zdalny VPS) lub razem na tej samej maszynie z węzłem lub już zainstalowany na maszynie z oprogramowaniem węzła.


Do wyboru są najpopularniejsze menedżery pakietów, takie jak poetry i nix. Domyślnie LNbits używa SQLite jako bazy danych. Można również użyć PostgreSQL, który jest zalecany dla aplikacji o dużym obciążeniu. [Oto przewodnik po podstawowej instalacji przy użyciu poetry lub nix](https://github.com/lnbits/lnbits/blob/main/docs/guide/installation.md).


Dla wszystkich początkujących znajdziesz bardziej szczegółowe przewodniki krok po kroku dotyczące uruchamiania LNbits w określonych środowiskach:


- [LNbits on clearnet](https://ereignishorizont.xyz/lnbits-server/en/) by Axel
- [LNbits na VPS](https://github.com/TrezorHannes/vps-lnbits) by Hannes
- [LNbits on cloudflare](https://www.nodeacademy.org/lnbits) by Leo


Można również znaleźć film na stronie [dockerised Setup on a VPS with PostgreSQ, LightningTipBot as a funding source using nginx](https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/).


[Więcej scenariuszy instalacji tutaj](https://darthcoin.substack.com/p/build-your-own-lnbits-app-server).


W przypadku węzłów oprogramowania bundle należy zapoznać się z ich szczegółową dokumentacją dotyczącą LNbits: [Citadel](https://runcitadel.space) | [Umbrel](https://umbrel.com) | [MyNode](https://mynodebtc.com) | [RaspiBlitz](https://raspiblitz.org/) | [RaspiBolt](https://raspibolt.org)


## LNbits SaaS


Jeśli nie zajmujesz się sprawami technicznymi i nie chcesz samodzielnie hostować swojego źródła finansowania ani lnbits, możesz skorzystać z wersji [LNbits SaaS](https://saas.lnbits.com) (Software-as-a-service). Jest to w zasadzie jak LNbits w chmurze, ale możesz samodzielnie zdefiniować źródło finansowania (np. swój węzeł, LNbits Wallet, LNtipbot, fakewallet itp.) i zmienne środowiskowe - co w większości przypadków nie ma miejsca w przypadku innych rozwiązań chmurowych.


[Tutaj znajduje się szczegółowy przewodnik, jak korzystać z LNbits SaaS w konkretnych przypadkach użycia] (https://darthcoin.substack.com/p/lnbits-saas-a-solution-for-schools).


## Źródła finansowania


LNbits nie jest oprogramowaniem do zarządzania węzłami, ale systemem księgowym skoncentrowanym na LN na szczycie źródła finansowania LND lub CLN. Po pierwszej instalacji można odwiedzić stronę LNbits pod adresem http://localhost:5000/.


Aby zmodyfikować źródło finansowania, przejdź do adresu URL superużytkownika i wybierz źródło finansowania w "Zarządzaj serwerem" lub edytuj plik .env, modyfikując `LNBITS_BACKEND_WALLET_CLASS` do potrzebnego źródła, jeśli ustawiłeś `adminUI=TRUE` w `.env`.


Plik .env można znaleźć w folderze lnbits/ lub lnbits/apps/data, rozszerzając polecenie do listy plików w katalogu za pomocą `ls -a`.


Może być również konieczne zainstalowanie dodatkowych pakietów lub wykonanie dodatkowych kroków konfiguracji, wybierając żądane źródło finansowania. Po ponownym uruchomieniu nowa konfiguracja będzie aktywna.


Z jakich źródeł finansowania mogę skorzystać w przypadku LNbits?


LNbits może działać na wielu źródłach finansowania sieci lightning. Obecnie dostępne jest wsparcie dla CoreLightning, LND, LNbits, LNPay, OpenNode, a kolejne są regularnie dodawane.

Ważne jest, aby wybrać źródło, które ma dobrą płynność i dobrych partnerów. Jeśli używasz LNbits do usług publicznych, płatności użytkowników mogą płynąć szczęśliwie w obu kierunkach.


Backend Wallet (źródło finansowania) można skonfigurować za pomocą następujących zmiennych środowiskowych LNbits w pliku `.env` lub na koncie superużytkownika w sekcji Manage-Server.

Jeśli chcesz użyć wersji .env, możesz znaleźć parametry tutaj:



### CoreLightning


- CLN
  - `LNBITS_BACKEND_WALLET_CLASS`: **CoreLightningWallet**
  - `CORELIGHTNING_RPC`: /file/path/lightning-RPC
- Spark (c-lightning)
  - `LNBITS_BACKEND_WALLET_CLASS`: **SparkWallet**
  - `SPARK_URL`: http://10.147.17.230:9737/RPC
   - `SPARK_TOKEN`: secret_access_key

### Lightning Network Daemon


- LND (REST)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndRestWallet**
  - `LND_REST_ENDPOINT`: http://10.147.17.230:8080/
  - `LND_REST_CERT`: /file/path/tls.cert
  - `LND_REST_MACAROON`: /file/path/admin.macaroon lub Bech64/Hex
  - `LND_REST_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn
- LND (gRPC)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LndWallet**
  - `LND_GRPC_ENDPOINT`: ip_address
  - `LND_GRPC_PORT`: port
  - `LND_GRPC_CERT`: /file/path/tls.cert
  - `LND_GRPC_MACAROON`: /file/path/admin.macaroon lub Bech64/Hex

Zamiast tego można również użyć makaronu zaszyfrowanego AES (więcej informacji), używając opcji


  - `LND_GRPC_MACAROON_ENCRYPTED`: eNcRyPtEdMaCaRoOn

Aby zaszyfrować macaroon, uruchom `./venv/bin/python lnbits/wallets/macaroon/macaroon.py`.


### LNbits (kolejna instancja LNbits)



- Instancja LNbits hostowana na serwerze w chmurze lub własnym serwerze domowym
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://lnbits.mydomain.com
  - `LNBITS_KEY`: my-lnbits-AdminKey
- Serwer demonstracyjny LNbits Legend (!! NIE używaj go do celów produkcyjnych / komercyjnych, tylko do testowania !!)
  - `LNBITS_BACKEND_WALLET_CLASS`: **LNbitsWallet**
  - `LNBITS_ENDPOINT`: https://legend.lnbits.com
  - `LNBITS_KEY`: legend-lnbits-AdminKey

### Lightning TipBot


Aby połączyć się z [Lightning Tipbot](https://t.me/LightningTipBot) z Telegram, musisz ustawić następujący parametr:


  - `LNBITS_BACKEND_WALLET_CLASS`: **LnTipsWallet**
  - `LNBITS_ENDPOINT`: https://LN.tips
  - `LNBITS_KEY`: Aby uzyskać klucz, należy raz uruchomić /api na prywatnym czacie z LightningTipbot na Telegramie.


Zobacz także ten samouczek, jak zainstalować [LNbits z LightningTipBot przez vps] (https://www.massmux.com/howto-complete-lightningtipbot-lnbits-setup-vps/)


### IBEX HUB


Zarejestruj się [tutaj] (https://ibexpay.ibexmercado.com/onboard), a następnie pobierz klucze/tokeny stamtąd, punkt końcowy to https://ibexpay-api.ibexmercado.com.

Więcej informacji można znaleźć w [IBEX API-Documentation](https://ibexpay-api.readme.io/reference/getting-started-with-your-api).


### LNPay

Aby słuchacz Invoice działał, musisz mieć publicznie dostępny adres URL w LNbits i skonfigurować [LNPay webhook](https://dashboard.lnpay.co/webhook/) wskazujący na `<twój host LNbits>/Wallet/webhook` ze zdarzeniem "Wallet Receive" i bez podanego sekretu. Ustawienie `https://mylnbits/Wallet/webhook` będzie adresem URL punktu końcowego, który zostanie powiadomiony o każdej płatności.


  - `LNBITS_BACKEND_WALLET_CLASS`: **LNPayWallet**
  - `LNPAY_API_ENDPOINT`: https://api.lnpay.co/v1/
  - `LNPAY_API_KEY`: sak_apiKey
  - `LNPAY_WALLET_KEY`: waka_apiKey


### OpenNode

Aby Invoice działał, musisz mieć publicznie dostępny adres URL w LNbits. Ustawienie webhook jest opcjonalne.


  - `LNBITS_BACKEND_WALLET_CLASS`: **OpenNodeWallet**
  - `OPENNODE_API_ENDPOINT`: https://api.opennode.com/
  - `OPENNODE_KEY`: opennodeAdminApiKey


### Alby


Alby to rozszerzenie przeglądarki z funkcjami LN Wallet i kontem LNDHUB, które może być używane jako źródło finansowania dla LNbits. [Więcej szczegółów tutaj](https://getalby.com/).


Aby Invoice działał, musisz mieć publicznie dostępny adres URL w LNbits. Nie jest konieczne ręczne ustawianie webhooków. Możesz generate token dostępu Alby tutaj: https://getalby.com/developer/access_tokens/new



- `LNBITS_BACKEND_WALLET_CLASS`: AlbyWallet
- `ALBY_API_ENDPOINT`: https://api.getalby.com/
- `ALBY_ACCESS_TOKEN`: AlbyAccessToken


## Dodatkowe / Przewodniki rozwiązywania problemów


Oto kilka dodatkowych instrukcji na wypadek, gdyby były potrzebne. Kliknij strzałkę, aby rozwinąć opis.


### The Killswitch 🚨


Ostatnio pojawiło się tak wiele niebezpiecznych błędów nie tylko w całej przestrzeni, ale także w LNbits, że postanowiliśmy coś z tym zrobić. Możesz teraz wyrazić zgodę na otrzymywanie ostrzeżeń i/lub podejmowanie bezpośrednich działań, gdy ponownie pojawi się luka lub błąd, który może prowadzić do utraty środków.


![killswitchn](assets/lnbits-killswitch.webp)


Po przełączeniu na void-Wallet wszystkie typy użytkowników na instancji zobaczą żółty baner w miejscu, w którym normalnie można znaleźć powiadomienie "LNbits jest w wersji beta" obok obszaru motywu / języka po prawej stronie - i jest to najbardziej oczywista wskazówka, że coś się stało. Spójrz na nową kartę serwera podświetloną w Green w lewej części okna.


Jak to działa? Gdy killswitch jest włączony, tajne repozytorium github dostępne tylko dla głównego zespołu LNbits będzie sprawdzane w odstępie X minut (który można określić). Jeśli podatny błąd zostanie opublikowany w tym repozytorium, służy to jako sygnał, który uruchamia killswitch na wszystkich instalacjach, które zasubskrybowały i przełącza twoją instancję lnbits do korzystania z void Wallet. Jeśli chmury zostały oczyszczone i zainstalowałeś aktualizację zabezpieczeń, możesz ustawić źródło finansowania na swój węzeł, Wallet lub cokolwiek innego, czego używasz, również za pośrednictwem sekcji Zarządzaj serwerem. Ta wiki zawiera sekcję dotyczącą przełączania źródeł finansowania, jeśli nie wiesz, co skonfigurować.



### Różnica między administratorem a superużytkownikiem


Interfejs administratora LNbits pozwala na zmianę ustawień LNbits poprzez frontend LNbits. Jest on domyślnie wyłączony i przy pierwszym ustawieniu zmiennej środowiskowej `LNBITS_ADMIN_UI=true` w pliku `.env`, ustawienia są inicjowane i będą używane. Od tego momentu używane są odpowiednie ustawienia z bazy danych zamiast tych z pliku .env.


### Superużytkownik


Wraz z interfejsem administratora wprowadziliśmy superużytkownika, który ma dostęp do serwera, dzięki czemu może zmieniać ustawienia, które mogą spowodować awarię serwera lub uniemożliwić jego działanie za pośrednictwem interfejsu frontend i api, np. zmieniając źródło finansowania. Superużytkownik jest przechowywany tylko w tabeli ustawień bazy danych. Po przywróceniu ustawień domyślnych i ponownym uruchomieniu tworzony jest nowy superużytkownik. Dodaliśmy również dekorator dla tras API, aby sprawdzić istnienie superużytkownika. Jego identyfikator nigdy nie jest wysyłany przez API i frontend i otrzymuje tylko bool (tak/nie), jeśli jesteś super użytkownikiem lub nie.


Tylko superużytkownik może przesyłać satoshis do różnych portfeli za pośrednictwem sekcji "Doładowanie".


Możesz również wysłać superużytkownika za pośrednictwem webhooka do innej usługi, gdy zostanie ona utworzona. Więcej informacji tutaj https://github.com/lnbits/lnbits/blob/main/lnbits/settings.py `class SaaSSettings`


W interfejsie użytkownika znajdziesz również możliwość zmiany obrazu sklepu, który jest wyświetlany na stronie "Utwórz Wallet", otwierając sekcję Zarządzaj serwerem i wybierając Motyw -> Niestandardowe logo.


### Użytkownicy admini


Zmienna środowiskowa: `LNBITS_ADMIN_USERS`, sortowana przecinkami lista identyfikatorów użytkowników. Użytkownicy admin mogą zmieniać ustawienia w interfejsie administratora - z wyjątkiem ustawień źródła finansowania, ponieważ wymagałoby to restartu serwera i mogłoby potencjalnie uniemożliwić dostęp do serwera. Mają również dostęp do wszystkich rozszerzeń dedykowanych im w `LNBITS_ADMIN_EXTENSIONS`.


### Dozwoleni użytkownicy


Zmienna środowiskowa: `LNBITS_ALLOWED_USERS`, sortowana przecinkami lista identyfikatorów użytkowników. Po zdefiniowaniu tych użytkowników LNbits nie będzie już dostępny publicznie. Tylko zdefiniowani użytkownicy i administratorzy mogą uzyskać dostęp do interfejsu LNbits.




#### Aktualizacja LNbits

Normalna aktualizacja lokalnej instancji LNbits polega po prostu na kopiowaniu i wklejaniu następujących poleceń CLI:


```
cd lnbits
## Stop LNbits with `ctrl + x`
git pull
## Keep your poetry install up to date, this can be done with
poetry self update
poetry install --only main
## or
git checkout main && git pull && poetry install
## Start LNbits with
poetry run lnbits
```


Jeśli korzystasz z Raspiblitz lub MyNode, możesz dodatkowo potrzebować aplikacji

```
sudo systemctl restart lnbits
```

na końcu, ponieważ uruchamia LNbits jako usługę.


Na Umbrel/Citadel polecenia będą następujące

```
cd ~/apps/lnbits
git pull upstream main
sudo ~/scripts/app start lnbits
```


#### Migracja SQLite do PostgreSQL


Jeśli LNbits jest już zainstalowany i działa na bazie danych SQLite, zdecydowanie zalecamy migrację do postgres, jeśli planujesz uruchomić LNbits na dużą skalę.


Dołączony jest skrypt, który może łatwo przeprowadzić migrację. Musisz mieć już zainstalowany Postgres i powinno być hasło dla użytkownika (patrz instrukcja instalacji Postgres powyżej). Ponadto instancja LNbits musi zostać uruchomiona raz na Postgres, aby zaimplementować bazę danych Schema, zanim migracja będzie mogła zadziałać:


```
# STOP LNbits

# add the database connection string to .env 'nano .env' LNBITS_DATABASE_URL=
# postgres://<user>:<password>@<host>/<database> - alter line bellow with your user, password and db name
LNBITS_DATABASE_URL="postgres://postgres:postgres@localhost/lnbits"
# save and exit

# START LNbits
# STOP LNbits
poetry run python tools/conv.py
# or
make migration
```

Miejmy nadzieję, że teraz wszystko działa i zostanie zmigrowane... Uruchom ponownie LNbits i sprawdź, czy wszystko działa poprawnie.



#### Tworzenie kopii zapasowych i przywracanie bazy danych


Zapoznaj się z [tym bardzo szczegółowym przewodnikiem po procesie tworzenia kopii zapasowych i przywracania] (https://ereignishorizont.xyz/lnbits-server/en/#94_LNbits_-_Databases_Backup_Restore).



#### Finansowanie mojego LNbits Wallet z mojego węzła nie działa


Jeśli chcesz wysyłać Sats z tego samego węzła, który jest źródłem finansowania twoich LNbits, będziesz musiał edytować plik LND.conf.


Parametry, które należy uwzględnić to: `allow-circular-route=1`


Należy to zrobić w sekcji Opcje aplikacji pliku LND.conf. W niektórych węzłach bundle uruchomienie LND może zakończyć się niepowodzeniem.


UWAGA: Zamiast tego zaleca się korzystanie z nowego rozszerzenia adminUI z opcją "TopUp", aby dodać środki do konta LNbits.


#### Błąd 426

Otrzymałem błąd: "lnurl musi być dostarczony przez publicznie dostępną domenę https lub tor. wymagana aktualizacja 426"</podsumowanie>


Ten błąd zwykle wynika z faktu, że LNbits za tunelem ngnix nie przekazuje poprawnie LNURL Address. Zatrzymaj LNbits i edytuj plik .env dodając ten wiersz:

`FORWARDED_ALLOW_IPS=*`


Również jeśli używasz konfiguracji ngnix, upewnij się, że masz te nagłówki w konfiguracji ngnix:


```
RequestHeader set "X-Forwarded-Proto" expr=%{REQUEST_SCHEME}
RequestHeader set "X-Forwarded-SSL" expr=%{HTTPS}
```


#### Błąd sieci

Otrzymałem "błąd https", błąd sieci" lub inne podczas skanowania QR</summary>


Zła wiadomość, jest to błąd routingu, który może mieć wiele przyczyn. Najpierw sprawdź LNURL QR za pomocą [Lightning Decoder](https://lightningdecoder.com/), jeśli znajdziesz tam coś dziwnego. Wypróbujmy kilka najbardziej możliwych problemów i ich rozwiązań.


LNbits działa tylko przez Tor, nie można go otworzyć w domenie publicznej, takiej jak lnbits.yourdomain.com



- Biorąc pod uwagę, że chcesz, aby Twoja konfiguracja pozostała w ten sposób, otwórz LNbits Wallet za pomocą .onion URI i utwórz go ponownie. W ten sposób QR jest generowany tak, aby był dostępny za pośrednictwem tego .onion URI, a więc tylko przez tor. Nie generate tego QR z .local URI, ponieważ nie będzie on dostępny przez Internet - tylko z domowej sieci LAN.
- Otwórz aplikację LN Wallet, której użyłeś do zeskanowania QR i tym razem użyj tor (zobacz ustawienia aplikacji Wallet). Jeśli aplikacja nie oferuje tor, można zamiast tego użyć Orbot (Android). Zobacz sekcję instalacji, aby uzyskać szczegółowe instrukcje dotyczące otwierania LNbits dla clearnet/https.



#### Uniemożliwienie innym generowania portfeli na moich LNbitach


Kiedy uruchamiasz swoje LNbits w clearnet, w zasadzie każdy może na nim generate i Wallet. Ponieważ fundusze węzła są powiązane z tymi portfelami, warto temu zapobiec. Można to zrobić na dwa sposoby:


Skonfiguruj dozwolonych użytkowników i rozszerzenia w pliku `.env` ([zobacz przykład env tutaj](https://github.com/lnbits/lnbits/blob/main/.env.example)). Działa to tylko wtedy, gdy używasz ustawienia `adminUI=FALSE` w .env, w przeciwnym razie musisz to zrobić w sekcji Zarządzaj serwerem -> Użytkownicy -> Dozwoleni użytkownicy. Wszyscy inni nie będą później dopuszczeni.




#### Dostosuj ramy czasowe wygaśnięcia Invoice


Teraz możesz wystawiać faktury generate z niestandardowym terminem ważności. Kompatybilny z backendami: LndRestWallet, LndWallet, CoreLightningWallet, EclairWallet, LnbitsWallet, SparkWallet jak dotąd!


Możesz ustawić `LIGHTNING_INVOICE_EXPIRY` w pliku .env lub użyć AdminUI, aby zmienić domyślną wartość dla wszystkich faktur. Istnieje również nowe pole w punkcie końcowym /api/v1/payments, w którym można ustawić wygaśnięcie w danych JSON.




## Usunięto Wallet-URL


### Wallet na serwerze demonstracyjnym legend.lnbits


Zawsze zapisuj kopię Wallet-URL, Export2phone-QR lub LNDhub dla własnych portfeli w bezpiecznym miejscu. LNbits NIE MOŻE pomóc w ich odzyskaniu w przypadku utraty.


### Wallet na własnym źródle finansowania/węźle

Zawsze zapisuj kopię Wallet-URL, Export2phone-QR lub LNDhub dla własnych portfeli w bezpiecznym miejscu. Wszystkich użytkowników LNbits i identyfikatory Wallet można znaleźć w rozszerzeniu menedżera użytkowników LNbits lub w bazie danych sqlite. Aby edytować lub odczytać bazę danych LNbits, przejdź do folderu LNbits /data i poszukaj pliku o nazwie sqlite.db. Można go otworzyć i edytować za pomocą programu Excel lub dedykowanego edytora SQL, takiego jak [SQLite browser](https://sqlitebrowser.org/).


Możesz także zrzucić portfele za pomocą CLI i wyświetlić każdy Wallet w swojej bazie danych.


```
cd ~/app-data/lnbits/data
sqlite3 database.sqlite3
.dump wallets
```


Wynik będzie wyglądał mniej więcej tak


```
INSERT INTO wallets VALUES('f8a43fc363ea428db5c53b3559935f1f','NAME OF WALLET','1280ff5910a9c485a782a2376f338b6c','33b95b099ce848e3b484124373f681e5','2cca208ae6d94d438227b9487ff216f9');
```

i chcesz umieścić te wartości w adresie url w następujący sposób


```
https://your.lnbits.com/wallet?usr=1280ff5910a9c485a782a2376f338b6c&wal=f8a43fc363ea428db5c53b3559935f1f
```


Przy czym f8a43fc363ea428db5c53b3559935f1f należy zastąpić wartością, która znajduje się przed nazwą (w naszym przykładzie f8a43fc363ea428db5c53b3559935f1f), a 1280ff5910a9c485a782a2376f338b6c jest użytkownikiem i powinno stać się wartością wyświetlaną po nazwie. Aby zamknąć sqlite3 wpisz


```
.quit
```

#### LNURL dla Lightning-Address odwrotnie


Wypróbuj ten [koder](https://lnurl-codec.netlify.app/) od fiatjaf lub [ten](https://lightningdecoder.com/). Aby zapłacić lub sprawdzić LNURLp, możesz również użyć [LNurlpay](https://wwww.lnurlpay.com/). Powinien on zawierać HTTPS, a nie HTTP.



#### Skonfiguruj komentarz, który ludzie widzą podczas płacenia za mój LNURLp QR

Podczas tworzenia LNURL-p pole komentarza nie jest domyślnie wypełnione. Oznacza to, że komentarze nie mogą być dołączane do płatności.


Aby zezwolić na komentarze, należy dodać znaki o długości od 1 do 250. Po wprowadzeniu liczby pole komentarza będzie wyświetlane w procesie płatności. Możesz także edytować już utworzony LNURL-p i dodać ten numer.


![lnbits comments](assets/lnbits-comments.webp)


#### Wpłać onchain BTC do LNbits

Istnieją dwa sposoby Exchange Sats z onchain BTC do LN BTC (resp. do LNbits).


##### Za pośrednictwem zewnętrznej usługi wymiany.


Inni użytkownicy, którzy nie mają dostępu do twojego LNb, mogą skorzystać z usługi wymiany, takiej jak [Boltz](https://boltz.Exchange/), [FixedFloat](https://fixedfloat.com/), [DiamondHands](https://swap.diamondhands.technology/) lub [ZigZag](https://zigzag.io/). Jest to przydatne, jeśli dostarczasz tylko faktury LNURL/LN ze swojej instancji LNbits, ale płatnik ma tylko onchain Sats, więc będzie musiał najpierw zamienić te Sats po swojej stronie. Procedura jest prosta: użytkownik wysyła onchain btc do usługi swap i podaje LNURL / LN Invoice z LNbits jako miejsce docelowe swapu.


##### Korzystanie z rozszerzenia Onchain i Boltz LNbits.


Należy pamiętać, że jest to oddzielny Wallet, a nie LN btc, który jest reprezentowany przez LNbits jako "twój Wallet" na źródle finansowania LN. Ten onchain Wallet może być również używany do wymiany LN btc na (np. portfel sprzętowy) za pomocą rozszerzenia LNbits Boltz lub Deezy. Jeśli prowadzisz sklep internetowy, który jest połączony z twoim LNbits dla płatności LN, bardzo przydatne jest regularne spuszczanie całego Sats z LN do onchain. Prowadzi to do większej ilości miejsca w kanałach LN, aby móc odbierać nowe, świeże Sats.


Procedura dla osób nieposiadających Bitcoin Hardware Wallet:



- Użyj Electrum lub Sparrow Wallet, aby utworzyć nowy onchain Wallet i zapisz kopię zapasową seed w bezpiecznym miejscu.
- Przejdź do informacji Wallet i skopiuj xpub.
- Przejdź do LNbits - Onchain extension i utwórz nowy Watch-only wallet z tym xpubem.
- Przejdź do LNbits - Rozszerzenie Tipjar i utwórz nowy Tipjar. Wybierz również opcję onchain oprócz LN Wallet.
- Opcjonalnie - przejdź do LNbits - rozszerzenie SatsPay i utwórz nową opłatę za btc onchain. Możesz wybrać pomiędzy onchain i LN lub obydwoma. Następnie utworzy Invoice, który można udostępnić.
- Opcjonalnie - jeśli używasz LNbits połączonego ze stroną Wordpress + Woocommerce, po utworzeniu / połączeniu Watch-only wallet ze sklepem LN btc Wallet, klient będzie miał obie opcje płatności na tym samym ekranie.


Po otrzymaniu płatności w LNbits, dziennik transakcji wyświetli tylko wznowiony typ transakcji.


![lnbits payment details](assets/lnbits-payment-details.webp)


W przeglądzie transakcji znajdziesz małą strzałkę Green oznaczającą środki otrzymane i czerwoną strzałkę oznaczającą środki wysłane.


Jeśli klikniesz na te strzałki, wyskakujące okienko szczegółów pokaże załączone wiadomości, a także nazwę nadawcy, jeśli została podana.


Aby skonfigurować nazwę do wyświetlania w płatnościach, w LNbits nie jest to obecnie możliwe - ale do odbioru. Jest to możliwe tylko wtedy, gdy LN Wallet nadawcy obsługuje [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (nameDesc) jak [OBW, Blixt, Alby, ZBD, BitBanana](https://github.com/lnurl/luds?tab=readme-ov-file#lnurl-documents).


Następnie zobaczysz alias/pseudonim w sekcji szczegółów swoich transakcji LNbits (kliknij strzałki). Pamiętaj, że możesz podać tam dowolną nazwę i może ona nie być powiązana z prawdziwą nazwą nadawcy, jeśli taką otrzymasz.


![lnbits namedesc](assets/lnbits-namedesc.webp)


Aby zaimportować konto LNbits do aplikacji Wallet, otwórz LNbits z kontem / Wallet, którego chcesz użyć, przejdź do "zarządzaj rozszerzeniami" i aktywuj rozszerzenie LNDHUB. Otwórz rozszerzenie LNDHUB, wybierz Wallet, którego chcesz użyć i zeskanuj QR "admin" lub "tylko Invoice", w zależności od poziomu bezpieczeństwa, który chcesz dla tego Wallet.


Możesz użyć [Zeus](https://zeusln.app/) lub [Bluewallet](https://bluewallet.io/) jako aplikacji Wallet dla konta lndhub, przy czym BW obsługuje więcej niż jeden taki Wallet.


Podczas wykonywania tej czynności zalecamy również ustawienie identyfikatora URI sieci LN na identyfikator własnego węzła. Jeśli twoja instancja LNbits to tylko Tor, musisz również używać tych aplikacji z aktywowanym Torem. Również w tym przypadku musisz otworzyć stronę LNbits za pośrednictwem Tor .onion Address.


Jeśli masz błąd "nieobsługiwany typ Hash" podczas korzystania z ypub w rozszerzeniu On-Chain, sprawdź, czy twoja instancja LNbits używa pythona 3.10, może to mieć wpływ na [ten problem] (https://stackoverflow.com/questions/72409563/unsupported-Hash-type-ripemd160-with-hashlib-in-python). Edytuj openssl.cnf jak opisano w odpowiedzi stackoverflow i uruchom ponownie LNbits.



## Oprzyrządowanie i tworzenie z LNbits


LNbits posiada różnego rodzaju [otwarte interfejsy API] (https://legend.lnbits.com/docs) i narzędzia do programowania i łączenia się z wieloma różnymi urządzeniami dla miliarda przypadków użycia.


Jeśli dopiero zaczynasz budować, zacznij od tego [Prezentacje MakerBits](https://www.youtube.com/channel/UCZhKfzK6_KWZ-CFC2wXQVBw/videos) od Bena Arc o budowaniu gadżetów opartych na LNbits.


### WAŻNE:


- LNbits działa w oparciu o protokół LNURL, którego żądania są ważne w dwóch formach: jako łącze https:// clearnet (bez certyfikatów z podpisem własnym) lub jako łącze cebulowe http:// v2/v3. Aby oferować usługi LNbits, takie jak kody QR LNURLp/w lub karty NFC, które mogą być używane na wolności, musisz otworzyć LNbits na clearnet (https).
- Do zasilania esp32 należy używać wyłącznie kabli DATA-Cables. Nie wszystkie kable obsługują dane oprócz zasilania esp. Nie byłbyś pierwszy, gdyby kabel dostarczony z esp był tylko kablem zasilającym
- Upewnij się, że nie używasz koncentratora USB z podłączonymi innymi urządzeniami. Może to prowadzić do dziwnych efektów, które są Hard do debugowania (np. brak uruchamiania lub zatrzymywania).
- Do realizacji projektów esp w systemie MacOS potrzebny jest sterownik mostka UART. Jeśli masz problemy ze sterownikiem w systemach Mac lub Linux, możesz je znaleźć tutaj lub, jeśli chodzi o wyświetlacz TTGO, tutaj. Jeśli korzystasz z systemu Windows i masz problemy z połączeniem, upewnij się, że pobrałeś STARĄ wersję 11.1.0, ponieważ nowsza nie działa! Możesz również znaleźć terminal szeregowy tutaj, aby sprawdzić połączenie - ustaw prędkość 115200.
- Chociaż korzystanie z Platform.io jest znacznie wygodniejsze (np. zależności są instalowane automatycznie), zalecamy korzystanie z Arduino wszystkim początkującym.
- TT-Go Display S3: Kolor zakładki folii ochronnej ekranu informuje, który dokładnie kontroler (ST7735_redtab, ST7735_blacktag, ST7735_greetab, greentab128, ..) został użyty do jej zbudowania. Zachowaj go, aby móc debugować, jeśli programujesz się, a ekran nie wyświetla poprawnie grafiki, np. kolory są nieprawidłowe, obrazy lustrzane lub zbłąkane piksele na krawędziach. Jeśli kiedykolwiek będziesz musiał to zrobić, istnieje epicki przewodnik na temat dostosowywania się do różnych wyświetlaczy
- Zawsze używaj małych liter lnurl239xx zamiast LNURLl239xx
- Dodanie lightning:lnurl1234xyz utworzy QR, który zażąda otwarcia Wallet użytkownika dla tego Invoice podczas skanowania (ostatnio zainstalowana aplikacja lightning na iOS, ustawienie w Androidzie)
- Jeśli flashujesz esp32 przez Internet, będzie działać tylko z tymi przeglądarkami (TL: DR Chrome, Edge i Opera).
- Zwróć uwagę na to odniesienie PIN-OUT dla esp
- Kiedy używasz FOSSoftware lub FOSGuides pls zawsze linkuj autora. Każdy uwielbia patrzeć, jak jego dziecko rośnie, a także inicjuje łańcuch budowania, który jest niesamowity do oglądania :)


Przyjdź do grupy [Makerbits Telegram Group](https://t.me/makerbits), jeśli potrzebujesz pomocy z projektem - mamy Cię!


![lnbits hackathlon](assets/lnbits-hackathlon.webp)


Oto kilka kategorii projektów, które można zbudować za pomocą LNbits:



- [Nostr Signing Device](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#nostr-signing-device)
- [Archade Machine](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#arcade-machine)
- [Gerty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#gerty)
- [Nostr Zap Lamp](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#zap-lamp)
- [BTC/LN ATM](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#atm)
- [LNPoS](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lnpos-terminal)
- [Lightning Piggy](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lightning-piggy)
- [Hardware Wallet](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#hardware-Wallet)
- [Bitcoin Switch](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-switch)
- [Automat](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#vending-machine)
- [Bolty](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#bolty)
- [Nerdminer](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Nerdminer)
- [Bitcoin Ticker](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#Bitcoin-ticker)
- [BTClock](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#btclock)
- [Lora i Mesh Networking](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#lora)



- [POMOCNICY I ZASOBY](https://github.com/lnbits/lnbits/wiki/Tooling-&-Building-with-LNbits#resources)
- [Więcej przykładów projektów "Powered by LNbits" tutaj](https://github.com/lnbits/lnbits/wiki/Powered-by-LNbits).
- [Przypadki użycia dla LNbits](https://github.com/lnbits/lnbits/wiki/Use-Cases-of-LNbits)