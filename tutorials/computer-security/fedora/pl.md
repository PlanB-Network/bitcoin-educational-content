---
name: Fedora
description: Dystrybucja Linuksa, która zapewnia darmową, kompletną i bezpieczną przestrzeń roboczą.
---


![cover](assets/cover.webp)





Fedora to darmowy, oparty na otwartym kodzie źródłowym system operacyjny Linux wprowadzony na rynek w 2003 roku, opracowany przez społeczność **Fedora Project** i wspierany przez **Red Hat Linux**. Jest znany ze swojej stabilności, dobrej wydajności i łatwości użytkowania, co czyni go doskonałym wyborem zarówno dla początkujących, jak i zaawansowanych użytkowników. System działa na większości nowoczesnych architektur procesorów, dzięki czemu można go łatwo zainstalować na praktycznie każdym komputerze. Fedora jest również dostępna w kilku wstępnie skonfigurowanych edycjach, zwanych "Fedora Spins" lub "Fedora Editions", zaprojektowanych do konkretnych potrzeb (gry wideo, astronomia, rozwój...).



## Architektura Fedora Linux



Jak przeczytałeś wcześniej, Fedora jest wolnym systemem operacyjnym opartym na jądrze Linux. Jądro Linux jest częścią systemu operacyjnego, która komunikuje się ze sprzętem komputerowym i zarządza zasobami systemowymi, takimi jak pamięć i moc obliczeniowa.



Fedora Linux zawiera różnorodne narzędzia programowe i aplikacje, które są wymagane do uruchomienia systemu operacyjnego na jądrze Linux. Modułowa architektura Fedory oznacza, że składa się ona głównie z kolekcji pojedynczych komponentów, które można łatwo dodawać, usuwać lub wymieniać w zależności od potrzeb. Pozwala to na kształtowanie systemu operacyjnego przy użyciu tylko potrzebnych zasobów.



Fedora zawiera również środowisko graficzne, które jest Interface, za pomocą którego użytkownicy wykonują zadania i uzyskują dostęp do aplikacji. Domyślnym środowiskiem graficznym Fedory jest GNOME, przyjazne dla użytkownika, łatwe w użyciu i wysoce konfigurowalne środowisko graficzne.



## Dlaczego warto wybrać Fedorę?



Wśród wielu dostępnych dystrybucji Linuksa, Fedora wyróżnia się w szczególności:





- Modułowość**: Kompatybilna z różnymi architekturami procesorów, Fedora może być zainstalowana na większości komputerów, nawet tych o niskiej mocy, dostosowując się idealnie do Twoich potrzeb.





- Prosty, intuicyjny Interface**: Fedora łączy nowoczesny graficzny Interface z potężnym Interface wiersza poleceń, dzięki czemu jest łatwy w użyciu dla wszystkich profili.





- Stabilność jądra**: Fedora, oparta na Red Hat, jest znana z niezawodności swoich aktualizacji, zwłaszcza aktualizacji jądra, które są przeprowadzane bez większych błędów dzięki bezpłatnemu wkładowi dużej społeczności.





- Szybka i łatwa instalacja**: dzięki rozmiarowi obrazu wynoszącemu zaledwie 3 GB instalacja jest szybka i łatwa, nawet na komputerach z ograniczonymi zasobami.



## Wydania Fedory



W zależności od profilu i sposobu użytkowania, Fedora oferuje edycje dostosowane do potrzeb użytkownika. Dostępne są głównie:





- Fedora Workstation**: Idealna do użytku osobistego i/lub profesjonalnego na komputerach, ta edycja jest instalowana z ogólnymi narzędziami, takimi jak przeglądarki, pakiet biurowy (edytory tekstu) i oprogramowanie do odtwarzania multimediów.





- Fedora Server**: Ta edycja jest poświęcona zarządzaniu serwerami. Fedora Server zawiera szereg narzędzi ułatwiających wdrażanie i zarządzanie serwerami na własną skalę.





- Fedora CoreOS**: Chcesz łatwo uruchamiać i wdrażać aplikacje chmurowe? Fedora CoreOS to edycja, która zapewnia narzędzia do tworzenia i zarządzania obrazami, na przykład za pomocą Docker i Kubernets.



W tym samouczku zajmiemy się edycją Fedora Workstation. Jednak procesy opisane poniżej są podobne dla innych edycji.



## Instalacja i konfiguracja Fedora Workstation



Instalacja Fedora Workstation wymaga następującej konfiguracji sprzętowej:




- Klucz USB o pojemności co najmniej **8 GB** do uruchomienia systemu operacyjnego.
- Co najmniej **40 GB wolnego miejsca** na dysku Hard komputera.
- 4 GB pamięci RAM** dla płynnego działania.



### Pobierz Fedora Workstation



Wersję [Fedora Workstation] (https://fedoraproject.org/fr/workstation/download) można pobrać z oficjalnej strony projektu Fedora. Następnie należy wybrać wersję odpowiadającą posiadanej architekturze procesora (32-bit - 64-bit) i kliknąć ikonę **Download**.



![download](assets/fr/01.webp)



![telecharger](assets/fr/02.webp)


### Utwórz bootowalny klucz USB



Aby zainstalować Fedorę, należy utworzyć bootowalny klucz USB za pomocą oprogramowania takiego jak [Balena Etcher](https://etcher.balena.io/).



![flashOs](assets/fr/03.webp)



![flash](assets/fr/04.webp)



Po zakończeniu instalacji Balena Etcher, otwórz aplikację i wybierz pobrany obraz ISO Fedora Workspace. Wybierz klucz USB jako nośnik docelowy i kliknij przycisk **Flash**, aby rozpocząć tworzenie klucza startowego.



![boot](assets/fr/05.webp)


### Instalacja Fedory



Po zakończeniu uruchamiania klucza USB wyłącz komputer.


Włącz komputer, a następnie uzyskaj dostęp do BIOS-u podczas uruchamiania, naciskając klawisz `F2`, `F12` lub `ESC`, w zależności od komputera.



W opcjach rozruchu wybierz klucz USB jako główne urządzenie rozruchowe. Po potwierdzeniu tego wyboru komputer uruchomi się ponownie i automatycznie uruchomi instalator Fedory** znajdujący się na kluczu USB.



Po uruchomieniu komputera z pamięci USB pojawi się ekran **GRUB**.



Na tym etapie dostępne są następujące opcje:




- Testuj nośnik**: Ta opcja umożliwia sprawdzenie integralności pamięci USB i upewnienie się, że wszystkie zależności wymagane do prawidłowej instalacji są obecne. Jest to krok opcjonalny, ale zalecany w przypadku jakichkolwiek wątpliwości dotyczących pamięci USB.



![install](assets/fr/06.webp)



![testing](assets/fr/07.webp)





- Uruchom Fedorę**: Uruchamia Fedorę w trybie "live", bez instalacji.



Na pulpicie Fedory (tryb live) kliknij **Install Fedora** (lub Install on Hard disk), aby rozpocząć proces instalacji. Możesz wybrać późniejszą instalację i przetestować Fedorę bez konieczności jej instalowania.



![install-live](assets/fr/08.webp)



Pierwszym krokiem jest wybranie **języka instalacji** i **układu klawiatury** Fedory



![language](assets/fr/10.webp)





- Wybór dysku instalacyjnego:



Wybierz dysk Hard, na którym chcesz zainstalować Fedorę.



Jeśli dysk jest pusty, Fedora automatycznie wykorzysta całą dostępną przestrzeń. W przeciwnym razie można dostosować partycjonowanie (ręczne lub automatyczne).



![disk](assets/fr/11.webp)





- Szyfrowanie:



Na tym etapie Fedora sugeruje zaszyfrowanie dysku, aby dodać dodatkowy Layer bezpieczeństwa. Gwarantuje to, że dane mogą być odczytywane tylko przez system Fedora.



![chiffrement](assets/fr/12.webp)



Przed rozpoczęciem instalacji Fedora wyświetli podsumowanie dokonanych wyborów. Potwierdź i kliknij przycisk instalacji, aby rozpocząć instalację Fedory.



![resume](assets/fr/13.webp)



Podczas instalacji Fedora kopiuje pliki i konfiguruje system. Po zakończeniu komputer uruchamia się ponownie automatycznie.



![installation](assets/fr/14.webp)



### Podstawowa konfiguracja


Przy pierwszym użyciu należy sfinalizować kilka ustawień:




- W razie potrzeby zmień język systemu.



![language](assets/fr/15.webp)





- Wybierz układ klawiatury odpowiadający Twoim preferencjom.



![keyboard](assets/fr/16.webp)





- Wybierz swoją strefę czasową, wpisując nazwę miasta w pasku wyszukiwania, a następnie kliknij odpowiednią sugestię.



![timezone](assets/fr/17.webp)





 - Włącz lub wyłącz dostęp do swojej pozycji dla aplikacji, które tego potrzebują, a także automatyczne wysyłanie raportów o błędach.



![location](assets/fr/18.webp)





- Zdecyduj, czy chcesz włączyć repozytoria oprogramowania innych firm.



![logs](assets/fr/19.webp)





- Wprowadź swoje imię i nazwisko oraz zdefiniuj nazwę użytkownika dla swojego konta.



![name](assets/fr/20.webp)





- Utwórz bezpieczne hasło do swojej sesji: jak najdłuższe (minimum 20 znaków), jak najbardziej losowe i zawierające różne znaki (małe i wielkie litery, cyfry i symbole). Pamiętaj, aby zapisać swoje hasło.



![mdp](assets/fr/21.webp)



Po wykonaniu wszystkich tych kroków uruchom Fedorę i zacznij z niej korzystać natychmiast, bez konieczności ponownego uruchamiania komputera.



![welcome](assets/fr/22.webp)



![start](assets/fr/23.webp)



Po zakończeniu instalacji można skonsultować się z domem Interface za pomocą kilku wstępnie zainstalowanych narzędzi.



![install-now](assets/fr/09.webp)



## Odkryj podstawowe zadania



### Przeglądanie Internetu


Domyślną przeglądarką Fedory jest **Firefox**. Jest łatwa w użyciu i odpowiednia dla większości potrzeb.


Jeśli wolisz inną przeglądarkę, możesz zainstalować ją z **menedżera oprogramowania** lub przez **terminal**.


### Przetwarzanie tekstu


Fedora domyślnie zawiera pakiet biurowy **LibreOffice**, który oferuje kilka przydatnych narzędzi:




- Writer** do przetwarzania tekstu.
- Calc** dla arkuszy kalkulacyjnych.
- Impress** do tworzenia prezentacji.


## Instalowanie aplikacji


Aby zainstalować nowe aplikacje, można użyć **menedżera oprogramowania** Fedory (zwanego _Software_), który sprawia, że instalacja jest łatwa i wizualna.  Jednakże, używanie **terminala** jest często szybsze i dokładniejsze.



Przed instalacją jakiegokolwiek oprogramowania, zawsze pamiętaj o aktualizacji **repozytoriów**, aby upewnić się, że masz dostęp do najnowszych dostępnych wersji.



Następnie użyj następującego polecenia, aby uruchomić instalację żądanej aplikacji:


sudo dnf install nazwa_oprogramowania`


## Aktualizacja systemu operacyjnego


Po instalacji ważne jest, aby zaktualizować Fedorę, aby skorzystać z najnowszych poprawek bezpieczeństwa i aktualizacji oprogramowania.


### Opcja 1: poprzez grafikę Interface




- Otwórz **Ustawienia** Fedory, a następnie przejdź do sekcji **System**.
- Kliknij na **Aktualizacja oprogramowania**.
- Rozpocznij pobieranie aktualizacji i poczekaj na zakończenie procesu.



Po zainstalowaniu aktualizacji może być wymagany **restart**.


### Opcja 2: Przez terminal




- Otwórz terminal i zacznij od aktualizacji **repozytoriów**, aby upewnić się, że masz najnowsze wersje:



```shell
sudo dnf check-update
```





- Następnie zaktualizuj całe zainstalowane oprogramowanie za pomocą następującego polecenia:



```shell
sudo dnf upgrade
```



Teraz Twój system Fedora jest aktualny i gotowy do użycia we wszystkich codziennych zadaniach. Zapoznaj się z naszym samouczkiem na temat Linux Mint, innej dystrybucji Linuksa, i dowiedz się, jak skonfigurować zdrowe i bezpieczne środowisko dla transakcji Bitcoin.



https://planb.network/tutorials/computer-security/operating-system/linux-mint-da44852e-513f-4004-949a-8fde60c1bca5