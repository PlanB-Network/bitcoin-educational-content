---
term: BIP0330
---

Et forslag kjent som "*Erlay*", som tar sikte på å optimalisere spredningen av ubekreftede transaksjoner i Bitcoin-nettverket. For øyeblikket sendes transaksjoner til alle peers på en node, noe som resulterer i redundans og overforbruk av båndbredde. BIP330 foreslår å begrense denne kringkastingen til 8 peers som standard, og deretter bruke en avstemmingsmekanisme for å dele manglende transaksjoner på en effektiv måte. Erlay reduserer båndbreddeforbruket med rundt 40 %. Den unngår også en lineær økning i båndbreddeforbruket med antall peers som er koblet til noden.