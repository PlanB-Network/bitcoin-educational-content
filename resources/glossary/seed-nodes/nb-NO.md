---
term: SEED NODES

---
Statisk liste over offentlige Bitcoin-noder, integrert direkte i kildekoden til Bitcoin Core (`bitcoin/src/chainparamsseeds.h`). Denne listen fungerer som tilkoblingspunkter for nye Bitcoin-noder som blir med i nettverket, men den brukes bare hvis DNS-frøene ikke gir et svar innen 60 sekunder etter forespørselen. I dette tilfellet vil den nye Bitcoin-noden koble seg til disse seed-nodene for å etablere en første tilkobling til nettverket og be om IP-adresser til andre noder. Det endelige målet er å skaffe den nødvendige informasjonen for å utføre Initial Block Download (IBD) og synkronisere med den kjeden som har mest akkumulert arbeid. Listen over seed-noder omfatter nesten 1000 noder, identifisert i samsvar med standarden som er etablert av BIP155. Dermed representerer seed-noder den tredje metoden for tilkobling til nettverket for en Bitcoin-node, etter den mulige bruken av `peers.dat`-filen, opprettet av noden selv, og anmodningen om DNS-frø.

> seed-noder må ikke forveksles med "DNS seeds", som er den andre metoden for å etablere forbindelser