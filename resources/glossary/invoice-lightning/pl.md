---
term: Faktura Lightning
definition: Żądanie płatności Lightning zawierające wszystkie informacje niezbędne do sfinalizowania transakcji.
---

Błyskawiczne żądanie płatności wygenerowane przez odbiorcę, zawierające wszystkie informacje potrzebne do sfinalizowania transakcji.


Invoice Lightning zawiera miejsce docelowe płatności w postaci klucza publicznego węzła odbiorcy, ale także prefiks `LN`, kwotę, czas do wygaśnięcia, Hash sekretu używanego w HTLC i inne metadane, z których niektóre są opcjonalne, takie jak opcje routingu. Faktury te są zdefiniowane w standardzie BOLT11. Po opłaceniu, Invoice Lightning nie może być ponownie użyty.


