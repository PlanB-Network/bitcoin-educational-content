---
term: P2WPKH

---
P2WPKH znamená *Pay to Witness Public Key Hash*. Jedná se o standardní model skriptu, který se používá pro stanovení podmínek výdajů na UTXO. P2WPKH byl zaveden s implementací SegWit v srpnu 2017.

Tento skript je podobný skriptu P2PKH (*Pay to Public Key Hash*), protože také zamyká bitcoiny na základě hashe veřejného klíče, tedy přijímací adresy. Rozdíl spočívá v tom, jak jsou podpisy a skripty zahrnuty do transakce. V případě P2WPKH jsou informace o podpisovém skriptu (`scriptSig`) přesunuty z tradiční struktury transakce do samostatné sekce nazvané `Witness`. Tento přesun je vlastností aktualizace SegWit (*Segregated Witness*), která pomáhá zabránit zfalšování podpisu. Transakce P2WPKH jsou ve srovnání s transakcemi Legacy obecně méně nákladné z hlediska poplatků, protože část ve svědkovi stojí méně.

Adresy P2WPKH jsou zapsány v kódování `Bech32` s kontrolním součtem v podobě kódu BCH. Tyto adresy vždy začínají znakem `bc1q`. P2WPKH je výstupem SegWit verze 0.