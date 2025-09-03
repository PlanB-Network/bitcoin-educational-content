---
name: Pi-Hole
description: Blokada reklam dla całej sieci
---
![cover](assets/cover.webp)



___



*Ten samouczek jest oparty na oryginalnej treści autorstwa Floriana Duchemin opublikowanej na stronie [IT-Connect](https://www.it-connect.fr/). Licencja [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). W oryginalnym tekście mogły zostać wprowadzone zmiany



___



## I. Prezentacja



Wszyscy zrobiliśmy to zaraz po uruchomieniu naszej ulubionej przeglądarki: zainstalowaliśmy **adblocker** (bloker reklam). Jednak w przypadku korzystania z przeglądarki telewizyjnej lub urządzenia z systemem Android itp. Znalezienie czegoś, co działa, jest nieco trudniejsze. A jeśli w domu jest więcej niż jedno urządzenie, cóż, trzeba powtórzyć operację dla każdej przeglądarki!



W tym samouczku rozwiążemy prosty problem**: udostępnimy bloker reklam wszystkim maszynom w naszej sieci i będziemy nim centralnie zarządzać**



W tym celu wykorzystamy opracowane w tym celu narzędzie: **Pi-Hole**



Pi-Hole to pułapka DNS. Wykorzystuje on żądania DNS wysyłane przez urządzenia do zatwierdzania lub odrzucania ruchu, chroniąc w ten sposób przed adresami i domenami, o których wiadomo, że rozpowszechniają reklamy, złośliwe oprogramowanie itp.



DNS to skrót od Domain Name System. Czym więc jest nazwa domeny? Cóż, "it-connect.fr" to tylko jeden przykład. Nazwa domeny jest unikalnym identyfikatorem dla jednego lub więcej zasobów, zwykle administrowanych przez jeden podmiot.



Nazwa komputera wraz z nazwą domeny to FQDN, czyli *Fully Qualified Domain Name*. Umożliwia ona dotarcie do określonej maszyny poprzez "wywołanie" jej. Na przykład, gdy wpiszesz "www.trucmachin.com", w rzeczywistości wywołujesz maszynę "www", która należy do domeny "trucmachin.com".



Z wyjątkiem tego, że nasze komputery nie rozumieją ludzkiego języka, wszystko, co rozumieją, to binarne, więc potrzebują IP Address, który jest odpowiednikiem numeru telefonu, aby dotrzeć do strony internetowej.



Tak więc za każdym razem, gdy wpisujesz nazwę strony internetowej w przeglądarce lub klikasz link, komputer najpierw pyta serwer DNS o adres IP Address odpowiadający tej nazwie.



**Pi-Hole będzie następnie sprawdzać te żądania (są ich setki każdego dnia!) i automatycznie blokować te, o których wiadomo, że zawierają reklamy lub nawet złośliwe pliki



## II. Instalacja Pi-Hole



Z nazwą taką jak Pi-Hole, można słusznie założyć, że potrzebujesz Raspberry-Pi... Ale to nie do końca prawda. **Pi-Hole można zainstalować na dowolnym komputerze z systemem Linux (Debian, Fedora, Rocky, Ubuntu itp.)



Z drugiej strony należy pamiętać, że **to urządzenie będzie musiało działać 24 godziny na dobę z prostego powodu: brak DNS, brak Internetu!** Raspberry jest zatem dobrym pomysłem, ponieważ nie zużywa prawie żadnej energii.



Aby zainstalować, wystarczy połączyć się z komputerem z systemem Linux przez SSH i wprowadzić następujące polecenie jako "*root*":



```
curl -sSL https://install.pi-hole.net | bash
```



> **Uwaga**: w normalnych okolicznościach nie zaleca się "hakowania" skryptu bez wcześniejszego zapoznania się z jego działaniem. Jeśli nie jesteś pewien, wejdź na stronę za pomocą przeglądarki lub pobierz zawartość jako plik.
>


> **Uwaga: w minimalnych wersjach Debiana 11, Curl nie jest zainstalowany, więc należy zainstalować go ręcznie za pomocą polecenia **apt-get install curl** przed wpisaniem powyższego polecenia.

Po uruchomieniu skryptu zostanie wykonana seria testów, a sama instalacja zajmie się sama:



![Image](assets/fr/019.webp)



Instalacja Pi-Hole



Po zakończeniu instalacji zostaniesz przeniesiony do tego ekranu:



![Image](assets/fr/020.webp)



Ekran startowy Pi-Hole



> **Uwaga**: jeśli korzystasz z DHCP na swoim komputerze, otrzymasz komunikat ostrzegawczy na ten temat. Oczywiście w celu prawidłowego użytkowania zdecydowanie zalecamy przypisanie stałego adresu IP do urządzenia.

Po tym ekranie pojawi się kilka komunikatów informacyjnych, a następnie zostaniesz przeniesiony do kreatora konfiguracji, który najpierw zapyta Cię, do którego serwera DNS Pi-Hole będzie przekazywać żądania. Ze swojej strony wybrałem Quad9, który posiada kartę prywatności użytkownika.



![Image](assets/fr/021.webp)



Wybór DNS - Pi-Hole



> **Uwaga: jeśli jesteś w firmie, istnieje duże prawdopodobieństwo, że Twój obecny serwer DNS jest kontrolerem domeny Active Directory. Ale nie martw się, możesz później określić warunkowy przekierowanie dla wybranej domeny. Zazwyczaj będziesz mógł przekierować dowolne żądanie dotyczące domeny lokalnej do swojego serwera DNS.

Zauważysz, że niektóre opcje zawierają opcję DNSSEC. Zasadniczo protokół DNS nie jest bezpieczny (nie został zaprojektowany z myślą o tym w tamtym czasie). DNSSEC rozwiązuje ten problem, dodając Layer bezpieczeństwa poprzez szyfrowanie i podpisywanie wymian, jak wyjaśniono w odpowiednim artykule: [Bezpieczeństwo DNS](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Każdy bloker reklam opiera się na jednej lub kilku listach, aby wykonać swoją pracę. Pi-Hole jest standardowo dostarczany z jedną listą, więc wybierz ją i dodaj więcej później.



![Image](assets/fr/022.webp)



Jeśli chodzi o Interface web, jego instalacja jest opcjonalna, ponieważ narzędzie ma własną linię poleceń do zarządzania i wizualizacji. Ale ten Interface jest dość przyjemny i dobrze wykonany, więc zalecam zainstalowanie go w tym samym czasie:



![Image](assets/fr/023.webp)



Jeśli instalujesz Pi-Hole na komputerze, który ma już serwer WWW, możesz odpowiedzieć "nie" na poniższe pytanie. Należy jednak pamiętać, że PHP i kilka modułów są wymagane, aby to działało. W przeciwnym razie **lighttpd zostanie zainstalowany ze wszystkimi niezbędnymi modułami**.



![Image](assets/fr/024.webp)



Następnie zostaniesz zapytany, czy chcesz rejestrować żądania DNS. **Jeśli chcesz zachować historię, ustaw to na tak; w przeciwnym razie ustaw to na nie, ale stracisz część funkcji** (patrz następny ekran).



![Image](assets/fr/025.webp)



W przypadku sieci Interface, Pi-Hole używa własnej funkcji o nazwie FTLDNS, która zapewnia interfejs API i generuje statystyki z żądań DNS. Funkcja ta może zawierać tryb "prywatności", który maskuje żądane domeny, klientów stojących za żądaniem lub jedno i drugie. Przydatne, jeśli chcesz monitorować bez naruszania prywatności ludzi lub po prostu jeśli chcesz zachować zgodność z odpowiednimi przepisami w przypadku korzystania z sieci publicznej.



![Image](assets/fr/026.webp)



Wybór prywatnego stylu życia



Po udzieleniu odpowiedzi na to ostatnie pytanie skrypt zrobi to, co do niego należy: pobierze repozytoria GitHub i skonfiguruje Pi-Hole. Pod koniec instalacji zostanie wyświetlony ekran podsumowania z ważnymi informacjami:



![Image](assets/fr/027.webp)



Ekran podsumowania instalacji



Zanotuj hasło sieciowe Interface i informacje o sieci. Teraz nadszedł czas, aby skonfigurować usługę DHCP w naszej bieżącej lokalizacji.



## III. Konfiguracja DHCP



Aby działać, Pi-Hole musi "rozwiązywać" żądania DNS od klientów, więc muszą oni wiedzieć, że to właśnie do niego należy je wysyłać. Można to zrobić na kilka sposobów:





- Modyfikacja ustawień DNS na serwerze DHCP (np. Box)
- Wyłącz ten serwer i użyj tego dostarczonego przez Pi-Hole
- Ręcznie zmodyfikuj każde urządzenie, aby używało Pi-Hole jako DNS



Osobiście wybieram pierwsze rozwiązanie. Są szanse, że **masz serwer DHCP tam, gdzie jesteś** (zwykle twój box). Nie ma więc potrzeby zawracać sobie tym głowy.



Ponieważ istnieje wiele możliwości, między różnymi skrzynkami operatorów (których nie znam) i tymi, którzy mają własny router, nie zamierzam udostępniać zrzutu ekranu dla tych modyfikacji. W każdym razie musisz przejść do ustawień DHCP i zmodyfikować parametr "DNS", aby zawierał IP Address twojego Pi-Hole.



Po wykonaniu tej czynności, jeśli jakiekolwiek urządzenia zostały wcześniej włączone, zachowają one stare ustawienia, więc konieczne będzie ponowne uruchomienie żądania konfiguracji.



Na stacjach roboczych z systemem Windows, za pomocą wiersza polecenia:



```
ipconfig /renew
```



Na stacji roboczej z systemem Linux:



```
dhclient
```



W przypadku wszystkich innych urządzeń należy je wyłączyć i włączyć ponownie.



Powinni więc uzyskać odpowiednie parametry do sprawdzenia:



```
ipconfig /all
```



W polu DNS powinieneś mieć Address swojego Pi-Hole, w moim przypadku 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Korzystanie z Interface web Pi-Hole



Aby ułatwić administrację, **Pi-Hole** korzysta z dobrze zaprojektowanego Interface web Interface. Przyjazny dla użytkownika i dostępny, pozwala:





- Wyświetlanie liczby żądań, zablokowanych żądań itp. w czasie rzeczywistym.
- Zarządzanie białą i czarną listą
- Dodawanie wpisów statycznych, aliasów itp.
- Dodaj listy
- I wiele innych funkcji!



Ze swojej strony dodam listę blokującą. Jak wspomniano powyżej, tylko jedna lista została zainstalowana w tym samym czasie co Soft. Istnieje wiele list dla witryn z reklamami, ale najlepiej jest wybrać przynajmniej jedną specyficzną dla kraju, w którym mieszkasz. Jedną z najbardziej znanych list jest **EasyList**, a jedna z nich jest specyficzna dla Francji: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Aby go dodać, należy najpierw połączyć się z administratorem Interface: **http://<ip_du_PiHole>/admin**



Hasło administratora zostało już wygenerowane (patrz zrzut ekranu po zakończeniu instalacji), więc wystarczy je wprowadzić, aby uzyskać dostęp do Interface:



![Image](assets/fr/030.webp)



Interface od Pi-Hole



Widzimy na przykład, że do Pi-Hole podłączonych jest dwóch klientów, że przetworzył on 442 żądania i że 8 z nich zostało zablokowanych. Wykresy te mogą być dobrym źródłem informacji, zwłaszcza w kontekście zawodowym.



Aby dodać naszą listę, przejdź do menu "**Zarządzanie grupą**" i "**Listy**":



![Image](assets/fr/031.webp)



Widzimy naszą pierwszą listę "**StevenBlack**", aby dodać naszą, skopiuj link, który podałem powyżej i wstaw go w polu "**Address**", w opisie wybieram nazwę listy:



![Image](assets/fr/032.webp)



Dodawanie listy w Pi-Hole



Pozostaje tylko kliknąć "**Dodaj**", aby go dodać. Aby go aktywować, musimy wykonać dodatkowy krok, aby "ostrzec" Pi-Hole o przejęciu tej listy. Aby to zrobić:





- Użyj wbudowanego wiersza poleceń
- Albo sieć Interface



Osobiście wybrałem drugą z nich, ponieważ jeśli dobrze się przyjrzeć, link do skryptu PHP wykonującego aktualizację znajduje się bezpośrednio na stronie, na której się znajdujemy (słowo "online"). Wystarczy więc na niego kliknąć, co przeniesie nas na stronę z tylko jedną opcją:



![Image](assets/fr/033.webp)



Strona wyświetli wynik działania skryptu po jego zakończeniu, co oznacza, że lista została uwzględniona (o ile oczywiście nie zostanie wyświetlony komunikat o błędzie).



Jak ogłoszono na początku tego samouczka, Pi-Hole pozwala również **blokować domeny znane z dystrybucji złośliwego oprogramowania. Aby wzmocnić tę funkcję, sugeruję również dodanie regularnie aktualizowanej listy domen dystrybuowanej przez Abuse.ch**, która znacznie wzmocni bezpieczeństwo twojej sieci, dostępnej pod adresem [this Address](https://urlhaus.abuse.ch/downloads/hostfile/).



Możesz oczywiście dodać dowolne listy, które uważasz za istotne, lub zarządzać czarną listą ręcznie za pomocą menu czarnej listy.



## V. Testy Pi-Hole



Teraz, gdy wszystko jest już gotowe, wszystko, co musisz zrobić, to przetestować rozwiązanie, aby upewnić się, że działa poprawnie.



Na przykład, spróbuję dotrzeć do domeny *http://admin.gentbcn.org/*, która znajduje się na liście Abuse.ch, ponieważ jest znana z hostowania złośliwego oprogramowania:



![Image](assets/fr/034.webp)



Oczywiście zostałem gdzieś zablokowany. Aby upewnić się, że to Pi-Hole wykonał zadanie, możemy sprawdzić dziennik zapytań w Interface web "Query Log", aby zobaczyć, że jest to blokada z wpisu na liście:



![Image](assets/fr/035.webp)



## VI. Wnioski



W tym samouczku pokazaliśmy, jak skonfigurować serwer DNS, który nie tylko eliminuje większość reklam dla wygody przeglądania, ale także dodaje ** Layer bezpieczeństwa, blokując domeny phishingowe i rozprzestrzeniające złośliwe oprogramowanie**.



Wszystkie bezpłatne i ekonomiczne, jeśli są zainstalowane na Raspberry-Pi (pod względem zużycia energii).