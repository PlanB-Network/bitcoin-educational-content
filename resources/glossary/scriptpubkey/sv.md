---
term: Scriptpubkey
definition: Skript i utdata från en transaktion som definierar utgiftsvillkoren för en UTXO.
---

Ett skript som finns i utdatadelen av en Bitcoin-transaktion som definierar villkoren under vilka den tillhörande UTXO kan spenderas. Detta skript säkrar således bitcoins. I sin vanligaste form innehåller `scriptPubKey` ett villkor som kräver att nästa transaktion tillhandahåller bevis på innehav av den privata nyckeln som motsvarar en specificerad Bitcoin Address. Detta uppnås ofta genom ett skript som kräver en signatur som motsvarar den publika nyckel som är associerad med den Address som används för att säkra dessa medel. När en transaktion försöker använda denna UTXO som input måste den tillhandahålla en `scriptSig` som, när den kombineras med `scriptPubKey`, uppfyller de fastställda villkoren och producerar ett giltigt script.


Här är t.ex. en klassisk P2PKH `scriptPubKey`:


```text
OP_DUP OP_HASH160 OP_PUSHBYTES_20 <address> OP_EQUALVERIFY OP_CHECKSIG
```


Motsvarande `scriptSig` skulle vara:


```text
<signature> <public key>
```





> ► *Detta script kallas ibland också för ett "locking script" på engelska*