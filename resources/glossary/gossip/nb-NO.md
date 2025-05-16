---
term: GOSSIP
---

Gossip er en distribuert algoritme for peer-to-peer (P2P) som sprer informasjon epidemisk til alle nettverksagenter. For Bitcoin, Lightning og andre distribuerte systemer gjør denne protokollen det mulig å utveksle og synkronisere nodenes Global State på bare noen få sykluser. Hver node sprer informasjon til en eller flere tilfeldige eller ikke-tilfeldige naboer, som i sin tur sprer informasjonen til andre naboer, og så videre, helt til en globalt synkronisert tilstand er nådd.


I Lightning er gossip en kommunikasjonsprotokoll mellom noder for å dele informasjon om nettverkets nåværende tilstand og topologi. Sladreprotokollen gjør det mulig for noder å kjenne til den dynamiske tilstanden til betalingskanaler og andre noder, slik at det blir enklere å dirigere transaksjoner gjennom nettverket uten at det kreves direkte forbindelser mellom alle noder.


> ► *På fransk kan "sladreprotokoll" oversettes med "protocole de bavardage". Kilde: https://dl.acm.org/doi/pdf/10.1145/41840.41841.*