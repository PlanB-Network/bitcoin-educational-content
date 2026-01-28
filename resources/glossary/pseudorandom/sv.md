---
term: Pseudoslumptalsmässig
definition: Sekvens av nummer genererad deterministiskt med egenskaper nära slumpmässighet.
---

Detta adjektiv används för att beskriva en talföljd som, trots att den är resultatet av en deterministisk process, uppvisar egenskaper som ligger nära egenskaperna hos en idealisk, verkligt slumpmässig talföljd. Begreppet idealisk slumpmässighet innebär en total avsaknad av förutsägbarhet och korrelation mellan på varandra följande Elements. Ett pseudoslumpmässigt tal genereras av en deterministisk algoritm och är därför i teorin helt förutsägbart om man känner till generatorns initiala tillstånd.


En pseudoslumptalsgenerator (PRNG) är en algoritm som används för att producera sådana tal. Den utgår i allmänhet från ett startvärde, eller "seed", och tillämpar sedan en serie matematiska omvandlingar för att producera talsekvensen. På grund av denna bestämbarhet är det viktigt för kryptografisk säkerhet att det initiala seed förblir hemligt. Pseudoslumpmässiga sekvenser används ofta inom olika områden, bland annat kryptografi, eftersom de uppvisar ett till synes slumpmässigt beteende som är tillräckligt för många tillämpningar. Utvärderingen av en PRNG:s kvalitet baseras på i vilken utsträckning dess utdata närmar sig sann slumpmässighet när det gäller distribution, korrelationer och andra statistiska egenskaper. I samband med Bitcoin används pseudoslumpmässiga tal för att producera privata nycklar, eller för generate och seed för deterministiska och hierarkiska plånböcker.