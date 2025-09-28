---
name: Boltzmann Calculator
description: Het concept entropie en het gebruik van Boltzmann begrijpen
---
![cover](assets/cover.webp)


***WAARSCHUWING:** Na de arrestatie van de oprichters van Samourai Wallet en de inbeslagname van hun servers op 24 april, is de KYCP.org website momenteel ontoegankelijk. De Gitlab die de Python Boltzmann Calculator code host is ook in beslag genomen. Vanaf nu is het niet meer mogelijk om deze tool te downloaden. Het is echter mogelijk dat de code in de komende weken door anderen opnieuw gepubliceerd wordt. In de tussentijd kun je nog steeds je voordeel doen met deze tutorial om de werking van de Boltzmann Calculator te begrijpen. De indicatoren van deze tool zijn toepasbaar op elke Bitcoin transactie en kunnen ook handmatig berekend worden. Ik zal alle benodigde berekeningen in deze tutorial geven. Als je de Python tool al had gedownload op je machine of als je een RoninDojo gebruikt, kun je de tool blijven gebruiken en deze tutorial gewoon volgen, het werkt nog steeds.*


we volgen de ontwikkelingen van deze zaak en de ontwikkelingen met betrekking tot de bijbehorende tools op de voet. Wees gerust dat we deze handleiding zullen bijwerken zodra er nieuwe informatie beschikbaar is._


deze handleiding is alleen bedoeld voor educatieve en informatieve doeleinden. We keuren het gebruik van deze tools voor criminele doeleinden niet goed en moedigen dit ook niet aan. Het is de verantwoordelijkheid van elke gebruiker om te voldoen aan de wetten in hun rechtsgebied._


---

De Boltzmann Calculator is een hulpmiddel om een Bitcoin transactie te analyseren door het entropieniveau te meten, samen met andere geavanceerde meetgegevens. Het geeft inzicht in de verbanden tussen de inputs en outputs van een transactie. Deze indicatoren bieden een gekwantificeerde beoordeling van de privacy van een transactie en helpen bij het identificeren van mogelijke fouten.


Deze Python-tool is ontwikkeld door de teams van Samourai Wallet en OXT, maar kan gebruikt worden voor elke Bitcoin transactie.


## Hoe gebruik je de Boltzmann Calculator?

Om de Boltzmann Calculator te gebruiken heb je twee opties. De eerste is om de Python tool direct op je machine te installeren. Als alternatief kun je kiezen voor de KYCP.org (_Know Your Coin Privacy_) website, die een vereenvoudigd gebruiksplatform biedt. Voor RoninDojo gebruikers: deze tool is al geïntegreerd in je node.


Het gebruik van de KYCP-site is heel eenvoudig: voer de transactie-identificatiecode (txid) die je wilt analyseren in de zoekbalk in en druk op `ENTER`.

![KYCP](assets/1.webp)

Je vindt dan verschillende informatie over de transactie, waaronder de koppelingen tussen de invoer en uitvoer. Klik op `deterministische koppelingen`.

![KYCP](assets/2.webp)

Je komt nu op de pagina die gewijd is aan de indicatoren van de Boltzmann Calculator.

![KYCP](assets/3.webp)

Voor degenen die het gereedschap liever direct vanuit hun RoninDojo node gebruiken, is het toegankelijk via `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.


Net als op de KYCP.org site hoef je alleen maar de txid van de transactie die je wilt analyseren te plakken als de Python tool is geïnstalleerd.


![KYCP](assets/7.webp)


Druk vervolgens op de `ENTER` toets om de resultaten te krijgen.


![KYCP](assets/8.webp)


## Wat zijn de indicatoren van de Boltzmann Calculator?

### Combinaties / Interpretaties:

De eerste indicator die de software berekent is het totale aantal mogelijke combinaties, aangegeven onder `nb combinaties` of `interpretaties` in de tool.


Rekening houdend met de waarden van de UTXO's die betrokken zijn bij de transactie, berekent deze indicator het aantal manieren waarop de inputs geassocieerd kunnen worden met de outputs. Met andere woorden, hij bepaalt het aantal plausibele interpretaties die een transactie kan oproepen vanuit het perspectief van een externe waarnemer die de transactie analyseert.

Bijvoorbeeld, een CoinJoin gestructureerd volgens het Whirlpool 5x5 model geeft `1.496` mogelijke combinaties: ![KYCP](assets/4.webp)

Een Whirlpool Surge Cycle 8x8 CoinJoin, daarentegen, geeft `9.934.563` mogelijke interpretaties: ![KYCP](assets/5.webp)

Daarentegen zal een meer traditionele transactie met 1 invoer en 2 uitgangen slechts een enkele interpretatie weergeven: ![KYCP](assets/6.webp)


### Entropie:

De tweede indicator die wordt berekend is de entropie van een transactie, aangeduid met `Entropie`.


In de algemene context van cryptografie en informatie is entropie een kwantitatieve maat voor de onzekerheid of onvoorspelbaarheid van een gegevensbron of een willekeurig proces. Met andere woorden, entropie is een manier om te meten hoe moeilijk informatie te voorspellen of te raden is.


In de specifieke context van ketenanalyse is entropie ook de naam van een indicator, afgeleid van Shannon entropie en [uitgevonden door LaurentMT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), die wordt berekend met de Boltzmann tool.


Als een transactie een groot aantal mogelijke combinaties heeft, is het vaak relevanter om naar de entropie ervan te verwijzen. Met deze indicator kan het gebrek aan kennis van analisten over de exacte configuratie van de transactie worden gemeten. Met andere woorden, hoe hoger de entropie, hoe moeilijker het wordt voor analisten om Bitcoin bewegingen tussen inputs en outputs te identificeren.


In de praktijk laat entropie zien of, vanuit het perspectief van een externe waarnemer, een transactie meerdere mogelijke interpretaties heeft, alleen gebaseerd op de hoeveelheden inputs en outputs, zonder rekening te houden met andere externe of interne patronen en heuristieken. Een hoge entropie staat dan gelijk aan een betere privacy voor de transactie.


Entropie wordt gedefinieerd als de binaire logaritme van het aantal mogelijke combinaties. Hier is de gebruikte formule:

```plaintext
E: the entropy of the transaction
C: the number of possible combinations for the transaction

E = log2(C)
```


In de wiskunde komt de binaire logaritme (basis-2 logaritme) overeen met de inverse bewerking van exponentiëren met 2. Met andere woorden, de binaire logaritme van `x` is de exponent waartoe `2` moet worden verheven om `x` te verkrijgen. Met andere woorden, de binaire logaritme van `x` is de exponent waartoe `2` verheven moet worden om `x` te verkrijgen. Deze indicator wordt dus uitgedrukt in bits.


Laten we het voorbeeld nemen van het berekenen van de entropie voor een CoinJoin transactie gestructureerd volgens het Whirlpool 5x5 model, dat, zoals eerder genoemd, een aantal mogelijke combinaties van `1.496` biedt:

```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```

Deze CoinJoin transactie vertoont dus een entropie van `10.5469 bits`, wat als zeer bevredigend wordt beschouwd. Hoe hoger deze waarde, hoe meer verschillende interpretaties de transactie toelaat, waardoor het niveau van privacy wordt versterkt.

Voor een 8x8 CoinJoin transactie met `9.934.563` interpretaties zou de entropie zijn:

```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```


Laten we een ander voorbeeld nemen met een meer conventionele transactie, met één invoer en twee uitgangen: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) In het geval van deze transactie is de enige mogelijke interpretatie: `(In.0) > (Out.0 ; Out.1)`. Bijgevolg is de entropie vastgesteld op `0`:

```plaintext
C = 1
E = log2(1)
E = 0 bits
```


### Efficiëntie:

De derde indicator van de Boltzmann Calculator heet `Wallet Efficiëntie`. Deze indicator beoordeelt de efficiëntie van de transactie door deze te vergelijken met de optimaal denkbare transactie in een identieke configuratie.


Dit leidt ons naar het concept van maximale entropie, dat overeenkomt met de hoogste entropie die een specifieke transactiestructuur theoretisch zou kunnen bereiken. De efficiëntie van de transactie wordt vervolgens berekend door deze maximale entropie te vergelijken met de werkelijke entropie van de geanalyseerde transactie.


De gebruikte formule is als volgt:

```plaintext
ER: the actual entropy of the transaction expressed in bits
EM: the maximum possible entropy for a given transaction structure expressed in bits
Ef: the efficiency of the transaction in bits

Ef = ER - EM
```


Bijvoorbeeld, voor een Whirlpool 5x5 type CoinJoin structuur is de maximale entropie ingesteld op `10,5469`:

```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```


Deze indicator wordt ook uitgedrukt als percentage, de formule is dan:

```plaintext
CR: the actual number of possible combinations
CM: the maximum number of possible combinations with the same structure
Ef: the efficiency expressed as a percentage

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```


Een efficiëntie van `100%` geeft dus aan dat de transactie haar potentieel voor privacy maximaliseert volgens haar structuur.


### Entropiedichtheid:

De vierde indicator is de entropiedichtheid, aangegeven op het hulpmiddel `Entropiedichtheid`. Deze geeft een beeld van de entropie ten opzichte van elke invoer of uitvoer van de transactie. Deze indicator is handig voor het evalueren en vergelijken van de efficiëntie van transacties van verschillende grootte. Om de indicator te berekenen, deel je simpelweg de totale entropie van de transactie door het totaal aantal betrokken in- en uitgangen:

```plaintext
ED: the entropy density expressed in bits
E: the entropy of the transaction expressed in bits
T: the total number of inputs and outputs in the transaction

ED = E / T
```


Laten we het voorbeeld nemen van een Whirlpool 5x5 CoinJoin:

```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```


Laten we ook de entropiedichtheid berekenen voor een Whirlpool 8x8 CoinJoin:

```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```


### Boltzmann-score:

Het vijfde stukje informatie dat de Boltzmann Calculator levert is de tabel met overeenkomende waarschijnlijkheden tussen de inputs en outputs. Deze tabel geeft, door middel van de Boltzmann score, de voorwaardelijke waarschijnlijkheid aan dat een specifieke input gerelateerd is aan een bepaalde output.


Het is dus een kwantitatieve maat voor de voorwaardelijke waarschijnlijkheid dat een associatie tussen een invoer en een uitvoer in een transactie optreedt, gebaseerd op de verhouding van het aantal gunstige voorvallen van deze gebeurtenis tot het totale aantal mogelijke voorvallen in een reeks interpretaties.


Als we het voorbeeld van een Whirlpool CoinJoin opnieuw nemen, zou de tabel met voorwaardelijke waarschijnlijkheden de kans op een verband tussen elke input en output benadrukken, wat een kwantitatieve maatstaf is voor de dubbelzinnigheid van de associaties in de transactie:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Hier kunnen we duidelijk zien dat elke invoer een gelijke kans heeft om geassocieerd te worden met elke uitvoer, wat de privacy van de transactie verbetert.

De Boltzmann score wordt berekend door het aantal interpretaties waarin een bepaalde gebeurtenis voorkomt te delen door het totale aantal beschikbare interpretaties. Dus om de score te bepalen die ingang nr. 0 associeert met uitgang nr. 3 (`512` interpretaties), wordt de volgende procedure gebruikt:

```plaintext
Interpretations (IN.0 > OUT.3) = 512
Total Interpretations = 1496
Score = 512 / 1496 = 34%
```


Als we het voorbeeld nemen van een Whirlpool 8x8 CoinJoin (piekcyclus), zou de Boltzmann tabel er als volgt uitzien:


|       | OUT.0 | OUT.1 | OUT.2 | OUT.3 | OUT.4 | OUT.5 | OUT.6 | OUT.7 |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| IN.0  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.1  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.2  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.3  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.4  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.5  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.6  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |
| IN.7  | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   | 23%   |

In het geval van een eenvoudige transactie met een enkele invoer en twee uitgangen is de situatie echter anders:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Hier is te zien dat de waarschijnlijkheid dat elke output afkomstig is van input nr. 0 `100%` is. Een lagere waarschijnlijkheid betekent dus meer privacy door de directe links tussen inputs en outputs te verdunnen.


### Deterministische koppelingen:

De zesde informatie die wordt gegeven is het aantal deterministische koppelingen, aangevuld met de verhouding van deze koppelingen. Deze indicator laat zien hoeveel verbindingen tussen de inputs en outputs in de geanalyseerde transactie onbetwistbaar zijn, met een waarschijnlijkheid van `100%`. De ratio, aan de andere kant, biedt een perspectief op het gewicht van deze deterministische links binnen de gehele set transactielinks.

Bijvoorbeeld, een Whirlpool type CoinJoin transactie heeft geen deterministische links en toont daarom een indicator en een ratio van `0%`. Omgekeerd, in onze tweede onderzochte eenvoudige transactie (met één input en twee outputs), is de indicator ingesteld op `2` en de ratio bereikt `100%`. Een nulindicator duidt dus op een uitstekende privacy door de afwezigheid van directe en onbetwistbare links tussen inputs en outputs.


**Externe bronnen:**



- Boltzmann-code op Samourai
- [Bitcoin Transacties & Privacy (Deel I) door Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin Transacties & Privacy (Deel II) door Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin Transacties & Privacy (Deel III) door Laurent MT](https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP-website
- [Medium-artikel over een inleiding tot het script van Boltzmann door Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)