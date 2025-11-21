---
term: WŁÓKNO
---

Skrót od "*Fast Internet Bitcoin Relay Engine*". Jest to protokół zaprojektowany przez Matta Corallo w 2016 roku w celu przyspieszenia dystrybucji bloków Bitcoin na całym świecie. Jego celem było zmniejszenie opóźnień propagacji tak blisko fizycznych limitów, jak to tylko możliwe. FIBRE miał na celu zapewnienie bardziej sprawiedliwej dystrybucji możliwości Mining, upewniając się, że proporcja bloków wydobytych przez uczestnika dokładnie odzwierciedla jego wkład pod względem mocy obliczeniowej, niezależnie od jego pozycji w sieci.


Rzeczywiście, opóźnienia w transmisji blokowej mogą faworyzować duże, dobrze połączone grupy Mining, często zlokalizowane blisko siebie, ze szkodą dla mniejszych. Zjawisko to może z czasem zwiększyć centralizację Mining i zmniejszyć ogólne bezpieczeństwo systemu. Aby rozwiązać tę kwestię w Address, FIBRE wprowadziło kody korekcji błędów i transmisję dodatkowych danych w celu zrównoważenia utraty pakietów, a także wykorzystanie kompaktowych bloków podobnych do tych opisanych w BIP152, wszystkie działające za pośrednictwem UDP w celu ominięcia pewnych ograniczeń TCP. Niemniej jednak FIBRE został porzucony w 2020 roku, głównie ze względu na jego zależność od jednego opiekuna oraz fakt, że przyjęcie BIP152 sprawiło, że taki system stał się mniej istotny.