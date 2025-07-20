---
term: Anchor
---

U RGB protokolu, Anchor predstavlja skup podataka na strani klijenta koji se koriste za dokazivanje uključivanja jednog Commitment u transakciju. U RGB protokolu, Anchor se sastoji od sledećih Elements:




- transaction ID Bitcoin (txid) od Witness Transaction ;
- Multi Protocol Commitment (MPC);
- Deterministic Bitcoin Commitment (DBC);
- Dodatni dokaz transakcije (ETP) ako se koristi mehanizam Tapret Commitment.


Anchor stoga služi za uspostavljanje proverljive veze između određene Bitcoin transakcije i privatnih podataka potvrđenih RGB protokolom. To garantuje da su ovi podaci zaista uključeni u Blockchain, bez da se njihov tačan sadržaj objavi.