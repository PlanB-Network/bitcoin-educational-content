---
name: Sygnał
description: Swobodne wyrażanie siebie
---
![cover](assets/cover.webp)



Signal to szyfrowana aplikacja do przesyłania wiadomości, zaprojektowana tak, aby domyślnie zapewniać wysoki poziom poufności. Każda wiadomość, połączenie i plik są chronione przez protokół Signal, uznawany za jeden z najbardziej niezawodnych protokołów przesyłania wiadomości. Jest on ponownie wykorzystywany przez wiele innych aplikacji, w tym WathsApp, Facebook Messenger, Skype i Google Messages do komunikacji RCS.



Signal został uruchomiony w 2014 roku przez Moxie Marlinspike (pseudonim) i rozwijany od 2018 roku przez Signal Foundation, organizację non-profit utworzoną przy wsparciu Briana Actona (współzałożyciela WhatsApp).



![Image](assets/fr/01.webp)



W porównaniu z WhatsApp, Signal wyróżnia się przejrzystością: kod aplikacji, zarówno po stronie klienta, jak i serwera, jest całkowicie open source. Umożliwia to każdemu przeprowadzenie audytu, a w szczególności sprawdzenie, czy szyfrowanie jest stosowane zgodnie z reklamą.



Signal opiera się jednak na wykorzystaniu numeru telefonu, co jest jego główną słabością, jeśli chodzi o anonimowość w porównaniu z innymi rozwiązaniami. Pomimo tego, aplikacja jest moim zdaniem jedną z najbardziej niezawodnych pod względem bezpieczeństwa i poufności, dzięki całkowicie otwartej architekturze i powszechnie przyjętemu protokołowi szyfrowania, a zatem testowana i audytowana, w przeciwieństwie do innych, bardziej marginalnych aplikacji.



| Application          | E2EE 1:1       | E2EE groupes   | Inscription anonyme | Licence client open-source | Licence serveur open-source | Serveur décentralisé | Année de création |
| -------------------- | -------------- | -------------- | ------------------- | -------------------------- | --------------------------- | -------------------- | ----------------- |
| WhatsApp             | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2009              |
| WeChat               | ❌              | ❌              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Facebook Messenger   | ✅              | 🟡 (optionnel) | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| Telegram             | 🟡 (optionnel) | ❌              | 🟡                  | ✅                          | ❌                           | ❌                    | 2013              |
| LINE                 | ✅              | ✅              | ❌                   | ❌                          | ❌                           | ❌                    | 2011              |
| **Signal**           | ✅              | ✅              | ❌                   | ✅                          | ✅                           | ❌                    | 2014              |
| Threema              | ✅              | ✅              | ✅                   | ✅                          | ❌                           | ❌                    | 2012              |
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




## Zainstaluj aplikację Signal



Signal jest dostępny na wszystkich platformach. Aplikację można pobrać bezpośrednio ze sklepu z aplikacjami w telefonie:




- [Google Play](https://play.google.com/store/apps/details?id=org.thoughtcrime.securesms);
- [App Store](https://apps.apple.com/us/app/signal-private-messenger/id874139669);



W systemie Android możliwa jest również [instalacja przez APK] (https://github.com/signalapp/Signal-Android/releases).



W tym poradniku skoncentrujemy się na wersji mobilnej, ale należy pamiętać, że [dostępne są również wersje desktopowe](https://signal.org/fr/download/) (MacOS, Linux i Windows). Zanim jednak będziesz mógł zsynchronizować swoje konto z wersją desktopową, musisz najpierw skonfigurować aplikację mobilną.



## Utwórz konto w usłudze Signal



Po pierwszym uruchomieniu aplikacji kliknij przycisk "*Kontynuuj*".



![Image](assets/fr/02.webp)



Wprowadź swój numer telefonu, a następnie kliknij "*Next*".



![Image](assets/fr/03.webp)



Kod weryfikacyjny zostanie wysłany w wiadomości SMS. Kod ten należy wprowadzić w aplikacji Signal.



![Image](assets/fr/04.webp)



Wybierz kod PIN, aby zabezpieczyć swoje konto Signal. Kod ten szyfruje dane i może zostać użyty do przywrócenia dostępu do konta w przypadku utraty urządzenia. Dlatego ważne jest, aby wybrać solidny kod PIN, który jest tak długi i losowy, jak to możliwe, oraz aby prowadzić jego wiarygodny zapis.



![Image](assets/fr/05.webp)



Potwierdź kod PIN po raz drugi.



![Image](assets/fr/06.webp)



Możesz teraz spersonalizować swój profil użytkownika. Wybierz zdjęcie, wprowadź imię i nazwisko lub pseudonim. Na tym etapie możesz również określić, kto może Cię znaleźć w Signal za pośrednictwem Twojego numeru. Wybierz "*Everyone*", jeśli chcesz być widoczny, lub "*Nobody*", aby pozostać niewykrywalnym za pośrednictwem numeru telefonu (możesz wtedy zostać dodany tylko za pomocą "*Username*"). Po dokonaniu wyboru kliknij "*Next*".



![Image](assets/fr/07.webp)



Jesteś teraz połączony z Signal i gotowy do Exchange wiadomości.



![Image](assets/fr/08.webp)



## Konfiguracja konta Signal



Kliknij swoje zdjęcie profilowe w lewym górnym rogu, aby uzyskać dostęp do ustawień aplikacji.



![Image](assets/fr/09.webp)



Menu "*Account*" pozwala zarządzać ustawieniami profilu. Radzę zachować ustawienia domyślne. Można również aktywować opcję "*Registration Lock*", która chroni konto przed niektórymi rodzajami ataków. To menu zawiera również opcje potrzebne do przeniesienia konta na nowe urządzenie.



![Image](assets/fr/10.webp)



Ponowne kliknięcie zdjęcia profilowego w ustawieniach spowoduje przejście do opcji personalizacji profilu. Zalecam ustawienie "*Username*": umożliwi to kontaktowanie się z innymi osobami bez ujawniania numeru telefonu.



![Image](assets/fr/11.webp)



Wybierając "*QR code or link*", otrzymasz informacje, które musisz udostępnić komuś, kto chce dodać Cię do Signal.



![Image](assets/fr/12.webp)



Szczególnie ważne jest menu "*Prywatność*". Znajdują się tu opcje kontrolowania widoczności swojego numeru, zarządzania wiadomościami z kontaktami, a także różne uprawnienia przyznane w aplikacji.



![Image](assets/fr/13.webp)



I nie krępuj się eksplorować menu "*Wygląd*", "*Czaty*" i "*Powiadomienia*", aby dostosować Interface i działanie aplikacji do swoich osobistych potrzeb.



## Aplikacja komputerowa Connect



Aby podłączyć aplikację komputerową, należy rozpocząć od zainstalowania oprogramowania na komputerze (patrz pierwsza część tego samouczka). Następnie w telefonie przejdź do Ustawień i otwórz sekcję "*Połączone urządzenia*".



![Image](assets/fr/14.webp)



Kliknij przycisk "*Połącz nowe urządzenie*".



![Image](assets/fr/15.webp)



Na komputerze uruchom oprogramowanie, a następnie zeskanuj telefonem kod QR wyświetlony na ekranie. Jeśli chcesz zaimportować swoje rozmowy, wybierz opcję "*Transferuj historię wiadomości*".



![Image](assets/fr/16.webp)



Twoje urządzenia są teraz w pełni zsynchronizowane.



![Image](assets/fr/17.webp)



## Wysyłanie wiadomości za pomocą Signal



Aby komunikować się z kimś w Signal, musisz najpierw dodać go jako kontakt. Istnieje kilka opcji: możesz dodać go za pomocą jego numeru telefonu (jeśli dana osoba aktywowała opcję wyszukiwania w ten sposób) lub użyć jego identyfikatora Signal ID.



Kliknij ikonę ołówka w prawym dolnym rogu Interface.



![Image](assets/fr/18.webp)



W moim przypadku chcę dodać osobę według nazwy użytkownika. Klikam więc na "*Find by username*".



![Image](assets/fr/19.webp)



Następnie można wkleić login lub zeskanować kod QR.



![Image](assets/fr/20.webp)



Wyślij mu wiadomość, aby nawiązać kontakt.



![Image](assets/fr/21.webp)



Rozmowa pojawi się na stronie głównej. Jeśli dana osoba zaakceptuje Twoją prośbę o kontakt, zobaczysz jej imię i nazwisko oraz zdjęcie profilowe.



![Image](assets/fr/22.webp)



Gratulacje, jesteś teraz na bieżąco z korzystaniem z komunikatora Signal, świetnej alternatywy dla WathsApp! Jeśli ten poradnik okazał się przydatny, będę bardzo wdzięczny, jeśli zostawisz poniżej kciuk Green. Zapraszam do udostępnienia tego poradnika w sieciach społecznościowych. Dziękuję bardzo!



Polecam również ten samouczek, w którym przedstawiam Proton Mail, znacznie bardziej przyjazną dla prywatności alternatywę dla Gmaila :



https://planb.network/tutorials/computer-security/communication/proton-mail-c3b010ce-254d-4546-b382-19ab9261c6a2