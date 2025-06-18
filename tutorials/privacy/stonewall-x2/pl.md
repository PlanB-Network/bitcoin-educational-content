---
name: Stonewall x2
description: Zrozumienie i korzystanie z transakcji Stonewall x2
---
![cover stonewall x2](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, transakcje Stonewallx2 działają tylko poprzez ręczną wymianę PSBT między zainteresowanymi stronami, pod warunkiem, że obaj użytkownicy są połączeni z własnym Dojo. Możliwe jest jednak, że narzędzia te zostaną ponownie uruchomione w nadchodzących tygodniach. W międzyczasie nadal możesz zapoznać się z tym artykułem, aby zrozumieć teoretyczne działanie Stonewallx2 i dowiedzieć się, jak wykonać je ręcznie


jeśli rozważasz wykonanie Stonewallx2 ręcznie, procedura jest bardzo podobna do tej opisanej w tym samouczku. Główna różnica polega na wyborze typu transakcji Stonewallx2: zamiast wybierać `Online`, kliknij `In Person / Manual`. Następnie będziesz musiał ręcznie Exchange PSBT, aby skonstruować transakcję Stonewallx2. Jeśli jesteś fizycznie blisko swojego współpracownika, możesz kolejno skanować kody QR. Jeśli jesteś na odległość, pliki JSON mogą być wymieniane za pośrednictwem bezpiecznego kanału komunikacji. Pozostała część samouczka pozostaje bez zmian


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> *Każdy wydatek to CoinJoin.*

## Czym jest transakcja Stonewall x2?


Stonewall x2 to specyficzna forma transakcji Bitcoin mająca na celu zwiększenie prywatności użytkownika podczas wydatków poprzez współpracę z osobą trzecią niezaangażowaną w te wydatki. Metoda ta symuluje mini-CoinJoin między dwoma uczestnikami, podczas dokonywania płatności na rzecz strony trzeciej. Transakcje Stonewall x2 są dostępne zarówno w aplikacji Samourai Wallet, jak i oprogramowaniu Sparrow Wallet. Oba są interoperacyjne.


Jego działanie jest stosunkowo proste: używamy UTXO będącego w naszym posiadaniu do dokonania płatności i szukamy pomocy strony trzeciej, która również wnosi swój własny UTXO. Transakcja skutkuje czterema wyjściami: dwa z nich o równych kwotach, jeden przeznaczony dla Address odbiorcy płatności, drugi dla Address należącego do współpracownika. Trzeci UTXO jest zwracany do innego Address współpracownika, umożliwiając mu odzyskanie początkowej kwoty (działanie neutralne dla niego, modulo opłaty Mining), a ostatni UTXO wraca do Address należącego do nas, co stanowi zmianę z płatności.


W związku z tym w transakcjach Stonewall x2 zdefiniowane są trzy różne role:


- Nadawca, który dokonuje faktycznej płatności;
- Współpracownik, który dostarcza bitcoiny w celu poprawy ogólnej anonimowości transakcji, jednocześnie w pełni odzyskując swoje środki na koniec (działanie neutralne dla niego, modulo opłaty Mining);
- Odbiorca, który może być nieświadomy szczególnego charakteru transakcji i po prostu oczekuje płatności od nadawcy.


Weźmy przykład, aby lepiej zrozumieć. Alice jest w piekarni, aby kupić bagietkę, która kosztuje `4 000 Sats`. Chce zapłacić bitcoinami, zachowując przy tym pewien poziom prywatności. Wzywa więc swojego przyjaciela Boba, który pomoże jej w tym procesie.

![schema stonewall x2](assets/en/1.webp)

Analizując tę transakcję, widzimy, że piekarz rzeczywiście otrzymał `4 000 Sats` jako zapłatę za bagietkę. Alicja wykorzystała `10 000 Sats` jako dane wejściowe i otrzymała `6 000 Sats` jako dane wyjściowe, w wyniku czego saldo netto wyniosło `4 000 Sats`, co odpowiada cenie bagietki. Jeśli chodzi o Boba, dostarczył on `15 000 Sats` jako wkład i otrzymał dwa wyjścia: jedno w wysokości `4 000 Sats` i drugie w wysokości `11 000 Sats`, co dało saldo `0`.

W tym przykładzie celowo pominąłem opłaty Mining, aby ułatwić zrozumienie. W rzeczywistości opłaty transakcyjne są dzielone równo między nadawcę płatności i współpracownika.


## Jaka jest różnica między Stonewall a Stonewall x2?


Transakcja StonewallX2 działa dokładnie tak samo jak transakcja Stonewall, z tą różnicą, że ta pierwsza jest oparta na współpracy, podczas gdy druga nie. Jak widzieliśmy, transakcja Stonewall x2 obejmuje udział strony trzeciej, która jest zewnętrzna w stosunku do płatności i która dostarczy swoje bitcoiny w celu zwiększenia prywatności transakcji. W typowej transakcji Stonewall rolę współpracownika przejmuje nadawca.


Powróćmy do naszego przykładu Alice w piekarni. Gdyby nie mogła znaleźć kogoś takiego jak Bob, aby towarzyszył jej w wydatkach, mogłaby sama dokonać transakcji Stonewall. W ten sposób dwa wejściowe UTXO należałyby do niej, a na wyjściu otrzymałaby 3.

![transaction stonewall](assets/en/2.webp)


Z zewnętrznego punktu widzenia schemat transakcji pozostałby taki sam.

![Stonewall or Stonewall x2?](assets/en/5.webp)

W związku z tym logika powinna być następująca w przypadku korzystania z narzędzia Samourai:


- Jeśli sprzedawca nie obsługuje PayJoin Stowaway, transakcja kolaboracyjna może zostać przeprowadzona z inną osobą spoza płatności przy użyciu Stonewall x2.
- Jeśli nie znajdzie się nikt, kto mógłby wykonać transakcję Stonewall x2, transakcja Stonewall może zostać wykonana samodzielnie, naśladując zachowanie transakcji Stonewall x2.
- Wreszcie, ostatnią opcją byłoby zawarcie transakcji z JoinBot, serwerem utrzymywanym przez Samourai, który może, na żądanie, działać jako współpracownik w transakcji Stonewall x2.


Jeśli chcesz znaleźć współpracownika, który jest chętny do pomocy w transakcji Stonewall X2, możesz również odwiedzić tę grupę Telegram (nieoficjalną) prowadzoną przez użytkowników Samourai w celu łączenia nadawców i współpracowników: [Make Every Spend a CoinJoin](https://t.me/EverySpendACoinjoin).


[**-> Dowiedz się więcej o transakcjach Stonewall**](https://planb.network/tutorials/privacy/on-chain/stonewall-033daa45-d42c-40e1-9511-cea89751c3d4)


## Jaki jest cel transakcji Stonewall x2?


Struktura Stonewall x2 dodaje znaczną ilość entropii do transakcji i myli analizę łańcucha. Z zewnątrz taka transakcja może być interpretowana jako mały CoinJoin między dwiema osobami. W rzeczywistości jest to jednak płatność. Metoda ta generuje niepewność w analizie łańcucha, a nawet prowadzi do fałszywych tropów.


Wróćmy do przykładu Alice, Boba i piekarza. Transakcja na Blockchain wyglądałaby następująco:

![stonewall x2 public](assets/en/3.webp)

Zewnętrzny obserwator polegający na heurystyce analizy łańcucha może błędnie dojść do wniosku, że "Alice i Bob wykonali mały CoinJoin, z jednym UTXO na wejściu i dwoma UTXO na wyjściu."![misinterpretation stonewall x2](assets/en/4.webp)

Ta interpretacja jest nieprawidłowa, ponieważ, jak wiadomo, UTXO został wysłany do Baker, Alice ma tylko jedno wyjście zmiany, a Bob ma dwa.

![transaction stonewall x2](assets/en/1.webp)

Nawet jeśli zewnętrznemu obserwatorowi uda się zidentyfikować schemat transakcji Stonewall x2, nie będzie on posiadał wszystkich informacji. Nie będzie w stanie określić, który z dwóch UTXO o tych samych kwotach odpowiada płatności. Co więcej, nie będą w stanie stwierdzić, czy to Alice czy Bob dokonali płatności. Wreszcie, nie będą w stanie określić, czy dwa wejściowe UTXO pochodzą od dwóch różnych osób, czy też należą do jednej osoby, która je połączyła. Ten ostatni punkt wynika z faktu, że klasyczne transakcje Stonewall, które omówiliśmy powyżej, przebiegają dokładnie według tego samego schematu, co transakcje Stonewall x2. Z zewnątrz i bez dodatkowych informacji o kontekście niemożliwe jest odróżnienie transakcji Stonewall od transakcji Stonewall x2. Jednak te pierwsze nie są transakcjami opartymi na współpracy, podczas gdy te drugie są. Dodaje to jeszcze więcej wątpliwości co do tego wydatku.

![Stonewall or Stonewall x2 ?](assets/en/5.webp)



## Jak ustanowić połączenie między Paynyms, aby móc współpracować za pośrednictwem Soroban?


Podobnie jak w przypadku innych transakcji opartych na współpracy na Samourai (*Cahoots*), wykonanie Stonewall x2 obejmuje Exchange częściowo podpisanych transakcji między nadawcą a współpracownikiem. Exchange można wykonać ręcznie, jeśli jesteś fizycznie ze swoim współpracownikiem, lub automatycznie za pośrednictwem protokołu komunikacyjnego Soroban.


Jeśli wybierzesz drugą opcję, będziesz musiał ustanowić połączenie między Paynyms, zanim będziesz mógł wykonać Stonewall x2. Aby to zrobić, twój Paynym musi "podążać" za Paynym twojego współpracownika i vice versa.


**Dostęp do Paynym współpracownika:**


Aby rozpocząć, konieczne jest uzyskanie kodu płatności Paynym współpracownika. W aplikacji Samourai Wallet współpracownik musi nacisnąć ikonę swojego Paynym (mały robot) znajdującą się w lewym górnym rogu ekranu, a następnie kliknąć swój pseudonim Paynym, zaczynając od `+...`. Na przykład mój to `+namelessmode0aF`.


![samourai paynym](assets/notext/6.webp)

Jeśli Twój współpracownik korzysta ze Sparrow Wallet, powinien kliknąć zakładkę "Narzędzia", a następnie "Pokaż PayNym".![paynym sparrow](assets/notext/7.webp)

**Podążając za PayNymem swojego współpracownika z Samourai Wallet:**


Jeśli korzystasz z Samourai Wallet, uruchom aplikację i uzyskaj dostęp do menu "PayNyms" w ten sam sposób. Jeśli używasz PayNym po raz pierwszy, musisz uzyskać jego identyfikator.


![request paynym samourai](assets/notext/8.webp)


Następnie kliknij niebieski "+" w prawym dolnym rogu ekranu.

![add collaborator paynym](assets/notext/9.webp)

Następnie możesz wkleić kod płatności swojego współpracownika, wybierając "PASTE PAYMENT CODE" lub otworzyć kamerę, aby zeskanować jego kod QR, naciskając "SCAN QR CODE".

![paste paynym identifier](assets/notext/10.webp)


Kliknij przycisk "ŚLEDŹ".

![follow paynym](assets/notext/11.webp)

Potwierdź, klikając "TAK".

![confirm follow paynym](assets/notext/12.webp)

Następnie oprogramowanie wyświetli przycisk "CONNECT". Kliknięcie tego przycisku nie jest konieczne w przypadku naszego samouczka. Ten krok jest wymagany tylko wtedy, gdy planujesz dokonywać płatności do innego PayNym w ramach BIP47, co nie jest związane z naszym samouczkiem.

![connect paynym](assets/notext/13.webp)

Gdy twój PayNym będzie podążał za PayNymem twojego współpracownika, powtórz ten proces w przeciwnym kierunku, aby twój współpracownik mógł również podążać za tobą. Następnie możesz wykonać transakcję Stonewall x2.


**Podążając za PayNymem swojego współpracownika ze Sparrow Wallet:**


Jeśli korzystasz z Wallet Sparrow, otwórz Wallet i przejdź do menu "Pokaż PayNym". Jeśli korzystasz z PayNym po raz pierwszy, musisz uzyskać identyfikator, klikając "Retrieve PayNym".

![request paynym sparrow](assets/notext/14.webp)

Następnie wprowadź identyfikator PayNym współpracownika (jego pseudonim "+..." lub kod płatności "PM...") w polu "Znajdź kontakt" i kliknij przycisk "Dodaj kontakt".

![add contact paynym](assets/notext/15.webp)

Oprogramowanie wyświetli przycisk "Połącz kontakt". Kliknięcie tego przycisku nie jest konieczne w przypadku naszego samouczka. Ten krok jest wymagany tylko wtedy, gdy planujesz dokonywać płatności na wskazany PayNym w ramach BIP47, co nie jest związane z naszym samouczkiem.


Gdy twój PayNym będzie podążał za PayNymem twojego współpracownika, powtórz ten proces w przeciwnym kierunku, aby twój współpracownik mógł również podążać za tobą. Następnie możesz wykonać transakcję Stonewall x2.

## Jak dokonać transakcji Stonewall x2 na Samourai Wallet?


Jeśli ukończyłeś poprzednie kroki łączenia Paynyms, jesteś wreszcie gotowy do dokonania transakcji Stonewall x2! Aby to zrobić, postępuj zgodnie z naszym samouczkiem wideo na Samourai Wallet:

![Stonewall x2 Tutorial - Samourai Wallet](https://youtu.be/89oYE1Hw3Fk?si=QTqUZ6IypiR6PPMr)


## Jak dokonać transakcji Stonewall x2 na Sparrow Wallet?


Jeśli ukończyłeś poprzednie kroki łączenia Paynyms, jesteś wreszcie gotowy do dokonania transakcji Stonewall x2! Aby to zrobić, postępuj zgodnie z naszym samouczkiem wideo na Sparrow Wallet:

![Stonewall x2 Tutorial - Sparrow Wallet](https://youtu.be/mO3Xpp34Hhk?si=bfYiTl0Gxjs9sNQq)


**Zasoby zewnętrzne:**


- https://sparrowwallet.com/docs/spending-privately.html;
- https://docs.samourai.io/en/spend-tools#stonewallx2.