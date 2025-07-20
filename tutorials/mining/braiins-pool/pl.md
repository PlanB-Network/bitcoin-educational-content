---
name: Basen Braiins

description: Wprowadzenie do Braiins Pool
---

![signup](assets/cover.webp)


Braiins Pool, wcześniej znany jako Slush Pool, jest pierwszym Bitcoin Mining pool. Założona w listopadzie 2010 roku, swój pierwszy blok wydobyła 16 grudnia 2010 roku, blok 97834.


Od maja 2024 r. Braiins Pool ma moc obliczeniową 13 EH/s, co stanowi około 1,8% całkowitego Bitcoin Hashrate. Wydobyto łącznie 1 307 188 bitcoinów, co stanowi około 6% z maksymalnej liczby 21 milionów bitcoinów, które kiedykolwiek będą istnieć.


### System wynagrodzeń


Od końca 2023 r. Braiins Pool zmienił swój system wynagrodzeń, przyjmując system FPPS (Full Pay Per Share). Oznacza to, że górnicy otrzymują nagrody każdego dnia za całą swoją pracę z poprzedniego dnia, nawet jeśli pula nie znalazła bloku. Różni się to od starego systemu, w którym górnicy otrzymywali nagrodę tylko wtedy, gdy pula znalazła blok.


**Warto zauważyć, [zgodnie z tweetem Mononauta](https://x.com/mononautical/status/1777686545715089605), który analizuje Bitcoin TimeChain, że wiele pul Mining korzystających z systemu FPPS wysyłałoby wydobyte bitcoiny do Address AntPool, co oznaczałoby, że AntPool kontroluje Hashrate wszystkich tych pul, około 47% globalnego Bitcoin Hashrate. To bardzo zła wiadomość dla decentralizacji sieci**


### Opłaty za korzystanie z basenu


Opłaty za Braiins Pool wynoszą 2,5%, jednak jeśli korzystasz z BraiinsOS na swoich maszynach, opłaty będą wynosić 0%


### Wypłaty


**Błyskawiczne wypłaty**

Błyskawiczne wypłaty umożliwiają wypłatę nagród bez minimalnej kwoty raz dziennie za pośrednictwem Lightning Address.

Aby korzystać z tej metody, musisz mieć Wallet kompatybilny z adresami Lightning.


**On-Chain Wypłaty**

Wypłaty z On-Chain są ograniczone do minimalnej kwoty i mogą podlegać opłatom.

Minimalna kwota: 20 000 Sats

Opłaty: 10.000 Sats dla kwot mniejszych niż 500.000 Sats

Bezpłatnie dla kwot powyżej 500 000 Sats

Wypłaty mogą być uruchamiane według przedziału czasowego lub kwoty.


## Tworzenie konta


Aby rozpocząć korzystanie z Braiins Pool [przejdź do ich strony internetowej] (https://braiins.com/pool) i kliknij "SIGN UP" w prawym górnym rogu



![signup](assets/3.webp)


Wprowadź swoje dane i zatwierdź je, a następnie otrzymasz wiadomość e-mail z prośbą o potwierdzenie Address. Potwierdź za pomocą linku w otrzymanej wiadomości e-mail, a następnie zaloguj się na platformie


![signup](assets/4.webp)



## Dodawanie "pracownika"

Pracownik to Miner, który zostanie podłączony do puli. Aby dodać nowy Miner, kliknij "Workers" w menu na lewym pasku bocznym.

![signup](assets/7.webp)


Następnie kliknij fioletowy przycisk "Połącz pracowników +".


W tym oknie wybierz swój obszar geograficzny.


Jeśli Miner, z którym chcesz się połączyć, korzysta z systemu BraiinsOS, wybierz protokół "Stratum V2". W przeciwnym razie wybierz "Stratum V1".


![signup](assets/8.webp)


Informacje do wprowadzenia znajdują się na stronie internetowej Miner (patrz dokumentacja Miner, aby dowiedzieć się, gdzie wprowadzić te informacje).


Tutaj, **"stratum+tcp://eu.stratum.braiins.com:3333"** jest adresem URL puli.


**JimZap.workerName** to twój identyfikator i nazwa twojego Miner, gdzie JimZap to identyfikator, a .workerName to nazwa Miner. Jeśli masz wielu górników, możesz nadać im tę samą nazwę, w którym to przypadku ich moc obliczeniowa zostanie zsumowana na pulpicie nawigacyjnym, lub nadać im różne nazwy, aby monitorować je indywidualnie.


A hasło jest zawsze takie samo **"anything123"**


Po wprowadzeniu tych informacji na stronie internetowej Miner i uruchomieniu Mining, po kilku minutach pojawią się one na pulpicie nawigacyjnym Braiins Pool.


## Przegląd pulpitu nawigacyjnego


![signup](assets/9.webp)


W górnym banerze można zobaczyć średni łączny Hashrate wszystkich górników w ciągu 5 minut, 1 godziny i 24 godzin. A także podsumowanie liczby górników online lub offline.

Poniżej znajduje się wykres umożliwiający śledzenie ewolucji mocy obliczeniowej.


![signup](assets/10.webp)


Poniżej tego wykresu znajduje się kilka informacji o nagrodach w Sats.


**"Dzisiejsze nagrody Mining"** Wskazuje liczbę wydobytych dziś Sats. Pod koniec dnia wartość ta zostanie zresetowana do 0, a Sats zostaną wysłane na konto użytkownika.


**"Wczorajsza całkowita nagroda "** Liczba Sats wydobytych poprzedniego dnia


**"Est. Rentowność (1 TH/s) "** Jest to szacunkowa liczba Sats zarobionych w ciągu jednego dnia przy mocy obliczeniowej 1 TH/s. Na przykład, jeśli wartość wynosi 77 Sats, a moc obliczeniowa wynosi 10 TH/s nieprzerwanie przez cały dzień, to teoretycznie można zarobić 77 x 10 = 770 Sats dziennie.


**"Nagroda wszech czasów "** Łączna liczba Sats wydobytych w puli Braiins


**"System nagród "** Stawka opłaty stosowana przez pulę


**"Next Payout ETA "** Szacunkowy czas, jaki upłynie, zanim będzie można wypłacić Sats z platformy. Tutaj szacunek nie pokazuje nic, ponieważ Mining jest w toku dopiero od kilku minut.


**"Saldo konta "** Liczba Sats dostępnych na koncie, które można następnie wypłacić.

## Konfigurowanie wypłat

Nagrody można wypłacić za pomocą On-Chain lub za pomocą Address.


Na górze kliknij "Fundusze". Domyślnie masz "Konto Bitcoin". Możesz utworzyć inne, aby dzielić się nagrodami. Wrócimy do tego w następnej sekcji.


Na razie kliknij "Konfiguracja".


![signup](assets/17.webp)


W nowym oknie możesz wybrać opcję "Wypłata Onchain".


Nazwij ten Wallet, podaj BTC Address i wybierz żądany typ wyzwalacza. "Próg" oznacza, że płatność zostanie uruchomiona po zgromadzeniu określonej kwoty BTC, a w przypadku "Interwału czasowego" płatność będzie uruchamiana w regularnych odstępach czasu (dni/tygodnie/miesiące).


Należy pamiętać, że minimalna kwota wynosi 0,0002 BTC, a poniżej 0,005 BTC zostanie naliczona opłata w wysokości 0,0001 BTC.


![signup](assets/18.webp)


Jeśli chcesz korzystać z wypłat Lightning, będziesz potrzebować Wallet, który zapewnia Lightning Address. Na przykład można użyć getAlby.


Kliknij w górnej części okna na "Błyskawiczna wypłata".


Wprowadź swój Lightning Address i zaznacz pole "Rozumiem...", a następnie zatwierdź.


Dzięki tej metodzie wypłaty nagrody będą wysyłane do Wallet każdego dnia.


![signup](assets/14.webp)


Po zatwierdzeniu ustawień wypłaty otrzymasz wiadomość e-mail z potwierdzeniem.


![signup](assets/15.webp)


## Dzielenie się nagrodami


Braiins Pool umożliwia również dzielenie się nagrodami w wielu portfelach.


Aby to zrobić, kliknij u góry na "Mining", a następnie po lewej stronie na "Ustawienia".


![signup](assets/19.webp)


Na tej stronie będziesz mógł dodać inne "Konto finansowe", klikając "Dodaj inne konto finansowe" i rozdzielić swoje nagrody w % na te różne konta, z którymi musisz powiązać Wallet. Aby powiązać nowy Wallet z kontem finansowym, zapoznaj się z poprzednią sekcją.