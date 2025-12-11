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

<partId>e545b7a7-b596-436e-86e9-d0ddceb72543</partId>


## Matematyka dla wdrożenia Bitcoin

<chapterId>790e5214-836b-40fe-bbd6-f4ccc920b778</chapterId>

![lecture](https://www.youtube.com/watch?v=OFHNu82g1mI)


## Kryptografia krzywych eliptycznych

<chapterId>7d3d842e-ae88-472e-85ff-196d60655815</chapterId>

![lecture](https://www.youtube.com/watch?v=xOXdKuF3UFw)


# Wewnętrzne elementy transakcji Bitcoin

<partId>774c0e80-d316-414a-bd59-0bbd185d3b58</partId>


## Bitcoin Parsowanie transakcji i podpisy ECDSA

<chapterId>ae86fc27-2f27-4de9-b17c-351c00690144</chapterId>

![lecture](https://www.youtube.com/watch?v=dEArQBDgXgA)


## Skrypt Bitcoin i walidacja transakcji

<chapterId>8f0d4381-2b36-4c66-8bee-1100b2dfd8ed</chapterId>

![lecture](https://www.youtube.com/watch?v=g1wd-qwbHM8)


## Budowa transakcji i płatność skryptem Hash


<chapterId>1a6ca3fa-a71f-4b7e-9337-7c84a0b3f928</chapterId>

![lecture](https://www.youtube.com/watch?v=j0VHdGsFy2o)


# Sieć wewnętrzna Bitcoin

<partId>6af9d722-07da-487b-bf08-1b30bc3db3d4</partId>


## Bloki Bitcoin i Proof of Work

<chapterId>28a0f5d3-af1b-4093-be49-e3112e1d48a4</chapterId>

![lecture](https://www.youtube.com/watch?v=lJYSM1iLWQU)


## Komunikacja sieciowa i drzewa Merkle'a

<chapterId>dd8e23bc-ddd6-45a6-8d3a-16bc86ba49ac</chapterId>

![lecture](https://www.youtube.com/watch?v=Yq02tjpYmaQ)


## Zaawansowana komunikacja z węzłami i oddzielny świadek

<chapterId>8d70c283-4609-46a8-ad24-83b04a68529a</chapterId>

![lecture](https://www.youtube.com/watch?v=itce1zdUqjQ)



# Sekcja końcowa


<partId>f338e5f4-216e-4b38-bf56-8333e674c04c</partId>


## Recenzje i oceny


<chapterId>e149d14b-e99f-428a-a775-ed50cd0a6e9b</chapterId>

<isCourseReview>true</isCourseReview>

## Final Exam

<chapterId>91db243d-8479-4636-afa8-dd189b0d4c5e</chapterId>


<isCourseExam>true</isCourseExam>


## Wnioski


<chapterId>247bcefb-b158-42a3-82f4-c58bcad4a47a</chapterId>

<isCourseConclusion>true</isCourseConclusion>
