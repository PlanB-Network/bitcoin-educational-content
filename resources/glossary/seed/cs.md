---
term: SEED
---

V konkrétním kontextu hierarchické deterministické Bitcoin peněženky je seed 512-bitový údaj odvozený z náhodnosti. Používá se k deterministickému a hierarchickému generování sady soukromých klíčů a jejich odpovídajících veřejných klíčů pro Bitcoin peněženku. Seed je často zaměňován s obnovovací frází. Nicméně, jde o odlišný údaj. Seed je získán aplikací funkce `PBKDF2` na mnemonickou frázi a jakékoli potenciální heslo.

Seed byl vynalezen s představením BIP32, který definuje základy hierarchické deterministické peněženky. V tomto standardu byl seed 128 bitů. To umožňuje odvození všech klíčů v peněžence z jediného údaje, na rozdíl od JBOK (*Just a Bunch Of Keys*) peněženek, které vyžadují nové zálohy pro každý generovaný klíč. BIP39 později představil kódování tohoto seedu, aby se zjednodušila jeho čitelnost pro lidi. Toto kódování je provedeno ve formě fráze, běžně označované jako mnemonická fráze nebo obnovovací fráze. Tento standard pomáhá předcházet chybám při zálohování seedu, zejména prostřednictvím použití kontrolního součtu.

Obecněji, v kryptografii, je seed kus náhodných dat použitých jako výchozí bod pro generování kryptografických klíčů, šifrování nebo pseudo-náhodných sekvencí. Kvalita a bezpečnost mnoha kryptografických procesů závisí na náhodnosti a důvěrnosti seedu.

> ► *Anglický překlad slova "graine" je "seed". Ve francouzštině mnozí přímo používají anglické slovo pro označení seedu.*