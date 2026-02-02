---
term: Återanvändbar betalkod
definition: Statisk identifierare från BIP47 som gör det möjligt att härleda unika adresser utan adressåteranvändning.
---

I BIP47 är en återanvändbar betalningskod en statisk identifierare som genereras från en Bitcoin Wallet och som möjliggör en aviseringstransaktion och härledning av unika adresser. På så sätt undviks återanvändning av adresser, vilket leder till förlust av integritet, utan att man manuellt behöver härleda och överföra nya, oanvända adresser för varje betalning. I BIP47 konstrueras återanvändbara betalningskoder på följande sätt:


- Byte 0 motsvarar versionen;
- Byte 1 är ett bitfält för att lägga till information i händelse av specifik användning;
- Byte 2 anger pariteten för `y` i den offentliga nyckeln;
- Från byte 3 till byte 34 hittar du `x`-värdet för den offentliga nyckeln;
- Från byte 35 till byte 66 finns chain code associerat med den publika nyckeln;
- Från byte 67 till byte 79 är det noll utfyllnad.


En Human-Readable Part (HRP) läggs i allmänhet till i början av betalningskoden och en checksumma i slutet, och sedan kodas den i base58. Konstruktionen av en betalningskod är således ganska lik den för en utökad nyckel. Här är till exempel min egen BIP47-betalningskod i base58:


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


I PayNym-implementeringen av BIP47 kan betalkoder också uttryckas i form av identifierare som är kopplade till bilden av en robot. Här är min, till exempel:


```text
+throbbingpond8B1
```


Användningen av betalkoder med PayNym-implementeringen är för närvarande tillgänglig på Sparrow wallet på PC och på Samourai Wallet på mobil.