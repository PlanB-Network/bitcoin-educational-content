---
name: PayJoin
description: Co to jest PayJoin na Bitcoin?
---
![Payjoin thumbnail - steganography](assets/cover.webp)


***UWAGA:** Po aresztowaniu założycieli Samourai Wallet i przejęciu ich serwerów 24 kwietnia, Payjoins Stowaway na Samourai Wallet działa tylko poprzez ręczną wymianę PSBT między zainteresowanymi stronami, pod warunkiem, że obaj użytkownicy są połączeni z własnym Dojo. Jeśli chodzi o Sparrow, Payjoiny przez BIP78 nadal działają. Możliwe jednak, że narzędzia te zostaną ponownie uruchomione w nadchodzących tygodniach. W międzyczasie nadal możesz przeczytać ten artykuł, aby zrozumieć teoretyczne działanie payjoins.*


uważnie śledzimy rozwój tej sprawy, a także rozwój związany z powiązanymi narzędziami. Zapewniamy, że będziemy aktualizować ten poradnik w miarę pojawiania się nowych informacji


ten samouczek służy wyłącznie celom edukacyjnym i informacyjnym. Nie popieramy ani nie zachęcamy do korzystania z tych narzędzi w celach przestępczych. Każdy użytkownik jest odpowiedzialny za przestrzeganie prawa obowiązującego w jego jurysdykcji


---
## Zrozumienie transakcji PayJoin na Bitcoin


PayJoin to specyficzna struktura transakcji Bitcoin, która zwiększa prywatność użytkownika podczas płatności poprzez współpracę z odbiorcą płatności.


W 2015 r. [LaurentMT](https://twitter.com/LaurentMT) po raz pierwszy wspomniał o tej metodzie jako o "transakcjach steganograficznych" w dokumencie dostępnym [tutaj](https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt). Technika ta została później przyjęta przez Samourai Wallet, który stał się pierwszym klientem, który wdrożył ją za pomocą narzędzia Stowaway w 2018 roku. Koncepcja PayJoin znajduje się również w [BIP79](https://github.com/Bitcoin/bips/blob/master/bip-0079.mediawiki) i [BIP78](https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki). W odniesieniu do PayJoin stosuje się kilka terminów:


- PayJoin
- Pasażer na gapę
- P2EP (Pay-to-End-Point)
- Transakcja steganograficzna


Wyjątkowość PayJoin polega na jego zdolności do generate transakcji, która na pierwszy rzut oka wydaje się zwyczajna, ale w rzeczywistości jest mini CoinJoin między dwiema stronami. Aby to osiągnąć, struktura transakcji obejmuje odbiorcę płatności obok faktycznego nadawcy w danych wejściowych. Odbiorca zawiera płatność dla siebie w środku transakcji, co pozwala mu na otrzymanie zapłaty.


Weźmy konkretny przykład: jeśli kupisz bagietkę za `4000 Sats` przy użyciu UTXO w wysokości `10 000 Sats` i zdecydujesz się na PayJoin, twój piekarz doda UTXO w wysokości `15 000 Sats`, który należy do niego jako wkład, który otrzyma w całości jako wynik, oprócz twoich `4000 Sats`:

![Payjoin transaction diagram](assets/en/1.webp)


W tym przykładzie piekarz wprowadza `15 000 Sats` jako wkład i wychodzi z `19 000 Sats`, z różnicą dokładnie `4000 Sats`, która jest ceną bagietki. Po twojej stronie, wchodzisz z `10,000 Sats` i kończysz z `6,000 Sats` jako wyjściem, reprezentując równowagę `-4000 Sats`, która jest ceną bagietki. Aby uprościć przykład, celowo pominąłem opłaty Mining w tej transakcji.


## Jaki jest cel transakcji PayJoin?


Transakcja PayJoin służy dwóm celom, które pozwalają użytkownikom zwiększyć prywatność ich płatności.

Po pierwsze, PayJoin ma na celu wprowadzenie w błąd zewnętrznego obserwatora poprzez stworzenie wabika w analizie łańcucha. Jest to możliwe dzięki heurystyce Common Input Ownership (CIOH). Zwykle, gdy transakcja na Blockchain ma wiele wejść, zakłada się, że wszystkie te wejścia prawdopodobnie należą do tego samego podmiotu lub użytkownika. Tak więc, gdy analityk bada transakcję PayJoin, jest przekonany, że wszystkie dane wejściowe pochodzą od tej samej osoby. Jednak takie postrzeganie jest nieprawidłowe, ponieważ odbiorca płatności również wnosi wkład obok faktycznego płatnika. W związku z tym analiza łańcucha kieruje się w stronę interpretacji, która okazuje się fałszywa.


Co więcej, PayJoin pozwala również oszukać zewnętrznego obserwatora co do faktycznej kwoty dokonanej płatności. Analizując strukturę transakcji, analityk może sądzić, że płatność jest równoważna kwocie jednego z wyjść. W rzeczywistości jednak kwota płatności nie odpowiada żadnemu z wyników. W rzeczywistości jest to różnica między wyjściem odbiorcy UTXO a wejściem odbiorcy UTXO. W tym sensie transakcja PayJoin należy do domeny steganografii. Pozwala ona na ukrycie rzeczywistej kwoty transakcji w ramach fałszywej transakcji, która działa jako wabik.


Zwróć uwagę na naszą definicję **stenografii**:

> Steganografia to technika ukrywania informacji w innych danych lub obiektach w taki sposób, że obecność ukrytej informacji nie jest zauważalna. Na przykład, tajna wiadomość może być ukryta wewnątrz kropki w tekście, który nie ma z nią nic wspólnego, dzięki czemu jest niewykrywalna gołym okiem (jest to technika mikropunktów). W przeciwieństwie do szyfrowania, które sprawia, że informacje są niezrozumiałe bez klucza deszyfrującego, steganografia nie modyfikuje informacji. Pozostaje ona widoczna gołym okiem. Jej celem jest raczej ukrycie istnienia tajnej wiadomości, podczas gdy szyfrowanie wyraźnie ujawnia obecność ukrytych informacji, choć niedostępnych bez klucza.

Wróćmy do naszego przykładu transakcji PayJoin dotyczącej płatności za bagietkę.

![Payjoin transaction schema from the outside](assets/en/2.webp)

Widząc tę transakcję na Blockchain, zewnętrzny obserwator, który postępuje zgodnie ze zwykłą heurystyką analizy łańcucha, zinterpretowałby ją w następujący sposób: "*Alice połączyła 2 UTXO jako dane wejściowe transakcji, aby zapłacić `19,000 Sats` Bobowi*"

![Incorrect interpretation of Payjoin transaction from the outside](assets/en/3.webp)

Ta interpretacja jest oczywiście błędna, ponieważ, jak już wiesz, dwa wejściowe UTXO nie należą do tej samej osoby. Co więcej, rzeczywista wartość płatności nie wynosi `19 000 Sats`, ale raczej `4 000 Sats`. Analiza zewnętrznego obserwatora jest zatem ukierunkowana na błędny wniosek, zapewniając zachowanie poufności zainteresowanych stron.![Schemat transakcji PayJoin](assets/en/1.webp)

Jeśli chcesz przeanalizować prawdziwą transakcję PayJoin, oto jedna, którą przeprowadziłem na Testnet: [8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c](https://Mempool.space/fr/Testnet/tx/8dba6657ab9bb44824b3317c8cc3f333c2f465d3668c678691a091cdd6e5984c)


[**-> Odkryj nasz poradnik, jak zrobić PayJoin z Samourai Wallet**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-samourai-Wallet-48a5c711-ee3d-44db-b812-c55913080eab)


[**-> Odkryj nasz samouczek, jak zrobić PayJoin z Sparrow Wallet**](https://planb.network/tutorials/privacy/On-Chain/PayJoin-sparrow-Wallet-087a0e49-61cd-41f5-8440-ac7b157bdd62)



**Zasoby zewnętrzne:**


- https://docs.samourai.io/en/spend-tools#stowaway;
- https://gist.githubusercontent.com/LaurentMT/e758767ca4038ac40aaf/raw/c8125f6a3c3d0e90246dc96d3b603690ab6f1dcc/gistfile1.txt;
- https://github.com/Bitcoin/bips/blob/master/bip-0078.mediawiki.