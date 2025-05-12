---
term: P2SH
---

P2SH to skrót od *Pay to Script Hash*. Jest to standardowy model skryptu używany do ustalania warunków wydatków na UTXO. W przeciwieństwie do skryptów P2PK i P2PKH, w których warunki wydatków są predefiniowane, P2SH umożliwia integrację dowolnych warunków wydatków i dodatkowych funkcji w skrypcie transakcji.


Technicznie, w transakcji P2SH, `scriptPubKey` zawiera kryptograficzny Hash z `redeemscript`, a nie wyraźne warunki wydatkowania. Ten Hash jest uzyskiwany przy użyciu `SHA256` Hash. Podczas wysyłania bitcoinów do P2SH Address, bazowy `redeemscript` nie jest ujawniany. Tylko jego Hash jest zawarty w transakcji. Adresy P2SH są zakodowane w `Base58Check` i zaczynają się od liczby `3`. Gdy odbiorca chce wydać otrzymane bitcoiny, musi dostarczyć `redeemscript`, który pasuje do Hash obecnego w `scriptPubKey`, wraz z danymi niezbędnymi do spełnienia warunków tego `redeemscript`. Na przykład, w skrypcie P2SH z wieloma podpisami, skrypt może wymagać podpisów z wielu kluczy prywatnych.


Korzystanie z P2SH oferuje większą elastyczność, ponieważ pozwala na tworzenie dowolnych skryptów bez znajomości szczegółów przez nadawcę. P2SH został wprowadzony w 2012 roku wraz z BIP16.