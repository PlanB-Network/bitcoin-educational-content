---
term: SEED

---
Ve specifickém kontextu hierarchické deterministické peněženky Bitcoin je seed 512bitová informace odvozená z náhodnosti. Používá se k deterministickému a hierarchickému generování sady soukromých klíčů a jim odpovídajících veřejných klíčů pro peněženku Bitcoin. Semínko se často zaměňuje se samotnou frází pro obnovení. Jedná se však o odlišnou informaci. Semínko se získá použitím funkce `PBKDF2` na mnemotechnickou frázi a jakoukoli potenciální frázi.

Se zavedením BIP32 byl vynalezen seed, který definuje základy hierarchické deterministické peněženky. V tomto standardu byl seed 128 bitů. To umožňuje odvodit všechny klíče v peněžence z jediné informace, na rozdíl od peněženek JBOK (*Just a Bunch Of Keys*), které vyžadují nové zálohy pro každý generovaný klíč. BIP39 později zavedl kódování tohoto seedu, aby se zjednodušila jeho čitelnost pro člověka. Toto kódování je provedeno ve formě fráze, běžně označované jako mnemotechnická fráze nebo fráze pro obnovu. Tento standard pomáhá zabránit chybám při zálohování seedu, zejména použitím kontrolního součtu.

Obecněji řečeno, v kryptografii je semeno část náhodných dat, která se používá jako výchozí bod pro generování kryptografických klíčů, šifrování nebo pseudonáhodných posloupností. Kvalita a bezpečnost mnoha kryptografických procesů závisí na náhodnosti a důvěrnosti seedu.

> ► Český překlad slova "graine" je "semeno". Ve francouzštině se pro označení semene často používá přímo anglické slovo *