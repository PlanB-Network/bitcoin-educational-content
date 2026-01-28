---
term: Scriptsig
definition: Indataelement som tillhandahåller data för att uppfylla scriptPubKey-villkoren.
---

Ett element i en Bitcoin-transaktion som finns i ingångarna. `scriptSig` tillhandahåller de uppgifter som behövs för att uppfylla de villkor som ställs av `scriptPubKey` i den föregående transaktionen från vilken medel används. Den spelar alltså en kompletterande roll till `scriptPubKey`. Vanligtvis innehåller `scriptSig` en digital signatur och en publik nyckel. Signaturen genereras av bitcoinsägaren med hjälp av dennes privata nyckel och bevisar att denne har rätt att spendera UTXO. I detta fall visar `scriptSig` att innehavaren av inmatningen har den privata nyckel som motsvarar den offentliga nyckel som är associerad med Address som anges i `scriptPubKey` i den föregående utgående transaktionen.


När transaktionen är verifierad exekveras uppgifterna från `scriptSig` i motsvarande `scriptPubKey`. Om resultatet är giltigt innebär det att villkoren för att använda medlen har uppfyllts. Om alla inmatningar i transaktionen ger en `scriptSig` som validerar deras `scriptPubKey`, är transaktionen giltig och kan läggas till i ett block för utförande.


Här är till exempel en klassisk P2PKH `scriptSig`:


```text
<signature> <public key>
```


Motsvarande `scriptPubKey` skulle vara:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```





> ► * `scriptSig` kallas ibland också för ett "unlocking script" på engelska*