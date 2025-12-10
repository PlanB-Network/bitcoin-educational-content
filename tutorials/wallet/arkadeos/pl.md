---
name: ArkadeOS
description: Kompletny przewodnik po portfolio Arkade i Ark Protocol
---

![cover](assets/cover.webp)



Sieć Bitcoin stoi przed poważnym wyzwaniem: skalowalnością. Podczas gdy główna warstwa (warstwa 1) oferuje niezrównane bezpieczeństwo i decentralizację, może obsługiwać tylko ograniczoną liczbę transakcji na sekundę. Lightning Network pojawił się jako obiecujące rozwiązanie drugiej warstwy (warstwa 2), umożliwiające szybkie i tanie płatności. Lightning nakłada jednak własne ograniczenia: zarządzanie kanałami, potrzebę płynności przychodzącej i złożoność techniczną, która może zniechęcić nowych użytkowników.



Jest to tło dla **Ark**, nowego protokołu warstwy 2 zaprojektowanego w celu zaoferowania uproszczonego doświadczenia użytkownika bez poświęcania suwerenności. **ArkadeOS** (lub Arkade) to pierwsza duża implementacja tego protokołu, oferująca portfolio Bitcoin nowej generacji.



Ten samouczek poprowadzi Cię przez świat Arkade. Zbadamy, jak działa protokół Ark, jak zainstalować i skonfigurować Arkade wallet oraz jak używać go do wysyłania i odbierania bitcoinów natychmiast, poufnie i bez zwykłych tarć Lightning Network.



## Zrozumienie protokołu Ark



Zanim zagłębimy się w korzystanie z Arkade, konieczne jest zrozumienie kluczowych koncepcji protokołu Ark, który go napędza. Ark nie jest oddzielnym blockchainem, ale inteligentnym mechanizmem koordynacji na szczycie Bitcoin.



### Koncepcja VTXO


Sercem Ark jest **VTXO** (wirtualny UTXO). VTXO to UTXO, który nie został jeszcze opublikowany na blockchainie Bitcoin: istnieje poza głównym łańcuchem (off-chain), ale jest wspierany przez transakcje wstępnie podpisane na blockchainie.



W przeciwieństwie do salda na scentralizowanej giełdzie, VTXO naprawdę należy do ciebie. Posiadasz dowód kryptograficzny, który pozwala ci w dowolnym momencie zażądać odpowiednich prawdziwych bitcoinów w łańcuchu bloków, nawet jeśli serwer Ark zniknie. VTXO umożliwiają natychmiastowy transfer wartości między użytkownikami bez czekania na potwierdzenie bloku.



### Rola dostawcy usług ASP (Ark Service Provider)


Protokół Ark działa w modelu klient-serwer. Serwer nazywany jest **ASP** (Ark Service Provider). ASP odgrywa rolę przewodnika:




- Zapewnia niezbędną płynność dla sieci.
- Koordynuje transakcje między użytkownikami.
- Organizuje "rundy" rozliczeniowe na blockchainie.



Ważne jest, aby pamiętać, że ASP jest **bezprawny**. Nigdy nie przechowuje kluczy prywatnych użytkownika ani nie może ukraść jego środków. Jego rola jest czysto techniczna i logistyczna. Jeśli ASP cenzuruje twoje transakcje lub przestaje działać, zawsze możesz odzyskać swoje środki za pomocą jednostronnej procedury wyjścia.



### Rundy i prywatność


Transakcje na Ark są finalizowane w partiach zwanych **Rounds**. Okresowo (np. co kilka sekund) ASP zbiera wszystkie oczekujące transakcje i zakotwicza je na blockchainie Bitcoin w pojedynczej zoptymalizowanej transakcji.


Mechanizm ten oferuje dwie główne zalety:




- Skalowalność**: Pojedyncza transakcja on-chain może zatwierdzić tysiące płatności off-chain, drastycznie zmniejszając koszty dla użytkowników.
- Poufność**: Każda runda działa jak **CoinJoin**. Środki od wszystkich uczestników są mieszane we wspólnej puli, a następnie redystrybuowane w postaci nowych VTXO. Powoduje to zerwanie połączenia między nadawcą a odbiorcą, co sprawia, że śledzenie płatności przez zewnętrznego obserwatora jest niezwykle trudne, jeśli nie niemożliwe.



## Prezentacja ArkadeOS



ArkadeOS to konkretna aplikacja, która udostępnia protokół Ark ogółowi społeczeństwa. Opracowany przez Ark Labs, jest kompletnym ekosystemem obejmującym portfolio (Wallet), serwer (Operator) i narzędzia programistyczne.



Dla użytkownika końcowego Arkade przybiera formę eleganckiego, intuicyjnego wallet (PWA - Progressive Web App). Ukrywa kryptograficzną złożoność VTXO i rund za znanym interfejsem. Dzięki Arkade masz adres do odebrania, przycisk do wysłania i historię transakcji, tak jak klasyczny wallet, ale z mocą natychmiastowości i poufności Ark.



## Instalacja i konfiguracja



Ponieważ Arkade jest progresywną aplikacją internetową, jest szczególnie łatwa w instalacji i niekoniecznie wymaga tradycyjnych sklepów z aplikacjami.



### Dostęp i instalacja


Dostęp do Arkade można uzyskać bezpośrednio z dowolnej nowoczesnej przeglądarki internetowej (Chrome, Safari, Brave) na komputerze lub telefonie komórkowym.





- Odwiedź oficjalną stronę aplikacji: **[arkade.money](https://arkade.money)**.



![arkade homepage](assets/fr/01.webp)



Zostaniesz powitany przez serię ekranów wprowadzających w kluczowe koncepcje Arkade: nowy ekosystem dla Bitcoin, znaczenie samodzielnego przechowywania i korzyści płynące z transakcji wsadowych.



![arkade onboarding](assets/fr/02.webp)





- W systemie Android (Chrome/Brave)** : Naciśnij menu przeglądarki (trzy kropki) i wybierz "Zainstaluj aplikację" lub "Dodaj do ekranu głównego".
- W systemie iOS (Safari)**: Naciśnij przycisk udostępniania (kwadrat ze strzałką w górę) i wybierz opcję "Na ekranie głównym".



Po zainstalowaniu, Arkade uruchamia się jak natywna aplikacja, na pełnym ekranie i bez paska adresu.



### Tworzenie portfolio


Przy pierwszym uruchomieniu zostaniesz poproszony o skonfigurowanie swojego portfolio.





- Kliknij na **"Create New Wallet"**.



![create wallet](assets/fr/03.webp)





- wallet jest tworzony natychmiastowo. W przeciwieństwie do tradycyjnych portfeli Bitcoin, **Arkade nie używa 12- lub 24-wyrazowej frazy odzyskiwania**. Zamiast tego Arkade automatycznie generuje **klucz prywatny** w formacie Nostr (nsec), który będzie używany do tworzenia kopii zapasowych i przywracania wallet. Pamiętaj, aby natychmiast zapisać ten klucz (patrz następna sekcja).





- Pojawi się ekran "Your new wallet is live!", potwierdzający, że wallet jest gotowy do użycia. Kliknij **"GO TO WALLET "**, aby uzyskać dostęp do głównego interfejsu.



Po wejściu do wallet zostaniesz przeniesiony do głównego interfejsu Arkade. Znajdziesz tu swoje saldo, przyciski do wysyłania i odbierania środków oraz zakładkę "Aplikacje", która daje dostęp do zintegrowanych aplikacji, takich jak Boltz (giełda Lightning), LendaSat i LendaSwap (usługi pożyczkowe) oraz Fuji Money (aktywa syntetyczne).



![wallet interface](assets/fr/04.webp)



### Połączenie z ASP


Domyślnie portfolio jest automatycznie skonfigurowane do łączenia się z oficjalnym serwerem Arkade Labs ASP. Możesz sprawdzić, z którym serwerem jesteś połączony, przechodząc do **Ustawienia** > **Informacje**, gdzie zobaczysz adres serwera (obecnie `https://arkade.computer`).



W obecnej wersji Arkade (Beta) nie ma możliwości ręcznej modyfikacji serwera ASP. Aplikacja automatycznie łączy się z oficjalnym serwerem Arkade Labs ASP. W przyszłości użytkownicy będą mogli wybierać między różnymi ASP zgodnie z własnymi preferencjami, ale ta funkcja nie jest jeszcze dostępna.



### Tworzenie kopii zapasowej klucza prywatnego


**Arkade używa klucza prywatnego w formacie Nostr (nsec) jako metody tworzenia kopii zapasowych i odzyskiwania. Aby utworzyć kopię zapasową klucza prywatnego :





- Przejdź do **Ustawień** na ekranie głównym.
- Wybierz **"Kopia zapasowa i prywatność "**.
- Zobaczysz swój **prywatny klucz** wyświetlony w formacie `nsec...`. Ten długi ciąg znaków jest jedynym sposobem na przywrócenie wallet.
- Naciśnij **"COPY NSEC TO CLIPBOARD "**, aby skopiować klucz prywatny.
- Przechowuj ten klucz w bezpiecznym miejscu**: zapisz go na papierze, przechowuj w bezpiecznym menedżerze haseł lub użyj innej metody tworzenia kopii zapasowych, która Ci odpowiada.
- Arkade oferuje również opcję **"Włącz kopie zapasowe Nostr "**. Ta funkcja wykorzystuje protokół Nostr (zdecentralizowaną sieć) do automatycznego tworzenia kopii zapasowych niektórych danych z wallet w postaci zaszyfrowanej do przekaźników Nostr. Ułatwia to synchronizację między wieloma urządzeniami i oferuje prostsze odzyskiwanie stanu wallet.



**Ważne**: Kopie zapasowe Nostr są tylko **wygodną** funkcją. Nie zastępują one kopii zapasowej klucza nsec. Przekaźniki Nostr nie gwarantują trwałego przechowywania danych. Klucz prywatny nsec pozostaje jedynym gwarantowanym sposobem na odzyskanie środków.



![backup private key](assets/fr/05.webp)




## Korzystanie z Arkade



Po skonfigurowaniu wallet możesz odkrywać możliwości Arkade. Interfejs został zaprojektowany tak, aby ujednolicić różne rodzaje płatności Bitcoin (On-chain, Lightning, Ark).



### Otrzymywanie środków



Aby zasilić swój portfel, naciśnij **"Odbierz "**. Arkade oferuje trzy metody odbioru:





- Płatność Ark**: Jeśli nadawca również korzysta z Arkade, udostępnij swój adres Ark, aby uzyskać natychmiastowy, poufny i praktycznie bezpłatny przelew.
- Depozyt na łańcuchu (Boarding)**: Użyj adresu Bitcoin (`bc1p...`), aby otrzymać od klasycznego wallet lub giełdy. Poczekaj na potwierdzenie (~10 min), zanim środki zostaną zamienione na VTXO.
- Lightning swap**: Wygeneruj fakturę Lightning i opłać ją z zewnętrznego wallet Lightning. Środki dotrą natychmiast dzięki automatycznej wymianie.



![receive amount](assets/fr/06.webp)



Ekran paragonu wyświetla wszystkie dostępne opcje: Kod QR, Adres Ark, Adres Bitcoin (BIP21) i Faktura Lightning. W przypadku płatności Lightning należy pozostawić aplikację otwartą podczas transakcji.



![receive confirmation](assets/fr/07.webp)



### Wysyłanie funduszy



Aby wysłać środki, naciśnij **"Wyślij "** i wklej adres odbiorcy lub zeskanuj kod QR. Arkade automatycznie wykryje rodzaj wymaganej płatności:





- Płatność Ark**: Na adres Ark przelew jest natychmiastowy, prywatny i praktycznie darmowy (0 opłaty SATS). Odbiorca nie musi być online.
- Płatność Lightning**: Zeskanuj fakturę Lightning (`lnbc...`), a Arkade automatycznie dokona zamiany. ASP płaci fakturę za Ciebie i obciąża Twoje saldo Arkade.
- Płatność w łańcuchu**: W kierunku klasycznego adresu Bitcoin (`bc1q...` lub `bc1p...`), Arkade inicjuje "Collaborative Output", który zostanie uwzględniony w następnej rundzie on-chain.



Sprawdź szczegóły na ekranie "Podpisz transakcję", a następnie potwierdź za pomocą **"TAP TO SIGN "**.



![send payment](assets/fr/08.webp)



**Obecne ograniczenie (Beta)**: VTXO utworzone mniej niż 24 godziny temu nie mogą być używane dla wyjść on-chain. Jeśli napotkasz błąd, poczekaj, aż twoje VTXO będą "dojrzałe".



**Poufność danych wyjściowych on-chain**: Poniższy przykład pokazuje [transakcję wyjściową Ark na mempool.space](https://mempool.space/fr/tx/153a70384d1c8a183c0e408e29b0a11820fd71a8bd5b4b00b12bc9b7f9decacb). Obserwujemy rozproszone wejście do 4 różnych wyjść, jak CoinJoin. Dla zewnętrznego obserwatora niemożliwe jest określenie, która kwota należy do którego użytkownika.



![transaction ark mempool](assets/fr/11.webp)



## Zaawansowane funkcje



### Zarządzanie wygaśnięciem VTXO


Techniczną cechą protokołu Ark jest to, że VTXO mają **ograniczony czas życia**. To ograniczenie czasowe jest nieodłącznie związane z projektem protokołu. Czas wygaśnięcia jest konfigurowalny przez każdy serwer ASP; na oficjalnym serwerze Arkade Labs ASP okres ten wynosi około **4 tygodni (≈30 dni)**.



**To ograniczenie pozwala serwerowi Ark na efektywne zarządzanie płynnością i czyszczenie VTXO z nieaktywnych użytkowników. Po wygaśnięciu serwer Ark może technicznie zażądać pozostałych środków w drzewie VTXO.



**Aby zachować aktywność VTXO, należy je "odświeżyć" przed wygaśnięciem. Odświeżanie polega na uczestnictwie w nowej "rundzie", w której VTXO bliskie wygaśnięcia są wymieniane na nowe VTXO z nowym pełnym okresem ważności (≈30 dni w Arkade Labs ASP).



Portfel Arkade zarządza tym procesem automatycznie: aplikacja stale monitoruje stan Twoich VTXO i automatycznie odświeża je na kilka dni przed ich wygaśnięciem. Tak długo, jak regularnie otwierasz aplikację (co najmniej raz w tygodniu), Twoje VTXO będą automatycznie aktywne.



**Jeśli nie otworzysz swojego portfela przez ponad 4 tygodnie, Twoje VTXO wygaśnie. Jednak nie stracisz swoich środków: zachowujesz możliwość ich odzyskania poprzez **jednostronne wyjście** (patrz następna sekcja). Ta procedura jest bardziej kosztowna i wolniejsza, ale zapewnia, że środki można odzyskać.



Konieczność regularnego otwierania aplikacji sprawia, że Arkade to **"Hot Wallet"** przeznaczony do codziennych wydatków, a nie sejf do długoterminowego oszczędzania. Aby przechowywać bitcoiny bez używania ich przez dłuższy czas, preferuj zimny sprzęt wallet.



**Sprawdź status VTXO**: Możesz monitorować status swoich VTXO w **Ustawieniach** > **Zaawansowane**. Zobacz "Następne odnowienie", aby zobaczyć, kiedy nastąpi kolejne automatyczne odnowienie, oraz "Wirtualne monety", aby zobaczyć szczegółową listę wszystkich VTXO wraz z datą ich wygaśnięcia.



![vtxo management](assets/fr/09.webp)



### Jednostronne wyjście (Unilateral Exit)



Jednostronne wyjście jest **podstawową gwarancją kryptograficzną** protokołu Ark, która zapewnia odzyskanie środków, nawet jeśli ASP zniknie, ocenzuruje transakcje lub odmówi współpracy. Technicznie rzecz biorąc, twoje VTXO są **podpisanymi transakcjami Bitcoin**, których jesteś właścicielem. W absolutnie nagłych przypadkach możesz transmitować te transakcje na blockchainie Bitcoin, aby odzyskać swoje środki bez niczyjej autoryzacji.



**Jak to działa? Proces odbywa się w dwóch etapach. Po pierwsze, **Unrolling**: sekwencyjnie transmitujesz wstępnie podpisane transakcje, które składają się na twoje VTXO w drzewie transakcji. Następnie **Finalizacja**: po wygaśnięciu blokad czasowych (zwykle 24 godziny), odbierasz swoje bitcoiny ze standardowego adresu.



**Aktualny status w Arkade**: W wersji Beta nie ma jeszcze przycisku ani prostego interfejsu użytkownika dla jednostronnego wyjścia. Ta funkcjonalność wymaga obecnie użycia Arkade SDK i wiedzy technicznej na temat programowania w języku TypeScript.



**Nawet jeśli procedura nie jest dostępna po naciśnięciu przycisku, gwarancja kryptograficzna jest dostępna. Twoje VTXO zawierają wstępnie podpisane transakcje, które legalnie należą do Ciebie. To właśnie ta techniczna gwarancja sprawia, że Ark jest protokołem **non-custodial**: nawet w najgorszym przypadku środki pozostają technicznie możliwe do odzyskania. Uproszczony interfejs zostanie prawdopodobnie dodany w przyszłych wersjach Arkade.



## Zalety i ograniczenia



Aby umieścić Arkade we właściwym kontekście, podsumujmy jego obecne mocne i słabe strony.



### Najważniejsze wydarzenia




- Doświadczenie użytkownika (UX)**: Brak zarządzania kanałami, przychodzącej przepustowości lub złożonych kopii zapasowych kanałów, jak w przypadku Lightning. Wystarczy zainstalować i używać.
- Prywatność** : Domyślna architektura CoinJoin oferuje znacznie wyższy poziom anonimowości niż standardowe transakcje on-chain lub Lightning.
- Interoperacyjność**: Płać dowolnym kodem Bitcoin QR (On-chain lub Lightning) z poziomu jednego interfejsu.



### Ograniczenia




- Młody protokół**: Ark to bardzo nowa technologia. Mogą w niej występować błędy. Zaleca się, aby nie używać Ark do przechowywania kwot, których utrata byłaby krytyczna.
- Zależność od ASP**: Chociaż system nie jest zależny, jego płynność zależy od dostępności ASP. Jeśli ASP jest w trybie offline, nie można już dokonywać natychmiastowych transakcji (tylko wyprowadzać środki z on-chain).
- Tylko Hot Wallet** : Konieczność regularnego otwierania aplikacji w celu odświeżenia VTXO nie jest odpowiednia dla przechowywania na zimno (Cold Storage).



## Porównanie: Arkade vs Lightning vs Cashu



Aby lepiej zrozumieć pozycję Arkade, porównajmy ją z pozostałymi dwoma głównymi rozwiązaniami w zakresie skalowalności.



| Critère | Arkade (Ark) | Lightning Network | Cashu (E-cash) |
| :--- | :--- | :--- | :--- |
| **Modèle** | UTXO partagé coordonné par serveur (ASP) | Réseau P2P de canaux de paiement | Jetons aveugles émis par une banque (Mint) |
| **Custodie** | **Non-custodial** (vous avez les clés) | **Non-custodial** (vous avez les clés) | **Custodial** (le Mint a les fonds) |
| **Confidentialité** | **Élevée** (CoinJoin natif, aveugle pour le public) | **Moyenne** (Routage en oignon, mais canaux visibles) | **Très Élevée** (Aveugle même pour le Mint) |
| **Scalabilité** | Excellente (Batching massif on-chain) | Excellente (Transactions infinies off-chain) | Excellente (Simples signatures serveur) |
| **Expérience** | Simple (proche d'un wallet on-chain) | Complexe (gestion de canaux, liquidité) | Très simple (comme du cash numérique) |
| **Risque principal** | Disponibilité de l'ASP & Expiration | Gestion des canaux & Backups | Confiance dans le Mint (risque de vol) |

**Arkade** to idealny kompromis: prostota i poufność Cashu, ale z suwerennością (bez aresztu) Lightning.



## Wsparcie i pomoc



W przypadku napotkania jakichkolwiek problemów lub pytań podczas korzystania z Arkade, aplikacja oferuje kilka opcji wsparcia:





- Przejdź do **Ustawienia** > **Wsparcie**.
- Dostępnych jest kilka opcji:
  - Obsługa klienta**: Uzyskaj pomoc dotyczącą swojego portfolio, zgłaszaj błędy lub zadawaj pytania.
  - Bezpieczny czat**: Rozmowy są bezpieczne i prywatne, a ich historia jest przechowywana pomiędzy sesjami.
  - Raporty o błędach**: Zgłaszaj wszelkie napotkane problemy, w tym kroki mające na celu ich odtworzenie.
  - Śledzenie postępów**: Śledź swoje zgłoszenia do pomocy technicznej i rozmowy przez cały czas.



![support](assets/fr/10.webp)



Zespół Arkade jest również aktywny w Telegramie za pośrednictwem kanału @arkade_os w celu uzyskania wsparcia i możliwości integracji.



## Ważna uwaga: aplikacja w wersji beta



**⚠️ Arkade jest obecnie w publicznej wersji beta na mainnet Bitcoin**. Chociaż aplikacja działa z prawdziwymi bitcoinami, ważne jest, aby podjąć pewne środki ostrożności.



### Zalecenia dotyczące użytkowania




- Używaj małych kwot**: Unikaj przechowywania dużych kwot na Arkade. Używaj tego wallet do codziennych wydatków i trzymaj swoje oszczędności na zimnym sprzęcie wallet.
- Możliwe błędy i ograniczenia**: Podobnie jak w przypadku każdej aktywnie rozwijanej aplikacji, Arkade może zawierać błędy lub nieoczekiwane zachowania. Wszelkie problemy należy zgłaszać za pośrednictwem zintegrowanej pomocy technicznej.
- Szybka ewolucja** : Aplikacja i protokół są stale ulepszane. Niektóre funkcje mogą ulec zmianie lub zostać dodane w przyszłych wersjach.



### Obecne znane ograniczenia




- 24-godzinne opóźnienie dla VTXO** : Nowo utworzone VTXO nie mogą być natychmiast użyte dla wyjść on-chain.
- Unikalny serwer ASP**: Nie ma jeszcze możliwości zmiany serwera ASP w aplikacji.
- Techniczne jednostronne wyjście**: Brak uproszczonego interfejsu dla jednostronnego wyjścia (wymaga SDK).



Zespół Arkade Labs aktywnie pracuje nad złagodzeniem tych ograniczeń w przyszłych wersjach.



## Wnioski



ArkadeOS stanowi istotny przełom w ekosystemie Bitcoin. Implementując protokół Ark, udowadnia, że możliwe jest pogodzenie prostoty użytkowania z podstawowymi zasadami Bitcoin: nie ufaj, weryfikuj.



Chociaż Arkade jest wciąż w powijakach, oferuje fascynujące spojrzenie na to, jak może wyglądać przyszłość płatności Bitcoin: natychmiastowe, prywatne i dostępne dla wszystkich bez żadnych wymagań technicznych. Jest to idealne narzędzie do codziennych wydatków, uzupełniające bezpieczne rozwiązanie oszczędnościowe (Cold Wallet).



Zachęcamy do przetestowania Arkade z niewielkimi kwotami, aby odkryć ten nowy protokół dla siebie. Ekosystem szybko ewoluuje, a Arkade jest liderem tej innowacji.



## Zasoby



Aby dowiedzieć się więcej, zapoznaj się z oficjalnymi zasobami:





- Strona internetowa Arkade**: [arkadeos.com](https://arkadeos.com)
- Dokumentacja**: [docs.arkadeos.com](https://docs.arkadeos.com)
- Protokół Ark**: [ark-protocol.org](https://ark-protocol.org)
- Kod źródłowy** : [GitHub Arkade](https://github.com/arkade-os)