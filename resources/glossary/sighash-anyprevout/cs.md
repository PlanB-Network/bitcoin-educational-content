---
term: SIGHASH_ANYPREVOUT

---
Návrh na implementaci nového modifikátoru SigHash Flag v Bitcoinu, který byl zaveden s BIP118. `SIGHASH_ANYPREVOUT` umožňuje větší flexibilitu při správě transakcí, zejména pro pokročilé aplikace, jako jsou platební kanály v síti Lightning Network a aktualizace Eltoo. Příznak `SIGHASH_ANYPREVOUT` umožňuje, aby podpis nebyl vázán na žádný konkrétní předchozí UTXO (*Any Previous Output*). Při použití v kombinaci s `SIGHASH_ALL` by umožňoval podepsat všechny výstupy transakce, ale žádný ze vstupů. To by umožnilo opakované použití podpisu pro různé transakce, pokud jsou splněny určité stanovené podmínky.

> ► *Tento modifikátor SigHash SIGHASH_ANYPREVOUT je odvozen od myšlenky SIGHASH_NOINPUT, kterou původně navrhl Joseph Poon v roce 2016, aby vylepšil svůj koncept Lightning Network.*