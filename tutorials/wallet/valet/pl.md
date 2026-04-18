---
name: Valet Bitcoin
description: Valet przenosi węzeł Lightning bez nadzoru do kieszeni użytkownika
---

![cover_valet](assets/cover.webp)



## Wprowadzenie


Valet to lekki, samoobsługowy Bitcoin i Lightning wallet, który oferuje łatwy i wygodny proces wdrażania dla początkujących. Został specjalnie dostosowany do obsługi społeczności Bitcoin i gospodarek o obiegu zamkniętym, zwłaszcza w odległych obszarach.


Jest to fork z **Simple Bitcoin Wallet (SBW)**, z zaawansowaną funkcją hostowanego kanału Lightning o nazwie **Fiat Channels**, zaprojektowaną tak, aby umożliwić każdemu akceptowanie płatności Lightning bez ryzyka zmienności.


Valet jest obecnie dostępny tylko na urządzenia z systemem Android i można go pobrać i zainstalować z kilku sklepów z aplikacjami o otwartym kodzie źródłowym. Valet nie jest jednak **hostowany** w **Google Play Store** ze względu na obawy związane z prywatnością deweloperów i KYC.



## Pobierz i zainstaluj Valet


Valet można pobrać jako plik APK ze strony Standard Sats w serwisie GitHub. [Standard Sats](https://standardsats.github.io/) to firma, która opracowała Valet.


aby pobrać Valet, odwiedź Standard Sats [stronę GitHub](https://github.com/standardsats/valet/releases) i znajdź **najnowszą** wersję (często jest to najwyższa wersja).


👉 Przejdź do **Assets** i kliknij plik z rozszerzeniem **.apk**. Pobieranie rozpocznie się automatycznie.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


po zakończeniu pobierania przejdź do **Menedżera plików** > **Pobieranych plików** i wybierz plik apk Valet.


![Select_valet_apk](assets/en/002.webp)


zainstaluj ją, a po kilku sekundach aplikacja będzie gotowa i pojawi się na ekranie głównym.


![valet_icon_on_homescreen](assets/en/003.webp)


Alternatywnie można również pobrać aplikację Valet ze sklepu z aplikacjami **F-Droid**. Jeśli nie masz aplikacji F-Droid na swoim urządzeniu, możesz ją pobrać i zainstalować [tutaj] (https://f-droid.org/en/).


na ekranie głównym otwórz F-Droid i wyszukaj **Valet**. Wybierz pierwszą opcję z **fioletowo-białą ikoną** spośród dwóch opcji, które się pojawią, i kliknij **Pobierz**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


po pobraniu kliknij **Install** i postępuj zgodnie z instrukcjami wyświetlanymi na ekranie. Po zakończeniu instalacji możesz uruchomić aplikację Valet z F-Droid, klikając **Open** lub uruchamiając ją z ekranu głównego urządzenia.



## Tworzenie Bitcoin Wallet


Możesz skonfigurować Bitcoin wallet w Valet w dwóch prostych krokach.


uruchom aplikację Valet z ekranu głównego urządzenia lub z aplikacji F-Droid. Pojawi się ekran konfiguracji wallet z dwiema opcjami: **Utwórz nowy Wallet** i **Przywróć istniejący Wallet**.


wybierz **Create New Wallet**, a natychmiast zostanie utworzony nowy wallet i nastąpi przekierowanie do strony głównej.


![set_up_a\_new_wallet](assets/en/006.webp)



## Tworzenie kopii zapasowej frazy seed


na stronie głównej wallet kliknij kartę **Green** z napisem **"Dotknij, aby zapisać frazę odzyskiwania wallet na wypadek utraty lub wymiany urządzenia "**


![seed_phrase_green_card](assets/en/007.webp)


wyświetlony zostanie zestaw 12 angielskich słów. Zapisz je na papierze w kolejności od 1 do 12 i zachowaj w bezpiecznym miejscu.


![the_seed_phrase](assets/en/008.webp)


### Uwaga ⚠️:


Zwróć uwagę na następujące elementy:


- Jak już wiesz, Valet jest samowystarczalnym wallet, więc twoja fraza seed jest jedynym dostępem do odzyskania Wallet.
- Jeśli kiedykolwiek utracisz frazę seed, **nigdy** nie uzyskasz dostępu do wallet.
- Jeśli ktoś zdobędzie frazę seed, może nieodwracalnie ukraść wszystkie Bitcoin.


Musisz więc zapisać swoją 12-wyrazową frazę seed i przechowywać ją w bezpiecznym miejscu. Nigdy nie powinieneś robić zrzutu ekranu, zapisywać go jako wersji roboczej w wiadomości e-mail ani zapisywać go na żadnym urządzeniu elektronicznym, które kiedykolwiek było podłączone do Internetu.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Odbieranie i wysyłanie Bitcoin na Valet


Valet jest samowystarczalnym wallet z możliwością on-chain i Lightning Bitcoin. Oznacza to, że można odbierać i wysyłać Bitcoin z Valet za pośrednictwem **On-chain** lub **Lightning Network**.


Aby jednak móc odbierać lub wysyłać Bitcoin za pośrednictwem Lightning, należy skonfigurować kanał Lightning przy użyciu on-chain Bitcoin jako Liquidity. Można też zakupić płynność kanału Lightning od sprzedawców.



## Generowanie łańcucha Bitcoin Address


Aby otrzymywać Bitcoin przez on-chain, należy wygenerować adres Bitcoin.


na stronie głównej wallet zobaczysz **pomarańczową** i **fioletową kartę**, odpowiednio oznaczone jako **Bitcoin** i **Lightning**.


kliknij pomarańczową kartę oznaczoną **Bitcoin**. Nastąpi przekierowanie do ekranu wyświetlającego adres Bitcoin.


![click_on_Bitcoin_card](assets/en/009.webp)


możesz **skopiować** adres i wysłać go do osoby, która wysyła do Ciebie Bitcoin, lub kliknąć przycisk **udostępnij**, aby wysłać kod QR do tej osoby za pośrednictwem mediów społecznościowych lub innych kanałów komunikacji.


możesz także kliknąć przycisk **Edytuj**, aby ustawić ilość Bitcoin, które mają zostać wysłane na ten adres.


**Uwaga:** Podobnie jak w przypadku faktur, funkcja edycji przydaje się w scenariuszach, w których możesz chcieć otrzymać określoną ilość Bitcoin na adres w danym momencie; nie oznacza to jednak, że adres nie może otrzymać wyższych lub niższych kwot.


kliknij na **Więcej świeżych adresów**, aby wygenerować nowe losowe adresy.


![generating_a\_bitcoin_add](assets/en/010.webp)


możesz również wygenerować adres on-chain Bitcoin, klikając przycisk **Odbierz** na dole strony głównej wallet. Następnie wybierz **Odbierz na adres bitcoin** i kontynuuj ten sam proces powyżej.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Wysyłanie Bitcoin przez On-chain


Wysyłanie Bitcoin z Valet wallet przez on-chain jest prostym zadaniem.


na dole strony głównej wallet kliknij przycisk **Wyślij**, wprowadź adres Bitcoin lub kliknij **Skanuj**, aby zeskanować kod QR adresu, a następnie kliknij **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


wprowadź kwotę Bitcoin, którą chcesz wysłać. Możesz ręcznie wprowadzić kwotę w Sats lub w walucie fiat lub kliknąć **Max**, aby wykorzystać całe saldo on-chain.


możesz również dostosować opłaty, które chcesz zapłacić za transakcję, klikając małe zielone pole oznaczone **opłata**, a następnie przesuwając białą kropkę w prawo lub w lewo, aby odpowiednio zwiększyć lub zmniejszyć opłaty. Kliknij **Ok**, aby wysłać transakcję.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Konfiguracja kanału Lightning Network


Jak wspomniano powyżej, Valet jest samowystarczalnym Bitcoin i Lightning wallet; w związku z tym, aby móc wysyłać i odbierać Bitcoin za pośrednictwem sieci Lightning, należy najpierw skonfigurować kanał Lightning, wykonując następujące kroki:


na ekranie głównym kliknij **fioletową kartę** oznaczoną **Piorun**. Zostaniesz przeniesiony na stronę z następującymi opcjami:



- Skanowanie węzła QR
- Zakup na LNBIG.COM
- Zakup na BITREFILL.COM
- Żądanie resynchronizacji wykresu LN.


Po wybraniu **Zakup z lnbig.com** lub **Zakup z bitrefill.com**, zostaniesz przekierowany na strony internetowe tych firm, gdzie możesz zakupić płynność przychodzącą o kilku pojemnościach. Zignoruj na razie ostatnią opcję **Request LN graph resync**.


Naszym wyborem jest więc **Scan a Node QR**. W tym momencie musisz zdecydować i uzyskać **kod QR** węzła, do którego chcesz otworzyć kanał. Możesz otwierać kanały do dowolnego wybranego węzła publicznego. Sprawdź [1ML](https://1ml.com/) lub [Amboss](https://amboss.space/), wybierz dowolny węzeł publiczny i zeskanuj powiązany kod QR wybranego węzła.


![channel_opening_options](assets/en/016.webp)


nastąpi automatyczne przekierowanie do następnej strony, na której należy sfinansować kanał. Ponownie, samodzielne korzystanie z sieci Lightning wymaga użycia Bitcoin do sfinansowania kanału. Oznacza to, że musisz mieć Bitcoin w on-chain wallet, za pomocą których możesz sfinansować kanał Lightning. Więcej informacji na temat sieci Lightning można znaleźć w tym artykule autorstwa [Hacken](https://hacken.io/discover/lightning-network/).


![fund_channel](assets/en/017.webp)


wprowadź **kwotę** Bitcoin, którymi chcesz zasilić kanał, lub kliknij **Max**, aby wykorzystać całe saldo on-chain Bitcoin. Możesz dostosować **opłatę** lub pozostawić domyślne ustawienie opłaty i kliknąć **Ok**.


**Uwaga:** Kwota, którą zasilisz kanał, będzie przepustowością twojego nowego kanału (tj. całkowity wolumen Sats, który może być przedmiotem transakcji do i z tego kanału)


Ważne jest również, aby użyć ponad **100 000 Sats** jako kwoty finansowania podczas otwierania kanału. Wynika to z faktu, że wiele węzłów Lightning wymaga co najmniej 100 000 Sats, aby otworzyć do nich kanał. Tak więc, aby uniknąć prób i błędów, po prostu użyj kwot wyższych niż ten zakres.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


w tym momencie, gdy sprawdzisz stronę główną wallet, zobaczysz, że kwota finansowania została przeniesiona z **karty Bitcoin** na **kartę Lightning**. W historii transakcji zobaczysz, że transakcja finansowania jest przetwarzana.


![channel_funding_processing](assets/en/020.webp)


jeśli klikniesz kartę Lightning, zobaczysz informacje wskazujące, że Twój kanał Lightning jest otwarty. Na liście transakcji pojawi się również **transakcja finansowania kanału**. Poczekaj, aż transakcja finansowania zostanie potwierdzona na blockchain, a Twój kanał Lightning będzie gotowy.


![channel_opening](assets/en/021.webp)


gdy tylko transakcja finansowania zostanie potwierdzona, kliknij **kartę Lightning** na stronie głównej, a zobaczysz następujące informacje o swoim kanale Lightning:



- RANDOMOWY ZESTAW LICZB ODDZIELONYCH KROPKAMI:** Są to adresy IP węzłów. (odpowiednio IPV4 i IPV6)
- CAPACITY:** Jest to całkowita objętość Sats, która może być wysyłana i odbierana przez ten kanał
- MOŻNA WYSŁAĆ:** Jest to ilość Sats, którą można wysłać w tym momencie. Zauważysz, że jest to prawie taka sama liczba jak **Pojemność**. Wynika to z faktu, że nie wysłałeś żadnych płatności za pośrednictwem kanału.
- CAN RECEIVE:** Jest to liczba Sats, które można obecnie odebrać na tym kanale. (W tym momencie będzie to niewiele lub nic, ponieważ aby móc odbierać, musisz najpierw wysłać Sats, aby utworzyć przychodzący Liquidity)
- REFUNDABLE:** Wyświetla kwotę, która zostanie zwrócona na adres on-chain po zamknięciu kanału. Jest to również określane jako **lokalne saldo kanału**. Zauważ, że jest ona nieco mniejsza niż pojemność kanału, a to dlatego, że podczas zamykania kanału musisz uiścić opłatę za opublikowanie transakcji zamknięcia na blockchain, tak jak to zrobiłeś podczas finansowania kanału. Tak więc system odliczył przybliżoną najniższą kwotę, jaką zapłacisz)
- VALUE IN FLIGHT:** Gdy ktoś wysyła sats na twój kanał lub gdy próbujesz wysłać sats do kogoś i z jakiegokolwiek powodu transakcja jest opóźniona, często jest to wyświetlane w tym polu.


![channel_info](assets/en/022.webp)


## Wysyłanie Sats przez swój kanał


Wysyłanie Sats przez Lightning Network jest prostym zadaniem.


na dole strony głównej kliknij **Wyślij** i **wklej** fakturę Lightning (musisz ją skopiować) w odpowiednim polu lub kliknij **Skanuj**, aby zeskanować kod QR faktury Lightning.


![click_send_or_scan](assets/en/023.webp)


Większość faktur Lightning zawiera wstępnie wprowadzoną kwotę do zapłaty. Jednak w kilku przypadkach może to być faktura otwarta, w której należy wpisać kwotę.


wprowadź kwotę w **dolarach** lub **Sats** lub kliknij **Max**, aby wykorzystać całe saldo na kanale Lightning, a następnie kliknij **Ok**. Gdy tylko zostanie znaleziona dobra ścieżka, płatność zostanie wysłana i zakończona w ciągu kilku sekund. Obserwuj stronę główną, aby sprawdzić, czy płatność została zakończona. Po jej zakończeniu pojawi się zielony znacznik wyboru.


![enter_the_amount](assets/en/024.webp)


## Odbieranie Sats przez kanał użytkownika


Otrzymywanie płatności na kanale Lightning w dużej mierze zależy od tego, czy masz przychodzącą Liquidity, czy nie. Po otwarciu kanału nie będziesz mógł otrzymywać płatności, dopóki nie wyślesz przynajmniej Sats, aby **utworzyć płynność przychodzącą** na drugim końcu połączenia kanału. Aby potwierdzić, czy możesz otrzymywać Sats i ile Sats możesz otrzymać, sprawdź pole **Możesz otrzymywać** w informacjach o kanale. Pokaże to, ile Sats otrzymujesz w każdym momencie.


Załóżmy teraz, że wysłałeś Sats ze swojego kanału, masz teraz płynność przychodzącą i możesz odbierać Sats.


Aby odbierać w kanale Lightning, należy wygenerować fakturę. W przeciwieństwie do Bitcoin on-chain, który używa adresów, sieć Lightning używa faktur. Istnieją dwie drogi do wygenerowania faktury w Valet.


#### OPCJA 1


na dole strony głównej kliknij **Odbierz**, wybierz **Odbierz do faktury Lightning**. Wypełnij kwotę do otrzymania na fakturze i kliknij **Ok**. Skopiuj fakturę lub udostępnij kod QR płatnikowi.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPCJA 2


kliknij fioletową kartę Lightning na stronie głównej wallet. Stuknij w dowolnym miejscu na swoim kanale, a pojawi się lista opcji. Wybierz **Odbierz na kanał** i wprowadź kwotę, którą otrzymujesz (w Sats lub dolarach). Zobaczysz również, ile Sats możesz otrzymać (pojemność przychodząca) podczas wypełniania faktury. Kliknij **Ok** i skopiuj fakturę lub udostępnij kod QR płatnikowi.


![receive_to_channel](assets/en/028.webp)


**Uwaga:** Pierwsza opcja jest opcją uniwersalną, co oznacza, że jeśli masz więcej niż jeden aktywny kanał i użyjesz pierwszej opcji, system automatycznie wybierze jeden z Twoich kanałów do odbioru Sats.


Tak więc w tym scenariuszu druga opcja jest najlepsza, jeśli chcesz odbierać Sats na określonym kanale.


### Objaśnienie opcji wyskakujących okienek kanału


Po dotknięciu kanału wyświetlone zostaną następujące pola opcji:


![channel_pop_ups](assets/en/029.webp)


**SHARE LIGHTNING CHANNEL DETAILS:** Umożliwia udostępnianie szczegółów kanału, takich jak zdalny identyfikator peera, lokalny identyfikator kanału, transakcja finansowania, data utworzenia itp.


**ZAMKNIJ KANAŁ DO PORTFELA:** Możesz zamknąć swój kanał lightning w dowolnym momencie. Aby zamknąć kanał, system sprawdza saldo Bitcoin, które masz po swojej stronie kanału (pamiętaj o polu **"Can Send "**, znanym również jako saldo lokalne) i wysyła je z powrotem do ciebie. W Valet możesz wybrać, gdzie chcesz wysłać Bitcoin po zamknięciu kanału. Tak więc, **Zamknij kanał do wallet** jest jedną z dwóch opcji.


kliknij tę opcję i wybierz **Bitcoin**. Rozpocznie się zamykanie kanału, a saldo kanału Bitcoin zostanie przesłane z powrotem na adres on-chain kanału wallet.


![close_channel_to_wallet](assets/en/030.webp)


**ZAMKNIJ KANAŁ DO ADDRESS:** Jest to druga opcja zamknięcia kanału. Po wybraniu tej opcji zostanie wyświetlony monit o wprowadzenie adresu wallet, na który zostanie wysłane saldo Bitcoin na kanale. Pamiętaj, że w tej opcji możesz zeskanować tylko kod QR adresu Bitcoin, na który chcesz zamknąć kanał. Obecnie nie ma opcji ręcznego wklejenia adresu.


kliknij tę opcję, zeskanuj adres Bitcoin i kliknij przycisk **Ok**. Rozpocznie się zamykanie kanału, a saldo Lightning Bitcoin zostanie wysłane na zeskanowany adres.


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL:** Jest to to samo, co generowanie faktury, ale w niektórych przypadkach możesz mieć więcej niż jeden kanał, w tym kanały Fiat (unikalny rodzaj kanału Lightning dostępny w Valet wallet). Tak więc, jeśli masz otwartych wiele kanałów, ta opcja zapewnia możliwość otrzymania płatności na określony kanał.


** UZUPEŁNIANIE Z INNYCH KANAŁÓW:** Ta opcja umożliwia uzupełnianie jednego kanału z innych istniejących kanałów. Na przykład, jeśli masz 2 różne kanały Lightning (A i B), a saldo Bitcoin na kanale A wyczerpało się, dzięki tej opcji możesz łatwo i automatycznie uzupełnić saldo kanału A z kanału B.


**DIRECT NOT PRIVATE RECEIVE:** Jest to również opcja generowania faktury w celu otrzymania płatności, ale gdy korzystasz z tej opcji, nadawca płaci Ci bezpośrednio. Oznacza to, że płatność nie przeskakuje przez różne węzły, zanim dotrze do użytkownika, jak ma to miejsce w przypadku zwykłej płatności Lightning. Zasadniczo nadawca wie, że to Ty zapłaciłeś, zna Twój identyfikator kanału itp. Ta opcja może być często używana, gdy otrzymujesz płatność z zaufanego źródła i nie musisz zachować prywatności.


## Kanały hostowane i Fiat


Podobnie jak wiele innych Bitcoin wallet, Valet jest prostym, lekkim Bitcoin i Lightning wallet. Posiada jednak unikalną funkcję Lightning, która odróżnia go od większości innych Bitcoin wallet. Funkcja ta nazywa się **Hosted and Fiat Channels**.


Kanały Fiat to rodzaj implementacji Lightning, która umożliwia łatwe wdrażanie i korzystanie z sieci Lightning. Jest to rozwiązanie powiernicze, które zapewnia pełną anonimowość, podobnie jak w przypadku zwykłego kanału Lightning. Technologia kanałów Fiat umożliwia również tworzenie instrumentów pochodnych Bitcoin w sieci Lightning. Przykładem jest to, że dzięki kanałom Fiat sprzedawcy mogą akceptować płatności Bitcoin o stabilnej wartości, nie martwiąc się o zmienność Bitcoin.


Obecna implementacja kanałów Fiata w Valet umożliwia tworzenie stabilnych syntetycznych walut Fiata wspieranych przez Sats. Wykorzystuje relację host-klient, w której hostem jest dowolny węzeł Lightning oferujący tę usługę, a klientem jest użytkownik Valet. Jest to rozwiązanie powiernicze, ponieważ wszystkie Sats znajdują się po stronie hosta; jednak generowanie faktur, routing tor i generowanie obrazów wstępnych nadal odbywa się po stronie klienta, tak jak w normalnym kanale Lightning.


Otwarcie kanału Fiat odbywa się w taki sam sposób, jak otwarcie kanału Lightning. Jedyną istotną różnicą jest to, że w tym przypadku klient (użytkownik Valet) nie musi angażować żadnej płynności on-chain w celu utworzenia pojemności kanału. Host ustawia pojemność kanału i kieruje wszystkie płatności dla klienta.


aby otworzyć kanał Fiata, kliknij fioletową **kartę Lightning** na stronie głównej wallet. Wybierz **Scan Node QR** (W tym momencie musisz zidentyfikować hosta, do którego chcesz otworzyć kanał i uzyskać QR węzła). Przykładem węzła hosta, do którego można otworzyć kanał Fiata, jest węzeł SATM w standardzie Sats)


**Uwaga:** Ważne jest, aby pamiętać, że każdy może być hostem. Wystarczy uruchomić węzeł Lightning z wtyczką **Fiat channel** i usługą **Hedging**. Kanały Fiat to projekt open-source autorstwa *Standard Sats*. Przeczytaj więcej na ten temat [tutaj](https://github.com/standardsats/fiat-channels-rfc) i [tutaj](https://standardsats.github.io/).


Węzeł SATM QR poniżej:


![SATM_node_QR](assets/en/032.webp)


po zeskanowaniu QR węzła kliknij na **Request USD fiat channel** lub **Request EUR fiat channels** (jest to nominał fiat, w którym będą kwotowane Twoje salda fiat). Na razie wybierz USD i kliknij **OK**. Kanał zostanie otwarty automatycznie i możesz od razu zacząć otrzymywać Sats. To takie proste!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Przejdź do strony głównej wallet, zobaczysz **jasnozieloną** kartę oznaczoną **USD**, która jest Twoim **kanałem Fiata**.


![fiat_channel_card](assets/en/035.webp)


**Uwaga:** Po otrzymaniu Sats na kanale fiat, wartość fiat otrzymanego Sats zostanie zablokowana jako stabilne saldo, podczas gdy wolumen Sats zmienia się wraz z ceną Bitcoin. Rozwiązanie to zostało zaprojektowane głównie dla sprzedawców, którzy chcą akceptować Sats do płatności, ale nie chcą stawić czoła wyzwaniom związanym ze zmiennością Bitcoin. Pomaga im to utrzymać stabilną wartość przez cały czas, jednocześnie będąc w stanie dokonywać transakcji w sieci Lightning, ciesząc się globalnym zasięgiem i szybkim rozliczeniem Bitcoin jako środka wymiany na Lightning Network.


Po utworzeniu kanału Fiat wyświetlane są następujące pola wartości i ich znaczenie:


![fiat_channel_info](assets/en/036.webp)



- RANDOMOWY ZESTAW LICZB ODDZIELONYCH KROPKAMI:** Są to adresy IP węzłów. (odpowiednio IPV4 i IPV6)
- CENA SERWERA:** Jest to cena rynkowa Bitcoin, po której host oferuje ci usługi. Często będzie się ona nieznacznie różnić od dominującej ceny rynkowej, ponieważ Host może dodać niewielką premię. Decyzja o tej stawce należy wyłącznie do hosta; dlatego też będzie się ona różnić w zależności od hosta.
- SALDO FIAT:** Jest to zablokowana stabilna wartość fiat każdego sat otrzymanego na tym kanale. Pamiętaj, jak wyjaśniono wcześniej, za każdym razem, gdy otrzymasz Sats na swoim kanale Fiat, wartość fiat Sats w momencie otrzymania jest natychmiast blokowana jako syntetyczna stabilna wartość fiat w tym polu. Wartość **balansu fiat** nie zmienia się wraz z ceną rynkową Bitcoin. Za każdym razem, gdy chcesz dokonać płatności z tego kanału, możesz wysłać tylko równowartość Sats tego salda fiat. Potraktuj to jako cyfrową walutę fiat wspieraną przez Sats.
- CAPACITY:** Jest to całkowita ilość Sats, która może być wysyłana i odbierana przez ten kanał. (Jest ona również ustawiana przez hosta. W przeciwieństwie do zwykłego kanału Lightning, pojemność ta może być regulowana przez hosta w zależności od przypadku)
- MOŻNA WYSŁAĆ:** Jest to ilość Sats, którą można wysłać w każdym punkcie w oparciu o saldo fiat. Jest to całkowicie odmienne od tego, co masz w normalnym kanale Lightning, ponieważ wartość ta zmienia się wraz z ceną Bitcoin. Dlatego to, co tutaj widzisz, to wartość Sats twojego salda Fiata w dowolnym momencie w oparciu o **Server Rate**.
- CAN RECEIVE:** Jest to liczba Sats, które można obecnie odebrać na tym kanale. Po utworzeniu kanału wartość ta powinna być taka sama jak pojemność kanału.
- VALUE IN FLIGHT:** Gdy ktoś wysyła sats na twój kanał lub gdy próbujesz wysłać sats do kogoś i z jakiegokolwiek powodu transakcja jest opóźniona, często jest to wyświetlane w tym polu.


Oto ważne informacje na temat kanałów Fiata:



- W przeciwieństwie do zwykłego kanału Lightning, po otwarciu kanału fiat można natychmiast rozpocząć odbieranie Sats, ale nie można wysyłać. Możesz wysłać Sats dopiero po otrzymaniu Sats.
- Przez cały czas aktywem wysyłanym do i z jest Sats. Saldo *Fiat Balance* jest tylko syntetyczną reprezentacją IOU wartości Bitcoin otrzymanej w dowolnym momencie. Nie jest to więc kreacja token ani nowa kryptowaluta.
- Kanał Fiat jest przydatny głównie dla sprzedawców/przedsiębiorców, którzy sceptycznie podchodzą do akceptowania płatności Bitcoin ze względu na obawy dotyczące zmienności. Może być również przydatny dla firm, które chcą wypłacać wynagrodzenia swoim pracownikom w Bitcoin bez ponoszenia konsekwencji zmienności Bitcoin, która może sprawić, że ich kapitał płacowy będzie niestabilny. Może być również przydatny dla osób, które mieszkają na obszarze o dominującym wykorzystaniu Bitcoin, ale mają stałe koszty utrzymania.
- Zauważ, że nie ma pola oznaczonego jako **REFUNDABLE**. Dzieje się tak dlatego, że z technicznego punktu widzenia nie można zamknąć kanału Fiata. Możesz przestać korzystać z kanału Fiat tylko poprzez przeniesienie jego salda do normalnego kanału Lightning.


### Wyjaśnienie opcji wyskakujących okienek kanału Fiata


Po dotknięciu kanału Fiat Lightning wyświetlone zostaną następujące pola:


![fiat_channel_pop_up](assets/en/037.webp)


**SHARE HOSTED CHANNEL DETAILS:** Umożliwia udostępnianie szczegółów kanału Fiat, takich jak identyfikator zdalnego urządzenia równorzędnego, identyfikator kanału lokalnego, data utworzenia itp.


**EKSPORTUJ STAN KANAŁU:** Umożliwia wyeksportowanie stanu kanału w dowolnym momencie. Jest to zwykle przydatne przy naprawianiu błędów kanału, a host może poprosić o udostępnienie tego, jeśli zajdzie taka potrzeba.


**OPRÓŻNIJ SALDO KANAŁU:** Jak wspomniano wcześniej, nie można technicznie zamknąć kanału Fiat, ale można opróżnić saldo kanału do istniejącego normalnego kanału Lightning. Spowoduje to automatyczne przeniesienie równowartości salda fiat do normalnego kanału Lightning.


**RECEIVE TO CHANNEL:** Jest to to samo, co generowanie faktury, ale w niektórych przypadkach użytkownik może mieć więcej niż jeden kanał Fiat z różnymi hostami, w tym zwykłe kanały Lightning. Tak więc, jeśli użytkownik ma otwartych wiele kanałów, ta opcja zapewnia, że może otrzymać płatność na określony kanał.


** UZUPEŁNIANIE Z INNYCH KANAŁÓW:** Ta opcja umożliwia użytkownikowi uzupełnienie jednego kanału z innych istniejących kanałów. Tak więc, dzięki tej opcji, możesz uzupełnić swój kanał Fiata z normalnego kanału lub innych kanałów Fiata, które posiadasz, w taki sam sposób, w jaki możesz opróżnić.


**DIRECT NOT PRIVATE RECEIVE:** Jest to również opcja generowania faktury w celu otrzymania płatności, ale gdy używasz tej opcji, nadawca płaci ci bezpośrednio. Oznacza to, że płatność nie przechodzi przez różne węzły, zanim dotrze do użytkownika. Zasadniczo nadawca wie, że to ty zapłaciłeś, zna twój identyfikator kanału itp. Ta opcja może być często używana, gdy otrzymujesz płatność z zaufanego źródła i nie musisz zachować prywatności.


## Ustawienia Valet:


Jak każda inna aplikacja, Valet ma ustawienia, które można dostosować do własnych upodobań. Dostęp do strony ustawień można uzyskać z ekranu głównego.


na ekranie głównym kliknij ikonę **Gear** znajdującą się w prawym górnym rogu ekranu, aby uzyskać dostęp do ustawień. Poniżej znajdują się elementy w sekcji ustawień.


![settings_icon](assets/en/038.webp)


**BACKUP KANAŁÓW LOKALNYCH JEST WŁĄCZONY:** Jeśli opcja ta jest **Wyłączona**, należy ją włączyć, ponieważ jest to jedyny sposób na odzyskanie normalnych kanałów Lightning po odinstalowaniu i ponownym zainstalowaniu Valet. Wyjaśnimy to później. Kliknij więc na to i daj Valetowi uprawnienia do **media storage**, ponieważ to tam zapisywany jest plik kopii zapasowej.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


**GDZIE PRZECHOWYWAĆ LOKALNĄ KOPIĘ ZAPASOWĄ:** Tak długo, jak dałeś Valet uprawnienia do swojej pamięci masowej, to pole zostanie automatycznie ustawione na przechowywanie lokalnych kopii zapasowych w folderze **Downloads**. Można to jednak zmienić, klikając tutaj i wybierając dowolny folder.


**MANAGE CHAIN WALLETS** Jest to trochę techniczne i nie musisz się tym przejmować, chyba że jesteś wystarczająco doświadczony. Domyślne ustawienie jest w porządku.


**ADD HARDWARE WALLET:** Nie powinieneś zawracać sobie tym głowy, chyba że masz sprzętowy wallet, który chcesz podłączyć i monitorować. Dzięki temu ustawieniu można skanować i podłączać sprzętowy wallet, taki jak Trezor lub karta Cold, i monitorować jego aktywność. Jest to funkcja tylko do obserwacji, co oznacza, że nie można z tego miejsca wykonywać transakcji na sprzętowym wallet. Można jedynie obserwować i monitorować działania wallet, salda itp.


**USTAWIENIE WŁASNEGO WĘZŁA ELECTRUM:** Jest to również kwestia techniczna i jeśli nie masz wystarczającej wiedzy, nie powinieneś zawracać sobie tym głowy. Domyślne ustawienie jest wystarczająco dobre.


**JEDNOSTKI BITCOIN:** Jest to sposób wyświetlania salda Bitcoin. Pierwsza opcja wyświetla saldo w jednostkach Satoshi, np. 1,000,000 Sats, podczas gdy druga opcja wyświetla je w jednostkach dziesiętnych BTC, np. 0.01BTC


**UŻYWAJ AUTENTYFIKACJI PIN** Jeśli zaznaczysz to pole, będziesz musiał skonfigurować kod PIN lub odcisk palca, który musisz wprowadzić, aby zalogować się do wallet i uwierzytelnić transakcje.


**UŻYWAJ POŁĄCZENIA TOR:** Jeśli zaznaczysz to pole, Twoje transakcje będą kierowane przez sieć Tor. Dodaje to dodatkową warstwę prywatności, ale może powodować opóźnienia w przepustowości płatności, szczególnie w przypadku płatności Lightning.


**W tym miejscu można uzyskać dostęp do 12-wyrazowej frazy seed w celu utworzenia kopii zapasowej. Jeśli więc nie zapisałeś go wcześniej lub nie możesz znaleźć miejsca, w którym go zapisałeś, o ile nadal masz dostęp do Wallet, możesz go skopiować z tego miejsca.


**STATYSTYKI UŻYTKOWANIA:** Pokazuje podsumowanie wszystkich transakcji i działań od momentu utworzenia wallet


![usage_stats](assets/en/041.webp)


## Odzyskiwanie Wallet


Valet to wallet bez nadzoru, więc jeśli zgubisz urządzenie lub odinstalujesz aplikację wallet, będziesz musiał wykonać odzyskiwanie wallet, aby odzyskać Bitcoin i kanały Lightning. Na początku tego samouczka wspomnieliśmy o znaczeniu zapisania **12-wyrazowej frazy seed**, ponieważ jest to klucz do odzyskania wallet. Nie ma przedstawicieli obsługi klienta, którzy mogą pomóc w odzyskaniu wallet.


Istnieją dwa ważne narzędzia potrzebne do odzyskania Valet wallet, w zależności od tego, czy miałeś aktywny kanał Lightning, czy nie. W przypadku użytkownika, który nie miał aktywnego normalnego kanału Lightning, wystarczy jego **12-słowna fraza seed**, wykonując proste czynności opisane poniżej:


zainstaluj nową aplikację Valet i uruchom ją.


wybierz **Przywróć istniejący Wallet**


![restore_existing_wallet](assets/en/042.webp)


wybierz **Tylko fraza odzyskiwania**.


![select_recovery_phrase](assets/en/043.webp)


wprowadź 12-wyrazową frazę odzyskiwania i kliknij przycisk **OK**.


![input_12_words](assets/en/044.webp)


Saldo wallet zostanie odzyskane. W takim przypadku przywrócone zostanie tylko saldo on-chain Bitcoin.


Jeśli jednak miałeś aktywny normalny kanał Błyskawicy i odzyskasz wallet tylko za pomocą frazy odzyskiwania, twój kanał Błyskawicy zostanie siłą zamknięty, a wszelkie posiadane na nim saldo Bitcoin zostanie automatycznie przesłane do twojego salda on-chain.


Innym sposobem na odzyskanie Valet wallet, zwłaszcza jeśli miałeś otwarty normalny kanał Lightning przed odinstalowaniem Valet, jest **użycie lokalnego pliku kopii zapasowej zapisanego na urządzeniu wraz z 12-słowową frazą seed**. Jeśli użyjesz tych dwóch, stan kanału Lightning zostanie przywrócony, a zatem kanał Lightning nie zostanie zamknięty na siłę.


Oto kroki:


zainstaluj nową aplikację Valet i uruchom ją.


wybierz **Przywróć istniejący Wallet**.


wybierz **Backup + Recovery phrase**.


![select_backup_and_recovery_seed](assets/en/045.webp)


wybierz plik kopii zapasowej z menedżera plików telefonu. (Domyślnie jest on zawsze przechowywany w folderze **Downloads**)


![local_backup_file_in_download_folder](assets/en/046.webp)


Po wybraniu prawidłowego pliku kopii zapasowej zostanie wyświetlony monit potwierdzający, że **"plik kopii zapasowej jest obecny "**, a następnie zostaniesz poproszony o wprowadzenie 12-wyrazowej frazy seed.


![enter_12_words](assets/en/047.webp)


wprowadź 12-wyrazową frazę odzyskiwania i kliknij przycisk **OK**. Nastąpi przejście do strony głównej wallet.


poczekaj na zakończenie synchronizacji sieci Bitcoin (**SYNC**) i synchronizacji węzła Lightning (**LN Sync**), a wallet zostanie w pełni przywrócony, w tym kanały Lightning.


![LN_sync](assets/en/048.webp)


## Wnioski


Valet to ekscytujące rozwiązanie wallet z funkcjami, które sprawiają, że nadaje się do wdrażania nowych użytkowników. Posiada również kanał Fiat, nie tak nową technologię, która zapewnia integrację firm zarządzanych przez fiat w standardzie Bitcoin.


Pobierz Valet już dziś i wypróbuj go!!! 🧡