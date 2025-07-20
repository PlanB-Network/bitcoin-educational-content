---
name: JoinBot
description: Zrozumienie i używanie JoinBot
---

![DALL·E – samurai robot in a red forest, 3D render](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, **usługa JoinBot nie jest już dostępna**. Od teraz nie jest już możliwe korzystanie z tego narzędzia. Jednak nadal można przeprowadzić Stonewall X2, ale trzeba znaleźć współpracownika i ręcznie Exchange PSBT. Usługa ta może zostać ponownie uruchomiona w nadchodzących miesiącach, w zależności od postępów w sprawie*


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

JoinBot to nowe narzędzie, które zostało dodane do pakietu Samourai Wallet wraz z najnowszą aktualizacją 0.99.98f słynnego oprogramowania Bitcoin Wallet. Umożliwia ono łatwe dokonywanie transakcji opartych na współpracy w celu optymalizacji prywatności, bez konieczności szukania partnera.


*Podziękowania dla wspaniałego Fanisa Michalakisa za pomysł wykorzystania DALL-E jako miniaturki!


## Czym jest transakcja współpracy na Bitcoin?


Bitcoin opiera się na rozproszonym i przejrzystym koncie Ledger. Każdy jest w stanie śledzić transakcje użytkowników tego elektronicznego systemu gotówkowego. Aby zapewnić pewien poziom prywatności, użytkownicy Bitcoin mogą dokonywać transakcji o określonej strukturze, aby dodać wiarygodności ich interpretacji.


Pomysł nie polega na bezpośrednim ukrywaniu informacji, ale na myleniu ich między innymi. Cel ten jest wykorzystywany w Coinjoins, transakcjach, które przerywają historię monety na Bitcoin i komplikują jej śledzenie. Aby osiągnąć ten rezultat, w transakcji należy utworzyć wiele wejść i wyjść o tej samej wartości.


Dane wejściowe to dane wejściowe transakcji Bitcoin, a dane wyjściowe reprezentują dane wyjściowe. Transakcja zużywa swoje dane wejściowe w celu utworzenia nowych danych wyjściowych poprzez zmianę warunków wydawania monety. Mechanizm ten umożliwia przenoszenie bitcoinów między użytkownikami.

Omawiam to szczegółowo w tym artykule: Mechanizm Transakcji Bitcoin: UTXO, Wejścia i Wyjścia.


Jednym ze sposobów na zatarcie śladów w transakcji Bitcoin jest zawarcie transakcji opartej na współpracy. Jak sama nazwa wskazuje, wiąże się ona z umową między wieloma użytkownikami, z których każdy wpłaca sumę bitcoinów jako dane wejściowe w tej samej transakcji i otrzymuje sumę jako dane wyjściowe.


Jak wspomniano wcześniej, najbardziej znaną strukturą transakcji opartej na współpracy jest CoinJoin. Na przykład w protokole CoinJoin Whirlpool transakcje obejmują 5 uczestników jako dane wejściowe i wyjściowe, z których każdy ma taką samą ilość bitcoinów.


![Diagram of a Coinjoin transaction on Whirlpool](assets/1.webp)


Zewnętrzny obserwator tej transakcji nie będzie w stanie stwierdzić, które wyjście należy do którego użytkownika jako dane wejściowe. Jeśli weźmiemy przykład użytkownika #4 (fioletowy), możemy rozpoznać jego wejście UTXO, ale nie będziemy wiedzieć, które z 5 wyjść jest faktycznie jego. Początkowe informacje nie są ukryte, ale raczej pomieszane w grupie.

Użytkownik jest w stanie zaprzeczyć posiadaniu określonego UTXO jako danych wyjściowych. Zjawisko to nazywane jest "wiarygodnym zaprzeczeniem" i pozwala na zachowanie poufności w przejrzystej transakcji Bitcoin.


Aby dowiedzieć się więcej o CoinJoin, wyjaśniam WSZYSTKO w tym długim artykule: Zrozumienie i używanie CoinJoin na Bitcoin.


Chociaż CoinJoin jest bardzo skuteczny w przerywaniu śledzenia UTXO, nie nadaje się do bezpośredniego wydatkowania. W istocie jego struktura oznacza konieczność korzystania z danych wejściowych o z góry określonej kwocie i danych wyjściowych o tej samej wartości (modulo opłaty Mining). Transakcja wydatków na Bitcoin jest jednak krytycznym momentem dla prywatności, ponieważ często tworzy fizyczne powiązanie między użytkownikiem a jego aktywnością na On-Chain. W związku z tym wydaje się niezbędne korzystanie z narzędzi do ochrony prywatności podczas dokonywania wydatków. Istnieją inne struktury transakcji opartych na współpracy, zaprojektowane specjalnie dla rzeczywistych transakcji płatniczych.


## Transakcja StonewallX2


Wśród niezliczonych narzędzi do wydawania pieniędzy oferowanych na Samourai Wallet, znajduje się transakcja współpracy StonewallX2. Jest to mini CoinJoin między dwoma użytkownikami przeznaczony do płatności. Z zewnątrz transakcja ta może prowadzić do kilku możliwych interpretacji. W ten sposób zapewnia wiarygodne zaprzeczenie, a co za tym idzie, poufność dla użytkownika.


Ta konfiguracja transakcji współpracy StonewallX2 jest dostępna w Samourai Wallet i Sparrow Wallet. Narzędzie to jest interoperacyjne między tymi dwoma programami.


Jego mechanizm jest dość prosty do zrozumienia. Oto jak to działa w praktyce:



- Użytkownik chce dokonać płatności w bitcoinach (na przykład u sprzedawcy).
- Pobierają one otrzymujący Address rzeczywistego odbiorcy płatności (sprzedawcy).
- Tworzą oni konkretną transakcję z wieloma danymi wejściowymi: co najmniej jednym należącym do nich i jednym należącym do zewnętrznego współpracownika.
- Transakcja będzie miała 4 wyjścia, w tym 2 o tej samej wartości: jedno do Address sprzedawcy w celu dokonania płatności, jedno jako zmiana, która wraca do użytkownika, jedno wyjście o tej samej wartości co płatność, które trafia do współpracownika, i kolejne wyjście, które również wraca do współpracownika.


Na przykład, oto typowa transakcja StonewallX2, w której dokonałem płatności w wysokości 50 125 Sats. Pierwszy wkład w wysokości 102 588 Sats pochodzi z mojego Samourai Wallet. Drugi wkład w wysokości 104 255 Sats pochodzi z Wallet mojego współpracownika:


![StonewallX2 transaction diagram](assets/2.webp)


Możemy zaobserwować 4 wyjścia, w tym 2 o tej samej wartości, aby zmylić ślady:



- `50,125 Sats`, które trafiają do faktycznego odbiorcy mojej płatności.
- `52,306 Sats`, które reprezentują moją zmianę, a tym samym powrót do Address w moim Wallet.
- `50,125 Sats`, które wracają do mojego współpracownika.
- `53,973 Sats` wraca do mojego współpracownika.


Pod koniec operacji współpracownik odzyska swoje początkowe saldo (pomniejszone o opłaty Mining), a użytkownik zapłaci sprzedawcy. Dodaje to znaczną ilość entropii do transakcji i przerywa niezaprzeczalne powiązania między nadawcą a odbiorcą płatności.


Siła transakcji StonewallX2 polega na tym, że całkowicie zaprzecza ona jednej z empirycznych zasad stosowanych przez analityków łańcucha: wspólnemu Ownership danych wejściowych w transakcji z wieloma danymi wejściowymi. Innymi słowy, w większości przypadków, jeśli obserwujemy transakcję Bitcoin z wieloma danymi wejściowymi, możemy założyć, że wszystkie te dane wejściowe należą do tej samej osoby. Satoshi Nakamoto zidentyfikował ten problem dla prywatności użytkowników już w swojej Białej Księdze:


> Jako dodatkowy firewall, dla każdej transakcji można użyć nowej pary kluczy, aby zapobiec powiązaniu ich ze wspólnym właścicielem. Powiązanie jest jednak nieuniknione w przypadku transakcji z wieloma danymi wejściowymi, które z konieczności ujawniają, że ich dane wejściowe należały do tego samego właściciela.

Jest to jedna z wielu empirycznych reguł stosowanych w analizie On-Chain do konstruowania klastrów Address. Aby dowiedzieć się więcej o tej heurystyce, polecam przeczytać serię czterech artykułów Samourai, które wspaniale wprowadzają w temat.


Siła transakcji StonewallX2 polega na tym, że zewnętrzny obserwator pomyśli, że różne dane wejściowe transakcji należą do wspólnego właściciela. W rzeczywistości są to dwaj różni użytkownicy współpracujący ze sobą. Analiza płatności jest zatem prowadzona do przynęty, a prywatność użytkownika jest zachowana.


Z zewnątrz transakcji StonewallX2 nie można odróżnić od transakcji Stonewall. Jedyną skuteczną różnicą między nimi jest to, że Stonewall nie współpracuje. Wykorzystuje tylko UTXO pojedynczego użytkownika. Jednak w swoich strukturach na koncie Ledger, Stonewall i StonewallX2 są całkowicie identyczne. Pozwala to na jeszcze więcej możliwych interpretacji tej struktury transakcji, ponieważ zewnętrzny obserwator nie będzie w stanie stwierdzić, czy dane wejściowe pochodzą od tej samej osoby, czy od dwóch współpracowników.


Co więcej, przewaga StonewallX2 nad PayJoin typu Stowaway polega na tym, że można go używać w każdej sytuacji. Rzeczywisty odbiorca płatności nie wnosi żadnych danych wejściowych do transakcji. Tak więc StonewallX2 może być używany do płacenia u dowolnego sprzedawcy akceptującego Bitcoin, nawet jeśli sprzedawca nie używa Samourai lub Sparrow.

Z drugiej strony, główną wadą tej struktury transakcji jest to, że wymaga ona współpracownika, który jest skłonny użyć swoich bitcoinów, aby uczestniczyć w płatności. Jeśli masz znajomych Bitcoin chętnych do pomocy w każdej sytuacji, nie stanowi to problemu. Jeśli jednak nie znasz żadnych innych użytkowników Samourai Wallet lub jeśli nikt nie jest dostępny do współpracy, utkniesz w martwym punkcie.


Aby rozwiązać ten problem, zespół Samourai niedawno dodał nową funkcję do swojej aplikacji: JoinBot.


## Czym jest JoinBot?


Zasada działania JoinBot jest prosta. Jeśli nie możesz znaleźć nikogo do współpracy przy transakcji StonewallX2, możesz współpracować z JoinBot. W praktyce będziesz przeprowadzać transakcje oparte na współpracy bezpośrednio z Samourai Wallet.


Usługa ta jest bardzo wygodna, zwłaszcza dla początkujących użytkowników, ponieważ jest dostępna 24 godziny na dobę, 7 dni w tygodniu. Jeśli musisz dokonać pilnej płatności i chcesz wykonać StonewallX2, nie musisz już kontaktować się ze znajomym ani szukać współpracownika online. JoinBot ci pomoże.


Kolejną zaletą JoinBot jest to, że UTXO, które dostarcza jako dane wejściowe, pochodzą wyłącznie z postmix Whirlpool, co zwiększa prywatność płatności. Ponadto, ponieważ JoinBot jest zawsze online, powinieneś współpracować z UTXO, które mają duże potencjalne Anonsety.


Oczywiście JoinBot ma pewne kompromisy, na które należy zwrócić uwagę:



- Podobnie jak w przypadku klasycznego StonewallX2, twój współpracownik musi być świadomy użytych UTXO i ich przeznaczenia. W przypadku JoinBot, Samourai zna szczegóły tej transakcji. Niekoniecznie jest to złe, ale należy o tym pamiętać.
- Aby uniknąć spamu, Samourai pobiera opłatę serwisową w wysokości 3,5% od kwoty rzeczywistej transakcji, z maksymalnym limitem 0,01 BTC. Na przykład, jeśli wyślę rzeczywistą płatność w wysokości 100 kilosatów za pomocą JoinBot, kwota opłaty za usługę wyniesie 3500 Sats.
- Aby korzystać z JoinBot, musisz mieć co najmniej dwa niepowiązane i dostępne UTXO w Wallet.
- W klasycznym StonewallX2 opłaty Mining są dzielone równo między dwóch współpracowników. W przypadku JoinBot będziesz oczywiście musiał uiścić pełną opłatę za Mining.
- Aby transakcja JoinBot była dokładnie taka sama jak klasyczna transakcja StonewallX2 lub Stonewall, opłata za usługę jest dokonywana w ramach całkowicie oddzielnej transakcji. Zwrot połowy opłat Mining początkowo zapłaconych przez Samourai zostanie dokonany podczas tej drugiej transakcji. Aby do końca zoptymalizować prywatność użytkownika, rozliczenie opłat odbywa się za pomocą transakcji strukturalnej Stowaway (PayJoin).


## Jak korzystać z JoinBot?


Aby wykonać transakcję JoinBot, musisz mieć Samourai Wallet. Można go pobrać tutaj lub z Google Playstore.


W przeciwieństwie do większości narzędzi opracowanych przez Samourai, Sparrow Wallet nie ogłosił jeszcze wdrożenia JoinBot. Narzędzie to jest zatem dostępne tylko na Samourai.


Dowiedz się krok po kroku, jak wykonać transakcję StonewallX2 za pomocą JoinBot w tym filmie:


![How to use Joinbot](https://youtu.be/80MoMz2Ne5g)


Oto schemat transakcji, który właśnie wykonaliśmy w filmie:


![Diagram of my StonewallX2 transaction with JoinBot.](assets/3.webp)


Widzimy 5 wejść:



- 3 wejścia po 100 kilosatów pochodzące od Samourai (JoinBot).
- 2 wejścia pochodzące z mojego osobistego Wallet, 3,524 Sats i 1.8 megasata.


4 wyjścia transakcji są następujące:



- 1 z 212 452 Sats do faktycznego odbiorcy mojej płatności.
- Kolejna taka sama kwota, która pochodzi z Samourai Address.
- 1, która również wraca do Samourai za 87 302 Sats. Stanowi to różnicę między sumą ich danych wejściowych (300 000 Sats) a wynikiem zaciemniania (212 452 Sats) minus opłaty Mining.
- 1 zmiana, która wraca do innego Address w moim Wallet. Stanowi ona różnicę między sumą moich danych wejściowych a rzeczywistą płatnością pomniejszoną o opłaty Mining.


Przypominamy, że opłaty Mining nie reprezentują wyników transakcji. Stanowią one po prostu różnicę między całkowitymi nakładami a całkowitymi wynikami.


## Wnioski


JoinBot to dodatkowe narzędzie, które zwiększa możliwości wyboru i swobodę użytkowników Samourai. Pozwala ono na wspólną transakcję StonewallX2 bezpośrednio z Samourai jako współpracownikiem. Ten rodzaj transakcji pomaga zwiększyć prywatność użytkowników.


Jeśli możesz wykonać klasyczne StonewallX2 z przyjacielem, nadal polecam korzystanie z tego narzędzia. Jeśli jednak utknąłeś i nie możesz znaleźć współpracowników do dokonania płatności, wiesz, że JoinBot będzie dostępny 24 godziny na dobę, 7 dni w tygodniu, aby z tobą współpracować.


**Zasoby zewnętrzne:**


- https://medium.com/oxt-research/understanding-Bitcoin-privacy-with-oxt-part-1-4-8177a40a5923
- https://www.pandul.fr/post/comprendre-et-utiliser-le-CoinJoin-sur-Bitcoin