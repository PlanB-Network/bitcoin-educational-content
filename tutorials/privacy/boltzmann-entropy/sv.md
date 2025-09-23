---
name: Boltzmann Calculator
description: Förstå begreppet entropi och hur man använder Boltzmann
---
![cover](assets/cover.webp)


*** VARNING:** Efter gripandet av grundarna av Samourai Wallet och beslagtagandet av deras servrar den 24 april är webbplatsen KYCP.org för närvarande otillgänglig. Gitlab som är värd för Python Boltzmann Calculator-koden har också beslagtagits. Från och med nu är det inte längre möjligt att ladda ner detta verktyg. Det är dock möjligt att koden kan återpubliceras av andra under de kommande veckorna. Under tiden kan du fortfarande dra nytta av den här handledningen för att förstå hur Boltzmann Calculator fungerar. De indikatorer som tillhandahålls av detta verktyg är tillämpliga på alla Bitcoin-transaktioner och kan också beräknas manuellt. Jag kommer att tillhandahålla alla nödvändiga beräkningar i denna handledning. Om du redan hade laddat ner Python-verktyget på din maskin eller om du använder en RoninDojo, kan du fortsätta att använda verktyget och följa denna handledning som vanligt, det fungerar fortfarande.*


_Vi följer noga utvecklingen av detta fall och utvecklingen av de tillhörande verktygen. Du kan vara säker på att vi kommer att uppdatera denna handledning när ny information blir tillgänglig._


_Den här handledningen tillhandahålls endast i utbildnings- och informationssyfte. Vi varken stödjer eller uppmuntrar användning av dessa verktyg i kriminella syften. Det är varje användares ansvar att följa de lagar som gäller i deras jurisdiktion._


---

Boltzmann Calculator är ett verktyg för att analysera en Bitcoin-transaktion genom att mäta dess entropinivå tillsammans med andra avancerade mätvärden. Det ger insikter i kopplingarna mellan inmatningar och utmatningar i en transaktion. Dessa indikatorer ger en kvantifierad bedömning av en transaktions integritet och hjälper till att identifiera potentiella fel.


Detta Python-verktyg utvecklades av teamen på Samourai Wallet och OXT, men det kan användas på alla Bitcoin-transaktioner.


## Hur använder man Boltzmann-kalkylatorn?

För att använda Boltzmann Calculator finns det två alternativ. Det första är att installera Python-verktyget direkt på din maskin. Alternativt kan du välja webbplatsen KYCP.org (_Know Your Coin Privacy_), som erbjuder en förenklad användningsplattform. För RoninDojo-användare, notera att det här verktyget redan är integrerat i din nod.


Att använda KYCP-webbplatsen är ganska enkelt: ange bara den transaktionsidentifierare (txid) som du vill analysera i sökfältet och tryck på `ENTER`.

![KYCP](assets/1.webp)

Du kommer då att hitta olika uppgifter om transaktionen, inklusive länkarna mellan inputs och outputs. Klicka på `deterministiska länkar`.

![KYCP](assets/2.webp)

Du kommer att komma till sidan för Boltzmann Calculator-indikatorerna.

![KYCP](assets/3.webp)

För dem som föredrar att använda verktyget direkt från sin RoninDojo-nod är det tillgängligt via `RoninCLI > Samourai Toolkit > Boltzmann Calculator`.


Precis som på KYCP.org-webbplatsen behöver du bara klistra in txid för den transaktion du vill analysera när Python-verktyget har installerats.


![KYCP](assets/7.webp)


Tryck sedan på tangenten `ENTER` för att få resultaten.


![KYCP](assets/8.webp)


## Vilka är indikatorerna för Boltzmannkalkylatorn?

### Kombinationer / Tolkningar:

Den första indikatorn som programmet beräknar är det totala antalet möjliga kombinationer, som anges under "kombinationer" eller "tolkningar" i verktyget.


Med hänsyn till värdena för de UTXO:er som är involverade i transaktionen beräknar denna indikator antalet sätt på vilka ingångarna kan associeras med utgångarna. Med andra ord avgörs antalet rimliga tolkningar som en transaktion kan ge upphov till från en extern observatörs perspektiv som analyserar den.

Till exempel, en CoinJoin strukturerad enligt Whirlpool 5x5 modellen ger `1,496` möjliga kombinationer: ![KYCP](assets/4.webp)

En Whirlpool Surge Cycle 8x8 CoinJoin, å andra sidan, presenterar `9,934,563` möjliga tolkningar: ![KYCP](assets/5.webp)

Däremot kommer en mer traditionell transaktion med 1 ingång och 2 utgångar bara att ge en enda tolkning: ![KYCP](assets/6.webp)


### Entropi:

Den andra indikatorn som beräknas är entropin för en transaktion, betecknad med "entropi".


När det gäller kryptografi och information är entropi ett kvantitativt mått på den osäkerhet eller oförutsägbarhet som är förknippad med en datakälla eller en slumpmässig process. Med andra ord är entropi ett sätt att mäta hur svårt det är att förutsäga eller gissa sig till information.


I det specifika sammanhanget med kedjeanalys är entropi också namnet på en indikator, härledd från Shannon-entropi och [uppfunnen av LaurentMT] (https://gist.github.com/LaurentMT/e758767ca4038ac40aaf), som beräknas med Boltzmann-verktyget.


När en transaktion uppvisar ett stort antal möjliga kombinationer är det ofta mer relevant att hänvisa till dess entropi. Denna indikator gör det möjligt att mäta analytikernas brist på kunskap om transaktionens exakta konfiguration. Med andra ord, ju högre entropi, desto svårare blir uppgiften att identifiera Bitcoin-rörelser mellan in- och utgångar för analytikerna.


I praktiken visar entropin om en transaktion, ur en extern observatörs perspektiv, ger flera möjliga tolkningar, enbart baserat på mängden in- och utdata, utan att ta hänsyn till andra externa eller interna mönster och heuristiker. Hög entropi är då synonymt med bättre integritet för transaktionen.


Entropi definieras som den binära logaritmen av antalet möjliga kombinationer. Här är den formel som används:

```plaintext
E: the entropy of the transaction
C: the number of possible combinations for the transaction

E = log2(C)
```


Inom matematiken motsvarar den binära logaritmen (bas-2-logaritmen) den omvända operationen av exponentiering av 2. Med andra ord är den binära logaritmen för `x` den exponent som `2` måste höjas till för att erhålla `x`. Denna indikator uttrycks alltså i bitar.


Låt oss ta exemplet att beräkna entropin för en CoinJoin-transaktion som är strukturerad enligt Whirlpool 5x5-modellen, som, som tidigare nämnts, erbjuder ett antal möjliga kombinationer på "1 496":

```plaintext
C = 1,496
E = log2(1,496)
E = 10.5469 bits
```

Således visar denna CoinJoin-transaktion en entropi på "10,5469 bitar", vilket anses vara mycket tillfredsställande. Ju högre detta värde är, desto fler olika tolkningar medger transaktionen, vilket stärker dess sekretessnivå.

För en 8x8 CoinJoin-transaktion som presenterar `9 934 563` tolkningar skulle entropin vara:

```plaintext
C = 9,934,563
E = log2(9,934,563)
E = 23.244 bits
```


Låt oss ta ett annat exempel med en mer konventionell transaktion, med en ingång och två utgångar: [1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce](https://Mempool.space/tx/1b1b0c3f0883a99f1161c64da19471841ed12a1f78e77fab128c69a5f578ccce) I fallet med denna transaktion är den enda möjliga tolkningen: `(In.0) > (Out.0 ; Out.1)`. Följaktligen är dess entropi fastställd till `0`:

```plaintext
C = 1
E = log2(1)
E = 0 bits
```


### Effektivitet:

Den tredje indikatorn som tillhandahålls av Boltzmann Calculator kallas "Wallet Efficiency". Denna indikator bedömer transaktionens effektivitet genom att jämföra den med den optimala transaktion som kan tänkas i en identisk konfiguration.


Detta leder oss till att diskutera begreppet maximal entropi, vilket motsvarar den högsta entropi som en specifik transaktionsstruktur teoretiskt skulle kunna uppnå. Transaktionens effektivitet beräknas sedan genom att denna maximala entropi konfronteras med den faktiska entropin i den analyserade transaktionen.


Formeln som används är följande:

```plaintext
ER: the actual entropy of the transaction expressed in bits
EM: the maximum possible entropy for a given transaction structure expressed in bits
Ef: the efficiency of the transaction in bits

Ef = ER - EM
```


Till exempel, för en Whirlpool 5x5 typ CoinJoin struktur, är den maximala entropin satt till `10,5469`:

```plaintext
ER = 10.5469
EM = 10.5469
Ef = 10.5469 - 10.5469 = 0 bits
```


Denna indikator uttrycks också som en procentsats och dess formel är då:

```plaintext
CR: the actual number of possible combinations
CM: the maximum number of possible combinations with the same structure
Ef: the efficiency expressed as a percentage

Ef = CR / CM
Ef = 1,496 / 1,496
Ef = 100%
```


En effektivitet på "100%" innebär således att transaktionen maximerar sin integritetspotential i enlighet med sin struktur.


### Entropidensitet:

Den fjärde indikatorn är entropidensiteten, som anges i verktyget `Entropy Density`. Den ger ett perspektiv på entropin i förhållande till varje in- eller utdata i transaktionen. Denna indikator är användbar för att utvärdera och jämföra effektiviteten i transaktioner av olika storlek. För att beräkna den dividerar du helt enkelt transaktionens totala entropi med det totala antalet in- och utgångar som är inblandade:

```plaintext
ED: the entropy density expressed in bits
E: the entropy of the transaction expressed in bits
T: the total number of inputs and outputs in the transaction

ED = E / T
```


Låt oss ta exemplet med en Whirlpool 5x5 CoinJoin:

```plaintext
T = 5 + 5 = 10
E = 10.5469
ED = 10.5469 / 10 = 1.054 bits
```


Låt oss också beräkna entropidensiteten för en Whirlpool 8x8 CoinJoin:

```plaintext
T = 8 + 8 = 16
E = 23.244
ED = 23.244 / 16 = 1.453 bits
```


### Boltzmanns poäng:

Den femte delen av informationen som Boltzmann Calculator levererar är tabellen över matchande sannolikheter mellan input och output. Denna tabell anger, genom Boltzmann-poängen, den villkorliga sannolikheten för att en specifik input är relaterad till en given output.


Det är således ett kvantitativt mått på den villkorliga sannolikheten för att ett samband mellan en input och en output i en transaktion inträffar, baserat på förhållandet mellan antalet gynnsamma händelser av denna händelse och det totala antalet möjliga händelser, i en uppsättning tolkningar.


Om vi tar exemplet med en Whirlpool CoinJoin igen, skulle tabellen över villkorliga sannolikheter belysa chanserna för koppling mellan varje input och output, vilket ger ett kvantitativt mått på tvetydigheten i transaktionens associationer:


| %       | Output 0 | Output 1 | Output 2 | Output 3 | Output 4 |
| ------- | -------- | -------- | -------- | -------- | -------- |
| Input 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Input 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Här kan vi tydligt se att varje inmatning har lika stor chans att associeras med varje utmatning, vilket ökar transaktionens integritet.

Beräkningen av Boltzmannpoängen innebär att antalet tolkningar i vilka en viss händelse inträffar divideras med det totala antalet tillgängliga tolkningar. För att bestämma den poäng som associerar ingång nr 0 med utgång nr 3 (`512` tolkningar) används således följande procedur:

```plaintext
Interpretations (IN.0 > OUT.3) = 512
Total Interpretations = 1496
Score = 512 / 1496 = 34%
```


Om vi tar exemplet med en Whirlpool 8x8 CoinJoin (surge cycle) skulle Boltzmann-tabellen se ut så här:


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

När det gäller en enkel transaktion med en enda inmatning och två utmatningar är situationen emellertid en annan:


| %       | Output 0 | Output 1 |
|---------|----------|----------|
| Input 0 | 100%     | 100%     |

Här kan man se att sannolikheten för att varje output härrör från input nr 0 är "100 %". En lägre sannolikhet innebär alltså större integritet genom att de direkta kopplingarna mellan inmatning och utmatning försvagas.


### Deterministiska länkar:

Den sjätte informationen är antalet deterministiska länkar, kompletterat med förhållandet mellan dessa länkar. Denna indikator visar hur många kopplingar mellan inputs och outputs i den analyserade transaktionen som är odiskutabla, med en sannolikhet på "100%". Förhållandet å andra sidan ger ett perspektiv på vikten av dessa deterministiska länkar inom hela uppsättningen av transaktionslänkar.

En CoinJoin-transaktion av typen Whirlpool har t.ex. inga deterministiska länkar och visar därför en indikator och ett förhållande på "0 %". I den andra enkla transaktionen som vi undersökte (med en ingång och två utgångar) är indikatorn däremot satt till "2" och kvoten når "100 %". En nollindikator signalerar således utmärkt integritet på grund av avsaknaden av direkta och obestridliga kopplingar mellan in- och utdata.


**Externa resurser:**



- Boltzmann-kod på Samourai
- [Bitcoin Transaktioner och integritet (del I) av Laurent MT](https://gist.github.com/LaurentMT/e758767ca4038ac40aaf)
- [Bitcoin Transaktioner och integritet (del II) av Laurent MT](https://gist.github.com/LaurentMT/d361bca6dc52868573a2)
- [Bitcoin Transaktioner och integritet (del III) av Laurent MT] (https://gist.github.com/LaurentMT/e8644d5bc903f02613c6)
- KYCP:s webbplats
- [Medium Article on an Introduction to Boltzmann Script by Laurent MT](https://medium.com/@laurentmt/introducing-boltzmann-85930984a159)