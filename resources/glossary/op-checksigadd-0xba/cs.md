---
term: OP_CHECKSIGADD (0XBA)
---

Extrahuje tři nejvyšší hodnoty ze zásobníku: `public key` (veřejný klíč), `CScriptNum` `n` a `signature` (podpis). Pokud podpis není prázdný vektor a není platný, skript se ukončí s chybou. Pokud je podpis platný nebo je prázdný vektor (`OP_0`), jsou prezentovány dva scénáře:
* Pokud je podpis prázdný vektor: na zásobník je vložen `CScriptNum` s hodnotou `n` a vykonávání pokračuje;
* Pokud podpis není prázdný vektor a zůstává platný: na zásobník je vložen `CScriptNum` s hodnotou `n + 1` a vykonávání pokračuje.
Zjednodušeně, `OP_CHECKSIGADD` provádí operaci podobnou `OP_CHECKSIG`, ale místo vkládání hodnot true nebo false na zásobník přidá `1` k druhé hodnotě na vrcholu zásobníku, pokud je podpis platný, nebo tuto hodnotu nechá nezměněnou, pokud podpis reprezentuje prázdný vektor. `OP_CHECKSIGADD` umožňuje vytváření stejných politik multisignatur v Tapscriptu jako s `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY`, ale v dávkově ověřitelném způsobu, což znamená, že odstraňuje proces vyhledávání při ověřování tradičního multisigu a tím urychluje ověřování, zatímco snižuje operační zátěž na CPU uzlů. Tento opcode byl přidán v Tapscriptu výhradně pro potřeby Taproot.