---
name: Stonewall
description: Zrozumienie i korzystanie z transakcji Stonewall
---
![cover stonewall](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, korzystanie z aplikacji Samourai Wallet wymaga teraz połączenia z własnym Dojo, aby działać poprawnie. Poza tym nie ma to żadnego wpływu na transakcje Stonewall i nadal można je wykonywać bez żadnych problemów. Rzeczywiście, tego typu transakcje są przeprowadzane autonomicznie, bez potrzeby zewnętrznej współpracy lub połączenia przez Soroban.*


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> *Złam założenia analizy Blockchain dzięki matematycznie udowodnionym wątpliwościom między nadawcą a odbiorcą transakcji

## Czym jest transakcja Stonewall?

Stonewall to specyficzna forma transakcji Bitcoin mająca na celu zwiększenie prywatności użytkownika podczas transakcji poprzez naśladowanie CoinJoin między dwiema stronami, nie będąc w rzeczywistości jedną z nich. W rzeczywistości transakcja ta nie jest oparta na współpracy. Użytkownik może skonstruować ją samodzielnie, angażując jedynie własne UTXO jako dane wejściowe. W związku z tym można utworzyć transakcję Stonewall na dowolną okazję bez konieczności koordynacji z innym użytkownikiem.


Działanie transakcji Stonewall jest następujące: jako dane wejściowe nadawca używa 2 UTXO, które do niego należą. Na wyjściu transakcja generuje 4 wyjścia, w tym 2, które będą dokładnie taką samą kwotą. Pozostałe 2 to zmiana. Spośród 2 wyjść o tej samej kwocie, tylko jedno faktycznie trafi do odbiorcy płatności.


W transakcji Stonewall występują tylko 2 role:


- Nadawca, który dokonuje faktycznej płatności;
- Odbiorca, który może być nieświadomy szczególnego charakteru transakcji i po prostu oczekuje płatności od nadawcy.


Weźmy przykład, aby zrozumieć tę strukturę transakcji. Alice jest w piekarni, aby kupić bagietkę, która kosztuje `4,000 Sats`. Chce zapłacić bitcoinami, zachowując przy tym pewien poziom prywatności płatności. Dlatego decyduje się na utworzenie transakcji Stonewall dla tej płatności.

![transaction stonewall bakery](assets/en/1.webp)

Analizując tę transakcję, widzimy, że piekarz rzeczywiście otrzymał `4 000 Sats` jako zapłatę za bagietkę. Alicja użyła 2 UTXO jako danych wejściowych: jednego o wartości `10 000 Sats` i jednego o wartości `15 000 Sats`. Na wyjściu otrzymała 3 UTXO: jeden o wartości `4 000 Sats`, jeden o wartości `6 000 Sats` i jeden o wartości `11 000 Sats`. Saldo netto Alicji w tej transakcji wynosi `4 000 Sats`, co odpowiada cenie bagietki.


W tym przykładzie celowo pominąłem opłaty Mining, aby ułatwić zrozumienie. W rzeczywistości opłaty transakcyjne są w pełni pokrywane przez nadawcę.


## Jaka jest różnica między Stonewall a Stonewall x2?

Transakcja Stonewall działa w taki sam sposób jak transakcja StonewallX2, z tą różnicą, że ta ostatnia wymaga współpracy, w przeciwieństwie do klasycznej transakcji Stonewall, stąd oznaczenie "x2". Rzeczywiście, transakcja Stonewall może być realizowana bez konieczności współpracy zewnętrznej: nadawca może ją przeprowadzić bez pomocy innej osoby. Jednak w przypadku transakcji Stonewall x2 do procesu dołącza dodatkowy uczestnik, zwany "współpracownikiem". Współpracownik wnosi własne bitcoiny jako wkład, wraz z bitcoinami nadawcy, i otrzymuje całą sumę jako wynik (minus opłaty Mining).


Powróćmy do naszego przykładu z Alicją w piekarni. Gdyby chciała dokonać transakcji Stonewall x2, musiałaby współpracować z Bobem (stroną trzecią) podczas tworzenia transakcji. Każdy z nich dostarczyłby dane wejściowe UTXO. Następnie Bob otrzymałby pełną kwotę swojego wkładu jako wynik. Piekarz otrzymałby zapłatę za swoją bagietkę w taki sam sposób, jak w transakcji Stonewall, podczas gdy Alicja otrzymałaby z powrotem swoje saldo początkowe pomniejszone o koszt bagietki.

![transaction stonewall x2](assets/en/2.webp)


Z perspektywy zewnętrznej schemat transakcji pozostałby dokładnie taki sam.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)


Podsumowując, transakcje Stonewall i Stonewall x2 mają identyczną strukturę. Różnica między nimi polega na ich wspólnym charakterze. Transakcja Stonewall jest opracowywana indywidualnie, bez potrzeby współpracy. Natomiast transakcja Stonewall x2 opiera się na współpracy między dwiema osobami w celu jej wdrożenia.


[**-> Dowiedz się więcej o transakcjach Stonewall x2**](https://planb.network/tutorials/privacy/on-chain/stonewall-x2-05120280-f6f9-4e14-9fb8-c9e603f73e5b)


## Jaki jest cel transakcji Stonewall?

Struktura Stonewall dodaje znaczną ilość entropii do transakcji i zaciemnia analizę łańcucha. Z perspektywy zewnętrznej taka transakcja może być interpretowana jako mały CoinJoin między dwiema osobami. Ale w rzeczywistości, podobnie jak transakcja Stonewall x2, jest to płatność. Metoda ta powoduje zatem niepewność w analizie łańcucha, a nawet może prowadzić do fałszywych tropów.


Powróćmy do przykładu Alicji w piekarni. Transakcja na Blockchain wyglądałaby następująco:

![Stonewall or Stonewall x2 ?](assets/en/4.webp)

Zewnętrzny obserwator polegający na heurystyce analizy łańcuchowej mógłby błędnie wywnioskować, że "*dwie osoby wykonały mały CoinJoin, z jednym UTXO jako wejściem i dwoma UTXO jako wyjściem*".

![Stonewall or Stonewall x2 ?](assets/en/5.webp)

Ta interpretacja jest nieprawidłowa, ponieważ, jak wiadomo, UTXO został wysłany do piekarza, 2 UTXO na wejściu pochodzą od Alice, a ona otrzymała 3 wyjścia zmiany.


![transaction stonewall baker](assets/en/1.webp)

Nawet jeśli zewnętrzny obserwator zdoła zidentyfikować schemat transakcji Stonewall, nie będzie miał wszystkich informacji. Nie będzie w stanie określić, który z dwóch UTXO o tych samych kwotach odpowiada płatności. Co więcej, nie będą w stanie określić, czy dwa UTXO w danych wejściowych pochodzą od dwóch różnych osób, czy też należą do jednej osoby, która je połączyła. Ten ostatni punkt wynika z faktu, że transakcje Stonewall x2, o których mówiliśmy powyżej, przebiegają dokładnie według tego samego schematu, co transakcje Stonewall. Z zewnątrz i bez dodatkowych informacji o kontekście niemożliwe jest odróżnienie transakcji Stonewall od transakcji Stonewall x2. Jednak te pierwsze nie są transakcjami opartymi na współpracy, podczas gdy te drugie są. Dodaje to jeszcze więcej wątpliwości co do tego wydatku.

![Stonewall or Stonewall x2 ?](assets/en/3.webp)

## Jak dokonać transakcji Stonewall na Samourai Wallet?

W przeciwieństwie do transakcji Stowaway lub Stonewall x2 (cahoots), transakcja Stonewall nie wymaga korzystania z Paynyms. Można ją wykonać bezpośrednio, bez żadnych kroków przygotowawczych. Aby to zrobić, postępuj zgodnie z naszym samouczkiem wideo na Samourai Wallet:

![Stonewall Tutorial - Samourai Wallet](https://youtu.be/mlRtZvWGuk0?si=e_lSKJLvybWUna1j)


## Jak dokonać transakcji Stonewall na Sparrow Wallet?

W przeciwieństwie do transakcji Stowaway lub Stonewall x2 (cahoots), transakcja Stonewall nie wymaga korzystania z Paynyms. Można ją wykonać bezpośrednio, bez żadnych kroków przygotowawczych. Aby to zrobić, postępuj zgodnie z naszym samouczkiem wideo na Sparrow Wallet:

![Stonewall Tutorial - Sparrow Wallet](https://youtu.be/su89ljkV_OI?si=1jNaSJGvECUYe6Or)



**Zasoby zewnętrzne:**


- https://docs.samourai.io/en/spend-tools#stonewall.