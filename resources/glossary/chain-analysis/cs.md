---
term: ANALÝZA ŘETĚZCE
---

Praxe, která zahrnuje všechny metody používané k sledování toku bitcoinů na blockchainu. Obecně se analýza řetězce spoléhá na pozorování charakteristik ve vzorcích předchozích transakcí. Poté zahrnuje identifikaci těchto stejných charakteristik v transakci, kterou chce někdo analyzovat, a odvození pravděpodobných interpretací. Tato metoda řešení problémů, založená na praktickém přístupu k nalezení dostatečně dobrého řešení, je známá jako heuristika. Zjednodušeně řečeno, analýza řetězce se provádí ve dvou hlavních krocích:
* Identifikace známých charakteristik;
* Odvozování hypotéz.

Jedním z cílů analýzy řetězce je seskupit různé aktivity na Bitcoinu za účelem určení jedinečnosti uživatele, který je provedl. Následně bude možné se pokusit spojit tento svazek aktivit s reálnou identitou prostřednictvím vstupního bodu. Je důležité pochopit, že analýza řetězce není přesná věda. Spoléhá na heuristiky odvozené z předchozích pozorování nebo logických interpretací. Tyto pravidla umožňují poměrně spolehlivé výsledky, ale nikdy s absolutní přesností. Jinými slovy, analýza řetězce vždy zahrnuje dimenzi pravděpodobnosti ve vyvozených závěrech. Například může být s větší či menší jistotou odhadnuto, že dvě adresy patří stejné entitě, ale úplná jistota bude vždy mimo dosah. Celý cíl analýzy řetězce spočívá přesně v agregaci různých heuristik za účelem minimalizace rizika chyby. Je to jakýsi akumulace důkazů, které nám umožňují přiblížit se k realitě. Tyto slavné heuristiky lze rozdělit do různých kategorií:
* Vzorce transakcí (nebo modely transakcí);
* Heuristiky interní k transakci;
* Heuristiky externí k transakci.

Je pozoruhodné, že první dvě heuristiky na Bitcoinu formuloval sám Satoshi Nakamoto. Představuje je v části 10 White Paperu. Je zajímavé pozorovat, že tyto dvě heuristiky si dodnes zachovávají přednostní postavení v analýze řetězce. Jsou to heuristika společného vlastnictví vstupu (CIOH) a opakované použití adresy.