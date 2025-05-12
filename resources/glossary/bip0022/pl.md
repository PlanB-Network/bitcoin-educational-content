---
term: BIP0022
---

BIP zaproponowany w 2012 roku przez Luke'a Dashjra, który wprowadza ustandaryzowaną metodę JSON-RPC dla zewnętrznych interfejsów Mining, zwaną "getblocktemplate". Wraz ze wzrostem trudności Mining, rozwinęło się wykorzystanie specjalistycznego oprogramowania zewnętrznego do produkcji Proof of Work. Niniejszy BIP proponuje wspólny standard komunikacji dla szablonu bloku między pełnymi węzłami a oprogramowaniem specjalizującym się w Mining. Metoda ta polega na wysyłaniu całej struktury bloku, a nie tylko nagłówka, aby umożliwić Miner dostosowanie go.