---
term: REKURENCYJNY (PRZYMIERZE)
---

Przymierze rekurencyjne na Bitcoin jest rodzajem Smart contract, który nakłada warunki nie tylko na bieżącą transakcję, ale także na przyszłe transakcje, które wydają wyniki tej transakcji. Pozwala to na tworzenie łańcuchów transakcji, z których każdy musi przestrzegać pewnych zasad określonych przez pierwszy w łańcuchu. Rekursywność tworzy sekwencję transakcji, z których każda dziedziczy ograniczenia z transakcji nadrzędnej. Umożliwiłoby to złożoną i długoterminową kontrolę nad sposobem wydawania bitcoinów, ale wprowadziłoby również ryzyko związane ze swobodą wydawania i zamiennością.


Podsumowując, umowa nierekurencyjna ograniczałaby się jedynie do transakcji następującej bezpośrednio po tej, która ustanowiła zasady. I odwrotnie, rekurencyjny pakt ma możliwość nakładania określonych warunków na Bitcoin w nieskończoność. Transakcje mogą następować po sobie, ale dany Bitcoin zawsze zachowa początkowe warunki z nim związane. Technicznie rzecz biorąc, ustanowienie nierekurencyjnego przymierza ma miejsce, gdy `scriptPubKey` UTXO definiuje ograniczenia na `scriptPubKey` wyjścia transakcji, która wydaje wspomniany UTXO. Z drugiej strony, ustanowienie rekursywnego przymierza ma miejsce, gdy `scriptPubKey` UTXO definiuje ograniczenia na `scriptPubKey` wyjścia transakcji, która wydaje ten UTXO i na wszystkie `scriptPubKey`, które nastąpią po wydaniu tego UTXO.


Mówiąc bardziej ogólnie, w informatyce to, co nazywa się "rekursją", to zdolność funkcji do wywoływania samej siebie, tworząc rodzaj pętli.