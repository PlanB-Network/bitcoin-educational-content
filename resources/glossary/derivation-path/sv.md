---
term: Härledningssökväg
definition: Sekvens av index som beskriver härledningsvägen för barnnycklar från masternyckeln i en HD-plånbok.
---

När det gäller hierarkiskt deterministiska (HD) plånböcker avser en härledningsväg den sekvens av index som används för att härleda underordnade nycklar från en huvudnyckel. Denna väg beskrivs i BIP32 och identifierar trädstrukturen för härledning av underordnade nycklar. En härledningsväg representeras av en serie index åtskilda av snedstreck och börjar alltid med huvudnyckeln (betecknad med `m/`). En typisk sökväg kan t.ex. vara `m/84'/0'/0'/0/0`. Varje härledningsnivå är associerad med ett specifikt djup:


- `m /` anger den privata huvudnyckeln. Den är unik för en Wallet och kan inte ha syskon på samma djup. Huvudnyckeln härleds direkt från seed;
- `m / purpose' /` anger avledningens syfte som hjälper till att identifiera den standard som följs. Detta fält beskrivs i BIP43. Om till exempel Wallet följer BIP84-standarden (SegWit V0), skulle indexet vara `84'`;
- `m / purpose' / coin-type' /` anger typen av kryptovaluta. Detta gör det möjligt att tydligt skilja mellan grenar som är dedikerade till en kryptovaluta och de som är dedikerade till en annan i en Wallet med flera mynt. Indexet som är dedikerat till Bitcoin är `0'`;
- `m / ändamål' / mynttyp' / konto' /` anger kontonumret. Detta djup gör det lätt att skilja ut och organisera en Wallet i olika konton. Dessa konton är numrerade med början från `0`. Utökade nycklar (`xpub`, `xprv`...) finns på denna djupnivå;
- `m / ändamål' / mynttyp' / konto' / växel /` anger sökvägen. Varje konto enligt definitionen på djup 3 har två vägar på djup 4: en extern kedja och en intern kedja (även kallad "change"). Den externa kedjan härleder adresser som är avsedda att delas offentligt, det vill säga de adresser som erbjuds oss när vi klickar på "ta emot" i vår Wallet-programvara. Den interna kedjan härleder adresser som inte är avsedda att utbytas publikt, främst ändringsadresser. Den externa kedjan identifieras med index "0" och den interna kedjan identifieras med index "1". Du kommer att märka att vi från detta djup inte längre utför en härdad avledning utan en normal avledning (det finns ingen apostrof). Det är tack vare denna mekanism som vi kan härleda alla underordnade publika nycklar från deras `xpub`;



- `m / purpose' / coin-type' / account' / change / Address-index` anger helt enkelt numret på den mottagande Address och dess nyckelpar, för att skilja den från dess syskon på samma djup på samma gren. Till exempel har den första härledda Address index `0`, den andra Address har index `1`, och så vidare...


Om till exempel min mottagare Address har avledningsvägen `m / 86' / 0' / 0' / 0 / 5`, kan vi härleda följande information:


- `86'` anger att vi följer avledningsstandarden för BIP86 (Taproot / SegWit V1);
- `0'` anger att det är en Bitcoin Address;
- `0'` indikerar att vi befinner oss på det första kontot i Wallet;
- `0` indikerar att det är en extern Address;
- "5" anger att det är den sjätte externa Address för detta konto.


