---
name: 1ML
description: Dowiedz się, jak korzystać z eksploratora 1ML, aby zrozumieć i przeanalizować sieć Lightning Bitcoin.
---
![cover](assets/cover.webp)



## Wprowadzenie



Lightning Network to szybkie, tanie rozwiązanie płatnicze zbudowane na Bitcoin, umożliwiające natychmiastowe, bezpieczne transakcje. Obserwacja tej sieci jest niezbędna do zrozumienia jej działania, topologii i stanu węzłów, które ją tworzą. Eksplorator Lightning, taki jak 1ML, służy do wizualizacji publicznych danych sieci, w tym aktywnych węzłów, otwartych kanałów i dostępnej przepustowości, zapewniając cenny przegląd dla użytkowników, programistów i operatorów węzłów.



## Dostęp do 1ML i zrozumienie strony głównej



Aby uzyskać dostęp do 1ML, wystarczy otworzyć przeglądarkę internetową i wpisać [https://1ml.com](https://1ml.com). Spowoduje to przejście do strony głównej, która służy jako globalny pulpit nawigacyjny Lightning Network.



![capture](assets/fr/03.webp)



Ta strona wyświetla kilka ważnych statystyk w górnej części ekranu, w tym :





- Całkowita liczba aktywnych węzłów** w sieci, tj. komputerów zaangażowanych w wysyłanie i odbieranie płatności Lightning.
- Liczba otwartych kanałów**, które odpowiadają połączeniom między tymi węzłami umożliwiającymi transfery środków.
- **Całkowita pojemność sieci**, wyrażona w bitcoinach (BTC), która wskazuje sumę pojemności wszystkich kanałów publicznych.



Dane te są regularnie aktualizowane, aby odzwierciedlić aktualny stan sieci. Dają one wyobrażenie o jej rozmiarze, wzroście i solidności.



![capture](assets/fr/04.webp)



Tuż poniżej strona oferuje listy z rankingami:





- **Najbardziej połączone węzły**, które mają najwięcej otwartych kanałów do innych węzłów.
- **Najwyższa wydajność** węzłów, wskazująca, które węzły mogą przesyłać największe ilości danych.
- Najważniejsze kanały pod względem przepustowości.



Filtry mogą być również używane do zawężania tych list według lokalizacji geograficznej lub innych kryteriów.



Ta strona jest idealnym punktem wyjścia do poznania Lightning Network i zrozumienia jego ogólnej topologii.



![capture](assets/fr/05.webp)



![capture](assets/fr/06.webp)



## Eksplorowanie węzłów Lightning



Aby zbadać węzeł w 1ML, zacznij od użycia paska wyszukiwania u góry strony. Możesz wprowadzić **Node ID**, czyli unikalny identyfikator węzła, lub jego **alias**, który jest łatwiejszą do zapamiętania nazwą.



Po zakończeniu wyszukiwania kliknij odpowiedni węzeł, aby uzyskać dostęp do jego szczegółowej strony.



![capture](assets/fr/07.webp)



Na tej stronie wyświetlanych jest kilka ważnych informacji:





- Identyfikator węzła**: ten unikalny identyfikator to długi ciąg znaków, który umożliwia precyzyjną identyfikację węzła w całej sieci.



![capture](assets/fr/08.webp)





- Alias**: jest to nazwa wybrana przez właściciela węzła, aby reprezentować go publicznie.



![capture](assets/fr/09.webp)





- Liczba kanałów** wskazuje, ile połączeń węzeł ma otwartych z innymi węzłami, podczas gdy **całkowita pojemność** reprezentuje sumę bitcoinów dostępnych w tych kanałach. Węzeł z dużą liczbą kanałów i wysoką przepustowością jest ogólnie dobrze połączony i zdolny do szybkiego przesyłania dużych ilości pieniędzy w sieci.



![capture](assets/fr/10.webp)





- **uptime**, czyli dostępność, mierzy jak długo węzeł pozostawał aktywny i dostępny online, odzwierciedlając jego niezawodność. Z drugiej strony **wiek** węzła wskazuje, jak długo jest on obecny w sieci, odzwierciedlając jego stabilność i doświadczenie w Lightning Network.



![capture](assets/fr/11.webp)



Dane te pomagają zrozumieć znaczenie i niezawodność węzła w Lightning Network. Na przykład węzeł z dużą liczbą kanałów, wysoką przepustowością i wysokim czasem sprawności jest często głównym graczem w sieci.



## Eksploracja kanałów oświetleniowych



### Czym jest kanał Lightning?



Kanał Lightning to bezpośrednie połączenie między dwoma węzłami sieci. Umożliwia on tym dwóm węzłom wymianę natychmiastowych, tanich płatności bez przechodzenia przez główny łańcuch Bitcoin dla każdej transakcji. Kanały są podstawą, która sprawia, że Lightning Network jest szybki i skalowalny.



### Przeczytaj informacje o kanale na 1ML



W 1ML każdy kanał ma własną stronę lub arkusz opisu zawierający szereg ważnych danych:



Ze strony węzła można uzyskać dostęp do listy jego kanałów. Klikając na kanał, 1ML wyświetla dedykowaną stronę z kilkoma kluczowymi informacjami.



![capture](assets/fr/12.webp)



![capture](assets/fr/13.webp)



Główne widoczne dane są następujące:





- Węzły partnerskie**: każdy kanał łączy dwa węzły. 1ML wyświetla oba identyfikatory i ich odpowiednie aliasy.



![capture](assets/fr/14.webp)





- Pojemność kanału**: jest to całkowita ilość bitcoinów zablokowanych w tym kanale. Pojemność ta reprezentuje maksymalny limit płatności, które mogą przejść przez ten kanał.



![capture](assets/fr/15.webp)





- Wiek kanału**: wskazuje, jak długo kanał był otwarty. Stary kanał jest często oznaką stabilnej relacji między dwoma węzłami.



![capture](assets/fr/16.webp)



### Ograniczenia widoczności kanału



Ważne jest, aby zrozumieć, że 1ML pokazuje tylko **część** Lightning Network. Eksplorator pokazuje tylko **kanały publiczne**, tj. te, które zostały ogłoszone w sieci. Kanały prywatne, często używane ze względu na poufność lub strategię, nie są widoczne. Ponadto 1ML nie pokazuje dokładnej dystrybucji środków po każdej stronie kanału, ani dokonanych płatności, ani płynności faktycznie dostępnej w danym momencie. Wyświetlane informacje mogą być zatem wykorzystane do analizy **ogólnej struktury sieci**, ale nie jej rzeczywistej działalności finansowej lub szczegółowego stanu płynności.



## Przeglądaj Lightning Network według lokalizacji



### Węzły według kraju i regionu



1ML umożliwia eksplorację Lightning Network według **podziału geograficznego**. Ze strony głównej lub za pośrednictwem dedykowanych sekcji można wyświetlać węzły według kraju lub regionu. Funkcja ta opiera się na informacjach o lokalizacji zadeklarowanych przez operatorów węzłów.


Na pasku nawigacyjnym zobaczysz link **Lokalizacja**. Na stronie węzły są pogrupowane według kontynentu, kraju i miasta.



![capture](assets/fr/17.webp)



Wybierając kraj, 1ML wyświetla listę powiązanych węzłów wraz z zagregowanymi statystykami, takimi jak liczba węzłów i całkowita widoczna przepustowość dla tego obszaru geograficznego.



#### Co to mówi o lokalnej adopcji





- Przyjęcie technologii**: Duża liczba węzłów w regionie wskazuje, że użytkownicy Bitcoin, firmy lub usługi aktywnie przyjmują Lightning Network. Świadczy to o dojrzałości technologicznej i chęci skorzystania z zalet Lightning (szybkie transakcje, niższe koszty).
- Ekosystem gospodarczy** : Gęsta obecność węzłów może również sygnalizować lokalną strukturę gospodarczą wokół Bitcoin: kupcy akceptujący Lightning, startupy opracowujące narzędzia, wydarzenia społecznościowe itp.
- Bezpieczeństwo i odporność**: Zróżnicowana dystrybucja geograficzna zwiększa odporność sieci w obliczu lokalnych awarii lub ograniczeń. Im bardziej rozproszone węzły, tym bardziej zdecentralizowana i trudniejsza do ocenzurowania sieć.
- Polityka i regulacje**: Niektóre kraje mogą odnotować szybszą adopcję dzięki korzystnym ramom regulacyjnym lub proaktywnej społeczności. I odwrotnie, w obszarach, w których przepisy są surowe lub wrogie, liczba węzłów będzie niższa.



#### Ograniczenia danych geograficznych



Należy jednak pamiętać, że geolokalizacja węzłów Lightning ma swoje ograniczenia i błędy:





- Przybliżona lokalizacja IP**: 1ML zazwyczaj wykorzystuje publiczny adres IP węzłów do oszacowania ich lokalizacji. Metoda ta może być jednak zniekształcona przez korzystanie z VPN, serwerów w chmurze (AWS, Google Cloud) lub hostingu w krajach innych niż rzeczywiste miejsce zamieszkania właściciela węzła.
- Węzły wirtualne**: Niektórzy operatorzy hostują swoje węzły na zdalnych serwerach ze względu na niezawodność i dostępność, co może dawać fałszywe poczucie fizycznej lokalizacji.
- Mobilność użytkownika**: Operator węzła może zmienić lokalizację, przenieść swoją infrastrukturę lub otworzyć kilka węzłów w różnych regionach, co czyni odczyt danych bardziej złożonym.
- Niewidoczność węzłów prywatnych**: Niektóre węzły nie publikują swojego adresu IP lub używają metod ukrywania swojej lokalizacji, uniemożliwiając geolokalizację.



## konkretne przypadki użycia 1ML



### Zrozumienie topologii sieci



1ML umożliwia wizualizację **ogólnej struktury Lightning Network**. Obserwując połączenia między węzłami, liczbę kanałów i ogólną przepustowość, można zrozumieć, jak zorganizowana jest sieć, które węzły odgrywają centralną rolę i jak teoretycznie mogą krążyć przepływy płatności.



To zrozumienie jest niezbędne, jeśli chcemy zrozumieć, jak działa Lightning Network, a nie tylko do użytku portfelowego.



### Identyfikacja ważnych węzłów



Dzięki rankingom oferowanym przez 1ML (najwięcej połączonych węzłów, największa przepustowość, wiek) możliwe jest zidentyfikowanie węzłów, które zajmują ważne miejsce w sieci. Węzły te często służą jako główne bramki dla płatności Lightning.



![capture](assets/fr/18.webp)



### Sprawdź publiczną widoczność węzła



Dla operatora węzła, 1ML pozwala sprawdzić, czy węzeł jest **publicznie reklamowany** na Lightning Network. Jeśli węzeł pojawia się na 1ML, oznacza to, że jest widoczny i dostępny dla innych węzłów w celu otwarcia kanałów publicznych.


Może to być przydatne do diagnozowania problemów z widocznością lub łącznością.



### Obserwowanie ewolucji Lightning Network w czasie



Porównując globalne statystyki w różnych okresach, 1ML pozwala nam obserwować ewolucję Lightning Network: wzrost lub spadek liczby węzłów, wahania całkowitej przepustowości lub zmiany w rozkładzie geograficznym.


Obserwacje te oferują interesującą perspektywę wzrostu, dojrzałości i trendów Lightning Network.



## najlepsze praktyki i ograniczenia 1ML



### Dane publiczne ≠ pełna rzeczywistość



1ML opiera się wyłącznie na **ogłoszonych publicznie** danych dotyczących Lightning Network. Oznacza to, że narzędzie pokazuje tylko część rzeczywistości. Wiele kanałów może być prywatnych, niektóre węzły mogą nie być reklamowane, a rzeczywista płynność dostępna w kanałach nie jest widoczna. Dlatego ważne jest, aby używać 1ML jako globalnego narzędzia analitycznego, a nie jako wyczerpującej reprezentacji sieci.



### Prywatność i błyskawice



Lightning Network został zaprojektowany z silnym naciskiem na **prywatność płatności**. Poszczególne transakcje nie są widoczne na 1ML, a dokładne salda kanałów nie są publiczne. To ograniczenie nie jest winą eksploratora, ale podstawową cechą Lightning Network, zaprojektowaną w celu ochrony prywatności użytkowników.



### Nie wyciągaj pochopnych wniosków



Węzeł o dużej przepustowości lub wielu kanałach niekoniecznie jest bardziej "niezawodny" lub "wydajny" we wszystkich przypadkach. Podobnie, tymczasowy spadek ogólnej przepustowości sieci niekoniecznie oznacza problem strukturalny. Dane liczbowe powinny być zawsze interpretowane z perspektywy czasu i umieszczane w kontekście.



### Komplementarność z innymi narzędziami



1ML jest doskonałym punktem wyjścia do eksploracji Lightning Network, ale najlepiej używać go w połączeniu z innymi narzędziami, takimi jak portfele Lightning, interfejsy zarządzania węzłami i inne eksploratory. Takie podejście zapewnia bardziej kompletny i zniuansowany widok sieci.



## opcja połączenia 1ML (zaawansowana funkcjonalność)



1ML oferuje opcję **zalogowania / utworzenia konta**, widoczną na stronie, ale nie jest to **konieczne** do przeglądania danych Lightning Network. Wszystkie funkcje omówione do tej pory w tym samouczku są dostępne **bez konta**.



Połączenie jest przeznaczone przede wszystkim dla **operatorów węzłów Lightning**. W szczególności umożliwia powiązanie węzła z kontem 1ML w celu zarządzania niektórymi informacjami publicznymi, takimi jak prezentacja węzła, linki kontaktowe i inne metadane. Ta funkcja ma na celu poprawę widoczności i identyfikacji węzła w eksploratorze.



Należy pamiętać, że 1ML nie jest **usługą powierniczą**. Utworzenie konta nie daje dostępu do funduszy, kanałów lub płatności węzła. Służy jedynie do interakcji z eksploratorem z deklaratywnego i informacyjnego punktu widzenia.



W kontekście nauki lub odkrywania Lightning Network, opcja ta może być zatem uważana za **opcjonalną** i zarezerwowaną dla bardziej zaawansowanych zastosowań.



## Wnioski



1ML jest cennym narzędziem do obserwacji i zrozumienia Lightning Network na podstawie jego publicznych danych. Pozwala badać strukturę sieci, analizować węzły i kanały oraz śledzić ogólną ewolucję adopcji Lightning Network w czasie. Bez konieczności posiadania konta lub obsługi funduszy, 1ML oferuje dostępną bramę dla każdego, kto chce pogłębić swoje zrozumienie działania Lightning.


Jeśli chcesz pójść dalej z Lightning Network, polecam kompletny kurs Wprowadzenie do Lightning Network:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb