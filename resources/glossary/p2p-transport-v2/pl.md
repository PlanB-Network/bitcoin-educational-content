---
term: P2P TRANSPORT V2
---

Nowa wersja protokołu transportowego Bitcoin P2P zawierająca szyfrowanie oportunistyczne w celu zwiększenia prywatności i bezpieczeństwa komunikacji między węzłami. Ulepszenie to ma na celu rozwiązanie kilku problemów związanych z podstawową wersją protokołu P2P, w szczególności poprzez uczynienie wymienianych danych nierozróżnialnymi dla biernego obserwatora (takiego jak dostawca usług internetowych), zmniejszając w ten sposób ryzyko cenzury i ataków poprzez wykrywanie określonych wzorców w pakietach danych.


Zaimplementowane szyfrowanie nie obejmuje uwierzytelniania, aby uniknąć dodawania niepotrzebnej złożoności i nie zagrażać bezprawnemu charakterowi połączenia sieciowego. Ten nowy protokół transportowy P2P oferuje jednak lepsze zabezpieczenia przed atakami pasywnymi i sprawia, że ataki aktywne są znacznie bardziej kosztowne i wykrywalne (zwłaszcza ataki MITM). Wprowadzenie pseudolosowego strumienia danych komplikuje zadanie atakującym, którzy chcą cenzurować lub manipulować komunikacją.


P2P Transport V2 został włączony jako opcja (domyślnie wyłączona) w wersji 26.0 Bitcoin Core, wdrożonej w grudniu 2023 roku. Można go aktywować za pomocą opcji `v2transport=1` w pliku konfiguracyjnym.