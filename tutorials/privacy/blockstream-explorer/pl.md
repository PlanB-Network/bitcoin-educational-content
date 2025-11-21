---
name: Blockstream Explorer
description: Poznaj główną warstwę Bitcoin i Liquid Network
---

![cover](assets/cover.webp)



Blockstream Explorer to projekt, który ułatwia eksplorację transakcji i globalnego stanu protokołu Bitcoin, a także [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) Liquid opracowanego przez firmę Blockstream.



Zainicjowany w 2014 roku przez Blockstream, firmę założoną przez Adama Backa, eksplorator [blockstream.info](https://blockstream.info) ma na celu zapewnienie solidnej infrastruktury dla Bitcoin, gwarantując interoperacyjność i śledzenie transakcji między warstwami (on-chain i Liquid), jednocześnie zwiększając bezpieczeństwo i prywatność użytkowników.



W tym samouczku przyjrzymy się temu, co go wyróżnia, jego usługom i temu, jak oferuje płynne monitorowanie operacji i stanu warstw Bitcoin on-chain i Liquid.



## Rozpoczęcie pracy z eksploratorem Blockstream



### Nawigacja po kanale głównym



Po przejściu do eksploratora Blockstream.info, w "**Dashboard**" domyślnie wybrany jest główny łańcuch protokołu Bitcoin. Z tego interfejsu można uzyskać przegląd :





- Główny rozmiar łańcucha: Ostatnio wydobyte bloki.



![blocks](assets/fr/01.webp)



Ta sekcja zawiera informacje o ostatnio wydobytych blokach, znaczniku czasu, liczbie transakcji zawartych w każdym bloku, rozmiarze w kilobajtach (kB) i pomiarze każdego bloku w jednostkach wagi (**WU** = *Weight Units*). Ten ostatni pomiar jest interesujący, ponieważ pozwala nam ocenić optymalizację bloku, biorąc pod uwagę, że każdy blok głównego łańcucha jest ograniczony do `4 000 000 WU` lub `4 000 kWU`.





- Ostatnie transakcje.



![transactions](assets/fr/02.webp)



Sekcja transakcji zawiera informacje o unikalnym identyfikatorze transakcji, zaangażowanej wartości bitcoinów, rozmiarze w wirtualnych bajtach (vB) - który reprezentuje sumę wszystkich danych (wejściowych i wyjściowych) - oraz powiązanej stawce opłaty. Na przykład transakcja o rozmiarze `153 vB` przy stawce `2 sat/vB` będzie wiązać się z opłatą w wysokości `306 satoshis`.



### Eksploracja płynów



Z menu "**Blocks**" można prześledzić historię całego głównego łańcucha aż do ostatniego wydobytego bloku.



![blocs](assets/fr/03.webp)



Klikając określony blok, można uzyskać więcej szczegółów na temat zawartych w nim informacji i transakcji. Na przykład dla bloku 919330: zobaczysz hash bloku. Możesz także przejść do poprzedniego bloku, ponieważ każdy wydobywany blok (oprócz Genesis) jest powiązany z poprzednim, zachowując hash swojego poprzednika.



![metadata](assets/fr/04.webp)



Klikając przycisk **"Szczegóły "**, można uzyskać więcej informacji na temat tego bloku, takich jak jego status, który potwierdza, że został on dodany do zachowanego i propagowanego łańcucha głównego. Dostępna jest również trudność, z jaką ten blok jest wydobywany: trudność ta reprezentuje moc obliczeniową wymaganą do rozwiązania problemu kryptograficznego mining i jest dostosowywana co 2016 bloków (około 2 tygodnie).



![details](assets/fr/05.webp)



Poniżej tej sekcji szczegółów znajdują się wszystkie transakcje zawarte w tym bloku.



Pierwsza transakcja w bloku nazywana jest **transaction coinbase**. Służy ona do alokacji nagrody mining górnika (wszystkie opłaty związane z transakcjami zawartymi w bloku i dotacją blokową). Bitcoiny utworzone przez tę transakcję można wydać dopiero po wydobyciu kolejnych 100 kolejnych bloków. Innymi słowy, aby móc z nich skorzystać, górnik będzie musiał poczekać na wyprodukowanie bloku **919430**. Jest to znane jako [*"okres zapadalności "*](https://planb.academy/fr/resources/glossary/maturity-period).



Coinbase jest szczególną transakcją: jest to jedyna transakcja bez rzeczywistego wkładu, ponieważ nie wydaje żadnych bitcoinów z poprzedniej transakcji.




![coinbase](assets/fr/06.webp)



Wszystkie inne transakcje są podzielone na dwie sekcje: wejścia i wyjścia.



Aby bitcoiny mogły zostać użyte jako dane wejściowe w nowej transakcji, inicjator transakcji musi udowodnić ich posiadanie, dostarczając podpis odpowiadający określonemu skryptowi. Każdy kawałek bitcoinów (UTXO) zawiera skrypt wymagający określonego podpisu, który może dostarczyć tylko klucz prywatny posiadacza. Skrypty te to ***scriptSig*** (w ASM), napisane w Bitcoin Script i mogą być różnego rodzaju. W tym przykładzie widzimy, że użyte UTXO były typu P2SH do wyjścia typu P2WPKH (*Pay-to-Witness-Public-Key-Hash*).



Możesz prześledzić historię konkretnego UTXO za pomocą heurystyki. Zapraszamy do zapoznania się z różnymi heurystykami Bitcoin i sposobami wzmocnienia poufności transakcji na Bitcoin:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Weźmy przykład wydatków wychodzących z tej transakcji. Klikając na identyfikator transakcji, zostajemy przekierowani do sekcji **Transakcje** na stronie szczegółów transakcji.



![transaction](assets/fr/08.webp)



Z tej strony można dowiedzieć się, w którym bloku transakcja została zawarta. W zależności od rodzaju użytego adresu, transakcja może zoptymalizować swoje dane (*wirtualne bajty*), a tym samym zapłacić mniej opłat transakcyjnych. Na przykład ta transakcja zaoszczędziła 53% opłat, używając natywnego formatu adresu SegWit Bech32 zaczynającego się od `bc1q`.



![trx_details](assets/fr/09.webp)



## Warstwa Liquid



Liquid Network to [*sidechain*](https://planb.academy/en/resources/glossary/sidechain) i rozwiązanie open source poziomu 2 dla protokołu Bitcoin. W szczególności umożliwia szybsze i bardziej poufne transakcje bitcoinowe.



W eksploratorze Blockstream.info kliknij przycisk **"Liquid"**, aby przełączyć się do sieci Liquid.



![liquid](assets/fr/10.webp)



Klikając na jedną z transakcji, które chcemy śledzić, widzimy, że kwoty bitcoinów zostały zastąpione słowami "**Poufne**". W tej sieci transakcje mogą być poufne, więc nie możemy zobaczyć kwot każdego UTXO, ani w transakcji, ani poza nią.



![liquid_trx](assets/fr/11.webp)



Zwracamy jednak uwagę, że zasady i mechanizmy obecne w głównej warstwie protokołu Bitcoin są takie same: skrypty blokujące bitcoiny i identyfikowalność UTXO.



![liquid_details](assets/fr/12.webp)



Liquid Network zapewnia również nie-depozytowe zasoby cyfrowe, z których mogą korzystać organizacje. W menu **"Assets "** znajdziesz listę zarejestrowanych zasobów, ich sumę i domenę, do której się odnoszą.



![assets](assets/fr/13.webp)



Dla każdego aktywa można prześledzić historię transakcji emisji i spalenia (usuwając sumę w obiegu).



![assets_trxs](assets/fr/14.webp)




## Więcej opcji



Eksplorator Blockstream.info zawiera również wizualizacje i śledzenie transakcji na Testnet, Bitcoin, on-chain i Liquid Network.



![testnet](assets/fr/15.webp)



Kiedy przechodzisz do sieci Testnet, nie używasz prawdziwych bitcoinów, ale masz wszystkie funkcje opisane powyżej.



![liquid_testnet](assets/fr/16.webp)



Sieć ta posiada łańcuch o różnej długości, do którego można podłączyć i przetestować działanie mechanizmów Bitcoin i Liquid.





- Sekcja API jest przeznaczona dla każdego, kto chce zintegrować niektóre funkcje Eksploratora z własną aplikacją. Za pomocą API można sprawdzić główny łańcuch różnych warstw (on-chain i Liquid), śledzić transakcje i dowiedzieć się na przykład o średnich opłatach za transakcje w bloku.



![api](assets/fr/17.webp)



Jesteś teraz gotowy, aby wykorzystać pełny potencjał Blockstream Explorer do odpytywania łańcuchów bloków w warstwach on-chain i Liquid. Mamy nadzieję, że ten samouczek był dla Ciebie pouczający i polecamy nasz samouczek na temat innego eksploratora Bitcoin:



https://planb.academy/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f