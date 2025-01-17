---
term: COINBASE (TRANSAKCE)

---
Transakce coinbase je speciální a jedinečná transakce, která je součástí každého bloku blockchainu bitcoinu. Představuje první transakci bloku a je vytvořena těžařem, který úspěšně nalezl hlavičku potvrzující důkaz práce (*Proof-of-Work*), tj. menší nebo rovnou cíli.

Transakce na coinbase slouží především ke dvěma účelům: k udělení blokové odměny těžaři a k přidání nových jednotek bitcoinů do peněžní zásoby v oběhu. Bloková odměna, která je ekonomickou pobídkou pro těžaře, aby se zapojili do proof of work, zahrnuje kumulované poplatky za transakce zahrnuté do bloku a stanovené množství nově vytvořených bitcoinů ex-nihilo (bloková dotace). Tato částka, která byla v roce 2009 původně stanovena na 50 bitcoinů za blok, se každých 210 000 bloků (přibližně každé 4 roky) snižuje na polovinu během události zvané "halving"

Transakce na coinbase se od běžných transakcí liší několika způsoby. Zaprvé nemá vstup, což znamená, že se při ní nespotřebovává žádný existující výstup transakce (UTXO). Dále podpisový skript (`scriptSig`) transakce coinbase obvykle obsahuje libovolné pole umožňující začlenění dalších údajů, jako jsou vlastní zprávy nebo informace o verzi těžebního softwaru. A konečně, bitcoiny vygenerované transakcí coinbase podléhají době splatnosti 100 bloků (101 potvrzení), než je lze utratit, aby se zabránilo případnému utracení neexistujících bitcoinů v případě reorganizace řetězce.

> ► *Ve francouzštině neexistuje žádný překlad slova "Coinbase". Proto je přijatelné používat tento termín přímo.*