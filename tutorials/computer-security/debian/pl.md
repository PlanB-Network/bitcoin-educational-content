---
name: Debian
description: Dystrybucja Linuksa znana ze swojej stabilności, solidności i kompatybilności.
---

![cover](assets/cover.webp)



Debian to wolna dystrybucja GNU/Linuksa, znana ze swojej solidności i niezawodności. Jądro Linux i wszystkie jego pakiety są rygorystycznie testowane, aby zapewnić solidną stabilność i wysoki poziom bezpieczeństwa. Odpowiedni zarówno dla serwerów, jak i stacji roboczych, Debian oferuje łatwą obsługę i szeroki katalog oprogramowania. Niezależnie od tego, czy szukasz bezpiecznego systemu do codziennego użytku, czy środowiska produkcyjnego, Debian jest właściwym wyborem.



## Dlaczego warto wybrać Debiana?





- Darmowy i otwarty**: Debian jest całkowicie open source, co gwarantuje przejrzystość i brak opłat licencyjnych.
- Stabilność i bezpieczeństwo**: każde wydanie przechodzi dokładny proces testowania, dzięki czemu Debian jest jedną z najbardziej niezawodnych i bezpiecznych dystrybucji na rynku.
- Aktywna społeczność**: ogromna społeczność i obszerna dokumentacja są dostępne, aby zapewnić wsparcie zawsze, gdy tego potrzebujesz.
- Lekkość i skalowalność**: można zainstalować Debiana na maszynach o skromnych zasobach, zachowując dobrą wydajność.
- Obszerny katalog oprogramowania**: ponad 50 000 oficjalnych pakietów jest dostępnych za pośrednictwem repozytoriów.



## Wybierz grafikę Interface



Debian oferuje kilka środowisk graficznych, które można dostosować do swoich potrzeb:





- GNOME**: nowoczesny, intuicyjny Interface, idealny dla początkujących. Oferuje płynne, łatwe w użyciu menu graficzne umożliwiające dostęp do aplikacji.
- XFCE**: lekki i szybki, idealny dla mniej wydajnych maszyn.
- KDE Plasma**: wysoce konfigurowalny, z wyglądem podobnym do Windows.
- Cinnamon**: prosty, elegancki Interface, inspirowany systemem Windows.
- LXDE / LXQt**: ultralekki, odpowiedni dla starszych komputerów.
- MATE**: prosty i klasyczny, zbliżony do starego GNOME.



dla wygodnego, łatwego chwytu, **GNOME jest wysoce zalecane**.



## Instalacja i konfiguracja Debiana


### Wymagania sprzętowe



Przed rozpoczęciem instalacji upewnij się, że posiadasz następujący sprzęt:





- Klucz USB**: minimum 8 GB do przechowywania bootowalnego obrazu ISO.
- Pamięć o dostępie swobodnym (RAM)**: 4 GB dla płynnej instalacji i działania.
- Miejsce na dysku**: co najmniej 15 GB wolnego miejsca na system i aktualizacje.



### Pobierz



Wybór obrazu Debiana zależy od architektury procesora:





- AMD64**: pobierz edycję "live hybrid" z listy [download] (https://debian.obspm.fr/debian-cd/12.11.0-live/amd64/iso-hybrid/).
- ARM64**: pobierz obraz DVD z oficjalnej strony [Debiana] (https://debian.obspm.fr/debian-cd/12.11.0/arm64/iso-dvd/).
- Inne architektury**: znajdź ISO odpowiadające twojej architekturze [tutaj](https://debian.obspm.fr/debian-cd/12.11.0/).



![download](assets/fr/01.webp)



### Tworzenie bootowalnego klucza USB



Po pobraniu odpowiedniego obrazu ISO należy przystąpić do tworzenia nośnika instalacyjnego:




- Pobierz Balena Etcher** z [oficjalnej strony internetowej] (https://etcher.balena.io/), a następnie pobierz plik binarny dla swojego systemu i zainstaluj go.



![etcher](assets/fr/02.webp)





- Uruchom Etcher**: otwórz oprogramowanie i wybierz wcześniej pobrany obraz ISO Debiana.
- Wybierz klucz USB**: określ klucz (8 GB+) jako cel.
- Uruchom flash**: kliknij **Flash!** i poczekaj na zakończenie procesu.



![flash](assets/fr/03.webp)



Klucz USB jest teraz gotowy do rozpoczęcia instalacji Debiana.



## Instalacja Debiana w systemie



### Uruchamianie z klucza USB



Aby uruchomić instalację z klucza USB:




- Całkowite wyłączenie** komputera.
- Uruchom ponownie komputer**, a następnie uzyskaj dostęp do BIOS/UEFI, naciskając klawisze `ESC`, `F2`, `F11` (lub dedykowany klawisz w zależności od marki).
- W menu rozruchowym **wybierz klucz USB** jako urządzenie rozruchowe.
- Potwierdź** klawiszem Enter, aby uruchomić obraz Debiana: spowoduje to przejście do ekranu powitalnego instalatora.



### Uruchamianie instalacji



Ekran startowy:



![starting](assets/fr/04.webp)



Podczas uruchamiania z pamięci USB ekran powitalny Debiana oferuje kilka opcji:




- Live System**: uruchamia Debiana bez instalacji, idealny do testowania środowiska.
- Start Installer**: rozpoczyna instalację bezpośrednio na dysku Hard.
- Zaawansowane opcje instalacji**: zapewniają dostęp do niestandardowych trybów instalacji.



Aby zapoznać się z Debianem w trybie na żywo, wybierz **System na żywo** i potwierdź przyciskiem **Enter**. Następnie możesz uruchomić instalację, klikając **Install Debian** w środowisku na żywo.



![system](assets/fr/05.webp)





- Wybór języka** (opcjonalnie)



Wybierz z listy główny język systemu Debian, a następnie kliknij OK.



![language](assets/fr/06.webp)





- Strefa czasowa** (GMT)



Wybierz strefę geograficzną, aby automatycznie ustawić datę i godzinę.



![timezone](assets/fr/07.webp)





- Układ klawiatury



Wybierz język i układ klawiatury. Użyj wbudowanego pola testowego, aby sprawdzić, czy każdy klawisz generuje oczekiwany znak.



![keyboard](assets/fr/08.webp)



### Podział dysku na partycje





- Wymaż dysk**: jeśli masz dedykowaną partycję, ta opcja usunie całą jej zawartość.
- Ręczne partycjonowanie**: wybierz tę opcję, aby utworzyć, zmienić rozmiar lub usunąć partycje zgodnie z wymaganiami.



![disk](assets/fr/09.webp)





- Tworzenie konta użytkownika



Wprowadź swoje imię i nazwisko, nazwę konta i silne hasło, aby zapewnić bezpieczeństwo sesji.



![user](assets/fr/10.webp)





- Podsumowanie parametrów**



Wyświetlone zostanie podsumowanie dokonanych wyborów: sprawdź każdy element i w razie potrzeby wróć do jego modyfikacji.



![settings](assets/fr/11.webp)





- Uruchamianie instalacji



Kliknij **Install**, aby rozpocząć kopiowanie plików i konfigurację systemu, a następnie poczekaj na zakończenie procesu.



![install](assets/fr/12.webp)





- Restart**



Po zakończeniu instalacji uruchom ponownie komputer, aby zastosować wszystkie konfiguracje i uzyskać dostęp do nowego systemu Debian.



![restart](assets/fr/13.webp)



Podczas uruchamiania należy wprowadzić nazwę użytkownika i hasło dostępu do systemu.



![login](assets/fr/14.webp)



## Aktualizacja systemu



Przed rozpoczęciem korzystania z systemu należy go zaktualizować. Pozwala to na korzystanie z najnowszych poprawek oprogramowania, aktualnych repozytoriów, a w niektórych przypadkach poprawek zabezpieczeń samego systemu operacyjnego.



### Opcja 1: Aktualizacja za pomocą graficznego Interface (GNOME)



Jeśli zainstalowałeś Debiana ze środowiskiem graficznym GNOME, możesz przeprowadzać aktualizacje graficznie. Aby to zrobić, otwórz aplikację **Oprogramowanie**, a następnie przejdź do zakładki **Aktualizacje**. Następnie kliknij **Restart and update**, aby rozpocząć proces.



### Opcja 2: Aktualizacja przez terminal (zalecane)



Ta metoda oferuje pełniejszą kontrolę. Umożliwia aktualizację repozytoriów, pakietów oprogramowania i, w razie potrzeby, jądra.




- Otwórz terminal za pomocą skrótu klawiszowego `Ctrl + Alt + T`.
- Zaktualizuj listę dostępnych pakietów za pomocą poniższego polecenia:



```shell
sudo apt update
```



Po wyświetleniu monitu wprowadź hasło (pamiętaj, że podczas wpisywania nie będą wyświetlane żadne znaki - jest to normalne).





- Aby zainstalować dostępne aktualizacje:



```shell
sudo apt full-upgrade
```



## Odkryj podstawowe zadania



### Przeglądanie Internetu



Domyślną przeglądarką na Debianie jest **Firefox**. Jeśli wolisz inną przeglądarkę, możesz zainstalować inną, pod warunkiem, że jest dostępna w repozytoriach Debiana (np. Chromium, Brave...).



### Przetwarzanie tekstu



Pakiet **LibreOffice** jest domyślnie zainstalowany na Debianie.





- Do pisania dokumentów służy **LibreOffice Writer**, odpowiednik programu Microsoft Word.
- W przypadku arkuszy kalkulacyjnych, **LibreOffice Calc** działa jako alternatywa dla Excela.
- Wreszcie, **LibreOffice Impress** pozwala tworzyć prezentacje, podobnie jak PowerPoint.



## Instalowanie aplikacji



Istnieją dwa sposoby instalowania aplikacji na Debianie:



### Metoda graficzna:



Możesz użyć **menedżera oprogramowania** (dostępnego za pośrednictwem graficznego Interface), aby łatwo wyszukiwać i instalować aplikacje.



### Metoda wiersza poleceń:



Jeśli aplikacja, której szukasz, nie pojawia się w graficznym Interface lub jeśli wolisz terminal, użyj następującego polecenia:



```shell
sudo apt install <name>
```



Zastąp `<nazwa>` nazwą pakietu. Na przykład, aby zainstalować `curl`:



```shell
sudo apt install curl
```



### Instalowanie ręcznie pobranego pakietu:



Jeśli pobrałeś plik `.deb` (pakiet Debiana), możesz go zainstalować za pomocą następującego polecenia:



```shell
sudo apt install ./name.deb
```



https://planb.network/tutorials/computer-security/operating-system/lynis-1cf865b3-a352-4dd2-94d2-f17fa65547af

System Debian jest teraz zainstalowany i gotowy do użycia w codziennych zadaniach.


Dzięki środowisku graficznemu **GNOME** można uzyskać dostęp do szerokiej gamy aplikacji za pośrednictwem przyjaznego dla użytkownika graficznego Interface, idealnego zarówno dla początkujących, jak i zaawansowanych użytkowników.



Możliwa jest również zmiana środowiska graficznego (np. na XFCE, KDE itp.) bez konieczności ponownej instalacji Debiana. Aby to zrobić, wystarczy użyć terminala i zainstalować nowe środowisko.



Aby dowiedzieć się więcej o Debianie i ogólnie o dystrybucjach GNU/Linux, polecam zapoznać się z tym kursem:



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1