---
term: WĘZEŁ SPV (WĘZEŁ ŚWIETLNY)
---

Węzeł SPV (*Simple Payment Verification*), czasami nazywany "lekkim węzłem", jest lekkim klientem węzła Bitcoin, który umożliwia użytkownikom walidację transakcji bez konieczności przechowywania całego Blockchain. Zamiast tego węzeł SPV przechowuje tylko nagłówki bloków i uzyskuje informacje o konkretnych transakcjach, wysyłając w razie potrzeby zapytania do pełnych węzłów. Ta zasada weryfikacji jest możliwa dzięki strukturze transakcji w blokach Bitcoin, które są zorganizowane w ramach akumulatora kryptograficznego (Merkle Tree).


Takie podejście jest korzystne dla urządzeń o ograniczonych zasobach, takich jak telefony komórkowe. Węzły SPV polegają jednak na pełnych węzłach w zakresie dostępności informacji, co oznacza dodatkowy poziom zaufania, a w konsekwencji mniejsze bezpieczeństwo w porównaniu z pełnymi węzłami. Węzły SPV nie mogą autonomicznie weryfikować transakcji, ale mogą sprawdzić, czy transakcja jest zawarta w bloku, sprawdzając dowody Merkle.