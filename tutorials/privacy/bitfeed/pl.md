---
name: Bitfeed
description: Poznaj główny łańcuch protokołów Bitcoin.
---

![cover](assets/cover.webp)



Bitfeed to platforma do wizualizacji warstwy onchain protokołu Bitcoin. Została zainicjowana przez jednego ze współtwórców projektu Mempool.space i wyróżnia się głównie minimalistycznym wyglądem i łatwością użytkowania.



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

W tym samouczku przyjrzymy się temu narzędziu, które pozwala przeglądać wszystkie transakcje i bloki w sieci.



## Rozpoczęcie pracy z Bitfeed



Bitfeed to platforma, która koncentruje się na trzech głównych punktach:





- Konsultacje Blockchain**,
- Wyszukiwanie transakcji**,
- Wizualizacja mempool**.



### Konsultacje dotyczące łańcucha bloków



Na stronie głównej Bitfeed można znaleźć głównie :





- Pasek wyszukiwania: Ta sekcja jest punktem wejścia dla zapytań blockchain. Tutaj można wyszukać określony blok według jego numeru lub skrótu. Możesz także wyszukiwać określone transakcje i adresy Bitcoin, aby zweryfikować określone informacje o transakcjach w sieci.



![searchBar](assets/fr/01.webp)



W lewym górnym rogu można zobaczyć aktualną cenę bitcoina, oszacowaną w dolarach amerykańskich (USD).



![price](assets/fr/02.webp)



Na prawym pasku bocznym znajduje się menu platformy. Z tego menu można dostosować interfejs platformy do własnych upodobań, dodawać lub usuwać elementy oraz dostosowywać filtry wyświetlania. Można na przykład wyświetlić rozmiar każdego bloku według wartości lub według wagi w bajtach wirtualnych (vBytes).



![menu](assets/fr/03.webp)



Pośrodku strony znajduje się ostatni wydobyty blok z widokiem wszystkich transakcji zawartych w tym bloku. Ta sekcja zawiera informacje o znaczniku czasu, całkowitej liczbie bitcoinów zaangażowanych w blok, rozmiarze bloku w bajtach, liczbie transakcji i średnim współczynniku kosztu transakcji na wirtualny bajt w bloku.



![block](assets/fr/04.webp)



Możesz cofnąć się do historii kanału, wyszukując określony blok na pasku wyszukiwania i przeglądać go zgodnie z własnymi kryteriami.



Na przykład, chcemy wyświetlić transakcje w bloku `879488`.



![bloc](assets/fr/05.webp)



Pierwsza transakcja tego bloku reprezentuje transakcję **coinbase**, która umożliwia górnikowi tego bloku zdobycie nagrody mining, którą można wydać dopiero po wydobyciu 100 bloków, składającej się z uwzględnionych opłat transakcyjnych i dotacji blokowej. Ta transakcja umożliwia emisję nowych bitcoinów w systemie.



![coinbase](assets/fr/06.webp)



https://planb.academy/courses/obtenir-ses-premiers-bitcoins-f3e3843d-1a1d-450c-96d6-d7232158b81f

Domyślnie transakcje w bloku są reprezentowane według dwóch kryteriów:




- Rozmiar, który może różnić się między wartością a wagą (vBytes);
- Kolor może się różnić w zależności od wieku i stosunku opłat transakcyjnych do wirtualnego bajtu.



![options](assets/fr/07.webp)



Możemy zatem stwierdzić, że wszystkie transakcje zawarte w tym samym bloku mają taką samą liczbę potwierdzeń w łańcuchu bloków. Największe kostki reprezentują transakcje zawierające największą ilość bitcoinów.



Interpretacja ta jest dodatkowo potwierdzona przez opcję menu **"Info "**, która informuje nas o tłumaczeniu koloru i rozmiaru transakcji bloku.



![infos](assets/fr/08.webp)



Można również wyświetlić transakcje bloku według wirtualnych bajtów i współczynnika opłat. Ten widok może różnić się od poprzedniego, ponieważ wartość bitcoinów zawarta w transakcji nie określa jej rozmiaru.



![visualisation](assets/fr/09.webp)



### Wyświetlanie transakcji



Transakcję można wyszukać za pomocą jej identyfikatora na pasku wyszukiwania. Możesz także kliknąć kostkę, aby wyświetlić informacje związane z tą transakcją.



W naszym przypadku weźmy transakcję zajmującą największą przestrzeń w bloku `879488`.



![biggest](assets/fr/10.webp)



Zobaczysz, że ta transakcja ma wartość `42,989`, która reprezentuje różnicę między ostatnim wydobywanym blokiem a naszym wybranym blokiem. Potwierdzenia te pomagają wzmocnić bezpieczeństwo sieci Bitcoin, ponieważ aby złośliwie zmodyfikować tę transakcję, atakujący musieliby posiadać równoważną moc obliczeniową, aby przepisać cały główny łańcuch bloków.



Rozmiar tej transakcji wynosi `57 088 vBajtów`, głównie ze względu na dużą liczbę UTXO użytych do jej budowy (842 wpisy). Co zaskakujące, zastosowany współczynnik opłat pozostaje stosunkowo niski (tylko 4 sats/vByte) w porównaniu do ogólnej średniej bloku wynoszącej 5,82 sats/vByte.



Transakcja zajmująca najwięcej miejsca niekoniecznie jest zatem transakcją o najwyższym współczynniku kosztów transakcyjnych.



![transaction](assets/fr/11.webp)



Jeśli podążasz za skalą w menu **Info**, transakcja o najwyższym współczynniku kosztów transakcji jest fioletowa. Jest to transakcja [bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35](https://bitfeed.live/tx/bfd81fdde02055ced809419b4fae094576bc4384a1d0444c723b3ba052e99a35) ze współczynnikiem kosztu transakcji `147.49 sats/vBytes`.



![mostfeerate](assets/fr/12.webp)



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

### Wizualizacja Mempool



Mempool to wirtualna lokalizacja, w której grupowane są transakcje Bitcoin oczekujące na włączenie do bloku. Bitfeed umożliwia przeglądanie [mempool](https://planb.academy/resources/glossary/mempool) kilku górników Bitcoin, oferując szeroki zakres śledzenia transakcji.



![mempool](assets/fr/13.webp)



W tej sekcji można śledzić wszystkie ważne i jeszcze niepotwierdzone transakcje w głównym łańcuchu sieci Bitcoin.



![unconfirmed](assets/fr/14.webp)



Masz teraz przewodnik po korzystaniu z platformy Bitfeed do analizowania bloków i transakcji w celu wizualizacji informacji dostępnych w głównym łańcuchu sieci Bitcoin, jednocześnie korzystając z minimalistycznego, łatwego w użyciu interfejsu. Jeśli spodobał Ci się ten samouczek, zalecamy wykonanie następnego kroku: odkrycie Lightning Network za pośrednictwem projektu Amboss.



https://planb.academy/tutorials/node/lightning-network/amboss-37044cad-0f85-41eb-af18-491384af1017