---
term: SIGOPS (SIGNATURE OPERATIONS)
---

Odnosi se na operacije digitalnog potpisa neophodne za validaciju transakcija. Svaka Bitcoin transakcija može sadržati više ulaza, od kojih svaki može zahtevati jedan ili više potpisa da bi se smatrali validnim. Verifikacija ovih potpisa se vrši korišćenjem specifičnih opkodova nazvanih "sigops". Konkretno, to uključuje `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY`. Ove operacije nameću određeno opterećenje na mrežne čvorove koji ih moraju verifikovati. Da bi se sprečili DoS napadi kroz veštačko povećanje broja sigops, protokol stoga nameće ograničenje na broj sigops dozvoljenih po bloku, kako bi se osiguralo da opterećenje validacije ostane upravljivo za čvorove. Ovo ograničenje je trenutno postavljeno na maksimalno 80,000 sigops po bloku. Da bi brojali, čvorovi prate ova pravila:


U `scriptPubKey`, `OP_CHECKSIG` i `OP_CHECKSIGVERIFY` računaju se kao 4 sigops. Opcode-ovi `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` računaju se za 80 sigops. Zaista, tokom brojanja, ove operacije se množe sa 4 kada nisu deo SegWit ulaza (za P2WPKH, broj sigops će stoga biti 1);


U `redeemscript`, opkodi `OP_CHECKSIG` i `OP_CHECKSIGVERIFY` takođe se računaju kao 4 sigopa, `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` se računaju kao `4n` ako prethode `OP_n`, ili 80 sigopa u suprotnom;


Za `witnessScript`, `OP_CHECKSIG` i `OP_CHECKSIGVERIFY` vrede 1 sigop, `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` se računaju kao `n` ako su uvedeni sa `OP_n`, ili 20 sigops u suprotnom;


U Taproot skriptama, sigops se tretiraju drugačije u poređenju sa tradicionalnim skriptama. Umesto direktnog brojanja svake operacije potpisa, Taproot uvodi budžet za sigops za svaki ulaz transakcije, koji je proporcionalan veličini tog ulaza. Ovaj budžet je 50 sigops plus veličina u bajtovima svedoka ulaza. Svaka operacija potpisa smanjuje ovaj budžet za 50. Ako izvršenje operacije potpisa smanji budžet ispod nule, skripta je nevažeća. Ova metoda omogućava veću fleksibilnost u Taproot skriptama, dok održava zaštitu protiv potencijalnih zloupotreba povezanih sa sigops, direktnim povezivanjem sa težinom ulaza. Tako, Taproot skripte nisu uključene u ograničenje od 80,000 sigops po bloku.