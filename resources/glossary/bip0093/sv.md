---
term: BIP0093
definition: Codex32-standard som gör det möjligt att säkerhetskopiera ett frö (seed) genom att dela upp det i flera delar via Shamirs hemliga delning.
---

Informational BIP som föreslår en standard för att spara och återställa seed för en hierarkisk deterministisk portfölj (enligt BIP32) med hjälp av Shamirs hemliga nyckeldelning. Detta protokoll definierar "codex32"-formatet, som är inspirerat av bech32-formatet, genom att införa en strukturerad sträng som består av ett prefix, en tröskelparameter, en identifierare, ett delningsindex, en nyttolast och en kontrollsumma (BCH). Metoden gör det möjligt att dela upp seed i upp till 31 delar, av vilka ett definierat tröskelvärde (mellan 1 och 9) krävs för fullständig återställning av seed.