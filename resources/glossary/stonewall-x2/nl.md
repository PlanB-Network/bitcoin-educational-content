---
term: Stonewall x2
definition: Gezamenlijke transactie die een mini-coinjoin met een derde partij simuleert om de betalingsprivacy te verbeteren.
---

Een specifieke vorm van Bitcoin transactie gericht op het verhogen van de privacy van de gebruiker tijdens een uitgave, door samen te werken met een derde partij die niet betrokken is bij de uitgave. Deze methode simuleert een mini-CoinJoin tussen twee deelnemers, terwijl er een betaling wordt gedaan aan een derde partij. Stonewall x2 transacties zijn beschikbaar op zowel de Samourai Wallet app als de Sparrow wallet software (beide zijn interoperabel).


De werking is relatief eenvoudig: het gebruikt een UTXO in ons bezit om de betaling te doen en roept de hulp in van een derde partij die ook bijdraagt met een UTXO die zij bezitten. De transactie eindigt met vier uitgangen: twee van gelijke bedragen, één bestemd voor de Address van de ontvanger van de betaling, de andere voor een Address van de medewerker. Een derde UTXO wordt teruggestuurd naar een andere Address van de medewerker, waardoor zij het oorspronkelijke bedrag kunnen terugkrijgen (een neutrale actie voor hen, minus de Mining kosten), en een laatste UTXO keert terug naar een Address van ons, die het wisselgeld van de betaling vormt. Er zijn dus drie verschillende rollen gedefinieerd in Stonewall x2 transacties:


- De verzender, die de effectieve betaling uitvoert;
- De medewerker, die bitcoins levert om de algehele anonimiteit van de transactie te verbeteren, terwijl hij zijn geld aan het einde volledig terugkrijgt;
- De ontvanger is zich mogelijk niet bewust van de specifieke aard van de transactie en wacht gewoon op een betaling van de verzender.





De Stonewall x2 structuur voegt veel entropie toe aan de transactie en vertroebelt de sporen van de ketenanalyse. Van buitenaf kan zo'n transactie worden geïnterpreteerd als een kleine CoinJoin tussen twee mensen. Maar in werkelijkheid is het een betaling. Deze methode genereert dus onzekerheden in de ketenanalyse, of leidt zelfs tot valse sporen. Zelfs als een externe waarnemer erin slaagt om het patroon van de Stonewall x2 transactie te identificeren, zal hij niet over alle informatie beschikken. Ze zullen niet kunnen bepalen welke van de twee UTXO's met gelijke bedragen overeenkomt met de betaling. Bovendien zullen ze niet weten wie de betaling heeft gedaan. Tot slot kunnen ze niet bepalen of de twee ingevoerde UTXO's van twee verschillende personen afkomstig zijn of dat ze toebehoren aan één persoon die ze heeft samengevoegd. Dit laatste is te wijten aan het feit dat klassieke Stonewall transacties precies hetzelfde patroon volgen als Stonewall x2 transacties. Van buitenaf en zonder aanvullende informatie over de context is het onmogelijk om een Stonewall-transactie te onderscheiden van een Stonewall x2-transactie. De eerstgenoemde zijn echter geen collaboratieve transacties, terwijl de laatstgenoemde dat wel zijn. Dit voegt nog meer twijfel toe over de uitgaven.