---
term: P2WSH

---
P2WSH znamená *Pay to Witness Script Hash*. Jedná se o standardní model skriptu, který se používá pro stanovení podmínek výdajů na UTXO. P2WSH byl zaveden s implementací SegWit v srpnu 2017.

Tento skript je podobný skriptu P2SH (*Pay to Public Script Hash*), protože také zamyká bitcoiny na základě hashe skriptu. Rozdíl spočívá v tom, jak jsou podpisy a skripty zahrnuty do transakce. Aby bylo možné utratit bitcoiny za tento typ skriptu, musí příjemce poskytnout původní skript nazvaný `witnessScript` (ekvivalentní k `redeemScript`) spolu s požadovanými podpisy. Tento mechanismus umožňuje implementovat sofistikovanější podmínky utrácení, například multisignály.

V kontextu P2WSH jsou informace o podpisovém skriptu (`scriptWitness`, ekvivalentní `scriptSig`) přesunuty z tradiční struktury transakce do samostatné sekce nazvané `Witness`. Tento přesun je vlastností aktualizace SegWit (*Segregated Witness*), která pomáhá zabránit zfalšování podpisu. Transakce P2WSH jsou ve srovnání s transakcemi Legacy obecně méně nákladné z hlediska poplatků, protože část ve svědkovi stojí méně.

Adresy P2WSH jsou zapsány v kódování `Bech32` s kontrolním součtem v podobě kódu BCH. Tyto adresy vždy začínají znakem `bc1q`. P2WSH je výstupem SegWit verze 0.