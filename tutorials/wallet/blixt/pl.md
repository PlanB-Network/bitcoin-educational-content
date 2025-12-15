---
name: Blixt Wallet
description: Jak zacząć korzystać z potężnego węzła LN na telefonie komórkowym?
---
![cover](assets/cover.webp)


Niniejszy przewodnik jest przeznaczony dla wszystkich nowych użytkowników, którzy chcą rozpocząć korzystanie z Bitcoin Lightning Network (LN) w sposób BEZPŁATNY, OPEN SOURCE, W PEŁNI NIEZAWODNY.


Korzystanie z [Blixt Wallet](https://blixtwallet.com/), pełnego węzła LN na telefonie komórkowym, gdziekolwiek jesteś.


Jeśli nigdy nie używałeś Bitcoin Lightning Network, zanim zaczniesz, [przeczytaj tę prostą analogię wyjaśniającą Lightning Network (LN)](https://darth-coin.github.io/beginner/LN-airport-analogy-en.html).


## WAŻNE ASPEKTY:



- Blixt jest węzłem prywatnym, NIE węzłem routingu! Należy o tym pamiętać: Oznacza to, że wszystkie kanały LN w Blixt będą niezapowiedziane na wykresie LN (tzw. kanały prywatne). Oznacza to, że TEN WĘZEŁ NIE BĘDZIE ROBIŁ ROUTINGU innych płatności przez węzeł Blixt. Ten węzeł Blixt NIE służy do routingu, powtarzam. Służy głównie do zarządzania własnymi kanałami LN i dokonywania płatności LN prywatnie, kiedy tylko zajdzie taka potrzeba. Ten węzeł Blixt musi być online i zsynchronizowany TYLKO PRZED dokonaniem transakcji. Dlatego na górze zobaczysz ikonę wskazującą status synchronizacji. Zajmuje to tylko kilka chwil, w zależności od tego, ile czasu pozostawałeś offline.



- Blixt używa LND (aezeed) jako backendu Wallet, więc nie próbuj importować do niego innych typów portfeli Bitcoin. [Tutaj masz wyjaśnione rodzaje nasion Wallet Mnemonic](https://coldbit.com/what-types-of-Mnemonic-seeds-are-used-in-Bitcoin/). A tutaj jest [bardziej obszerna lista wszystkich rodzajów portfeli](https://walletsrecovery.org/). Więc jeśli wcześniej miałeś węzeł LND, możesz zaimportować seed i backup.channels do Blixt, [jak wyjaśniono w tym przewodniku](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html).



- Na końcu tego przewodnika znajduje się specjalna sekcja z ["poradami i wskazówkami"] (https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#tips)



- Kolejne ważne linki - znajdują się na końcu tego przewodnika, prosimy o dodanie ich do zakładek.


---

## Blixt - Pierwszy kontakt


Więc... Mama Dartha postanowiła zacząć używać LN z Blixtem. Decyzja Hard, ale mądra. Blixt jest tylko dla inteligentnych ludzi i tych, którzy naprawdę chcą nauczyć się głębszego korzystania z LN.


![blixt](assets/en/01.webp)


Darth ostrzega swoją mamę:


"*Mamo, jeśli zaczniesz używać węzła Blixt LN, musisz najpierw wiedzieć, czym jest Lightning Network i jak działa, przynajmniej na poziomie podstawowym. [Tutaj umieściłem prostą listę zasobów na temat Lightning Network](https://blixtwallet.github.io/faq#what-is-LN). Przeczytaj je najpierw.*"


Mama Dartha zapoznała się z zasobami i wykonała pierwszy krok: zainstalowała Blixt na swoim nowym urządzeniu z Androidem. Blixt jest również dostępny na iOS i macOS (desktop). Ale te nie są dla mamy Dartha... Niemniej jednak zaleca się korzystanie z nowszej wersji Androida, co najmniej 9 lub 10, aby uzyskać lepszą kompatybilność i wrażenia. Uruchomienie pełnego węzła LN na urządzeniu mobilnym nie jest łatwym zadaniem i może zająć trochę miejsca (min. 600 MB) i pamięci.


Po otwarciu Blixt, ekran powitalny wyświetli kilka opcji:


![blixt](assets/en/02.webp)


W prawym górnym rogu widoczne są 3 kropki, które aktywują menu:



- "enable Tor" - użytkownik może uruchomić sieć Tor, w szczególności jeśli chce przywrócić stary węzeł LND, który działał tylko z peerami Tor.
- "Ustaw węzeł Bitcoin" - jeśli użytkownik chce połączyć się bezpośrednio z własnym węzłem, aby zsynchronizować bloki za pośrednictwem Neutrino, może to zrobić od razu na ekranie powitalnym. Ta opcja jest również dobra w przypadku, gdy połączenie internetowe lub Tor nie jest tak stabilne, aby połączyć się z domyślnym węzłem Bitcoin (node.blixtwallet.com).
- Wkrótce zostanie tam dodany język, dzięki czemu użytkownik będzie mógł zacząć od razu od języka, który jest dla niego wygodny. Jeśli chcesz przyczynić się do tego projektu open source z tłumaczeniami na inne języki, [dołącz tutaj](https://explore.transifex.com/blixt-Wallet/blixt-Wallet/).


### OPCJA A - Utworzenie nowego Wallet


Jeśli wybierzesz opcję "Utwórz nowy Wallet", zostaniesz przekierowany bezpośrednio do ekranu głównego Blixt Wallet.


To jest twój "kokpit", a także "Główny LN Wallet", więc pamiętaj, że pokaże on tylko saldo twojego LN Wallet. Główny Wallet jest wyświetlany osobno (patrz C).


![blixt](assets/en/03.webp)


A - Ikona wskaźnika synchronizacji bloków Blixt. Jest to najważniejsza rzecz dla węzła LN: synchronizacja z siecią. Jeśli ta ikona nadal działa, oznacza to, że węzeł NIE JEST GOTOWY! Należy więc uzbroić się w cierpliwość, szczególnie w przypadku pierwszej początkowej synchronizacji. Może to potrwać do 6-8 minut, w zależności od urządzenia i połączenia internetowego.


Możesz go kliknąć i zobaczyć status synchronizacji:


![blixt](assets/en/04.webp)


Możesz także kliknąć przycisk "Pokaż dziennik LND" (A), jeśli chcesz zobaczyć i przeczytać więcej szczegółów technicznych dziennika LND w czasie rzeczywistym. Jest to bardzo przydatne do debugowania i uczenia się, jak działa LN.


B - Tutaj można uzyskać dostęp do wszystkich ustawień Blixt, a jest ich wiele! Blixt oferuje wiele bogatych funkcji i opcji do zarządzania węzłem LN jak profesjonalista. Wszystkie te opcje są szczegółowo wyjaśnione w "[Strona funkcji Blixt](https://blixtwallet.github.io/features#blixt-options) - Menu opcji".


C - Tutaj znajduje się menu "Magic Drawer" [wyjaśnione szczegółowo tutaj] (https://blixtwallet.github.io/features#blixt-drawer). Tutaj jest "Onchain Wallet" (B), Lightning Channels (C), Kontakty, ikona statusu kanałów (A), Keysend (D).


![blixt](assets/en/05.webp)


D - To menu pomocy z linkami do strony FAQ / Przewodników, strony kontaktowej dewelopera, strony Github i grupy wsparcia Telegram.


E - Wskaż swój pierwszy BTC Address, gdzie możesz zdeponować swój pierwszy test Sats. JEST TO OPCJONALNE! Jeśli wpłacisz bezpośrednio do Address, otworzysz kanał LN w kierunku węzła Blixt. Oznacza to, że zdeponowany Sats zostanie przekazany do innej transakcji onchain (tx) w celu otwarcia kanału LN. Możesz to sprawdzić w Blixt onchain Wallet (patrz punkt C), klikając w prawym górnym menu TX.


![blixt](assets/en/06.webp)


Jak widać w dzienniku transakcji Onchain, kroki są bardzo szczegółowe, wskazując, dokąd zmierzają Sats (wpłata, otwarcie, zamknięcie kanału).


ZALECENIE:


Po przetestowaniu kilku sytuacji doszliśmy do wniosku, że znacznie bardziej efektywne jest otwieranie kanałów od 1 do 5 M Sats. Mniejsze kanały mają tendencję do szybkiego wyczerpywania się i płacenia wyższego % opłat w porównaniu z większymi kanałami.


F - Wskazuje główne saldo Lightning Wallet. NIE jest to całkowite saldo Blixt Wallet, reprezentuje tylko Sats, które masz w kanałach Lightning, dostępne do wysłania. Jak wskazano wcześniej, Onchain Wallet jest oddzielny. Należy pamiętać o tym aspekcie. Onchain Wallet jest oddzielny z ważnego powodu: jest używany głównie do otwierania/zamykania kanałów LN.


Ok, więc teraz mama Dartha zdeponowała trochę Sats w tym onchain Address wyświetlanym na ekranie głównym. Zaleca się, aby po wykonaniu tej czynności utrzymać aplikację Blixt online i aktywną przez jakiś czas, aż BTC tx zostanie pobrany przez górników do pierwszego bloku.


Następnie może to potrwać do 20-30 minut, aż kanał zostanie w pełni potwierdzony i otwarty, a zobaczysz go w Magic Drawer - Lightning Channels jako aktywny. Również mała kolorowa kropka na górze szuflady, jeśli jest to Green, wskaże, że kanał LN jest online i gotowy do użycia w celu wysłania Sats przez LN.


Address i wyświetlony komunikat powitalny znikną. Nie ma już potrzeby otwierania automatycznego kanału. Możesz również wyłączyć tę opcję w menu Ustawienia.


Nadszedł czas, aby przejść dalej, testując inne funkcje i opcje otwierania kanałów LN.


Teraz otwórzmy kolejny kanał z innym peerem węzła. Społeczność Blixt stworzyła [listę dobrych węzłów do rozpoczęcia korzystania z Blixt] (https://github.com/hsjoberg/blixt-Wallet/issues/1033).


**Procedura otwierania kanału LN w Blixt**


Jest to bardzo proste, wymaga jedynie kilku kroków i odrobiny cierpliwości:



- Dostałem się na listę rówieśników [Blixt Community](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- Wybierz węzeł i kliknij link do jego nazwy, co spowoduje otwarcie jego strony Amboss
- Kliknij, aby wyświetlić kod QR dla URI węzła Address


![blixt](assets/en/07.webp)


Otwórz Blixt i przejdź do górnej szuflady - Lightning Channels i kliknij przycisk "+"


![blixt](assets/en/08.webp)


Teraz kliknij kamerę (A), aby zeskanować kod QR ze strony Amboss, a szczegóły węzła zostaną wypełnione. Dodaj kwotę Sats dla wybranego kanału, a następnie wybierz stawkę opłaty za tx. Możesz pozostawić opcję automatyczną (B), aby uzyskać szybsze potwierdzenie, lub ustawić ją ręcznie, przesuwając przycisk. Możesz także długo nacisnąć numer i edytować go według własnego uznania.


Nie umieszczaj mniej niż 1 sat/vbyte! Zwykle lepiej jest sprawdzić [Opłaty Mempool] (https://Mempool.space/) przed otwarciem kanału i wybrać dogodną opłatę.


Gotowe, teraz wystarczy kliknąć przycisk "otwórz kanał" i poczekać na 3 potwierdzenia, co zwykle zajmuje 30 minut (1 blok co około 10 minut).


Po potwierdzeniu kanał będzie aktywny w sekcji "Kanały Lightning".


---

## Blixt - Drugi kontakt


Ok, więc teraz mamy kanał LN z płynnością tylko OUTBOUND. Oznacza to, że możemy tylko WYSYŁAĆ, nadal nie możemy ODBIERAĆ Sats przez LN.


![blixt](assets/en/09.webp)


Dlaczego? Czy przeczytałeś poradniki wskazane na początku? Nie? Wróć i przeczytaj je. Bardzo ważne jest, aby zrozumieć, jak działają kanały LN.


![blixt](assets/en/10.webp)


Jak widać na tym przykładzie, kanał otwarty z pierwszym depozytem nie ma zbyt dużej płynności INBOUND ("Can receive"), ale ma dużą płynność OUTBOUND ("Can send").


Jakie więc masz opcje, jeśli chcesz otrzymywać więcej Sats niż LN?



- Wydaj trochę Sats z istniejącego kanału. Tak, LN to sieć płatności Bitcoin, używana głównie do szybszego, tańszego, prywatnego i łatwego wydawania Sats. LN NIE jest sposobem na hodling, do tego służy onchain Wallet.



- Zamień trochę Sats z powrotem na swój onchain Wallet, korzystając z usługi wymiany podwodnej. W ten sposób nie wydajesz swoich Sats, ale oddajesz je z powrotem do swojego onchain Wallet. Szczegółowe informacje na temat niektórych metod można znaleźć na stronie [Blixt Guides Page] (https://blixtwallet.github.io/guides).



- Otwórz kanał INBOUND od dowolnego dostawcy LSP. Tutaj znajduje się demo wideo o tym, jak używać LNBig LSP do otwierania kanału przychodzącego. Oznacza to, że zapłacisz niewielką opłatę za PUSTY kanał (po Twojej stronie) i będziesz mógł otrzymywać więcej Sats do tego kanału. Jeśli jesteś sprzedawcą, który otrzymuje więcej niż wydaje, jest to dobra opcja. Również jeśli kupujesz Sats przez LN, używasz Robosats lub innego LN Exchange.



- Otwórz kanał Dunder z węzłem Blixt lub innym dostawcą Dunder LSP. Kanał Dunder to prosty sposób na uzyskanie płynności INBOUND, ale w tym samym czasie wpłacasz trochę Sats do tego kanału. Jest to również dobre, ponieważ otworzy kanał z [UTXO](https://en.Bitcoin.it/wiki/UTXO), który nie pochodzi z twojego Blixt Wallet. Dodaje to trochę prywatności. Jest to również dobre, ponieważ jeśli nie masz Sats w onchain Wallet, aby otworzyć normalny kanał LN, ale masz je w innym LN Wallet, możesz po prostu zapłacić z tego innego Wallet przez LN za otwarcie i depozyt (po twojej stronie) tego kanału Dunder. [Więcej szczegółów jak działa Dunder i jak uruchomić własny serwer tutaj](https://github.com/hsjoberg/dunder-lsp).


![blixt](assets/en/11.webp)


Oto kroki, aby aktywować otwarcie kanału Dunder:



- Przejdź do Ustawień, w sekcji "Eksperymenty" aktywuj pole "Włącz Dunder LSP".
- Gdy to zrobisz, wróć do sekcji "Lightning Network" i zobaczysz, że pojawiła się opcja "Ustaw serwer Dunder LSP". Tam domyślnie ustawiony jest "https://dunder.blixtwallet.com", ale można go zmienić na dowolnego innego dostawcę Dunder LSP Address. [Tutaj znajduje się lista społeczności Blixt](https://github.com/hsjoberg/blixt-Wallet/issues/1033) z węzłami, które mogą zapewnić kanały Dudner LSP dla twojego Blixt.
- Teraz możesz przejść do ekranu głównego i kliknąć przycisk "Odbierz". Następnie postępuj zgodnie z procedurą [wyjaśnioną w tym przewodniku] (https://blixtwallet.github.io/guides#guide-lsp).


OK, więc po potwierdzeniu kanału Dunder (zajmie to kilka minut) będziesz mieć 2 kanały LN: jeden otwarty początkowo z autopilotem (kanał A) i jeden z większą płynnością przychodzącą, otwarty z Dunder (kanał B).


![blixt](assets/en/12.webp)


Dobrze, teraz możesz wysyłać i odbierać wystarczającą ilość Sats przez LN!


SZCZĘŚLIWY Bitcoin LIGHTNING!


---

## Blixt - Trzeci kontakt


Pamiętaj, że w rozdziale pierwszym "Pierwszy kontakt" były 2 opcje na ekranie powitalnym:


- [Opcja A](https://darth-coin.github.io/wallets/getting-started-blixt-Wallet-en.html#option-a) - Utwórz nowy Wallet
- Opcja B - Przywrócenie Wallet


Porozmawiajmy teraz o tym, jak przywrócić uszkodzony węzeł Blixt Wallet lub inny LND. Jest to nieco bardziej techniczne, ale proszę o uwagę. To nie jest Hard.


### OPCJA B - Przywrócenie Wallet


W przeszłości napisałem dedykowany przewodnik na temat [jak przywrócić uszkodzony węzeł Umbrel] (https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), w którym wspomniałem również o metodzie użycia Blixt jako szybkiego procesu przywracania, przy użyciu pliku seed + channel.backup z Umbrel.


Napisałem również przewodnik, jak przywrócić węzeł Blixt lub zmigrować Blixt na inne urządzenie, [tutaj](https://blixtwallet.github.io/faq#blixt-restore).


![blixt](assets/en/13.webp)


Wyjaśnijmy jednak ten proces w prostych krokach. Jak widać na powyższym obrazku, są 2 rzeczy, które należy zrobić, aby przywrócić poprzedni węzeł Blixt/LND:



- górne pole to miejsce, w którym należy wpisać wszystkie 24 słowa z seed (stary / martwy węzeł)
- na dole znajdują się dwie opcje przycisków, aby wstawić / przesłać plik channel.backup, wcześniej zapisany ze starego węzła Blixt/LND. Może to być plik lokalny (przesłany wcześniej do urządzenia) lub z dysku Google / zdalnej lokalizacji iCloud. Blixt ma tę opcję, aby zapisać kopię zapasową kanałów bezpośrednio na dysku Google / iCloud. Więcej szczegółów można znaleźć na stronie [Blixt Features Page] (https://blixtwallet.github.io/features#blixt-options).


Niemniej jednak, jeśli wcześniej nie miałeś żadnych otwartych kanałów LN, nie ma potrzeby przesyłania żadnego pliku channels.backup. Wystarczy wstawić 24 słowa seed i nacisnąć przycisk przywracania.


Nie zapomnij aktywować Tora z górnego menu z 3 kropkami, jak wyjaśniliśmy w sekcji Opcja A. Dzieje się tak w przypadku, gdy masz TYLKO peerów Tor i nie można się z Tobą skontaktować przez clearnet (domena/IP). W przeciwnym razie nie jest to konieczne.


Inną przydatną funkcją jest ustawienie konkretnego węzła Bitcoin z górnego menu. Domyślnie synchronizuje bloki z node.blixtwallet.com (tryb neutrino), ale można ustawić dowolny inny węzeł Bitcoin, który zapewnia synchronizację neutrino.


Po wypełnieniu tych opcji i naciśnięciu przycisku przywracania, Blixt rozpocznie najpierw synchronizację bloków przez Neutrino, jak wyjaśniliśmy w rozdziale Pierwszy kontakt. Bądź więc cierpliwy i obserwuj proces przywracania na ekranie głównym, klikając ikonę synchronizacji.


![blixt](assets/en/14.webp)


Jak widać na tym przykładzie, bloki Bitcoin są w 100% zsynchronizowane (A), a proces odzyskiwania jest w toku (B). Oznacza to, że kanały LN, które miałeś wcześniej, zostaną zamknięte, a środki przywrócone do twojego Blixt onchain Wallet.


Ten proces wymaga czasu! Prosimy więc o cierpliwość i staranie się, aby Blixt był aktywny i online. Początkowa synchronizacja może potrwać do 6-8 minut, a zamykanie kanałów może potrwać do 10-15 minut. Lepiej więc mieć dobrze naładowane urządzenie.


Po rozpoczęciu tego procesu można sprawdzić w Magic Drawer - Lightning Channels status każdego z poprzednich kanałów, pokazując, że są one w stanie "oczekującym na zamknięcie". Po zamknięciu każdego kanału można zobaczyć zamykający tx w onchain Wallet (patrz Magic Drawer - Onchain) i otworzyć dziennik menu tx.


![blixt](assets/en/15.webp)


Dobrze będzie również sprawdzić i dodać, jeśli ich tam nie ma, poprzednie urządzenia równorzędne, które miałeś w starym węźle LN. Przejdź więc do menu Ustawienia, w dół do "Lightning Network" i wejdź w opcję "Show Lightning Peers".


![blixt](assets/en/16.webp)


Wewnątrz sekcji zobaczysz peerów, z którymi jesteś połączony w tym momencie i możesz dodać więcej, lepiej dodać tych, z którymi miałeś kanały wcześniej. Wystarczy przejść do [strony Amboss] (https://amboss.space/), wyszukać aliasy węzłów peer lub nodeID i zeskanować ich URI węzła.


![blixt](assets/en/17.webp)


Jak widać na powyższym obrazku, są 3 aspekty:


A - reprezentuje węzeł Clearnet Address URI (domena/IP)


B - reprezentuje węzeł cebuli Tor Address URI (.onion)


C - to kod QR do zeskanowania kamerą Blixt lub przycisk kopiowania.


Ten węzeł Address URI należy dodać do listy elementów równorzędnych. Należy więc pamiętać, że nie wystarczy tylko nazwa aliasu węzła lub nodeID.


Teraz możesz przejść do Magic Drawer (menu w lewym górnym rogu) - Lightning Channels i zobaczyć, przy jakiej wysokości bloku zapadalności środki zostaną zwrócone do twojego onchain Address.


![blixt](assets/en/18.webp)


Blok o numerze 764272 to moment, w którym środki będą dostępne w łańcuchu Bitcoin onchain Address. I może to potrwać do 144 bloków od pierwszego bloku potwierdzenia do ich uwolnienia. [Sprawdź to w Mempool](https://Mempool.space/).


I to wszystko. Wystarczy cierpliwie poczekać, aż wszystkie kanały zostaną zamknięte, a środki wrócą do Wallet.


**Tajna metoda przywracania :**


Istnieje inna metoda przywrócenia węzła Blixt LND nawet bez zamykania kanałów. Ale jest ukryta przed zwykłymi użytkownikami noob, ponieważ ta metoda jest TYLKO dla tych, którzy wiedzą, co robią.


W przypadku konieczności migracji istniejącego (działającego) węzła Blixt do innego nowego urządzenia, bez zamykania istniejących kanałów LN, należy wykonać następujące kroki:



- Przypuszczamy, że już zapisałeś Blixt Wallet seed (24 słowa aezeed)
- Na starym urządzeniu przejdź do "Ustawienia" - sekcja debugowania - "Kompaktuj bazę danych LND". Ten krok jest opcjonalny, ale zalecany, jeśli chcesz zmniejszyć rozmiar pliku channel.db. Zwykle jest on dość duży, w zależności od aktywności węzła. Spowoduje to ponowne uruchomienie Blixt i zmniejszenie rozmiaru pliku db.
- Po ponownym uruchomieniu przejdź do "Ustawień" i zmień swój zwykły pseudonim na "Hampus". Spowoduje to aktywację ukrytych opcji, tylko dla zaawansowanych użytkowników.
- Przejdź do sekcji "Debug", a zobaczysz nową opcję "Eksportuj plik channel.db". OSTRZEŻENIE! Po wykonaniu tego eksportu istniejący węzeł Blixt LN zostanie wyłączony na tym starym urządzeniu i wyeksportuje całą bazę danych węzła (channel.db) gotową do zaimportowania do nowego urządzenia.
- Ten plik db zostanie zapisany w wyznaczonym folderze na starym urządzeniu (Dokumenty lub Pobrane) i stamtąd będzie musiał zostać przeniesiony na nowe urządzenie. Możesz użyć na przykład aplikacji [LocalSend FOSS] (https://github.com/localsend/localsend), aby przesłać plik bezpośrednio między urządzeniami.
- W tym momencie stary Blixt MUSI pozostać wyłączony. NIE OTWIERAJ GO PONOWNIE!
- Po przeniesieniu pliku channel.db na nowe urządzenie, uruchom nową instalację Blixt i wybierz "Restore Wallet" na pierwszym ekranie.
- Na przycisku z napisem "Wybierz plik SCB" należy długo nacisnąć (NIE klikać!), a następnie pojawi się opcja wyboru pliku channel.db, w którym zostanie on zapisany lokalnie w nowym urządzeniu. Jeśli po prostu naciśniesz ten przycisk, domyślnie zostanie użyty plik SCB (z zamkniętymi kanałami), nie działa to w przypadku pełnej kopii zapasowej kanałów na żywo.
- Wpisz 24 słowa seed, a następnie kliknij "Przywróć"
- Zobaczysz, że Blixt rozpocznie synchronizację z Neutrino. Możesz również oglądać dzienniki synchronizacji.
- PAMIĘTAJ! W tej fazie Blixt powinien być cały czas otwarty! Nie pozwól mu przejść w stan uśpienia ani zamknąć ekranu aplikacji. Może to zakłócić początkową synchronizację i będziesz musiał zrobić to ponownie. Poczekaj cierpliwie, nie zajmie to więcej niż kilka minut.
- Po zakończeniu początkowej synchronizacji bloków szybko przeskanuje poprzednie adresy Wallet, a następnie kanały powrócą do trybu online, żywe i zdrowe.
- Niestety nie można (jeszcze) przywrócić poprzedniej historii płatności i kontaktów. Ale to i tak nie jest takie ważne.


I ZROBIONE! Teraz masz w pełni przywrócony węzeł Blixt LN. Może działać również z innymi kopiami zapasowymi LND (Umbrel, Raspiblitz itp.), Jeśli wcześniej poprawnie zapisałeś plik channel.db. Tak więc Blixt może dosłownie uratować każdy martwy węzeł LND.


---

## Blixt - Czwarty kontakt


Ten rozdział dotyczy dostosowywania i lepszego poznania węzła Blixt. Nie będę opisywał wszystkich dostępnych funkcji, jest ich zbyt wiele i zostały już wyjaśnione na stronie [Blixt Features Page](https://blixtwallet.github.io/features).


Zwrócę jednak uwagę na niektóre z nich, które są niezbędne, aby korzystać z Blixt i mieć wspaniałe doświadczenia.


### A - Nazwa (NameDesc)


![blixt](assets/en/19.webp)


[NamDesc](https://github.com/lightning/blips/blob/master/blip-0011.md) to standard przekazywania "nazwy odbiorcy" w fakturach BOLT11.


Może to być dowolna nazwa i można ją zmienić w dowolnym momencie.


Ta opcja jest naprawdę przydatna w różnych przypadkach, gdy chcesz wysłać nazwę wraz z opisem Invoice, aby odbiorca mógł uzyskać wskazówkę, kto otrzymał te Sats. Jest to w pełni opcjonalne i również na ekranie płatności użytkownik musi zaznaczyć pole wskazujące na wysłanie nazwy aliasu.


Oto przykład tego, co pojawi się po użyciu [chat.blixtwallet.com](https://chat.blixtwallet.com/)


![blixt](assets/en/20.webp)


Jest to kolejny przykład wysyłania do innej aplikacji Wallet, która obsługuje NameDesc:


![blixt](assets/en/21.webp)


### B - Lightning Box


Począwszy od nowej wersji v0.6.9-420 [niedawno ogłoszonej] (https://github.com/hsjoberg/blixt-Wallet/releases/tag/v0.6.9-420), Blixt wprowadził nową potężną funkcję dla Lightning Address w Blixt.


Ta nowa funkcja jest opcjonalna i nie jest domyślnie włączona!


W tej chwili domyślny LN Box jest uruchamiany przez serwer Blixt i oferuje @blixtwallet.com LN Address. Ale KAŻDY z węzłem publicznym LND może uruchomić serwer Lightning Box i oferować LN Address dla własnej domeny, z własnym nadzorem.


Obecnie serwer Blixt przesyła płatności wysyłane na adresy LN @blixtwallet.com tylko do użytkowników Blixt, którzy ustawili swoje LN Address. Użytkownicy muszą ustawić swój węzeł Blixt Wallet w "trybie trwałym", aby otrzymywać te płatności na swoje adresy @blixtwallet.com LN.


Zobacz w informacjach o wydaniu demo wideo o tym, jak skonfigurować LN Address w Blixt.


Ten LN Address zaimplementowany w aplikacji Blixt Wallet jest jak czat przez LN, natychmiastowy i zabawny, obsługujący również [LUD-18](https://github.com/lnurl/luds/blob/luds/18.md) (dodawanie aliasu do płatności). Możesz dodać do listy kontaktów wszystkie swoje zwykłe adresy LN, których często używasz i mieć je pod ręką do czatowania. Teraz Blixt można uznać za pełną aplikację do czatowania LN 😂😂.


Kolejną przydatną funkcją jest pełne wsparcie dla LUD-18 (które obsługuje również [Stacker.News](https://stacker.news/r/DarthCoin) i inne).


![blixt](assets/en/22.webp)


Jak widać na powyższym zrzucie ekranu, wysyłając z konta Stacker News, ładnie wyświetliło się logo + LN Address + wiadomość. W ten sam sposób działa wysyłanie z Blixt, możesz dołączyć swój Blixt LN Address lub po prostu dodać nazwę aliasu (wcześniej ustawioną w ustawieniach Blixt) lub nawet oba.


Ta opcja z LUD-18 może być przydatna również w przypadku usług subskrypcji, w których użytkownik może wysłać określony alias (NIE jest to alias węzła ani prawdziwe imię i nazwisko!) i na tej podstawie może zostać zarejestrowany lub otrzymać określoną wiadomość zwrotną lub cokolwiek innego. Dołączenie nazwy aliasu ([LUD-18](https://github.com/lnurl/luds/blob/luds/18.md))+komentarza ([LUD-12](https://github.com/lnurl/luds/blob/luds/12.md)) do płatności LN może mieć wiele zastosowań!


Oto kod dla [Lightning Box](https://github.com/hsjoberg/lightning-box), jeśli uruchamiasz go dla siebie, rodziny i przyjaciół, na własnym węźle.


Tutaj również można uruchomić [serwer LSP Dunder](https://github.com/hsjoberg/dunder-lsp) dla mobilnych węzłów Blixt i zaoferować płynność użytkownikom Blixt, jeśli masz dobry publiczny węzeł LN (działa tylko z LND).


### C - Zapasowe kanały LN i słowa seed


To bardzo ważna funkcja!


Po otwarciu lub zamknięciu kanału LN należy wykonać kopię zapasową. Można to zrobić ręcznie, zapisując niewielki plik na urządzeniu lokalnym (zwykle w folderze pobierania) lub korzystając z konta Google Drive lub iCloud.


![blixt](assets/en/23.webp)


Przejdź do Ustawienia Blixt - sekcja Wallet. Dostępne są tam opcje zapisywania wszystkich ważnych danych dla Blixt Wallet:



- "Pokaż Mnemonic" - wyświetli 24 słowa seed, aby je zapisać
- "Remove Mnemonic from device" (Usuń Mnemonic z urządzenia) - ta opcja jest opcjonalna i należy jej użyć tylko wtedy, gdy naprawdę chcemy usunąć słowa seed z urządzenia. NIE spowoduje to wyczyszczenia Wallet, tylko seed. Ale uwaga! Nie ma możliwości ich odzyskania, jeśli nie zostały wcześniej zapisane.
- "Eksportuj kopię zapasową kanału" - ta opcja spowoduje zapisanie małego pliku na urządzeniu lokalnym, zwykle w folderze "pliki do pobrania", skąd można go pobrać i przenieść poza urządzenie w celu bezpiecznego przechowywania.
- "Weryfikuj kopię zapasową kanału" - jest to dobra opcja, jeśli korzystasz z Dysku Google lub iCloud, aby sprawdzić integralność kopii zapasowej wykonanej zdalnie.
- " Kopia zapasowa kanału dysku Google" - zapisze plik kopii zapasowej na osobistym dysku Google. Plik jest zaszyfrowany i przechowywany w oddzielnym repozytorium niż zwykłe pliki Google. Nie ma więc obaw, że może zostać odczytany przez kogokolwiek. W każdym razie ten plik jest całkowicie bezużyteczny bez słów seed, więc nikt nie może pobrać środków tylko z tego pliku.


Zalecałbym w tej sekcji następujące elementy:



- użyj menedżera haseł do bezpiecznego przechowywania seed i pliku kopii zapasowej. KeePass lub Bitwarden są do tego bardzo dobre i mogą być używane na wielu platformach i samodzielnie hostowane lub offline.
- RÓB KOPIĘ ZAPASOWĄ ZA KAŻDYM RAZEM, gdy otwierasz lub zamykasz kanał. Plik ten jest aktualizowany o informacje o kanałach. Nie ma potrzeby robienia tego po każdej transakcji wykonanej na LN. Kopia zapasowa kanału nie przechowuje tych informacji, tylko status kanału.


![blixt](assets/en/24.webp)


---

## Blixt - porady i wskazówki


### PRZYPADEK 1 - PROBLEMY Z SYNCHRONIZACJĄ


"_Mój Blixt nie synchronizuje się... Mój Blixt nie pokazuje salda... Mój Blixt nie może otwierać kanałów... Próbowałem przywrócić go na innym urządzeniu... itd."


Wszystkie te problemy zaczynają się, ponieważ URZĄDZENIE NIE JEST WŁAŚCIWIE SYNCHRONIZOWANE. Prosimy o zrozumienie tego ważnego aspektu: Blixt jest mobilnym węzłem LND, który używa Neutrino do synchronizacji / odczytu bloków.



- Oto mniej techniczne wyjaśnienie z [Bitcoin Magazine] (https://bitcoinmagazine.com/technical/why-Bitcoin-wallets-need-block-filters)
- Oto więcej zasobów technicznych z [Bitcoin Optech](https://bitcoinops.org/en/topics/compact-block-filters/)
- Oto jak można aktywować Neutrino na własnym węźle domowym i obsługiwać filtry bloków dla węzła mobilnego, z [Docs Lightning Engineering](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core)


PRZYPOMNIENIE: Używanie Neutrino przez clearnet jest całkowicie bezpieczne, twoje IP lub xpub nie wyciekną. Po prostu czytasz bloki ze zdalnego węzła za pomocą neutrino. To wszystko. Cała reszta odbywa się na urządzeniu lokalnym.


Nie ma więc potrzeby używania go z Torem. Tor doda ogromne opóźnienie do procesu synchronizacji i sprawi, że Blixt będzie bardzo niestabilny. Jeśli naprawdę chcesz korzystać z Tora, upewnij się, co robisz, miej dobre połączenie i cierpliwość. To samo dotyczy korzystania z VPN. Należy uważać, jakie opóźnienia są podawane przez VPN.


Możesz przetestować opóźnienie serwera neutrino, po prostu pingując go z komputera lub telefonu komórkowego.


![blixt](assets/en/25.webp)


Jest to zwykły ping do serwera neutrino europe.blixtwallet.com, który pokazuje, że połączenie jest bardzo dobre z czasem odpowiedzi wynoszącym średnio 50 ms i TTL wynoszącym 51. Czas odpowiedzi może się różnić, ale nie za bardzo. TTL musi być stabilny.


Jeśli wartości te są wyższe niż 100-150 ms, proces synchronizacji będzie nieaktualny lub, co gorsza, może spowodować zamknięcie kanałów przez urządzenia równorzędne! Nie ignoruj tego aspektu.


Bez prawidłowej synchronizacji nie można również zobaczyć prawidłowego balansu lub kanały LN nie będą dostępne online i nie będą działać. Nie ma znaczenia ile giga ultra terra mbps masz prędkości pobierania. Liczy się czas reakcji i TTL (time to live).


Jest to ogólny przypadek dla użytkowników z Ameryki Łacińskiej. Nie wiem, co się tam dzieje, ale macie okropne połączenie z pingami przekraczającymi 200 ms, które mogą zakłócić każdą synchronizację.


Jakie jest więc rozwiązanie dla tych zdesperowanych użytkowników?



- przestań używać Blixt z Torem. Jest całkowicie bezużyteczny
- możesz użyć VPN, ale wybierz go mądrze i cały czas monitoruj ping. Użyj takiego, który jest bliżej Twojej lokalizacji geograficznej. Odległość oznacza dłuższy czas odpowiedzi ms, pamiętaj.
- wybierz mądrze swoje serwery równorzędne neutrino, oto lista dobrze znanych publicznych serwerów neutrino:


```txt
For US region
btcd1.lnolymp.us | btcd2.lnolymp.us
btcd-mainnet.lightning.computer
swest.blixtwallet.com (Seattle)
node.eldamar.icu
noad.sathoarder.com
bb1.breez.technology | bb2.breez.technology
neutrino.shock.network
For EU region
europe.blixtwallet.com (Germany)
For Asia region
sg.lnolymp.us
asia.blixtwallet.com
```


Innym sposobem jest wybranie jednego z tej listy węzłów ogłaszających "filtry kompaktowe" (BIP157 / neutrino) - [Bitnodes Page Neutrino filter](https://bitnodes.io/nodes/?q=NODE_COMPACT_FILTERS). Wybierz ten, który znajduje się bliżej Twojej lokalizacji geograficznej.


Innym sposobem (najlepszym) jest połączenie się z lokalnym węzłem społeczności, prowadzonym przez znajomego lub grupę, która oferuje połączenie neutrino. [Tutaj znajdują się instrukcje, jak to zrobić](https://docs.lightning.engineering/lightning-network-tools/LND/enable-neutrino-mode-in-Bitcoin-core) Ich węzeł nie zostanie w żaden sposób naruszony, potrzebują tylko stabilnego i publicznego połączenia.


Potrzeba więcej serwerów neutrino w regionie LATAM, dla lepszej i szybszej synchronizacji. Dlatego prosimy o zorganizowanie się z lokalną społecznością Bitcoin i ustalenie, kto i gdzie uruchamia Bitcoin Core + Neutrino na własny użytek. Wystarczy publiczny adres IP. Jeśli nie masz dostępu do publicznego adresu IP, możesz użyć adresu IP VPS i utworzyć tunel wireguard do węzła domowego. W ten sposób przekierujesz cały ruch do lokalnego adresu IP VPS, nie ujawniając żadnych prywatnych informacji o węźle domowym.


### PRZYPADEK 2 - SYNCHRONIZACJA NIGDY SIĘ NIE KOŃCZY


"_Mój Blixt ma dobre połączenie z serwerem neutrino, ale nie synchronizuje się."


#### Serwer czasu


Czasami ludzie używają różnych starych urządzeń lub nie są prawidłowo podłączeni do serwera czasu. Neutrino synchronizuje się dobrze, dopóki nie osiągnie rzeczywistych bloków, które nie odpowiadają rzeczywistemu czasowi lokalnemu. W logach Blixt LND zobaczysz błąd mówiący, że "znacznik czasu bloku jest daleki od przyszłości" lub coś związanego z "nagłówek nie przechodzi kontroli poprawności".


Szybkie rozwiązanie: ustaw prawidłową godzinę i datę dla swojego urządzenia i uruchom ponownie Blixt.


#### Mało miejsca na urządzeniu


Czasami używając starego urządzenia, z małą ilością miejsca, może osiągnąć limit progowy i utknąć. Rzeczywiście, gdy używasz tego mobilnego węzła LND, pliki neutrino stają się większe, a także plik channel.db.


Szybkie rozwiązanie: Przejdź do Opcje Blixt - Sekcja Debug - Wybierz "zatrzymaj LND i usuń pliki neutrino". Spowoduje to ponowne uruchomienie aplikacji i rozpoczęcie nowej synchronizacji. Czasami ta szybka naprawa może również naprawić uszkodzone dane. Należy pamiętać, że pełna ponowna synchronizacja zajmie trochę czasu, od 1 do 3 minut. NIE usuwa istniejących funduszy ani kanałów, ale tak, po ponownej synchronizacji może uruchomić ponowne skanowanie adresów Bitcoin, co może zająć więcej czasu.


Następnym krokiem jest sprawdzenie, ile danych jest jeszcze zajętych. Można to sprawdzić w Android App info - data. Jeśli nadal jest większa niż 400-500 MB, można skompaktować pliki LND. Przejdź do Blixt Options - sekcja Debug - wybierz "Compact DB LND". Uruchom ponownie aplikację Blixt, jeśli nie robi tego automatycznie. Kompaktowanie odbywa się podczas uruchamiania i tylko raz. Teraz zobaczysz, że dane Blixt są mniej zajęte.


#### Tryb trwały


Czasami ludzie nie otwierają Blixt przez długi czas, więc jest o wiele za stary na synchronizację. Ale oczekują synchronizacji natychmiast po otwarciu.


Prosimy o cierpliwość i spojrzenie na górne obracające się koło. Opcjonalnie możesz przejść do Options - See Node Info i sprawdzić, czy jest zsynchronizowany z łańcuchem i zsynchronizowany z wykresem oznaczonym jako "true". Bez tej "prawdziwej" wzmianki nie można prawidłowo korzystać z Blixt, nie można poprawnie zobaczyć salda, nie można zobaczyć kanałów LN online, nie można dokonywać płatności.


Szybkie rozwiązanie: Istnieje potężna opcja "utrzymania przy życiu" węzła Blixt. Przejdź do Options - Experiments - Wybierz "Activate Persistent Mode". Spowoduje to ponowne uruchomienie Blixt i umieści usługę LND w trybie trwałym, czyli zawsze będzie aktywna i utrzyma synchronizację online, nawet jeśli przełączysz się na inną aplikację lub po prostu zamkniesz Blixt (nie wymusisz zamknięcia lub zabicia zadania). Możesz to utrzymać w ten sposób przez cały dzień, jeśli masz stabilne połączenie i musisz użyć Blixt kilka razy. Nie zużyje to zbyt wiele baterii.


### PRZYPADEK 3 - CHCĘ DOKONAĆ MIGRACJI NA INNE URZĄDZENIE


OK, o tym scenariuszu napisałem obszerny przewodnik na [stronie FAQ] (https://blixtwallet.github.io/faq#blixt-restore): z 2 opcjami, szybką (spółdzielcze zamknięcie kanałów przed migracją) i wolną (wymuś zamknięcie kanałów, ponieważ stare urządzenie jest martwe).


Chciałbym jednak powtórzyć tutaj kilka ważnych aspektów i dodać nową "tajną" procedurę.


PRZYPOMNIENIE:



- Zawsze wykonuj kopię zapasową stanu kanałów (SCB) PO każdym otwarciu lub zamknięciu kanału. Zajmuje to zaledwie kilka sekund.
- Nie zachowuj starych plików SCB, aby nie pomylić ich i nie przywrócić. Są całkowicie bezużyteczne i mogą uruchomić procedurę karną, jeśli je wykorzystasz. Zawsze używaj ostatniej wersji pliku SCB, jeśli chcesz przywrócić.
- Zapisz plik SCB (zaszyfrowany tekst z rozszerzeniem .bin) poza urządzeniem, w bezpiecznym miejscu. Możesz użyć [LocalSend](https://github.com/localsend/localsend), aby przenieść ten plik na komputer lub inne urządzenie.
- Zapisz również seed swojego Blixt Wallet w bezpiecznym miejscu, na przykład w menedżerze haseł offline / zaszyfrowanym USB.


Sekretna metoda: Jak zmigrować węzeł Blixt bez zamykania istniejących kanałów. W tym celu należy uważnie przeczytać poprzednią sekcję "Trzeci kontakt" w tym przewodniku na temat "Przywracania Wallet".


Ta procedura NIE JEST DLA NOOBÓW, jest tylko dla zaawansowanych użytkowników! Dlatego nie jest powszechnie dostępna i zalecam jej wykonanie tylko z pomocą programistów Blixt lub mojego wsparcia. Proszę nie ignoruj tej rady.


### PRZYPADEK 4 - JAKICH URZĄDZEŃ RÓWNORZĘDNYCH UŻYWAĆ DO OTWIERANIA KANAŁÓW?


Jak napisałem na stronie [Blixt guides page](https://blixtwallet.github.io/guides), istnieje wiele sposobów otwierania kanałów za pomocą tego mobilnego węzła LND. Chciałbym jednak przypomnieć kilka ważnych aspektów:



- otwarte z dobrze znanymi węzłami LSP i z potwierdzonymi przez społeczność peerami. [Zobacz listę tutaj](https://github.com/hsjoberg/blixt-Wallet/issues/1033)
- nie otwieraj z losowymi węzłami tylko Tor. Są one bezwartościowe i będziesz mieć tylko problemy z brakiem możliwości dokonywania płatności. Bez względu na to, jak dobry jest twój przyjaciel "node runner" z podejrzanym węzłem Tor w dżungli, nigdy nie da ci najlepszych tras dla mobilnego węzła prywatnego. Nie otwierasz kanałów z kimś, kto jest twoim przyjacielem. To nie Facebook! Otwierasz kanał dla: dobrych tras, niskich opłat, dostępności.
- nie ma potrzeby otwierania tony małych kanałów, 2-3 lub maksymalnie 4, ale z dużą ilością Sats. Nie otwieraj małych kanałów, są całkowicie bezużyteczne. Mniejsze niż 200k dla telefonu komórkowego nie mają większego zastosowania.
- należy pamiętać o LSP, które oferują kanały przychodzące i kanały JIT (just in time). Są one bardzo przydatne, ponieważ nie musisz używać żadnych UTXO, możesz opłacić kanał otwierający środkami, które już masz w innych portfelach LN, układając je i przygotowując na otwarcie większego kanału. Powinieneś użyć tych kanałów JIT na swoją korzyść. [Wyjaśniłem w tym przewodniku](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) więcej opcji dla peerów dla prywatnych węzłów, takich jak Blixt. Również [tutaj w tym przewodniku opublikowanym na SN](https://stacker.news/items/679242/r/DarthCoin) wyjaśniłem, jak zarządzać płynnością prywatnych węzłów mobilnych.


---

## Wnioski


OK, istnieje wiele innych niesamowitych funkcji, które oferuje Blixt, pozwolę ci odkrywać je jeden po drugim i dobrze się bawić.


Ta aplikacja jest naprawdę niedoceniana, głównie dlatego, że nie jest wspierana przez żadne fundusze VC, jest napędzana przez społeczność, zbudowana z miłością i pasją do Bitcoin i Lightning Network.


Ten mobilny węzeł LN, Blixt, jest bardzo potężnym narzędziem w rękach wielu użytkowników, jeśli wiedzą, jak go dobrze używać. Wyobraź sobie, że chodzisz po świecie z węzłem LN w kieszeni i nikt o tym nie wie.


Nie wspominając już o wszystkich innych bogatych funkcjach, które oferuje Wallet.


Tymczasem tutaj znajdują się wszystkie linki dotyczące tego niesamowitego Bitcoin Lightning Node:



- [Oficjalna strona Blixt](https://blixtwallet.com/)
- [Strona Blixt Github](https://github.com/hsjoberg/blixt-Wallet/)
- [Strona funkcji Blixt](https://blixtwallet.github.io/features) - wyjaśniająca po kolei każdą funkcję i funkcjonalność.
- [Blixt FAQ page](https://blixtwallet.github.io/faq) - Lista pytań i odpowiedzi oraz rozwiązywanie problemów z Blixt
- [Blixt Guides page](https://blixtwallet.github.io/guides) - wersje demonstracyjne, samouczki wideo, dodatkowe przewodniki i przypadki użycia dla Blixt
- Pobierz: [Android Play Store](https://play.google.com/store/apps/details?id=com.blixtwallet) | [iOS](https://testflight.apple.com/join/EXvGhRzS) | [APK direct download](https://github.com/hsjoberg/blixt-Wallet/releases)
- [Grupa Telegram dla bezpośredniego wsparcia](https://t.me/blixtwallet)
- [Twitter](https://twitter.com/BlixtWallet)
- [Strona crowdfundingowa Geyser](https://geyser.fund/project/blixt) - przekaż darowiznę Sats, jak chcesz, aby wesprzeć projekt
- [LNURL Chat Blixt](https://chat.blixtwallet.com/) - anonimowy czat LN
- [Blixt presentation - promo video](https://lightning.video/06fdf68f99e246a6ec6ba1470677b9e632faaad4aa0ca9773c38714b682a4ac1)
- [Blixt Girls Calendar](https://lightning.video/eeb744202ad3f14c18bf6d719970ebd9c53f0f13b79c94d299c6be623fba64b6) - film promocyjny (możesz przetestować swoje pierwsze użycie LN)
- [Ulotka A4 do wydrukowania z pierwszymi krokami przy użyciu Blixt, w różnych językach](https://github.com/BlixtWallet/blixtwallet.github.io/tree/master/assets/flyer).
- [Blixt oferuje również w pełni funkcjonalne demo](https://blixt-Wallet-git-master-hsjoberg.vercel.app/) bezpośrednio na swojej stronie internetowej lub w dedykowanej wersji internetowej, aby mieć pełne doświadczenie w testowaniu, zanim zaczniesz używać w prawdziwym świecie.


---
**OŚWIADCZENIE:**


*Nie jestem w żaden sposób opłacany ani wspierany przez twórców tej aplikacji. Napisałem ten przewodnik, ponieważ zauważyłem, że zainteresowanie tą aplikacją Wallet rośnie, a nowi użytkownicy wciąż nie rozumieją, jak zacząć z nią korzystać. Również, aby pomóc Hampusowi (głównemu deweloperowi) z dokumentacją dotyczącą korzystania z tego węzła Wallet.*


*Nie mam żadnego innego interesu w promowaniu tej aplikacji LN, poza forsowaniem przyjęcia Bitcoin i LN. To jedyny sposób!*


---