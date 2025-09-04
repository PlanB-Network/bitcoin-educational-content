---
name: PureOS
description: Dystrybucja Linuksa, która zapewnia kontrolę nad cyfrowym życiem.
---

![cover](assets/cover.webp)



Ochrona danych osobowych w erze cyfrowej jest najwyższym priorytetem dla każdego użytkownika Internetu. Firmy, organizacje, a nawet systemy operacyjne są przydatnymi źródłami informacji do określenia profilu i stylu życia użytkownika. Wybór odpowiedniego systemu operacyjnego jest pierwszym krokiem do wzmocnienia prywatności online. W tym samouczku przyjrzymy się PureOS, dystrybucji Linuksa skoncentrowanej na prywatności.



https://planb.network/tutorials/computer-security/operating-system/debian-d09a57ec-8372-40ca-bcff-499415209e1f

## Rozpoczęcie pracy z PureOS



PureOS to oparty na Debianie system operacyjny opracowany przez firmę Purism. PureOS jest odpowiedni zarówno dla profesjonalistów IT, jak i użytkowników szukających prostej, łatwej w użyciu dystrybucji. Jego wyjątkowość polega na tym, że jest *wolnym oprogramowaniem* i koncentruje się na ochronie danych osobowych użytkowników, tworząc ramy oparte na prywatności, wolności, bezpieczeństwie i stabilności oferowanej przez Debiana.



### Dlaczego warto wybrać PureOS?





- Prosty, intuicyjny Interface**: GNOME oferuje przejrzysty pulpit Interface, zaprojektowany tak, aby był łatwy w użyciu, nawet dla osób, które nie czują się komfortowo z wierszem poleceń.





- Darmowy**: podobnie jak większość dystrybucji Linuksa, PureOS jest całkowicie darmowy. Dostępna jest jednak miesięczna subskrypcja wspierająca deweloperów.





- Bezpieczeństwo i stabilność**: Architektura i tryb pracy PureOS sprawiają, że jest to wysoce bezpieczna dystrybucja, gwarantująca ochronę danych i stabilność systemu.





- Dokumentacja i aktywna społeczność**: PureOS posiada przejrzystą, przystępną dokumentację i zaangażowaną, responsywną społeczność, co ułatwia rozwiązywanie problemów i naukę systemu krok po kroku.



## Instalacja i konfiguracja



Instalacja i konfiguracja PureOS na komputerze będzie wymagać następujących minimalistycznych funkcji:




- Klucz USB o pojemności co najmniej 8 GB do flashowania systemu.
- 4 GB RAM.
- 30 GB wolnego miejsca na dysku Hard.



Przejdź do [oficjalnej strony PureOS] (https://pureos.net/), a następnie pobierz obraz ISO systemu operacyjnego zgodnie z architekturą swojego komputera.



Aby uruchomić instalację PureOS, należy utworzyć bootowalny klucz USB za pomocą oprogramowania flash, takiego jak [Balena Etcher](https://www.balena.io/etcher).



W trzech prostych krokach można uruchomić pamięć USB z systemem operacyjnym PureOS.





- Podłącz klucz USB i uruchom pobrane oprogramowanie Balena.
- Następnie wybierz obraz ISO PureOS
- Wybierz klucz USB jako urządzenie wyjściowe, a następnie kliknij przycisk **Flash** i poczekaj na zakończenie procesu.



![0_01](assets/fr/01.webp)



Po uruchomieniu klucza USB uruchom ponownie komputer, na którym chcesz zainstalować PureOS.



Po uruchomieniu komputera należy uzyskać dostęp do BIOS-u, naciskając klawisz `ESC`, `F9` lub `F11`, w zależności od urządzenia. Wybierz klucz USB jako urządzenie rozruchowe, a następnie naciśnij `ENTER`, aby potwierdzić.



### Ekran startowy



PureOS oferuje kilka opcji uruchamiania systemu operacyjnego. Wybierz opcję **Test or Install PureOS**, aby uruchomić instalację systemu operacyjnego.



![0_02](assets/fr/02.webp)



Ustaw język i układ klawiatury, których chcesz używać na komputerze.



![0_03](assets/fr/03.webp)



![0_04](assets/fr/04.webp)



Zezwalaj lub odmawiaj dostępu do swojej **lokalizacji geograficznej** aplikacjom w celu uzyskania spersonalizowanych rekomendacji opartych na Twojej okolicy.



![0_05](assets/fr/05.webp)



Możesz połączyć się z istniejącym kontem **NextCloud**, aby pobrać dane powiązane z pakietem biurowym, którego używasz w innym systemie.



![0_06](assets/fr/06.webp)



Dostępny jest samouczek, ale możesz zamknąć okno, jeśli chcesz pominąć ten krok.



![0_08](assets/fr/08.webp)



### Uruchamianie instalacji



Kliknij menu **Activities** i zapoznaj się z aplikacjami i narzędziami preinstalowanymi w systemie. Kliknij **Install PureOS**, aby rozpocząć instalację



![0_09](assets/fr/09.webp)



Ustaw język systemu i układ klawiatury zgodnie z wymaganiami, a następnie skonfiguruj tryb partycjonowania dysku Hard.



![0_10](assets/fr/10.webp)



![0_11](assets/fr/11.webp)



![0_12](assets/fr/12.webp)



![0_13](assets/fr/13.webp)



Dostępne są dwie opcje partycjonowania dysku Hard:




- Wymaż dysk**: W celu pełnej instalacji systemu PureOS, usunięcie wszystkich wcześniej istniejących danych na dysku Hard.



![0_14](assets/fr/14.webp)





- Ręczne partycjonowanie** do tworzenia własnych wyników



⚠️ Podczas ręcznego tworzenia partycji dla systemu operacyjnego należy przydzielić co najmniej 2 GB partycji na działanie PureOS, a następnie kolejną partycję na dane.



![0_15](assets/fr/15.webp)



Aktywuj **szyfrowanie dysku**, jeśli chcesz zabezpieczyć swoje dane. Wprowadź silne, złożone hasło.



Aby zwiększyć bezpieczeństwo danych, należy powiązać użytkownika z systemem operacyjnym, definiując nazwę użytkownika i hasło alfanumeryczne składające się z co najmniej 20 znaków.



![0_16](assets/fr/16.webp)



Przejrzyj wprowadzone ustawienia i zmodyfikuj je w razie potrzeby.



![0_17](assets/fr/17.webp)



Kliknij **Install**, a następnie **Install Now**, aby potwierdzić, że PureOS został zainstalowany na komputerze.



![0_18](assets/fr/18.webp)



![0_19](assets/fr/19.webp)



Po zakończeniu instalacji zaznacz pole **Restart now**, aby ponownie uruchomić komputer, a następnie potwierdź:




- Język.
- Układ klawiatury.
- Konto NextCloud (opcjonalnie).



![0_25](assets/fr/25.webp)



## Aktualizacje



Przed rozpoczęciem korzystania z PureOS należy zaktualizować system. Umożliwi to korzystanie z najnowszych funkcji i poprawek bezpieczeństwa oraz zapewni większą stabilność.





- Aktualizacja poprzez grafikę Interface**:


Otwórz aplikację **Oprogramowanie**, a następnie przejdź do zakładki **Aktualizacje**. Dostępne aktualizacje zostaną wyświetlone automatycznie. Kliknij **Pobierz**, a następnie **Zainstaluj** po zakończeniu pobierania.





- Aktualizacja przez terminal**:


Otwórz terminal, a następnie wprowadź następujące polecenie, aby zaktualizować listę dostępnych pakietów:



```shell
sudo apt update
```



Wprowadź hasło i potwierdź. Następnie zainstaluj aktualizacje za pomocą:



```shell
sudo apt full-upgrade
```



## PureOS dla deweloperów



Domyślnie PureOS nie zawiera wszystkich narzędzi potrzebnych do programowania.


Można je szybko zainstalować za pomocą poniższego polecenia:



```shell
sudo apt install build-essential git curl
```



Spowoduje to zainstalowanie narzędzi do kompilacji **Git** i **Curl**, przydatnych w większości środowisk programistycznych.



## Środowisko PureOS



PureOS wyróżnia się innowacyjnym podejściem do prawdziwej konwergencji: jeden system operacyjny zapewnia płynne, bezproblemowe działanie na różnych urządzeniach, w tym laptopach, tabletach, mini-PC i smartfonach.



Aplikacje PureOS są zaprojektowane tak, aby były adaptacyjne: automatycznie dostosowują się do rozmiaru ekranu i trybu wprowadzania danych (dotyk lub klawiatura/mysz). Na przykład przeglądarka internetowa GNOME dynamicznie dostosowuje swój Interface, aby zapewnić optymalne wrażenia zarówno na urządzeniach mobilnych, jak i stacjonarnych.



PureOS zawiera również pakiet biurowy **LibreOffice**, który obejmuje:





- Writer**: kompletny edytor tekstu do tworzenia i edycji dokumentów.
- Calc**: potężny arkusz kalkulacyjny do zarządzania danymi i obliczeniami.
- Impress**: narzędzie do tworzenia profesjonalnych prezentacji.



Ten darmowy pakiet umożliwia wydajną pracę bez konieczności polegania na zastrzeżonym oprogramowaniu.



PureOS oferuje ujednolicone, bezpieczne i elastyczne środowisko, oparte w 100% na dystrybucji open source, która gwarantuje całkowitą kontrolę i ścisłe poszanowanie prywatności. Jego prawdziwa konwergencja ułatwia tworzenie aplikacji kompatybilnych z różnymi typami urządzeń, takimi jak komputery, tablety i smartfony, bez konieczności skomplikowanych adaptacji.



Dzięki natywnemu dostępowi do niezbędnych narzędzi, solidnym menedżerom pakietów i bogatemu ekosystemowi open-source, PureOS upraszcza tworzenie, testowanie i wdrażanie aplikacji w bezpiecznym środowisku. Jego stabilna architektura i Commitment do poufności sprawiają, że jest to niezawodna platforma do różnych zastosowań, w tym rozwoju Blockchain, szybkiego prototypowania lub środowisk produkcyjnych.



Odkryj nasz kurs na temat wzmacniania bezpieczeństwa i ochrony prywatności cyfrowej.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1