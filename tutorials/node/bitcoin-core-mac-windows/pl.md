---
name: Bitcoin Core (macOS i Windows)
description: Instalacja Bitcoin Core na komputerach Mac lub Windows
---

Można zainstalować Bitcoin Core na zwykłym komputerze, ale nie jest to idealne rozwiązanie. Jeśli nie masz nic przeciwko pozostawieniu komputera włączonego 24/7, to będzie działać dobrze. W przypadku konieczności wyłączenia komputera irytujące staje się oczekiwanie na synchronizację oprogramowania przy każdym ponownym włączeniu.


Te instrukcje są przeznaczone dla użytkowników komputerów Mac lub Windows. Użytkownicy Linuksa najprawdopodobniej nie będą potrzebować mojej pomocy, ale instrukcje dla Linuksa są bardzo podobne do tych dla Maca.


## Start Clean


Najlepiej jest korzystać z czystego komputera, na którym nie ma złośliwego oprogramowania. Nawet jeśli korzystasz z Hardware Wallet, złośliwe oprogramowanie może wyłudzić monety.


Możesz wyczyścić stary komputer i używać go jako dedykowanego komputera Bitcoin lub kupić dedykowany komputer/laptop.


## Napęd Hard


Bitcoin Core zajmie około 400 gigabajtów danych na dysku i będzie nadal rosnąć. Możesz użyć dysku wewnętrznego, ale możesz też podłączyć zewnętrzny dysk Hard. Wyjaśnię obie opcje. Najlepiej byłoby użyć dysku półprzewodnikowego. Jeśli masz stary komputer, prawdopodobnie nie ma on takiego dysku wewnętrznego. Wystarczy kupić zewnętrzny dysk SSD o pojemności 1 lub 2 terabajtów i użyć go. Zwykły dysk prawdopodobnie będzie działał, ale możesz mieć problemy i będzie znacznie wolniejszy.


![image](assets/1.webp)


## Pobierz Bitcoin Core


Wejdź na Bitcoin.org (upewnij się, że nie wchodzisz na Bitcoin.com, która jest stroną z shitcoinami należącą do Rogera Vera, oszukującą ludzi, by kupili Bitcoin Cash zamiast Bitcoin)


Po wejściu na stronę nie jest oczywiste, skąd pobrać oprogramowanie. Przejdź do menu zasobów i kliknij "Bitcoin Core", jak pokazano poniżej:


![image](assets/2.webp)


Spowoduje to przejście do strony pobierania:


![image](assets/3.webp)


Kliknij pomarańczowy przycisk Pobierz Bitcoin Core:


![image](assets/4.webp)


Istnieje kilka opcji do wyboru, w zależności od komputera. Pierwsze dwie są istotne dla tego przewodnika; wybierz Windows lub Mac na pasku po lewej stronie. Po kliknięciu rozpocznie się pobieranie, najprawdopodobniej do katalogu Pobrane.


## Weryfikacja pobierania (część 1)


Potrzebny jest plik zawierający hashe różnych wydań. Plik ten znajdował się kiedyś na stronie pobierania Bitcoin.org, ale teraz został przeniesiony na bitcoincore.org/en/download:


![image](assets/5.webp)


Potrzebny jest plik skrótów binarnych SHA256. Plik ten zawiera skróty SHA256 różnych pakietów Bitcoin Core do pobrania.


Następnie musimy pobrać Hash z Bitcoin Core i porównać go z tym, co według pliku powinno być Hash. Wtedy wiemy, że pobrany plik jest identyczny z oczekiwanym, zgodnie z bitcoincore.org.


Przejdź ponownie do katalogu Downloads i wykonaj to polecenie (zamień znaki X dokładnie na nazwę pliku do pobrania Full node Bitcoin):


```bash
shasum -a 256 XXXXXXXXXXXX # <--- FOR MAC
certutil -hashfile XXXXXXXXXXX SHA256 # <--- FOR WINDOWS
```


Otrzymasz wynik Hash. Zanotuj go i porównaj z Hash zawartym w pliku SHA256SUMS.


Jeśli wyniki są identyczne, to zweryfikowałeś, że żaden bit danych nie został naruszony... prawie. Nadal musimy mieć pewność, że plik SHA256SUMS nie jest złośliwy.


Aby przejść do następnego kroku, musimy mieć zainstalowany gpg na naszym komputerze.


Aby to zrobić, zapoznaj się z moim przewodnikiem SHA256/gpg i przewiń mniej więcej do połowy sekcji "Pobierz gpg" i poszukaj podtytułu swojego systemu operacyjnego. Następnie wróć tutaj.


## Pobierz klucz publiczny


Wracając do strony pobierania, pobierz plik podpisów SHA256 Hash


![image](assets/6.webp)


Kliknij go i zapisz plik na dysku, najlepiej w katalogu Pobrane.


Plik ten zawiera podpisy różnych osób pod plikiem SHA256SUMS.


Chcemy, aby klucz publiczny głównego programisty, Wladimira J. van der Laana, znajdował się na breloku kluczy naszego komputera. Jego identyfikator klucza publicznego to:

1 - 01EA 5486 DE18 A882 D4C2 6845 90C8 019E 36C2 E964


Skopiuj ten tekst do poniższego polecenia:


```bash
gpg --keyserver hkp://keyserver.ubuntu.com --recv-keys 01EA5486DE18A882D4C2684590C8019E36C2E964
```


Z ciekawostek, w każdej chwili można sprawdzić, jakie klucze znajdują się w pęku kluczy komputera za pomocą tego polecenia:


```bash
gpg --list-keys
```


## Weryfikacja pobierania (część 2)


Mamy klucz publiczny, więc możemy teraz zweryfikować plik SHA256SUMS, który zawiera skróty pobranych plików Bitcoin Core i podpis dla tych skrótów.


Otwórz ponownie Terminal lub CMD i upewnij się, że znajdujesz się w katalogu Pobrane. Stamtąd wykonaj to polecenie:


```bash
gpg –verify SHA256SUMS.asc SHA256SUMS
```


Pierwszy wymieniony plik jest dokładną pisownią pliku podpisu. Drugi wymieniony plik powinien być dokładną pisownią pliku tekstowego zawierającego skróty. Oba pliki powinny znajdować się w tym samym katalogu i musisz być w katalogu plików, w przeciwnym razie musisz wpisać pełną ścieżkę dla każdego pliku.


Oto dane wyjściowe, które powinieneś otrzymać


![image](assets/7.webp)


Bezpiecznie jest zignorować komunikat OSTRZEŻENIE - to tylko przypomina ci, że nie spotkałeś Wladimira na kluczowej części i osobiście zapytałeś go, jaki jest jego klucz publiczny, a następnie powiedziałeś komputerowi, aby całkowicie zaufał temu kluczowi.


Jeśli otrzymałeś tę wiadomość, wiesz teraz, że plik SHA256SUMS.asc nie został zmodyfikowany po podpisaniu go przez Wladimira.


## Instalacja rdzenia Bitcoin


Nie powinieneś potrzebować szczegółowych instrukcji dotyczących instalacji programu.


![image](assets/8.webp)


## Rdzeń Bitcoin


Na komputerach Mac może pojawić się ostrzeżenie (Apple nadal jest przeciwne Bitcoin)


![image](assets/9.webp)


Kliknij OK, a następnie otwórz Preferencje systemowe


![image](assets/10.webp)


Kliknij ikonę Bezpieczeństwo i prywatność:


![image](assets/11.webp)


Następnie kliknij "Otwórz mimo to":


![image](assets/12.webp)


Błąd pojawi się ponownie, ale tym razem dostępny będzie przycisk OTWÓRZ. Kliknij go.


![image](assets/13.webp)


Bitcoin Core powinien się załadować i zostanie wyświetlonych kilka opcji:


![image](assets/14.webp)


Tutaj możesz wybrać domyślną ścieżkę, na którą zostanie pobrany Blockchain, lub możesz wybrać dysk zewnętrzny. Zalecam, aby nie zmieniać domyślnej ścieżki, jeśli zamierzasz korzystać z dysku wewnętrznego, ułatwia to konfigurację podczas instalowania innego oprogramowania do komunikacji z Bitcoin Core.


Możesz wybrać uruchomienie przyciętego węzła, oszczędza to miejsce, ale ogranicza możliwości węzła. Tak czy inaczej, będziesz pobierać cały Blockchain i weryfikować go, więc jeśli masz miejsce, zachowaj to, co pobrałeś i nie przycinaj, jeśli możesz tego uniknąć.


Po potwierdzeniu rozpocznie się pobieranie Blockchain. Zajmie to wiele dni.


![image](assets/15.webp)


Możesz wyłączyć komputer i wrócić do pobierania, jeśli chcesz, nie spowoduje to żadnych szkód.