---
term: BIP0044
definition: Standard som definierar den fullständiga strukturen för härledningssökvägar för HD-plånböcker purpose, coin_type, account, change och address_index.
---

Ett förbättringsförslag som introducerar en standardiserad hierarkisk härledningsstruktur för HD-plånböcker. BIP44 bygger på de principer som fastställdes av BIP32 för härledning av nycklar och på BIP43 för användningen av fältet "purpose". Den introducerar en härledningsstruktur på fem nivåer: `m / purpose' / coin_type' / account' / change / address_index`. Här är detaljerna för varje djup:


- `m /` anger den privata huvudnyckeln. Den är unik för en Wallet och kan inte ha syskon på samma djup. Huvudnyckeln är direkt härledd från Wallet:s seed;
- `m / purpose' /` anger avledningens syfte som hjälper till att identifiera den standard som följs. Detta fält beskrivs i BIP43. Till exempel, om Wallet följer BIP84 (SegWit V0) standarden, skulle indexet vara `84'`;
- `m / purpose' / coin-type' /` anger typen av kryptovaluta. Detta gör det möjligt att tydligt skilja mellan grenar som är dedikerade till en kryptovaluta och de som är dedikerade till en annan kryptovaluta i en Wallet med flera mynt. Indexet som är dedikerat till Bitcoin är `0'`;
- `m / ändamål' / mynttyp' / konto' /` anger kontonumret. Detta djup gör det möjligt att enkelt skilja ut och organisera en Wallet i olika konton. Dessa konton är numrerade med början från `0`. Utökade nycklar (`xpub`, `xprv`...) finns på detta djup;
- `m / ändamål' / mynttyp' / konto' / växel /` anger kedjan. Varje konto enligt definitionen på djup 3 har två kedjor på djup 4: en extern kedja och en intern kedja (även kallad "change"). Den externa kedjan härleder adresser som är avsedda att kommuniceras offentligt, dvs. de adresser som erbjuds oss när vi klickar på "receive" i vår Wallet-programvara. Den interna kedjan härleder adresser som inte är avsedda att utbytas offentligt, dvs. främst ändringsadresser. Den externa kedjan identifieras med index "0" och den interna kedjan identifieras med index "1". Du kommer att märka att vi från detta djup inte längre utför en härdad avledning utan en normal avledning (det finns ingen apostrof). Det är tack vare denna mekanism som vi kan härleda alla underordnade publika nycklar från deras `xpub`;
- `m / purpose' / coin-type' / account' / change / Address-index` anger helt enkelt numret på den mottagande Address och dess nyckelpar, för att skilja den från dess syskon på samma djup på samma gren. Till exempel har den första härledda Address index `0`, den andra Address har index `1`, och så vidare...

Om till exempel min mottagare Address har avledningsvägen `m / 86' / 0' / 0' / 0 / 5`, kan vi härleda följande information:


- `86'` anger att vi följer avledningsstandarden för BIP86 (Taproot eller SegWitV1);
- `0'` anger att det är en Bitcoin Address;
- `0'` indikerar att vi befinner oss på det första kontot i Wallet;
- `0` indikerar att det är en extern Address;
- "5" anger att det är den sjätte externa Address för detta konto.