---
term: COVENANT
---

Mechanismus, který umožňuje uvalení specifických podmínek na to, jak lze danou měnu utratit, včetně budoucích transakcí. Kromě podmínek obvykle povolených skriptovacím jazykem na UTXO, covenant ukládá další omezení na to, jak lze tyto Bitcoiny utratit v následujících transakcích. Technicky je covenant zřízen, když `scriptPubKey` UTXO definuje omezení na `scriptPubKey` výstupů transakce, která dané UTXO utratí. Rozšířením rozsahu skriptu by covenants umožnily řadu vývojových kroků na Bitcoinu, jako je bilaterální ukotvení drivechainů, implementace trezorů nebo zlepšení nadstavbových systémů jako Lightning. Návrhy covenantů se liší podle tří kritérií:
* Jejich rozsah;
* Jejich implementace;
* Jejich rekurzivita.

Existuje mnoho návrhů, které by umožnily použití covenantů na Bitcoinu. Nejdále v procesu implementace jsou: `OP_CHECKTEMPLATEVERIFY` (CTV), `SIGHASH_ANYPREVOUT` (APO) a `OP_VAULT`. Mezi další návrhy patří: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT` atd.

Pro lepší pochopení konceptu covenantu si představte tuto analogii: představte si trezor obsahující 500€ v malých bankovkách. Pokud se vám podaří tento trezor odemknout správným klíčem, pak můžete tyto peníze utratit, jak chcete. To je normální situace u Bitcoinu. Nyní si představte, že tentýž trezor neobsahuje 500€ v bankovkách, ale spíše stravenky ekvivalentní hodnoty. Pokud se vám podaří tento trezor otevřít, můžete tuto sumu utratit. Vaše svoboda utrácení je však omezena, protože tyto poukázky můžete použít pouze na platbu v určitých restauracích. Existuje tedy první podmínka pro utrácení těchto peněz, která spočívá v tom, že se vám musí podařit otevřít trezor s vhodným klíčem. Ale existuje také další podmínka týkající se budoucího použití této sumy: musí být utracena výhradně v partnerských restauracích, a ne volně. Tento systém omezení budoucích transakcí se nazývá covenant.

> ► *Ve francouzštině neexistuje termín, který by přesně zachytil význam slova "covenant". Mohlo by se mluvit o "klauzuli", "paktu" nebo "závazku", ale tyto by přesně neodpovídaly termínu "covenant". Tento termín je převzat z právní terminologie, která umožňuje popsat smluvní klauzuli ukládající trvalé povinnosti na majetek.*