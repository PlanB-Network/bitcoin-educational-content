---
name: Lightning Network+
description: Uzyskaj bezpłatną płynność przychodzącą dzięki otwarciom współpracy w węźle Lightning
---

![cover](assets/cover.webp)



## Wprowadzenie



[LN+ (Lightning Network Plus)](https://lightningnetwork.plus/) to platforma społecznościowa zaprojektowana w celu ułatwienia współpracy między operatorami węzłów Lightning Network. Jej głównym celem jest poprawa łączności, płynności i decentralizacji sieci Lightning, bez potrzeby scentralizowanych pośredników.



Ten samouczek skupi się na usłudze **"Swapy "**, która jest obecnie najczęściej używaną i strukturyzującą funkcją LN+. Przedstawione zostaną również inne usługi oferowane przez platformę.



## Przegląd LN+



### Czym jest Lightning Network Plus?



Lightning Network Plus (LN+) to platforma społecznościowa dla operatorów węzłów Lightning, którzy chcą współpracować bezpośrednio i dobrowolnie. Jej celem jest ułatwienie tworzenia użytecznych, zrównoważonych i zrównoważonych kanałów Lightning, przy jednoczesnym uniknięciu potrzeby scentralizowanych rozwiązań lub narzuconych centrów.



LN+ opiera się na fundamentalnej zasadzie: współpracy peer-to-peer, opartej na przejrzystości, wzajemności i reputacji.



### Usługi LN+ w skrócie



LN+ oferuje kilka usług zaprojektowanych w celu poprawy topologii i płynności sieci Lightning, w tym :





- Swapy**: wzajemne otwieranie kanałów między operatorami (usługa główna).
- Pierścienie**: okrągłe kanały pomiędzy kilkoma uczestnikami.
- Swapy oparte na zaufaniu**: warianty, które w większym stopniu opierają się na zaufaniu i historii uczestników.
- Funkcje społecznościowe**: profile, komentarze i system reputacji.



W dalszej części tego samouczka skoncentrujemy się wyłącznie na usłudze **Swaps**, która jest sercem obecnego wykorzystania LN+.



## Usługa LN+ "Swaps"



### Definicja zamiany LN+



LN+ **swap** to dobrowolna umowa między dwoma operatorami węzłów Lightning o wzajemnym otwarciu kanałów Lightning o równoważnej (lub wcześniej uzgodnionej) przepustowości. W przeciwieństwie do konwencjonalnego jednostronnego otwarcia kanału, swap opiera się na **wyraźnej wzajemności**.



W praktyce :





- Otwierasz kanał do węzła swojego partnera.
- Twój partner otwiera kanał do Twojego węzła.
- Obie strony wiążą podobną ilość bitcoinów on-chain.



### Jaki jest cel swapów dla operatorów węzłów?



Usługa Swaps rozwiązuje kilka kluczowych problemów napotykanych przez operatorów Lightning:





- Ulepszona łączność**: tworzenie użytecznych kanałów dwukierunkowych natychmiast po ich otwarciu.
- Lepsze zarządzanie płynnością**: każda strona ma zarówno przychodzącą, jak i wychodzącą przepustowość.
- Zmniejszone ryzyko niepotrzebnych kanałów**: partner jest zachęcany do utrzymania otwartego kanału.
- Większa decentralizacja**: bezpośrednie połączenia między operatorami, bez narzuconych węzłów.



### Dla których profili węzłów swapy są przydatne?



Swapy są szczególnie przydatne w przypadku :





- Nowe węzły, które chcą szybko poprawić swoje możliwości routingu.
- Operatorzy pośredniczący, którzy chcą zwiększyć gęstość swojego wykresu kanału.
- Węzły zorientowane na routing, które chcą zoptymalizować swoją topologię.



## Podłącz węzeł Lightning do LN+



### Wymagania techniczne



Zanim zaczniesz, będziesz potrzebować :





- Działający węzeł Lightning (LND, Core Lightning lub Eclair).
- Dostęp do interfejsu zarządzania węzłem.
- Wystarczająca przepustowość on-chain do otwarcia kanałów.



Wejdź na stronę [Lightning Network](https://lightningnetwork.plus/) Plus i kliknij przycisk `Login` w prawym górnym rogu interfejsu.



![capture](assets/fr/03.webp)



### Uwierzytelnianie za pomocą podpisu wiadomości



Aby się uwierzytelnić, należy podpisać dostarczoną wiadomość przy użyciu klucza prywatnego węzła Lightning. Dzięki ThunderHub operacja ta jest bardzo prosta.



Zacznij od skopiowania komunikatu wyświetlanego przez LN+.



![capture](assets/fr/04.webp)



W ThunderHub przejdź do zakładki `Tools`, a następnie kliknij przycisk `Sign` w sekcji `Messages`.



![capture](assets/fr/05.webp)



Wklej wiadomość uwierzytelniającą dostarczoną przez LN+, a następnie kliknij `Podpisz`.



![capture](assets/fr/06.webp)



Następnie ThunderHub podpisuje tę wiadomość przy użyciu klucza prywatnego węzła. Skopiuj wygenerowany podpis.



![capture](assets/fr/07.webp)



Wklej ten podpis do odpowiedniego pola na stronie LN+, a następnie kliknij przycisk `Zaloguj`.



![capture](assets/fr/08.webp)



Jesteś teraz połączony z LN+ za pomocą swojego węzła Lightning. Ten proces pozwala LN+ zweryfikować, czy jesteś prawowitym właścicielem węzła, który zgłaszasz na ich platformie.



![capture](assets/fr/09.webp)



Jeśli chcesz, możesz spersonalizować swój profil LN+, na przykład dodając krótką biografię.



## Udział w istniejącej transakcji swap



### Dostęp do ofert wymiany



Aby wziąć udział w pierwszym otwarciu kanału, przejdź do menu `Swaps` w górnej części interfejsu. Znajdziesz tam wszystkie aktualnie dostępne swapy, w zależności od charakterystyki twojego węzła.



![capture](assets/fr/10.webp)



### Warunki kwalifikowalności



Aby dołączyć do istniejącej oferty wymiany, wystarczy wybrać odpowiednią reklamę i zarejestrować się. LN+ pozwala jednak twórcy swapu na zdefiniowanie pewnych **warunków kwalifikowalności**, takich jak :





- minimalna liczba otwartych kanałów;
- minimalna całkowita pojemność węzła ;
- akceptowane są określone typy połączeń.



### Ostatnie węzły



W rezultacie, szczególnie na wczesnych etapach użytkowania, możliwe jest, że **niewiele lub żadne oferty nie są dostępne** dla węzła. Jest to częsta sytuacja w przypadku nowych węzłów lub tych, które nie są jeszcze połączone.



W moim przypadku, pomimo istnienia kilku otwartych kanałów, żadna z ofert nie spełniała wymaganych kryteriów.



## Stwórz własną ofertę wymiany



### Kiedy należy utworzyć własny swap?



Gdy nie jest dostępna żadna istniejąca oferta, utworzenie własnego swapu jest często najlepszym rozwiązaniem. Pozwala to również zachować kontrolę nad parametrami swapu.



### Konfiguracja wymiany



Kliknij **Start Liquidity Swap**, a następnie skonfiguruj parametry oferty:





- wybierz całkowitą liczbę uczestników (3, 4 lub 5);
- wskazują przepustowość kanałów, które mają zostać otwarte;
- określić okres zobowiązania, w którym uczestnicy zgadzają się nie zamykać swoich kanałów;
- określić wszelkie ograniczenia mające zastosowanie do uczestników (minimalna liczba kanałów, minimalna łączna pojemność, akceptowany typ połączenia).



![capture](assets/fr/11.webp)



### Publikacja i oczekiwania uczestników



Po wprowadzeniu wszystkich parametrów kliknij **Start Liquidity Swap**, aby opublikować swoją ofertę. Teraz wystarczy poczekać na rejestrację innych operatorów.



![capture](assets/fr/12.webp)



## Finalizowanie wymiany



### Efektywne otwarcie kanału



Teraz, gdy wszystkie pozycje wymiany zostały zajęte, każdy uczestnik może zobaczyć z interfejsu LN+, do którego węzła musi otworzyć kanał Lightning.



![capture](assets/fr/13.webp)



Po swojej stronie otwórz kanał, używając identyfikatora węzła dostarczonego przez LN+ i przestrzegając wskazanej kwoty. Tę operację można wykonać za pośrednictwem ThunderHub, innego menedżera węzła Lightning lub bezpośrednio za pośrednictwem podstawowego interfejsu węzła.



![capture](assets/fr/14.webp)



Po otwarciu kanał pojawi się w sekcji kanałów oczekujących.



![capture](assets/fr/15.webp)



### Potwierdzenie w LN+



Następnie wróć do LN+, aby potwierdzić zainicjowanie otwarcia kanału, klikając przycisk `Channel Opening Started`.



![capture](assets/fr/16.webp)



### Koniec wymiany



Gdy wszyscy uczestnicy otworzą kanały, do których się zobowiązali, swap uznaje się za zakończony.



## Reputacja i dobre praktyki komunikacyjne



### System reputacji LN+



LN+ zawiera system reputacji oparty na opiniach pozostawionych przez uczestników po zakończeniu swapów. Opinie te są publiczne i bezpośrednio wpływają na zdolność operatora do dołączania lub tworzenia przyszłych swapów.



![capture](assets/fr/17.webp)



### Zalecane najlepsze praktyki



Aby zachować dobrą reputację i zapewnić płynne działanie swapów, zaleca się :





- przestrzeganie terminów otwarcia kanału ;
- szybko komunikować się w przypadku problemów lub opóźnień;
- skorzystaj z sekcji komentarzy, aby wymienić poglądy z innymi uczestnikami;
- nie zamykać kanału przed końcem okresu zobowiązania.




![capture](assets/fr/18.webp)



### Dlaczego reputacja ma kluczowe znaczenie dla LN+



LN+ opiera się na modelu dobrowolnej współpracy, bez silnych ograniczeń technicznych. Reputacja jest zatem główną zachętą do zapewnienia niezawodności i wiarygodności uczestników.



## Inne usługi LN+



Oprócz Swapów, LN+ oferuje inne usługi zaprojektowane w celu poprawy łączności i koordynacji między operatorami węzłów Lightning. Pierścienie** umożliwiają kilku uczestnikom utworzenie pętli otwarć kanałów, wzmacniając w ten sposób redundancję ścieżek routingu i gęstość grafu Lightning. Swapy oparte na zaufaniu** opierają się na zasadach podobnych do klasycznych swapów, ale oferują większą elastyczność uczestnikom, którzy mają już ugruntowaną reputację na platformie.



LN+ integruje również funkcje społecznościowe, takie jak publiczne profile węzłów, komentarze wymiany i system reputacji. Narzędzia te nie są same w sobie usługami technicznymi, ale odgrywają kluczową rolę w sprawnym funkcjonowaniu platformy, ułatwiając komunikację, koordynację i zaufanie między operatorami.



## Wnioski



Usługa LN+ Swaps jest skutecznym narzędziem do poprawy łączności, płynności i decentralizacji w sieci Lightning. Promując wzajemne, skoordynowane otwieranie kanałów, LN+ umożliwia operatorom węzłów wzmocnienie ich topologii, jednocześnie promując odpowiedzialną, zdecentralizowaną współpracę.