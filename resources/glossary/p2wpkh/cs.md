---
term: P2WPKH
---

P2WPKH znamená *Pay to Witness Public Key Hash*. Jedná se o standardní skriptový model používaný k určení podmínek pro výdaje UTXO. P2WPKH byl zaveden s implementací SegWit v srpnu 2017.

Tento skript je podobný P2PKH (*Pay to Public Key Hash*), protože také uzamčení bitcoinů na základě hashe veřejného klíče, tedy přijímací adresy. Rozdíl spočívá v tom, jak jsou podpisy a skripty zahrnuty do transakce. V případě P2WPKH jsou informace o skriptu podpisu (`scriptSig`) přesunuty z tradiční struktury transakce do samostatné sekce nazvané `Witness`. Tento krok je funkcí aktualizace SegWit (*Segregated Witness*), která pomáhá zabránit manipulaci s podpisy. Transakce P2WPKH jsou obecně méně nákladné z hlediska poplatků ve srovnání s Legacy transakcemi, protože část ve svědkovi stojí méně.

Adresy P2WPKH jsou zapsány pomocí kódování `Bech32` s kontrolním součtem ve formě BCH kódu. Tyto adresy vždy začínají `bc1q`. P2WPKH je verze 0 výstupu SegWit.