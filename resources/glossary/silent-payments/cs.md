---
term: SILENT PAYMENTS
---

Metoda používání statických Bitcoinových adres pro přijímání plateb bez opakovaného použití adresy, bez interakce a bez viditelného on-chain spojení mezi různými platbami a statickou adresou. Tato technika eliminuje potřebu generovat nové, nepoužité přijímací adresy pro každou transakci, čímž se vyhýbá obvyklým interakcím v Bitcoinu, kde musí příjemce poskytnout novou adresu platícímu.

U Silent Payments platící používá veřejné klíče příjemce (veřejný klíč pro utrácení a veřejný klíč pro skenování) a součet svých vlastních soukromých klíčů jako vstup pro generování nové adresy pro každou platbu. Pouze příjemce, se svými soukromými klíči, může vypočítat soukromý klíč odpovídající této platební adrese. ECDH (*Elliptic-Curve Diffie-Hellman*), algoritmus pro výměnu kryptografických klíčů, je použit k vytvoření sdíleného tajemství, které je poté použito k odvození přijímací adresy a soukromého klíče (pouze na straně příjemce). Aby identifikovali Silent Payments určené pro ně, musí příjemci prohledávat blockchain a zkoumat každou transakci odpovídající kritériím protokolu. Na rozdíl od BIP47, který používá notifikační transakci pro zřízení platebního kanálu, Silent Payments tento krok eliminují, čímž se ušetří transakce. Kompromisem je však, že příjemce musí prohledat všechny potenciální transakce, aby určil, aplikací ECDH, zda jsou na ně adresovány.

Například Bobova statická adresa $B$ reprezentuje konkatenaci jeho veřejného klíče pro skenování a jeho veřejného klíče pro utrácení:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$

Tyto klíče jsou jednoduše odvozeny z následující cesty:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Tuto statickou adresu zveřejní Bob. Alice ji získá, aby mohla Bobovi poslat Silent Payment. Alice vypočítá Bobovu platební adresu $P_0$ tímto způsobem:

$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G  $$

Kde:

$$  \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A)  $$

S:
* $B_{\text{scan}}$: Bobův veřejný klíč pro skenování (statická adresa);
* $B_{\text{spend}}$: Bobův veřejný klíč pro utrácení (statická adresa);
* $A$: Součet veřejných klíčů ve vstupu (úprava);
* $a$: Soukromý klíč úpravy, tj. součet všech párů klíčů použitých v `scriptPubKey` UTXO spotřebovaných jako vstupy v Alicině transakci;
* $\text{outpoint}_L$: Nejmenší UTXO (lexikograficky) použité jako vstup v Alicině transakci;
* $\text{ ‖ }$: Konkatenace (operace spojení operandů konec s koncem);
* $G$: Generátorový bod eliptické křivky `secp256k1`;
* $\text{hash}$: SHA256 hash funkce označená s `BIP0352/SharedSecret`;
* $P_0$: První veřejný klíč / unikátní adresa pro platbu Bobovi;
* $0$: Celé číslo použité pro generování více unikátních platebních adres.

Bob prohledává blockchain, aby našel svou Silent Payment tímto způsobem:
$$  P_0 = B_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G  $$
S:
* $b_{\text{scan}}$: Bobův soukromý skenovací klíč.

Pokud najde $P_0$ jako adresu obsahující Tichou platbu adresovanou jemu, vypočítá $p_0$, soukromý klíč, který mu umožní utratit prostředky poslané od Alice na $P_0$:

$$ p_0 = (b_{\text{spend}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

S:
* $b_{\text{spend}}$: Bobův soukromý klíč pro utrácení;
* $n$: řád eliptické křivky `secp256k1`.

Kromě této základní verze lze použít také štítky pro generování několika různých statických adres ze stejné základní statické adresy s cílem oddělit více použití bez zbytečného násobení práce vyžadované při skenování.