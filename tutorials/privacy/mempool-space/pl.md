---
name: Mempool
description: Poznaj cały ekosystem Bitcoin.
---

![cover](assets/cover.webp)



Protokół Bitcoin jest pseudonimową, zdecentralizowaną siecią otwartą na konsultacje. Członkowie (węzły), tj. komputery z instancją oprogramowania Bitcoin, mają nieograniczony dostęp do wszystkich danych opublikowanych w Bitcoin. Jednak we wczesnych latach Bitcoin protokół nie był tak szeroko dostępny jak obecnie.


We wczesnych dniach Bitcoin konieczne było uruchomienie węzła Bitcoin w celu uzyskania dostępu do odpowiednich narzędzi (bitcoin-cli) do przesłuchiwania sieci z linii poleceń.



https://planb.academy/tutorials/node/bitcoin/bitcoin-core-linux-568c13a6-8746-4d63-8e95-f4a61c5ae0ed

https://planb.academy/tutorials/node/bitcoin/bitcoin-knots-e04b2196-4df2-4246-86ef-c02269c29098

W związku z tym uruchomiono projekty mające na celu rozszerzenie społeczności Bitcoin, czyniąc ją bardziej dostępną dla każdego, kto nie jest właścicielem węzła i/lub nie posiada wymaganych umiejętności technicznych.



W tym samouczku przyjrzymy się projektowi **Mempool.space**, jego funkcjom i wpływowi, jaki wywarł na ekosystem Bitcoin.



## Czym jest Mempool.space?



**Mempool.space** to eksplorator typu open source, który dostarcza przydatnych informacji na temat transakcji, opłat transakcyjnych, bloków i górników w różnych sieciach protokołu Bitcoin. Uruchomiony w 2020 r., zapewnia znaczną poprawę komfortu użytkowania dzięki reprezentatywnej grafice, płynnym animacjom i przejrzystym interfejsom.



Aby zrozumieć projekt, Mempool (pula pamięci) to wirtualna przestrzeń, w której przechowywane są wszystkie transakcje oczekujące na potwierdzenie w sieci Bitcoin. Mempool jest jak "poczekalnia", w której transakcje Bitcoin czekają na potwierdzenie. Każdy komputer w sieci (węzeł) ma własną poczekalnię, co wyjaśnia, dlaczego nie wszystkie transakcje są widoczne dla wszystkich w tym samym czasie.



Główny wpływ platformy w ekosystemie Bitcoin polega na tym, że umożliwia ona dostęp do różnych informacji w obszarach pamięci większości węzłów obecnych na Bitcoin bez konieczności uruchamiania jednego z nich. Mempool.space to repozytorium do przeglądania i przeszukiwania sieci protokołów Bitcoin.



Coraz szersze zastosowanie w ekosystemie oraz fakt, że Mempool.space jest oprogramowaniem open source, umożliwiły jego integrację z coraz większą liczbą osobistych systemów hostingowych. Teraz możesz mieć własną instancję Mempool.space bezpośrednio na swoim osobistym węźle. Zobacz nasz samouczek dotyczący konfiguracji Mempool.space na węźle Umbrel poniżej.



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Podstawy Mempool.space



Jak wspomniano powyżej, [Mempool.space](https://Mempool.space) to eksplorator protokołu Bitcoin, który pozwala monitorować transakcje i ich propagację w wybranej sieci Bitcoin w czasie rzeczywistym, z poziomu graficznego Interface.



Mempool.space obsługuje wiele sieci protokołu Bitcoin.


Na pasku menu znajdują się następujące sieci:




- **Mainnet**: Główna sieć Bitcoin, w której odbywają się prawdziwe transakcje Bitcoin.
- **Signet**: Sieć testowa, która wykorzystuje podpisy cyfrowe do walidacji bloków bez konieczności korzystania z zasobów wymaganych przez sieć główną.
- **Testnet 3**: Wolna od ryzyka sieć testowa i rozwojowa na protokole Bitcoin.
- **Testnet 4**: Nowa wersja Testnet 3 zapewnia większą stabilność i nowe zasady konsensusu w środowisku testowym.



![reseaux](assets/fr/01.webp)



Na stronie głównej, po lewej stronie w Green, zobaczysz możliwe przyszłe bloki (grupy transakcji) gotowe do zatwierdzenia i zintegrowania (wydobycia) z siecią Bitcoin. Średnio blok jest wydobywany co dziesięć minut: zachowaj tę informację, ponieważ przyda się ona później w naszym rozwoju.


W kolorze fioletowym, po prawej stronie, znajdują się ostatnie bloki wydobyte na Bitcoin, przy czym numer ostatniego wydobytego bloku reprezentuje aktualną wysokość sieci.



![blocs](assets/fr/02.webp)



Sekcja **Opłaty transakcyjne** to estymator opłat transakcyjnych. Im wyższe opłaty przypisane do transakcji, tym większe prawdopodobieństwo, że transakcja zostanie dodana do następnego bloku gotowego do wydobycia.


Opłaty transakcyjne stanowią koszt, jaki Miner pobierze od użytkownika za wstawienie transakcji do bloku kandydującego dla Mining. Jest ona definiowana przez stosunek sat/vB (Satoshi/Virtual Bytes) reprezentujący liczbę satoshis, które płacisz za miejsce, które twoja transakcja zajmie w bloku kandydującym.



⚠️ WAŻNE: W przypadku nasycenia Mempool, górnicy priorytetowo traktują transakcje oferujące najlepszy stosunek Satoshi/vByte. Im cięższa (większa) transakcja, tym więcej satoshis będzie potrzebnych do jej szybkiego uwzględnienia.



![fees-visualizer](assets/fr/03.webp)



Sekcja **Mempool Goggles** umożliwia wizualizację przestrzeni zajmowanej przez transakcję.



![mempool](assets/fr/04.webp)



Blok jest wydobywany w przybliżeniu co dziesięć minut ze względu na trudność Proof of Work, którą górnicy muszą zapewnić, aby dodać swój kandydujący blok do łańcucha wydobytych bloków. Trudność ta zmienia się co **2016 bloków**, co odpowiada około **2 tygodniom**. Ewolucję tej trudności można zobaczyć tutaj.



![difficulty](assets/fr/05.webp)



Dodanie nowego bloku do głównego łańcucha uprawnia Miner zatwierdzonego bloku do nagrody składającej się ze stałej części (zmniejszanej o połowę co 210 000 bloków**, co odpowiada około 4 latom** podczas halvingów) i opłat transakcyjnych.



![halving](assets/fr/06.webp)



## Dostęp do szczegółów transakcji



W pasku wyszukiwania Mempool.space można wpisać Bitcoin Address lub transaction ID, aby dowiedzieć się więcej o swojej historii.



![search](assets/fr/07.webp)



Na stronie szczegółów transakcji znajdują się ogólne informacje na jej temat:




- **Status**: Potwierdzony w przypadku dodania do bloku, niepotwierdzony w przypadku oczekiwania w Mempool.
- **Opłaty transakcyjne**.
- **Szacowany czas przybycia (ETA)**: Przybliżony czas potrzebny na dodanie transakcji do bloku. Jest on obliczany zgodnie ze współczynnikiem stanowiącym opłaty związane z tą transakcją.



![general-txinfo](assets/fr/08.webp)



Sekcja **Flow** pokazuje wykres składników transakcji.



Wejścia (poprzednie UTXO), używane do transakcji, oraz wyjścia dające odbiorcom prawo do korzystania z bitcoinów z każdego wyjścia poprzez przedstawienie podpisu wymaganego do ich wydatkowania.



![flow](assets/fr/09.webp)



Więcej szczegółów na temat używanych adresów można znaleźć w sekcji **Wejścia i wyjścia**.



![address](assets/fr/10.webp)



Odkryj różne schematy transakcji Bitcoin, aby zwiększyć swoją poufność.



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Przyspiesz swoje transakcje



W ekosystemie Bitcoin aspekt walidacji transakcji przez górników jest nierozerwalnie związany z opłatami transakcyjnymi związanymi z tą transakcją. Górnicy priorytetowo traktują transakcje o wyższym współczynniku opłat (satoshis/vBytes), co może wpłynąć na ważność transakcji, jeśli nie zapłacisz rozsądnych opłat akceptowanych przez górników. Twoja transakcja utknęłaby w Mempool, czekając na blok, który akceptuje jej współczynnik opłat.



Na szczęście w sieci Bitcoin dostępne są dwie metody przyspieszające potwierdzenie transakcji.





- **RBF** - Zastąpienie przez opłatę: Metoda, która pozwala wydać te same wpisy, co transakcja z niską opłatą, ale tym razem poprzez zwiększenie opłaty transakcyjnej w celu przyspieszenia walidacji. Nowa transakcja zostanie szybciej zweryfikowana i uwzględniona w bloku, unieważniając transakcję z niską opłatą.



Akcję wymiany opłat można przeprowadzić z portfelami, które akceptują ten mechanizm. Na przykład, zobacz nasz artykuł na temat portfela Blue Wallet.



https://planb.academy/tutorials/wallet/mobile/blue-wallet-2f4093da-6d03-4f26-8378-b9351d0dbc90



- **CPFP** - Child pay for parent: Podejście inspirowane RBF, ale po stronie odbiorcy. Gdy transakcja, w której jesteś odbiorcą, zostanie zablokowana w Mempool, masz możliwość wydania wyników (UTXO) tej transakcji, mimo że nie została ona jeszcze potwierdzona, przydzielając więcej opłat do tej nowej transakcji, tak aby średnie opłaty - transakcji, w której jesteś odbiorcą i zainicjowanej transakcji - zachęcały górników do włączenia obu transakcji do bloku.



⚠️ Pierwsza transakcja musi być zawarta w bloku, aby umożliwić potwierdzenie drugiej transakcji.



Jeśli wszystkie te terminy wydają się zbyt techniczne, polecam [zapoznać się z naszym glosariuszem] (https://planb.academy/resources/glossary), który zawiera definicje wszystkich terminów technicznych związanych z Bitcoin i jego ekosystemem.



Oprócz tych metod, Mempool.space, dzięki swoim połączeniom z ponad 80% górników obecnych w sieci Bitcoin, pozwala również przyspieszyć dowolne **niepotwierdzone** transakcje, nawet te, które nie aktywują RBF, płacąc górnikom w Exchange za wstawienie taniej transakcji do następnego bloku gotowego do wydobycia.



Na stronie szczegółów transakcji kliknij przycisk **Accelerate**, a następnie przejdź do płatności kontrahenta na rzecz górników.



![accelerate-section](assets/fr/11.webp)


## Nieletni



Miner odnosi się do osoby, która zarządza kopalnią, tj. komputerem zaangażowanym w proces Mining, który polega na uczestnictwie w Proof-of-Work. Miner grupuje oczekujące transakcje w swoim Mempool, aby utworzyć blok kandydujący. Następnie szuka ważnego Hash, mniejszego lub równego celowi, dla nagłówka tego bloku, modyfikując różne nonces. Jeśli znajdzie ważny Hash, transmituje swój blok do sieci Bitcoin i zgarnia związaną z nim nagrodę pieniężną, na którą składa się dotacja blokowa (tworzenie nowych bitcoinów ex-nihilo) oraz opłata transakcyjna.



https://planb.academy/courses/ce272232-0d97-4482-884a-0f77a2ebc036

minerzy są jak "walidatorzy", którzy weryfikują i grupują transakcje w bloki. Aby dodać nowy blok do sieci Bitcoin, muszą rozwiązać złożoną zagadkę matematyczną (Proof-of-Work). Pierwszy Miner, który rozwiąże zagadkę, wygrywa nagrodę Bitcoin (dotacja do bloku + opłaty za transakcje zawarte w bloku).



Trudność tego Proof of Work jest monitorowana, co pozwala na wizualizację ewolucji mocy obliczeniowej wymaganej dla górników. W poniższych sekcjach można znaleźć :





- Oszacowanie całkowitych nagród uzyskanych przez górników podczas ostatniego dostosowania trudności, a także szacunki dotyczące następnego Halving dotacji blokowej, która ma miejsce co 210 000 bloków (około 04 lat).



![rewards](assets/fr/12.webp)



Trudność ta jest dostosowywana co 2016 bloków (około dwóch tygodni). Jest ona odwrotnie proporcjonalna do średniego czasu potrzebnego górnikom na Miner co 2016 bloków.


Gdy średni czas zajmowany przez górników jest krótszy niż 10 minut, trudność wzrasta, co dowodzi, że górnikom łatwiej było walidować bloki Miner. I odwrotnie, gdy średni czas jest dłuższy niż 10 minut, trudność spada.



![mining-pool](assets/fr/13.webp)





- Grupy górników: Biorąc pod uwagę trudność, grupa górników współpracuje, aby pomóc w znalezieniu Proof of Work na Bitcoin, w czymś, co nazywamy **poolem**. Gdy blok jest wydobywany przez grupę, uzyskana nagroda jest rozdzielana zgodnie z procentem sukcesu w częściowym poszukiwaniu rozwiązania dla każdego Miner, tj. wkładu w moc obliczeniową w poszukiwaniu Proof-of-Work, lub zgodnie z metodą wynagradzania uzgodnioną w ramach współpracy.





![mining](assets/fr/14.webp)



## Infrastruktura Lightning Network



Mempool nie tylko dostarcza informacji o infrastrukturze sieciowej Bitcoin (główny łańcuch). Integruje również narzędzia do wizualizacji i eksploracji nakładki Lightning Bitcoin.



W sekcji **Lightning** można wyświetlić wszystkie istniejące połączenia między węzłami Lightning.



![network-stats](assets/fr/15.webp)



Niniejszy Interface zawiera informacje na temat :





- Statystyki Lightning Network.



![distribution](assets/fr/16.webp)




⚠️ **WAŻNE**: Pojemność kanału płatności określa maksymalną kwotę, jaką węzeł może wysłać do innego węzła podczas transakcji Lightning.





- Węzły Lightning są przydzielane zgodnie z dostawcą usług internetowych (usługa hostingowa) i opcjonalnie zgodnie z przepustowością kanału płatności.



![distribution](assets/fr/17.webp)





- Historia ogólnej wydajności Lightning Network.


Znajdziesz tu również ranking tych węzłów według przepustowości ich kanałów płatności.



![ranking](assets/fr/18.webp)



## Więcej grafiki



Mempool.space to idealna platforma do interakcji z sieciami protokołu Bitcoin. Wykresy nie tylko dostarczają wizualnych danych, które pomagają zdecydować, kiedy dokonać transakcji, ale także precyzyjne parametry umożliwiające wizualizację w czasie rzeczywistym siły i kondycji sieci Bitcoin oraz powiązanej infrastruktury Lightning.



W sekcji **Grafika** można wyświetlić istotne dane dotyczące sieci Bitcoin:




- Ewolucja rozmiaru Mempool: Można obserwować, jak zmienia się rozmiar Mempool, co może wskazywać na okresy wysokiej lub niskiej aktywności w sieci.



![graphs](assets/fr/19.webp)






- Ewolucja transakcji i opłat transakcyjnych w wybranej sieci: Śledząc zmiany w transakcjach na sekundę, można przewidzieć okresy przeciążenia lub niskiej aktywności i zoptymalizować opłaty transakcyjne. Ten wykres daje perspektywę na zdolność sieci do obsługi wolumenu transakcji.



![graphs](assets/fr/20.webp)



Teraz, gdy dotarłeś do końca swojej podróży na Mempool.space, zostań swoim własnym odkrywcą i śledź swoje transakcje w czasie rzeczywistym. Poniżej znajduje się nasz artykuł na temat eksploratora Bitcoin **Public Pool**.



https://planb.academy/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1