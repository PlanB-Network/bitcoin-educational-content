---
term: BIP0021
definition: Standard som definierar formatet för Bitcoin URIer (länkar som börjar med bitcoin) för att underlätta betalningar via länkar eller QR-koder.
---

Förslag skrivet av Nils Schneider och Matt Corallo, baserat på BIP20 skrivet av Luke Dashjr, som i sin tur kom från ett annat dokument skrivet av Nils Schneider. BIP21 definierar hur mottagaradresser ska kodas i URI:er (*Uniform Resource Identifier*) för att underlätta betalningar. Till exempel skulle en Bitcoin URI som följer BIP21 där jag under etiketten "*Pandul*" skulle begära att skicka mig 0,1 BTC se ut så här:


```text
bitcoin:bc1qmp7emyf7un49eaz0nrxk9mdfrtn67v5y866fvs?amount=0.1&label=Pandul
```


Denna standardisering förbättrar användarupplevelsen av Bitcoin-transaktioner genom att göra det möjligt att klicka på en länk eller skanna en QR-kod för att initiera sina parametrar. BIP21-standarden används nu i stor utsträckning i Bitcoin Wallet-programvara.