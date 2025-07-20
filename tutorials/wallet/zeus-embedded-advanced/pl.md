---
name: Zeus Embedded - Advanced
description: Wielowęzłowy, samoobsługowy Wallet
---

![Zeus](assets/cover.webp)


## Wprowadzenie do ZEUS Wallet


ZEUS to mobilna aplikacja do zarządzania Bitcoin Wallet i węzłami z pełną funkcjonalnością Bitcoin Lightning Wallet, która sprawia, że płatności Bitcoin są proste, daje użytkownikom pełną kontrolę nad ich finansami i pozwala bardziej zaawansowanym użytkownikom zarządzać węzłami Lightning z dłoni.


### Dla kogo przeznaczony jest ZEUS?

Obecnie ZEUS jest przeznaczony dla osób prowadzących własne [Lightning Network Daemon (LND)](https://lightning.engineering/) lub [Core Lightningning (CLN)](https://blockstream.com/lightning/) węzły domowe / biznesowe i zarządzających nimi zdalnie za pośrednictwem Zeusa.


Sprzedawcy korzystający z [BTCPay](https://btcpayserver.org/) lub [LNBits](https://lnbits.com/) lub [Alby](https://getalby.com/) (lub dowolnego innego konta LNDhub) mogą również łączyć się, używać i zarządzać swoimi węzłami / kontami z ZEUS.


[Począwszy od wersji 0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS zacznie zaspokajać potrzeby przeciętnych użytkowników, którzy chcą po prostu prostego sposobu na dokonywanie szybkich, tanich płatności Bitcoin ze swojego urządzenia mobilnego, posiadając [wbudowany mobilny węzeł Lightning](https://docs.zeusln.app/category/embedded-node) ze zintegrowanym [dostawcą usług Lightning (LSP)](https://docs.zeusln.app/lsp/intro).


### Ważne zasoby Zeusa:


- Oficjalna strona Zeusa - [https://zeusln.app/](https://zeusln.app/)
- Dokumentacja Zeusa - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [repozytorium Zeus Github](https://github.com/ZeusLN/zeus)
- [Grupa wsparcia Zeus Telegram](https://t.me/ZeusLN)
- [Zeus na NOSTR](https://iris.to/zeus@zeusln.app)
- [Zeus Blog Announcements](https://blog.zeusln.com)


### Cechy Zeusa

#### Cechy ogólne:


- Samodzielna opieka, tylko Bitcoin i Lightning Wallet
- Brak opłat manipulacyjnych, brak KYC
- W pełni otwarte oprogramowanie (APGLv3)
- Obsługa wielu węzłów / kont (można zarządzać własnymi węzłami domowymi, uruchamiać wbudowane węzły LND, łączyć się z wieloma kontami LNDhub)
- Łatwe w użyciu menu aktywności
- Szyfrowanie kodem PIN lub passphrase, tryb prywatności - ukrywanie poufnych danych
- Książka kontaktów, wiele motywów, wiele języków


#### Właściwości techniczne


- Połączenie przez Tor
- Pełna obsługa LNURL (płatność, wypłata, autoryzacja, kanał), wysyłanie na adresy Lightning
- Szczegółowe zarządzanie kanałami oświetlenia, obsługa MPP/AMP, Keysend, zarządzanie opłatami za routing
- Replace-by-fee (RBF) i wsparcie "dziecko płaci za rodzica" (CPFP)
- Płatności i żądania NFC, podpisywanie i weryfikacja wiadomości
- Obsługa SegWit i Taproot
- Proste kanały Taproot
- Samodzielne adresy błyskawiczne (@zeuspay.com)
- Punkt sprzedaży przez Square (wkrótce otwarty PoS)


### Przewodniki i samouczki wideo

Aby móc korzystać z Zeusa i zarządzać kanałami Lightning, płynnością, opłatami itp., lepiej najpierw przeczytać kilka ważnych przewodników na temat Lightning Network.


#### Przewodniki:


- [LND - Dokumentacja Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Core Lightning Documentation](https://lightning.readthedocs.io/index.html)
- [Poradnik dla początkujących](https://bitcoiner.guide/lightning/) - Bitcoin Q&A
- [Lightning Node Management](https://www.lightningnode.info/) - by openoms
- [Lightning Network i analogia lotniska](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Zarządzanie płynnością węzła Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Konserwacja węzła Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Samouczek wideo przygotowany przez BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Przewodnik po tym, jak rozpocząć korzystanie z wbudowanego węzła Zeus LN na urządzeniu mobilnym


![Image](assets/en/01.webp)


Dedykuję ten przewodnik wszystkim nowym użytkownikom Lightning Network (LN), którzy chcą rozpocząć nową, suwerenną podróż przy użyciu węzła self-custody Wallet na swoich urządzeniach mobilnych.


Weźmy pod uwagę, że przeszedłeś już przez całą tę mnogość portfeli powierniczych LN, ale nie jesteś jeszcze gotowy, aby uruchomić węzeł PUBLIC routing LN, po prostu chcesz umieścić więcej Sats na LN w bardziej samodzielny sposób i dokonywać regularnych płatności za pośrednictwem LN.


Oto Zeus, począwszy od [wersji v0.8.0 ogłoszonej na ich blogu](https://blog.zeusln.com/new-release-zeus-v0-8-0/), oferuje teraz wbudowany węzeł LND w aplikację. Do tej pory Zeus był aplikacją do zdalnego zarządzania węzłami + kontami LNDhub. Ale teraz... węzeł jest w telefonie!


![Image](assets/en/02.webp)


### Szybkie podsumowanie głównych funkcji Zeus Node:



- Prywatny węzeł LND** - Oznacza to, że ten węzeł NIE będzie publicznie przekierowywał innych płatności przez twój węzeł. Węzeł i kanały są niezapowiedziane (prywatne, niewidoczne na publicznym wykresie LN). Odbieranie i dokonywanie płatności będzie odbywać się za pośrednictwem połączonych peerów LSP. PAMIĘTAJ: Zeus Embedded Node NIE będzie wykonywał publicznego routingu!
- Trwała usługa LND** - użytkownik może aktywować tę funkcję i utrzymywać usługę LND aktywną w sposób ciągły, jak każdy zwykły węzeł LN. Aplikacja nie musi być otwarta, trwała usługa utrzyma całą komunikację online.
- Filtry blokowe Neutrino** - synchronizacja bloków odbywa się przy użyciu [filtrów blokowych i protokołu Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (bez informacji o środkach On-Chain naszych użytkowników). Przypomnienie: w przypadku dużych opóźnień / wolnych połączeń internetowych synchronizacja bloków oparta na protokole Neutrino może czasami zawieść. Próba przełączenia się na pobliski serwer neutrino może pomóc przywrócić synchronizację. Bez tej synchronizacji węzeł LND nie może zostać uruchomiony!
- Proste kanały Taproot** - Zamykając te kanały, użytkownicy ponoszą mniejsze opłaty i otrzymują większą prywatność, ponieważ wydają się jak każdy inny Taproot podczas sprawdzania ich śladu On-Chain.
- Zintegrowany LSP** - Olympus jest nowym węzłem LSP dla Zeus. Użytkownicy mogą od razu odbierać Sats przez LN, bez konieczności wcześniejszego konfigurowania kanałów LN. Wystarczy utworzyć LN Invoice i płacić z dowolnego innego LN Wallet, z usługą kanału Zeus 0-conf. Więcej o usłudze Zeus LSP można przeczytać tutaj. LSP zapewnia również dodatkową prywatność naszym użytkownikom, dostarczając im zawinięte faktury, które ukrywają klucze publiczne ich węzłów przed płatnikami.
- Książka kontaktów** - możesz zapisywać kontakty ręcznie lub importować je z NOSTR, aby łatwo wysyłać płatności do stałych miejsc docelowych.
- Pełne wsparcie dla LNURL, LN Address wysyłania i odbierania** - teraz możesz skonfigurować własny automatyczny LN Address z @zeuspay.com. Przypomnienie: Można również użyć Zeus do LN-auth na stronach, gdzie można zalogować się za pomocą uwierzytelniania LN. Jest to bardzo przydatne.
- Punkt sprzedaży** - teraz użytkownicy handlowi mogą konfigurować własne produkty i sprzedawać bezpośrednio z Zeus, ze zintegrowanym PoS. Na razie zawiera podstawowe potrzeby, ale w przyszłości będzie zawierać rozszerzone funkcje.
- Dzienniki LND** - użytkownik może odczytywać w czasie rzeczywistym dzienniki usługi LND i używać ich do debugowania możliwych problemów (głównie w przypadku złych połączeń)
- Automatyczne kopie zapasowe** - kanały węzła LN są automatycznie archiwizowane na serwerze Olympus. Ta automatyczna kopia zapasowa jest szyfrowana za pomocą Wallet seed (bez seed jest całkowicie bezużyteczna). Użytkownik może również ręcznie wyeksportować SCB (statyczną kopię zapasową kanałów) w celu odzyskania danych po awarii.


### Jak uzyskać dostęp do Zeus LN Node (LND embedded)


W tym przewodniku omówię tylko wbudowany węzeł LND, a nie inne sposoby korzystania z tej wspaniałej aplikacji (zdalne zarządzanie węzłami i konta LNDhub). Inne rodzaje połączeń można znaleźć na stronie [Zeus Docs page](https://docs.zeusln.app/category/getting-started), która jest bardzo dobrze wyjaśniona i nie ma potrzeby pisania dedykowanego przewodnika.


#### KROK 1 - KONFIGURACJA POCZĄTKOWA


Ze względu na fakt, że Zeus jest pełnym węzłem LND, będę miał kilka wstępnych zaleceń:



- Nie używaj starego urządzenia, które może wpłynąć na korzystanie z tej potężnej aplikacji. Szczególnie w okresie synchronizacji aplikacja może intensywnie wykorzystywać procesor i pamięć RAM. Ich brak może nawet uniemożliwić korzystanie z aplikacji Zeus.
- Używaj co najmniej Androida 11 jako mobilnego systemu operacyjnego i aktualizuj go tak często, jak to możliwe. W przypadku iOS to samo, spróbuj użyć znacznie wyższej wersji systemu operacyjnego.
- Będziesz potrzebował co najmniej 1 GB miejsca na dysku do przechowywania danych. Z czasem może wzrosnąć więcej, ale istnieje funkcja kompaktowania bazy danych do poziomu MB.
- Nie ma potrzeby używania Zeusa z usługą Tor lub Orbot. Nie komplikuj sprawy bardziej niż to konieczne. Tor w tym przypadku nie zapewni większej prywatności, a jedynie pogorszy początkową synchronizację. Należy również uważać na używane sieci VPN i sprawdzać opóźnienia połączenia z serwerami Neutrino. Należy pamiętać, że filtr bloków Neutrino nie wycieka ani nie śledzi tożsamości urządzenia, a jedynie serwuje bloki. Ruch LN odbywa się również za LSP z prywatnymi kanałami, więc bardzo niewiele informacji wychodzi na zewnątrz, nie ma powodu, aby bać się o prywatność.
- Należy uzbroić się w cierpliwość podczas początkowej synchronizacji, która może potrwać kilka minut. Staraj się być podłączony do szerokopasmowego połączenia internetowego z dobrym opóźnieniem. Jeśli prowadzisz własny węzeł Bitcoin, [możesz aktywować usługę neutrino](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) i podłączyć Zeusa do własnego węzła, nawet przy użyciu wewnętrznej sieci LAN, dzięki czemu uzyskasz maksymalną prędkość.


Po skonfigurowaniu typu połączenia "Węzeł wbudowany" aplikacja rozpocznie synchronizację. Poczekaj cierpliwie na zakończenie tej części, a następnie przejdź do głównej strony ustawień.


![Image](assets/en/03.webp)


Zanim zaczniesz korzystać z Zeusa, zapoznajmy się z każdą z sekcji ustawień i zrozumiemy niektóre z głównych funkcji:


**A - USTAWIENIA**


Jest to sekcja z ogólnymi ustawieniami dla całej aplikacji


**1 - Lightning Service Provider (LSP)**


Poniżej przedstawiono dwie usługi LSP:



- _Just in time channels_ - gdy nie masz żadnego otwartego kanału lub dostępnej płynności przychodzącej, jeśli usługa jest aktywna, otworzy dla ciebie kanał w locie. Opcję tę można wyłączyć, jeśli nie chcesz otwierać więcej kanałów tego typu.
- _Zamów kanały z wyprzedzeniem_ - możesz kupić kanały przychodzące od Olympus LSP bezpośrednio w aplikacji z wieloma opcjami i kwotami (dla przychodzących i wychodzących).


LSP pomaga połączyć użytkowników z Lightning Network, otwierając kanały płatności do ich węzłów. [Więcej o LSP można przeczytać tutaj](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS ma zintegrowany nowy LSP o nazwie [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), który jest dostępny dla wszystkich użytkowników korzystających z nowego wbudowanego węzła.


W tej sekcji domyślnie ustawiony jest Olympus LSP (https://0conf.lnolymp.us), ale wkrótce będzie można również ustawić inny 0conf LSP, który obsługuje ten protokół.


należy pamiętać:_

po otwarciu kanału z Olympus LSP przy użyciu zapakowanych faktur LN otrzymujesz również 100k płynności przychodzącej! Jest to naprawdę dobra opcja w przypadku konieczności natychmiastowego otrzymania większej ilości Sats

przykład: wpłacasz 400 tys. Sats, aby otworzyć kanał LSP, a następnie LSP otwiera kanał o przepustowości 500 tys. Sats w kierunku twojego węzła Zeus i przesuwa 400 tys. Sats, które wpłaciłeś na swoją stronę

"Płynność przychodząca" = więcej "miejsca" w kanale do odbioru


Mamy nadzieję, że w przyszłości będziemy mieli wiele innych LSP, które będzie można zintegrować z Zeusem i używać alternatywnie każdego z nich. To tylko kwestia czasu, aż nowe LSP przyjmą otwarty standard dla tego rodzaju kanałów 0conf.


Jeśli nie chcesz otwierać nowych kanałów "w locie", możesz wyłączyć tę opcję.


W tej samej sekcji można również wybrać opcję "żądania prostych kanałów Taproot", gdy LSP otworzy kanał w kierunku węzła Zeus. Te proste kanały Taproot oferują lepszą prywatność On-Chain i niższe opłaty za zamknięcie kanału. Są tylko dwa powody, dla których nie warto z nich korzystać:



- Są one nowe i nadal mogą występować błędy w LND podczas ich używania.
- Twój kontrahent ich nie obsługuje. Nawet węzły LND muszą na razie wyrazić na nie zgodę.


**2 - Ustawienia płatności**


Ta funkcja oferuje możliwość ustawienia własnych preferowanych opłat za płatności, przez LN lub onchain. Zapewnia również opcję zwiększenia lub zmniejszenia limitu czasu dla faktur.


Jeśli niektóre z płatności LN nie powiodą się, możesz zwiększyć opłatę, aby znaleźć lepszą trasę. Ponadto, jeśli wykonujesz onchain txs, możesz skonfigurować określoną opłatę, aby twój tx nie utknął w Mempool na długi czas, w przypadku wysokich opłat.


**3 - Ustawienia faktur**


W tej sekcji znajdują się opcje generate faktur:



- Ustawienie standardowej notatki do wyświetlenia w Invoice lub generate
- Czas wygaśnięcia w sekundach, w przypadku, gdy chcesz, aby określony czas, dłuższy lub krótszy dla Invoice został wypłacony
- Uwzględnienie wskazówek dotyczących trasy - dostarczanie informacji w celu znalezienia niereklamowanych lub prywatnych kanałów. Umożliwia to kierowanie płatności do węzłów, które nie są publicznie widoczne w sieci. Wskazówka dotycząca trasy zapewnia częściową trasę między węzłem prywatnym odbiorcy a węzłem publicznym. Ta podpowiedź routingu jest następnie uwzględniana w Invoice generowanym przez odbiorcę i dostarczanym płatnikowi. Sugeruję, aby była ona domyślnie włączona, w przeciwnym razie płatności przychodzące mogą zakończyć się niepowodzeniem (nie znaleziono trasy).
- AMP Invoice - Atomic Multi-path Payments to nowy typ płatności Lightning zaimplementowany przez LND, który pozwala na otrzymywanie Sats bez określonego Invoice, przy użyciu [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Jest to praktycznie statyczny kod płatności. [Więcej informacji tutaj](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Pokaż niestandardowe pole obrazu wstępnego - używaj tej opcji tylko w bardzo szczególnych przypadkach, gdy naprawdę chcesz użyć niestandardowych pól w obrazie wstępnym. [Więcej informacji tutaj](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Inną opcją w tej sekcji jest ustawienie typu łańcucha Address, którego chcesz użyć: SegWit zagnieżdżony, SegWit, Taproot.


![Image](assets/en/04.webp)


Kliknij górny przycisk kółka, a pojawi się wyskakujący ekran, aby wybrać żądany typ Address. Po ustawieniu tego, następnym razem, gdy naciśniesz przycisk odbioru dla onchain, generate wybierze typ Address. Można go zmienić w dowolnym momencie.


**4 - Ustawienia kanałów**


W tej sekcji można wstępnie ustawić niektóre funkcje kanałów otwierających, takie jak:



- liczba potwierdzeń
- Ogłaszaj kanał (domyślnie wyłączony), co oznacza, że będą to kanały niezapowiedziane
- Proste kanały Taproot
- Pokaż przycisk zakupu kanału


**5 - Ustawienia prywatności**


Tutaj znajdziesz kilka podstawowych ustawień, aby dodać więcej prywatności za pomocą aplikacji Zeus:



- Block explorer, aby otworzyć szczegóły tx (Mempool.space, blockstream.info lub niestandardowy osobisty)
- Czytaj schowek - przełącznik włączania/wyłączania, jeśli chcesz, aby Zeus odczytywał schowek urządzenia
- Tryb Lurker - przełącznik on/off, jeśli chcesz ukryć określone poufne informacje z aplikacji Zeus. Jest to dobra opcja do tworzenia demonstracji lub zrzutów ekranu.
- Sugestia opłaty Mempool - aktywuj tę opcję, jeśli chcesz korzystać z zalecanych poziomów opłat z [Mempool.space](https://Mempool.space/)


**6 - Bezpieczeństwo**


Ta sekcja ma tylko dwie opcje zabezpieczenia aplikacji podczas otwierania: ustawienie hasła lub kodu PIN.


Po ustawieniu kodu PIN do otwierania aplikacji można również ustawić "kod PIN pod przymusem". Ten tajny dodatkowy kod PIN będzie używany TYLKO w sytuacji przymusu, jeśli jesteś zagrożony. Jeśli wprowadzisz ten kod PIN, cała konfiguracja zostanie wymazana. Lepiej więc aktualizować kopie zapasowe. Automatyczne kopie zapasowe są domyślnie włączone, ale dobrze jest mieć również własne kopie zapasowe poza urządzeniem.


**7 - Waluta**


Włącz lub wyłącz opcję wyświetlania konwersji walut fiducjarnych w aplikacji Zeus. Obecnie obsługuje ponad 30 światowych walut fiducjarnych.


**8 - Język**


Możesz przełączać się między wieloma językami tłumaczeń, sprawdzonymi przez społeczność Zeus z native speakerami.


**9 - Wyświetlacz**


W tej sekcji można spersonalizować wyświetlacz Zeusa, wybierając różne motywy kolorystyczne, domyślny ekran (klawiatura lub balans), wyświetlać alias węzła, aktywować duże przyciski klawiatury, wyświetlać więcej miejsc dziesiętnych.


**10 - Punkt sprzedaży**


Jest to specjalna funkcja umożliwiająca włączanie/wyłączanie zintegrowanego systemu PoS w Zeus. Można uruchomić samodzielny system PoS lub połączyć go z systemem Square PoS. Obecnie obsługuje podstawowe funkcje jako PoS, ale wystarczy na dobry początek i może pomóc tym małym sprzedawcom (bary / restauracje, sklepy spożywcze) w rozpoczęciu przyjmowania BTC w natywny sposób.


Wewnątrz tych ustawień znajdziesz różne opcje konfiguracji PoS:



- Typ płatności potwierdzającej: Tylko LN, 0-conf, 1-conf
- Włączanie/wyłączanie napiwków dla pracowników obsługujących PoS
- Pokaż / ukryj klawiaturę
- Procent podatku do zastosowania na bilecie
- Tworzenie produktów i kategorii produktów
- Prosta lista wszystkich sprzedaży


Oto film demonstracyjny na żywo, jak korzystać z Zeus PoS:


**B - Kopia zapasowa Wallet**


Wbudowany węzeł w ZEUS jest oparty na LND i wykorzystuje [aezeed seed format](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Różni się on od typowego formatu [BIP39](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki), który można zobaczyć w większości portfeli Bitcoin, choć może wydawać się podobny. Aezeed zawiera dodatkowe dane, w tym datę urodzenia Wallet, które pomogą w bardziej efektywnym ponownym skanowaniu podczas odzyskiwania.


Format klucza aezeed powinien być kompatybilny z następującymi portfelami mobilnymi: Blixt, BlueWallet i Breez. Należy pamiętać, że sam seed będzie niewystarczający do odzyskania wszystkich sald, jeśli masz otwarte lub oczekujące na zamknięcie kanały!


Więcej informacji na temat procesu tworzenia kopii zapasowych i przywracania można znaleźć na stronie [Zeus Docs page](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


POWER ADVICE: Zapisując seed, zapisz również pubkey węzła! Czasami dobrze jest mieć go pod ręką, razem z seed i SCB (Static Channels Backup) na wypadek konieczności weryfikacji odzyskiwania.


SCB jest konieczny tylko wtedy, gdy masz otwarte kanały LN. W przypadku posiadania tylko środków onchain, nie jest konieczne.


Jeśli zauważysz, że po długim czasie nadal nie wyświetla starej historii txs, przejdź do Embedded node - Peers i wyłącz opcję korzystania z listy wybranych peerów (domyślnie jest to btcd.lnolymp.us). Spowoduje to ponowne uruchomienie i połączenie z pierwszym dostępnym węzłem neutrino z lepszym czasem odpowiedzi. Lub użyj innych dobrze znanych peerów neutrino wymienionych poniżej.


Jeśli chcesz zobaczyć więcej opcji odzyskiwania dla węzła LND, [przeczytaj mój poprzedni przewodnik] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), w którym znajdziesz kroki, jak zaimportować zamrożony seed do Sparrow Wallet lub inne metody.


**C - Węzeł wbudowany**


W tej sekcji znajdziemy kilka podstawowych narzędzi do zarządzania zintegrowanym węzłem:



- _Disaster Recovery_ - Automatyczne i ręczne tworzenie kopii zapasowych dla kanałów LN. Więcej informacji na temat korzystania z tej funkcji można znaleźć na stronie Zeus Docs.
- _Express Graph Sync_ - aplikacja Zeus pobierze wykres danych plotek LN z dedykowanego serwera, aby zapewnić szybszą i lepszą synchronizację, oferując najlepsze ścieżki płatności. Można również wyczyścić poprzednie dane wykresu podczas uruchamiania.
- _Peers_ - sekcja do zarządzania urządzeniami równorzędnymi neutrino i 0-conf. Jeśli masz problemy z początkową synchronizacją, kanały nie pojawiają się online, to dlatego, że twoje urządzenie ma duże opóźnienia ze skonfigurowanym peerem neutrino. Spróbuj przełączyć listę preferowanych serwerów równorzędnych lub dodaj konkretny serwer równorzędny, o którym wiesz, że ma lepsze opóźnienie synchronizacji. Dobrze znane serwery neutrino to:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - dla regionu USA
 - sg.lnolymp.us - dla regionu Azji
 - btcd-Mainnet.lightning.computer - dla regionu USA
 - uswest.blixtwallet.com (Seattle) - dla regionu USA
 - europe.blixtwallet.com (Niemcy) - dla regionu UE
 - asia.blixtwallet.com - dla regionu Azji
 - node.eldamar.icu - dla regionu USA
 - noad.sathoarder.com - dla regionu USA
 - bb1.breez.technology | bb2.breez.technology - dla regionu USA
 - neutrino.shock.network - region USA



- _LND logs_ - bardzo przydatne narzędzie do debugowania problemów z węzłem LN i dogłębnej kontroli tego, co dzieje się na bardziej technicznym poziomie.
- _Ustawienia zaawansowane_ - więcej narzędzi do kontrolowania korzystania z węzła LND:



 - _Pathfinding mode_ - bimodal lub apriori, sposoby na znalezienie lepszej trasy dla płatności LN, a także resetowanie poprzednich informacji o routingu. Zapoznaj się z tymi bardzo dobrymi przewodnikami na temat wyszukiwania ścieżek: [Pathfinding](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - autorstwa Docs Lightning Engineering i [LN Payment Pathfinding](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - autorstwa Voltage
 - _Persistent LND_ - aktywuj ten tryb, jeśli chcesz, aby usługa LND działała nieprzerwanie w tle i utrzymywała węzeł online 24/7. Jest to bardzo przydatne, jeśli używasz Zeusa jako PoS w małym sklepie lub otrzymujesz wiele wskazówek LN przez LN Address.
 - _Rescan wallet_ - ta opcja uruchomi przy ponownym uruchomieniu pełne skanowanie wszystkich onchain tx twojego Wallet. Aktywuj ją tylko w przypadku braku niektórych tx w Wallet. Zadanie ponownego skanowania zajmie trochę czasu, kilka minut, więc bądź cierpliwy i zawsze sprawdzaj dzienniki, aby zobaczyć więcej szczegółów na temat postępu.
 - _Compact Database_ - ta opcja jest bardzo przydatna, jeśli aplikacja Zeus zajmuje dużo miejsca na urządzeniu (zobacz szczegóły aplikacji w ustawieniach urządzenia). W przypadku dużej aktywności aplikacji Zeus zalecałbym częstsze wykonywanie tej operacji. Gdy zobaczysz, że masz więcej niż 1-1,5 GB danych dla aplikacji Zeus, wykonaj kompresję. Zrestartuje się i zajmie trochę czasu, więc bądź cierpliwy.
 - _Delete Neutrino files_ - ta opcja usuwania plików neutrino (po ponownym uruchomieniu) znacznie zmniejszy zużycie pamięci masowej. Zmniejszenie zużycia danych ma również duży wpływ na zużycie baterii, zwłaszcza jeśli używasz Zeusa w trybie trwałym.


**D - Informacje o węźle**


W tej sekcji można znaleźć więcej szczegółów na temat stanu węzła Zeus:



- Alias - krótki identyfikator węzła
- Klucz publiczny - pełny klucz publiczny węzła wymagany przez inne węzły do znalezienia ścieżki do węzła. Pamiętaj, że ten klucz publiczny NIE jest widoczny na zwykłych eksploratorach LN (Mempool, Amboss, 1ML itp.). Ten klucz publiczny jest dostępny TYLKO za pośrednictwem połączonych urządzeń równorzędnych i kanałów LN.
- Wersja implementacji LN
- Wersja aplikacji Zeus
- Synced to chain i Synced to graph status - bardzo ważne, pokazujące prawidłowy status węzła. Jeśli te dwa elementy nie wyświetlają wartości "true", oznacza to, że węzeł nadal się synchronizuje lub ma pewne problemy z synchronizacją. Sugeruje się więc zajrzenie do dzienników LND lub poczekanie trochę dłużej.
- Wysokość bloku i Hash - pokazuje ostatni blok i Hash, które węzeł widział i zsynchronizował.


**E - Informacje o sieci**


Ta sekcja wyświetla więcej szczegółów na temat ogólnego stanu Lightning Network, wyodrębnionych z danych synchronizacji wykresu: liczba dostępnych kanałów publicznych, liczba węzłów, liczba kanałów zombie (offline lub martwych), średnica wykresu, średni i maksymalny stopień dla wykresu.


Te dane informacyjne mogą być przydatne do debugowania lub po prostu wykorzystywane do statystyk.


**F - Lightning Address**


W tej sekcji użytkownik może skonfigurować własny depozyt LN Address @zeuspay.com.


ZEUS PAY wykorzystuje generowane przez użytkowników hashe preimage, faktury HODL i schemat poświadczania Zaplocker Nostr, aby umożliwić użytkownikom, którzy mogą nie być online 24/7, otrzymywanie płatności na statyczną błyskawicę Address. Użytkownicy muszą jedynie zalogować się do swoich portfeli ZEUS w ciągu 24 godzin, aby odebrać płatności, w przeciwnym razie zostaną one zwrócone do nadawcy.


Jeśli aktywujesz "tryb stały", wszystkie płatności do LN Address będą natychmiast odbierane.


Dowiedz się, jak działają płatności [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) i więcej o opłatach [ZeusPay tutaj](https://docs.zeusln.app/lightning-Address/fees).


**G - Adresy Onchain**


W tej sekcji można sprawdzić wygenerowane adresy onchain w celu lepszej kontroli monet


**H - Kontakty**


W Zeus v 0.8.0 wprowadzono nową książkę kontaktów, której można używać do szybkiego wysyłania płatności do znajomych i rodziny, również z możliwością importowania kontaktów z Nostr.


Wystarczy wprowadzić swój numer NIP-05 Address w formacie Nostr npub lub czytelnym dla człowieka, a ZEUS wyszuka w Nostr wszystkie kontakty. Stamtąd można wysłać szybką płatność do kontaktu lub zaimportować wszystkie lub wybrane kontakty do lokalnej książki kontaktów


Oto krótki film instruktażowy, jak skonfigurować i używać kontaktów Zeus:


**I - Narzędzia**


Tutaj mamy różne podsekcje z większą liczbą narzędzi:



- _Accounts_ - tutaj można zaimportować zewnętrzne konta / portfele, portfele Cold, portfele Hot, aby kontrolować lub używać ich jako zewnętrznego źródła finansowania kanałów węzła Zeus. Ta funkcja jest wciąż eksperymentalna.
- _Przyspiesz transakcję_ - Ta funkcja może być pomocna, gdy masz zablokowany tx do Mempool i chcesz podnieść opłatę. Będziesz musiał podać dane wyjściowe tx ze szczegółów tx i wybrać żądaną nową opłatę, której chcesz użyć. Musi być wyższa niż poprzednia i wymagać większej ilości środków dostępnych w łańcuchu Wallet.


![Image](assets/en/05.webp)


Musisz przejść do oczekującego zlecenia i skopiować punkt txid. Następnie przejdź do tej sekcji i wklej go, a następnie wybierz nową opłatę, której chcesz użyć, aby go podbić. Pojawi się nowy ekran z zalecanymi opłatami w tym momencie lub możesz ustawić niestandardową. Pamiętaj, że MUSI być wyższa niż poprzednia.


Zawsze lepiej jest trzymać UTXO z maksymalnie 100k Sats w swoim Zeus onchain Wallet, aby móc go użyć do podbijania opłat, gdy jest to konieczne.



- _Podpisz lub zweryfikuj_ - Dzięki tej funkcji można podpisać określoną wiadomość za pomocą kluczy Wallet. Może być również użyty do weryfikacji wiadomości, aby udowodnić, że pochodzi z określonych kluczy Wallet.
- _Currency converter_ - proste narzędzie do obliczania konwersji kursu między BTC a innymi walutami fiducjarnymi.


**J - Merch and Support**


Tutaj znajdziesz więcej informacji i linków na temat Zeusa, sklepu internetowego, sponsorów, mediów społecznościowych.


**K - Pomoc**


W tej ostatniej sekcji znajdziesz linki do strony z dokumentacją Zeusa, Github issues (jeśli chcesz opublikować błąd lub prośbę bezpośrednio do twórców aplikacji), e-mail wsparcia.



### KROK 2 - ROZPOCZĘCIE KORZYSTANIA Z WĘZŁA ZEUS



Pamiętaj, że Zeus ma być używany głównie jako LN Wallet, do łatwych i szybkich płatności przez LN. Oczywiście, zawiera również onchain Wallet, ale ten powinien być używany wyłącznie do otwierania / zamykania kanałów LN, a nie do regularnych płatności za kawę.


Przeczytaj mój inny poradnik na temat [jak być swoim własnym bankiem przy użyciu 3 poziomów Stash] (https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


W tym momencie użytkownik ma 2 sposoby na rozpoczęcie korzystania z Zeus:



- Od razu przez LN, używając kanału 0-conf z Olympus LSP
- Wpłać najpierw w onchain Wallet, a następnie otwórz normalny kanał LN z wybranym peerem.


#### Metoda A - Korzystanie z usługi Olympus LSP


Jest to bardzo łatwy i prosty sposób na wprowadzenie nowego użytkownika LN do Zeus. Może to być zupełnie nowy użytkownik Bitcoin, który nie ma żadnego Sats, wprowadzony przez znajomego lub nowy sprzedawca rozpoczynający swoją pierwszą płatność LN.


Domyślnie Zeus będzie korzystał z własnego LSP, Olympus. Ale później można przełączyć się również na inne LSP, które obsługują ten protokół 0-conf do otwierania kanałów.


Po prostu tworząc Invoice na swoim Zeusie (wpisz kwotę i kliknij przycisk "żądanie"), będziesz mógł od razu otrzymać te Sats.


Invoice generate zostanie [zawinięty](https://docs.zeusln.app/lsp/wrapped-invoices) i zostaną przedstawione opłaty związane z usługą, jeśli zostaną uiszczone. Ten zawinięty Invoice zawiera wskazówki dotyczące trasy do węzła Zeus, więc LSP może znaleźć nowy węzeł i otworzyć kanał z nowymi środkami, które wpłacasz.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Aby uzyskać kanał LN od LSP ze środkami, które chcesz otrzymać za pierwszym razem, ten Invoice musi zostać opłacony z innego LN Wallet i poczekać kilka chwil, aż LSP otworzy kanał w kierunku węzła Zeus, odliczy opłatę i przepchnie pozostałą kwotę płatności po twojej stronie kanału.


Wszystko, co musisz zrobić, to zapłacić Invoice wygenerowany dla ciebie w ZEUS z innym piorunem Wallet, a twój kanał zostanie natychmiast otwarty. [Prosimy o zapoznanie się z opłatami Zeus LSP](https://docs.zeusln.app/lsp/fees).


Kolejną korzyścią z płacenia za kanał jest routing bez opłat. Oznacza to, że podczas przekierowywania płatności pierwszy przeskok przez OLYMPUS by ZEUS nie wiąże się z żadnymi opłatami za przekierowanie. Należy pamiętać, że przeskoki poza OLYMPUS by ZEUS nadal będą obciążać użytkownika.


Gdy kanał jest gotowy, kliknij prawy przycisk u dołu ekranu, który wyświetla kanały Zeus.


![Image](assets/en/08.webp)


Zobaczysz taki kanał, pokazujący twoją stronę równowagi kanału:


![Image](assets/en/09.webp)


Jeśli wydasz więcej z tego kanału, będziesz mieć więcej płynności przychodzącej. Im więcej Sats otrzymasz w tym kanale, tym mniejszą płynnością przychodzącą będziesz dysponować.


Oto prosta demonstracja wizualna (autorstwa Rene Pickhardta) dotycząca działania kanałów LN:


W tym momencie, biorąc pod uwagę ekran demonstracyjny kanałów, kliknij nazwę kanału, a zobaczysz więcej szczegółów na jego temat.


Masz pojedynczy kanał z Olympus, o łącznej pojemności 490 000 Sats, z saldem 378 tys. Sats po twojej stronie i 88 tys. Sats po stronie Olympus. Oznacza to, że możesz otrzymać maksymalnie 88 tys. Sats więcej na tym samym kanale.


Jeśli chcesz otrzymać więcej niż 88 tys. Sats (dostępna płynność przychodząca w tym przypadku), powiedzmy kolejne 500 tys. Sats, po prostu tworząc nowy LN Invoice z tą ilością, uruchomi nowe żądanie kanału do Olympus LSP. Otrzymasz więc drugi kanał.


Dlatego, aby uniknąć płacenia większych opłat za otwarcie wielu kanałów, zaleca się otwarcie najpierw większego kanału, powiedzmy 1-2 mln Sats. Po otwarciu można wymienić część Sats, powiedzmy 50%, na onchain, korzystając z dowolnej zewnętrznej usługi wymiany opisanej w tym przewodniku.


Po wymianie z tego kanału, powiedzmy 50% i przywróceniu Sats do własnego Zeus onchain Wallet, jesteś gotowy, aby przejść do następnej metody otwierania nowego kanału - z równowagi onchain.


#### Metoda B - Korzystanie z salda onchain


Dzięki tej metodzie można otworzyć kanały do dowolnego innego węzła LN, w tym tego samego LSP Olympus. Ale jeśli masz już kanał z Olympus, zaleca się, aby mieć również z innym węzłem, dla większej niezawodności, a także może korzystać z MPP (płatności wieloczęściowe).


![Image](assets/en/10.webp)


Powyżej znajduje się przykład płatności LN Invoice przy użyciu MPP. Jak widać, w dolnej części ekranu znajduje się opcja "Ustawienia", która otwiera rozwijaną stronę z bardziej szczegółowymi informacjami na temat płatności, której zamierzasz dokonać. Na tym ekranie, jeśli masz otwarte co najmniej 2 kanały, funkcja MPP będzie domyślnie włączona. Możesz także aktywować AMP (atomic multi-path) i ustawić określone części, które chcesz. To potężna funkcja!


W przypadku prywatnego węzła, takiego jak Zeus, zalecałbym posiadanie 2-3 dobrych kanałów (maks. 4-5), z dobrymi LSP i dobrą płynnością, aby zaspokoić wszystkie potrzeby związane z płaceniem lub otrzymywaniem Sats przez LN. [Zobacz więcej porad dotyczących płynności węzła LN w tym przewodniku](/nodes/managing-lightning-node-liquidity-pl.html). Również tutaj inny [ogólny przewodnik o płynności LN](https://Bitcoin.design/guide/how-it-works/liquidity/) od zespołu projektowego Bitcoin.


Wiem, że wybór odpowiednich węzłów peer nie jest łatwym zadaniem, nawet dla doświadczonych użytkowników. [Podam więc kilka opcji na początek](https://github.com/ZeusLN/zeus/discussions/2265), są to węzły peer, które sam przetestowałem przy użyciu Zeusa (starałem się łączyć tylko z węzłami LND, aby uniknąć problemów z niekompatybilnością)


Tutaj znajduje się również lista potwierdzonych węzłów równorzędnych dla Zeusa. Jeśli znasz dobre węzły, możesz dodać je do tej listy.


Kanał można otworzyć w aplikacji Zeus, przechodząc do widoku kanałów, klikając ikonę kanału w prawym dolnym rogu widoku głównego, a następnie naciskając ikonę + w prawym górnym rogu.


![Image](assets/en/11.webp)


Jeśli chcesz otworzyć kanał z określonym węzłem, kliknij (A) w górnym rogu, aby zeskanować QR nodeID węzła (w Mempool, Amboss, 1ML możesz uzyskać ten QR), a wszystkie szczegóły peera zostaną wypełnione.


PRZYPOMNIENIE:


- Węzeł wbudowany Zeus nie korzysta z usługi Tor! Więc nie próbuj otwierać kanałów z węzłami, które są pod Torem! Wyrządzacie sobie więcej szkody niż dodajecie więcej prywatności. Tor dla LN nie oferuje większej prywatności, ale dodaje więcej kłopotów.
- wybieraj mądrze swoich peerów, lepiej być dobrymi LSP, dobrymi węzłami routingu, a nie przypadkowymi węzłami pleb, które mogą zamknąć twoje kanały i nie mogą zaoferować dobrej płynności. [Tutaj napisałem dedykowany przewodnik](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) na temat płynności i przykładów węzłów.


Bezpośrednie kliknięcie przycisku "Open Channel to Olympus" spowoduje wypełnienie pól wymaganych do otwarcia kanału do [OLYMPUS by ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


W przeciwieństwie do płatnych kanałów LSP, Twój kanał będzie wymagał potwierdzenia On-Chain przy użyciu środków onchain (możesz wybrać z UTXO w widoku otwartego kanału); nie otworzy się natychmiast. Sprawdź najpierw rzeczywiste opłaty Mempool i dostosuj je odpowiednio, w zależności od tego, jak szybko chcesz otworzyć ten kanał.


Przed naciśnięciem przycisku, aby otworzyć kanał, przesuń w dół opcje zaawansowane:


![Image](assets/en/12.webp)


Należy również upewnić się, że kanał jest niezapowiedziany (prywatny). Domyślnie opcja ta jest wyłączona dla kanałów ogłoszonych. Nie zaleca się aktywowania tej opcji dla wbudowanego węzła Zeus, jest ona przydatna tylko wtedy, gdy Zeus jest używany z węzłem zdalnym, jako publiczny węzeł routingu.


W przeciwieństwie do płatnych kanałów LSP, otwierając kanały za pomocą tej metody, nie skorzystasz z routingu bez opłat.


I gotowe, wystarczy kliknąć przycisk "Open Channel", poczekać na potwierdzenie tx przez górników. Po otwarciu kanału możesz dokonywać dowolnych transakcji za pomocą Sats ze swoich kanałów.


Pamiętaj, że te kanały będą miały całe saldo po TWOJEJ stronie, więc nie będziesz mieć płynności przychodzącej. Jak wspomniałem wcześniej, wymień lub wydaj trochę Sats na zakup rzeczy w LN, aby "zrobić więcej miejsca" na odbiór.


Pomyśl o swoich kanałach LN jak o szklance wody. Wlewasz trochę wody (Sats) do pustej szklanki (swojego kanału), aż ją napełnisz. Nie możesz nalać więcej wody, dopóki jej nie wypijesz (wydasz/wymienisz). Gdy szklanka jest prawie pusta, wlej do niej więcej wody (Sats), korzystając z usługi swap in. [Przeczytaj więcej o zewnętrznych usługach wymiany tutaj](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Istnieją również inne usługi LSP, takie jak sprzedaż kanałów przychodzących: LNBig lub Bitrefill. Myślę, że jest więcej takich usług, ale nie pamiętam ich w tej chwili.


Jeśli więc potrzebujesz praktycznie pustego kanału LN (saldo jest w 100% po stronie peera od samego początku), aby otrzymywać więcej płatności, niż możesz obsłużyć na istniejących zapełnionych kanałach, może to być bardzo dobra opcja. Zapłacisz określoną opłatę za otwarcie tych kanałów i otrzymasz dużo przestrzeni przychodzącej.



## PORADY I WSKAZÓWKI


### Limity rezerw przychodzących


Obecnie, ze względu na pewne ograniczenia kodu LN, nie jest możliwe otrzymanie dokładnie takiej kwoty, jaka jest wyświetlana w polu "Przychodzące". Zawsze pamiętaj, że powinieneś wystawiać faktury z nieco mniejszą kwotą, odpowiednio kwotą "Lokalnej rezerwy kanału".


![Image](assets/en/13.webp)


Jak widać na powyższym obrazku, "przychodzące" wyświetla, że nadal mogę odebrać 5101 Sats, ale w rzeczywistości w tym momencie nie można odebrać więcej. I można zaobserwować, że jest to taka sama kwota jak "Lokalna rezerwa".


Należy więc pamiętać, że wystawiając faktury do otrzymania, należy również przyjrzeć się płynności swoich kanałów i odjąć od tej kwoty lokalną rezerwę, jeśli chce się przekroczyć limit należności.


### Szybka rada dla nowych użytkowników rozpoczynających pracę z węzłem Zeus:



- Prawidłowo wykorzystaj nowe kanały.


Na przykład, jeśli wiesz, że otrzymasz w ciągu tygodnia powiedzmy 1 mln Sats, otwórz kanał 2 mln Sats i wymień na onchain Wallet lub na inne (tymczasowe) konto powiernicze LN 50-60% swojej płynności wychodzącej. Zawsze bądź przygotowany na większą płynność. Gdy będziesz potrzebować więcej płynności z powrotem w swoich kanałach Zeus, możesz przenieść ją z powrotem z kont powierniczych.


Jeśli wiesz, że będziesz wysyłać powiedzmy 500 tys. Sats tygodniowo, otwórz kanał 1 mln Sats. W ten sposób nadal będziesz mieć rezerwę, dopóki jej nie zapełnisz.



- Jeśli jesteś sprzedawcą i zawsze będziesz otrzymywać więcej niż regularnie wydajesz, kup dedykowany kanał przychodzący. To najtańszy sposób. Płacisz minimalną opłatę i otrzymujesz "pusty" kanał.



- Nie otwieraj małych bezsensownych kanałów 50-100-300-500k Sats. Zapełnisz je w ciągu kilku dni, nawet jeśli używasz ich tylko do zapów. Otwieraj większe i różne, NIE tylko jeden kanał.


Po otwarciu większego kanału zawsze można użyć zewnętrznych swapów podwodnych, aby przenieść Sats do portfeli onchain (w tym z powrotem do Zeus onchain). Utrzymanie równowagi między płynnością przychodzącą i wychodzącą jest dobre, a także można "ponownie wykorzystać" te Sats, aby otworzyć więcej kanałów, jeśli chcesz.


### Owinięty Invoice


Jeśli chcesz dodać więcej prywatności podczas odbioru, możesz użyć metody "wrapped Invoice". Przypomnienie: aby móc to zrobić, potrzebujesz kanału z Olympus LSP. Zawinięte faktury "ukryją" ostateczne miejsce docelowe (węzeł Zeus) i wyświetlą węzeł LSP jako miejsce docelowe dla płatnika.


Aby otrzymać zafoliowany Invoice, przejdź do głównego ekranu klawiatury, wprowadź kwotę i naciśnij żądanie. Zostanie wyświetlony normalny kod QR dla Invoice. Teraz kliknij prawy górny przycisk "X", a zostaniesz przekierowany do większej liczby opcji dla Invoice.


![Image](assets/en/14.webp)


Teraz musisz aktywować opcję na górze "Włącz LSP" i nacisnąć przycisk "Utwórz Invoice". Ta opcja utworzy zapakowany Invoice i pamiętaj, że pobierze niewielką opłatę.


### Faktury z podpowiedziami tras


Jest to bardzo przydatna funkcja, jeśli chcesz zarządzać płynnością wielu kanałów przychodzących. Praktycznie można wskazać, do którego kanału przychodzącego ma trafić Sats z Invoice.


Ta funkcja może być również używana do rebalansowania kołowego, gdy chcesz przenieść płynność z jednego wypełnionego kanału do innego wyczerpanego.


Jak utworzyć Invoice z podpowiedziami trasy?



- Na ekranie głównym przesuń w prawo szufladę LN i kliknij "Odbierz"
- W konfiguracji Invoice przejdź do dolnej części i aktywuj przycisk "Wstaw wskazówki dotyczące trasy", a następnie wybierz zakładkę "Niestandardowe". Otworzy się ekran ze wszystkimi dostępnymi kanałami. Wybierz ten, który chcesz odbierać.
- Wypełnij wszystkie pozostałe dane Invoice, kwotę, notatkę itp. i kliknij "Utwórz Invoice".
- Opłacenie Invoice spowoduje przeniesienie Sats na wskazany kanał.


Jeśli chcesz zapłacić sobie ten Invoice (równoważenie kołowe), gdy płacisz go z tego samego węzła Zeus, na ekranie płatności wybierz kanał wychodzący (ten z większą płynnością), którego chcesz użyć do wysłania płatności.


### Płać za pomocą Keysend


Keysend to bardzo niedoceniana funkcja LN, z której użytkownicy powinni korzystać częściej.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) pozwala użytkownikom Lightning Network na wysyłanie płatności do innych, bezpośrednio na ich klucz publiczny, o ile ich węzeł ma kanały publiczne i ma włączony keysend. Keysend nie wymaga od odbiorcy płatności wydania Invoice.


Jak więc można to zrobić z Zeusem?


Wystarczy zeskanować lub skopiować identyfikator węzła docelowego (lub użyć kontaktów Zeus, aby zapisać zwykłe węzły docelowe jako kontakty), a następnie na głównym ekranie Zeus kliknąć przycisk "Wyślij". Na tym ekranie wklej identyfikator węzła lub wybierz go z kontaktów.


Wpisz kwotę Sats, wiadomość, jeśli jest to konieczne (tak, możesz go również użyć jako tajnego czatu przez LN) i kliknij przycisk "Wyślij". Gotowe!


![Image](assets/en/15.webp)


Jeśli masz bezpośredni kanał z docelowym peerem, nie będzie żadnych opłat.


Jeśli nie masz bezpośredniego kanału z peerem docelowym, wówczas płatność keysend będzie uiszczać opłaty jako normalna płatność LN Invoice, kierowana po ścieżce regulacyjnej jak każda inna płatność. Pamiętaj tylko, że nie pozostanie po niej żaden ślad jako LN Invoice.


## Konluzja


Zalecam zapoznanie się z przewodnikiem [Advanced usage of Zeus] (https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) zawierającym więcej instrukcji i przypadków użycia.


I... to wszystko! Od teraz możesz po prostu używać Zeus Node jako zwykłego BTC/LN Wallet na swoim telefonie komórkowym. Interfejs użytkownika jest dość prosty i łatwy w użyciu, intuicyjny dla każdego typu użytkownika, nie sądzę, żebym musiał wprowadzać więcej szczegółów na temat dokonywania i otrzymywania płatności.


Podsumowując, oto tabela porównawcza prywatności:


![Image](assets/en/16.webp)