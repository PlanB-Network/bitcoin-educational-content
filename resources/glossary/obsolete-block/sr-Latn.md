---
term: ZASTARELO (BLOK)
---

Odnosi se na blok bez dece: važeći blok, ali isključen iz glavnog Bitcoin lanca. To se dešava kada dva rudara pronađu važeći blok na istoj visini lanca u kratkom vremenskom periodu i emituju ga preko mreže. Čvorovi na kraju biraju samo jedan blok za uključivanje u lanac, prema principu lanca sa najviše akumuliranog rada, čineći drugi "zastarelim". Proces koji vodi do proizvodnje zastarelog bloka je sledeći:


- Dva rudara pronađu važeći blok na istoj visini lanca u kratkom vremenskom intervalu. Nazovimo ih `Blok A` i `Blok B`;
- Svaki emituje svoj blok mreži čvorova Bitcoin. Svaki čvor sada ima 2 bloka na istoj visini. Dakle, postoje dva važeća lanca;
- Rudari nastavljaju da traže dokaze o radu za sledeće blokove, ali da bi to učinili, moraju nužno izabrati samo jedan blok između `Block A` i `Block B` na kojem će kopati;
- Miner na kraju pronalazi važeći blok iznad `Block B`. Nazovimo ga `Block B+1`;
- Oni emituju `Block B+1` mrežnim čvorovima;
- Pošto čvorovi prate najduži lanac (sa najviše akumuliranog rada), proceniće da je `Lanac B` taj koji treba pratiti;
- Oni će napustiti `Block A` koji više nije deo glavnog lanca. Tako je postao zastareli blok.


![](../../dictionnaire/assets/9.webp)


> ► *U engleskom jeziku, to se naziva "Stale Block". Na francuskom, može se nazvati i "bloc périmé" ili "bloc abandonné". Iako se ne slažem s ovom upotrebom, neki bitkoineri koriste izraz "bloc orphelin" da označe ono što je zapravo zastareli blok.*