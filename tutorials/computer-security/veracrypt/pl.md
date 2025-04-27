---
name: VeraCrypt
description: Jak łatwo zaszyfrować urządzenie pamięci masowej?
---
![cover](assets/cover.webp)


W dzisiejszych czasach ważne jest wdrożenie strategii zapewniającej dostępność, bezpieczeństwo i tworzenie kopii zapasowych plików, takich jak dokumenty osobiste, zdjęcia lub ważne projekty. Utrata tych danych może być katastrofalna w skutkach.


Aby zapobiec tym problemom, radzę utrzymywać wiele kopii zapasowych plików na różnych nośnikach. Powszechnie stosowaną strategią w informatyce jest strategia tworzenia kopii zapasowych "3-2-1", która zapewnia ochronę plików:


- 3** kopie plików;
- Zapisane na co najmniej **2** różnych typach nośników;
- Z co najmniej **1** kopią przechowywaną poza siedzibą firmy.


Innymi słowy, zaleca się przechowywanie plików w 3 różnych lokalizacjach, przy użyciu nośników o różnym charakterze, takich jak komputer, zewnętrzny dysk Hard, pamięć USB lub usługa przechowywania danych online. Wreszcie, posiadanie kopii zapasowej poza siedzibą firmy oznacza, że należy przechowywać kopię zapasową poza domem lub firmą. Ten ostatni punkt pomaga uniknąć całkowitej utraty plików w przypadku lokalnych katastrof, takich jak pożary lub powodzie. Zewnętrzna kopia, oddalona od domu lub firmy, gwarantuje, że dane przetrwają niezależnie od lokalnych zagrożeń.


Aby łatwo wdrożyć tę strategię tworzenia kopii zapasowych 3-2-1, możesz zdecydować się na rozwiązanie do przechowywania danych online, automatycznie lub okresowo synchronizując pliki z komputera z plikami w chmurze. Wśród tych rozwiązań do tworzenia kopii zapasowych online są oczywiście te od dużych firm cyfrowych, które znasz: Google Drive, Microsoft OneDrive czy Apple iCloud. Nie są to jednak najlepsze rozwiązania do ochrony prywatności. W poprzednim poradniku przedstawiłem alternatywę, która szyfruje dokumenty dla lepszej poufności: Proton Drive.


https://planb.network/tutorials/computer-security/data/proton-drive-03cbe49f-6ddc-491f-8786-bc20d98ebb16

Przyjmując tę strategię tworzenia kopii zapasowych lokalnie i w chmurze, korzystasz już z dwóch różnych typów nośników dla swoich danych, z których jeden znajduje się poza siedzibą firmy. Aby uzupełnić strategię 3-2-1, wystarczy dodać dodatkową kopię. Radzę po prostu okresowo eksportować dane obecne lokalnie i w chmurze na nośnik fizyczny, taki jak pamięć USB lub zewnętrzny dysk Hard. W ten sposób, nawet jeśli serwery rozwiązania do przechowywania danych online zostaną zniszczone, a komputer ulegnie awarii, nadal będziesz mieć trzecią kopię na nośniku zewnętrznym, aby nie stracić danych.

![VeraCrypt](assets/notext/01.webp)

Ale ważne jest również, aby pomyśleć o bezpieczeństwie przechowywania danych, aby upewnić się, że nikt inny niż Ty lub Twoi bliscy nie ma do nich dostępu. Zarówno dane lokalne, jak i online są zazwyczaj bezpieczne. Na komputerze prawdopodobnie ustawiłeś hasło, a dyski Hard nowoczesnych komputerów są często domyślnie szyfrowane. Jeśli chodzi o przechowywanie danych online (w chmurze), w poprzednim samouczku pokazałem, jak zabezpieczyć konto silnym hasłem i uwierzytelnianiem dwuskładnikowym. Jednak w przypadku trzeciej kopii przechowywanej na nośniku fizycznym, jedynym zabezpieczeniem jest jej fizyczne posiadanie. Jeśli włamywaczowi uda się ukraść pamięć USB lub zewnętrzny dysk Hard, może on z łatwością uzyskać dostęp do wszystkich danych.

![VeraCrypt](assets/notext/02.webp)

Aby zapobiec temu ryzyku, zaleca się zaszyfrowanie nośnika fizycznego. W ten sposób każda próba uzyskania dostępu do danych będzie wymagała wprowadzenia hasła w celu odszyfrowania zawartości. Bez tego hasła dostęp do danych będzie niemożliwy, zabezpieczając osobiste pliki nawet w przypadku kradzieży pamięci USB lub zewnętrznego dysku Hard.

![VeraCrypt](assets/notext/03.webp)

W tym samouczku pokażę, jak łatwo zaszyfrować zewnętrzny nośnik danych za pomocą VeraCrypt, narzędzia typu open source.


## Wprowadzenie do VeraCrypt


VeraCrypt to oprogramowanie typu open-source dostępne w systemach Windows, macOS i Linux, które umożliwia szyfrowanie danych na różne sposoby i na różnych nośnikach.

![VeraCrypt](assets/notext/04.webp)

Oprogramowanie to umożliwia tworzenie i utrzymywanie zaszyfrowanych woluminów w locie, co oznacza, że dane są automatycznie szyfrowane przed zapisaniem i odszyfrowywane przed odczytaniem. Metoda ta zapewnia ochronę plików nawet w przypadku kradzieży nośnika danych. VeraCrypt szyfruje nie tylko pliki, ale także nazwy plików, metadane, foldery, a nawet wolne miejsce na nośniku pamięci.


VeraCrypt może być używany do szyfrowania plików lokalnie lub całych partycji, w tym dysku systemowego. Można go również użyć do pełnego zaszyfrowania zewnętrznego nośnika, takiego jak pamięć USB lub dysk, jak zobaczymy w tym samouczku.


Główną przewagą VeraCrypt nad rozwiązaniami własnościowymi jest to, że jest on całkowicie open source, co oznacza, że jego kod może zostać zweryfikowany przez każdego.


## Jak zainstalować VeraCrypt?


Przejdź do [oficjalnej strony VeraCrypt](https://www.veracrypt.fr/en/Downloads.html) w zakładce "*Downloads*".

![VeraCrypt](assets/notext/05.webp)

Pobierz wersję odpowiednią dla swojego systemu operacyjnego. Jeśli korzystasz z systemu Windows, wybierz "*EXE Installer*".

![VeraCrypt](assets/notext/06.webp)

Wybierz język dla Interface.

![VeraCrypt](assets/notext/07.webp)

Zaakceptuj warunki licencji.

![VeraCrypt](assets/notext/08.webp)

Wybierz opcję "*Install*".

![VeraCrypt](assets/notext/09.webp)

Na koniec wybierz folder, w którym zostanie zainstalowane oprogramowanie, a następnie kliknij przycisk "*Install*".

![VeraCrypt](assets/notext/10.webp)

Poczekaj na zakończenie instalacji.

![VeraCrypt](assets/notext/11.webp)

Instalacja została zakończona.

![VeraCrypt](assets/notext/12.webp)

Jeśli chcesz, możesz przekazać darowiznę w bitcoinach, aby wesprzeć rozwój tego narzędzia open-source.

![VeraCrypt](assets/notext/13.webp)

## Jak zaszyfrować urządzenie pamięci masowej za pomocą VeraCrypt?


Po pierwszym uruchomieniu dotrzesz do tego Interface:

![VeraCrypt](assets/notext/14.webp)

Aby zaszyfrować wybrane urządzenie pamięci masowej, zacznij od podłączenia go do komputera. Jak zobaczysz później, proces tworzenia nowego zaszyfrowanego woluminu na pamięci USB lub dysku Hard potrwa znacznie dłużej, jeśli urządzenie zawiera już dane, których nie chcesz usuwać. Dlatego zalecam użycie pustej pamięci USB lub opróżnienie urządzenia przed utworzeniem zaszyfrowanego woluminu, aby zaoszczędzić czas.


W VeraCrypt kliknij zakładkę "*Volumes*".

![VeraCrypt](assets/notext/15.webp)

Następnie wybierz menu "*Create New Volume...*".

![VeraCrypt](assets/notext/16.webp)

W nowo otwartym oknie wybierz opcję "*Encrypt a non-system partition/drive*" i kliknij "*Next*".

![VeraCrypt](assets/notext/17.webp)

Następnie należy wybrać pomiędzy opcjami "*Standardowy wolumin VeraCrypt*" i "*Ukryty wolumin VeraCrypt*". Pierwsza opcja tworzy standardowy zaszyfrowany wolumin na urządzeniu. Opcja "*Ukryty wolumen VeraCrypt*" umożliwia utworzenie ukrytego wolumenu w ramach standardowego wolumenu VeraCrypt. Ta metoda pozwala zaprzeczyć istnieniu ukrytego woluminu w przypadku przymusu. Na przykład, jeśli ktoś fizycznie zmusi cię do odszyfrowania twojego urządzenia, możesz odszyfrować tylko standardową część, aby zadowolić agresora, ale nie ujawniać ukrytej części. W moim przykładzie pozostanę przy standardowym wolumenie.

![VeraCrypt](assets/notext/18.webp)

Na następnej stronie kliknij przycisk "*Select Device...*".

![VeraCrypt](assets/notext/19.webp)

Otworzy się nowe okno, w którym można wybrać partycję urządzenia pamięci masowej z listy dysków dostępnych na komputerze. Zazwyczaj partycja, która ma zostać zaszyfrowana, znajduje się w wierszu zatytułowanym "*Removable Disk N*". Po wybraniu odpowiedniej partycji kliknij przycisk "*OK*".

![VeraCrypt](assets/notext/20.webp)

Wybrane wsparcie pojawi się w polu. Możesz teraz kliknąć przycisk "*Next*". ![VeraCrypt](assets/notext/21.webp)

Następnie należy wybrać pomiędzy opcjami "*Utwórz zaszyfrowany wolumin i sformatuj go*" lub "*Szyfruj partycję na miejscu*". Jak wspomniano wcześniej, pierwsza opcja spowoduje trwałe usunięcie wszystkich danych z pamięci USB lub dysku Hard. Wybierz tę opcję tylko wtedy, gdy urządzenie jest puste; w przeciwnym razie utracisz wszystkie zawarte w nim dane. Jeśli chcesz zachować istniejące dane, możesz tymczasowo przenieść je w inne miejsce, wybrać opcję "*Utwórz zaszyfrowany wolumin i sformatuj go*", aby przyspieszyć proces, który usuwa wszystko, lub wybrać opcję "*Szyfruj partycję w miejscu*". Ta ostatnia opcja pozwala na zaszyfrowanie woluminu bez usuwania już znajdujących się na nim danych, ale proces ten będzie znacznie dłuższy. W tym przykładzie, ponieważ moja pamięć USB jest pusta, wybieram "*Utwórz zaszyfrowany wolumin i sformatuj go*", opcję, która usuwa wszystko.

![VeraCrypt](assets/notext/22.webp)

Następnie będziesz mieć możliwość wyboru algorytmu szyfrowania i funkcji Hash. Jeśli nie masz szczególnych potrzeb, radzę zachować domyślne opcje. Kliknij "*Next*", aby kontynuować.

![VeraCrypt](assets/notext/23.webp)

Upewnij się, że wskazany rozmiar woluminu jest prawidłowy, aby zaszyfrować całą dostępną przestrzeń na pamięci USB, a nie tylko jej część. Po zweryfikowaniu kliknij "*Next*".

![VeraCrypt](assets/notext/24.webp)

Na tym etapie konieczne będzie ustawienie hasła do szyfrowania i odszyfrowywania urządzenia. Ważne jest, aby wybrać silne hasło, aby uniemożliwić atakującemu odszyfrowanie zawartości za pomocą ataków siłowych. Hasło powinno być losowe, jak najdłuższe i zawierać kilka rodzajów znaków. Radzę wybrać losowe hasło składające się z co najmniej 20 znaków, w tym małych i wielkich liter, cyfr i symboli.


Radzę również zapisać hasło w menedżerze haseł. Ułatwia to dostęp do hasła i eliminuje ryzyko jego zapomnienia. W naszym konkretnym przypadku menedżer haseł jest lepszy niż nośnik papierowy. Rzeczywiście, w przypadku włamania, chociaż urządzenie pamięci masowej może zostać skradzione, hasło w menedżerze nie może zostać znalezione przez atakującego, co uniemożliwi dostęp do danych. I odwrotnie, jeśli menedżer haseł zostanie naruszony, fizyczny dostęp do urządzenia jest nadal konieczny, aby wykorzystać hasło i uzyskać dostęp do danych.


Aby uzyskać więcej informacji na temat zarządzania hasłami, radzę zapoznać się z tym innym kompletnym samouczkiem:


https://planb.network/tutorials/computer-security/authentication/bitwarden-0532f569-fb00-4fad-acba-2fcb1bf05de9

Wprowadź hasło w 2 wyznaczonych polach, a następnie kliknij "*Next*". ![VeraCrypt](assets/notext/25.webp)

Następnie VeraCrypt zapyta, czy planujesz przechowywać pliki większe niż 4 GiB w zaszyfrowanym woluminie. To pytanie pozwala oprogramowaniu wybrać najbardziej odpowiedni system plików. Ogólnie rzecz biorąc, system FAT jest używany, ponieważ jest kompatybilny z większością systemów operacyjnych, ale narzuca maksymalny limit rozmiaru pliku wynoszący 4 GiB. Jeśli chcesz zarządzać większymi plikami, możesz wybrać system exFAT.

![VeraCrypt](assets/notext/26.webp)

Następnie przejdziesz do strony, która umożliwia generate losowy klucz. Ten klucz jest ważny, ponieważ będzie używany do szyfrowania i odszyfrowywania danych. Będzie on przechowywany w określonej sekcji nośnika, zabezpieczonej wcześniej ustalonym hasłem. Aby uzyskać silny klucz szyfrowania generate, VeraCrypt potrzebuje entropii. Dlatego oprogramowanie prosi o losowe przesuwanie myszy nad oknem; te ruchy są następnie wykorzystywane do generate klucza. Kontynuuj przesuwanie myszy, aż wskaźnik entropii zostanie całkowicie wypełniony. Następnie kliknij "*Format*", aby rozpocząć tworzenie zaszyfrowanego woluminu.

![VeraCrypt](assets/notext/27.webp)

Poczekaj na zakończenie formatowania. W przypadku dużych woluminów może to zająć dużo czasu.

![VeraCrypt](assets/notext/28.webp)

Następnie otrzymasz potwierdzenie.

![VeraCrypt](assets/notext/29.webp)

## Jak używać zaszyfrowanego dysku z VeraCrypt?


Na razie nośnik jest zaszyfrowany i nie można go otworzyć. Aby go odszyfrować, przejdź do VeraCrypt.

![VeraCrypt](assets/notext/30.webp)

Wybierz literę dysku z listy. Na przykład wybrałem "*L:*".

![VeraCrypt](assets/notext/31.webp)

Kliknij przycisk "*Wybierz urządzenie...*".

![VeraCrypt](assets/notext/32.webp)

Z listy wszystkich dysków na komputerze wybierz zaszyfrowany wolumin na nośniku, a następnie kliknij przycisk "*OK*".

![VeraCrypt](assets/notext/33.webp)

Widać, że głośność jest dobrze dobrana.

![VeraCrypt](assets/notext/34.webp)

Kliknij przycisk "*Mount*".

![VeraCrypt](assets/notext/35.webp)

Wprowadź hasło wybrane podczas tworzenia woluminu, a następnie kliknij "*OK*".

![VeraCrypt](assets/notext/36.webp)

Widać, że wolumin jest teraz odszyfrowany i dostępny na literze dysku "*L:*".

![VeraCrypt](assets/notext/37.webp)

Aby uzyskać do niego dostęp, otwórz eksplorator plików i przejdź do dysku "*L:*" (lub innej litery w zależności od tego, którą wybrałeś w poprzednich krokach). ![VeraCrypt](assets/notext/38.webp)

Po dodaniu osobistych plików do nośnika, aby ponownie zaszyfrować wolumin, wystarczy kliknąć przycisk "*Dismount*".

![VeraCrypt](assets/notext/39.webp)

Wolumin nie jest już wyświetlany pod literą "*L:*". Jest więc ponownie zaszyfrowany.

![VeraCrypt](assets/notext/40.webp)

Teraz można usunąć nośnik pamięci.


Gratulacje, masz teraz zaszyfrowany nośnik do bezpiecznego przechowywania danych osobowych, a tym samym kompletną strategię 3-2-1 oprócz kopii na komputerze i rozwiązania do przechowywania danych online.


Jeśli chcesz wesprzeć rozwój VeraCrypt, możesz również przekazać darowiznę w bitcoinach [na tej stronie] (https://www.veracrypt.fr/en/Donation.html).