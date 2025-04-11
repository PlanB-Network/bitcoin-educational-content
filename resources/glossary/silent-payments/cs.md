---
term: TICHÉ PLATBY

---
Způsob použití statických adres Bitcoin k přijímání plateb bez opakovaného použití adresy, bez interakce a bez viditelného propojení v řetězci mezi různými platbami a statickou adresou. Tato technika eliminuje potřebu generovat nové, nepoužívané přijímací adresy pro každou transakci, a tím se vyhýbá obvyklým interakcím v Bitcoinu, kdy příjemce musí plátci poskytnout novou adresu.

Při tichých platbách používá plátce veřejné klíče příjemce (veřejný klíč výdaje a veřejný klíč skenování) a součet svých soukromých klíčů jako vstup pro generování nové adresy pro každou platbu. Pouze příjemce může pomocí svých soukromých klíčů vypočítat soukromý klíč odpovídající této platební adrese. ECDH (*Elliptic-Curve Diffie-Hellman*), kryptografický algoritmus výměny klíčů, se používá k vytvoření sdíleného tajemství, které se pak použije k odvození adresy příjemce a soukromého klíče (pouze na straně příjemce). Aby příjemci identifikovali Tiché platby, které jsou jim určeny, musí prohledat blockchain a prozkoumat každou transakci odpovídající kritériím protokolu. Na rozdíl od BIP47, který k vytvoření platebního kanálu používá notifikační transakci, Tiché platby tento krok eliminují a šetří transakci. Kompromisem však je, že příjemce musí proskenovat všechny potenciální transakce, aby pomocí ECDH zjistil, zda jsou určeny jemu.

Například Bobova statická adresa $B$ představuje konkatenaci jeho skenovacího veřejného klíče a jeho výdajového veřejného klíče:

$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{výdaje}} $$

Tyto klíče jsou jednoduše odvozeny z následující cesty:

```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```

Tuto statickou adresu zveřejňuje Bob. Alice ji načte, aby mohla provést tichou platbu Bobovi. Bobovu platební adresu $P_0$ vypočítá tímto způsobem:

$$ P_0 = B_{\text{výdaj}} + \text{hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$

Kde:

$$ \text{inputHash} = \text{hash}(\text{outpoint}_L \text{ ‖ } A) $$

S:


- $B_{\text{scan}}$: Bobův skenovací veřejný klíč (statická adresa);
- $B_{\text{spend}}$: Bobův veřejný klíč (statická adresa);
- $A$: Součet veřejných klíčů na vstupu (tweak);
- $a$: Soukromý klíč tweaku, tj. součet všech párů klíčů použitých ve `scriptPubKey` UTXO, které jsou použity jako vstupy v Alicině transakci;
- $\text{outpoint}_L$: Nejmenší UTXO (lexikograficky) použitý jako vstup v Alicině transakci;
- $\text{ ‖ }$: Konkatenace (operace spojování operandů od konce ke konci);
- $G$: Generátorový bod eliptické křivky `secp256k1`;
- $\text{hash}$: SHA256 hashovací funkce s označením `BIP0352/SharedSecret`;
- $P_0$: První veřejný klíč / jedinečná adresa pro platbu Bobovi;
- $0$: Celé číslo, které se používá k vygenerování více jedinečných platebních adres.

Bob tímto způsobem prohledá blockchain a najde svou tichou platbu:

$$ P_0 = B_{\text{výdaj}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$

S:


- $b_{\text{scan}}$: Bobův soukromý skenovací klíč.

Pokud najde $P_0$ jako adresu obsahující tichou platbu adresovanou jemu, vypočítá $p_0$, soukromý klíč, který mu umožní utratit prostředky zaslané Alicí na $P_0$:

$$ p_0 = (b_{\text{výdaj}} + \text{hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$

S:


- $b_{\text{spend}}$: Bobův soukromý výdajový klíč;
- $n$: řád eliptické křivky `secp256k1`.

Kromě této základní verze lze štítky použít také k vygenerování několika různých statických adres ze stejné základní statické adresy s cílem oddělit více použití, aniž by se nepřiměřeně znásobila práce potřebná při skenování.