---
name: Programowanie Bitcoin
goal: Zbuduj kompletną bibliotekę Bitcoin od podstaw i zrozum podstawy kryptograficzne Bitcoin
objectives: 

 - Implementacja arytmetyki pól skończonych i operacji na krzywych eliptycznych w Pythonie
 - Programowe konstruowanie i analizowanie transakcji Bitcoin
 - Tworzenie adresów Testnet i rozgłaszanie transakcji w sieci
 - Opanuj podstawy matematyczne leżące u podstaw modelu bezpieczeństwa Bitcoin

---
# Podróż do skryptów i programów Bitcoin


Ten intensywny dwudniowy kurs, prowadzony przez Jimmy'ego Songa, pozwala zagłębić się w techniczne podstawy Bitcoin, budując kompletną bibliotekę Bitcoin od podstaw. Zaczynając od podstawowej matematyki pól skończonych i krzywych eliptycznych, przejdziesz przez parsowanie transakcji, wykonywanie skryptów i komunikację sieciową. Dzięki praktycznym ćwiczeniom kodowania w notatnikach Jupyter stworzysz własny Testnet Address, ręcznie skonstruujesz transakcje i wyślesz je bezpośrednio do sieci - a wszystko to przy jednoczesnym dogłębnym zrozumieniu zasad kryptograficznych, które sprawiają, że Bitcoin jest bezpieczny i Trustless.


Miłego odkrywania!


+++

# Wprowadzenie

<partId>bd35d5be-323e-42e0-a0ba-10729f71c3bd</partId>

## Przegląd kursu

<chapterId>ee9d6cdf-4c97-455b-8220-cf6dfc95cb8e</chapterId>

Witamy na kursie PRO 202 _**Programming Bitcoin**_, intensywnej podróży, która prowadzi cię od arytmetyki ciał skończonych aż po tworzenie i nadawanie prawdziwych transakcji w sieci testowej Bitcoina.

W tym kursie będziesz stopniowo budować bibliotekę Bitcoina w Pythonie, jednocześnie zdobywając podstawy kryptograficzne, protokołowe i programistyczne niezbędne do precyzyjnego zrozumienia bezpieczeństwa i wewnętrznego działania Bitcoina. Podejście PRO 202 jest całkowicie praktyczne: każda koncepcja jest natychmiast implementowana w notatnikach Jupyter, zapewniając wzajemne wzmocnienie teorii i kodu.

### Podstawowe pojęcia matematyczne dla Bitcoina

Ta pierwsza sekcja ustala niezbędne podstawy matematyczne. Zaimplementujesz arytmetykę ciał skończonych oraz operacje na krzywych eliptycznych (prawo grupy, dodawanie, podwajanie, mnożenie skalarne...) — warunki wstępne do ECDSA. Cel jest dwojaki: zrozumieć strukturę algebraiczną umożliwiającą podpisy kryptograficzne oraz zbudować niezawodne narzędzia w Pythonie do ich manipulacji.

Następnie sformalizujesz komponenty ECDSA: generowanie kluczy, formatowanie punktów, haszowanie, tworzenie i weryfikację podpisów. Ta sekcja bezpośrednio łączy teorię z praktyką, podkreślając szczegóły implementacji oraz solidność podstawowego modelu bezpieczeństwa.

### Wewnętrzne działanie transakcji Bitcoina

W drugiej części przeanalizujesz strukturę transakcji Bitcoina: UTXO, wejścia/wyjścia, sekwencje, skrypty, kodowania i inne. Napiszesz kod do konstruowania, podpisywania i weryfikowania transakcji, uzyskując precyzyjne zrozumienie tego, co jest zobowiązane przez hash i dlaczego.

Następnie zaimplementujesz minimalny wykonawca _Script_, przeanalizujesz kluczowe kody operacji i zweryfikujesz ścieżki wydatków. Celem jest umożliwienie ci audytu zachowania transakcji, diagnozowania błędów walidacji oraz rozumowania o bezpieczeństwie polityk wydatkowych.

### Wewnętrzne działanie sieci Bitcoina

W trzeciej części umieścisz transakcję w szerszym systemie: struktura bloku, nagłówki, trudność i mechanizm Proof-of-Work. Będziesz obsługiwać komunikaty protokołu, nagłówki bloków i drzewa Merkle’a.

Na koniec przeanalizujesz komunikację między węzłami peer-to-peer, optymalizację wiadomości oraz wprowadzenie SegWit.

Jak w każdym kursie na Plan ₿ Academy, ostatnia sekcja zawiera ocenę zaprojektowaną tak, aby utrwalić twoje zrozumienie. Gotowy odkryć wewnętrzne mechanizmy Bitcoina i napisać kod, który go napędza? Zaczynajmy!

# Podstawowe pojęcia matematyczne dla Bitcoin

<partId>2d7c7fe9-9a40-544c-92bc-d9222169ae08</partId>


## Matematyka dla wdrożenia Bitcoin

<chapterId>e6eac2b0-6067-5a0b-9fcd-bbe46f4d7346</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kryptografia krzywych eliptycznych

<chapterId>fbbaf4e1-e292-5973-aae8-5d4ba593b9fb</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Wewnętrzne elementy transakcji Bitcoin

<partId>5da35ad0-6180-11f0-bd66-13724db9fbbd</partId>


## Bitcoin Parsowanie transakcji i podpisy ECDSA

<chapterId>fde364cd-d696-562f-847d-2ef4ffb29a95</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Skrypt Bitcoin i walidacja transakcji

<chapterId>40b20c16-c21e-5173-9e4f-52620f5840a3</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Budowa transakcji i płatność skryptem Hash


<chapterId>860f50fc-0c9d-5767-a2d8-2934bf8181ba</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Sieć wewnętrzna Bitcoin

<partId>c058ed10-33b0-58e3-8b81-08e1ebede253</partId>


## Bloki Bitcoin i Proof of Work

<chapterId>12d77b0d-7807-52b8-8d86-8e8570300e6d</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Komunikacja sieciowa i drzewa Merkle'a

<chapterId>dc88b974-e09d-5ae5-ab0d-efc139fc7ffe</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Zaawansowana komunikacja z węzłami i oddzielny świadek

<chapterId>c7af1f3b-8a8f-5853-b547-3c178bc7f669</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sekcja końcowa


<partId>5d5d98dc-6c7b-11f0-83b5-eb1625573c9d</partId>


## Recenzje i oceny


<chapterId>f551b514-6ba5-11f0-833e-b33af48c067b</chapterId>

<isCourseReview>true</isCourseReview>


## Wnioski


<chapterId>7fdf0d2c-6c7c-11f0-9a86-d308a341f341</chapterId>

<isCourseConclusion>true</isCourseConclusion>
