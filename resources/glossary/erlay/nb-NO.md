---
term: ERLAY
---

Foreslått nettverksprotokoll for å forbedre effektiviteten ved videresending av ubekreftede transaksjoner mellom Bitcoin-noder.


I dag spres hver transaksjon via et system der hver node kringkaster den transaksjonen den kjenner til, til alle de andre nodene. Problemet er at dette fører til mye redundans og bruk av båndbredde til duplikater. Mange transaksjonssendinger er unødvendige, siden mottakeren allerede vet om transaksjonene, og hver node trenger bare å vite om hver transaksjon én gang. Erlay foreslår å begrense antallet motparter som en node sender transaksjoner den kjenner til, til 8 som standard, og deretter bruke en avstemmingsprosess basert på minisketch-biblioteket for å dele manglende transaksjoner mer effektivt.


Erlay vil redusere båndbreddeforbruket med rundt 40 %, noe som gjør Full node-drift mer tilgjengelig for brukere med begrensede Internett-tilkoblinger, og dermed fremmer bedre desentralisering av nettverket. Denne protokollen vil også opprettholde et nesten konstant båndbreddeforbruk etter hvert som antallet tilkoblinger øker. Det betyr at det blir mye enklere for nodeoperatører å akseptere et svært stort antall tilkoblinger fra sine jevnaldrende, noe som vil øke sikkerheten i Bitcoin-nettverket ved å redusere risikoen for partisjonering, enten den er tilsiktet eller utilsiktet. I tillegg vil Erlay gjøre det vanskeligere å finne ut hvilken node en transaksjon kommer fra, noe som vil øke konfidensialiteten for brukere av noder som ikke opererer under Tor.


Erlay er foreslått i BIP330.