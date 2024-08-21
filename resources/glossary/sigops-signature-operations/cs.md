---
term: SIGOPS (SIGNATURE OPERATIONS)
---

Odkazuje na operace digitálního podpisu potřebné k ověření transakcí. Každá Bitcoinová transakce může obsahovat více vstupů, z nichž každý může vyžadovat jeden nebo více podpisů, aby byl považován za platný. Ověření těchto podpisů se provádí pomocí specifických operací s kódy nazývaných "sigops". Konkrétně to zahrnuje `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY`. Tyto operace kládou určité zatížení na uzly sítě, které je musí ověřit. Aby se zabránilo útokům DoS prostřednictvím umělého zvyšování počtu sigops, protokol proto ukládá limit na počet sigops povolených na blok, aby se zajistilo, že zatížení ověřování zůstane pro uzly zvládnutelné. Tento limit je v současné době nastaven na maximálně 80 000 sigops na blok. Pro počítání uzly následují tato pravidla:

V `scriptPubKey`, `OP_CHECKSIG` a `OP_CHECKSIGVERIFY` se počítají jako 4 sigops. Opcodes `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` se počítají za 80 sigops. Skutečně, při počítání se tyto operace násobí čtyřmi, pokud nejsou součástí SegWit vstupu (pro P2WPKH bude počet sigops tedy 1);

V `redeemScript`, opcodes `OP_CHECKSIG` a `OP_CHECKSIGVERIFY` se také počítají jako 4 sigops, `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` se počítají jako `4n`, pokud předcházejí `OP_n`, nebo 80 sigops jinak;

Pro `witnessScript`, `OP_CHECKSIG` a `OP_CHECKSIGVERIFY` mají hodnotu 1 sigop, `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` se počítají jako `n`, pokud jsou zavedeny `OP_n`, nebo 20 sigops jinak;

V Taproot skriptech se sigops zpracovávají odlišně ve srovnání s tradičními skripty. Místo přímého počítání každé operace podpisu, Taproot zavádí rozpočet sigops pro každý vstup transakce, který je proporcionální k velikosti tohoto vstupu. Tento rozpočet je 50 sigops plus bajtová velikost svědectví vstupu. Každá operace podpisu tento rozpočet snižuje o 50. Pokud provedení operace podpisu sníží rozpočet pod nulu, skript je neplatný. Tato metoda umožňuje větší flexibilitu v Taproot skriptech, zatímco chrání před potenciálními zneužitími souvisejícími s sigops, tím, že je přímo spojuje s váhou vstupu. Taproot skripty tedy nejsou zahrnuty v limitu 80 000 sigops na blok.