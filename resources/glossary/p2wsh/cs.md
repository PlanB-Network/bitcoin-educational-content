---
term: P2WSH
---

P2WSH znamená *Pay to Witness Script Hash*. Jedná se o standardní skriptový model používaný k určení podmínek výdaje na UTXO. P2WSH byl zaveden s implementací SegWit v srpnu 2017.

Tento skript je podobný P2SH (*Pay to Public Script Hash*), protože také uzamčuje bitcoiny na základě hashe skriptu. Rozdíl spočívá v tom, jak jsou podpisy a skripty zahrnuty do transakce. Pro výdaj bitcoinů na tomto typu skriptu musí příjemce poskytnout původní skript, nazývaný `witnessScript` (ekvivalent k `redeemScript`), spolu s požadovanými podpisy. Tento mechanismus umožňuje implementaci složitějších podmínek výdaje, jako jsou multisigy.

V kontextu P2WSH jsou informace o podpisovém skriptu (tzv. `scriptWitness`, ekvivalent k `scriptSig`) přesunuty z tradiční struktury transakce do samostatné sekce nazvané `Witness`. Tento krok je funkcí aktualizace SegWit (*Segregated Witness*), která pomáhá zabránit manipulaci s podpisy. Transakce P2WSH jsou obecně méně nákladné z hlediska poplatků ve srovnání s Legacy transakcemi, jelikož část v sekci witness stojí méně.

Adresy P2WSH jsou zapsány pomocí kódování `Bech32` s kontrolním součtem ve formě BCH kódu. Tyto adresy vždy začínají `bc1q`. P2WSH je výstup SegWit verze 0.