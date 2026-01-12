---
name: Sparrow Wallet - Stonewall
description: Zrozumienie i korzystanie z transakcji Stonewall na Sparrow
---

![cover](assets/cover.webp)




> *Złam założenia analizy blockchain dzięki matematycznie udowodnionym wątpliwościom między nadawcą a odbiorcą transakcji*

## Co to jest transakcja Stonewall?



Stonewall to specyficzna forma transakcji Bitcoin zaprojektowana w celu zwiększenia poufności użytkowników podczas wydawania pieniędzy poprzez imitowanie połączenia monet między dwiema osobami, bez faktycznego bycia jedną z nich. W rzeczywistości transakcja ta nie jest oparta na współpracy. Użytkownik może zbudować ją samodzielnie, używając tylko UTXO należących do niego jako danych wejściowych. Można więc utworzyć transakcję Stonewall na dowolną okazję, bez konieczności synchronizacji z innym użytkownikiem.



Transakcja Stonewall działa w następujący sposób: jako dane wejściowe do transakcji emitent wykorzystuje 2 UTXO, które do niego należą. Po stronie wyjściowej transakcja generuje 4 wyjścia, z których 2 mają dokładnie taką samą wartość. Pozostałe 2 to waluty obce. Z 2 wyjść o tej samej kwocie, tylko jedno faktycznie trafi do odbiorcy.



W transakcji Stonewall występują więc tylko 2 role:




- Emitent, który dokonuje faktycznej płatności;
- Odbiorca, który może być nieświadomy szczególnego charakteru transakcji i po prostu oczekuje płatności od nadawcy.



Weźmy przykład, aby zrozumieć tę strukturę transakcji. Alice jest u piekarza, aby kupić bagietkę, która kosztuje `4,000 sats`. Chce zapłacić w bitcoinach, zachowując jednocześnie pewną formę poufności co do swojej płatności. Postanawia więc utworzyć transakcję Stonewall dla tej płatności.



![image](assets/fr/01.webp)



Analizując tę transakcję, widzimy, że piekarz rzeczywiście otrzymał `4,000 sats` jako zapłatę za bagietkę. Alice wykorzystał 2 UTXO jako dane wejściowe: jeden o wartości `10 000 sats` i jeden o wartości `15 000 sats`. Na wyjściu odzyskał 3 UTXO: jeden o wartości `4,000 sats`, jeden o wartości `6,000 sats` i jeden o wartości `11,000 sats`. Alice ma zatem saldo netto w wysokości `- 4,000 sats` na tej transakcji, co dobrze odpowiada cenie bagietki.



W tym przykładzie celowo pominąłem opłaty mining, aby ułatwić jego zrozumienie. W rzeczywistości koszty transakcji są w całości ponoszone przez emitenta.



## Jaka jest różnica między Stonewall a Stonewall x2?



Transakcja Stonewall działa identycznie jak transakcja StonewallX2, z tym wyjątkiem, że ta ostatnia wymaga współpracy, w przeciwieństwie do klasycznej transakcji Stonewall, stąd nazwa "x2". Wynika to z faktu, że transakcja Stonewall jest wykonywana bez potrzeby współpracy zewnętrznej: nadawca może ją przeprowadzić bez pomocy innej osoby. W przeciwieństwie do tego, w przypadku transakcji Stonewall x2, do procesu dołącza dodatkowy uczestnik, znany jako "współpracownik". Wnosi on do transakcji własne bitcoiny wraz z bitcoinami nadawcy, a na koniec przejmuje całą kwotę (pomniejszoną o koszty mining).



Wróćmy do naszego przykładu z Alice w piekarni. Gdyby chciała dokonać transakcji Stonewall x2, Alice musiałaby współpracować z Bob (stroną trzecią) podczas konfigurowania transakcji. Każdy z nich przyniósłby UTXO. Bob otrzymałby wtedy pełną kwotę swojego wkładu przy wyjściu. Piekarz otrzymałby zapłatę za swoją bagietkę w taki sam sposób, jak w transakcji Stonewall, podczas gdy Alice odzyskałby swoje saldo początkowe, pomniejszone o koszt bagietki.



![image](assets/fr/02.webp)



Z punktu widzenia osoby postronnej transakcja pozostałaby dokładnie taka sama.



![image](assets/fr/03.webp)



Podsumowując, transakcje Stonewall i Stonewall x2 mają identyczną strukturę. Różnica między nimi polega na ich współpracy lub braku współpracy. Transakcja Stonewall jest opracowywana indywidualnie, bez potrzeby współpracy. Z drugiej strony, transakcja Stonewall x2 opiera się na współpracy między dwiema osobami.



[**-> Dowiedz się więcej o transakcjach Stonewall x2**](https://planb.academy/tutorials/privacy/on-chain/ashigaru-stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)



## Jaki jest sens transakcji Stonewall?



Struktura Stonewall dodaje ogromną ilość entropii do transakcji, zacierając linie analizy łańcucha. Patrząc z zewnątrz, taka transakcja może być interpretowana jako niewielki coinjoin między dwiema osobami. Ale w rzeczywistości, podobnie jak transakcja Stonewall x2, jest to płatność. Metoda ta generuje zatem niepewność w analizie łańcucha, a nawet prowadzi do fałszywych tropów.



Weźmy przykład Alice u piekarza. Transakcja na blockchainie wyglądałaby następująco:



![image](assets/fr/04.webp)



Zewnętrzny obserwator polegający na heurystyce analizy łańcucha może błędnie dojść do wniosku, że "*dwie osoby wykonały mały coinjoin, z jednym UTXO na wejściu i dwoma UTXO na wyjściu*".



![image](assets/fr/05.webp)



Ta interpretacja jest niedokładna, ponieważ, jak wiadomo, jeden UTXO został wysłany do piekarza, 2 przychodzące UTXO pochodziły od Alices, a ona odzyskała 3 wyjścia wymiany.



![image](assets/fr/01.webp)



Nawet jeśli zewnętrzny obserwator zdoła zidentyfikować stronę transakcji Stonewall, nie będzie miał wszystkich informacji. Nie będzie w stanie określić, który z dwóch UTXO o tych samych kwotach odpowiada płatności. Ponadto nie będzie w stanie określić, czy dwa wpisy UTXO pochodzą od dwóch różnych osób, czy też należą do jednej osoby, która je połączyła. Ten ostatni punkt wynika z faktu, że wspomniane powyżej transakcje Stonewall x2 przebiegają dokładnie według tego samego schematu, co transakcje Stonewall. Patrząc z zewnątrz i bez dodatkowych informacji kontekstowych, nie można odróżnić transakcji Stonewall od transakcji Stonewall x2. Te pierwsze nie są transakcjami opartymi na współpracy, podczas gdy te drugie są. Dodaje to jeszcze więcej wątpliwości do wydatków.



![image](assets/fr/03.webp)



## Jak mogę dokonać transakcji Stonewall na Sparrow?



Pierwotnie opracowane przez zespół Samurai Wallet, transakcje Stonewall zostały przejęte przez aplikację Ashigaru, fork z oryginalnego portfolio stworzonego po aresztowaniu deweloperów Samurai, a także na Sparrow Wallet.



Konieczne będzie zainstalowanie Sparrow i utworzenie pliku :



https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d

W przeciwieństwie do transakcji Stowaway lub Stonewall x2 (*cahoots*), transakcje Stonewall nie wymagają korzystania z Paynyms. Mogą być przeprowadzane bezpośrednio, bez specjalnego przygotowania lub współpracy z innym użytkownikiem.



Aby wykonać transakcję Stonewall na Sparrow, procedura jest bardzo prosta: zacznij od utworzenia transakcji jak zwykle, albo poprzez menu `Send`, albo z menu `UTXOs`, jeśli chcesz wykonać *Coin Control*.



![Image](assets/fr/06.webp)



Następnie wprowadź szczegóły transakcji: adres odbiorcy, etykietę, kwotę do wysłania oraz kwotę lub stawkę opłat, w zależności od warunków rynkowych.



![Image](assets/fr/07.webp)



Przed potwierdzeniem, w tym miejscu możesz wybrać strukturę Stonewall. W dolnej części interfejsu zamień `Efficiency` na `Privacy`. Jeśli ta opcja się nie pojawi, oznacza to, że w portfelu nie ma wystarczającej liczby UTXO do zbudowania tego typu transakcji.



![Image](assets/fr/08.webp)



Po wybraniu opcji `Privacy`, zauważysz, że struktura transakcji została całkowicie zmodyfikowana: staje się ona transakcją Stonewall, zużywając kilka UTXO jako dane wejściowe i produkując dwie identyczne kwoty wyjściowe, z których jedna odpowiada rzeczywistej płatności `100 000 sats`, oprócz wyników wymiany.



![Image](assets/fr/09.webp)



Jeśli wszystko się zgadza, kliknij `Twórz transakcję`.



Następnie możesz sprawdzić szczegóły transakcji po raz ostatni i kliknąć `Finalizuj transakcję do podpisania`.



![Image](assets/fr/10.webp)



Następnie podpisz transakcję zgodnie z metodą właściwą dla Twojego portfela i kliknij `Broadcast Transaction`, aby rozesłać ją w sieci Bitcoin, oczekując na potwierdzenie.



![Image](assets/fr/11.webp)



Wiesz już, jak działa transakcja Stonewall na Sparrow Wallet i jak ją utworzyć. Aby pogłębić znajomość tych narzędzi zaprojektowanych w celu wzmocnienia poufności onchain, zapraszam do śledzenia mojego szkolenia BTC 204 na Plan ₿ Academy :



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c