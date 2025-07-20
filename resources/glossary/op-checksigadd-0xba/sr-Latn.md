---
term: OP_CHECKSIGADD (0XBA)
---

Izvlači tri najviša vrednosti sa steka: `javni ključ`, `CScriptNum` `n` i `potpis`. Ako potpis nije prazan vektor i nije važeći, skripta se završava greškom. Ako je potpis važeći ili je prazan vektor (`OP_0`), predstavljena su dva scenarija:


- Ako je potpis prazan vektor: `CScriptNum` sa vrednošću `n` se postavlja na stek, i izvršavanje se nastavlja;
- Ako potpis nije prazan vektor i ostaje važeći: `CScriptNum` sa vrednošću `n + 1` se stavlja na stek, i izvršavanje se nastavlja.

Da pojednostavimo, `OP_CHECKSIGADD` izvodi operaciju sličnu `OP_CHECKSIG`, ali umesto da gura true ili false na stek, dodaje `1` drugoj vrednosti na vrhu steka ako je potpis validan, ili ostavlja ovu vrednost nepromenjenom ako potpis predstavlja prazni vektor. `OP_CHECKSIGADD` omogućava kreiranje istih multisignature politika u Tapscript-u kao sa `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY`, ali na način koji omogućava grupnu verifikaciju, što znači da uklanja proces pretrage u verifikaciji tradicionalnog Multisig i time ubrzava verifikaciju dok smanjuje operativno opterećenje na CPU-ima čvorova. Ovaj opcode je dodat u Tapscript isključivo za potrebe Taproot.