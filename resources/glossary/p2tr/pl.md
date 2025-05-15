---
term: P2TR
---

P2TR to skrót od *Pay to Taproot*, który jest standardowym modelem skryptu używanym do ustalania warunków wydatków na UTXO (niewydane dane wyjściowe transakcji). Został on wprowadzony wraz z wdrożeniem Taproot w listopadzie 2021 roku. P2TR wykorzystuje protokół Schnorra do agregacji kluczy kryptograficznych, a także drzewa Merkle dla alternatywnych skryptów, znanych jako MAST (*Merkelized Alternative Script Tree*). W przeciwieństwie do tradycyjnych transakcji, w których warunki wydatków są publicznie ujawniane (czasami w momencie otrzymania, czasami w momencie wydania), P2TR pozwala na ukrycie złożonych skryptów za pojedynczym pozornym kluczem publicznym.


Technicznie rzecz biorąc, skrypt P2TR blokuje bitcoiny na unikalnym kluczu publicznym Schnorra, oznaczonym jako $K$. Klucz $K$ jest jednak w rzeczywistości agregatem klucza publicznego $P$ i klucza publicznego $M$, przy czym ten ostatni jest obliczany na podstawie Merkle Root listy `scriptPubKey`. Bitcoiny zablokowane skryptem P2TR można wydać na dwa różne sposoby: albo publikując podpis dla klucza publicznego $P$, albo spełniając jeden ze skryptów zawartych w Merkle Tree. Pierwsza opcja nazywana jest "*ścieżką klucza*", a druga "*ścieżką skryptu*".


W ten sposób P2TR umożliwia użytkownikom wysyłanie bitcoinów albo do klucza publicznego, albo do wielu wybranych skryptów. Kolejną zaletą tego skryptu jest to, że chociaż istnieje wiele sposobów na wydanie wyjścia P2TR, tylko ten, który jest używany, musi zostać ujawniony w momencie wydawania, pozwalając niewykorzystanym alternatywom pozostać prywatnymi. P2TR jest wyjściem SegWit w wersji 1, co oznacza, że podpisy dla wejść P2TR są przechowywane w świadku transakcji, a nie w `scriptSig`. Adresy P2TR używają kodowania `Bech32m` i zaczynają się od `bc1p`.