---
term: Forcerad adressåteranvändning
definition: Attack som skickar små belopp för att spåra transaktioner och identifiera adressinnehavare.
---

En attack som innebär att små mängder bitcoins skickas till ett stort antal mottagaradresser. Angriparens mål är att tvinga mottagarna att konsolidera dessa belopp med andra UTXO:er. Angriparen spårar sedan de framtida rörelserna för dessa små mängder bitcoins och strävar efter att bilda kluster av adresser, det vill säga att avgöra om flera adresser tillhör samma enhet. Genom att korsreferera den information som samlats in under attacken med andra data och heuristik som används i kedjeanalys är det möjligt för angriparen att identifiera vissa enheter och deras associerade adresser. Denna metod utgör endast ett hot mot användarnas integritet, men påverkar inte säkerheten för deras medel.


> ► * Den ursprungliga termen för att beskriva denna attack är "Dusting Attack", men vissa bitcoiners föreslår att man använder termen "tvingad Address-återanvändning", eftersom de anser att termen "Dust" är olämplig här.*