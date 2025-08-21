---
term: TRANSACTIE (TX)
---

In de context van Bitcoin is een transactie (afgekort als "TX") een operatie die wordt geregistreerd op de Blockchain die de Ownership van bitcoins van een of meer ingangen naar een of meer uitgangen overbrengt. Elke transactie verbruikt UTXO's (Unspent Transaction Outputs) als inputs, die outputs zijn van eerdere transacties, en creëert nieuwe UTXO's als outputs, die kunnen worden gebruikt als inputs in toekomstige transacties.


Elke invoer bevat een verwijzing naar een bestaande uitvoer samen met een handtekeningscript (`scriptSig`) dat voldoet aan de bestedingsvoorwaarden (`scriptPubKey`) die zijn vastgesteld door de uitvoer waarnaar wordt verwezen. Hierdoor kunnen bitcoins worden ontgrendeld. De uitgangen definiëren nieuwe bestedingsvoorwaarden (`scriptPubKey`) voor de overgedragen bitcoins, vaak in de vorm van een publieke sleutel of een Address waaraan de bitcoins nu zijn gekoppeld.