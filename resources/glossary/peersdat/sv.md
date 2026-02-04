---
term: Peers.dat
definition: Bitcoin Core-fil som lagrar information om nodens kända partners (peers).
---

Namnet på den datafil som används av Bitcoin Core-programvaran för att lagra information om peers (dvs. noder) i nätverket som användarens nod har interagerat med eller potentiellt kan interagera med. Den innehåller detaljer som IP-adresser, portnummer och olika metadata. De noder som finns med i listan är som standard seed-noderna, följt av alla andra upptäckta eller manuellt tillagda noder. Den här filen innehåller vanligtvis en mycket stor lista över peers från vilka noden slumpmässigt väljer att upprätta sina anslutningar.