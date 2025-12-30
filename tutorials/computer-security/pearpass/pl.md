---
name: PearPass
description: Odzyskaj kontrolę nad swoimi hasłami dzięki lokalnemu menedżerowi haseł w chmurze, działającemu w modelu peer-to-peer
---

![cover](assets/cover.webp)



W czasach, gdy każda osoba zarządza dziesiątkami, a nawet setkami kont online, bezpieczeństwo loginów stało się kluczową kwestią w bezpieczeństwie IT. Sieci społecznościowe, systemy przesyłania wiadomości, usługi profesjonalne, platformy finansowe: każdy z tych dostępów opiera się na tajemnicy, której naruszenie może mieć poważne konsekwencje dla życia użytkownika.



A jednak, pomimo rosnącej liczby ataków, złe praktyki pozostają powszechne wśród populacji: słabe hasła, ponownie używane hasła, hasła przechowywane w postaci zwykłego tekstu lub hasła w przybliżeniu zapamiętane. Aby rozwiązać te problemy bez komplikowania sobie codziennego życia, rozwiązaniem jest korzystanie z menedżera haseł.



Istnieją już dziesiątki menedżerów haseł, a Plan ₿ Academy oferuje samouczek dla większości z nich. W tym poradniku chciałbym jednak przedstawić jeden, który wyraźnie wyróżnia się na tle innych pod względem sposobu działania: **PearPass**.



**PearPass to open-source'owy, lokalny menedżer haseł typu peer-to-peer, zaprojektowany w celu zapewnienia użytkownikom całkowitej kontroli nad ich danymi



![Image](assets/fr/01.webp)



## Dlaczego warto wybrać PearPass?



Menedżer haseł to oprogramowanie, które generuje, przechowuje i organizuje wszystkie hasła w bezpieczny sposób. Zamiast zapamiętywać lub ponownie używać haseł, masz tylko jeden sekret do ochrony: hasło główne, które szyfruje cały sejf. Takie podejście umożliwia stosowanie unikalnych, długich, losowych haseł dla każdej usługi, zmniejszając zarówno ryzyko zapomnienia, jak i kompromitacji, jednocześnie ograniczając wpływ ewentualnego wycieku. Obecnie jest to podstawowe narzędzie IT, z którego każdy powinien korzystać.



Istnieją dwie główne kategorie menedżerów haseł. Z jednej strony istnieje oprogramowanie tylko lokalne, które jest bardzo bezpieczne, ponieważ dane nigdy nie są przechowywane na centralnym serwerze, ale niezbyt praktyczne, ponieważ nie pozwala na łatwą synchronizację danych uwierzytelniających między kilkoma urządzeniami (komputer, smartfon, tablet...). Z drugiej strony, menedżery haseł oparte na chmurze przechowują dane uwierzytelniające na swoich serwerach i synchronizują je na wszystkich urządzeniach. Ich główną zaletą jest wygoda, ale wiążą się one z kompromisem w zakresie bezpieczeństwa, ponieważ hasła są przechowywane w infrastrukturze, nad którą nie masz kontroli.



PearPass celowo zrywa z obydwoma modelami. Pozycjonuje się pomiędzy lokalnymi menedżerami a rozwiązaniami chmurowymi: umożliwia synchronizację haseł, gwarantując jednocześnie, że nigdy nie są one przechowywane na zdalnych serwerach. W rezultacie wszystkie dane uwierzytelniające są przechowywane lokalnie na urządzeniach, a synchronizacja między wieloma maszynami odbywa się wyłącznie w trybie peer-to-peer. Taka architektura eliminuje pojedyncze punkty awarii związane ze scentralizowanymi bazami danych: nie ma serwerów, które można by skompromitować, ani infrastruktury stron trzecich, która mogłaby uzyskać dostęp do danych uwierzytelniających. Komunikacja między urządzeniami jest szyfrowana od końca do końca, zapewniając, że tylko posiadane klucze umożliwiają dostęp do danych.



![Image](assets/fr/02.webp)



Aby było to możliwe, jak sama nazwa wskazuje, PearPass opiera się na **Pears**, ekosystemie technologii peer-to-peer przeznaczonym do tworzenia i wykonywania aplikacji bezserwerowych. Pears zapewnia środowisko wykonawcze, mechanizmy dystrybucji i warstwy sieciowe potrzebne do uruchamiania w pełni zdecentralizowanych aplikacji, zdolnych do synchronizacji bezpośrednio między peerami, bez żadnej centralnej infrastruktury. W przypadku PearPass, Pears zapewnia wykrywanie urządzeń, nawiązywanie szyfrowanych połączeń i synchronizację haseł między maszynami. Takie podejście zapewnia, że PearPass pozostaje funkcjonalny, odporny i niezależny od jakiegokolwiek zewnętrznego organu.



https://planb.academy/tutorials/computer-security/communication/pears-6d42b312-c69f-4504-8f71-b03b56c42fdd

Oprócz tej innowacyjnej architektury, PearPass jest całkowicie open-source, a wszystkie jego funkcje są bezpłatne. Oprogramowanie zostało również poddane niezależnemu audytowi przez Secfault Security. Oprócz swojej specyficznej architektury, PearPass oferuje oczywiście wszystkie klasyczne funkcje, których oczekuje się od dobrego menedżera haseł, które odkryjemy w tym samouczku.



Krótko mówiąc, podczas gdy tradycyjne menedżery haseł wymagają zaufania firmie i jej serwerom, PearPass przyjmuje logikę suwerenności: bez chmury, bez scentralizowanych kont, bez pośredników. Użytkownik zachowuje wyłączną kontrolę nad swoimi danymi uwierzytelniającymi, jednocześnie korzystając z synchronizacji między urządzeniami.



## Jak zainstalować PearPass?



PearPass jest dostępny na wszystkich platformach: Windows, Linux, macOS, Android, iOS i rozszerzeniach do przeglądarek. Nie ma potrzeby instalowania Pears na swoim komputerze: PearPass działa samodzielnie.



### Instalacja w systemie Windows



W systemie Windows PearPass jest dostarczany jako klasyczny instalator. Przejdź do [oficjalnej strony pobierania] (https://pass.pears.com/download), a następnie kliknij przycisk `Pobierz instalator Windows`.



Po pobraniu pliku należy otworzyć instalator i postępować zgodnie z instrukcjami kreatora. Dostęp do aplikacji można następnie uzyskać z `Menu Start` lub poprzez skrót na pulpicie.



![Image](assets/fr/03.webp)



### Instalacja na macOS



W systemie macOS PearPass jest dystrybuowany jako obraz dysku (`.dmg`). Wejdź na [oficjalną stronę pobierania] (https://pass.pears.com/download) i wybierz wersję odpowiadającą architekturze twojego Maca (Intel lub Apple Silicon). Po pobraniu otwórz plik `.dmg` i uruchom aplikację z folderu `Applications`.



Przy pierwszym uruchomieniu macOS wyświetli komunikat bezpieczeństwa wskazujący, że aplikacja pochodzi z Internetu: wystarczy potwierdzić, aby kontynuować.



### Instalacja w systemie Linux



W systemie Linux PearPass jest dostępny w formacie `.AppImage`, który gwarantuje szeroką kompatybilność z większością dystrybucji bez żadnych konkretnych zależności. Pobierz plik `.AppImage` z [oficjalnej strony pobierania] (https://pass.pears.com/download), a następnie uruchom go bezpośrednio, klikając dwukrotnie.



W zależności od środowiska może być konieczne wykonanie pliku za pomocą właściwości pliku (kliknięcie prawym przyciskiem myszy) lub polecenia `chmod +x`. Po autoryzacji PearPass uruchamia się jako samodzielna aplikacja.



### Instalacja rozszerzenia przeglądarki



PearPass oferuje rozszerzenie przeglądarki umożliwiające automatyczne logowanie i szybki dostęp do sejfu podczas przeglądania stron internetowych. Rozszerzenie jest obecnie dostępne dla Google Chrome i kompatybilnych przeglądarek. Aby je zainstalować, przejdź do [oficjalnej strony pobierania] (https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/04.webp)



Po dodaniu można je przypiąć do paska narzędzi w celu szybkiego dostępu. Aktywacja rozszerzenia wymaga następnie połączenia z aplikacją PearPass zainstalowaną lokalnie na komputerze (wrócimy do tego w dalszej części samouczka).



### Instalacja na systemach iOS i Android



W przypadku urządzeń iPhone i Android wystarczy pobrać aplikację ze sklepu z aplikacjami:




- [Google Play Store](https://play.google.com/store/apps/details?id=com.pears.pass);
- [App Store](https://apps.apple.com/us/app/pearpass/id6752954830).



![Image](assets/fr/05.webp)



Oprócz tych klasycznych metod instalacji, możliwe jest również pobranie oprogramowania bezpośrednio z repozytoriów GitHub, dla każdego :




- [Desktop](https://github.com/tetherto/pearpass-app-desktop);
- [Mobile](https://github.com/tetherto/pearpass-app-mobile);
- [Rozszerzenie przeglądarki](https://github.com/tetherto/pearpass-app-browser-extension).



Po zainstalowaniu PearPass na jednej lub kilku platformach można przejść do wstępnej konfiguracji. W tym poradniku zaczniemy od konfiguracji oprogramowania na komputerze stacjonarnym, a następnie zsynchronizujemy je z rozszerzeniem przeglądarki i aplikacją mobilną.



## Jak utworzyć sejf PearPass?



Po pierwszym uruchomieniu PearPass na komputerze aplikacja prowadzi użytkownika przez dwa kroki: ustawienie hasła głównego, a następnie utworzenie pierwszego sejfu.



### Ustawianie hasła głównego



Po pierwszym uruchomieniu aplikacji na pulpicie, kliknij przycisk `Skip`, a następnie `Continue`, aby przejść przez ekran wprowadzający i dotrzeć do etapu konfiguracji hasła głównego.



![Image](assets/fr/06.webp)



Następnym ważnym krokiem jest wybór hasła głównego. Jak widzieliśmy we wstępie, hasło to jest bardzo ważne, ponieważ daje dostęp do wszystkich innych haseł zapisanych w menedżerze. Technicznie rzecz biorąc, jest ono używane do uzyskiwania kluczy kryptograficznych używanych do szyfrowania danych.



Hasło główne wiąże się z dwoma głównymi zagrożeniami: utratą i złamaniem. Jeśli utracisz dostęp do tego hasła, nie będziesz już w stanie uzyskać dostępu do swoich danych logowania. PearPass nigdy nie przechowuje hasła głównego: **Jeśli zostanie utracone, dane logowania zostaną trwale utracone**. Nie ma mechanizmu odzyskiwania. I odwrotnie, jeśli to hasło zostanie złamane, a atakujący uzyska dostęp do jednego z twoich urządzeń, będzie mógł uzyskać dostęp do wszystkich twoich kont.



Aby ograniczyć ryzyko utraty hasła, można utworzyć fizyczną kopię zapasową hasła głównego, na przykład na papierze, i przechowywać ją w bezpiecznym miejscu. Najlepiej zapieczętować tę kopię zapasową w kopercie, aby móc okresowo sprawdzać, czy nie uzyskano do niej dostępu. Z drugiej strony, nigdy nie twórz cyfrowej kopii zapasowej tego hasła.



Aby zmniejszyć ryzyko naruszenia bezpieczeństwa, hasło główne musi być silne. Powinno być tak długie, jak to możliwe, zawierać szeroką gamę znaków i być wybierane w prawdziwie losowy sposób. W 2025 r. minimalne zalecenia wymagają co najmniej 13 znaków, w tym wielkich i małych liter, cyfr i symboli, pod warunkiem, że hasło jest losowe. Zalecałbym jednak hasło składające się z co najmniej 20 znaków, jeśli nie więcej, ze wszystkimi typami znaków, aby zapewnić trwalszy poziom bezpieczeństwa.



Wprowadź hasło główne w odpowiednim polu, potwierdź je po raz drugi, a następnie kliknij przycisk `Kontynuuj`.



![Image](assets/fr/07.webp)



Następnie zostaniesz przekierowany do ekranu logowania: wprowadź hasło główne, aby sprawdzić, czy wszystko działa poprawnie.



![Image](assets/fr/08.webp)



### Stwórz swój pierwszy sejf



Po zalogowaniu PearPass poprosi o utworzenie pierwszego sejfu. Sejf to zaszyfrowany pojemnik, w którym przechowywane są hasła, identyfikatory, bezpieczne notatki i inne informacje. Każdy sejf jest izolowany i może być identyfikowany za pomocą odrębnej nazwy, co pozwala organizować dane zgodnie z ich przeznaczeniem (osobiste, zawodowe, określone projekty...).



Kliknij przycisk `Utwórz nowy skarbiec`.



![Image](assets/fr/09.webp)



Wybierz nazwę dla tego skarbca, a następnie ponownie kliknij `Twórz nowy skarbiec`, aby sfinalizować tworzenie.



![Image](assets/fr/10.webp)



Twój sejf jest natychmiast gotowy do użycia. Możesz od razu zacząć dodawać hasła, loginy lub bezpieczne notatki.



![Image](assets/fr/11.webp)



## Jak dodać login do PearPass?



Po utworzeniu sejfu możesz zacząć zapisywać w nim swoje przedmioty. PearPass obsługuje rejestrację wielu rodzajów przedmiotów:




- logowanie do witryny lub usługi ;
- tożsamość: dane osobowe do szybkiego wypełniania formularzy, ale także do przechowywania dokumentów tożsamości bezpośrednio w PearPass;
- karta kredytowa: numery karty kredytowej w celu szybszej płatności podczas zakupów online;
- Wi-Fi: hasła do sieci Wi-Fi ;
- PassPhrase: tajna fraza składająca się z kilku słów (ostrzeżenie: zdecydowanie odradzam używanie jej do mnemonicznych fraz wallet Bitcoin);
- uwaga: tworzenie bezpiecznych notatek ;
- niestandardowy: ta funkcja umożliwia utworzenie niestandardowego typu elementu, dostosowanego do konkretnych potrzeb.



Zacznij od otwarcia PearPass i zalogowania się przy użyciu hasła głównego.



![Image](assets/fr/12.webp)



Wybierz sejf, w którym chcesz zapisać ten identyfikator.



![Image](assets/fr/13.webp)



Na stronie głównej kliknij przycisk, aby dodać nowy element, w zależności od rodzaju informacji, które chcesz zarejestrować. W moim przypadku chcę dodać login do mojego konta w witrynie Plan ₿ Academy: klikam więc przycisk `Utwórz login`.



![Image](assets/fr/14.webp)



Po wybraniu rodzaju elementu, który chcesz dodać, pojawi się formularz umożliwiający wprowadzenie informacji związanych z daną usługą. W zależności od potrzeb można wprowadzić nazwę usługi, login, hasło, a w razie potrzeby adres strony internetowej i dodatkowe uwagi.



PearPass posiada również generator haseł, umożliwiający utworzenie silnego hasła bezpośrednio z formularza. Aby z niego skorzystać, kliknij ikonę przedstawiającą trzy małe kropki w polu `Hasło`, wybierz żądaną długość, a następnie kliknij `Wstaw hasło`.



Po wypełnieniu wszystkich pól kliknij przycisk "Zapisz", aby zapisać identyfikator w sejfie.



![Image](assets/fr/15.webp)



Identyfikator został zapisany. Pojawia się on na liście elementów w wybranym sejfie i można go wyświetlić, klikając na niego.



![Image](assets/fr/16.webp)



Możesz łatwo zmodyfikować element, klikając na niego, a następnie na przycisk `Edit`. Można go również usunąć, klikając trzy małe kropki w prawym górnym rogu interfejsu, a następnie przycisk `Usuń element`.



![Image](assets/fr/22.webp)



Na urządzeniach mobilnych logika pozostaje taka sama, choć interfejs został dostosowany. Po zalogowaniu się należy wybrać żądany sejf, dotknąć przycisku `+`, wybrać typ przedmiotu, który ma zostać utworzony, a następnie wypełnić niezbędne informacje.



![Image](assets/fr/17.webp)



## Jak zorganizować PearPass?



Jak widzieliśmy w poprzednich sekcjach, PearPass umożliwia tworzenie kilku różnych skarbców. Umożliwia to oddzielenie różnych zastosowań i stanowi pierwszy poziom organizacji menedżera haseł. Ze strony głównej można łatwo przełączać się z jednego skarbca do drugiego, klikając strzałkę w lewym górnym rogu interfejsu.



![Image](assets/fr/18.webp)



Innym sposobem organizowania haseł, nawet w ramach skarbca, jest tworzenie folderów. Aby to zrobić, w lewej kolumnie interfejsu kliknij symbol `+` obok `All Folders`, a następnie wprowadź nazwę folderu, który chcesz utworzyć.



![Image](assets/fr/19.webp)



Następnie można zapisać wybrane identyfikatory, bezpośrednio podczas tworzenia elementu lub później, klikając `Edit`. Wszystko, co musisz zrobić, to wybrać żądany folder w lewym górnym rogu formularza.



![Image](assets/fr/20.webp)



Po otwarciu elementu, takiego jak login, można kliknąć ikonę gwiazdki w prawym górnym rogu interfejsu, aby dodać go do ulubionych. Ulubione można szybko znaleźć w dedykowanym folderze, oprócz folderu podstawowego.



![Image](assets/fr/21.webp)



Wreszcie, w górnej części interfejsu znajduje się pasek wyszukiwania, dzięki czemu można szybko znaleźć poszukiwany element, nawet jeśli skarbiec zawiera wiele identyfikatorów.



## Jak zsynchronizować PearPass na telefonie komórkowym?



Teraz, gdy masz już działający skarbiec z elementami przechowywanymi na komputerze, prawdopodobnie będziesz chciał uzyskać dostęp do swoich haseł ze smartfona lub innego urządzenia. PearPass umożliwia bezpieczną synchronizację menedżera na wielu komputerach za pomocą Pears. Dowiedzmy się, jak to zrobić.



Aby rozpocząć, na komputerze źródłowym (na przykład komputerze) zaloguj się do skarbca przy użyciu hasła głównego. Na stronie głównej kliknij przycisk "Dodaj urządzenie", znajdujący się w prawym dolnym rogu interfejsu.



![Image](assets/fr/23.webp)



Następnie PearPass generuje link z zaproszeniem, dostępny również jako kod QR, w celu synchronizacji wybranego sejfu na wybranym urządzeniu.



![Image](assets/fr/24.webp)



Jeśli chcesz zsynchronizować się na urządzeniu mobilnym, najpierw zainstaluj aplikację, a następnie uruchom ją. Zostaniesz poproszony o utworzenie hasła głównego dla menedżera mobilnego. Możesz użyć tego samego hasła co na komputerze lub innego. We wszystkich przypadkach należy postępować zgodnie z tymi samymi zaleceniami: silne, losowe hasło zapisane na nośniku fizycznym.



![Image](assets/fr/25.webp)



Następnie możesz aktywować uwierzytelnianie biometryczne, aby uniknąć konieczności ręcznego wprowadzania hasła głównego za każdym razem, gdy odblokowujesz telefon.



![Image](assets/fr/26.webp)



Wprowadź ponownie hasło główne, a następnie kliknij przycisk "Kontynuuj".



![Image](assets/fr/27.webp)



Wybierz opcję `Load a vault`, a następnie kliknij `Scan QR Code` i zeskanuj kod QR zaproszenia wyświetlony przez PearPass na urządzeniu źródłowym (komputerze).



![Image](assets/fr/28.webp)



Twoje sejfy na komputerze i telefonie komórkowym są teraz zsynchronizowane. Każdy identyfikator dodany na jednym urządzeniu będzie bezpiecznie przechowywany i replikowany na drugim.



![Image](assets/fr/29.webp)



W telefonach komórkowych można również aktywować automatyczne wypełnianie pól. Aby to zrobić, przejdź do `Ustawienia > Zaawansowane`, a następnie kliknij przycisk `Ustaw jako domyślne` w sekcji `Autouzupełnianie`.



![Image](assets/fr/30.webp)



## Jak zsynchronizować PearPass z rozszerzeniem przeglądarki?



Posiadanie menedżera haseł zsynchronizowanego między komputerem a smartfonem jest już bardzo praktyczne, ale zintegrowanie go bezpośrednio z przeglądarką jest jeszcze bardziej praktyczne. Aby to zrobić, zacznij od [dodania oficjalnego rozszerzenia PearPass do przeglądarki](https://chromewebstore.google.com/detail/pearpass/pdeffakfmcdnjjafophphgmddmigpejh).



![Image](assets/fr/31.webp)



Z poziomu oprogramowania PearPass zainstalowanego na komputerze lokalnym, przejdź do `Ustawienia > Zaawansowane`, a następnie aktywuj opcję `Aktywuj rozszerzenie przeglądarki`.



![Image](assets/fr/32.webp)



PearPass generuje plik parowania token. Należy go skopiować.



![Image](assets/fr/33.webp)



Następnie otwórz rozszerzenie PearPass w przeglądarce, wklej parowanie token i kliknij przycisk `Verify`, a następnie `Complete`.



![Image](assets/fr/34.webp)



Menedżer haseł jest teraz zsynchronizowany z rozszerzeniem przeglądarki.



![Image](assets/fr/35.webp)



Można go teraz używać do łatwego łączenia się z różnymi kontami internetowymi.



![Image](assets/fr/36.webp)



Teraz już wiesz, jak korzystać z menedżera haseł PearPass. Poza tym narzędziem, codzienne bezpieczeństwo cyfrowe zależy od prawidłowego korzystania z odpowiednich rozwiązań. Jeśli chcesz dowiedzieć się, jak skonfigurować bezpieczne, stabilne i wydajne osobiste środowisko cyfrowe, zapraszam do zapoznania się z naszym kursem szkoleniowym poświęconym tej tematyce:



https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1