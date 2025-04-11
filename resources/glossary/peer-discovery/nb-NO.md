---
term: PEER DISCOVERY

---
Prosessen der noder i Bitcoin-nettverket kobler seg til andre noder for å innhente informasjon. Når en Bitcoin-node først lanseres, har den ingen informasjon om andre noder i nettverket. Likevel må den etablere forbindelser for å synkronisere med den blokkjeden som har mest akkumulert arbeid. Det finnes flere mekanismer som brukes for å finne disse jevnaldrende, i prioritert rekkefølge:


- Noden starter med å konsultere sin lokale `peers.dat`-fil, som inneholder informasjon om noder som den tidligere har samhandlet med. Hvis noden er ny, vil denne filen være tom, og prosessen går videre til neste trinn;
- Hvis det ikke finnes informasjon i filen `peers.dat` (noe som er normalt for en nystartet node), utfører noden DNS-spørringer til DNS-frøene. Disse serverne gir en liste over IP-adresser til antatt aktive noder for å etablere forbindelser. Adressene til DNS-frøene er hardkodet i Bitcoin Core-koden. Dette trinnet er vanligvis tilstrekkelig for å fullføre oppdagelsen av jevnaldrende;
- Hvis DNS-frøene ikke svarer innen 60 sekunder, kan noden henvende seg til seed-nodene. Dette er offentlige Bitcoin-noder som er oppført i en statisk liste med nesten tusen oppføringer som er integrert direkte i kildekoden til Bitcoin Core. Den nye noden bruker denne listen til å etablere en første tilkobling til nettverket og skaffe IP-adresser til andre noder;
- I det svært usannsynlige tilfellet at alle de foregående metodene mislykkes, har nodeoperatøren alltid muligheten til å legge til IP-adresser til noder manuelt for å opprette en første tilkobling.