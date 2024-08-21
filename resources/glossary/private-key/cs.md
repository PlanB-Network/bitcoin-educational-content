---
term: SOUKROMÝ KLÍČ
---

Soukromý klíč je základním prvkem asymetrické kryptografie. Jedná se o číslo (256 bitů v kontextu Bitcoinu), které představuje kryptografické tajemství. Tento klíč se používá k digitálnímu podepisování transakcí a prokázání vlastnictví veřejného klíče Bitcoinu (a tím i přijímací adresy) splněním `scriptPubKey`. Soukromé klíče tedy umožňují utrácení bitcoinů odemknutím UTXO spojených s odpovídajícím veřejným klíčem. Soukromé klíče musí být přísně důvěrné, protože jejich zveřejnění by mohlo umožnit zlomyslným třetím stranám ovládnout přidružené fondy.

V systému Bitcoin je soukromý klíč spojen s veřejným klíčem prostřednictvím algoritmu digitálního podpisu používajícího eliptické křivky (ECDSA nebo Schnorr). Veřejný klíč je odvozen ze soukromého klíče, ale opačný proces je prakticky nemožné dosáhnout kvůli výpočetní složitosti spojené s řešením základního matematického problému (problém diskrétního logaritmu). Veřejný klíč se obvykle používá k generování Bitcoinové adresy, která se používá k uzamčení bitcoinů pomocí skriptu. V kryptografii jsou soukromé klíče často náhodná nebo pseudonáhodná čísla. Ve specifickém kontextu Bitcoinu deterministických a hierarchických peněženek jsou soukromé klíče deterministicky odvozeny ze seedu. Soukromé klíče jsou často zaměňovány se seedem nebo s obnovovací frází (mnemonikou). Tyto prvky jsou však odlišné.

> ► *V angličtině se soukromý klíč nazývá "private key." Tento termín se někdy zkracuje jako "privkey" nebo "PV."*