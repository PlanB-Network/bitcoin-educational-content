---
term: UPROSZCZONA WERYFIKACJA PŁATNOŚCI
---

Metoda umożliwiająca lekkim klientom weryfikację transakcji Bitcoin bez pobierania całego Blockchain. Węzeł korzystający z SPV pobiera tylko nagłówki bloków, które są znacznie lżejsze niż kompletne bloki. Kiedy musi zweryfikować transakcję, węzeł SPV żąda dowodu Merkle od pełnych węzłów, aby potwierdzić, że transakcja jest zawarta w określonym bloku. Takie podejście jest skuteczne w przypadku urządzeń o ograniczonych zasobach, takich jak smartfony, ale oznacza zależność od pełnych węzłów, co może zmniejszyć bezpieczeństwo i zwiększyć wymagane zaufanie.


> skrót "SPV" jest często używany w odniesieniu do tej metody