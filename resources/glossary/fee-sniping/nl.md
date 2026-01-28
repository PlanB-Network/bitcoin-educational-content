---
term: Fee sniping
definition: Aanval waarbij miners een recent blok herschrijven om de hoge transactiekosten ervan te innen.
---

Een aanvalsscenario waarbij miners een recent bevestigd blok proberen te herschrijven om de transactiekosten die het blok bevat op te eisen, terwijl ze transacties met hoge kosten toevoegen die ondertussen in de Mempool zijn binnengekomen. Het uiteindelijke doel van deze aanval voor de Miner is om hun winstgevendheid te verhogen. Fee sniping kan steeds winstgevender worden naarmate de Block reward afneemt en transactievergoedingen een groter deel van de inkomsten van miners uitmaken. Het kan ook voordelig zijn als de vergoedingen in het vorige blok aanzienlijk hoger zijn dan die in het volgende beste kandidaatblok. Ter vereenvoudiging, de Miner wordt geconfronteerd met deze keuze in termen van stimulansen:


- Mijn op een normale manier na het laatste blok, met een grote kans op het winnen van een lage beloning;
- Probeer een vorig blok te mijnen (fee sniping), met een lage kans op een hoge beloning.


Deze aanval vormt een risico voor het Bitcoin systeem, want hoe meer mijnwerkers het toepassen, hoe meer andere, aanvankelijk eerlijke, mijnwerkers gestimuleerd worden om hetzelfde te doen. Elke keer dat een nieuwe Miner zich aansluit bij degenen die fee sniping proberen, neemt de kans toe dat een van de aanvallende miners slaagt, en de kans dat een van de eerlijke miners de keten uitbreidt, neemt in ruil af. Als deze aanval massaal wordt uitgevoerd en volgehouden, neemt de kans toe dat een van de eerlijke miners de keten uitbreidt. Als deze aanval massaal en langdurig wordt uitgevoerd, zouden blokbevestigingen niet langer een betrouwbare indicator zijn van de onveranderlijkheid van een Bitcoin transactie. Dit zou het systeem onbruikbaar kunnen maken.


Om dit risico tegen te gaan, vult de meeste Wallet software automatisch het `nLocktime` veld in, zodat het de validatie van de transactie afhankelijk maakt van opname in de volgende blokhoogte. Zo wordt het onmogelijk om de transactie op te nemen in een herschrijving van het vorige blok. Als het wijdverspreide gebruik van `nLocktime` wordt overgenomen door Bitcoin gebruikers, vermindert het de stimulans voor fee sniping aanzienlijk. Sterker nog, het moedigt de voortgang van de Blockchain aan in plaats van het herschrijven ervan, door de potentiële winsten ervan te verminderen. Voor Taproot transacties stelt BIP326 voor om het `nSequence` veld op een vergelijkbare manier te gebruiken om hetzelfde effect te bereiken als het `nLocktime` veld voor andere typen transacties. Dit gebruik zou twee vliegen in één klap slaan door ook de privacy te verbeteren van tweede Layer protocollen die hetzelfde veld gebruiken.