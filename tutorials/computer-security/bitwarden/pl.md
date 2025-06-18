---
name: Bitwarden
description: Jak skonfigurować menedżera haseł?
---
![cover](assets/cover.webp)


W erze cyfrowej musimy zarządzać wieloma kontami online obejmującymi różne aspekty naszego codziennego życia, w tym bankowość, platformy finansowe, e-maile, przechowywanie plików, zdrowie, administrację, sieci społecznościowe, gry wideo itp.


Aby uwierzytelnić się na każdym z tych kont, używamy identyfikatora, często adresu e-mail Address, któremu towarzyszy hasło. W obliczu niemożności zapamiętania dużej liczby unikalnych haseł, można ulec pokusie ponownego użycia tego samego hasła lub nieznacznej modyfikacji wspólnej bazy, aby łatwo je zapamiętać. Jednak takie praktyki poważnie zagrażają bezpieczeństwu kont.


Pierwszą zasadą, której należy przestrzegać w przypadku haseł, jest nieużywanie ich ponownie. Każde konto online powinno być chronione unikalnym hasłem, które całkowicie różni się od pozostałych. Jest to ważne, ponieważ jeśli atakującemu uda się złamać jedno z twoich haseł, nie chcesz, aby miał dostęp do wszystkich twoich kont. Posiadanie unikalnego hasła dla każdego konta izoluje potencjalne ataki i ogranicza ich zakres. Na przykład, jeśli używasz tego samego hasła do platformy gier wideo i poczty e-mail, a hasło to zostanie złamane za pośrednictwem strony phishingowej związanej z platformą gier, atakujący może łatwo uzyskać dostęp do poczty e-mail i przejąć kontrolę nad wszystkimi innymi kontami online.


Drugą istotną zasadą jest siła hasła. Hasło jest uważane za silne, jeśli jest trudne do złamania, czyli odgadnięcia metodą prób i błędów. Oznacza to, że hasła muszą być jak najbardziej losowe, długie i zawierać różne znaki (małe i wielkie litery, cyfry i symbole).


Stosowanie tych dwóch zasad bezpieczeństwa haseł (unikalność i solidność) może okazać się trudne w codziennym życiu, ponieważ zapamiętanie unikalnego, losowego i silnego hasła do wszystkich naszych kont jest prawie niemożliwe. W tym miejscu do gry wkracza menedżer haseł.


Menedżer haseł generuje i bezpiecznie przechowuje silne hasła, umożliwiając dostęp do wszystkich kont online bez konieczności ich indywidualnego zapamiętywania. Wystarczy zapamiętać tylko jedno hasło, hasło główne, które zapewnia dostęp do wszystkich haseł zapisanych w menedżerze. Korzystanie z menedżera haseł zwiększa bezpieczeństwo online, ponieważ zapobiega ponownemu użyciu haseł i systematycznie generuje losowe hasła. Upraszcza również codzienne korzystanie z kont poprzez scentralizowanie dostępu do poufnych informacji.

W tym poradniku dowiemy się, jak skonfigurować i używać menedżera haseł w celu zwiększenia bezpieczeństwa online. Przedstawię ci Bitwarden, a w kolejnym poradniku przyjrzymy się innemu rozwiązaniu o nazwie KeePass.

https://planb.network/tutorials/computer-security/authentication/keepass-f8073bb7-5b4a-4664-9246-228e307be246

Ostrzeżenie: Menedżer haseł jest świetny do przechowywania haseł, ale **nigdy nie należy przechowywać w nim frazy Mnemonic Bitcoin Wallet!** Pamiętaj, że fraza Mnemonic powinna być zapisana wyłącznie w formacie fizycznym, takim jak kawałek papieru lub metalu.


## Wprowadzenie do Bitwarden


Bitwarden to menedżer haseł odpowiedni zarówno dla początkujących, jak i zaawansowanych użytkowników. Oferuje on liczne zalety. Przede wszystkim Bitwarden jest rozwiązaniem wieloplatformowym, co oznacza, że można go używać jako aplikacji mobilnej, aplikacji internetowej, rozszerzenia przeglądarki i oprogramowania komputerowego.

![BITWARDEN](assets/notext/01.webp)

Bitwarden umożliwia zapisywanie haseł online i synchronizowanie ich na wszystkich urządzeniach, zapewniając jednocześnie kompleksowe szyfrowanie hasła głównego. Umożliwia to na przykład dostęp do haseł zarówno na komputerze, jak i smartfonie, z synchronizacją między nimi. Ponieważ hasła są zaszyfrowane, pozostają niedostępne dla nikogo, w tym dla Bitwarden, bez klucza deszyfrującego, którym jest hasło główne.


Co więcej, Bitwarden jest oprogramowaniem typu open-source, co oznacza, że może być audytowane przez niezależnych ekspertów. Jeśli chodzi o ceny, Bitwarden oferuje trzy plany:


- Darmowa wersja, którą omówimy w tym poradniku. Chociaż jest darmowa, zapewnia poziom bezpieczeństwa równoważny z płatnymi wersjami. Możesz przechowywać nieograniczoną liczbę haseł i synchronizować dowolną liczbę urządzeń;
- Wersja premium za 10 USD rocznie, która obejmuje dodatkowe funkcje, takie jak przechowywanie plików, tworzenie kopii zapasowych kart bankowych, możliwość skonfigurowania 2FA za pomocą fizycznego klucza bezpieczeństwa oraz dostęp do uwierzytelniania TOTP 2FA bezpośrednio z Bitwarden;
- A także plan rodzinny za 40 USD rocznie, który rozszerza korzyści wersji premium na sześciu różnych użytkowników.

![BITWARDEN](assets/notext/02.webp)

Moim zdaniem ceny te są uczciwe. Darmowa wersja jest doskonałą opcją dla początkujących, a wersja premium oferuje bardzo dobry stosunek jakości do ceny w porównaniu z innymi menedżerami haseł na rynku, oferując jednocześnie więcej funkcji. Dodatkowo, dużą zaletą jest fakt, że Bitwarden jest oprogramowaniem open-source. Jest to zatem interesujący kompromis, szczególnie dla początkujących.

Kolejną funkcją Bitwarden jest możliwość samodzielnego hostowania menedżera haseł, jeśli posiadasz na przykład NAS w domu. Dzięki takiej konfiguracji hasła nie są przechowywane na serwerach Bitwarden, ale na własnych serwerach. Daje to pełną kontrolę nad dostępnością haseł. Opcja ta wymaga jednak rygorystycznego zarządzania kopiami zapasowymi, aby uniknąć utraty dostępu. W związku z tym samodzielny hosting Bitwarden jest bardziej odpowiedni dla zaawansowanych użytkowników i omówimy go w innym samouczku.

## Jak utworzyć konto Bitwarden?


Odwiedź [stronę Bitwarden] (https://bitwarden.com/) i kliknij "*Get Started*".

![BITWARDEN](assets/notext/03.webp)

Zacznij od wprowadzenia adresu e-mail Address, a także imienia i nazwiska lub pseudonimu.

![BITWARDEN](assets/notext/04.webp)

Następnie należy skonfigurować hasło główne. Jak widzieliśmy we wstępie, hasło to jest bardzo ważne, ponieważ daje dostęp do wszystkich innych zapisanych haseł w menedżerze. Wiąże się to z dwoma głównymi zagrożeniami: utratą i kompromitacją. Jeśli utracisz dostęp do tego hasła, nie będziesz już mógł uzyskać dostępu do wszystkich swoich poświadczeń. Jeśli hasło zostanie skradzione, atakujący będzie mógł uzyskać dostęp do wszystkich kont.


Aby zminimalizować ryzyko utraty, zalecam wykonanie fizycznej kopii zapasowej hasła głównego na papierze i przechowywanie jej w bezpiecznym miejscu. Jeśli to możliwe, Seal tę kopię zapasową w bezpiecznej kopercie, aby regularnie upewniać się, że nikt inny nie uzyskał do niej dostępu.


Aby zapobiec złamaniu hasła głównego, musi być ono niezwykle solidne. Powinno być tak długie, jak to możliwe, używać szerokiej gamy znaków i być wybierane losowo. W 2024 r. minimalne zalecenia dotyczące bezpiecznego hasła to 13 znaków, w tym cyfry, małe i wielkie litery, a także symbole, pod warunkiem, że hasło jest naprawdę losowe. Zalecam jednak wybranie hasła składającego się z co najmniej 20 znaków, w tym wszystkich możliwych typów znaków, aby zapewnić jego bezpieczeństwo na dłużej.


Wprowadź hasło główne w dedykowanym polu i potwierdź je w następnym polu.

![BITWARDEN](assets/notext/05.webp)

Jeśli chcesz, możesz dodać podpowiedź do hasła głównego. Jednak odradzam to, ponieważ podpowiedź nie zapewnia niezawodnej metody odzyskiwania w przypadku utraty hasła, a nawet może być przydatna dla atakujących próbujących odgadnąć lub brutalnie wymusić hasło. Zasadniczo należy unikać tworzenia publicznych podpowiedzi, które mogłyby zagrozić bezpieczeństwu hasła głównego.

![BITWARDEN](assets/notext/06.webp)

Następnie kliknij przycisk "*Załóż konto*".

![BITWARDEN](assets/notext/07.webp)

Możesz teraz zalogować się na swoje nowe konto Bitwarden. Wprowadź swój adres e-mail Address.

![BITWARDEN](assets/notext/08.webp)

Następnie wpisz hasło główne.

![BITWARDEN](assets/notext/09.webp)

Znajdujesz się teraz na stronie Interface swojego menedżera haseł.

![BITWARDEN](assets/notext/10.webp)

## Jak skonfigurować Bitwarden?


Na początek potwierdzimy nasz adres e-mail Address. Kliknij "*Wyślij e-mail*".

![BITWARDEN](assets/notext/11.webp)

Następnie kliknij przycisk otrzymany w wiadomości e-mail.

![BITWARDEN](assets/notext/12.webp)

Na koniec zaloguj się ponownie.

![BITWARDEN](assets/notext/13.webp)

Przede wszystkim zdecydowanie zalecam skonfigurowanie uwierzytelniania dwuskładnikowego (2FA) w celu zabezpieczenia menedżera haseł. Masz wybór między korzystaniem z aplikacji TOTP lub fizycznego klucza bezpieczeństwa. Aktywując 2FA, za każdym razem, gdy logujesz się na swoje konto Bitwarden, zostaniesz poproszony nie tylko o podanie hasła głównego, ale także o dowód drugiego czynnika uwierzytelniania. Jest to dodatkowy Layer bezpieczeństwa, szczególnie przydatny w przypadku, gdy papierowa kopia zapasowa hasła głównego zostanie naruszona.


Jeśli nie masz pewności, jak skonfigurować i korzystać z tych urządzeń 2FA, polecam skorzystanie z tych 2 innych samouczków:


https://planb.network/tutorials/computer-security/authentication/authy-a76ab26b-71b0-473c-aa7c-c49153705eb7

https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e

Aby to zrobić, przejdź do zakładki "*Security*" w menu "*Settings*".

![BITWARDEN](assets/notext/14.webp)

Następnie kliknij zakładkę "*Dwuetapowe logowanie*".

![BITWARDEN](assets/notext/15.webp)

Tutaj możesz wybrać preferowaną metodę 2FA. Na przykład wybiorę 2FA z aplikacją TOTP, klikając przycisk "*Zarządzaj*".

![BITWARDEN](assets/notext/16.webp)

Potwierdź hasło główne.

![BITWARDEN](assets/notext/17.webp)

Następnie zeskanuj kod QR za pomocą aplikacji 2FA.

![BITWARDEN](assets/notext/18.webp)

Wprowadź 6-cyfrowy kod podany w aplikacji 2FA, a następnie kliknij przycisk "*Włącz*". ![BITWARDEN](assets/notext/19.webp)

Uwierzytelnianie dwuskładnikowe zostało pomyślnie skonfigurowane na Twoim koncie.

![BITWARDEN](assets/notext/20.webp)

Teraz, jeśli spróbujesz zalogować się ponownie do swojego menedżera, będziesz musiał najpierw wprowadzić hasło główne, a następnie dynamiczny 6-cyfrowy kod wygenerowany przez aplikację 2FA. Upewnij się, że zawsze masz dostęp do tego dynamicznego kodu; bez niego nie będziesz w stanie odzyskać swoich haseł.

![BITWARDEN](assets/notext/21.webp)

W ustawieniach dostępna jest również opcja dostosowania menedżera w zakładce "*Preferencje*". W tym miejscu można zmienić czas trwania automatycznej blokady menedżera, a także język i motyw Interface.

![BITWARDEN](assets/notext/22.webp)

Zdecydowanie zalecam dostosowanie długości haseł generowanych przez Bitwarden. Domyślnie długość ustawiona jest na 14 znaków, co może być niewystarczające dla optymalnego bezpieczeństwa. Teraz, gdy masz menedżera do zapamiętywania wszystkich haseł, możesz równie dobrze wykorzystać go do używania bardzo silnych haseł.


W tym celu należy przejść do menu "*Generator*".

![BITWARDEN](assets/notext/23.webp)

Tutaj możesz zwiększyć długość haseł do 40 i zaznaczyć pole wyboru, aby uwzględnić symbole.

![BITWARDEN](assets/notext/24.webp)

## Jak zabezpieczyć swoje konta w Bitwarden?


Po skonfigurowaniu menedżera haseł można rozpocząć przechowywanie danych uwierzytelniających do kont online. Aby dodać nowy element, kliknij bezpośrednio przycisk "*New item*" lub przycisk "*New*" znajdujący się w prawym górnym rogu ekranu, a następnie "*item*".

![BITWARDEN](assets/notext/25.webp)

W otwartym formularzu zacznij od określenia charakteru elementu, który ma zostać zapisany. Aby zapisać dane logowania, wybierz opcję "*Login*" z rozwijanego menu.

![BITWARDEN](assets/notext/26.webp)

W polu "*Name*" wprowadź opisową nazwę swoich poświadczeń. Ułatwi to wyszukiwanie i porządkowanie haseł, zwłaszcza w przypadku ich dużej liczby. Na przykład, jeśli chcesz zapisać swoje dane uwierzytelniające dla witryny PlanB Network, możesz nazwać ten element w sposób, który sprawi, że będzie on natychmiast rozpoznawalny podczas przyszłych wyszukiwań.

![BITWARDEN](assets/notext/27.webp)

Opcja "*Folder*" umożliwia klasyfikowanie poświadczeń w folderach. Na razie nie utworzyliśmy jeszcze żadnego, ale później pokażę, jak to zrobić.

![BITWARDEN](assets/notext/28.webp)

W polu "*Username*" wprowadź swoją nazwę użytkownika, która zwykle jest Twoim adresem e-mail Address. ![BITWARDEN](assets/notext/29.webp)

Następnie w polu "*Hasło*" można wprowadzić hasło. Zdecydowanie zalecam jednak, aby Bitwarden generate utworzył dla ciebie długie, losowe i unikalne hasło. Zapewni to silne hasło. Aby skorzystać z tej funkcji, kliknij ikonę podwójnej strzałki nad polem do wypełnienia.

![BITWARDEN](assets/notext/30.webp)

Możesz zobaczyć, że Twoje hasło zostało wygenerowane.

![BITWARDEN](assets/notext/31.webp)

W polu "*URI 1*" można wprowadzić nazwę domeny strony internetowej.

![BITWARDEN](assets/notext/32.webp)

Wreszcie, w polu "*Notes*" można w razie potrzeby dodać dodatkowe szczegóły.

![BITWARDEN](assets/notext/33.webp)

Po wypełnieniu wszystkich pól kliknij przycisk "*Zapisz*".

![BITWARDEN](assets/notext/34.webp)

Twój identyfikator pojawi się teraz w menedżerze Bitwarden.

![BITWARDEN](assets/notext/35.webp)

Klikając na nią, można uzyskać dostęp do jej szczegółów i zmodyfikować je.

![BITWARDEN](assets/notext/36.webp)

Klikając trzy małe kropki po prawej stronie, można szybko skopiować hasło lub identyfikator.

![BITWARDEN](assets/notext/37.webp)

Gratulacje, pomyślnie zapisałeś swoje pierwsze hasło w menedżerze! Jeśli chcesz lepiej zorganizować swoje identyfikatory, możesz utworzyć określone foldery. Aby to zrobić, kliknij przycisk "*Nowy*" znajdujący się w prawym górnym rogu ekranu, a następnie wybierz "*Folder*".

![BITWARDEN](assets/notext/38.webp)

Wprowadź nazwę folderu.

![BITWARDEN](assets/notext/39.webp)

Następnie kliknij "*Zapisz*".

![BITWARDEN](assets/notext/40.webp)

Folder pojawi się teraz w menedżerze.

![BITWARDEN](assets/notext/41.webp)

Możesz przypisać folder do identyfikatora podczas jego tworzenia, tak jak zrobiliśmy to wcześniej, lub modyfikując istniejący identyfikator. Na przykład, klikając na identyfikator PlanB Network, mogę sklasyfikować go w folderze "*Bitcoin*".

![BITWARDEN](assets/notext/42.webp)

W ten sposób można uporządkować menedżera haseł, aby ułatwić znajdowanie identyfikatorów. Można je organizować za pomocą folderów, takich jak osobiste, zawodowe, banki, e-maile, sieci społecznościowe, subskrypcje, zakupy, administracja, przesyłanie strumieniowe, przechowywanie, podróże, zdrowie itp.

Jeśli wolisz korzystać tylko z internetowej wersji Bitwarden, możesz pozostać przy tym rozwiązaniu. Zalecam wtedy dodanie menedżera haseł do ulubionych w przeglądarce, aby uzyskać łatwy dostęp i uniknąć ryzyka phishingu. Bitwarden oferuje jednak również pełną gamę klientów umożliwiających korzystanie z menedżera na różnych urządzeniach i upraszczających jego codzienne użytkowanie. W szczególności oferuje aplikację mobilną, rozszerzenie przeglądarki i oprogramowanie komputerowe. Zobaczmy, jak skonfigurować je razem.


![BITWARDEN](assets/notext/43.webp)


## Jak korzystać z rozszerzenia przeglądarki Bitwarden?


Po pierwsze, możesz skonfigurować rozszerzenie przeglądarki, jeśli chcesz. Rozszerzenie to działa jako okrojona wersja menedżera i oferuje możliwość automatycznego zapisywania nowych haseł, sugestii generate dotyczących bezpiecznych haseł i automatycznego wypełniania danych uwierzytelniających na stronach logowania do witryn internetowych.


Codzienne korzystanie z tego rozszerzenia jest niezwykle wygodne, ale może również otwierać nowe wektory ataku. Dlatego też niektórzy eksperci ds. cyberbezpieczeństwa odradzają korzystanie z rozszerzeń przeglądarki do zarządzania hasłami. Jeśli jednak zdecydujesz się skorzystać z rozszerzenia Bitwarden, oto jak postępować:


Zacznij od odwiedzenia [oficjalnej strony pobierania Bitwarden] (https://bitwarden.com/download/#downloads-web-browser).


![BITWARDEN](assets/notext/44.webp)


Wybierz przeglądarkę z podanej listy. W tym przykładzie korzystam z przeglądarki Firefox, więc zostałem przekierowany do oficjalnego rozszerzenia Bitwarden w Firefox Add-ons Store. Procedura jest dość podobna dla innych przeglądarek.


![BITWARDEN](assets/notext/45.webp)


Kliknij przycisk "*Dodaj do Firefox*".


![BITWARDEN](assets/notext/46.webp)


Następnie możesz dołączyć Bitwarden do paska rozszerzeń, aby mieć do niego łatwy dostęp. Kliknij rozszerzenie, aby się zalogować.


![BITWARDEN](assets/notext/47.webp)


Wprowadź swój adres e-mail Address.


![BITWARDEN](assets/notext/48.webp)


Następnie hasło główne.


![BITWARDEN](assets/notext/49.webp)


Na koniec wprowadź 6-cyfrowy kod z aplikacji uwierzytelniającej.


![BITWARDEN](assets/notext/50.webp)


Jesteś teraz połączony ze swoim menedżerem Bitwarden za pośrednictwem rozszerzenia przeglądarki.


![BITWARDEN](assets/notext/51.webp)


Na przykład, jeśli wrócę do witryny PlanB Network i spróbuję zalogować się na swoje konto, można zauważyć, że rozszerzenie Bitwarden zintegrowane z przeglądarką rozpoznaje pola logowania i automatycznie proponuje mi wybranie identyfikatora, który wcześniej zapisałem.


![BITWARDEN](assets/notext/52.webp)

Jeśli wybiorę ten identyfikator, Bitwarden wypełni za mnie pola logowania. Ta funkcja rozszerzenia pozwala na szybkie łączenie się ze stronami internetowymi, bez konieczności kopiowania i wklejania danych uwierzytelniających z aplikacji internetowej Bitwarden lub oprogramowania.

![BITWARDEN](assets/notext/53.webp)

Rozszerzenie zostało również zaprojektowane do wykrywania tworzenia nowych kont. Przykładowo, podczas tworzenia nowego konta w PlanB Network, Bitwarden automatycznie sugeruje zapisanie nowego identyfikatora.

![BITWARDEN](assets/notext/54.webp)

Kliknięcie wyświetlonej sugestii powoduje otwarcie rozszerzenia. Pozwala mi wprowadzić szczegóły nowego identyfikatora i generate silne, unikalne hasło.

![BITWARDEN](assets/notext/55.webp)

Po uzupełnieniu informacji i kliknięciu przycisku "*Zapisz*", rozszerzenie zapisze dane uwierzytelniające.

![BITWARDEN](assets/notext/56.webp)

Następnie rozszerzenie automatycznie wypełnia nasze dane uwierzytelniające w odpowiednich polach na stronie internetowej.

![BITWARDEN](assets/notext/57.webp)

## Jak korzystać z oprogramowania Bitwarden?


Aby zainstalować oprogramowanie Bitwarden desktop, zacznij od przejścia do [strony pobierania] (https://bitwarden.com/download/#downloads-desktop). Wybierz i pobierz wersję odpowiadającą Twojemu systemowi operacyjnemu.

![BITWARDEN](assets/notext/58.webp)

Po zakończeniu pobierania należy przystąpić do instalacji oprogramowania na komputerze. Przy pierwszym uruchomieniu oprogramowania Bitwarden konieczne będzie wprowadzenie danych uwierzytelniających w celu odblokowania menedżera haseł.

![BITWARDEN](assets/notext/59.webp)

Następnie przejdziesz do strony głównej swojego menedżera. Interface jest prawie taki sam jak w aplikacji internetowej.

![BITWARDEN](assets/notext/60.webp)

## Jak korzystać z aplikacji Bitwarden?


Aby uzyskać dostęp do haseł z telefonu, można zainstalować aplikację mobilną Bitwarden. Zacznij od przejścia do [strony pobierania] (https://bitwarden.com/download/#downloads-mobile) i zeskanowania smartfonem kodu QR odpowiadającego Twojemu systemowi operacyjnemu.

![BITWARDEN](assets/notext/61.webp)

Pobierz i zainstaluj oficjalną aplikację mobilną Bitwarden. Przy pierwszym otwarciu aplikacji wprowadź swoje dane uwierzytelniające, aby odblokować dostęp do menedżera haseł.

![BITWARDEN](assets/notext/62.webp)

Po nawiązaniu połączenia będziesz mógł sprawdzać wszystkie swoje hasła i zarządzać nimi bezpośrednio z poziomu aplikacji.

![BITWARDEN](assets/notext/63.webp)

Aby zwiększyć bezpieczeństwo aplikacji, radzę przejść do ustawień i aktywować ochronę kodem PIN. Doda to dodatkowy Layer bezpieczeństwa w przypadku utraty lub kradzieży telefonu.

![BITWARDEN](assets/notext/64.webp)

## Jak wykonać kopię zapasową Bitwarden?

Aby nigdy nie utracić dostępu do swoich haseł, nawet w przypadku utraty hasła głównego lub katastrofy wpływającej na serwery Bitwarden, radzę regularnie wykonywać zaszyfrowaną kopię zapasową menedżera na zewnętrznym nośniku.


Pomysł polega na zaszyfrowaniu wszystkich danych uwierzytelniających Bitwarden hasłem innym niż hasło główne i zapisaniu tej zaszyfrowanej kopii zapasowej na pamięci USB lub dysku Hard, który przechowujesz na przykład w domu. Następnie można przechowywać fizyczną kopię hasła deszyfrującego w oddzielnej lokalizacji od miejsca przechowywania nośnika kopii zapasowej. Można na przykład przechowywać pamięć USB w domu i powierzyć fizyczną kopię hasła szyfrowania zaufanemu znajomemu.


Metoda ta gwarantuje, że nawet w przypadku kradzieży nośnika kopii zapasowej, dane pozostaną niedostępne bez hasła deszyfrującego. Podobnie, twój znajomy nie będzie mógł uzyskać dostępu do twoich danych bez posiadania fizycznego nośnika.


Jednak w przypadku wystąpienia problemu można użyć hasła i nośnika zewnętrznego, aby odzyskać dostęp do swoich danych uwierzytelniających, niezależnie od Bitwarden. Tak więc, nawet jeśli serwery Bitwarden zostaną zniszczone, nadal będziesz mieć możliwość odzyskania swoich haseł.


Dlatego radzę regularnie wykonywać te kopie zapasowe, aby zawsze zawierały najnowsze dane uwierzytelniające. Aby nie zawracać głowy znajomemu, który posiada kopię hasła szyfrującego, przy każdej nowej kopii zapasowej można zapisać to hasło w menedżerze haseł. Nie ma to na celu tworzenia kopii zapasowej, ponieważ twój przyjaciel ma już fizyczną kopię, ale raczej uproszczenie przyszłych procedur eksportu.


Aby kontynuować eksport, jest to całkiem proste: przejdź do sekcji "*Narzędzia*" w menedżerze Bitwarden, a następnie wybierz "*Eksportuj skarbiec*".

![BITWARDEN](assets/notext/65.webp)

Jako format wybierz "*.json (Encrypted)*".

![BITWARDEN](assets/notext/66.webp)

Następnie wybierz opcję "*Zabezpieczone hasłem*".

![BITWARDEN](assets/notext/67.webp)

W tym przypadku ważne jest, aby wybrać silne, unikalne i losowo generowane hasło do szyfrowania kopii zapasowej. Gwarantuje to, że nawet w przypadku kradzieży zaszyfrowanej kopii zapasowej atakujący nie będzie w stanie odszyfrować jej metodą siłową.

![BITWARDEN](assets/notext/68.webp)

Kliknij "*Potwierdź format*" i wprowadź hasło główne, aby kontynuować eksport.

![BITWARDEN](assets/notext/69.webp)

Po zakończeniu eksportu zaszyfrowany plik kopii zapasowej znajdziesz w pobranych plikach. Przenieś go na bezpieczne zewnętrzne urządzenie pamięci masowej, takie jak pamięć USB lub dysk Hard. Powtarzaj tę operację okresowo, w zależności od sposobu użytkowania. Możesz na przykład odnawiać kopię zapasową co tydzień lub co miesiąc, w zależności od potrzeb.