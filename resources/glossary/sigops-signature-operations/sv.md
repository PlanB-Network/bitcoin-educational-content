---
term: Sigops (signaturoperationer)
definition: Digitala signaturoperationer som är nödvändiga för att validera Bitcoin-transaktioner.
---

Avser de operationer för digital signatur som krävs för att validera transaktioner. Varje Bitcoin-transaktion kan innehålla flera ingångar, som var och en kan kräva en eller flera signaturer för att anses giltiga. Verifieringen av dessa signaturer sker genom användning av specifika opkoder som kallas "sigops". Detta inkluderar särskilt `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` och `OP_CHECKMULTISIGVERIFY`. Dessa operationer innebär en viss arbetsbelastning för de nätverksnoder som måste verifiera dem. För att förhindra DoS-attacker genom artificiell inflation av antalet sigops, inför protokollet därför en gräns för antalet sigops som tillåts per block, för att säkerställa att valideringsbelastningen förblir hanterbar för noderna. Denna gräns är för närvarande satt till maximalt 80 000 sigops per block. För att räkna följer noderna dessa regler:


I `scriptPubKey` räknas `OP_CHECKSIG` och `OP_CHECKSIGVERIFY` som 4 sigop. Opkoderna `OP_CHECKMULTISIG` och `OP_CHECKMULTISIGVERIFY` räknas för 80 sigop. Under räkningen multipliceras dessa operationer med 4 när de inte är en del av en SegWit-ingång (för en P2WPKH blir antalet sigops därför 1);


I `redeemscript` räknas även opkoderna `OP_CHECKSIG` och `OP_CHECKSIGVERIFY` som 4 sigops, `OP_CHECKMULTISIG` och `OP_CHECKMULTISIGVERIFY` räknas som `4n` om de föregår `OP_n`, eller 80 sigops annars;


För `witnessScript`, `OP_CHECKSIG` och `OP_CHECKSIGVERIFY` är värda 1 sigop, `OP_CHECKMULTISIG` och `OP_CHECKMULTISIGVERIFY` räknas som `n` om de introduceras av `OP_n`, eller 20 sigops annars;


I Taproot-skript behandlas sigops på ett annat sätt jämfört med traditionella skript. I stället för att direkt räkna varje signaturoperation inför Taproot en sigops-budget för varje transaktionsinmatning, som är proportionell mot storleken på den inmatningen. Denna budget är 50 sigops plus bytestorleken på inmatningens vittne. Varje signaturoperation minskar denna budget med 50. Om utförandet av en signaturoperation sänker budgeten under noll är skriptet ogiltigt. Denna metod ger större flexibilitet i Taproot-skript, samtidigt som den skyddar mot potentiella missbruk relaterade till sigops, genom att direkt koppla dem till vikten på inmatningen. Taproot-skript ingår således inte i gränsen på 80 000 sigops per block.