---
name: Rykoszet
description: Zrozumienie i korzystanie z transakcji Ricochet
---
![cover ricochet](assets/cover.webp)


***OSTRZEŻENIE:** Po aresztowaniu założycieli Samourai Wallet i zajęciu ich serwerów 24 kwietnia, narzędzie Ricochet nie jest już dostępne. Możliwe jest jednak, że narzędzie to zostanie przywrócone w nadchodzących tygodniach. W międzyczasie rykoszet można wykonać tylko ręcznie. Teoretyczna część tego artykułu pozostaje istotna, aby zrozumieć jego działanie i dowiedzieć się, jak wykonać go ręcznie


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---

> Narzędzie premium, które dodaje dodatkową historię do transakcji. Pozwala ominąć czarne listy i chroni przed niesprawiedliwym zamknięciem konta przez osoby trzecie.

## Czym jest Ricochet?


Rykoszet to technika polegająca na przeprowadzaniu wielu fikcyjnych transakcji na swoją rzecz w celu symulacji transferu Bitcoin Ownership. Narzędzie to różni się od innych transakcji Samourai, ponieważ nie zapewnia anonimowości prospektywnej, ale raczej formę anonimowości retrospektywnej. Ricochet pomaga zatrzeć specyfikę, która mogłaby zagrozić zamienności monety Bitcoin.


Na przykład, jeśli wykonasz CoinJoin, twoje monety wyjściowe z miksu zostaną zidentyfikowane jako takie. Narzędzia do analizy łańcucha są w stanie wykryć wzorce transakcji CoinJoin i oznaczyć monety, które z nich wynikają. Rzeczywiście, CoinJoin ma na celu zerwanie historycznych powiązań monety, ale jej przejście przez coinjoiny pozostaje wykrywalne. Aby dokonać analogii, zjawisko to jest podobne do szyfrowania tekstu: nawet jeśli nie możemy uzyskać dostępu do oryginalnego tekstu jawnego, łatwo jest zidentyfikować, że zastosowano szyfrowanie.


Właśnie ta etykieta "monety wyjściowej CoinJoin" może wpływać na zamienność UTXO. Podmioty regulowane, takie jak platformy Exchange, mogą odmówić przyjęcia UTXO, która przeszła CoinJoin, a nawet zażądać wyjaśnień od jej właściciela, ryzykując zablokowanie konta lub zamrożenie środków. W niektórych przypadkach platforma może nawet zgłosić zachowanie użytkownika organom państwowym.


W tym miejscu do gry wkracza metoda Ricochet. Aby zatrzeć ślad pozostawiony przez CoinJoin, Ricochet wykonuje cztery kolejne transakcje, w których użytkownik przelewa swoje środki do siebie na różne adresy. Po tej sekwencji transakcji narzędzie Ricochet ostatecznie kieruje bitcoiny do miejsca docelowego, takiego jak platforma Exchange. Celem jest stworzenie dystansu między pierwotną transakcją CoinJoin a ostatecznym aktem wydatkowania. W ten sposób narzędzia do analizy łańcucha uznają, że po CoinJoin prawdopodobnie nastąpił transfer Ownership, a zatem nie jest konieczne podejmowanie działań przeciwko nadawcy.


![ricochet diagram](assets/en/1.webp)


W obliczu metody Ricochet można by sobie wyobrazić, że oprogramowanie do analizy łańcucha pogłębi swoje badanie poza cztery odbicia. Platformy te stoją jednak przed dylematem optymalizacji progu detekcji. Muszą one ustalić limit liczby przeskoków, po których przyznają, że prawdopodobnie nastąpiła zmiana właściwości i że połączenie z poprzednim CoinJoin powinno zostać zignorowane. Określenie tego progu jest jednak ryzykowne: każde wydłużenie obserwowanej liczby przeskoków wykładniczo zwiększa liczbę wyników fałszywie dodatnich, tj. osób błędnie oznaczonych jako uczestnicy CoinJoin, podczas gdy operacja została faktycznie wykonana przez kogoś innego. Scenariusz ten stanowi poważne ryzyko dla tych firm, ponieważ fałszywe alarmy prowadzą do niezadowolenia, które może prowadzić klientów do konkurencji. W dłuższej perspektywie zbyt ambitny próg prowadzi platformę do utraty większej liczby klientów niż jej konkurenci, co może zagrozić jej rentowności. W związku z tym skomplikowane jest dla tych platform zwiększenie liczby obserwowanych odrzuceń, a 4 jest często wystarczającą liczbą, aby przeciwdziałać ich analizom.


Dlatego **najczęstszy przypadek użycia Ricochet pojawia się, gdy konieczne jest ukrycie wcześniejszego udziału w CoinJoin na UTXO, który należy do ciebie**. Najlepiej jest unikać przesyłania bitcoinów, które przeszły CoinJoin do podmiotów regulowanych. Jednak w przypadku, gdy nie ma innej opcji, zwłaszcza w pilnej potrzebie upłynnienia bitcoinów w walucie fiducjarnej, Ricochet oferuje skuteczne rozwiązanie.


## Jak działa Ricochet na Samourai Wallet?

Ricochet to po prostu metoda wysyłania bitcoinów do samego siebie. Jest zatem całkowicie możliwe ręczne symulowanie rykoszetu bez użycia specjalistycznego narzędzia. Jednak dla tych, którzy chcą zautomatyzować ten proces, jednocześnie korzystając z bardziej dopracowanego wyniku, dobrym rozwiązaniem jest narzędzie Ricochet dostępne za pośrednictwem aplikacji Samourai Wallet.


Ponieważ usługa jest płatna w Samourai, Ricochet ponosi koszt `100,000 Sats` jako opłatę za usługę, oprócz opłat Mining. Dlatego jego użycie jest bardziej zalecane w przypadku przelewów na znaczne kwoty.


Aplikacja Samourai oferuje dwa warianty Ricochet:


- Wzmocniony rykoszet, czyli "dostawa rozłożona w czasie", oferuje korzyść w postaci rozłożenia opłat za usługę Samourai na pięć kolejnych transakcji. Ta opcja zapewnia również, że każda transakcja jest nadawana w innym czasie i rejestrowana w innym bloku, co ściśle naśladuje zachowanie zmiany Ownership. Metoda ta, choć wolniejsza, jest preferowana dla tych, którzy się nie spieszą, ponieważ maksymalizuje wydajność Ricochet poprzez zwiększenie jego odporności na analizę łańcucha.
- Klasyczny rykoszet, który ma na celu szybkie wykonanie operacji poprzez rozgłaszanie wszystkich transakcji w ograniczonym przedziale czasowym. Metoda ta oferuje zatem mniejszą prywatność i niższą odporność na analizę w porównaniu do metody wzmocnionej. Powinna być preferowana tylko w przypadku pilnych transferów.


## Jak wykonać rykoszet na Samourai Wallet?

Aby wykonać transakcję Ricochet z aplikacji Samourai Wallet, postępuj zgodnie z naszym samouczkiem wideo:

![Ricochet YouTube video tutorial](https://youtu.be/Gsz0zuVo3N4)


Jeśli chcesz zapoznać się z transakcjami Ricochet przeprowadzonymi w tym samouczku, oto one:


- Pierwsza transakcja Ricochet: [8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc](https://Mempool.space/fr/Testnet/tx/8deec9054dab10a35897b5efe0b3418e5012983888f8674835a9989a494921dc)
- Ostatnia transakcja Ricochet: [27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777](https://Mempool.space/fr/Testnet/tx/27980ce507630882f2a1ef94b941a0a3e086b80b10faf7bd168f3ebb4c3e4777)


**Zasoby zewnętrzne:**


- https://docs.samourai.io/en/Wallet/features/ricochet