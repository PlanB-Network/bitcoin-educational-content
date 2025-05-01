---
term: Address REUSE
---

Ponowne wykorzystanie Address odnosi się do praktyki używania tego samego Address do blokowania wielu UTXO, czasami w ramach kilku różnych transakcji. Bitcoiny są zazwyczaj blokowane przy użyciu pary kluczy kryptograficznych, która odpowiada unikalnemu Address. Ponieważ Blockchain jest publiczny, łatwo jest sprawdzić, które adresy są powiązane z iloma bitcoinami. W przypadku ponownego użycia tego samego Address do wielu płatności, rozsądne jest wyobrażenie sobie, że wszystkie powiązane UTXO należą do tego samego podmiotu. W związku z tym ponowne wykorzystanie Address stanowi problem dla prywatności użytkownika. Pozwala to na deterministyczne powiązania między wieloma transakcjami i UTXO, a także utrwala śledzenie funduszy On-Chain. Satoshi Nakamoto wspomniał już o tym problemie w swojej Białej Księdze:


> "*Jako dodatkowy firewall, nowa para kluczy mogłaby być używana dla każdej transakcji, aby uniemożliwić ich powiązanie ze wspólnym właścicielem." - Nakamoto, S. (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System". Konsultacje pod adresem https://Bitcoin.org/Bitcoin.pdf.

Aby zachować prywatność na minimalnym poziomie, zdecydowanie zaleca się użycie każdego otrzymanego Address tylko raz. Dla każdej nowej płatności należy użyć nowego Address. W przypadku zmiany danych wyjściowych należy również użyć nowego Address. Na szczęście, dzięki deterministycznym i hierarchicznym portfelom, korzystanie z wielu adresów stało się bardzo łatwe. Wszystkie pary kluczy powiązane z Wallet można łatwo zregenerować z seed. Dlatego też oprogramowanie Wallet zawsze generuje nowy, inny Address po kliknięciu przycisku "Odbierz".


> w języku angielskim nazywa się to "Address Reuse"