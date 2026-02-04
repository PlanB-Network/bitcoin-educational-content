---
term: Eltoo
definition: Protokoll som förenklar hanteringen av Lightning-kanaltillstånd med en linjär uppdateringsmetod.
---

Ett allmänt protokoll för Bitcoin:s andra lager som definierar hur man gemensamt hanterar Ownership i en UTXO. Eltoo designades av Christian Decker, Rusty Russell och Olaoluwa Osuntokun, i synnerhet för att lösa problemen med förhandlingsmekanismerna för Lightning channel states, det vill säga mellan öppning och stängning. Eltoo-arkitekturen förenklar förhandlingsprocessen genom att införa ett linjärt system för tillståndshantering, som ersätter det etablerade straffbaserade tillvägagångssättet med en mer flexibel och mindre straffande uppdateringsmetod. Detta protokoll kräver användning av en ny typ av SigHash som gör det möjligt att ignorera alla indata i signaturen för en transaktion. Denna SigHash kallades ursprungligen `SIGHASH_NOINPUT`, sedan `SIGHASH_ANYPREVOUT` (*Any Previous Output*). Implementeringen är planerad i BIP118.


> ► *Eltoo kallas ibland också för "LN-Symmetry" *