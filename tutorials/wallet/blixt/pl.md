---
name: Blixt

description: Mobilny LN Węzeł Wallet
---

![presentation](assets/blixt_intro_en.webp)


## Potężny węzeł BTC/Lightning w kieszeni, gdziekolwiek jesteś


Chciałbym przedstawić interesujący i potężny nowy węzeł mobilny BTC/LN i Wallet - Blixt. Nazwa pochodzi z języka szwedzkiego i oznacza "błyskawicę".

Jeśli nigdy nie korzystałeś z Bitcoin Lightning Network, zanim zaczniesz, przeczytaj [tę prostą analogię wyjaśniającą Lightning Network (LN)] (https://darthcoin.substack.com/p/the-lightning-network-and-the-airport).


## WAŻNE ASPEKTY:


### 1. Blixt jest węzłem prywatnym, a NIE węzłem routingu! Należy o tym pamiętać.


Oznacza to, że wszystkie kanały LN w Blixt będą niezapowiedziane na wykresie LN (tzw. kanały prywatne). Oznacza to, że TEN WĘZEŁ NIE BĘDZIE ROBIŁ ROUTINGU innych płatności przez węzeł Blixt. [Więcej o kanałach prywatnych i publicznych można przeczytać tutaj](https://voltage.cloud/blog/lightning-network-faq/what-are-the-differences-between-public-and-private-channels/).


Mobilny węzeł Blixt NIE służy do routingu, powtarzam. Służy głównie do zarządzania własnymi kanałami LN i dokonywania płatności LN prywatnie, kiedy tylko zajdzie taka potrzeba.


Węzeł mobilny Blixt musi być online i zsynchronizowany TYLKO PRZED dokonaniem transakcji. Dlatego na górze pojawi się ikona wskazująca status synchronizacji. Zajmuje to tylko kilka chwil, w zależności od tego, ile czasu pozostawałeś offline i ponownie zsynchronizowałeś wykres LN.


### 2. Blixt używa LND (aezeed) jako backendu Wallet, więc nie próbuj importować do niego innych typów portfeli Bitcoin.


[Tutaj wyjaśniono rodzaje portfeli](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). Więc jeśli wcześniej miałeś węzeł LND, możesz zaimportować seed i backup.channels do Blixt, [jak wyjaśniono w tym przewodniku](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario).


### 3. Następne ważne linki (prosimy o dodanie ich do zakładek):



- [Blixt Github repository](https://github.com/hsjoberg/blixt-Wallet) | [Github Releases](https://github.com/hsjoberg/blixt-Wallet/releases) (pobierz bezpośrednio plik apk)
- [Strona funkcji Blixt](https://blixtwallet.github.io/features) - wyjaśniająca po kolei każdą funkcję i funkcjonalność.
- [Blixt FAQ page](https://blixtwallet.github.io/faq) - Lista pytań i odpowiedzi oraz rozwiązywanie problemów z Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - wersje demonstracyjne, samouczki wideo, dodatkowe przewodniki i przypadki użycia dla Blixt
- [Ulotka A4 do wydrukowania](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer) z pierwszymi krokami przy użyciu Blixt, w różnych językach.
- Blixt oferuje również w pełni funkcjonalne demo bezpośrednio na [swojej stronie internetowej] (https://blixtwallet.com) lub na dedykowanej [wersji internetowej] (https://blixt-Wallet-git-master-hsjoberg.vercel.app/), aby mieć pełne doświadczenie w testowaniu, przed rozpoczęciem korzystania z Blixt w prawdziwym świecie.
- [Strona crowdfundingowa Geyser](https://geyser.fund/project/blixt) - przekaż Sats, jak chcesz, aby wesprzeć projekt
- [Grupa wsparcia Telegram](https://t.me/blixtwallet)


# Dostępne kluczowe funkcje


## Węzeł Neutrino


Blixt domyślnie łączy się z serwerem Blixt w celu synchronizacji bloków i indeksu z Neutrino (tryb SPV dla uproszczonej weryfikacji płatności), ale użytkownik może również połączyć się z własnym węzłem. Zaskakujące jest to, że synchronizacja węzła SPV zajmuje mniej niż 5 minut, w moim przypadku na Androidzie 11, aby być gotowym do użycia Full node Wallet (On-Chain i LN).


## Kompletny węzeł bez opieki


Użytkownik może zarządzać własnymi kanałami za pomocą łatwego w użyciu Interface i z wystarczającą ilością wyświetlanych informacji, aby mieć dobre wrażenia. W lewym górnym menu szuflady można przejść do kanałów Lightning, aby rozpocząć otwieranie z innymi węzłami, jak chcesz. Nie zapomnij włączyć Tora w ustawieniach. Jest to o wiele lepsze dla prywatności, a także dlatego, że jako węzeł mobilny, jeśli często zmieniasz połączenie internetowe / adres IP Clearnet, twoje peery mogą zostać zakłócone. Dzięki URI węzła Tor zawsze będziesz mieć ten sam prywatny identyfikator, niezależnie od lokalizacji / adresu IP.


## Tworzenie kopii zapasowej/przywracanie węzła LND


Potężną, łatwą w zarządzaniu i przydatną funkcją jest przywracanie innych martwych węzłów LND, przy użyciu tylko 24-słownej listy seed i pliku channels.backup. [Tutaj jest przewodnik jak przywrócić martwe węzły Umbrel w Blixt w przypadku SHTF](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario)


Użytkownik ma również możliwość zapisania kopii zapasowej kanału Blixt na Dysku Google i/lub w lokalnej pamięci na własnym urządzeniu mobilnym (aby później przenieść ją w bezpieczne miejsce, z dala od telefonu).


Proces przywracania jest dość prosty: wstaw 24-słowowy seed, dodaj plik kopii zapasowej (wcześniej skopiowany do pamięci telefonu komórkowego) i kliknij przycisk przywracania. Synchronizacja i skanowanie wszystkich bloków pod kątem wcześniejszych transakcji zajmie trochę czasu. Kanały zostaną automatycznie zamknięte, a środki zwrócone do On-Chain Wallet (patrz menu szuflady w lewym górnym rogu - On-Chain).


**Uwaga** Jeśli wcześniej miałeś otwarte kanały ze starym węzłem za Tor, musisz najpierw włączyć opcję Tor (i ponownie uruchomić aplikację) w ustawieniach menu. W ten sposób procedura zamknięcia nie zakończy się niepowodzeniem i/lub opcja wymuszonego zamknięcia nie zostanie użyta.


Pamiętaj, aby wykonać kopię zapasową kanałów LN po otwarciu i/lub zamknięciu kanałów. To zajmie tylko kilka sekund. Później można przenieść plik kopii zapasowej w bezpieczne miejsce z dala od urządzenia mobilnego.

Aby przetestować seed w scenariuszu przywracania, przed dodaniem środków wystarczy użyć tego samego 24-słownego seed (aezeed) w BlueWallet. Jeśli wygenerowany BTC Address jest taki sam w Blixt, możesz zacząć. Po tym nie ma potrzeby korzystania z BlueWallet, można po prostu usunąć testowany Wallet w celu przywrócenia.


## Wbudowany Tor


Po aktywacji aplikacja uruchomi się ponownie za siecią Tor. Od tego momentu w ustawieniach menu można zobaczyć identyfikator węzła z cebulą Address, dzięki czemu inne węzły mogą otwierać kanały do małego węzła mobilnego Blixt. Lub powiedzmy, że masz własny węzeł w domu i chcesz mieć małe kanały z węzłem mobilnym Blixt. Idealne połączenie.


## Dunder LSP - dostawca usług płynnościowych


Prosta i fantastyczna funkcja, która oferuje nowym użytkownikom możliwość natychmiastowego rozpoczęcia przyjmowania BTC na Lightning Network, bez konieczności wpłacania środków On-Chain, a następnie otwierania kanałów LN.


Dla nowych użytkowników jest to świetna wiadomość, ponieważ mają oni mieć możliwość rozpoczęcia od zera, bezpośrednio na LN. Aby to zrobić, wystarczy utworzyć LN Invoice z ekranu głównego na przycisku "odbierz", wprowadzić kwotę, opis itp. i zapłacić z innego Wallet. Blixt otworzy kanał do 400 tys. Sats na każdą otrzymaną transakcję. W razie potrzeby można otworzyć wiele kanałów.


Interesujący i przydatny przypadek jest następujący: powiedzmy, że pierwsza otrzymana kwota to 200 tys. Blixt otworzy kanał Sats o wartości 400 tys. z już 200 tys. (minus opłaty za otwarcie) po twojej stronie, ale ponieważ nadal masz 200 tys. dostępnego "miejsca", możesz otrzymać więcej. Tak więc następna płatność, powiedzmy 100 tys. zł, dotrze bezpośrednio przez ten kanał, bez dodatkowych opłat, a ty nadal masz 100 tys. miejsca, aby otrzymać więcej.


Ale jeśli zdecydujesz się otrzymać, powiedzmy, 300 tys. za trzecią płatność, utworzy to kolejny nowy kanał 400 tys. i przeniesie te 300 tys. na twoją stronę.


Jeśli jest zbyt wiele żądań, węzeł Blixt może dostosować przepustowość kanału podczas otwierania.


## Automatyczne otwieranie kanału


W ustawieniach użytkownik może aktywować tę opcję i uzyskać automatyczną usługę, która otwiera kanały z najlepszymi węzłami i trasami w oparciu o dostępne saldo w On-Chain Wallet aplikacji Blixt. Jest to korzystna funkcja dla nowych użytkowników, którzy nie są pewni, z którym węzłem otworzyć kanał i/lub jak otworzyć kanał LN. To jak autopilot dla LN.


**Ta opcja jest używana tylko raz, podczas tworzenia nowego Wallet Blixt i jest domyślnie włączona. Jeśli więc nowy użytkownik zeskanuje kod QR On-Chain na ekranie głównym i zdeponuje swój pierwszy Sats na tym Address, Blixt automatycznie otworzy kanał z tymi Sats, z węzłem publicznym Blixt.


## Usługi płynności przychodzącej


Funkcja dedykowana sprzedawcom, którzy potrzebują więcej PRZYCHODZĄCEJ płynności, łatwa w użyciu. Aby to zrobić, wystarczy wybrać jednego z dostawców płynności z listy, zapłacić żądaną kwotę za kanał i podać swój identyfikator węzła, a stamtąd kanał zostanie otwarty dla węzła Blixt.


## Listy kontaktów


Przydatna funkcja, jeśli chcesz mieć trwałą listę odbiorców, z którymi handlujesz przez większość czasu. Lista ta może składać się z adresów LNURL, adresów Lightning lub przyszłych statycznych informacji o płatnościach/fakturach. Na razie lista ta nie może być zapisana poza aplikacją, ale planowana jest opcja jej eksportu.


## LNURL i Lightning Address


Pełna obsługa LNURL. Możesz zapłacić za LNURL, LN-auth, LN-chan request z LNURL.

Można wysłać do dowolnego LN Address, a także dodać go do listy kontaktów.

Począwszy od wersji. 0.6.9 dostępny jest odbiór do własnego typu LN Address _@blixtwallet.com_, poprzez funkcję [Blixt Lightning Box](https://github.com/hsjoberg/lightning-box).


## Keysend


Bardzo potężna funkcja, którą posiada niewiele portfeli mobilnych. Możesz wysyłać/przesyłać środki bezpośrednio przez kanał lub wskazać inny węzeł, dodając w razie potrzeby wiadomość. To jak tajny czat przez LN. Ta funkcja jest bardzo przydatna do wyświetlania wiadomości na billboardzie Amboss.space ([tutaj znajduje się przewodnik po billboardzie Amboss](https://darthcoin.substack.com/p/amboss-billboard-amazing-tool)).


## Podpisywanie wiadomości


Bardzo przydatne narzędzie do podpisywania wiadomości kluczem prywatnym węzła Blixt, wiadomości uwierzytelniających itp. Bardzo niewiele portfeli mobilnych ma tę funkcję, prawie żaden.


## Płatności wielokanałowe - płatności wielościeżkowe (MPP)


Przydatna funkcja dla płatności LN, umożliwiająca podzielenie płatności LN na wiele części w wielu kanałach. To dobry sposób na zrównoważenie płynności w sieci i poprawę prywatności.


## Przeglądarka Lightning


Seria usług stron trzecich z LN, zorganizowana w ramach prostej, dostępnej i przyjaznej dla użytkownika przeglądarki. Jest to również dobry sposób na promowanie firm, które akceptują BTC na LN. Jest to funkcja, która będzie dalej rozwijana w przyszłości. Na razie nie działa ona za Torem, więc przeglądanie tych aplikacji będzie odbywać się w trybie clear (clearnet).


## Log Explorers


Jest to potężne narzędzie do sprawdzania logów LND i ogólnego stanu węzła. Istnieje opcja zapisania pliku dziennika. Bardzo przydatne jest posiadanie tych dzienników pod ręką na wypadek, gdyby potrzebna była pomoc programisty w zidentyfikowaniu niektórych problemów.


## Bezpieczeństwo


W ustawieniach aplikacji można ustawić, dla większego bezpieczeństwa Wallet/node, możliwość uruchamiania aplikacji za pomocą kodu PIN i/lub odcisku palca.


## On-Chain Wallet


Ta funkcja jest nieco ukryta w menu szuflady w lewym górnym rogu. Ponieważ nie jest często używana przez użytkownika LN, nie jest widoczna na ekranie głównym. Ale to nie szkodzi, można ją mieć na oddzielnym Wallet, gdzie można zarządzać adresami i przeglądać dziennik transakcji, importując seed na przykład na Sparrow. Być może w przyszłości Blixt Wallet będzie również zawierał funkcję zarządzania UTxO. Ale na razie, TYLKO używaj tego On-Chain Wallet do otwierania lub zamykania kanałów na LN.


## Funkcje specjalne



- Wraz z wersją. 0.6.9 wprowadzono "persistent mode", który pozwala użytkownikowi uruchomić Blixt jako zawsze online węzeł LN, utrzymując usługi LND przy życiu, a LN Wallet gotowy do odbierania/wysyłania w dowolnym momencie.
- Proste kanały Taproot - umożliwiają otwieranie kanałów Taproot w celu zapewnienia większej prywatności i zaawansowanych funkcji
- Kanały z zerowym potwierdzeniem z Blixt Dunder LSP
- Speedloader ("Synchronizacja kanałów LN") - Oznacza to, że wszystkie kanały zostaną szybko zsynchronizowane podczas uruchamiania, w celu lepszego wyszukiwania ścieżek. Choć konieczność zobaczenia ekranu synchronizacji na początku jest nieco irytująca, zapewni to, że Wallet będzie wiedział o wszystkich kanałach, a płatności będą szybsze i bardziej niezawodne.
- Przetłumaczone na ponad 25 języków!


## "Easter Eggs"


Tak, w aplikacji Blixt są pewne ukryte funkcje, małe rzeczy, które sprawiają, że aplikacja jest urocza, aktywując zabawne/interesujące działania i reakcje.

Wskazówka: spróbuj kliknąć dwa razy na logo Blixt w szufladzie 🙂 Pozwolę ci odkryć resztę.


# Przewodnik krok po kroku po rozpoczęciu korzystania z Blixt


**Wskazówka:** Jako nowy użytkownik LN, jeśli zaczynasz korzystać z Blixt LN Node, musisz najpierw wiedzieć, czym jest Lightning Network i jak działa, przynajmniej na poziomie podstawowym. [Tutaj przygotowaliśmy prostą listę zasobów na temat Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Przeczytaj je najpierw.


Uruchomienie pełnego węzła LN na urządzeniu mobilnym nie jest łatwym zadaniem i może zająć trochę miejsca (min. 600 MB) i pamięci. Zalecamy posiadanie dobrego urządzenia mobilnego, zaktualizowanego i korzystającego z co najmniej Androida 11 jako systemu operacyjnego.


Po otwarciu Blixt, ekran powitalny wyświetli kilka opcji:


![Demo Blixt 01](assets/blixt_t01.webp)


W prawym górnym rogu widoczne są 3 kropki, które aktywują menu:



- "enable Tor" - użytkownik może uruchomić sieć Tor, w szczególności jeśli chce przywrócić stary węzeł LND, który działał tylko z peerami Tor.
- "Ustaw węzeł Bitcoin" - jeśli użytkownik chce połączyć się bezpośrednio z własnym węzłem, aby zsynchronizować bloki za pośrednictwem Neutrino, może to zrobić od razu na ekranie powitalnym. Ta opcja jest również dobra w przypadku, gdy połączenie internetowe lub Tor nie jest tak stabilne, aby połączyć się z domyślnym węzłem Bitcoin (node.blixtwallet.com).


## Pierwszy krok - utworzenie nowego Wallet


Jeśli wybierzesz opcję "Utwórz nowy Wallet", zostaniesz przekierowany bezpośrednio do ekranu głównego Blixt Wallet.


To jest twój "kokpit", a także "Główny LN Wallet", więc pamiętaj, że pokaże on tylko saldo twojego LN Wallet. Główny Wallet jest wyświetlany osobno (patrz C).


![Demo Blixt 02](assets/blixt_t02.webp)


A - Ikona wskaźnika synchronizacji bloków Blixt. Jest to najważniejsza rzecz dla węzła LN: synchronizacja z siecią. Jeśli ta ikona nadal działa, oznacza to, że węzeł NIE JEST GOTOWY! Należy więc uzbroić się w cierpliwość, szczególnie w przypadku pierwszej początkowej synchronizacji. Może to potrwać do 6-8 minut, w zależności od urządzenia i połączenia internetowego.


Możesz go kliknąć i zobaczyć status synchronizacji:


![Demo Blixt 03](assets/blixt_t03.webp)


Możesz także kliknąć przycisk "Pokaż dziennik LND" (A), jeśli chcesz zobaczyć i przeczytać więcej szczegółów technicznych dziennika LND w czasie rzeczywistym. Jest to bardzo przydatne do debugowania i uczenia się, jak działa LN.


B - Tutaj można uzyskać dostęp do wszystkich ustawień Blixt, a jest ich wiele! Blixt oferuje wiele bogatych funkcji i opcji do zarządzania węzłem LN jak profesjonalista. Wszystkie te opcje są szczegółowo wyjaśnione w ["Blixt Features Page - Options Menu"](https://blixtwallet.github.io/features#blixt-options).


C - Tutaj znajduje się menu "Magic Drawer", również szczegółowo opisane tutaj. Tutaj znajduje się "Onchain Wallet" (B), Lightning Channels (C), Kontakty, ikona statusu kanałów (A), Keysend (D).


![Demo Blixt 04](assets/blixt_t04.webp)


D - To menu pomocy z linkami do strony FAQ / Przewodników, strony kontaktowej dewelopera, strony Github i grupy wsparcia Telegram.


E - Wskaż swój pierwszy BTC Address, gdzie możesz zdeponować swój pierwszy test Sats. JEST TO OPCJONALNE! Jeśli wpłacisz bezpośrednio do Address, otworzysz kanał LN w kierunku węzła Blixt. Oznacza to, że zobaczysz zdeponowane Sats, przechodzące do innej transakcji onchain (tx), w celu otwarcia tego kanału LN. Możesz to sprawdzić w Blixt onchain Wallet (patrz punkt C), klikając w prawym górnym menu TX.


![Demo Blixt 05](assets/blixt_t05.webp)


Jak widać w dzienniku transakcji Onchain, kroki są bardzo szczegółowe, wskazując, dokąd zmierzają Sats (wpłata, otwarcie, zamknięcie kanału)


**Zalecenie:** Po przetestowaniu kilku sytuacji doszliśmy do wniosku, że znacznie bardziej efektywne jest otwieranie kanałów między 1 a 5 M Sats. Mniejsze kanały mają tendencję do szybkiego wyczerpywania się i płacenia wyższego % opłat w porównaniu z większymi kanałami.


F - Wskazuje główne saldo Lightning Wallet. NIE jest to całkowite saldo Blixt Wallet, reprezentuje tylko Sats, które masz w kanałach Lightning, dostępne do wysłania. Jak wskazano wcześniej, Onchain Wallet jest oddzielny. Należy pamiętać o tym aspekcie. Onchain Wallet jest oddzielny z ważnego powodu: jest używany głównie do otwierania/zamykania kanałów LN.


Ok, więc teraz zdeponowałeś trochę Sats w tym onchain Address wyświetlanym na ekranie głównym. Zaleca się, aby po wykonaniu tej czynności utrzymać aplikację Blixt online i aktywną przez jakiś czas, aż BTC tx zostanie pobrany przez górników do pierwszego bloku.


Następnie może to potrwać do 20-30 minut, aż kanał zostanie w pełni potwierdzony i otwarty, a zobaczysz go w Magic Drawer - Lightning Channels jako aktywny. Również mała kolorowa kropka na górze szuflady, jeśli jest to Green, wskaże, że kanał LN jest online i gotowy do użycia w celu wysłania Sats przez LN.


Address i wyświetlony komunikat powitalny znikną. Nie ma już potrzeby otwierania automatycznego kanału. Możesz również wyłączyć tę opcję w menu Ustawienia.


Nadszedł czas, aby przejść dalej, testując inne funkcje i opcje otwierania kanałów LN.


Teraz otwórzmy kolejny kanał z innym peerem węzła. Społeczność Blixt stworzyła [listę dobrych węzłów do rozpoczęcia korzystania z Blixt] (https://github.com/hsjoberg/blixt-Wallet/issues/1033)


### Procedura otwierania normalnego niezapowiedzianego (prywatnego) kanału LN w węźle mobilnym Blixt


Jest to bardzo proste, wymaga jedynie kilku kroków i odrobiny cierpliwości:



- Przejdź do [listy społeczności Blixt] (https://github.com/hsjoberg/blixt-Wallet/issues/1033) dobrych rówieśników
- Wybierz węzeł i kliknij link do jego nazwy, co spowoduje otwarcie jego strony Amboss
- Kliknij, aby wyświetlić kod QR dla węzła URI Address


![Demo Blixt 06](assets/blixt_t06.webp)


Teraz otwórz Blixt i przejdź do górnej szuflady - Lightning Channels i kliknij przycisk "+"


![Demo Blixt 07](assets/blixt_t07.webp)


Teraz kliknij kamerę (A), aby zeskanować kod QR ze strony Amboss, a szczegóły węzła zostaną wypełnione. Dodaj kwotę Sats dla wybranego kanału, a następnie wybierz stawkę opłaty za tx. Możesz pozostawić opcję automatyczną (B), aby uzyskać szybsze potwierdzenie, lub ustawić ją ręcznie, przesuwając przycisk. Można również długo nacisnąć numer i edytować go według własnego uznania.


Nie należy umieszczać mniej niż 1 sat/vbyte! Zwykle lepiej jest [zapoznać się z opłatami Mempool] (https://Mempool.space/) przed otwarciem kanału i wybrać dogodną opłatę.


Gotowe, teraz wystarczy kliknąć przycisk "otwórz kanał" i poczekać na 3 potwierdzenia, co zwykle zajmuje 30 minut (1 blok co około 10 minut).


Po potwierdzeniu kanał będzie aktywny w sekcji "Kanały Lightning".


## Drugi krok - uzyskanie większej płynności przychodzącej


Ok, więc teraz mamy kanał LN z płynnością tylko OUTBOUND. Oznacza to, że możemy tylko WYSYŁAĆ, nadal nie możemy ODBIERAĆ Sats przez LN. Dlaczego? Czy przeczytałeś przewodniki wskazane na początku? Nie? Wróć i przeczytaj je. Bardzo ważne jest, aby zrozumieć, jak działają kanały LN.


![Demo Blixt 08](assets/blixt_t08.webp)


Jak widać na tym przykładzie, kanał otwarty z pierwszym depozytem nie ma zbyt dużej płynności INBOUND ("Can receive"), ale ma dużą płynność OUTBOUND ("Can send").


Jakie więc masz opcje, jeśli chcesz otrzymywać więcej Sats niż LN?



- Wydaj trochę Sats z istniejącego kanału. Tak, LN to sieć płatności Bitcoin, używana głównie do szybszego, tańszego, prywatnego i łatwego wydawania Sats. LN NIE jest sposobem na hodling, do tego służy onchain Wallet.
- Zamień część Sats z powrotem na swój onchain Wallet, korzystając z usługi wymiany podwodnej. W ten sposób nie wydajesz swojego Sats, ale oddajesz go z powrotem do swojego onchain Wallet. Szczegółowe informacje na temat niektórych metod można znaleźć na stronie [Blixt Guides Page] (https://blixtwallet.github.io/guides).
- Otwórz kanał INBOUND od dowolnego dostawcy LSP. Oto demo wideo na temat [jak używać LNBig LSP do otwierania kanału przychodzącego] (https://blixtwallet.github.io/assets/images/blixt-lnbig.mp4). Oznacza to, że zapłacisz niewielką opłatę za PUSTY kanał (po swojej stronie) i będziesz mógł otrzymywać więcej Sats do tego kanału. Jeśli jesteś sprzedawcą, który otrzymuje więcej niż wydaje, jest to dobra opcja. Również jeśli kupujesz Sats zamiast LN, używasz Robosats lub innego LN Exchange.
- Otwórz kanał Dunder z węzłem Blixt lub innym dostawcą Dunder LSP. Kanał Dunder to prosty sposób na uzyskanie płynności INBOUND, ale w tym samym czasie wpłacasz trochę Sats do tego kanału. Jest to również dobre, ponieważ otworzy kanał z [UTXO](https://en.Bitcoin.it/wiki/UTXO), który nie pochodzi z twojego Blixt Wallet. To dodaje trochę prywatności.

Jest to również dobre, ponieważ jeśli nie masz Sats w onchain Wallet, aby otworzyć normalny kanał LN, ale masz je w innym LN Wallet, możesz po prostu zapłacić z tego innego Wallet przez LN za otwarcie i depozyt (po twojej stronie) tego kanału Dunder. [Więcej szczegółów jak działa Dunder i jak uruchomić własny serwer tutaj](https://github.com/hsjoberg/dunder-lsp)


![Demo Blixt 09](assets/blixt_t09.webp)


Oto kroki, jak aktywować otwarcie kanału Dunder:



- Przejdź do Ustawień, w sekcji "Eksperymenty" aktywuj pole "Włącz Dunder LSP".
- Gdy to zrobisz, wróć do sekcji "Lightning Network" i zobaczysz, że pojawiła się opcja "Ustaw serwer Dunder LSP". Tam domyślnie ustawiony jest "https://dunder.blixtwallet.com", ale można go zmienić na dowolnego innego dostawcę Dunder LSP Address. [Tutaj jest lista społeczności Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) z węzłami, które mogą zapewnić kanały Dudner LSP dla twojego Blixt.
- Teraz możesz przejść do ekranu głównego i kliknąć przycisk "Odbierz". Następnie postępuj zgodnie z procedurą opisaną [w tym przewodniku] (https://blixtwallet.github.io/guides#guide-lsp).


Ok, więc po potwierdzeniu kanału Dunder (zajmie to kilka minut) będziesz mieć 2 kanały LN: jeden otwarty początkowo z autopilotem (kanał A) i jeden z większą płynnością przychodzącą, otwarty z Dunder (kanał B).


![Demo Blixt 10](assets/blixt_t10.webp)


Dobrze, teraz możesz wysyłać i odbierać wystarczającą ilość Sats przez LN!


## Krok trzeci - Procedura przywracania węzła


Omówmy teraz, jak przywrócić uszkodzony węzeł Blixt Wallet lub inny LND. Jest to nieco bardziej techniczne, ale prosimy o uwagę. To nie jest Hard.


**Przypomnienie:** w przeszłości napisałem dedykowany przewodnik z wieloma opcjami [jak przywrócić uszkodzony węzeł LND](https://darthcoin.substack.com/p/umbrel-btcln-node-shtf-scenario), gdzie wspomniałem również o metodzie użycia Blixt jako szybkiego procesu przywracania, przy użyciu pliku seed + channel.backup z martwego węzła LND. Napisałem również przewodnik, jak przywrócić węzeł Blixt lub zmigrować Blixt na inne urządzenie, [tutaj](https://blixtwallet.github.io/faq#blixt-restore).


![Demo Blixt 11](assets/blixt_t11.webp)


Wyjaśnijmy jednak ten proces w prostych krokach. Jak widać na powyższym obrazku, są 2 rzeczy, które należy zrobić, aby przywrócić poprzedni węzeł Blixt/LND:



- górne pole to miejsce, w którym należy wpisać wszystkie 24 słowa z seed (stary / martwy węzeł)
- na dole znajdują się dwie opcje przycisków, aby wstawić / przesłać plik channel.backup, wcześniej zapisany ze starego węzła Blixt/LND. Może to być plik lokalny (przesłany wcześniej do urządzenia) lub z dysku Google / zdalnej lokalizacji iCloud. Blixt ma tę opcję, aby zapisać kopię zapasową kanałów bezpośrednio na dysku Google / iCloud. Więcej szczegółów można znaleźć na stronie [Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options).


Niemniej jednak, jeśli wcześniej nie miałeś żadnych otwartych kanałów LN, nie ma potrzeby przesyłania żadnego pliku channels.backup. Wystarczy wstawić 24 słowa seed i nacisnąć przycisk przywracania.


Nie zapomnij aktywować Tora z górnego menu z 3 kropkami, jak wyjaśniliśmy w rozdziale "Pierwszy krok" tego przewodnika. Dzieje się tak w przypadku, gdy masz TYLKO peerów Tor i nie można się z Tobą skontaktować przez clearnet (domena/IP). W przeciwnym razie nie jest to konieczne.


Inną przydatną funkcją jest ustawienie konkretnego węzła Bitcoin z tego górnego menu. Domyślnie synchronizuje bloki z node.blixtwallet.com (tryb neutrino), ale można ustawić dowolny inny węzeł Bitcoin, który zapewnia synchronizację neutrino.


Po wypełnieniu tych opcji i naciśnięciu przycisku przywracania, Blixt rozpocznie najpierw synchronizację bloków przez Neutrino, jak wyjaśniliśmy w rozdziale "Pierwszy krok" tego przewodnika. Bądź więc cierpliwy i obserwuj proces przywracania na ekranie głównym, klikając ikonę synchronizacji.


![Demo Blixt 12](assets/blixt_t12.webp)


Jak widać na tym przykładzie, bloki Bitcoin są w 100% zsynchronizowane (A), a proces odzyskiwania jest w toku (B). Oznacza to, że kanały LN, które miałeś wcześniej, zostaną zamknięte, a środki przywrócone do twojego Blixt onchain Wallet.


Ten proces wymaga czasu! Prosimy więc o cierpliwość i staranie się, aby Blixt był aktywny i online. Początkowa synchronizacja może potrwać do 6-8 minut, a zamykanie kanałów może potrwać do 10-15 minut. Lepiej więc mieć dobrze naładowane urządzenie.


Po rozpoczęciu tego procesu można sprawdzić w Magic Drawer - Lightning Channels status każdego z poprzednich kanałów, pokazując, że są one w stanie "oczekującym na zamknięcie". Gdy każdy kanał zostanie zamknięty, możesz zobaczyć zamykający tx w onchain Wallet (patrz Magic Drawer - Onchain) i otworzyć dziennik menu tx.


![Demo Blixt 13](assets/blixt_t13.webp)


Dobrze będzie również sprawdzić i dodać, jeśli ich tam nie ma, poprzednie urządzenia równorzędne, które miałeś w starym węźle LN. Przejdź więc do menu Ustawienia, w dół do "Lightning Network" i wejdź w opcję "Show Lightning Peers".


![Demo Blixt 14](assets/blixt_t14.webp)


Wewnątrz sekcji zobaczysz rówieśników, z którymi jesteś połączony w tym momencie i możesz dodać więcej, lepiej dodać tych, z którymi miałeś kanały wcześniej. Wystarczy przejść do strony Amboss, wyszukać aliasy węzłów peer lub nodeID i zeskanować ich URI węzła.


![Demo Blixt 15](assets/blixt_t15.webp)


Jak widać na powyższym obrazku, są 3 aspekty:


A - reprezentuje węzeł Clearnet Address URI (domena/IP)


B - reprezentuje węzeł cebuli Tor Address URI (.onion)


C - to kod QR do zeskanowania kamerą Blixt lub przycisk kopiowania.


Ten węzeł Address URI należy dodać do listy peerów. Należy więc pamiętać, że nie wystarczy tylko nazwa aliasu węzła lub nodeID.


Teraz możesz przejść do Magic Drawer (menu w lewym górnym rogu) - Lightning Channels i zobaczyć, przy jakiej wysokości bloku zapadalności środki zostaną zwrócone do twojego onchain Address.


![Demo Blixt 16](assets/blixt_t16.webp)


Blok o numerze 764272 to moment, w którym środki będą dostępne w łańcuchu Bitcoin onchain Address. I może to potrwać do 144 bloków od pierwszego bloku potwierdzenia do ich uwolnienia. Więc sprawdź to w [Mempool](https://Mempool.space/).


I to wszystko. Wystarczy cierpliwie poczekać, aż wszystkie kanały zostaną zamknięte, a środki wrócą do łańcucha Wallet.


## Krok czwarty - personalizacja


Ten rozdział dotyczy dostosowywania i lepszego poznania węzła Blixt. Nie będę opisywał wszystkich dostępnych funkcji, jest ich zbyt wiele i zostały już wyjaśnione na stronie [Blixt Features Page](https://blixtwallet.github.io/features).


Zwrócę jednak uwagę na niektóre z nich, które są niezbędne, aby korzystać z Blixt i mieć wspaniałe doświadczenia.


### A - Nazwa (NameDesc)


![Demo Blixt 17](assets/blixt_t17.webp)


[NameDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) to standard przekazywania "nazwy odbiorcy" w fakturach BOLT11.


Może to być dowolna nazwa i można ją zmienić w dowolnym momencie.


Ta opcja jest naprawdę przydatna w różnych przypadkach, gdy chcesz wysłać nazwę wraz z opisem Invoice, aby odbiorca mógł uzyskać wskazówkę, kto otrzymał te Sats. Jest to w pełni opcjonalne i również na ekranie płatności użytkownik musi zaznaczyć pole wskazujące na wysłanie nazwy aliasu.


Oto przykład tego, co pojawi się po użyciu [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![Demo Blixt 18](assets/blixt_t18.webp)


Jest to kolejny przykład wysyłania do innej aplikacji Wallet, która obsługuje NameDesc:


![Demo Blixt 19](assets/blixt_t19.webp)


### B - Zapasowe kanały LN i słowa seed


To bardzo ważna funkcja!


Po otwarciu lub zamknięciu kanału LN należy wykonać kopię zapasową. Można to zrobić ręcznie, zapisując niewielki plik na urządzeniu lokalnym (zwykle w folderze pobierania) lub korzystając z konta Google Drive lub iCloud.


![Demo Blixt 20](assets/blixt_t20.webp)


Przejdź do Ustawienia Blixt - sekcja Wallet. Dostępne są tam opcje zapisywania wszystkich ważnych danych dla Blixt Wallet:



- "Pokaż Mnemonic" - wyświetli 24 słowa seed, aby je zapisać
- "Usuń Mnemonic z urządzenia" - jest to opcjonalne i należy go używać tylko wtedy, gdy naprawdę chcesz usunąć słowa seed z urządzenia. NIE spowoduje to wyczyszczenia Wallet, tylko seed. Ale uwaga! Nie ma możliwości ich odzyskania, jeśli nie zostały wcześniej zapisane.
- "Eksportuj kopię zapasową kanału" - ta opcja spowoduje zapisanie małego pliku na urządzeniu lokalnym, zwykle w folderze "pliki do pobrania", skąd można go pobrać i przenieść poza urządzenie w celu bezpiecznego przechowywania.
- "Weryfikuj kopię zapasową kanału" - jest to dobra opcja, jeśli korzystasz z Dysku Google lub iCloud, aby sprawdzić integralność kopii zapasowej wykonanej zdalnie.
- "Google drive channel backup" - zapisze plik kopii zapasowej na osobistym dysku Google. Plik jest zaszyfrowany i przechowywany w oddzielnym repozytorium niż zwykłe pliki Google. Nie ma więc obaw, że może zostać odczytany przez kogokolwiek. W każdym razie plik ten jest całkowicie bezużyteczny bez słów seed, więc nikt nie może pobrać środków tylko z tego pliku.


Zalecałbym w tej sekcji następujące elementy:



- użyj menedżera haseł do bezpiecznego przechowywania seed i pliku kopii zapasowej. [KeePass](https://keepass.info/) lub Bitwarden są do tego bardzo dobre i mogą być używane na wielu platformach i samodzielnie hostowane lub offline.
- RÓB KOPIĘ ZAPASOWĄ ZA KAŻDYM RAZEM, gdy otwierasz lub zamykasz kanał. Plik ten jest aktualizowany o informacje o kanałach. Nie ma potrzeby robienia tego po każdej transakcji wykonanej na LN. Kopia zapasowa kanału nie przechowuje tych informacji, tylko status kanału.


![Demo Blixt 21](assets/blixt_t21.webp)


## Wnioski


Ok, istnieje wiele innych niesamowitych funkcji, które oferuje Blixt, pozwolę ci odkrywać je jeden po drugim i dobrze się bawić.


Ta aplikacja jest naprawdę niedoceniana, głównie dlatego, że nie jest wspierana przez żadne fundusze VC, jest napędzana przez społeczność, zbudowana z miłością i pasją do Bitcoin i Lightning Network.


Ten mobilny węzeł LN, Blixt, jest bardzo potężnym narzędziem w rękach wielu użytkowników, jeśli wiedzą, jak go dobrze używać. Wyobraź sobie, że chodzisz po świecie z węzłem LN w kieszeni i nikt o tym nie wie.


Nie wspominając już o wszystkich innych bogatych funkcjach, które oferuje Wallet.


Mam nadzieję, że spodoba ci się korzystanie z niego. Osobiście go uwielbiam i jest dla mnie bardzo przydatny (zobacz tutaj przypadek użycia, w którym Wallet jest świetnym narzędziem).


SZCZĘŚLIWY Bitcoin LIGHTNING!


Niech ₿ITCOIN będzie z tobą!


**Zrzeczenie się odpowiedzialności:** Nie jestem opłacany ani wspierany w żaden sposób przez twórców tej aplikacji. Napisałem ten przewodnik, ponieważ zauważyłem, że zainteresowanie tą aplikacją Wallet rośnie, a nowi użytkownicy wciąż nie rozumieją, jak zacząć z nią korzystać. Również po to, aby pomóc Hampusowi (głównemu deweloperowi) z dokumentacją dotyczącą korzystania z tego węzła Wallet. Nie mam żadnego innego interesu w promowaniu tej aplikacji LN, poza popychaniem do przodu adopcji Bitcoin i LN. To jedyny sposób!