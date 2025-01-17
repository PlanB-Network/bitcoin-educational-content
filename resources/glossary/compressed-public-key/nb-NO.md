---
term: KOMPRIMERT OFFENTLIG NØKKEL

---
En offentlig nøkkel brukes i skript (enten direkte i form av en offentlig nøkkel eller som en adresse) for å motta og sikre bitcoins. En rå offentlig nøkkel representeres av et punkt på en elliptisk kurve, som består av to koordinater (`x, y`) på 256 bits hver. I råformat måler en offentlig nøkkel derfor 512 bits, uten å regne med den ekstra byten som identifiserer formatet. En komprimert offentlig nøkkel er derimot en mer kompakt form for offentlig nøkkelrepresentasjon. Den bruker bare x-koordinaten og et prefiks (02 eller 03) som angir pariteten til y-koordinaten (partall eller oddetall).

Hvis vi forenkler dette til det reelle tallfeltet, gitt at den elliptiske kurven er symmetrisk i forhold til x-aksen, vil det for ethvert punkt $P$ (`x, y`) på kurven finnes et punkt $P'$ (`x, -y`) som også ligger på samme kurve. Dette betyr at for hver `x` finnes det bare to mulige verdier av `y`, positive og negative. For eksempel vil det for en gitt abscisse `x` finnes to punkter $P1$ og $P2$ på den elliptiske kurven, som deler samme abscisse, men med motsatte ordinater:

![](../../dictionnaire/assets/29.webp)

For å velge mellom de to potensielle punktene på kurven, legges det til et prefiks til `x` som angir hvilket `y` som skal velges. Denne metoden gjør det mulig å redusere størrelsen på en offentlig nøkkel fra 520 bits til bare 264 bits (8 bits prefiks + 256 bits for `x`). Denne representasjonen kalles den komprimerte formen av den offentlige nøkkelen.

I forbindelse med elliptisk kurvekryptografi bruker vi imidlertid ikke de reelle tallene, men et endelig felt av orden `p` (et primtall). I denne sammenhengen bestemmes "fortegnet" til `y` av pariteten, det vil si om `y` er partall eller oddetall. Prefikset `0x02` indikerer da et partall, mens `0x03` indikerer et oddetall.

Se på følgende eksempel på en rå offentlig nøkkel (et punkt på den elliptiske kurven) i heksadesimal:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Vi kan isolere prefikset, `x` og `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Base 16 (heksadesimal): f

Basis 10 (desimal): 15

y er oddetall

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```