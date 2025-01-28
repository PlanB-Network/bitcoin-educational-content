---
term: KOMPRIMOVANÝ VEŘEJNÝ KLÍČ

---
Veřejný klíč se používá ve skriptech (buď přímo ve formě veřejného klíče, nebo jako adresa) k přijímání a zabezpečení bitcoinů. Nezpracovaný veřejný klíč je reprezentován bodem na eliptické křivce, který se skládá ze dvou souřadnic (`x, y`), z nichž každá má 256 bitů. V surovém formátu tedy veřejný klíč měří 512 bitů, nepočítaje další bajt pro identifikaci formátu. Naproti tomu komprimovaný veřejný klíč je kompaktnější formou reprezentace veřejného klíče. Používá pouze souřadnici `x` a předponu (`02` nebo `03`), která označuje paritu souřadnice `y` (sudá nebo lichá).

Zjednodušíme-li to na obor reálných čísel, pak za předpokladu, že eliptická křivka je symetrická vzhledem k ose x, pro libovolný bod $P$ (`x, y`) na křivce existuje bod $P'$ (`x, -y`), který bude také na téže křivce. To znamená, že pro každé `x` existují pouze dvě možné hodnoty `y`, kladná a záporná. Například pro danou abscisu `x` budou na eliptické křivce existovat dva body $P1$ a $P2$, které budou mít stejnou abscisu, ale opačné ordináty:

![](../../dictionnaire/assets/29.webp)

Pro výběr mezi dvěma potenciálními body na křivce se k `x` přidá předpona určující, který `y` se má vybrat. Tato metoda umožňuje snížit velikost veřejného klíče z 520 bitů na pouhých 264 bitů (8 bitů prefixu + 256 bitů pro `x`). Tato reprezentace je známá jako komprimovaná forma veřejného klíče.

V kontextu kryptografie eliptických křivek však nepoužíváme reálná čísla, ale konečné pole řádu `p` (prvočíslo). V tomto kontextu je "znaménko" `y` určeno jeho paritou, tj. zda je `y` sudé nebo liché. Předpona `0x02` pak označuje sudé `y`, zatímco `0x03` označuje liché `y`.

Uvažujme následující příklad nezpracovaného veřejného klíče (bod na eliptické křivce) v hexadecimálním tvaru:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Můžeme oddělit prefix `x` a `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Základna 16 (hexadecimální): f

Základ 10 (desetinné číslo): 15

y je liché

```
The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```