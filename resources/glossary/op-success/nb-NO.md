---
term: OP_SUCCESS

---
OP_SUCCESS representerer en rekke opkoder som tidligere har vært deaktivert, og som nå er reservert for fremtidig bruk i Tapscript. Målet er å gjøre det enklere å oppdatere og utvide skriptspråket ved å tillate innføring av nye funksjoner via soft forks. Når en av disse opkodene dukker opp i et skript, betyr det at den delen av skriptet automatisk er fullført, uavhengig av hvilke data eller betingelser som er til stede. Dette betyr at skriptet fortsetter kjøringen uten feil, uavhengig av tidligere operasjoner.

Når en ny opcode legges til på en `OP_SUCCESS`, representerer det nødvendigvis en mer restriktiv regel enn den forrige. Oppdaterte noder kan da verifisere at denne regelen overholdes, og noder som ikke er oppdatert, vil ikke nekte de tilknyttede transaksjonene og blokkene som inkluderer dem, fordi `OP_SUCCESS` validerer den delen av skriptet. Derfor er det ingen hard fork.

Til sammenligning fungerer `OP_NOP` (*No Operation*) også som plassholdere i skriptet, men de har ingen innvirkning på utførelsen av skriptet. Når en `OP_NOP` oppstår, fortsetter skriptet ganske enkelt uten å endre stakkens tilstand eller skriptets progresjon. Hovedforskjellen ligger derfor i deres innvirkning på kjøringen: `OP_SUCCESS` garanterer en vellykket passering gjennom den aktuelle delen av skriptet, mens `OP_NOP` er nøytral og ikke påvirker verken stakken eller skriptets flyt. Disse opkodene betegnes med `OP_SUCCESSN`, der `N` er et tall som brukes til å skille mellom `OP_SUCCESS`.