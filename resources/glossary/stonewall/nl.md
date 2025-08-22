---
term: STEENWALL
---

Een specifieke vorm van Bitcoin transactie gericht op het verhogen van de privacy van gebruikers tijdens een uitgave door een CoinJoin tussen twee mensen na te bootsen, zonder er daadwerkelijk een te zijn. Deze transactie werkt niet samen. Een gebruiker kan hem alleen maken, met alleen zijn eigen UTXO's als invoer. Daarom kun je voor elke gelegenheid een Stonewall-transactie maken, zonder dat je hoeft te synchroniseren met een andere gebruiker.


De werking van de Stonewall-transactie is als volgt: bij de invoer van de transactie gebruikt de zender 2 UTXO's die bij hem horen. De transactie produceert dan 4 uitgangen, waarvan er 2 precies hetzelfde bedrag zijn. De andere 2 vormen de wijziging. Van de 2 uitgangen van hetzelfde bedrag gaat er slechts één daadwerkelijk naar de ontvanger van de betaling.


Er zijn dus slechts 2 rollen in een Stonewall-transactie:


- De verzender, die de betaling uitvoert;
- De ontvanger is zich mogelijk niet bewust van de specifieke aard van de transactie en wacht gewoon op een betaling van de verzender.


![](../../dictionnaire/assets/33.webp)

Stonewall transacties zijn beschikbaar op zowel de Samourai Wallet applicatie als de Sparrow wallet software.


De Stonewall structuur voegt veel entropie toe aan de transactie en versluiert het spoor voor ketenanalyse. Van buitenaf kan zo'n transactie worden geïnterpreteerd als een kleine CoinJoin tussen twee mensen. Maar in werkelijkheid is het, net als de Stonewall x2 transactie, een betaling. Deze methode genereert dus onzekerheden in de ketenanalyse, of leidt zelfs tot valse sporen. Zelfs als een externe waarnemer erin slaagt om het patroon van de Stonewall-transactie te identificeren, zal hij niet over alle informatie beschikken. Ze zullen niet kunnen bepalen welke van de twee UTXO's met dezelfde bedragen overeenkomt met de betaling. Bovendien zullen ze niet kunnen bepalen of de twee UTXO's bij de invoer afkomstig zijn van twee verschillende personen of dat ze toebehoren aan één persoon die ze heeft samengevoegd. Dit laatste komt doordat Stonewall x2 transacties precies hetzelfde patroon volgen als Stonewall transacties. Van buitenaf en zonder extra contextinformatie is het onmogelijk om een Stonewall-transactie te onderscheiden van een Stonewall x2-transactie. De eerstgenoemde zijn echter geen collaboratieve transacties, terwijl de laatstgenoemde dat wel zijn. Dit voegt nog meer twijfel toe over deze uitgave.