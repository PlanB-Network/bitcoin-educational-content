---
name: Slipstream
description: Wysyłanie podpisanej transakcji bezpośrednio do górnika za pomocą Slipstream, bez rozgłaszania jej w sieci Bitcoin
---

![cover](assets/cover.webp)

Zwykle, gdy podpisujesz transakcję, jest ona automatycznie rozgłaszana do wszystkich węzłów Bitcoina w sieci. Następnie czeka na wydobycie.

Dopóki jednak nie znajdzie się w bloku, atakujący, który zdobył twój klucz prywatny, mógłby ją zastąpić i ukraść środki. Tak jest zwykle w przypadku, gdy używasz hardware walleta ColdCard.

Narzędzie Slipstream od firmy wydobywczej MARA pozwala pominąć rozgłaszanie transakcji w sieci: jest ona wysyłana bezpośrednio (i wyłącznie) do jednego górnika, co utrzymuje ją w prywatności i pozwala uniknąć ujawnienia jej w sieci. Wydobycie transakcji zajmie prawdopodobnie więcej czasu, ale będzie ona chroniona przed atakiem polegającym na zastąpieniu.

Poniżej przedstawiamy poradnik pozwalający użytkownikom [Liana](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), a także użytkownikom portfela [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) korzystać z narzędzia Slipstream górnika MARA za pośrednictwem strony [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

⚠️ **Ostrzeżenie**: to narzędzie jest przeznaczone tylko dla określonych profili, głównie portfeli Liana, portfeli miniscript i niektórych rodzajów multisiga. Wizardsardine **wyraźnie odradza** używanie go w przypadku portfeli, których środki są już narażone na krytyczne ryzyko kradzieży, na przykład tych, których fraza odzyskiwania została wygenerowana na urządzeniu ColdCard dotkniętym luką w generatorze liczb losowych. W takiej sytuacji wyścig z atakującym rozstrzyga się w kilka sekund, a transakcja wysłana do jednego górnika potwierdza się znacznie dłużej niż transakcja rozgłoszona normalnie. Jeśli cię to dotyczy, przeczytaj najpierw nasz osobny poradnik:

https://planb.academy/tutorials/wallet/hardware/coldcard-seed-vulnerability-1348b153-89db-429c-80af-b5d3d8506b9a

## Dla użytkowników Liany

Liana jest utrzymywana przez Wizardsardine, wydawcę strony [outofband.wizardsardine.com](https://outofband.wizardsardine.com/), więc droga jest prosta: wystarczy, że wyeksportujesz podpisany plik PSBT, zamiast rozgłaszać transakcję.

*Wymagane: mieć środki na swoim portfelu Liana.*

### Krok 1: Utwórz transakcję w Lianie

Jak zwykle zbuduj transakcję, dodając adres docelowy, opis i kwotę (tutaj maksimum dostępne w portfelu).

Aby ustawić stawkę opłat:

- wybierz monety, które chcesz wydać, klikając małe pole w lewym dolnym rogu, pod "Coins selection";
- następnie wpisz stawkę opłat. Pamiętaj, aby ustawić opłaty znacznie wyższe niż sugerowana stawka, jak opisano na tej stronie: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Na koniec kliknij "Next".

![Budowanie transakcji w Lianie](assets/fr/01.webp)

### Krok 2: Sprawdź szczegóły transakcji

Przed kliknięciem "Sign" sprawdź szczegóły swojej transakcji, w szczególności:

- wysyłaną kwotę;
- liczbę satoshi przeznaczonych na opłaty transakcyjne;
- ale przede wszystkim adres, na który wysyłasz środki (pamiętaj, aby sprawdzić pierwsze 5/6 znaków, ostatnie 5/6 oraz 5/6 znaków w środku adresu, aby uniknąć ataków typu "address poisoning").

![Sprawdzanie szczegółów transakcji](assets/fr/02.webp)

### Krok 3: Wybierz portfele podpisujące

Następnie wybierz portfele software'owe i/lub hardware'owe, którymi musisz podpisać swoją transakcję. Krótkie przypomnienie: w przypadku portfela multisig 2 z 2 potrzebujesz 2 podpisów z 2.

### Krok 4: Wyeksportuj plik PSBT swojej transakcji

Transakcja Bitcoin jest teraz podpisana odpowiednimi kluczami. Nie klikaj "Broadcast", w przeciwnym razie zostanie ona udostępniona całej sieci, a jeśli używasz hardware walleta ColdCard, twoja transakcja zostanie publicznie ujawniona i twoje środki będą zagrożone.

Możesz teraz kliknąć "Export", a następnie zapisać plik PSBT lokalnie na swoim komputerze.

![Eksportowanie pliku PSBT z Liany](assets/fr/03.webp)

### Krok 5: Wyślij transakcję do górnika przez outofband.wizardsardine.com

Teraz ostatnie kroki. Aby wysłać transakcję do górnika, wystarczy wziąć plik PSBT i przeciągnąć go do wyznaczonego obszaru.

![Upuszczanie pliku PSBT na outofband.wizardsardine.com](assets/fr/04.webp)

Transakcja jest wtedy wyświetlana tak, jak pokazano poniżej.

![Transakcja w kolejce](assets/fr/05.webp)

### Krok 6: Wyślij transakcję przez Slipstream

Na koniec wystarczy kliknąć "Send", aby transakcja została wysłana do MARA przez Slipstream.

![Wysyłanie transakcji przez Slipstream](assets/fr/06.webp)

W ciągu kilku sekund status transakcji zmienia się ze "Sending" na "Accepted":

![Transakcja zaakceptowana przez Slipstream](assets/fr/07.webp)

Pozostaje już tylko skopiować identyfikator transakcji (TXID), a następnie wkleić go w [mempool.space](https://mempool.space/), aby obserwować jej wydobycie:

![Wyszukiwanie TXID na mempool.space](assets/fr/08.webp)

Uwaga: transakcja będzie wyświetlana jako "Transaction not found", dopóki górnik MARA nie wykopie bloku i nie umieści w nim twojej transakcji. Może to zająć kilkadziesiąt minut, a nawet godziny, ponieważ MARA posiada zaledwie około 4,5% hashrate'u sieci Bitcoin. Na dzień 4 sierpnia 2026 r. odpowiada to w przybliżeniu jednemu blokowi wydobywanemu co 3 godziny i 45 minut.

## Dla użytkowników innych portfeli

Jeśli nie używasz [Liany](https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04), ale nadal chcesz skorzystać z tego narzędzia, oto poradnik wykorzystujący portfel multisig 2 z 2. Użyjemy do tego portfela software'owego [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d).

*Wymagane: mieć środki na swoim portfelu Sparrow.*

### Krok 1: Utwórz transakcję

W [Sparrow](https://planb.academy/tutorials/wallet/desktop/sparrow-c674e2ac-d46f-4c82-92a7-7d1b0e262f5d) utwórz transakcję w swoim portfelu multisig. Pamiętaj, aby ustawić opłaty znacznie wyższe niż sugerowana stawka, jak opisano na tej stronie: [outofband.wizardsardine.com](https://outofband.wizardsardine.com/).

Po jej utworzeniu kliknij "Create Transaction".

![Tworzenie transakcji w Sparrow](assets/fr/09.webp)

### Krok 2: Sfinalizuj transakcję

Aby sfinalizować transakcję, musisz ją teraz podpisać. W tym celu kliknij "Finalize Transaction for Signing".

![Finalizowanie transakcji do podpisu](assets/fr/10.webp)

### Krok 3: Podpisz transakcję swoimi różnymi kluczami

Teraz nadchodzi czas na podpisanie transakcji. Aby to zrobić, wystarczy podpisać ją portfelem software'owym lub hardware'owym, którego używasz.

![Podpisywanie transakcji kluczami multisiga](assets/fr/11.webp)

### Krok 4: Pobierz podpisaną transakcję i nie rozgłaszaj jej w sieci

Transakcja Bitcoin jest teraz podpisana oboma kluczami naszego multisiga 2 z 2. Nie klikaj "Broadcast Transaction", w przeciwnym razie zostanie ona udostępniona całej sieci, a jeśli używasz hardware walleta ColdCard, twoja transakcja zostanie publicznie ujawniona i twoje środki będą zagrożone.

![Podpisana transakcja, gotowa, ale nierozgłoszona](assets/fr/12.webp)

### Krok 5: Wyświetl skrypt podpisanej transakcji lub pobierz plik PSBT

Aby wyświetlić podpisaną transakcję Bitcoin, kliknij teraz "View Final Transaction". Możesz następnie skopiować skrypt podpisanej transakcji Bitcoin:

*02000000000101ade28cc43b2f51e09c88a87dfaeda8a601a78cddb458e47d99f0651020c1aaa60000000000fdffffff010b370000000000002200201810640a195e5a992d1f6da58a9781f77db47ac63a332b072580cc5b57dd1c2e04004730440220320777c52799cc8015be7c3f724a3d77906ce3d551205c893347910279ed796a02204ee45912623c1c45bf3d93d6558d878737f88f20dcbd152dc28fac80e788f2aa01473044022008bf6ea8432e3fee0eaa7edb923f60e44bb5eb37e52a93d8fdb4e30814340b0f0220473f8fcfbadda9c86fdfc4d3dd55c7883f62312794361e4d4d93f52964bce6520147522102bd28ad9b52829baf62621821abb49339262c7ef32f8adf15bf01b4d91fb5a9a72103ace1a518996275cbf9ebdbeaa4703318a50d5ab7f0fe22b9e566d2f2f644ed3752ae9fa90e00*

![Wyświetlanie skryptu podpisanej transakcji](assets/fr/13.webp)

Jeśli chcesz pobrać plik transakcji, możesz albo:

- kliknąć "File", a następnie "Save transaction…";
- albo kliknąć przycisk połączenia sieciowego w prawym dolnym rogu (żółty przycisk), a następnie kliknąć "Save Final Transaction".

Transakcja zostanie wtedy zapisana lokalnie na twoim komputerze.

![Zapisywanie finalnej transakcji lokalnie](assets/fr/14.webp)

### Krok 6: Wyślij transakcję do górnika przez outofband.wizardsardine.com

Teraz ostatnie kroki. Aby wysłać transakcję do górnika, wystarczy:

- przejść na [outofband.wizardsardine.com](https://outofband.wizardsardine.com/);
- wkleić skrypt podpisanej transakcji skopiowany w poprzednim kroku, a następnie kliknąć "ADD TO QUEUE" poniżej;

![Wklejanie skryptu transakcji do narzędzia](assets/fr/15.webp)

- albo wziąć plik i przeciągnąć go do wyznaczonego obszaru.

![Upuszczanie pliku transakcji na narzędzie](assets/fr/16.webp)

Transakcja jest wtedy wyświetlana tak, jak pokazano poniżej.

![Transakcja w kolejce](assets/fr/17.webp)

Jeśli komunikat informuje cię, że całkowita kwota wejściowa satoshi w twojej transakcji jest nieznana (i że w związku z tym nie można obliczyć liczby satoshi na opłaty), wystarczy, że wpiszesz całkowitą kwotę wejściową satoshi ręcznie. Aby ją znaleźć, wystarczy kliknąć na widok swojej transakcji w Sparrow, w środku diagramu:

![Całkowita kwota wejściowa pokazana w Sparrow](assets/fr/18.webp)

Następnie wpisz tę kwotę (15 904 sats w naszym przykładzie) w narzędziu [outofband.wizardsardine.com](https://outofband.wizardsardine.com/):

![Ręczne wpisywanie całkowitej kwoty wejściowej](assets/fr/19.webp)

Na koniec sprawdź, czy stawka opłat jest prawidłowa.

### Krok 7: Wyślij transakcję przez Slipstream

Na koniec wystarczy kliknąć "Send", aby transakcja została wysłana do MARA przez Slipstream.

![Wysyłanie transakcji przez Slipstream](assets/fr/20.webp)

W ciągu kilku sekund status transakcji zmienia się ze "Sending" na "Accepted":

![Transakcja zaakceptowana przez Slipstream](assets/fr/21.webp)

Pozostaje już tylko skopiować identyfikator transakcji (TXID), a następnie wkleić go w [mempool.space](https://mempool.space/), aby obserwować jej wydobycie:

![Wyszukiwanie TXID na mempool.space](assets/fr/22.webp)

Uwaga: transakcja będzie wyświetlana jako "Transaction not found", dopóki górnik MARA nie wykopie bloku i nie umieści w nim twojej transakcji. Może to zająć kilkadziesiąt minut, a nawet godziny, ponieważ MARA posiada zaledwie około 4,5% hashrate'u sieci Bitcoin. Na dzień 4 sierpnia 2026 r. odpowiada to w przybliżeniu jednemu blokowi wydobywanemu co 3 godziny i 45 minut.
