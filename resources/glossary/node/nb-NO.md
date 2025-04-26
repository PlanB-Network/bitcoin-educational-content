---
term: NODE

---
I Bitcoin-nettverket er en node (eller "node" på engelsk) en datamaskin som kjører en Bitcoin-protokollklient (som for eksempel Bitcoin Core). Den deltar i nettverket ved å vedlikeholde en kopi av blokkjeden, videreformidle og verifisere transaksjoner og nye blokker, og eventuelt delta i utvinningsprosessen. Summen av alle Bitcoin-noder representerer selve Bitcoin-nettverket.

Det finnes flere typer noder i Bitcoin, blant annet fullnoder og lysnoder. Fullstendige noder oppbevarer en fullstendig kopi av blokkjeden, verifiserer alle transaksjoner og blokker i henhold til konsensusregler, og deltar aktivt i spredningen av transaksjoner og blokker i nettverket. Light-noder, eller SPV-noder (*Simple Payment Verification*), oppbevarer derimot bare overskriftene til blokkene og er avhengige av fullstendige noder for å få tak i transaksjonsinformasjon.

> noen skiller også mellom såkalte "pruned nodes" ("beskjærte noder" på engelsk). Dette er fullstendige noder som laster ned og verifiserer alle blokker fra Genesis-blokken, men som bare beholder de nyeste blokkene i minnet