---
term: Anchor
---

W protokole RGB Anchor reprezentuje zestaw danych po stronie klienta używanych do udowodnienia włączenia pojedynczego Commitment do transakcji. W protokole RGB Anchor składa się z następujących Elements:




- transaction ID Bitcoin (txid) od Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Dodatkowy dowód transakcji (ETP), jeśli używany jest mechanizm Tapret Commitment.


Anchor służy zatem do ustanowienia weryfikowalnego powiązania między konkretną transakcją Bitcoin a prywatnymi danymi zweryfikowanymi przez protokół RGB. Gwarantuje on, że dane te są rzeczywiście zawarte w Blockchain, bez podawania ich dokładnej treści do wiadomości publicznej.