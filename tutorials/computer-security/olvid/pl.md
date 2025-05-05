---
name: Olvid
description: Prywatne wiadomości dla wszystkich
---
![cover](assets/cover.webp)



Olvid to francuski komunikator internetowy uruchomiony w 2019 roku, zaprojektowany z myślą o zapewnieniu wysokiego poziomu bezpieczeństwa bez uszczerbku dla prywatności. W przeciwieństwie do WhatsApp czy Signal, Olvid nie wymaga podawania żadnych danych osobowych podczas rejestracji: żadnego numeru telefonu, adresu e-mail, niczego. Identyfikacja między użytkownikami opiera się na Exchange kluczy, bez serwera katalogowego lub współdzielonej książki Address.



Wszystkie wiadomości są szyfrowane od końca do końca przy użyciu oryginalnego protokołu kryptograficznego, zaprojektowanego również w celu ochrony metadanych: nikt nie wie, z kim rozmawiasz ani kiedy. Kod klienta jest open source, ale centralny serwer używany do kierowania zaszyfrowanych wiadomości pozostaje zastrzeżony i hostowany w AWS.



Olvid oferuje wersję darmową i subskrypcyjną w cenie 4,99 euro miesięcznie. Darmowa wersja oferuje pełną funkcjonalność, z wyjątkiem wykonywania połączeń audio i wideo (choć możliwe jest ich odbieranie), i nie pozwala na synchronizację konta na wielu urządzeniach. Jeśli więc planujesz korzystać wyłącznie ze smartfona i nie potrzebujesz wykonywać połączeń, Olvid jest doskonałym rozwiązaniem.



Olvid jest certyfikowany przez ANSSI (francuski organ ds. cyberbezpieczeństwa). Aplikacja ta jest doskonałą alternatywą dla tradycyjnych usług przesyłania wiadomości (WhatsApp, Facebook Messenger, WeChat...) dla osób poszukujących prywatności przy jednoczesnym zachowaniu prostoty użytkowania.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Signal               | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                   | ✅                          | N/A                         | 🟡 (via email)       | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                   | ✅                          | ✅                           | 🟡 (fédéré)          | 2014              |
| Session              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2020              |
| SimpleX              | ✅              | ✅              | ✅                   | ✅                          | ✅                           | ✅                    | 2021              |
| **Olvid**                | **✅**              | **✅**              | **✅**                   | **✅**                          | **❌**                           | **❌**                    | **2019**              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = szyfrowanie typu end-to-end*



## Zainstaluj aplikację Olvid



Olvid jest dostępny na wszystkich platformach. Aplikację można pobrać bezpośrednio ze sklepu z aplikacjami na telefonie:




- [Google Play](https://play.google.com/store/apps/details?id=io.olvid.messenger);
- [App Store](https://apps.apple.com/app/olvid/id1414865219);



W systemie Android możliwa jest również [instalacja przez APK] (https://www.olvid.io/download/).



W tym poradniku skupimy się na wersji mobilnej, ale należy pamiętać, że [dostępne są również wersje komputerowe](https://www.olvid.io/download/) (MacOS, Linux i Windows). Jeśli wybierzesz wersję płatną, będziesz mógł synchronizować swoje konto na wielu urządzeniach.



![Image](assets/fr/01.webp)



## Utwórz konto w serwisie Olvid



Przy pierwszym uruchomieniu aplikacji należy kliknąć przycisk "*Jestem nowym użytkownikiem*".



![Image](assets/fr/02.webp)



Wybierz pseudonim lub wprowadź imię i nazwisko.



![Image](assets/fr/03.webp)



Dodaj zdjęcie profilowe.



![Image](assets/fr/04.webp)



Twoje konto zostało utworzone.



![Image](assets/fr/05.webp)



Aby zapobiec utracie dostępu do konta Olvid, zalecamy skonfigurowanie automatycznych kopii zapasowych. Aby to zrobić, otwórz ustawienia, klikając trzy kropki w prawym górnym rogu Interface, a następnie wybierz "*Ustawienia*".



![Image](assets/fr/06.webp)



Przejdź do menu "*Zapisz klucze i kontakty*".



![Image](assets/fr/07.webp)



Następnie kliknij "*generate a backup key*". Ten klucz zaszyfruje kopie zapasowe. Jeśli chcesz odzyskać swoje konto na innym urządzeniu i nie masz już do niego dostępu, będziesz potrzebować zarówno kopii zapasowej, jak i tego klucza, aby je odszyfrować.



![Image](assets/fr/08.webp)



Klucz ten należy przechowywać w bezpiecznym miejscu. Możesz również wykonać kopię papierową.



![Image](assets/fr/09.webp)



Następnie można utworzyć lokalną kopię zapasową lub automatyczną kopię zapasową w usłudze w chmurze. Ta druga opcja jest wysoce zalecana, aby zagwarantować dostęp do konta Olvid w każdych okolicznościach, nawet w przypadku utraty telefonu.



![Image](assets/fr/10.webp)



Upewnij się, że opcja "*Włącz automatyczne tworzenie kopii zapasowych*" jest zaznaczona.



![Image](assets/fr/11.webp)



Możesz także zapoznać się z innymi dostępnymi ustawieniami, aby dostosować aplikację do swoich potrzeb.



![Image](assets/fr/12.webp)



## Wysyłanie wiadomości za pomocą Olvid



Aby móc wysyłać wiadomości, należy najpierw dodać kontakty. Na stronie głównej kliknij niebieski przycisk "*+*".



![Image](assets/fr/13.webp)



Następnie Olvid wyświetli identyfikator użytkownika. Możesz następnie przekazać go osobom, z którymi chcesz się komunikować, aby mogły dodać Cię jako kontakt.



Aby dodać osobę, zeskanuj jej identyfikator za pomocą aparatu lub wklej go ręcznie, klikając trzy małe kropki w prawym górnym rogu.



![Image](assets/fr/14.webp)



Po zeskanowaniu identyfikatora można poprosić osobę kontaktową o zeskanowanie wyświetlonego kodu QR lub wysłać jej prośbę o zdalne połączenie, klikając "*Zdalny kontakt*".



![Image](assets/fr/15.webp)



Połączenie zostało nawiązane.



![Image](assets/fr/16.webp)



Możesz teraz rozpocząć wymianę wiadomości i innych treści ze swoim korespondentem!



![Image](assets/fr/17.webp)



Na stronie głównej znajdziesz wszystkie swoje rozmowy.



![Image](assets/fr/18.webp)



Druga karta zawiera wszystkie kontakty.



![Image](assets/fr/19.webp)



Możesz także tworzyć dyskusje grupowe.



![Image](assets/fr/20.webp)



Gratulacje, jesteś teraz na bieżąco z korzystaniem z komunikatora Olvid, świetnej alternatywy dla WathsApp! Jeśli ten poradnik okazał się przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zachęcam również do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!



Polecam również ten samouczek, w którym przedstawiam Proton Mail, znacznie bardziej przyjazną dla prywatności alternatywę dla Gmaila :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2