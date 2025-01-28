---
term: BECH32 E BECH32M

---
`Bech32` e `Bech32m` sono due formati di codifica degli indirizzi per la ricezione di bitcoin. Si basano su una base 32 leggermente modificata. Incorporano un checksum basato su un algoritmo di correzione degli errori chiamato BCH (*Bose-Chaudhuri-Hocquenghem*). Rispetto agli indirizzi Legacy, codificati in `Base58check`, gli indirizzi `Bech32` e `Bech32m` hanno un checksum più efficiente, che consente di rilevare e potenzialmente correggere automaticamente gli errori di battitura. Il loro formato offre anche una migliore leggibilità, con solo caratteri minuscoli. Ecco la matrice di addizione per questo formato in base 10:

&nbsp;

| + | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |

| --- | --- | --- | --- | --- | --- | --- | --- | --- |

| 0 | q | p | z | r | y | 9 | x | 8 |

| 8 | g | f | 2 | t | v | d | w | 0 |

| 16 | s | 3 | j | n | 5 | 4 | k | h |

| 24 | c | e | 6 | m | u | a | 7 | l |

&nbsp;

Bech32 e Bech32m sono formati di codifica utilizzati per rappresentare gli indirizzi SegWit. Bech32 è un formato di codifica degli indirizzi introdotto da BIP173 nel 2017. Utilizza un insieme specifico di caratteri, composto da numeri e lettere minuscole, per ridurre al minimo gli errori di digitazione e facilitare la lettura. Gli indirizzi Bech32 iniziano generalmente con `bc1` per indicare che sono nativi di SegWit. Questo formato è utilizzato solo per gli indirizzi SegWit V0, con gli script P2WPKH (Pay to Witness Public Key Hash) e P2WSH (Pay to Witness Script Hash). Tuttavia, esiste un piccolo e inaspettato difetto specifico del formato Bech32. Ogni volta che l'ultimo carattere dell'indirizzo è una `p`, l'aggiunta o la rimozione di qualsiasi numero di caratteri `q` immediatamente precedenti non invalida la somma di controllo. Questo non influisce sugli usi esistenti degli indirizzi SegWit V0 (BIP173) a causa della loro limitazione a due lunghezze definite. Tuttavia, ciò potrebbe influire sugli usi futuri della codifica Bech32. Il formato Bech32m è semplicemente un formato Bech32 con questo errore corretto. È stato introdotto con il BIP350 nel 2020. Anche gli indirizzi Bech32m iniziano con `bc1`, ma sono specificamente progettati per essere compatibili con SegWit V1 (Taproot) e versioni successive, con lo script P2TR (Pay to TapRoot).