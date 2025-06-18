---
term: Commitment Transaction
---

W kontekście dwukierunkowego kanału w Lightning, Commitment Transaction jest transakcją, którą obie strony tworzą i podpisują, bez publikowania jej w głównym łańcuchu. Reprezentuje ona aktualny stan dystrybucji środków między stronami kanału, a każda płatność Lightning skutkuje nowym Commitment Transaction. Transakcje te są ważne, ale są transmitowane tylko wtedy, gdy kanał zostanie jednostronnie zamknięty. Zawierają one dane wyjściowe dla każdej ze stron, odzwierciedlające podział środków zgodnie z płatnościami Lightning dokonanymi od momentu otwarcia kanału. Mechanizmy kar są powiązane, aby powstrzymać strony przed nadawaniem nieaktualnych stanów kanału, tj. starych transakcji Commitment, które odzwierciedlają nieprawidłowy podział środków.