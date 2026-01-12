---
name: Jade DIY
description: Przekształć płytkę deweloperską za 15 USD we w pełni funkcjonalny sprzęt Bitcoin wallet
---

![cover](assets/cover.webp)


## Bitcoin Hardware Wallet - Zestaw dla początkujących


**Odbiorcy:** Ciekawi konstruktorzy z niewielkim lub zerowym doświadczeniem w zakresie systemów wbudowanych.


**Czas trwania:** 2 godziny (elastycznie)


**Rezultaty:** Do końca kursu uczniowie będą:



- Rozpoznanie modelu bezpieczeństwa portfeli sprzętowych DIY w porównaniu z urządzeniami komercyjnymi.
- Montaż urządzenia podpisującego opartego na mikrokontrolerze.
- Flashowanie oprogramowania układowego typu open source i weryfikacja sumy kontrolnej kompilacji.
- Podpisz i wyślij transakcję mainnet za pomocą nowego urządzenia.


---

## Streszczenie


Ten 2-godzinny warsztat uczy początkujących, jak zbudować funkcjonalny sprzęt Bitcoin wallet poprzez flashowanie oprogramowania układowego Jade o otwartym kodzie źródłowym na płytce LilyGO T-Display za 15 USD. Studenci przekształcają ogólny sprzęt programistyczny w urządzenie do podpisywania porównywalne z komercyjnymi portfelami kosztującymi 150 USD, ucząc się podstaw bezpieczeństwa poprzez praktyczne doświadczenie, a nie samą teorię.


### Filozofia


Zbudowanie własnego urządzenia podpisującego to nie tylko oszczędność pieniędzy - to zrozumienie technologii chroniącej Bitcoin. Ten warsztat obejmuje "bezpieczeństwo poprzez zrozumienie", a nie zaufanie do czarnej skrzynki. Pozyskując komponenty, flashując oprogramowanie układowe typu open source i samodzielnie generując entropię, uczniowie zmniejszają ryzyko związane z łańcuchem dostaw, jednocześnie ucząc się krytycznej oceny roszczeń dotyczących bezpieczeństwa. Celem jest świadoma autonomia: uczniowie powinni rozumieć zarówno moc, jak i ograniczenia swojego urządzenia DIY w porównaniu do wzmocnionych alternatyw komercyjnych.


---

## Elementarz koncepcji (15 min)


### Co to jest samoubezpieczenie i dlaczego ma znaczenie?


Bitcoin został stworzony, aby usunąć z naszego systemu pieniężnego potrzebę istnienia zaufanych stron trzecich, takich jak banki i korporacje. Zamiast zaufania, bitcoin wykorzystuje matematykę, fizykę i kryptografię, aby umożliwić każdemu posiadanie i kontrolowanie swoich pieniędzy bez konieczności uzyskiwania niczyjej zgody.


Sposób, w jaki to działa, polega na tym, że bitcoin istnieje w globalnej księdze cyfrowej zwanej blockchain lub bitcoin timechain, która jest publiczną i przejrzystą księgą prowadzoną przez komputery, zamiast scentralizowanej księgi, takiej jak konto bankowe.


Ważną rzeczą do zrozumienia jest to, że aby przenieść bitcoiny z jednego miejsca do drugiego, musisz podpisać tę transakcję za pomocą tak zwanego klucza prywatnego. Można to porównać do odblokowania skarbca za pomocą hasła i przeniesienia bitcoinów do skarbca innej osoby. Bitcoin daje ci możliwość samodzielnego posiadania kluczy do tego skarbca, zamiast polegać na banku, który przeniesie twoje pieniądze za ciebie.


Z wielką władzą wiąże się wielka odpowiedzialność - zgub klucze, a twoje fundusze przepadną na zawsze. W ten sposób można myśleć o kluczach do skarbca jak o samych pieniądzach. Choć klucze to nie to samo co bitcoiny, stanowią one mechanizm przenoszenia środków i dlatego ich ochrona jest niezwykle ważna. Dlatego mówimy "nie klucze, nie monety".


Termin self-custody może wydawać się mylący, ale oznacza on jedynie posiadanie własnych kluczy prywatnych i kontrolowanie własnych bitcoinów. Jeśli nie posiadasz tego klucza, powierzasz go komuś innemu. Jeśli twój bitcoin znajduje się w ETF lub na giełdzie (Mt. Gox, FTX, Coinbase, Binance itp.), nie jesteś właścicielem bitcoina, ale posiadasz roszczenie do bitcoina. Wprowadza to wszelkiego rodzaju ryzyko, takie jak włamania na giełdy i utrata bitcoinów lub firmy pożyczające pieniądze i dające tylko ułamek rezerwy. Ponadto zaufane strony trzecie miałyby pełną kontrolę nad Twoimi pieniędzmi i mogłyby ograniczyć lub zamrozić wypłaty.


![image](assets/fr/01.webp)


Samodzielne przechowywanie środków eliminuje zaufanie z równania. Nikt nie może zamrozić twoich środków ani odmówić transakcji, możesz wysyłać pieniądze za granicę, do każdego, w dowolnym momencie i nie potrzebujesz konta bankowego, dowodu osobistego ani niczyjej zgody. Nikt nie może cię zatrzymać, ocenzurować ani okraść, odblokowując pełną moc bitcoina jako pieniądza wolności. Dlatego mówimy, że dzięki bitcoinowi możesz być swoim własnym bankiem.


Bitcoin został stworzony, aby rozwiązać problem manipulacji zaufaniem i pieniędzmi, wyjście z naszego obecnego systemu, ale wyjście działa tylko wtedy, gdy weźmiesz klucze. Dlatego tak ważna jest samoopieka.


### Co to jest Wallet?


Termin wallet jest nieco mylący i dlatego może być mylący. Tak, to prawda, że bitcoin wallet, podobnie jak fizyczny wallet, przechowuje wartość. Główna różnica polega jednak na tym, że portfele bitcoin nie przechowują żadnych bitcoinów.


Bitcoin istnieje tylko jako wpis w publicznej księdze blockchain lub w metaforycznych skarbcach w cyberprzestrzeni. Pamiętaj, że aby przenieść bitcoiny, musisz użyć swoich kluczy, aby odblokować skarbiec i przenieść monety w inne miejsce, klucze prywatne są tym, co jest używane do wydawania bitcoinów. Kiedy dokonujesz transakcji za pomocą wallet, tak naprawdę używasz swoich kluczy do podpisania transakcji. W ten sposób pokazujesz dowód, że jesteś właścicielem pieniędzy i masz prawo do wydawania tych monet.


Portfele Bitcoin tak naprawdę przechowują tylko klucze prywatne, więc bardziej trafne byłoby nazwanie ich pękami kluczy.


### Portfele Hot vs Cold


Hot wallet to aplikacja na telefonie lub komputerze. Jest ona połączona z Internetem, więc jest łatwiejsza w użyciu i szybsza do podpisywania transakcji, ale oznacza to również, że jest bardziej narażona na ataki hakerów, złośliwe oprogramowanie i phishing. Nazywa się go "gorącym", ponieważ jest podłączony do Internetu, jest podłączony i włączony. Przykładem może być telefon wallet lub przeglądarka wallet.


Z drugiej strony zimny wallet lub sprzętowy wallet to urządzenie, które tworzy i przechowuje klucz offline. Eliminuje to możliwość włamania się do twoich środków i jest znacznie bezpieczniejsze dla długoterminowych oszczędności, jednak jest to urządzenie potrzebne do podpisania każdej transakcji i może być mniej wygodne.


### Model zagrożenia Hardware Wallet


Portfele sprzętowe istnieją po to, aby rozwiązać podstawowy problem: w jaki sposób podpisywać transakcje Bitcoin bez narażania swoich kluczy prywatnych na działanie komputera podłączonego do Internetu, który może zostać zaatakowany przez złośliwe oprogramowanie lub zdalnych napastników? Podstawowy model zagrożeń zakłada, że twój codzienny laptop lub telefon jest potencjalnie wrogi. Sprzętowy wallet tworzy odizolowane środowisko, w którym klucze prywatne nigdy nie opuszczają urządzenia, a podpisywanie transakcji odbywa się w secure element lub mikrokontrolerze, który przekazuje tylko podpis z powrotem do komputera hosta, a nie sam klucz. Nawet jeśli komputer jest całkowicie zagrożony, atakujący nie może ukraść Bitcoin bez fizycznego dostępu do urządzenia i kodu PIN.


Portfele sprzętowe wprowadzają jednak własne zagrożenia. Musisz ufać, że producent nie wprowadził backdoorów, łańcuch dostaw nie został naruszony, a generowanie liczb losowych jest naprawdę losowe. Osoby atakujące fizycznie mogą wyodrębnić klucze poprzez ataki bocznymi kanałami lub manipulację chipem, a ktoś z tymczasowym dostępem może zmodyfikować urządzenie. Zbudowanie własnego sprzętowego wallet pomaga zrozumieć te kompromisy - będziesz podejmować decyzje dotyczące bezpiecznych elementów w porównaniu z mikrokontrolerami ogólnego przeznaczenia, jak weryfikować transakcje na wyświetlaczu i jak chronić się zarówno przed zagrożeniami zdalnymi, jak i fizycznymi. Celem nie jest doskonałe bezpieczeństwo, ale zrozumienie, przed którymi zagrożeniami chronisz, a które pozostają.


### Kluczowe koncepcje



- Entropia i frazy seed:** Twój wallet jest tak bezpieczny, jak losowość, która go zrodziła. Zmieszamy generator liczb losowych urządzenia z przyjaznymi dla człowieka sztuczkami, takimi jak rzuty kostką, przekształcimy tę entropię w 12- lub 24-słowną [frazę BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) i opuścimy pokój z pisemną lub metalową kopią zapasową, której ufasz.
- Higiena fraz nasiennych:** Traktuj seed jak główne klucze do swoich oszczędności. Nigdy nie wpisuj tych słów w telefonie lub komputerze - keyloggery, zrzuty ekranu i kopie zapasowe w chmurze mogą wyciec na zawsze. Zachowaj frazę offline, przechowuj ją w miejscu, do którego tylko ty masz dostęp i ćwicz czytanie jej na głos przed wyjściem.
- Bezpieczny element + mikrokontroler:** Potraktuj secure element jako skarbiec, a mikrokontroler jako mózg. secure element strzeże kluczy prywatnych z odpornością na manipulacje, podczas gdy mikrokontroler obsługuje ekran, przyciski i logikę oprogramowania układowego. Należy zauważyć, że portfele sprzętowe, które budujemy dzisiaj, nie mają secure element. Nie oznacza to, że są one niezabezpieczone, a jedynie, że mają o jeden poziom ochrony mniej.
- Zaufanie do firmware:** Firmware jest niewidzialnym systemem operacyjnym wallet. Zawsze pobieraj z oznaczonych wydań, sprawdzaj opublikowany hash i zrozum, że odtwarzalne kompilacje pozwalają wielu osobom skompilować ten sam kod i uzyskać dokładnie ten sam plik binarny. Jeśli suma kontrolna się nie zgadza, nie podpisujesz.


---

## Co budujemy?


Bierzemy ogólny sprzęt, LilyGo T-Display, i flashujemy na nim oprogramowanie Jade SDK. Jade Plus](https://blockstream.com/jade/jade-plus/) to wallet o otwartym kodzie źródłowym, który zwykle kosztuje 150 USD:


![image](assets/fr/02.webp)


Dziś zamiast tego będziemy flashować ich oprogramowanie układowe na sprzęcie za 15 USD.


### Co kupić


![image](assets/fr/03.webp)



- LilyGO T-Display (16MB z obudową, model K164)** - [Zamów bezpośrednio w LilyGO](https://lilygo.cc/products/t-display?srsltid=AfmBOornob5U3FzZifuSwBBOdeXKcdPDqkYEnAVYKBLdzl0BPyNglGBR) za około 15 USD. Ta płytka ESP32 zapewnia wyświetlacz, przyciski i interfejs USB, które odzwierciedlają Jade Plus firmy Blockstream. Na pokładzie ESP32 znajdują się również radia Wi-Fi i Bluetooth; dostarczymy oprogramowanie układowe, które utrzymuje je wyłączone, ale kształtują one model zagrożenia, ponieważ złośliwy kod może je ponownie włączyć.
- Kabel USB-C** - weź ze sobą kabel obsługujący dane, abyś mógł flashować oprogramowanie układowe i zasilać płytkę bezpośrednio z laptopa (całkowicie w porządku do użytku w klasie).


### Dlaczego warto zbudować własny Hardware Wallet?



- Oszczędność około 135 USD w porównaniu z zakupem urządzenia komercyjnego.
- Zbuduj komfort dzięki flashowaniu oprogramowania układowego, bezpiecznym elementom i higienie wallet.
- Uruchom dodatkowe urządzenia podpisujące, aby rozłożyć oszczędności na wiele portfeli.
- Zmniejsz ryzyko związane z łańcuchem dostaw, samodzielnie pozyskując i montując każdy komponent.
- Należy pamiętać o mantrze Loppa: suwerenność i wygoda są zawsze sprzeczne.


## Konfiguracja fizyczna


### Przygotowanie sprawy


Istnieją dwie opcje obudowy tablicy LilyGO T-Display: obudowa drukowana w 3D lub oficjalna obudowa LilyGO. Drukowaną obudowę można znaleźć i wydrukować ze strony [this model](https://www.printables.com/model/119144-lilygo-ttgo-t-display-enclosure). Oferuje ona lekką i konfigurowalną obudowę dla urządzenia.


![image](assets/fr/04.webp)


Alternatywnie można użyć oficjalnego etui LilyGO, które zapewnia nieco inne dopasowanie i wykończenie, oferując solidniejszą ochronę i dopracowany wygląd.


![image](assets/fr/05.webp)


Należy pamiętać, że drukowane i oficjalne obudowy różnią się nieznacznie konstrukcją i montażem. Niezależnie od wybranej opcji, upewnij się, że płyta jest prawidłowo umieszczona wewnątrz obudowy, aby uniknąć luźnych połączeń lub uszkodzeń.


### Kontrola płyty


Przed przystąpieniem do dalszych czynności należy dokładnie sprawdzić płytę LilyGO T-Display pod kątem widocznych wad lub zanieczyszczeń. Sprawdź, czy wyświetlacz, przyciski i port USB-C są czyste i wolne od kurzu lub rozprysków lutowia. Ostrożnie obchodź się z płytą i przestrzegaj zasad bezpieczeństwa dotyczących wyładowań elektrostatycznych (ESD), uziemiając się lub używając paska na nadgarstek ESD, aby zapobiec uszkodzeniu wrażliwych komponentów.


### Połączenie z laptopem


Za pomocą kabla USB-C z obsługą danych podłącz płytkę LilyGO do laptopa. To połączenie zapewni zasilanie i umożliwi flashowanie oprogramowania układowego.


Po uruchomieniu zostanie wyświetlony następujący ekran:


![image](assets/fr/06.webp)



Po włączeniu zasilania LilyGO wyświetli kolorowy ekran testowy przechodzący przez stałe kolory. Potwierdza to prawidłowe działanie wyświetlacza i karty przed flashowaniem oprogramowania sprzętowego.


Po zakończeniu testu kolorów ekran przejdzie do stanu domyślnego, wskazując, że płyta jest gotowa do kolejnych kroków w procesie kompilacji.


![image](assets/fr/07.webp)


## Łatwy sposób lub sposób Hard


Istnieją dwa główne podejścia do flashowania oprogramowania sprzętowego wallet: łatwy i trudny sposób. Łatwy sposób wykorzystuje wstępnie skonfigurowane narzędzia lub flashery internetowe, które automatycznie ładują oprogramowanie sprzętowe do urządzenia przy minimalnym wkładzie. Ta metoda jest idealna dla początkujących, którzy chcą szybko wygrać lub wolą uniknąć złożoności debugowania i interakcji z wierszem poleceń. Upraszcza ona proces i pozwala na szybsze rozpoczęcie pracy, czyniąc go dostępnym dla osób dopiero rozpoczynających przygodę z programowaniem wbudowanym lub portfelami sprzętowymi.


Z drugiej strony, trudny sposób polega na ręcznym użyciu narzędzi wiersza poleceń do flashowania oprogramowania układowego. Podejście to wymaga weryfikacji podpisów oprogramowania układowego i sum kontrolnych w celu zapewnienia autentyczności i integralności, dając głębsze zrozumienie procesu flashowania i interakcji oprogramowania układowego ze sprzętem. Chociaż wymaga to więcej wysiłku i znajomości poleceń terminala, oferuje większą kontrolę, przejrzystość i pewność co do bezpieczeństwa urządzenia.


Każda metoda ma swoje kompromisy: łatwy sposób poświęca pewien stopień zaufania i zrozumienia na rzecz szybkości i wygody, podczas gdy trudny sposób wymaga więcej czasu i umiejętności technicznych, ale nagradza cię elastycznością i lepszym zrozumieniem podstawowej technologii. Instruktorzy powinni zachęcać uczniów do wyboru ścieżki, która najlepiej odpowiada ich poziomowi komfortu i ciekawości, wspierając zarówno pewność siebie, jak i eksplorację.


## Prosty sposób


Najprostszy sposób na flashowanie ESP32



- Przejdź do oficjalnego Blockstream Github: [https://github.com/Blockstream/jadediyflasher](https://github.com/Blockstream/jadediyflasher)


![image](assets/fr/08.webp)



- Możesz pobrać plik źródłowy i uruchomić stronę lokalnie, ale GitHub już ją hostuje pod adresem [https://blockstream.github.io/jadediyflasher/](https://blockstream.github.io/jadediyflasher/). GitHub serwuje HTML, CSS, JavaScript itp. bezpośrednio do przeglądarki, dzięki czemu można flashować urządzenie bez instalowania narzędzi programistycznych.


![image](assets/fr/09.webp)



- Otwórz menu rozwijane (prawdopodobnie domyślnie jest to `M5Stack Core2`) i wybierz swoją płytkę rozwojową - dla tej klasy wybierz `LILYGO T-Display`.


![image](assets/fr/10.webp)



- Po kliknięciu flash pojawi się ten komunikat. Aby dowiedzieć się, które urządzenie to LILYGO, odłącz je i podłącz ponownie. Port COM lilygo pojawi się i zniknie. Kliknij port COM, do którego podłączone jest urządzenie Jade


![image](assets/fr/11.webp)



- Powinien pojawić się pasek postępu, a po jego zakończeniu będzie można przystąpić do konfiguracji


## Konfiguracja Jade Wallet


Po pomyślnym sflashowaniu oprogramowania sprzętowego, wyświetlacz LilyGO T-Display jest teraz w pełni funkcjonalnym sprzętem Jade wallet. Ta sekcja przeprowadzi Cię przez początkowy proces konfiguracji, od wygenerowania frazy seed do podłączenia urządzenia za pomocą oprogramowania wallet, takiego jak Sparrow lub aplikacja mobilna Blockstream Green.


### Początkowy rozruch i konfiguracja urządzenia



- Włącz urządzenie:** Gdy LilyGO jest nadal podłączone do laptopa przez USB-C, oprogramowanie układowe Jade powinno uruchomić się automatycznie. Na wyświetlaczu pojawi się logo Jade.



- Wejdź w tryb konfiguracji:** Urządzenie wyświetli menu początkowe. Do nawigacji służą dwa fizyczne przyciski na płycie:
 - Lewy przycisk:** Przesuwanie w górę/w tył
 - Prawy przycisk:** Przejście w dół/do przodu
 - Oba przyciski jednocześnie:** Wybór/potwierdzenie



- Wybierz "Setup":** Przejdź do opcji Setup i naciśnij oba przyciski, aby potwierdzić. Urządzenie przeprowadzi użytkownika przez proces wstępnej konfiguracji.


### Tworzenie Wallet



- Wybierz "Begin Setup":** Urządzenie wyświetli monit o rozpoczęcie procesu tworzenia wallet. Potwierdź swój wybór.



- Wybierz "Utwórz nowy Wallet":** Zostaną wyświetlone dwie opcje:
 - Create New Wallet:** Generuje nową frazę seed (wybierz ją dla warsztatu)
 - Przywróć Wallet:** Odzyskaj istniejący wallet z frazy seed (dla zaawansowanych użytkowników)



- Wybierz "Utwórz nowy Wallet" i potwierdź.



- Generowanie entropii:** Urządzenie użyje generatora liczb losowych do utworzenia entropii kryptograficznej. Proces ten trwa kilka sekund, ponieważ urządzenie zbiera losowość z wielu źródeł.


### Nagrywanie frazy seed



- Zapisz swoją frazę seed:** Urządzenie wyświetli teraz 12-wyrazową frazę BIP39 seed, po jednym słowie na raz. Jest to najważniejszy krok w całym procesie.


**Ważne praktyki bezpieczeństwa:**


- Zapisz każde słowo wyraźnie na papierze (użyj dostarczonych kart seed, jeśli są dostępne)
- Dokładnie sprawdzaj każde słowo podczas pisania
- Nigdy nie fotografuj frazy seed telefonem
- Nigdy nie wpisuj tych słów na żadnym komputerze ani telefonie
- Zachowaj swoją frazę seed jako prywatną - nie udostępniaj ekranu ani nie pokazuj go innym



- Weryfikacja frazy seed:** Po zapisaniu wszystkich 12 słów urządzenie poprosi o potwierdzenie kilku słów z frazy, aby upewnić się, że zostały one poprawnie zapisane. Użyj przycisków, aby wybrać prawidłowe słowo dla każdego monitu.


**Wskazówka dla profesjonalistów:** Zanim przejdziesz dalej, poćwicz odczytywanie frazy seed do siebie na głos (po cichu, aby inni nie słyszeli). Pomoże to wychwycić wszelkie błędy lub niejasności.


### Metoda połączenia



- Wybierz typ połączenia:** Oprogramowanie układowe Jade obsługuje dwie metody połączenia:
 - USB:** Połączenie przewodowe za pomocą kabla USB-C (zalecane dla tego warsztatu)
 - Bluetooth:** Bezprzewodowe połączenie z urządzeniami mobilnymi



- Na razie wybierz **USB**, ponieważ jest to najprostsza opcja dla oprogramowania wallet na komputery stacjonarne i nie wprowadza wektorów ataków bezprzewodowych.



- Nazewnictwo urządzeń:** Jade wyświetli unikalny identyfikator, taki jak "Connect Jade A7D924". Ten identyfikator pomaga rozróżnić wiele portfeli sprzętowych, jeśli w końcu zbudujesz więcej niż jeden. W razie potrzeby należy zanotować ten identyfikator.


### Łączenie z oprogramowaniem Wallet


Masz teraz dwie główne opcje łączenia się z nowo utworzonym sprzętem wallet: aplikacja mobilna Blockstream Green (do użytku w podróży) lub Sparrow Wallet (do użytku na komputerze z bardziej zaawansowanymi funkcjami). W tym warsztacie skupimy się na Sparrow Wallet, ponieważ oferuje on lepszy wgląd w szczegóły techniczne transakcji Bitcoin.


#### Opcja 1: Aplikacja mobilna Blockstream Green (szybki start)


Jeśli chcesz szybko przetestować swoje urządzenie za pomocą urządzenia mobilnego:



- Pobierz aplikację **Blockstream Green** ze sklepu App Store (iOS) lub Google Play (Android)
- Otwórz aplikację i wybierz "Połącz Hardware Wallet"
- Wybierz "Jade" z listy obsługiwanych urządzeń
- Podłącz urządzenie Jade do telefonu za pomocą kabla USB-C na USB-C (lub przejściówki USB-C na Lightning dla iPhone'a 15+)
- Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie, aby połączyć się i utworzyć swój pierwszy wallet


**Uwaga dotycząca Liquid:** Aplikacja Blockstream Green obsługuje zarówno Bitcoin, jak i Liquid (łańcuch boczny Bitcoin). Jeśli korzystasz z funkcji Liquid, możesz zostać poproszony o "Eksportowanie głównego klucza zaślepiającego" - pozwala to aplikacji zobaczyć kwoty transakcji w sieci Liquid, które w przeciwnym razie są poufne. W tym warsztacie można pominąć funkcje Liquid i skupić się na standardowych transakcjach Bitcoin.


#### Opcja 2: Sparrow Wallet (zalecane dla warsztatów)


Sparrow Wallet to potężna aplikacja komputerowa, która zapewnia szczegółową kontrolę nad transakcjami Bitcoin i płynnie łączy się ze sprzętem Jade wallet.


**Instalacja:**



- Pobierz Sparrow Wallet z oficjalnej strony internetowej: [sparrowwallet.com](https://sparrowwallet.com)
- Zweryfikuj podpis pobierania (szczegółowe informacje można znaleźć w dokumentacji Sparrow)
- Zainstaluj i uruchom aplikację


**Podłączenie Jade do Sparrow:**



- W Sparrow przejdź do **Plik → Nowy Wallet**
- Nadaj swojemu wallet nazwę (np. "My Jade Wallet")
- Kliknij **Podłączony Hardware Wallet**
- Sparrow powinien automatycznie wykryć podłączone urządzenie Jade
- Jeśli pojawi się monit, potwierdź połączenie na wyświetlaczu Jade, naciskając oba przyciski
- Wybierz żądany typ skryptu:
 - Native Segwit (P2WPKH):** Zalecany dla początkujących - najniższe opłaty, najszersza kompatybilność z nowoczesnymi portfelami
 - Zagnieżdżony Segwit (P2SH-P2WPKH):** Dla kompatybilności ze starszymi usługami
 - Taproot (P2TR):** Najbardziej zaawansowany, oferuje najlepszą prywatność i najniższe opłaty, ale wymaga najnowocześniejszej obsługi wallet
- Kliknij **Import Keystore**, aby zakończyć połączenie


**Konfiguracja połączenia serwera Sparrow:**


Zanim będziesz mógł zobaczyć swoje saldo lub transmitować transakcje, Sparrow musi połączyć się z węzłem Bitcoin, aby pobrać dane blockchain. Masz kilka opcji, z których każda ma różne kompromisy między wygodą, prywatnością i zaufaniem:



- Publiczny Electrum Server (najłatwiejszy, najmniej prywatny):** Łączy się z publicznym serwerem obsługiwanym przez stronę trzecią. Szybka konfiguracja, ale serwer może zobaczyć adresy wallet i potencjalnie połączyć je z Twoim adresem IP. Dobre do testowania w sieci testowej.
 - W Sparrow przejdź do **Narzędzia → Preferencje → Serwer**
 - Wybierz **Serwer publiczny** i wybierz serwer z listy
 - Kliknij **Testuj połączenie**, aby zweryfikować



- Węzeł Bitcoin Core lub Knots (najbardziej prywatny, najwięcej pracy):** Uruchom własny pełny węzeł Bitcoin. Jest to złoty standard w zakresie prywatności i weryfikacji, ponieważ sam weryfikujesz każdą transakcję i nie ufasz serwerowi innej osoby. Wymaga to jednak pobrania całego łańcucha bloków (~600 GB) i utrzymywania synchronizacji węzła.
 - Instalacja i synchronizacja Bitcoin Core lub węzłów
 - W Sparrow przejdź do **Narzędzia → Preferencje → Serwer**
 - Wybierz **Bitcoin Core lub Knots** i wprowadź szczegóły połączenia węzła



- Prywatny Electrum Server (dobra równowaga):** Hostuj własny serwer Electrum (jak Fulcrum lub Electrs) podłączony do węzła Bitcoin Core lub Knots. Oferuje pełną prywatność bez konieczności uruchamiania Sparrow na tej samej maszynie co węzeł.
 - Skonfiguruj serwer Electrum wskazujący węzeł Bitcoin Core lub Knots
 - W Sparrow przejdź do **Narzędzia → Preferencje → Serwer**
 - Wybierz **Private Electrum** i wprowadź adres URL swojego serwera


W przypadku tego warsztatu korzystanie z **Publicznego Electrum Server** jest całkowicie w porządku dla transakcji w sieci testowej. W środowisku produkcyjnym z prawdziwymi środkami warto rozważyć uruchomienie własnego węzła lub użycie zaufanego serwera prywatnego w celu zapewnienia maksymalnej prywatności.


#### Opcja 3: Aplikacja Blockstream Green Desktop (szybki start)


Blockstream Green to oprogramowanie do ukończenia konfiguracji JadeDIY i musi być w wersji desktopowej



- Pobierz oficjalną aplikację Blockstream - link do niej znajduje się na ich stronie internetowej. Po wejściu na stronę kliknij [Pobierz teraz](https://blockstream.com/app/).


![image](assets/fr/12.webp)



- W zależności od miejsca pobierania, najprawdopodobniej plik będzie znajdował się w folderze Pobrane. Sprawdź go i kliknij dwukrotnie plik wykonywalny, aby zainstalować oprogramowanie.


![image](assets/fr/13.webp)



- Do uruchomienia instalatora może być konieczne nadanie uprawnień administratora. Gdy to zrobisz, pojawi się okno, które powinno wyglądać jak na poniższym obrazku - kliknij **Next**.


![image](assets/fr/14.webp)



- Wybierz miejsce, w którym ma znajdować się zainstalowana aplikacja (lokalizacja wraz z innymi programami lub w łatwym do znalezienia miejscu), a następnie kliknij przycisk **Next**.


![image](assets/fr/15.webp)



- Instalator zapyta o nazwę skrótu. Wprowadź ją lub zachowaj domyślną, a następnie kliknij **Next**.


![image](assets/fr/16.webp)



- Jeśli chcesz utworzyć skrót na pulpicie, zaznacz to pole; w przeciwnym razie kliknij **Next**.


![image](assets/fr/17.webp)



- Na koniec kliknij **Install** i poczekaj kilka minut na zakończenie instalacji.


![image](assets/fr/18.webp)



- Pasek postępu powinien wypełnić się do końca.


![image](assets/fr/19.webp)



- Po zakończeniu pojawi się nowa strona - kliknij **Finish**.


![image](assets/fr/20.webp)



- Znajdź nowo zainstalowaną aplikację Blockstream (przykład pokazany w menu Start systemu Windows 11).


![image](assets/fr/21.webp)



- Po jej znalezieniu kliknij, aby ją uruchomić - powinien pojawić się ekran powitalny.


### Weryfikacja konfiguracji


Po połączeniu z Sparrow (lub inną aplikacją wallet):



- Sprawdź swoje adresy:** Sparrow wyświetli adresy odbiorcze pochodzące z frazy seed. Możesz zweryfikować adres na urządzeniu Jade, przechodząc do zakładki "Odbierz" w Sparrow i klikając "Wyświetl Address" - adres powinien pojawić się zarówno na ekranie komputera, jak i na wyświetlaczu Jade.



- Wygeneruj adres odbiorczy:** Kliknij zakładkę **Odbierz** w Sparrow i skopiuj swój pierwszy adres odbiorczy Bitcoin.



- Gotowy do transakcji:** Twój sprzęt wallet jest teraz w pełni skonfigurowany i gotowy do odbierania i podpisywania transakcji Bitcoin. Przejdź do następnej sekcji, aby przećwiczyć podpisywanie transakcji testnet.



---

### Lista kontrolna szybkiej konfiguracji



- Oprogramowanie układowe Jade uruchamia się pomyślnie
- Nowy wallet utworzony z 12-wyrazową frazą seed
- Wyraźnie zapisana i zweryfikowana fraza seed
- Wybrany tryb połączenia USB
- Zainstalowane i podłączone oprogramowanie Wallet (Sparrow)
- Skonfigurowane połączenie z serwerem (publiczny Electrum dla mainnet)
- Pierwszy adres odbiorczy wygenerowany i zweryfikowany na urządzeniu



---

**Licencja MIT**


**Copyright (c) 2025 The Bitcoin Network NYC**


Niniejszym udziela się bezpłatnego zezwolenia każdej osobie, która uzyskała kopię tego oprogramowania i powiązanych plików dokumentacji ("Oprogramowanie"), na nieograniczone korzystanie z Oprogramowania, w tym bez ograniczeń praw do używania, kopiowania, modyfikowania, łączenia, publikowania, rozpowszechniania, sublicencjonowania i/lub sprzedaży kopii Oprogramowania, a także zezwalania na to osobom, którym Oprogramowanie zostało dostarczone, z zastrzeżeniem następujących warunków:


Powyższa informacja o prawach autorskich i niniejsza informacja o zezwoleniu będą zawarte we wszystkich kopiach lub istotnych częściach Oprogramowania.


OPROGRAMOWANIE JEST DOSTARCZANE W STANIE, W JAKIM SIĘ ZNAJDUJE, BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ LUB DOROZUMIANEJ, W TYM MIĘDZY INNYMI GWARANCJI PRZYDATNOŚCI HANDLOWEJ, PRZYDATNOŚCI DO OKREŚLONEGO CELU I NIENARUSZANIA PRAW. W ŻADNYM WYPADKU AUTORZY ANI WŁAŚCICIELE PRAW AUTORSKICH NIE PONOSZĄ ODPOWIEDZIALNOŚCI ZA JAKIEKOLWIEK ROSZCZENIA, SZKODY LUB INNĄ ODPOWIEDZIALNOŚĆ, CZY TO W RAMACH UMOWY, CZYNU NIEDOZWOLONEGO LUB W INNY SPOSÓB, WYNIKAJĄCĄ Z OPROGRAMOWANIA, JEGO UŻYTKOWANIA LUB INNYCH TRANSAKCJI Z NIM ZWIĄZANYCH.


---