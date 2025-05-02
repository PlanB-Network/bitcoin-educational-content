---
name: Linux Mint

description: Konfiguracja komputera dla transakcji Bitcoin
---

![image](assets/cover.webp)


## Co jest nie tak, jeśli używasz zwykłego komputera?


Podczas dokonywania transakcji Bitcoin idealnie jest, jeśli na komputerze nie ma złośliwego oprogramowania. Oczywiście.


Jeśli trzymasz swoją frazę Bitcoin seed (zwykle 12 lub 24 słowa) poza komputerem za pomocą urządzenia podpisującego (np. Hardware Wallet - jego główne przeznaczenie), możesz pomyśleć, że nie jest tak ważne, aby mieć "czysty" komputer - nieprawda.


Zainfekowany złośliwym oprogramowaniem komputer może odczytać adresy Bitcoin, ujawniając atakującemu stan konta - nie może on przejąć Bitcoin tylko na podstawie znajomości Address, ale może zobaczyć, ile masz, i obliczyć na tej podstawie, czy jesteś godnym celem. Mogą również w jakiś sposób dowiedzieć się, gdzie mieszkasz, na przykład, i wyciągnąć od ciebie paznokcie lub dzieci, aby zmusić cię do zapłacenia okupu.


## Jakie jest rozwiązanie?


Zachęcam większość użytkowników Bitcoina do korzystania z dedykowanego, wolnego od złośliwego oprogramowania komputera (z dostępem do Internetu) do dokonywania transakcji Bitcoin. Sugeruję korzystanie z systemu operacyjnego o otwartym kodzie źródłowym, takiego jak Linux Mint, ale jeśli musisz, użyj systemu Windows lub Mac - to lepsze niż używanie zwykłego, dobrze używanego komputera, w którym niezmiennie ukryte jest złośliwe oprogramowanie.


Jedną z przeszkód, które napotykają ludzie, jest instalacja nowego systemu operacyjnego na takich komputerach. Ten przewodnik ma w tym pomóc.


Istnieje wiele odmian Linuksa i wypróbowałem kilka z nich. Moją rekomendacją dla Bitcoinerów jest Linux Mint, ponieważ jest łatwy w instalacji, bardzo szybki (szczególnie podczas uruchamiania i zamykania systemu), nie jest rozdęty (każde dodatkowe oprogramowanie to ryzyko) i rzadko się zawieszał lub zachowywał dziwnie (w porównaniu do innych wersji, takich jak Ubuntu i Debian).


Niektórzy mogą być bardzo oporni na nowy system operacyjny, preferując Windows lub Mac OS. Rozumiem to, ale systemy operacyjne Windows i Apple są zamkniętymi źródłami, więc musimy ufać temu, co robią; nie sądzę, że to dobra polityka, ale nie jest to wszystko albo nic. Wolałbym, aby ludzie korzystali ze świeżo zainstalowanego systemu Windows lub Mac OS, a nie z dobrze używanego komputera (na którym kto wie, jakie złośliwe oprogramowanie się nagromadziło). O krok lepszym rozwiązaniem jest użycie świeżo zainstalowanego komputera z systemem Linux, co właśnie zademonstruję.


Jeśli denerwujesz się przed używaniem Linuksa z powodu nieznanego, to jest to naturalne, ale tak samo jest z poświęceniem trochę czasu na naukę. Tak wiele informacji jest dostępnych online. Oto doskonały krótki film wprowadzający w podstawy wiersza poleceń, który gorąco polecam.

Wybór komputera


Zacznę od tego, co moim zdaniem jest najlepszą opcją. Następnie przedstawię moją opinię na temat alternatyw.


Idealna opcja:


Moim zaleceniem, jeśli możesz sobie na to pozwolić i jeśli rozmiar twojego stosu Bitcoin to uzasadnia, jest zakup zupełnie nowego laptopa klasy podstawowej. Najbardziej podstawowy model zbudowany w dzisiejszych czasach jest wystarczająco dobry, aby poradzić sobie z tym, do czego będzie używany. Specyfikacje procesora i pamięci RAM nie mają znaczenia, ponieważ wszystkie będą wystarczająco dobre.


Unikaj:



- Dowolny zestaw tabletów, w tym Surface Pro
- Chromebooki - często pojemność pamięci jest zbyt mała
- Dowolny komputer z dyskiem eMMC; jeśli ma dysk SSD, to idealnie
- Komputery Mac - są drogie, a z mojego doświadczenia wynika, że sprzęt nie współpracuje dobrze z systemami operacyjnymi Linux
- Cokolwiek odnowionego lub z drugiej ręki (nie jest to jednak bezwzględne kryterium)


Zamiast tego poszukaj laptopa z systemem Windows 11 (obecnie Windows 11 jest najnowszą wersją. Nie martw się, pozbędziemy się tego oprogramowania). Wyszukałem na amazon.com hasło "Windows 11 Laptop" i znalazłem ten dobry przykład:


![image](assets/1.webp)


Cena tego powyżej jest dobra. Specyfikacja jest wystarczająco dobra. Ma wbudowaną kamerę, którą możemy wykorzystać do transakcji PSBT z kodem QR (w przeciwnym razie musiałbyś kupić kamerę USB, aby to zrobić). Nie przejmuj się faktem, że nie jest to dobrze rozpoznawalna marka (jest tania). Jeśli chcesz lepszej marki, będzie cię to kosztować, np:


![image](assets/2.webp)


Niektóre z tańszych mają tylko 64 GB miejsca na dysku; nie testowałem laptopów z tak małymi dyskami - prawdopodobnie 64 GB jest w porządku, ale może to być przesada.


## Inne opcje - ogony


Tails to system operacyjny, który uruchamia się z pendrive'a i tymczasowo przejmuje sprzęt dowolnego komputera. Korzysta wyłącznie z połączeń Tor, więc musisz czuć się komfortowo korzystając z Tora. Żadne z danych zapisywanych w pamięci podczas sesji nie są zapisywane na dysku (za każdym razem zaczyna się od nowa), chyba że dostosujesz ustawienia i utworzysz opcję trwałego przechowywania (na pendrive) - którą zablokujesz hasłem.


Nie jest to zła opcja i jest darmowa, ale jest trochę niezgrabna dla naszych celów. Instalacja nowego oprogramowania nie jest łatwa. Jedną dobrą cechą jest to, że jest dostarczany z Electrum, ale wadą tego jest to, że nie zainstalowałeś go sam. Upewnij się, że używany dysk USB ma pojemność co najmniej 8 GB.


Elastyczność jest ograniczona, jeśli używasz Tails. Możesz nie być w stanie podążać za różnymi przewodnikami, aby skonfigurować to, czego potrzebujesz i sprawić, by działało poprawnie. Na przykład, jeśli postępujesz zgodnie z moim przewodnikiem po instalacji Bitcoin Core, potrzebne są modyfikacje, aby to działało. Nie sądzę, bym przygotował poradnik dotyczący Tails, więc będziesz musiał rozwinąć swoje umiejętności i zrobić to sam.


Nie jestem również pewien, jak dobrze portfele sprzętowe będą współdziałać z tym systemem operacyjnym.


Mimo wszystko, komputer Tails do transakcji Bitcoin jest miłą dodatkową opcją i z pewnością pomoże w nauce korzystania z Tails.


## Inne opcje - Live OS Boot


Jest to bardzo podobne do Tails, z wyjątkiem tego, że system operacyjny nie jest dedykowany prywatności. Podstawowym sposobem korzystania z tej funkcji jest flashowanie dysku USB z wybranym systemem operacyjnym Linux i uruchamianie komputera z tego dysku zamiast z dysku wewnętrznego. Jak to zrobić, wyjaśniono później.


Zaletą jest to, że jesteś mniej ograniczony i wszystko będzie działać bez zaawansowanych poprawek.


Nie jestem pewien, jak dobrze taki system izoluje złośliwe oprogramowanie na istniejącym komputerze od dysku rozruchowego USB, na którym znajduje się nowy system operacyjny. Prawdopodobnie wykonuje dobrą robotę i prawdopodobnie nie jest tak dobry jak Tails. Ponieważ nie wiem, preferuję dedykowany laptop.

Inne opcje - własny używany laptop lub komputer stacjonarny


Korzystanie z używanego komputera nie jest idealnym rozwiązaniem, głównie dlatego, że nie jestem świadomy wewnętrznego działania wyrafinowanego złośliwego oprogramowania ani tego, czy wyczyszczenie dysku wystarczy, aby się go pozbyć. Prawdopodobnie tak, ale nie chcę lekceważyć tego, jak sprytni mogą być hakerzy. Możesz zdecydować, ja nie chcę się angażować.


Jeśli zdecydujesz się użyć starego komputera stacjonarnego zamiast starego laptopa, będzie to w porządku, z wyjątkiem tego, że będzie on stale zajmował miejsce na prawdopodobnie rzadkie transakcje Bitcoin; nie powinieneś używać go do niczego innego. Natomiast w przypadku laptopa można go po prostu odłożyć, a nawet ukryć dla dodatkowego bezpieczeństwa.


## Instalacja Linux Mint na dowolnym komputerze


Są to instrukcje usuwania dowolnego systemu operacyjnego z nowego laptopa i instalacji Linux Mint, ale można je dostosować do instalacji dowolnej wersji Linuksa na dowolnym komputerze.


Będziemy używać dowolnego komputera do flashowania systemu operacyjnego na pendrive. Nie ma znaczenia, jaka to pamięć, o ile jest kompatybilna z portem USB i sugeruję minimum 16 GB.


Kup jedną z tych rzeczy:


![image](assets/3.webp)


Można też użyć czegoś takiego:


![image](assets/4.webp)


Następnie przejdź do linuxmint.com


![image](assets/5.webp)


Najedź kursorem myszy na menu pobierania u góry, a następnie kliknij łącze "Linux Mint 20.3" lub dowolną wersję, która jest najnowsza zalecana w momencie wykonywania tej czynności.


![image](assets/6.webp)


Do wyboru będzie kilka "smaków". Wybierz "Cinnamon", aby postępować zgodnie z tym przewodnikiem. Kliknij przycisk Pobierz.


![image](assets/7.webp)


Na następnej stronie można przewinąć w dół, aby zobaczyć serwery lustrzane (serwery lustrzane to różne serwery, które przechowują kopię żądanego pliku). Możesz zweryfikować pobieranie za pomocą SHA256 i gpg (zalecane), ale pominę to tutaj, ponieważ napisałem już przewodniki na ten temat.


![image](assets/8.webp)


Wybierz najbliższy serwer lustrzany i kliknij jego link (tekst Green w kolumnie lustra). Rozpocznie się pobieranie pliku - wersja, którą pobieram, ma 2,1 gigabajta.


Po pobraniu pliku można go sflashować do pamięci przenośnej i uruchomić z niej komputer. Aby to zrobić, najprostszym sposobem jest użycie Balena Etcher. Pobierz i zainstaluj go, jeśli jeszcze go nie masz.


Następnie uruchom go:


![image](assets/9.webp)


Kliknij przycisk flash from file i wybierz pobrany plik LinuxMint.


Następnie kliknij przycisk Wybierz cel. Upewnij się, że urządzenie pamięci jest podłączone i upewnij się, że wybierasz właściwy dysk, w przeciwnym razie możesz zniszczyć zawartość niewłaściwego dysku!


Następnie wybierz Flash! Może być konieczne wprowadzenie hasła. Po zakończeniu dysk prawdopodobnie nie będzie odczytywany przez komputer z systemem Windows lub Mac, ponieważ został przekształcony w urządzenie z systemem Linux. Wystarczy go wyciągnąć.

Przygotowanie komputera docelowego


Włącz nowego laptopa i podczas jego włączania przytrzymaj klawisz BIOS. Zazwyczaj jest to F2, ale może to być F1, F8, F10, F11, F12 lub Delete. Wypróbuj każdy z nich, aż uzyskasz odpowiedź, lub wyszukaj w Internecie model swojego komputera i zadaj właściwe pytanie.


Na przykład "Klucz BIOS laptopów Dell".


Każdy komputer ma inne menu systemu BIOS. Sprawdź, które menu pozwala skonfigurować kolejność rozruchu. Dla naszych celów chcemy, aby komputer próbował uruchomić się z podłączonego urządzenia USB (jeśli jest podłączone), przed próbą uruchomienia z wewnętrznego dysku Hard (w przeciwnym razie system Windows zostanie załadowany). Po ustawieniu może być konieczne zapisanie przed wyjściem lub automatyczne zapisanie.


Uruchom ponownie komputer i powinien załadować się z pamięci USB. Nie możemy zainstalować Linuksa na dysku wewnętrznym, a Windows zostanie usunięty na dobre.


Gdy dojdziesz do następnego ekranu, wybierz "Instalacja OEM (dla producentów)". Jeśli zamiast tego wybierzesz "Start Linux Mint", otrzymasz sesję Linux Mint załadowaną z urządzenia pamięci, ale po wyłączeniu komputera żadne informacje nie zostaną zapisane - jest to w zasadzie sesja tymczasowa, abyś mógł ją wypróbować.


![image](assets/10.webp)


Zostaniesz przeniesiony przez kreatora graficznego, który zada ci kilka pytań, które powinny być proste. Jednym z nich będą ustawienia Languange, innym będzie połączenie z domową siecią internetową i hasło. Jeśli pojawi się monit o zainstalowanie dodatkowego oprogramowania, odrzuć go. Gdy dojdziesz do pytania o typ instalacji, niektórzy mogą się zawahać - musisz wybrać "Wymaż dysk i zainstaluj Linux Mint". Nie szyfruj też dysku i nie wybieraj LVM.


W końcu dotrzesz do pulpitu. W tym momencie jeszcze nie skończyłeś. W rzeczywistości działasz jako producent (tj. ktoś, kto buduje komputer i konfiguruje Linuksa dla klienta). Musisz dwukrotnie kliknąć ikonę na pulpicie, "Zainstaluj Linux Mint", aby ją sfinalizować.


![image](assets/11.webp)


Pamiętaj, aby wyjąć kartę pamięci, a następnie uruchom ponownie komputer. Po ponownym uruchomieniu będziesz korzystać z systemu operacyjnego po raz pierwszy jako nowy użytkownik. Gratulacje.


Jedną z pierwszych rzeczy, które należy zrobić (i robić regularnie), jest aktualizowanie systemu.


Otwórz aplikację Terminal i wpisz następujące polecenie:


```bash
sudo apt-get update
```


naciśnij <enter>, potwierdź wybór, a następnie to polecenie:


```bash
sudo apt-get upgrade
```


naciśnij <enter> i potwierdź swój wybór.


Może to potrwać kilka minut.


Następnie chcę zainstalować Tor (wielkość liter ma znaczenie):


```bash
sudo apt-get install tor
```


**Pro Tip:** Możesz także uruchomić rozruch Linux Mint z "instalacji OEM" (upewnij się, że masz połączenie z Internetem, w przeciwnym razie mogą pojawić się błędy). Jeśli to zrobisz, musisz później kliknąć ikonę "Wyślij do użytkownika końcowego", która powinna znajdować się na pulpicie. Następnie należy zrestartować komputer i uruchomić system operacyjny tak, jakbyśmy otwierali komputer po raz pierwszy.


W tym przewodniku wyjaśniono, dlaczego możesz potrzebować dedykowanego komputera do transakcji Bitcoin i jak zainstalować na nim nowy system operacyjny Linux Mint.