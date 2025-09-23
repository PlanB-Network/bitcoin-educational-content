---
name: Session
description: Wysyłanie zaszyfrowanych wiadomości, a nie metadanych
---
![cover](assets/cover.webp)



Session to aplikacja do szyfrowania wiadomości stworzona w 2020 roku, zaprojektowana w celu zapewnienia wyższego poziomu poufności niż tradycyjne wiadomości. Najpierw została opracowana przez *Oxen Privacy Tech Foundation*, a następnie przez *Session Technology Foundation*.



Session może pochwalić się kilkoma interesującymi cechami technicznymi: kompleksowym szyfrowaniem wiadomości, zdecentralizowaną siecią zorganizowaną w celu zagwarantowania dostępności i redundancji oraz trasowaniem cebulowym inspirowanym siecią Tor. Ponadto, w przeciwieństwie do WathsApp czy Signal, które wymagają podania numeru telefonu do rejestracji, Session nie wymaga podawania żadnych danych osobowych (żadnego numeru, adresu e-mail, a jedynie parę kluczy kryptograficznych).



Session umożliwia wysyłanie wiadomości, plików, wiadomości głosowych, połączeń audio, a także grup liczących do 100 członków (i społeczności powyżej tej liczby), przy jednoczesnym zminimalizowaniu wycieków metadanych.



![Image](assets/fr/01.webp)



Session jest skierowany przede wszystkim do użytkowników, którzy stawiają poufność w centrum swoich priorytetów. Ta usługa przesyłania wiadomości stanowi poważną alternatywę dla WhatsApp, z architekturą zaprojektowaną tak, aby wytrzymać nowoczesne modele nadzoru.



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
| Olvid                | ✅              | ✅              | ✅                   | ✅                          | ❌                           | 🟡(pas d'annuaire)   | 2019              |
| Keet                 | ✅              | ✅              | ✅                   | ❌                          | N/A                         | ✅                    | 2022              |
| Jami                 | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2005              |
| Briar                | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2018              |
| Tox                  | ✅              | ✅              | ✅                   | ✅                          | N/A                         | ✅                    | 2013              |

*E2EE = szyfrowanie typu end-to-end*



## Zainstaluj aplikację Session



Session jest dostępna na wszystkich platformach. Aplikację można pobrać bezpośrednio ze sklepu z aplikacjami w telefonie:




- [Google Play](https://play.google.com/store/apps/details?id=network.loki.messenger);
- [App Store](https://apps.apple.com/us/app/session-private-messenger/id1470168868);
- [F-Droid](https://fdroid.getsession.org/).



W systemie Android możliwa jest również [instalacja przez APK] (https://github.com/session-foundation/session-android/releases).



W tym samouczku skoncentrujemy się na wersji mobilnej, ale należy pamiętać, że [wersje komputerowe są również dostępne](https://getsession.org/download) (MacOS, Linux i Windows). Później przyjrzymy się, jak zsynchronizować konto na wielu urządzeniach.



## Utwórz konto na stronie Session



Przy pierwszym uruchomieniu kliknij na "*Create account*".



![Image](assets/fr/02.webp)



Wybierz nazwę wyświetlaną dla swojego profilu. Może to być pseudonim lub prawdziwe imię i nazwisko.



![Image](assets/fr/03.webp)



Następnie będziesz musiał wybrać jeden z dwóch trybów zarządzania powiadomieniami:





- Tryb szybki (**Firebase Cloud Messaging/Apple Push Notification Service**): umożliwia otrzymywanie powiadomień o wiadomościach w czasie zbliżonym do rzeczywistego, dzięki usługom powiadomień dostarczanym przez Google lub Apple (w zależności od systemu). Aby to zadziałało, Twój adres IP Address i unikalny identyfikator powiadomienia są przesyłane do Google lub Apple, a identyfikator konta sesji jest również rejestrowany na serwerze STF (przez Tor). Ten tryb wiąże się z (co prawda minimalną) ekspozycją metadanych, ale nie naraża na szwank treści wiadomości ani kontaktów i nie pozwala na śledzenie rzeczywistej aktywności użytkownika. Tryb ten jest zatem bardziej wydajny pod względem szybkości reakcji, ale opiera się na scentralizowanej infrastrukturze i jest nieco mniej skuteczny pod względem poufności.





- Tryb powolny (**background polling**): aplikacja Session pozostaje aktywna w tle, okresowo sprawdzając sieć pod kątem nowych wiadomości. To podejście gwarantuje większą poufność niż pierwsze, ponieważ żadne dane nie są przesyłane do serwerów stron trzecich; ani Google, ani Apple, ani serwery STF nie otrzymują żadnych informacji. Z drugiej strony, tryb ten ma dwie wady: powiadomienia mogą być opóźnione (do kilku minut), a zużycie energii jest ogólnie wyższe ze względu na aktywność aplikacji w tle.



![Image](assets/fr/04.webp)



Jesteś teraz połączony z aplikacją Session i możesz rozpocząć wymianę wiadomości.



![Image](assets/fr/05.webp)



## Zapisz swoje konto sesji



Pierwszą rzeczą do zrobienia przed rozpoczęciem korzystania z Session jest zapisanie konta, aby można było je przywrócić w przypadku utraty urządzenia. Aby to zrobić, kliknij przycisk "*Kontynuuj*" obok opcji "*Zapisz hasło odzyskiwania*".



![Image](assets/fr/06.webp)



Session wyświetli wówczas frazę Mnemonic. Należy ją dokładnie skopiować i przechowywać w bezpiecznym miejscu. Ta fraza zapewnia pełny dostęp do konta Session, dlatego ważne jest, aby jej nie ujawniać. Będzie ona potrzebna do uzyskania dostępu do konta na innym urządzeniu, zwłaszcza w przypadku zgubienia lub wymiany telefonu.



![Image](assets/fr/07.webp)



Fraza ta działa w podobny sposób jak frazy Mnemonic używane w portfelach Bitcoin. Dlatego zalecam zapoznanie się z tym innym samouczkiem, w którym wyjaśniam najlepsze praktyki dotyczące zapisywania frazy Mnemonic:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

**Uwaga**: W przeciwieństwie do fraz Mnemonic używanych na portfelach Bitcoin, na Session, **musisz bezwzględnie zapisać każde słowo w całości**. Pierwsze 4 litery nie wystarczą!



## Konfigurowanie aplikacji Session



Aby uzyskać dostęp do ustawień aplikacji, kliknij swoje zdjęcie profilowe w lewym górnym rogu Interface. W tym miejscu można dodać zdjęcie profilowe.



![Image](assets/fr/08.webp)



W menu "*Privacy*" można włączyć lub wyłączyć różne funkcje (uwaga, niektóre mogą ujawnić adres IP Address). Zalecam również włączenie opcji "*Lock App*", która wymaga uwierzytelnienia w celu uzyskania dostępu do aplikacji.



![Image](assets/fr/09.webp)



W menu "*Notification*" znajdziesz wybór pomiędzy "*Fast Mode*" i "*Slow Mode*" (zobacz poprzednie części samouczka). Powiadomienia można również dostosować do własnych preferencji.



![Image](assets/fr/10.webp)



Na koniec należy przejść do menu "*Appearance*", aby dostosować Interface do własnych upodobań. Menu "*Recovery Password*" umożliwia odzyskanie frazy Mnemonic, jeśli chcesz wykonać nową kopię zapasową.



![Image](assets/fr/11.webp)



## Wysyłanie wiadomości za pomocą Session



Aby skontaktować się z innymi osobami, kliknij przycisk "*+*" na stronie głównej.



![Image](assets/fr/12.webp)



Dostępnych jest kilka opcji. Jeśli chcesz utworzyć grupę lub dołączyć do niej, wybierz "*Create Group*" lub "*Join Community*".



![Image](assets/fr/13.webp)



Jeśli chcesz, aby ktoś dodał Cię jako kontakt, możesz poprosić go o zeskanowanie Twojego identyfikatora sesji jako kodu QR.



![Image](assets/fr/14.webp)



Aby wysłać swój login zdalnie, kliknij "*Zaproś znajomego*". Następnie możesz skopiować swój identyfikator sesji i wysłać go za pośrednictwem innego kanału komunikacji. Informacje te można również uzyskać, klikając swoje zdjęcie profilowe na stronie głównej.



![Image](assets/fr/15.webp)



Jeśli posiadasz identyfikator sesji innej osoby i chcesz go dodać, kliknij "*Nowa wiadomość*".



![Image](assets/fr/16.webp)



Następnie możesz wkleić jego identyfikator w tekście lub zeskanować go bezpośrednio, jeśli masz go jako kod QR.



![Image](assets/fr/17.webp)



Następnie wyślij wstępną wiadomość do tej osoby.



![Image](assets/fr/18.webp)



Gdy tylko dana osoba zaakceptuje Twoją prośbę, zobaczysz jej nazwę użytkownika i będziesz mógł z nią swobodnie rozmawiać.



![Image](assets/fr/19.webp)



## Oprogramowanie Synchronize Desktop



Aby zsynchronizować konto na komputerze, należy zainstalować oprogramowanie. [Pobierz je z oficjalnej strony internetowej](https://getsession.org/download). Radzę sprawdzić jego autentyczność i integralność przed instalacją.



![Image](assets/fr/20.webp)



Przy pierwszym uruchomieniu kliknij "*Mam konto*".



![Image](assets/fr/21.webp)



Wprowadź frazę Mnemonic, pamiętając o pozostawieniu spacji między każdym słowem.



![Image](assets/fr/22.webp)



Możesz teraz uzyskać dostęp do swoich rozmów z komputera.



![Image](assets/fr/23.webp)



Gratulacje, już wiesz jak korzystać z komunikatora Session, doskonałej alternatywy dla WathsApp!



Polecam również ten poradnik, w którym przedstawiam Threema, kolejną ciekawą alternatywę dla aplikacji do przesyłania wiadomości:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74