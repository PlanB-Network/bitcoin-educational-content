---
term: DAMMANDE ATTACK
---

En Dusting Attack innebär att man skickar små mängder bitcoins till ett stort antal mottagaradresser. Angriparens mål är att tvinga mottagarna att konsolidera dessa belopp med andra UTXO. Angriparen spårar sedan de framtida rörelserna för dessa små mängder bitcoins och strävar efter att bilda kluster av adresser, det vill säga att avgöra om flera adresser tillhör samma enhet. Genom att korrelera den information som samlas in under en dusting-attack med andra data och heuristik som används i kedjeanalys är det möjligt för angriparen att identifiera vissa enheter och deras associerade adresser. Denna metod utgör endast ett hot mot användarnas integritet, men påverkar inte säkerheten för deras medel.


> ► * Vissa bitcoiners föreslår att man inte längre använder termen "dusting attack" eftersom den kan vara vilseledande. Termen "Dust" beskriver faktiskt något mycket specifikt i Bitcoin Core. Om dusting-attacken faktiskt använde Dust enligt beskrivningen i Core skulle attacken vara ineffektiv. Därför föreslår vissa att man använder termen "tvingad Address-återanvändning" för att mer exakt beskriva denna attack.*