---
name: Jade

description: Jak skonfigurować urządzenie JADE
---

![image](assets/cover.webp)


## Film instruktażowy


![video](https://www.youtube.com/watch?v=_U1jsTeqbTw)

Blockstream Jade - Mobile Bitcoin Hardware Wallet PEŁNY TUTORIAL by BTCsession


## Pełny przewodnik pisania


![image](assets/cover2.webp)


### Wymagania wstępne


1. Pobierz najnowszą wersję Blockstream Green.


2. Zainstaluj ten sterownik, aby upewnić się, że Jade jest rozpoznawany przez komputer.


### Konfiguracja pulpitu


![full guide](https://youtu.be/0fPVzsyL360)


Otwórz Blockstream Green, a następnie kliknij logo Blockstream w sekcji Urządzenia.


![image](assets/1.webp)


Podłącz Jade do komputera za pomocą dostarczonego kabla USB.


**Uwaga:** Jeśli Jade nie jest rozpoznawany przez komputer, upewnij się, że zainstalowane są niezbędne sterowniki, a także sprawdź, czy może to być spowodowane uprawnieniami USB.


Gdy Jade pojawi się w Green, zaktualizuj Jade, klikając Sprawdź aktualizacje i wybierz najnowszą wersję oprogramowania sprzętowego. Użyj kółka przewijania lub przełącznika na Jade, aby potwierdzić i kontynuować aktualizację. Upewnij się, że Jade nadal pokazuje przycisk "Initialize", w przeciwnym razie będziesz musiał poczekać do momentu skonfigurowania Jade, aby go zaktualizować. W razie potrzeby użyj przycisku Wstecz, aby przejść do tego ekranu.


![image](assets/2.webp)


Po zaktualizowaniu oprogramowania sprzętowego Jade wybierz opcję Konfiguracja Jade w sieci i zasady bezpieczeństwa, których chcesz używać.


**Wskazówka:** Polityka bezpieczeństwa jest wymieniona w sekcji Typ na ekranie logowania pokazanym poniżej. Jeśli nie masz pewności, czy wybrać Singlesig czy Multisig Shield, zapoznaj się z naszym przewodnikiem [tutaj](https://help.blockstream.com/hc/en-us/articles/4403642609433)


![image](assets/3.webp)


Następnie wybierz opcję utworzenia nowego Wallet i wybierz 12 słów jako frazę odzyskiwania generate. Kliknięcie przycisku Zaawansowane spowoduje wyświetlenie opcji 12- i 24-słownej frazy odzyskiwania.


![image](assets/4.webp)


Zapisz frazę odzyskiwania offline na papierze (lub za pomocą dedykowanego urządzenia do tworzenia kopii zapasowych frazy odzyskiwania dla dodatkowego bezpieczeństwa). Następnie użyj kółka lub przełącznika na górze Jade, aby zweryfikować frazę odzyskiwania. Ten krok gwarantuje, że fraza została zapisana poprawnie.


![image](assets/5.webp)


Ustaw i potwierdź sześciocyfrowy kod PIN. Służy on do odblokowywania Blockstream Jade przy każdym logowaniu do Wallet.


![image](assets/6.webp)


Teraz wystarczy wybrać opcję Przejdź do Wallet w aplikacji Green na pulpicie, aby zobaczyć Wallet otwarty na Blockstream Green. Blockstream Jade również pokaże, że jest gotowy! Możesz teraz używać Jade do wysyłania i odbierania transakcji Bitcoin.


![image](assets/7.webp)


Po zakończeniu korzystania z Wallet odłącz urządzenie Blockstream Jade od urządzenia. Następnym razem, gdy będziesz chciał użyć Wallet na Blockstream Jade, po prostu podłącz ponownie urządzenie i postępuj zgodnie z instrukcjami.


źródło: https://help.blockstream.com/hc/en-us/articles/17478506300825


### Dodatek A - Weryfikacja pliku do pobrania Green Wallet


Weryfikacja pobierania oznacza sprawdzenie, czy pobrany plik nie został zmodyfikowany od czasu jego udostępnienia przez dewelopera.


Robimy to, sprawdzając, czy podpis (wygenerowany przez klucz prywatny dewelopera) wraz z pobranym plikiem i kluczem publicznym dewelopera zwraca wynik TRUE podczas przechodzenia przez funkcję gpg -verify. Pokażę ci, jak to zrobić w następnej kolejności.


Najpierw otrzymujemy klucz podpisujący:


W przypadku systemu Linux otwórz terminal i uruchom to polecenie (powinieneś po prostu skopiować i wkleić tekst, dołączając cudzysłowy):


```bash
gpg --keyserver keyserver.ubuntu.com --recv-keys "04BE BF2E 35A2 AF2F FDF1 FA5D E7F0 54AA 2E76 E792"
```


W przypadku komputerów Mac należy zrobić to samo, ale najpierw trzeba pobrać i zainstalować pakiet GPG Suite.


W przypadku systemu Windows należy zrobić to samo, ale najpierw trzeba pobrać i zainstalować GPG4Win.


Otrzymasz wynik informujący, że klucz publiczny został zaimportowany.


![image](assets/9.webp)


Ten obraz ma pusty atrybut alt; jego nazwa pliku to image-3-1024x162.webp


Następnie musimy pobrać plik zawierający Hash oprogramowania. Jest on przechowywany na stronie GitHub firmy Blockstream. Najpierw przejdź do ich strony informacyjnej tutaj i kliknij link do "pulpitu". Spowoduje to przejście do strony najnowszej wersji w serwisie GitHub, a tam zobaczysz link do pliku SHA256SUMS.asc, który jest dokumentem tekstowym zawierającym opublikowany przez Blockstream Hash pobranego przez nas programu.


![image](assets/10.webp)


GitHub:


![image](assets/11.webp)


Nie jest to konieczne, ale po zapisaniu na dysku zmieniłem nazwę "SHA256SUMS.asc" na "SHA256.txt", aby łatwiej otworzyć plik na komputerze Mac za pomocą edytora tekstu. Tak wyglądała zawartość pliku:


![image](assets/12.webp)


Tekst, którego szukamy, znajduje się na górze. W zależności od tego, który plik pobraliśmy, istnieje odpowiedni wynik Hash, który porównamy później.


Dolna część dokumentu zawiera podpis złożony na powyższej wiadomości - to dwa w jednym pliku.


Kolejność nie ma znaczenia, ale przed sprawdzeniem Hash sprawdzimy, czy wiadomość Hash jest autentyczna (tj. nie została zmodyfikowana).


Otwórz terminal. Musisz znajdować się we właściwym katalogu, do którego został pobrany plik SHA256SUMS.asc. Zakładając, że został on pobrany do katalogu "Downloads", w przypadku systemów Linux i Mac należy przejść do tego katalogu (wielkość liter ma znaczenie):


```bash
cd Downloads
```


Oczywiście po tych poleceniach należy nacisnąć <enter>. W przypadku systemu Windows otwórz CMD (wiersz polecenia) i wpisz to samo (chociaż nie jest rozróżniana wielkość liter).


W przypadku systemów Windows i Mac konieczne było wcześniejsze pobranie odpowiednio GPG4Win i GPG Suite, zgodnie z wcześniejszymi instrukcjami. W przypadku systemu Linux, gpg jest dostarczany z systemem operacyjnym. Z Terminala (lub CMD dla Windows) wpisz to polecenie:


```bash
gpg --verify SHA256SUMS.asc
```


Dokładna pisownia nazwy pliku (na czerwono) może być inna w dniu pobrania pliku, więc upewnij się, że polecenie jest zgodne z pobraną nazwą pliku. Powinieneś otrzymać te dane wyjściowe i zignorować ostrzeżenie o zaufanym podpisie - oznacza to po prostu, że nie powiedziałeś ręcznie komputerowi, że ufasz kluczowi publicznemu, który zaimportowaliśmy wcześniej.


![image](assets/13.webp)


Ten obraz ma pusty atrybut alt; jego nazwa pliku to image-4-1024x165.webp


Wynik ten potwierdza, że podpis jest dobry i mamy pewność, że klucz prywatny "info@greenaddress.it" podpisał dane (raport Hash).


Teraz powinniśmy Hash nasz pobrany plik zip i porównać opublikowane dane wyjściowe. Zauważ, że w pliku SHA256SUMS.asc znajduje się fragment tekstu o treści "Hash: SHA512", co mnie dezorientuje, ponieważ plik wyraźnie zawiera dane wyjściowe SHA256, więc zamierzam to zignorować.


W przypadku komputerów Mac i Linux otwórz terminal, przejdź do miejsca, w którym pobrano plik zip (prawdopodobnie będziesz musiał ponownie wpisać "cd Downloads", chyba że od tego czasu nie zamykałeś terminala). Przy okazji zawsze możesz sprawdzić, w jakim katalogu się znajdujesz, wpisując PWD ("print working directory"), a jeśli to wszystko jest obce, warto obejrzeć krótki film na YouTube, wyszukując "jak poruszać się po systemie plików Linux/Mac/Windows".


Aby otworzyć plik, wpisz to:


```bash
shasum -a 256 BlockstreamGreen_MacOS_x86_64.zip
```


Powinieneś sprawdzić, jak dokładnie nazywa się twój plik i w razie potrzeby zmodyfikować tekst na niebiesko powyżej.


Otrzymasz następujące dane wyjściowe (twoje będą się różnić, jeśli plik jest inny niż mój):


![image](assets/14.webp)


Następnie wizualnie porównaj dane wyjściowe Hash z tym, co znajduje się w pliku SHA256SUMS.asc. Jeśli się zgadzają, to -> SUKCES! Gratulacje.


źródło: https://armantheparman.com/jade/


### Używanie go na Sparrow


Jeśli już wiesz, jak używać SParrow, to tak jak zawsze:


**Uwaga:** ten sam proces zachodzi na przykład w przypadku Spectera


Pobierz Sparrow za pomocą linku podanego tutaj.


![image](assets/14.5.webp)


Kliknij Dalej, aby postępować zgodnie z instrukcjami konfiguracji i dowiedzieć się więcej o różnych opcjach połączenia.


![image](assets/15.webp)


Wybierz żądany serwer, a następnie wybierz opcję Utwórz nowy Wallet.


![image](assets/16.webp)


Wprowadź nazwę swojego Wallet i kliknij Create Wallet.


![image](assets/17.webp)


Wybierz żądane zasady i typy skryptów, a następnie wybierz Connected Hardware Wallet.


**Uwaga:** Jeśli wcześniej korzystałeś z Blockstream Jade jako Singlesig Wallet z Blockstream Green i chcesz przeglądać swoje transakcje w Sparrow, upewnij się, że typ skryptu odpowiada typowi konta, na którym znajdują się Twoje środki w Green. Konieczne będzie również dopasowanie ścieżki derywacji.


![image](assets/18.webp)


Podłącz urządzenie Blockstream Jade i kliknij przycisk Skanuj. Następnie zostaniesz poproszony o wprowadzenie kodu PIN na Jade.


**Wskazówka:** Przed podłączeniem Jade, upewnij się, że aplikacja Blockstream Green nie jest otwarta. Jeśli Green jest otwarty, może to spowodować problemy z wykrywaniem Jade w Sparrow.


![image](assets/19.webp)


Wybierz Import Keystore, aby zaimportować klucz publiczny domyślnego konta lub wybierz strzałkę, aby ręcznie wybrać ścieżkę derywacji, której chcesz użyć.


![image](assets/20.webp)


Po zaimportowaniu żądanego klucza kliknij przycisk Zastosuj.


![image](assets/21.webp)


Pomyślnie skonfigurowałeś Wallet i możesz rozpocząć odbieranie, przechowywanie i wydawanie Bitcoin za pomocą Sparrow i Blockstream Jade.


**Uwaga:** Jeśli wcześniej korzystałeś z Jade z Blockstream Green jako Multisig Shield Wallet, nie powinieneś oczekiwać, że twój nowy Sparrow Wallet pokaże to samo saldo - są to różne portfele. Aby ponownie uzyskać dostęp do Multisig Shield Wallet, wystarczy podłączyć Jade z powrotem do Blockstream Green.


![image](assets/22.webp)


źródło: https://help.blockstream.com/hc/en-us/articles/7559912660761-How-do-I-use-Blockstream-Jade-with-Sparrow-


### Aplikacja Green


jeśli jesteś bardziej mobilnym przewodnikiem, możesz użyć go z Blockstream Green



- Jak skonfigurować Blockstream Jade z Green | Blockstream Jade - https://youtu.be/7aacxnc6DHg
- Jak podłączyć Bitcoin do Jade Wallet | Blockstream Jade - https://youtu.be/CVtcDdiPqLA