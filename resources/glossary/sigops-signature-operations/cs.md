---
term: SIGOPS (PODPISOVÉ OPERACE)

---
Vztahuje se na operace s digitálním podpisem, které jsou nezbytné k ověření transakcí. Každá bitcoinová transakce může obsahovat více vstupů, z nichž každý může vyžadovat jeden nebo více podpisů, aby byl považován za platný. Ověřování těchto podpisů se provádí pomocí specifických opkódů zvaných "sigops". Konkrétně se jedná o `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY`. Tyto operace představují určitou zátěž pro síťové uzly, které je musí ověřit. Aby se zabránilo útokům DoS prostřednictvím umělého nafouknutí počtu sigops, zavádí proto protokol omezení počtu sigops povolených na blok, aby se zajistilo, že zátěž při ověřování zůstane pro uzly zvládnutelná. Tento limit je v současné době stanoven na maximálně 80 000 sigops na blok. Pro počítání se uzly řídí těmito pravidly:

V `scriptPubKey` se `OP_CHECKSIG` a `OP_CHECKSIGVERIFY` počítají jako 4 sigopy. Opkódy `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` se počítají na 80 sigops. Při počítání se totiž tyto operace násobí 4, pokud nejsou součástí vstupu SegWit (pro P2WPKH bude tedy počet sigops 1);

V `redeemScriptu` se opkódy `OP_CHECKSIG` a `OP_CHECKSIGVERIFY` počítají také jako 4 sigopy, `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` se započítávají jako `4n`, pokud předcházejí `OP_n`, nebo 80 sigopů v opačném případě;

Pro `witnessScript` mají `OP_CHECKSIG` a `OP_CHECKSIGVERIFY` hodnotu 1 sigop, `OP_CHECKMULTISIG` a `OP_CHECKMULTISIGVERIFY` se počítají jako `n`, pokud jsou zavedeny pomocí `OP_n`, nebo 20 sigop v opačném případě;

Ve skriptech Taproot se se sigopy zachází jinak než v tradičních skriptech. Místo přímého počítání každé podpisové operace zavádí Taproot pro každý vstup transakce rozpočet sigops, který je úměrný velikosti tohoto vstupu. Tento rozpočet je 50 sigops plus velikost bytu svědka vstupu. Každá podpisová operace snižuje tento rozpočet o 50. Pokud provedení podpisové operace sníží rozpočet pod nulu, skript je neplatný. Tato metoda umožňuje větší flexibilitu skriptů Taproot a zároveň zachovává ochranu před možným zneužitím souvisejícím se sigopy tím, že je přímo spojuje s váhou vstupu. Skripty Taproot tedy nejsou zahrnuty do limitu 80 000 sigops na blok.