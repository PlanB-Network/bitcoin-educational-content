---
name: Amboss
description: Eksploruj i analizuj Lightning Network
---

![cover](assets/cover.webp)



Lightning Network to Layer protokołu Bitcoin, który został opracowany przede wszystkim w celu promowania przyjmowania płatności Bitcoin na co dzień poprzez zwiększenie szybkości przetwarzania każdej transakcji. Opierając się na zasadzie decentralizacji, Lightning Network składa się z węzłów (komputerów z implementacją Lightning) komunikujących się peer-to-peer, przekazujących sobie nawzajem dane (płatności i weryfikację płatności).



https://planb.network/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Podobnie jak w przypadku głównego łańcucha, konieczne stało się umożliwienie użytkownikom poznania informacji i statusu sieci, aby ułatwić połączenia między węzłami i zminimalizować problem płynności, który zwykle pojawia się w sieci. Rzeczywiście, na Lightning Network zalecamy mikropłatności o stosunkowo mniejszych kwotach niż w przypadku transakcji na głównym łańcuchu Bitcoin.



Należy zauważyć, że nie wszystkie węzły Lightning są dostępne na platformie Amboss.



Podobnie jak [Mempool Space](https://Mempool.space), który dostarcza przydatnych informacji na temat głównego łańcucha protokołu Bitcoin, od 2022 roku [Amboss](https://amboss.space) dostarcza informacji na temat :





- Węzły na Lightning Network
- Kanały płatności i ich zdolność płatnicza
- Ewolucja Lightning Network w czasie
- Statystyki dotyczące opłat dla węzłów przekaźnikowych za płatności.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

W tym samouczku zabierzemy Cię na wycieczkę po tej platformie, która jest niezbędnym zasobem dla użytkowników Lightning Network, tych, którzy chcą podłączyć swój węzeł, aby rozszerzyć sieć itp.




## Znajdź pary



Jednym z celów platformy Amboss jest umożliwienie różnym węzłom w sieci łączenia się i przekazywania informacji między sobą. Na stronie głównej platformy możesz bezpośrednio wyszukać nazwę węzła, który już znasz, lub znaleźć węzły z najpopularniejszych portfeli Lightning, z których korzystasz.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.network/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Na stronie głównej znajdują się również węzły sklasyfikowane według :




- Ewolucja przepustowości: ilość Bitcoin powiązana z kluczem publicznym węzła i całkowita dostępna we wszystkich jego kanałach.
- Ewolucja kanału: liczba nowych połączeń z innymi węzłami w sieci.
- Popularność węzła: jak często węzeł jest używany.



![nodes](assets/fr/03.webp)



Wybór odpowiedniego węzła do połączenia sprowadza się zatem do sprawdzenia następujących kryteriów:





- Upewnij się, że węzeł ma wystarczającą ilość bitcoinów; im większa pojemność węzła, tym większą ilość bitcoinów możesz zapłacić.





- Upewnij się, że węzeł ma dużą liczbę połączeń i otwartych kanałów z innymi węzłami w sieci.





- Upewnij się, że węzeł jest aktywny i nadal doceniany przez rówieśników, sprawdzając liczbę nowych kanałów; im więcej nowych kanałów ma otwarty węzeł, tym bardziej jest doceniany przez inne węzły w sieci.



Po znalezieniu odpowiedniego węzła kliknij jego nazwę, aby zostać przekierowanym na stronę z informacjami o węźle.



Na tym Interface, sprawdzając Timestamp nowo utworzonego kanału, otrzymasz wskazówkę dotyczącą aktywności tego węzła. Znajdziesz tam również informacje na temat przepustowości kanałów tego węzła: ta informacja jest niezbędna, jeśli chcesz aktywnie korzystać z tego węzła do dokonywania płatności.




![node_info](assets/fr/04.webp)



W sekcji po lewej stronie znajdziesz więcej szczegółów na temat lokalizacji tego węzła. Na przykład można wyświetlić :




- Klucz publiczny: identyfikator tuż pod nazwą węzła.
- Położenie geograficzne tego węzła.




![channels](assets/fr/05.webp)



Ten Interface informuje o Address połączenia dla tego węzła: przyjmuje postać `pubkey@ip:port`. W naszym przykładzie chcemy połączyć się z węzłem, którego :




- klucz publiczny `pubkey` to: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Port: `9735`



![geoinfo](assets/fr/06.webp)



W sekcji **Kanały** zobaczysz listę otwartych kanałów i połączeń węzła z innymi węzłami w sieci. W tym Interface kilka informacji jest niezbędnych do potwierdzenia, że ten węzeł odpowiada naszym potrzebom lub jest niezawodny:





- Współczynnik przychodzący**: Kwota, jaką węzeł pobierze za każdy milion Satoshi, które otrzyma, w zależności od wybranego kanału.
- Współczynnik (części na milion)** : który reprezentuje liczbę Satoshi na milion jednostek, które węzeł naliczy, gdy zdecydujesz się dokonać płatności za pośrednictwem jednego z jego kanałów. Powiedzmy, że zdecydujesz się dokonać płatności w wysokości `10_000 Sats` za pośrednictwem kanału, którego współczynnik ppm wynosi `500 Sats`, będziesz musiał zapłacić węzłowi `10_000 * 500 / 1_000_000` satoshi, co odpowiada `5 Sats`.
- Maksymalna wartość [HTLC](https://planb.network/resources/glossary/htlc)** : Maksymalna kwota, jaką ten węzeł pozwala przesyłać za pośrednictwem jednego z tych kanałów.



Przeglądając tabelę w tym Interface, można również znaleźć wszystkie te informacje na temat węzła, do którego jest dopasowany.



![channels_info](assets/fr/07.webp)



W sekcji **Mapy kanałów** można zobaczyć dystrybucję i przepustowość różnych kanałów w tym węźle. Możesz zmienić wyświetlane kryteria dystrybucji, wybierając jedną z opcji z listy rozwijanej po prawej stronie.



![cha_maps](assets/fr/08.webp)



Sekcja **Zamknięte kanały** grupuje wszystkie poprzednie kanały węzła zgodnie z typem zamknięcia:




- Wzajemne zamknięcie**: reprezentuje porozumienie obu stron, które używają swojego klucza prywatnego do podpisania transakcji oznaczającej zamknięcie kanału i dystrybucję sald w jego ramach
- **Wymuszone zamknięcie**: reprezentuje nagłe, jednostronne zamknięcie jednej części kanału. Ten rodzaj zamknięcia nie jest zalecany, ponieważ Lightning Network jest protokołem opartym na karach: gdy próbujesz wyłudzić saldo kanału, ryzykujesz utratę całego dostępnego salda w tym kanale.



![closed](assets/fr/09.webp)



Uzyskaj informacje o opłatach tranzytowych za przekierowanie płatności przez kanał w używanym węźle



![fees](assets/fr/10.webp)



## Informacje o sieci



Amboss koncentruje się nie tylko na informacjach o członkach sieci, ale także na stanie samej sieci.



W sekcji **Statystyki**, pod lewym menu "Symulacje", znajdziesz wykres pokazujący prawdopodobieństwo udanej płatności w funkcji kwoty płatności.



W rzeczywistości zauważysz, że krzywa maleje, ponieważ wraz ze wzrostem kwoty płatności masz mniejsze szanse na jej realizację. Odzwierciedla to prawdziwy problem z płynnością na Lightning Network. Na przykład, płatność w wysokości `10_000` satoshi ma `79%` szans na realizację. Z drugiej strony, dla płatności w wysokości `3_000_000` satoshis masz mniej niż `13%` szans na sukces.



![network](assets/fr/11.webp)



Menu **Statystyki sieci** umożliwia graficzne wyświetlanie statystyk dla :




- Kanały płatności
- Węzły
- Pojemność
- Opłaty
- Ewolucja kanałów.



![network_stat](assets/fr/12.webp)



W menu **Statystyki rynkowe**, opcja **Szczegóły zamówienia** umożliwia wyświetlenie popytu na płynność na Lightning Network. Wykres ten może również pokazywać, które kanały cieszą się największym popytem i/lub które mają znaczną przepustowość.



![markets](assets/fr/13.webp)




## Narzędzia



Amboss oferuje szereg narzędzi pomagających w optymalizacji wyszukiwań i działań.



### Dekoder Lightning Network



To narzędzie jest głównie odpowiedzialne za podanie szczegółów struktury Lightning Invoice, Lightning Address lub Lightning URL.



Na stronie głównej, w sekcji **Narzędzia**, prześlij swój Lightning Address, na przykład.



![decoder](assets/fr/14.webp)



Z tego dekodera można uzyskać informacje takie jak :




- klucz publiczny węzła powiązany z Lightning Address;
- Czas wygaśnięcia Invoice z Address;
- Minimalna i maksymalna wartość, jaką można wysłać;
- Węzeł Nostr powiązany z twoim Address, jeśli Nostr jest włączony w tym węźle.



![decode](assets/fr/15.webp)



### Magma IA



Odkryj najnowsze narzędzie zaprezentowane przez Amboss, aby efektywnie zarządzać połączeniami z węzłami Lightning Network. Magma AI wykorzystuje dedykowaną sztuczną inteligencję, aby skupić się na ważnym problemie: dokonaniu dobrego wyboru węzłów do połączenia.



![magma](assets/fr/16.webp)



### Kalkulator Satoshi



Sprawdź aktualną cenę Bitcoin w lokalnej walucie (EUR / USD). Na stronie głównej użyj kalkulatora satoshis, aby sprawdzić aktualną cenę rynkową.



![calculator](assets/fr/17.webp)




Zapoznałeś się już z funkcjami i narzędziami analitycznymi platformy. Poniżej znajduje się nasz artykuł na temat eksploratora Bitcoin **Mempool.space**.



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f