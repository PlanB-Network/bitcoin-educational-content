---
term: KOMPRIMOVANÝ VEŘEJNÝ KLÍČ
---

Veřejný klíč se používá ve skriptech (buď přímo ve formě veřejného klíče nebo jako adresa) pro přijímání a zabezpečení bitcoinů. Nezpracovaný veřejný klíč je reprezentován bodem na eliptické křivce, skládající se ze dvou souřadnic (`x, y`), každá o 256 bitech. V nezpracovaném formátu má tedy veřejný klíč 512 bitů, nepočítaje dodatečný bajt pro identifikaci formátu. Komprimovaný veřejný klíč je naopak kompaktnější forma reprezentace veřejného klíče. Používá pouze souřadnici `x` a předponu (`02` nebo `03`), která udává paritu souřadnice `y` (sudou nebo lichou).

Pokud to zjednodušíme na pole reálných čísel, vzhledem k tomu, že eliptická křivka je symetrická vzhledem k ose x, pro každý bod $P$ (`x, y`) na křivce existuje bod $P'$ (`x, -y`), který bude také na této stejné křivce. To znamená, že pro každé `x` existují pouze dvě možné hodnoty `y`, kladné a záporné. Například pro danou souřadnici `x` by na eliptické křivce byly dva body $P1$ a $P2$, které sdílejí stejnou souřadnici, ale mají opačné souřadnice:

![](../../dictionnaire/assets/29.png)
Pro výběr mezi dvěma potenciálními body na křivce se k `x` přidá předpona specifikující, které `y` vybrat. Tato metoda umožňuje snížit velikost veřejného klíče z 520 bitů na pouhých 264 bitů (8 bitů předpony + 256 bitů pro `x`). Tato reprezentace je známá jako komprimovaná forma veřejného klíče.

Nicméně, v kontextu kryptografie s eliptickými křivkami, nepoužíváme reálná čísla, ale konečné pole řádu `p` (prvočíslo). V tomto kontextu je "znaménko" `y` určeno jeho paritou, tj. zda je `y` sudé nebo liché. Předpona `0x02` pak označuje sudé `y`, zatímco `0x03` označuje liché `y`.

Uvažujme následující příklad nezpracovaného veřejného klíče (bod na eliptické křivce) v hexadecimálním zápisu:
```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```

Můžeme izolovat předponu, `x` a `y`:
```plaintext
Předpona = 04
Pro určení parity `y` zkoumáme poslední hexadecimální znak `y`:
```plaintext
Základ 16 (hexadecimální): f
Základ 10 (decimální): 15
y je liché
```

Předpona pro komprimovaný veřejný klíč bude `03`. Komprimovaný veřejný klíč v hexadecimálním zápisu se stává:
```plaintext
K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6
```