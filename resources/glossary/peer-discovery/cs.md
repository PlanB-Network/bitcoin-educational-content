---
term: PEER DISCOVERY

---
Proces, při kterém se uzly v síti Bitcoin spojují s jinými uzly za účelem získání informací. Když je uzel bitcoinu poprvé spuštěn, nemá žádné informace o ostatních uzlech v síti. Přesto musí navázat spojení, aby se synchronizoval s blokovým řetězcem, který má nejvíce nahromaděné práce. K objevení těchto rovnocenných uzlů se používá několik mechanismů, seřazených podle priority:


- Uzel začne prohlížením svého místního souboru `peers.dat`, který uchovává informace o uzlech, s nimiž již dříve komunikoval. Pokud je uzel nový, bude tento soubor prázdný a proces přejde k dalšímu kroku;
- Pokud v souboru `peers.dat` nejsou žádné informace (což je u nově spuštěného uzlu běžné), provede uzel dotazy DNS na zárodky DNS. Tyto servery poskytují seznam IP adres pravděpodobně aktivních uzlů pro navázání spojení. Adresy DNS seedů jsou pevně zakódovány v kódu jádra bitcoinu. Tento krok obvykle stačí k dokončení zjišťování rovnocenných partnerů;
- Pokud semenné uzly DNS neodpoví do 60 sekund, může se uzel obrátit na semenné uzly. Jedná se o veřejné bitcoinové uzly uvedené ve statickém seznamu téměř tisíce položek integrovaném přímo do zdrojového kódu jádra Bitcoinu. Nový uzel použije tento seznam k navázání prvního připojení k síti a získání IP adres ostatních uzlů;
- Ve velmi nepravděpodobném případě, kdy všechny předchozí metody selžou, má provozovatel uzlu vždy možnost ručně přidat IP adresy uzlů pro navázání prvního spojení.