---
term: redeemscript
---

Skrypt, który definiuje określone warunki, które muszą spełnić dane wejściowe, aby odblokować środki powiązane z wyjściem P2SH. W P2SH UTXO, `scriptPubKey` zawiera Hash z `redeemscript`. Gdy transakcja chce wydać ten UTXO jako wkład, musi dostarczyć czysty `redeemscript`, który pasuje do Hash zawartego w `scriptPubKey`. W ten sposób `redeemscript` jest podawany w `scriptSig` danych wejściowych, wraz z innymi Elements niezbędnymi do spełnienia warunków skryptu, takich jak podpisy lub klucze publiczne. Ta zamknięta struktura zapewnia, że szczegóły warunków wydawania pozostają ukryte, dopóki bitcoiny nie zostaną faktycznie wydane. Jest ona w szczególności wykorzystywana w portfelach wielopodpisowych Legacy P2SH.