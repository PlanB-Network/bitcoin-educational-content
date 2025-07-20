---
name: Keet
description: Czat peer-to-peer
---
![cover](assets/cover.webp)



Keet to aplikacja do obsługi wiadomości błyskawicznych zaprojektowana do pracy bez żadnych serwerów. Uruchomiona w 2022 roku przez Holepunch (firmę finansowaną przez Tether i Bitfinex), aplikacja opiera się w całości na sieci peer-to-peer i charakteryzuje się radykalnie zdecentralizowanym podejściem: wiadomości, połączenia i pliki są wymieniane bezpośrednio między użytkownikami, bez pośredników.



Keet szyfruje całą komunikację i nie wymaga podawania żadnych danych osobowych. Rejestracja jest anonimowa i nie wymaga podawania numeru telefonu ani adresu e-mail. Oprócz wymiany wiadomości tekstowych, Keet oferuje bardzo wysokiej jakości połączenia wideo, a także nieograniczone udostępnianie plików. Aplikacja może być zatem używana w sposób hybrydowy, zarówno do użytku osobistego, jak i zawodowego.



![Image](assets/fr/01.webp)



W chwili obecnej (kwiecień 2025 r.) Keet nie jest całkowicie open-source. Część kodu źródłowego jest dostępna na [repozytorium GitHub Holepuncha](https://github.com/holepunchto), zwłaszcza komponenty kryptograficzne i sieciowe, ale klient Interface jeszcze nie. Holepunch ogłosił jednak, że zamierza ostatecznie uczynić całą aplikację open-source. W zależności od tego, kiedy odkryjesz ten samouczek, być może zostało to już zrobione.




| Aplikacja            | E2EE 1:1       | E2EE grupy     | Anonimowa rejestracja | Licencja klienta open-source | Licencja serwera open-source | Zdecentralizowany serwer | Rok utworzenia    |
| -------------------- | -------------- | -------------- | --------------------- | ---------------------------- | ---------------------------- | ------------------------ | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                     | ❌                            | ❌                            | ❌                        | 2009              |
| WeChat               | ❌              | ❌              | ❌                     | ❌                            | ❌                            | ❌                        | 2011              |
| Facebook Messenger   | ✅              | 🟡 (opcjonalne) | ❌                     | ❌                            | ❌                            | ❌                        | 2011              |
| Telegram             | 🟡 (opcjonalne) | ❌              | 🟡                    | ✅                            | ❌                            | ❌                        | 2013              |
| LINE                 | ✅              | ✅              | ❌                     | ❌                            | ❌                            | ❌                        | 2011              |
| Signal               | ✅              | ✅              | ❌                     | ✅                            | ✅                            | ❌                        | 2014              |
| Threema              | ✅              | ✅              | ✅                     | ✅                            | ❌                            | ❌                        | 2012              |
| Element (Matrix)     | ✅              | ✅              | ✅                     | ✅                            | ✅                            | 🟡 (federacyjny)        | 2016              |
| Delta Chat           | ✅              | ✅              | ✅                     | ✅                            | N/A                          | 🟡 (przez email)        | 2017              |
| Conversations (XMPP) | ✅              | ✅              | ✅                     | ✅                            | ✅                            | 🟡 (federacyjny)        | 2014              |
| Session              | ✅              | ✅              | ✅                     | ✅                            | ✅                            | ✅                        | 2020              |
| SimpleX              | ✅              | ✅              | ✅                     | ✅                            | ✅                            | ✅                        | 2021              |
| Olvid                | ✅              | ✅              | ✅                     | ✅                            | ❌                            | 🟡(brak katalogu)      | 2019              |
| Keet                 | ✅              | ✅              | ✅                     | ❌                            | N/A                          | ✅                        | 2022              |
| Jami                 | ✅              | ✅              | ✅                     | ✅                            | N/A                          | ✅                        | 2005              |
| Briar                | ✅              | ✅              | ✅                     | ✅                            | N/A                          | ✅                        | 2018              |
| Tox                  | ✅              | ✅              | ✅                     | ✅                            | N/A                          | ✅                        | 2013              |

*E2EE = szyfrowanie typu end-to-end*



## Zainstaluj Keet



Keet jest dostępny na wszystkich platformach. Aplikację można pobrać bezpośrednio ze sklepu z aplikacjami na telefonie:




- [Google Play](https://play.google.com/store/apps/details?id=io.keet.app&pli=1);
- [App Store](https://apps.apple.com/us/app/keet-by-holepunch/id6443880549);



W systemie Android możliwa jest również [instalacja przez APK] (https://github.com/holepunchto/keet-mobile-releases/releases).



W tym poradniku skupimy się na wersji mobilnej, ale należy pamiętać, że [dostępne są również wersje komputerowe](https://keet.io/) (MacOS, Linux i Windows). Istnieje również możliwość synchronizacji konta na wielu urządzeniach.



## Utwórz konto na Keet



Przy pierwszym uruchomieniu można zignorować ekrany prezentacji.



![Image](assets/fr/02.webp)



Kliknij przycisk "*Jestem nowym użytkownikiem*".



![Image](assets/fr/03.webp)



Zaakceptuj warunki użytkowania, a następnie kliknij "*Quick setup*".



![Image](assets/fr/04.webp)



Wybierz nazwę lub pseudonim, a następnie kliknij "*Finish setup*".



![Image](assets/fr/05.webp)



Twój profil został utworzony. Kliknij ponownie "*Finish setup*", aby zakończyć.



![Image](assets/fr/06.webp)



Możesz dostosować swój profil w dowolnym momencie w zakładce "*Profile*".



## Zapisz swoje konto Keet



Pierwszą rzeczą, jaką należy zrobić z nowym kontem Keet, jest zapisanie frazy odzyskiwania. Jest to sekwencja 24 słów, które umożliwią przywrócenie dostępu do konta w przypadku utraty lub zmiany urządzenia. Ta fraza daje pełny dostęp do konta każdemu, kto ją zna, dlatego ważne jest, aby wykonać niezawodną kopię zapasową i nigdy jej nie ujawniać.



Aby to zrobić, kliknij zakładkę "*Profile*" w prawym dolnym rogu Interface.



![Image](assets/fr/07.webp)



Następnie przejdź do menu "*Ustawienia*".



![Image](assets/fr/08.webp)



Wybierz "*Prywatność i bezpieczeństwo*".



![Image](assets/fr/09.webp)



Następnie kliknij na "*Recovery phrase*".



![Image](assets/fr/10.webp)



Naciśnij przycisk "*Wyświetl frazę*", aby wyświetlić frazę odzyskiwania. Skopiuj ją dokładnie i przechowuj w bezpiecznym miejscu.



![Image](assets/fr/11.webp)



## Wysyłanie wiadomości za pomocą Keet



Aby komunikować się na Keet, musisz utworzyć "*Rooms*". Aby to zrobić, kliknij ikonę ołówka w prawym górnym rogu Interface.



![Image](assets/fr/12.webp)



Wybierz opcję "*Nowy czat grupowy*".



![Image](assets/fr/13.webp)



Wybierz nazwę i opis swojego "*Room*", a następnie kliknij "*Create group chat*".



![Image](assets/fr/14.webp)



Twój "*Room*" został utworzony. Kliknij ikonę "*+*" w prawym górnym rogu, aby zaprosić uczestników.



![Image](assets/fr/15.webp)



Zdefiniuj prawa, które przyznasz nowym członkom za pośrednictwem linku zaproszenia, a także czas ważności linku. Następnie kliknij "*Zaproszenie generate*".



![Image](assets/fr/16.webp)



Keet wyświetli generate link umożliwiający dołączenie do "*Room*". Możesz go skopiować i udostępnić lub poprosić o zeskanowanie kodu QR przez osoby, które chcesz zaprosić.



![Image](assets/fr/17.webp)



Można teraz rozpocząć wymianę wiadomości i plików multimedialnych. Aby rozpocząć połączenie, kliknij ikonę telefonu w prawym górnym rogu.



![Image](assets/fr/18.webp)



Z poziomu tej grupy można również wysyłać prywatne wiadomości do określonych członków. Kliknij zdjęcie profilowe grupy, a następnie wybierz żądanego członka w sekcji "*Członkowie*".



![Image](assets/fr/19.webp)



Kliknij przycisk "*Wyślij żądanie DM*" i wprowadź wiadomość.



![Image](assets/fr/20.webp)



Gdy prośba o DM zostanie zaakceptowana, znajdziesz ten kontakt na stronie głównej, gdzie możesz porozmawiać z nim prywatnie.



![Image](assets/fr/21.webp)



## Synchronizacja konta na wielu urządzeniach



Teraz, gdy wiesz już, jak korzystać z Keet i masz konto, możesz również zsynchronizować je na innym urządzeniu, takim jak komputer. Aby to zrobić, otwórz aplikację na telefonie komórkowym, a następnie kliknij "*Profile*" i przejdź do "*Settings*".



![Image](assets/fr/22.webp)



Następnie przejdź do menu "*Moje urządzenia*".



![Image](assets/fr/23.webp)



Kliknij na "*Dodaj urządzenie*". Keet wyświetli generate link do synchronizacji nowego urządzenia. Skopiuj ten link.



![Image](assets/fr/24.webp)



Na drugim urządzeniu zainstaluj Keet. Na ekranie głównym wybierz opcję "*Jestem obecnym użytkownikiem*".



![Image](assets/fr/25.webp)



Następnie kliknij "*Połącz urządzenie*".



![Image](assets/fr/26.webp)



Wklej link dostarczony przez pierwsze urządzenie, a następnie kliknij "*Rozpocznij synchronizację*".



![Image](assets/fr/27.webp)



Na pierwszym urządzeniu kliknij "*Confirm link devices*", aby autoryzować połączenie.



![Image](assets/fr/28.webp)



Na drugim urządzeniu zakończ proces, klikając "*Połącz urządzenia*".



![Image](assets/fr/29.webp)



Możesz teraz uzyskać dostęp do wszystkich swoich "*Room*" i rozmów z tego nowego urządzenia.



![Image](assets/fr/30.webp)



Gratulacje, jesteś teraz na bieżąco z korzystaniem z komunikatora Keet, świetnej alternatywy dla WathsApp! Jeśli ten poradnik okazał się przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zapraszam do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!



Polecam również ten samouczek, w którym przedstawiam Proton Mail, znacznie bardziej przyjazną dla prywatności alternatywę dla Gmaila :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2