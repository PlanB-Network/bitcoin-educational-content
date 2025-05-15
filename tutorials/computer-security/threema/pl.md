---
name: Threema
description: Bezpieczne, anonimowe wiadomości błyskawiczne
---
![cover](assets/cover.webp)



Założona w 2012 roku w Szwajcarii, Threema jest komunikatorem internetowym zaprojektowanym w celu zagwarantowania prywatności i bezpieczeństwa. W przeciwieństwie do WhatsApp, Telegram czy Signal, Threema nie wymaga numeru telefonu ani adresu e-mail Address do utworzenia konta. Każdy użytkownik posiada unikalny identyfikator, umożliwiający całkowicie anonimową rejestrację.



Od strony technicznej komunikacja za pośrednictwem Threema jest szyfrowana od końca do końca. Kod aplikacji mobilnej jest open source od 2020 roku, ale infrastruktura serwerowa pozostaje zastrzeżona i scentralizowana. Serwery są hostowane wyłącznie w Szwajcarii (kraju słynącym z ram prawnych w zakresie ochrony danych).



![Image](assets/fr/01.webp)



Threema posiada podstawowe klienty dla systemów Android i iOS. Istnieje również aplikacja internetowa, a także oprogramowanie dostępne dla systemów Windows, Linux i macOS. Aby z nich skorzystać, należy jednak najpierw zarejestrować się na urządzeniu mobilnym.



Aplikacja Threema nie jest darmowa. Działa w modelu jednorazowego zakupu: 5,99 euro za dożywotnie korzystanie z aplikacji (lub 4,99 euro, jeśli kupisz ją bezpośrednio). Aby naprawdę anonimowo korzystać z Threema, płatności również muszą być anonimowe. Dlatego też można kupić klucz aktywacyjny w bitcoinach lub gotówce w "*Threema Shop*", aby aktywować wersję na Androida. Z drugiej strony, na iOS zakup musi odbyć się za pośrednictwem App Store, ze względu na ograniczenia Apple dotyczące monetyzacji aplikacji.



Istnieje również dedykowana wersja biznesowa o nazwie "*Threema Work*". W tym poradniku skupimy się na wersji domowej.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| **Threema**          | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| Olvid                | **✅**          | **✅**          | **✅**               | **✅**                      | **❌**                       | **❌**                | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = szyfrowanie typu end-to-end*



## Zainstaluj aplikację Threema



Threema jest dostępna na wszystkich platformach. Aplikację można pobrać bezpośrednio ze sklepu z aplikacjami na telefonie:




- [Google Play](https://play.google.com/store/apps/details?id=ch.threema.app);
- [F-Cold](https://f-droid.org/en/packages/ch.threema.app.libre/);
- [Huawei AppGallery](https://appgallery.huawei.com/#/app/C103713829);
- [App Store](https://apps.apple.com/us/app/threema-the-secure-messenger/id578665578).



W systemie Android możliwa jest również [instalacja przez APK] (https://shop.threema.ch/en/download).



Istnieją również [wersje komputerowe](https://threema.ch/download) (MacOS, Linux i Windows). Ten samouczek pokaże, jak je zsynchronizować.



## Kup licencję Threema



Po zainstalowaniu aplikacji, jeśli przeszedłeś bezpośrednio przez sklep z aplikacjami, zapłaciłeś już za licencję i powinieneś mieć do niej natychmiastowy dostęp. Jeśli przeszedłeś przez F-Droid lub APK, musisz teraz kupić licencję na oficjalnej stronie internetowej.



[Przejdź do "*Threema Shop*" (https://shop.threema.ch/) i kliknij przycisk "*Buy Threema for Android*".



![Image](assets/fr/02.webp)



Wybierz liczbę licencji, które chcesz kupić (tylko jedną, jeśli jest tylko dla Ciebie), wybierz walutę i wybierz metodę dostawy licencji. Możesz wybrać otrzymanie licencji pocztą elektroniczną lub bezpośrednio na stronie, jeśli chcesz pozostać anonimowy. Następnie kliknij "*Przejdź do płatności*".



![Image](assets/fr/03.webp)



Wybierz metodę płatności. W moim przypadku zamierzam zapłacić bitcoinami, co również polecam, ponieważ pozwala to zachować anonimowość (pod warunkiem odpowiedniego korzystania z Bitcoin) i jest znacznie wygodniejsze niż zdalna płatność gotówką. Następnie kliknij "*Next*".



![Image](assets/fr/04.webp)



Jeśli nie potrzebujesz Invoice, kliknij ponownie "*Next*" bez wprowadzania jakichkolwiek danych osobowych.



Następnie potwierdź zakup, klikając "*Potwierdź płatność*".



![Image](assets/fr/05.webp)



Następnie musisz wysłać wskazaną kwotę na Bitcoin Address (niestety, Lightning nie jest jeszcze obsługiwany). Po potwierdzeniu transakcji na Blockchain, kliknij "*Zamknij*" obok Invoice.



Następnie uzyskasz dostęp do klucza licencyjnego. Uwaga: jeśli nie wprowadziłeś adresu e-mail Address, klucz ten zostanie wyświetlony tylko tutaj. Pamiętaj, aby zapisać adres URL strony, aby w razie potrzeby móc uzyskać do niej dostęp później.



![Image](assets/fr/06.webp)



## Utwórz konto na Threema



Teraz, gdy masz już klucz licencyjny, możesz wreszcie uruchomić aplikację. Przy pierwszym uruchomieniu, jeśli nie zakupiłeś Threema za pośrednictwem sklepu z aplikacjami, zostaniesz poproszony o wprowadzenie klucza licencyjnego zakupionego na stronie.



![Image](assets/fr/07.webp)



Następnie kliknij przycisk "*Set up now*".



![Image](assets/fr/08.webp)



Przesuń palcem po ekranie, aby generate źródło entropii, potrzebne do stworzenia "*Threema ID*".



![Image](assets/fr/09.webp)



Zostanie wyświetlony Twój "*Threema ID*". Umożliwi on kontakt z innymi użytkownikami. Kliknij na "*Next*".



![Image](assets/fr/10.webp)



Wybierz hasło. Umożliwi ono przywrócenie dostępu do konta w razie potrzeby. Hasło powinno być możliwie jak najdłuższe i losowe, a jego kopia powinna być przechowywana w bezpiecznym miejscu, na przykład w menedżerze haseł.



![Image](assets/fr/11.webp)



Następnie wybierz nazwę użytkownika, która może być Twoim prawdziwym imieniem lub pseudonimem.



![Image](assets/fr/12.webp)



Następnie można połączyć swój identyfikator Threema ID z numerem telefonu. Ułatwia to przeszukiwanie kontaktów, ale jeśli korzystasz z Threema, ma to również na celu zachowanie anonimowości: dlatego najlepiej nie łączyć go. Kliknij "*Next*".



![Image](assets/fr/13.webp)



Po zakończeniu tego kroku kliknij "*Finish*".



![Image](assets/fr/14.webp)



Jesteś teraz połączony z Threema i możesz rozpocząć komunikację.



![Image](assets/fr/15.webp)



## Konfiguracja Threema



Po pierwsze, przejdź do ustawień, klikając trzy małe kropki w prawym górnym rogu, a następnie wybierz "*Ustawienia*".



![Image](assets/fr/16.webp)



W zakładce "*Prywatność*" znajdziesz kilka opcji, które możesz dostosować do swoich potrzeb:




- Synchronizowanie kontaktów w telefonie ;
- Przyjmowanie wiadomości od nieznanych osób;
- Wskaźnik zapisu podczas wprowadzania danych ;
- Zawiadomienie o otrzymaniu wiadomości...



![Image](assets/fr/17.webp)



W zakładce "*Security*" zalecam aktywowanie opcji "*Locking mechanism*" w celu ochrony dostępu do aplikacji. Zaleca się również aktywowanie passphrase w celu zabezpieczenia lokalnych kopii zapasowych.



![Image](assets/fr/18.webp)



Zachęcamy do zapoznania się z innymi sekcjami ustawień, aby dostosować aplikację do własnych preferencji.



![Image](assets/fr/19.webp)



## Tworzenie kopii zapasowej konta Threema



Przed rozpoczęciem wymiany wiadomości ważne jest, aby zaplanować sposób odzyskania konta, zwłaszcza w przypadku zmiany lub utraty telefonu. Aby to zrobić, kliknij trzy kropki w prawym górnym rogu Interface, a następnie przejdź do menu "*Backups*".



![Image](assets/fr/20.webp)



Tutaj znajdziesz dwie opcje tworzenia kopii zapasowych danych:




- "*Threema Safe*";
- "*Backup danych*".



"Threema Safe* zapisuje na serwerach Threema wszystkie informacje o koncie użytkownika, z wyjątkiem rozmów. Dane te są szyfrowane hasłem wybranym podczas tworzenia konta, dzięki czemu Threema nie ma do nich dostępu. Kopie zapasowe są tworzone automatycznie i regularnie.



Dzięki "*Threema Safe*", aby odzyskać konto na nowym urządzeniu, wystarczy wprowadzić swój "*Threema ID*" i hasło. Brak jednej z tych dwóch informacji uniemożliwi przywrócenie konta.



Ta opcja pozwala jedynie na odzyskanie identyfikatora, profilu, kontaktów, grup i niektórych ustawień, ale **nie historii konwersacji**.



Aby aktywować "*Threema Safe*", wystarczy zaznaczyć opcję w menu "*Backups*".



![Image](assets/fr/21.webp)



Jeśli chcesz również utworzyć kopię zapasową i przywrócić historię konwersacji, musisz skorzystać z opcji "*Data Backup*". Spowoduje to wygenerowanie pełnej kopii zapasowej konta, przechowywanej lokalnie w telefonie. Będziesz musiał przenieść tę kopię zapasową na nowe urządzenie i użyć hasła (i ewentualnie passphrase), aby przywrócić całe konto.



Ponieważ ta kopia zapasowa jest tylko lokalna, musi być regularnie kopiowana na nośnik zewnętrzny. W przeciwnym razie, w przypadku utraty urządzenia, odzyskanie danych będzie niemożliwe. Dlatego też metoda ta najlepiej sprawdza się w przypadku planowanego przenoszenia danych z jednego urządzenia na drugie, a nie w sytuacjach awaryjnych.



Uwaga: "*Data Backup*" działa tylko w przypadku korzystania z tego samego systemu operacyjnego. Nie będzie można jej użyć na przykład do migracji z Samsunga na iPhone'a.



## Dostosuj swój profil Threema



W lewym górnym rogu Interface kliknij swoje zdjęcie profilowe, a następnie wybierz "*Mój profil*".



![Image](assets/fr/22.webp)



Tutaj możesz dostosować swój profil: dodać zdjęcie, wybrać, kto może je zobaczyć lub wyświetlić swój login Threema.



![Image](assets/fr/23.webp)



## Synchronizacja oprogramowania PC



Jeśli chcesz uzyskać dostęp do swoich rozmów na komputerze, możesz zsynchronizować swoje konto Threema za pomocą dedykowanego oprogramowania. Pobierz oprogramowanie dla swojego systemu operacyjnego [z oficjalnej strony internetowej] (https://threema.ch/en/download).



![Image](assets/fr/24.webp)



W telefonie kliknij trzy kropki w prawym górnym rogu, a następnie otwórz menu "*Threema 2.0 for Desktop*".



![Image](assets/fr/25.webp)



Kliknij "*Dodaj urządzenie*", a następnie zeskanuj telefonem kod QR wyświetlony przez oprogramowanie na komputerze.



![Image](assets/fr/26.webp)



Aby potwierdzić synchronizację, kliknij grupę emoji wyświetlaną w oprogramowaniu.



![Image](assets/fr/27.webp)



Na komputerze zaloguj się przy użyciu hasła.



![Image](assets/fr/28.webp)



Oprócz aplikacji mobilnej można teraz uzyskać dostęp do konta Threema bezpośrednio z komputera.



![Image](assets/fr/29.webp)



## Wysyłanie wiadomości za pomocą Threema



Teraz, gdy wszystko jest już poprawnie skonfigurowane, możesz rozpocząć komunikację. Kliknij przycisk "*Rozpocznij czat*".



![Image](assets/fr/30.webp)



Wybierz opcję "*Nowy kontakt*".



![Image](assets/fr/31.webp)



Wprowadź lub zeskanuj "*Threema ID*" swojego korespondenta.



![Image](assets/fr/32.webp)



Kliknij ikonę wiadomości.



![Image](assets/fr/33.webp)



Wyślij pierwszą wiadomość do korespondenta.



![Image](assets/fr/34.webp)



Gdy twój korespondent odpowie, połączenie zostanie nawiązane, a ty będziesz mógł zobaczyć jego imię i nazwisko oraz zdjęcie profilowe. Następnie możesz wysyłać wiadomości Exchange, pliki multimedialne, a nawet wykonywać połączenia.



![Image](assets/fr/35.webp)



Gratulacje, jesteś teraz na bieżąco z korzystaniem z komunikatora Threema, świetnej alternatywy dla WathsApp! Jeśli ten poradnik okazał się przydatny, będę bardzo wdzięczny za pozostawienie kciuka Green poniżej. Zapraszam do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!



Polecam również ten samouczek, w którym przedstawiam Proton Mail, znacznie bardziej przyjazną dla prywatności alternatywę dla Gmaila :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2