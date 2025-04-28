---
term: DUSTRELAYFEE
---

Sheria ya kusanifisha inayotumiwa na nodi za mtandao ili kubaini kile wanachokizingatia "kikomo cha Dust." Kigezo hiki huweka kiwango cha ada katika Sats kwa kila kilobaiti pepe (Sats/kvB) ambayo hutumika kama marejeleo ya kukokotoa ikiwa thamani ya UTXO ni chini ya ada zinazohitajika ili kuijumuisha katika shughuli ya ununuzi. Hakika, UTXO inachukuliwa kuwa "Dust" kwenye Bitcoin ikiwa inahitaji ada zaidi kuhamishwa kuliko thamani inayojiwakilisha yenyewe. Hesabu ya kikomo hiki ni kama ifuatavyo.


```text
limit = (input size + output size) * fee rate
```


Kwa vile kiwango cha ada kinachohitajika cha shughuli itakayojumuishwa kwenye kizuizi cha Bitcoin hubadilika kila mara, kigezo cha `DustRelayFee` huruhusu kila nodi kubainisha kiwango cha ada kinachotumika katika hesabu hii. Kwa chaguo-msingi, kwenye Bitcoin Core, thamani hii imewekwa kuwa 3,000 Sats/kvB. Kwa mfano, ili kukokotoa kikomo cha Dust kwa ingizo na pato la P2PKH, ambalo hupima baiti 148 na 34 mtawalia, hesabu itakuwa:


```text
limit (sats) = (148 + 34) * 3000 / 1000 = 546 sats
```


Hii inamaanisha kuwa nodi inayohusika haitarejelea miamala ikijumuisha UTXO iliyolindwa ya P2PKH ambayo thamani yake ni chini ya 546 Sats.