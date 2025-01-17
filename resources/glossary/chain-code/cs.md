---
term: CHAIN CODE

---
V kontextu hierarchické deterministické (HD) derivace peněženek Bitcoin je řetězový kód 256bitová kryptografická hodnota soli, která se podle standardu BIP32 používá ke generování podřízených klíčů z klíče nadřazeného. Řetězový kód se používá v kombinaci s rodičovským klíčem a indexem dítěte k deterministickému generování nového páru klíčů (soukromého a veřejného klíče), aniž by byl odhalen rodičovský klíč nebo jiné odvozené dětské klíče.

Pro každou dvojici klíčů proto existuje jedinečný řetězový kód. Řetězový kód se získá buď hashováním seedu peněženky a odebráním pravé poloviny bitů. V tomto případě se označuje jako hlavní řetězový kód, spojený s hlavním soukromým klíčem. Případně jej lze získat hašováním nadřazeného klíče s jeho nadřazeným řetězovým kódem a indexem, přičemž se ponechá pravá část bitů. Pak se označuje jako podřízený řetězový kód.

Bez znalosti řetězového kódu přiřazeného ke každému rodičovskému páru nelze klíče odvodit. Do procesu odvozování zavádí pseudonáhodná data, aby bylo zajištěno, že generování kryptografických klíčů zůstane pro útočníky nepředvídatelné, zatímco pro držitele peněženky bude deterministické.

> ► V angličtině se "code de chaîne" nazývá "chain code" a "code de chaîne maître" se nazývá "master chain code".*