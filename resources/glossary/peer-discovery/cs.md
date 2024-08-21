---
term: PEER DISCOVERY
---

Proces, při kterém se uzly v síti Bitcoin připojují k ostatním uzlům za účelem získání informací. Když je uzel Bitcoinu poprvé spuštěn, nemá žádné informace o ostatních uzlech v síti. Přesto musí navázat spojení, aby se synchronizoval s blockchainem, který má nejvíce nahromaděné práce. K objevení těchto peerů se používá několik mechanismů podle priority:
* Uzel začíná konzultací svého lokálního souboru `peers.dat`, který uchovává informace o uzlech, se kterými dříve interagoval. Pokud je uzel nový, tento soubor bude prázdný a proces přejde k dalšímu kroku;
* V případě, že soubor `peers.dat` neobsahuje žádné informace (což je normální u nově spuštěného uzlu), uzel provádí DNS dotazy na DNS semena. Tyto servery poskytují seznam IP adres předpokládaně aktivních uzlů pro navázání spojení. Adresy DNS semen jsou zakódovány přímo v kódu Bitcoin Core. Tento krok obvykle stačí k dokončení objevování peerů;
* Pokud DNS semena neodpoví do 60 sekund, uzel se může obrátit na seed uzly. Jedná se o veřejné Bitcoin uzly uvedené v statickém seznamu téměř tisíce záznamů integrovaných přímo do zdrojového kódu Bitcoin Core. Nový uzel použije tento seznam k navázání prvního spojení se sítí a získání IP adres ostatních uzlů;
* V velmi nepravděpodobném případě, že všechny předchozí metody selžou, má operátor uzlu vždy možnost ručně přidat IP adresy uzlů pro navázání prvního spojení.