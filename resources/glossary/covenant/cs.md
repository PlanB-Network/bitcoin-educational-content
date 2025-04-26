---
term: COVENANT

---
Mechanismus, který umožňuje stanovit specifické podmínky pro to, jak lze danou měnu utratit, a to i v budoucích transakcích. Nad rámec podmínek, které obvykle umožňuje skriptovací jazyk na UTXO, vynucuje smlouva další omezení, jak lze tento Bitcoin utratit v následných transakcích. Z technického hlediska dochází k vytvoření smlouvy, když `scriptPubKey` UTXO definuje omezení pro `scriptPubKey` výstupů transakce, která utrácí uvedené UTXO. Rozšířením rozsahu skriptu by covenanty umožnily četný vývoj na Bitcoinu, jako je například oboustranné ukotvení drivechainů, implementace trezorů nebo vylepšení překryvných systémů, jako je Lightning. Návrhy paktů se rozlišují na základě tří kritérií:


- Jejich rozsah;
- Jejich provedení;
- Jejich rekurzivita.

Existuje mnoho návrhů, které by umožňovaly použití smluv o bitcoinech. Nejpokročilejší v procesu implementace jsou: (CTV), `SIGHASH_ANYPREVOUT` (APO) a `OP_VAULT`. Mezi dalšími návrhy jsou např: `OP_TX`, `OP_TAPLEAFUPDATEVERIFY` (TLUV), `OP_EVICT`, `OP_CHECKSIGFROMSTACKVERIFY` (CSFSV), `OP_CAT` atd.

Pro lepší pochopení pojmu smlouva zvažte následující analogii: představte si trezor, ve kterém je 500 EUR v drobných bankovkách. Pokud se vám podaří tento trezor odemknout správným klíčem, můžete s těmito penězi volně nakládat podle svého uvážení. Taková je běžná situace v případě Bitcoinu. Nyní si představte, že stejný trezor neobsahuje 500 € v bankovkách, ale stravenky v ekvivalentní hodnotě. Pokud se vám podaří tento trezor otevřít, můžete tuto částku použít. Vaše svoboda utrácení je však omezena, protože tyto poukázky můžete použít pouze k placení v určitých restauracích. Existuje tedy první podmínka pro utracení těchto peněz, kterou je zvládnutí otevření trezoru příslušným klíčem. Existuje však také další podmínka týkající se budoucího použití této částky: musí být utracena výhradně v partnerských restauracích, a nikoliv volně. Tento systém omezení budoucích transakcí se nazývá smlouva.

> ► Ve francouzštině neexistuje výraz, který by přesně vystihoval význam slova "smlouva". Mohli bychom mluvit o "klauzuli", "smlouvě" nebo "závazku", ale ty by přesně neodpovídaly termínu "smlouva". Tento termín je převzat z právní terminologie, která umožňuje popsat smluvní doložku ukládající trvalé závazky k majetku*