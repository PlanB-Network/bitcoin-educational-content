---
term: PRIVÁTNÍ KLÍČ

---
Soukromý klíč je základním prvkem asymetrické kryptografie. Je to číslo (v kontextu Bitcoinu 256 bitů), které představuje kryptografické tajemství. Tento klíč se používá k digitálnímu podepisování transakcí a k prokázání vlastnictví veřejného klíče Bitcoinu (a tím i přijímací adresy) splněním podmínky `scriptPubKey`. Soukromé klíče tedy umožňují utrácet bitcoiny odemknutím UTXO spojených s příslušným veřejným klíčem. Soukromé klíče musí být přísně důvěrné, protože jejich zveřejnění by mohlo umožnit zlomyslným třetím stranám převzít kontrolu nad přidruženými prostředky.

V systému Bitcoin je soukromý klíč spojen s veřejným klíčem pomocí algoritmu digitálního podpisu využívajícího eliptické křivky (ECDSA nebo Schnorr). Veřejný klíč je odvozen ze soukromého klíče, ale opačný postup je prakticky nemožný vzhledem k výpočetní náročnosti spojené s řešením základního matematického problému (problém diskrétního logaritmu). Veřejný klíč se obvykle používá k vygenerování bitcoinové adresy, která se pomocí skriptu používá k uzamčení bitcoinů. V kryptografii jsou soukromé klíče často náhodná nebo pseudonáhodná čísla. Ve specifickém kontextu deterministických a hierarchických peněženek Bitcoinu jsou soukromé klíče deterministicky odvozeny ze semínka. Soukromé klíče jsou často zaměňovány se seedem nebo s frází pro obnovení (mnemotechnickou). Tyto prvky jsou však odlišné.

> ► V angličtině se soukromý klíč nazývá "private key" Tento termín se někdy zkracuje na "privkey" nebo "PV".*