---
name: SimpleX Chat
description: Pierwsza skrzynka pocztowa bez identyfikatora użytkownika
---
![cover](assets/cover.webp)



Uruchomiony w 2021 roku SimpleX to darmowy komunikator internetowy z radykalnie odmiennym podejściem do prywatności. W przeciwieństwie do WhatsApp, Signal i innych scentralizowanych usług przesyłania wiadomości, SimpleX wyróżnia się zarządzaniem użytkownikami: nie ma identyfikatorów użytkowników, pseudonimów, numerów ani widocznych kluczy publicznych. Ten całkowity brak identyfikatorów praktycznie uniemożliwia skorelowanie użytkowników, gwarantując wysoki poziom prywatności.



W przeciwieństwie do większości aplikacji, które wymagają konta lub numeru telefonu, SimpleX umożliwia inicjowanie konwersacji poprzez udostępnienie linku lub efemerycznego kodu QR. Każdy link tworzy unikalny zaszyfrowany kanał, a kontakty nie mogą znaleźć ani ponownie skontaktować się z nadawcą bez wyraźnego Exchange. Wiadomości są szyfrowane od końca do końca i przechodzą przez serwery przekaźnikowe, które usuwają je po wysłaniu i nie widzą ani nadawcy, ani odbiorcy, ani ich kluczy.



![Image](assets/fr/01.webp)



Architektura sieci jest całkowicie zdecentralizowana i niesfederowana: serwery nie znają się nawzajem, nie prowadzą globalnego katalogu i nie przechowują żadnych profili użytkowników. Co więcej, każdy użytkownik może wdrożyć i używać własnego serwera przekaźnikowego, zachowując jednocześnie interoperacyjność z serwerami w sieci publicznej.



SimpleX jest całkowicie open-source (klienci, protokoły i serwery), dostępny na Androida, iOS, Linux, Windows i macOS. Jego lokalna pamięć masowa jest szyfrowana i przenośna, dzięki czemu można przenosić profil z jednego urządzenia na drugie bez konieczności polegania na scentralizowanym serwerze.



SimpleX integruje wszystkie klasyczne funkcje aplikacji do przesyłania wiadomości. Jednak jego ergonomia pozostaje mniej płynna niż w przypadku WhatsApp czy Signal. Może być również bardziej restrykcyjna w użyciu, zwłaszcza podczas dodawania kontaktów. Moim zdaniem jest to więc odpowiednia alternatywa dla WhatsApp lub Signal dla użytkowników, którzy stawiają poufność w centrum swoich priorytetów i którzy z tego powodu są gotowi pójść na kilka ustępstw w zakresie codziennego komfortu użytkowania.



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



## Zainstaluj aplikację SimpleX Chat



Aplikacja SimpleX Chat jest dostępna na wszystkich platformach. Aplikację można pobrać bezpośrednio ze sklepu z aplikacjami na telefonie:




- [Google Play](https://play.google.com/store/apps/details?id=chat.simplex.app);
- [App Store](https://apps.apple.com/us/app/simplex-chat-secure-messenger/id1605771084);
- [F-Droid](https://simplex.chat/fdroid/).



W systemie Android możliwa jest również [instalacja przez APK] (https://github.com/simplex-chat/simplex-chat/releases).



W tym samouczku skoncentrujemy się na wersji mobilnej, ale należy pamiętać, że [dostępne są również wersje desktopowe](https://simplex.chat/downloads/) (MacOS, Linux i Windows). Możliwe jest powiązanie wersji desktopowej z istniejącym profilem użytkownika mobilnego, ale aby ta synchronizacja działała, oba urządzenia muszą być podłączone do tej samej sieci lokalnej.



![Image](assets/fr/02.webp)



## Utwórz konto na czacie SimpleX



Po pierwszym uruchomieniu aplikacji kliknij przycisk "*Utwórz swój profil*".



![Image](assets/fr/03.webp)



Wybierz nazwę użytkownika, która może być Twoim prawdziwym imieniem lub pseudonimem, a następnie kliknij "*Create*".



![Image](assets/fr/04.webp)



Następnie ustaw częstotliwość, z jaką aplikacja będzie sprawdzać dostępność nowych wiadomości. Jeśli żywotność baterii telefonu nie jest problemem, wybierz "*Instant*", aby otrzymywać wiadomości w czasie rzeczywistym. Jeśli wolisz oszczędzać baterię i zapobiec działaniu aplikacji w tle, wybierz "*Gdy aplikacja jest uruchomiona*": będziesz wtedy otrzymywać wiadomości tylko wtedy, gdy aplikacja jest otwarta. Możliwym kompromisem jest wybranie okresowego sprawdzania co 10 minut.



Po dokonaniu wyboru kliknij "*Użyj czatu*".



![Image](assets/fr/05.webp)



Jesteś teraz połączony z SimpleX Chat i gotowy do rozpoczęcia rozmowy.



![Image](assets/fr/06.webp)



## Konfiguracja czatu SimpleX



Po pierwsze, przejdź do ustawień, klikając swoje zdjęcie profilowe w prawym dolnym rogu, a następnie "*Ustawienia*".



![Image](assets/fr/07.webp)



Ustawienia domyślne są ogólnie odpowiednie dla większości użytkowników. Zalecam jednak przejście do menu "*Baza danych passphrase i eksport*". W tym miejscu można wyeksportować bazę danych konta SimpleX w celu utworzenia kopii zapasowej.



Można również zmodyfikować passphrase używany do szyfrowania tej bazy danych. Domyślnie jest on generowany losowo i przechowywany lokalnie na urządzeniu. Jeśli wolisz, możesz zdefiniować własny passphrase i usunąć lokalną kopię zapasową passphrase: będziesz musiał wprowadzić go ręcznie za każdym razem, gdy otworzysz aplikację, a także podczas migracji na inne urządzenie.



**Uwaga**: jeśli wybierzesz tę opcję, utrata passphrase spowoduje trwałą utratę wszystkich profili i wiadomości SimpleX.



![Image](assets/fr/08.webp)



Zalecam również przejście do menu "*Prywatność i bezpieczeństwo*", gdzie można aktywować opcję "*SimpleX Lock*". Zabezpiecza ona dostęp do aplikacji za pomocą kodu blokady.



![Image](assets/fr/09.webp)



Wreszcie, menu "*Notifications*" i "*Appearance*" pozwalają dostosować SimpleX Chat do własnych preferencji.



![Image](assets/fr/10.webp)



## Wysyłanie wiadomości za pomocą SimpleX Chat



Aby połączyć się z inną osobą w serwisie SimpleX, dostępne są dwie opcje:




- Użyj linku jednorazowego użytku;
- Użyj statycznego Address wielokrotnego użytku.



Statyczny Address pozwala każdemu, kto go zna, skontaktować się z tobą w SimpleX. Jest to trwały Address, który może być używany wielokrotnie, przez różne osoby, bez ograniczeń czasowych. To właśnie ta trwałość sprawia, że jest on bardziej podatny na spam. Jednak w przeciwieństwie do innych aplikacji do przesyłania wiadomości, usunięcie Address SimpleX wystarczy, aby zatrzymać cały spam, bez wpływu na istniejące konwersacje. W rzeczywistości Address jest używany tylko do ustanowienia początkowego połączenia i nie jest już potrzebny po rozpoczęciu Exchange.



Z drugiej strony linki jednorazowe mogą być użyte tylko raz przez dowolnego użytkownika. Gdy kontakt go użyje, link staje się nieważny. Dla każdego nowego połączenia należy utworzyć nowy link generate.



### Ze statycznym Address



Jeśli chcesz korzystać z Address, kliknij swoje zdjęcie profilowe w lewym dolnym rogu Interface, a następnie wybierz "*Create SimpleX Address*". Następnie ponownie kliknij "*Create SimpleX Address*".



![Image](assets/fr/11.webp)



Twój Address wielokrotnego użytku został utworzony. Możesz udostępnić go osobom, które chcą się z Tobą skontaktować, pokazując im kod QR lub wysyłając im link.



![Image](assets/fr/12.webp)



Kliknij przycisk "*Ustawienia Address*". W tym miejscu można skonfigurować uprawnienia związane z Address. Opcja "*Udostępnij kontaktom*" sprawia, że Address jest widoczny na profilu SimpleX. Twoje kontakty będą mogły się z nim zapoznać i przekazać go innym osobom, które chcą się z Tobą skontaktować.



Opcja "*Auto-accept*" automatycznie akceptuje połączenia przychodzące za pośrednictwem Address. Oznacza to, że każdy użytkownik Address będzie mógł zobaczyć Twój profil i wysłać Ci wiadomość, chyba że aktywujesz opcję "*Akceptuj incognito*". Ukrywa ona imię i nazwisko oraz zdjęcie profilowe podczas nawiązywania nowego połączenia, zastępując je losowym pseudonimem, odrębnym dla każdego rozmówcy.



![Image](assets/fr/13.webp)



### Z łącznikiem wielokrotnego użytku



Drugim sposobem połączenia się z daną osobą jest utworzenie jednorazowego linku. Aby to zrobić, kliknij ikonę ołówka w prawym dolnym rogu Interface, a następnie wybierz "*Utwórz jednorazowy link*".



Jeśli kontakt wysłał ci link, kliknij "*Scan / Paste link*", aby go zeskanować lub wkleić.



![Image](assets/fr/14.webp)



Następnie SimpleX generuje jednorazowy link. Możesz przekazać go swojemu kontaktowi w dowolny sposób: fizyczny Exchange, inne wiadomości itp.



![Image](assets/fr/15.webp)



Możesz również wybrać profil, który ma być powiązany z tym linkiem do zaproszenia. Aby to zrobić, kliknij swój profil tuż pod kodem QR. Będziesz wtedy mógł :




- wybierz jeden z istniejących profili (w następnej sekcji zobaczymy, jak utworzyć kilka profili);
- lub wybrać tryb "*Incognito*", który ukrywa imię i nazwisko oraz zdjęcie profilowe pod losowo wygenerowanym pseudonimem korespondenta.



Tutaj wybieram tryb "*Incognito*".



![Image](assets/fr/16.webp)



Mój rozmówca skorzystał z tego linku. Ze swojej strony nie aktywował trybu "*Incognito*", dlatego widzę nazwę jego profilu "*Bob*". Z drugiej strony Bob nie widzi mojego prawdziwego imienia "*Loïc Morel*", ale losowy pseudonim, w tym przypadku "*RealSynergy*".



![Image](assets/fr/17.webp)



Mógłbym rozpocząć czat natychmiast, ale najpierw chciałbym sprawdzić, czy rozmawiam z Bobem, a nie z jakąś złośliwą osobą, która mogła przechwycić łącze lub przeprowadzić atak MITM.



Aby to zrobić, sprawdzimy nasz link bezpieczeństwa **poza aplikacją**. Jest to ważne, ponieważ w przypadku ataku MITM wewnętrzna weryfikacja zostałaby naruszona. Użyj więc innego bezpiecznego systemu przesyłania wiadomości lub nawet lepiej, sprawdź kody osobiście.



Na czacie kliknij zdjęcie Boba, a następnie "*Weryfikuj kod bezpieczeństwa*". Bob musi zrobić to samo po swojej stronie.



![Image](assets/fr/18.webp)



Jeśli pracujesz zdalnie, porównaj kody w innym bezpiecznym systemie wiadomości (muszą być identyczne). Lub jeszcze lepiej, jeśli możesz spotkać się twarzą w twarz, zeskanuj kod QR swojego kontaktu, klikając "*Scan code*".



![Image](assets/fr/19.webp)



Jeśli weryfikacja przebiegnie pomyślnie, obok nazwy kontaktu pojawi się ikona tarczy ze znacznikiem wyboru. Jest to potwierdzenie, że wymieniasz dane z Bobem. Jeśli weryfikacja nie powiedzie się, pojawi się komunikat "*Poprawny kod bezpieczeństwa!*".



![Image](assets/fr/20.webp)



Możesz teraz swobodnie Exchange wiadomości, połączeń i plików z Bobem, w zależności od uprawnień ustawionych dla tej konwersacji.



## Dostosuj swoje profile SimpleX Chat



Jedną z najpotężniejszych funkcji SimpleX jest możliwość zarządzania kilkoma całkowicie oddzielnymi profilami użytkowników, z których wszystkie są dostępne z tego samego konta lokalnego. Pozwala to na staranne oddzielenie różnych tożsamości bez komplikowania zarządzania wiadomościami.



Na przykład, można utworzyć :




- Profil z prawdziwym imieniem i nazwiskiem oraz prawdziwym zdjęciem na potrzeby profesjonalnej wymiany;
- Profil z prawdziwym imieniem i zabawnym zdjęciem do wymiany rodzinnej;
- Profil z fałszywym zdjęciem i pseudonimem do osobistych rozmów;
- Kolejny pseudonimowy profil do czatowania z nieznajomymi.



To właśnie zamierzamy tutaj zrobić. Zaczynam od skonfigurowania mojego głównego profilu, tego powiązanego z moją prawdziwą tożsamością. Aby to zrobić, klikam na moje zdjęcie profilowe w prawym dolnym rogu, a następnie na moją nazwę użytkownika.



![Image](assets/fr/21.webp)



Następnie klikam moje zdjęcie profilowe, aby je zmienić i dodać nowe.



![Image](assets/fr/22.webp)



Aby dodać inne profile, kliknij menu "*Twoje profile czatów*".



![Image](assets/fr/23.webp)



Tutaj zobaczysz wszystkie swoje profile. Kliknij "*Dodaj profil*", aby utworzyć nowy profil.



![Image](assets/fr/24.webp)



Następnie wybierz informacje dla swojego nowego profilu: nazwę, zdjęcie itp. Tutaj używam pseudonimu i innego obrazu, aby ukryć moją prawdziwą tożsamość w niektórych wymianach.



![Image](assets/fr/25.webp)



Przytrzymując palec na profilu, można go ukryć. Sprawi to, że będzie on niewidoczny w aplikacji, wraz ze wszystkimi powiązanymi z nim konwersacjami. Możesz także wybrać opcję "*Wycisz*", aby przestać otrzymywać powiadomienia.



![Image](assets/fr/26.webp)



Po utworzeniu profili można zarządzać nimi niezależnie. Na stronie głównej wystarczy wybrać aktywny profil do wyświetlenia.



![Image](assets/fr/27.webp)



Podczas tworzenia linku zaproszenia lub statycznego Address można teraz wybrać profil, który ma być z nim powiązany. Na przykład, jeśli wybiorę profil "*Satoshi Nakamoto*" do generate i wyślę go do Alice, zobaczy ona tylko moją pseudonimową tożsamość "*Satoshi Nakamoto*", nie znając mojej prawdziwej tożsamości "*Loïc Morel*". I odwrotnie, jeśli podam jej link z mojego prawdziwego profilu, nie będzie miała możliwości połączenia się z moim pseudonimowym profilem.



![Image](assets/fr/28.webp)



Gratulacje, jesteś teraz na bieżąco z komunikatorem SimpleX, doskonałą alternatywą dla WathsApp!



Polecam również ten poradnik, w którym przedstawiam Threema, kolejną ciekawą alternatywę dla aplikacji do przesyłania wiadomości:



https://planb.network/tutorials/computer-security/communication/threema-24382d25-df7b-4e96-b332-6968f748df74