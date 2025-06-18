---
term: ŚCIĄGANIE OPŁAT
---

Scenariusz ataku, w którym górnicy starają się przepisać niedawno potwierdzony blok w celu pobrania zawartych w nim opłat transakcyjnych, jednocześnie dodając transakcje o wysokiej opłacie, które pojawiły się w międzyczasie w Mempool. Ostatecznym celem tego ataku dla Miner jest zwiększenie ich rentowności. Fee sniping może stać się coraz bardziej opłacalny, gdy Block reward maleje, a opłaty transakcyjne stanowią większą część przychodów górników. Może to być również korzystne, gdy opłaty zawarte w poprzednim bloku są znacznie wyższe niż te w następnym najlepszym bloku kandydującym. Upraszczając, Miner staje przed takim wyborem pod względem zachęt:


- Wydobywaj w normalny sposób po ostatnim bloku, z wysokim prawdopodobieństwem zdobycia niskiej nagrody;
- Próba wydobycia poprzedniego bloku (fee sniping), z niskim prawdopodobieństwem zdobycia wysokiej nagrody.


Atak ten stanowi zagrożenie dla systemu Bitcoin, ponieważ im więcej górników go stosuje, tym bardziej inni górnicy, początkowo uczciwi, są zachęcani do robienia tego samego. Rzeczywiście, za każdym razem, gdy nowy Miner dołącza do tych, którzy próbują snipować opłaty, prawdopodobieństwo, że jeden z atakujących górników odniesie sukces, wzrasta, a prawdopodobieństwo, że jeden z uczciwych górników przedłuży łańcuch, maleje. Jeśli atak ten zostanie przeprowadzony masowo i utrzyma się w czasie, potwierdzenia bloków nie będą już wiarygodnym wskaźnikiem niezmienności transakcji Bitcoin. Mogłoby to potencjalnie uczynić system bezużytecznym.


Aby przeciwdziałać temu ryzyku, większość oprogramowania Wallet automatycznie wypełnia pole `nLocktime`, warunkując walidację transakcji włączeniem do następnej wysokości bloku. W ten sposób niemożliwe staje się włączenie transakcji do przepisania poprzedniego bloku. Jeśli powszechne stosowanie `nLocktime` zostanie przyjęte przez użytkowników Bitcoin, znacznie zmniejszy to zachęty do snipowania opłat. W rzeczywistości zachęca to raczej do progresji Blockchain niż do jego przepisywania, zmniejszając potencjalne zyski z niego. Dla transakcji Taproot, BIP326 proponuje użycie pola `nSequence` w podobny sposób, aby osiągnąć równoważny efekt pola `nLocktime` dla innych typów transakcji. Takie użycie upiekłoby dwie pieczenie na jednym ogniu, poprawiając również prywatność protokołów drugiego Layer, które używają tego samego pola.