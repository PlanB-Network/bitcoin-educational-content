---
term: PRUNED NODE

---
Pruned node, inglise keeles "kärbitud sõlme", on täisnood, mis teostab plokiahela kärpimist. See hõlmab vanimate plokkide järkjärgulist eemaldamist pärast nende nõuetekohast kontrollimist, et säilitada ainult kõige uuemad plokid. Säilitamispiirang määratakse failis `bitcoin.conf` parameetriga `prune=n`, kus `n` on plokkide maksimaalne suurus megabaitides (MB). Kui selle parameetri järele on märgitud `0`, siis on kärpimine välja lülitatud ja sõlm säilitab plokiahelat tervikuna.

Lõigatud sõlmede puhul on mõnikord tegemist täissõlmedest erinevat tüüpi sõlmedega. Lõigatud sõlmede kasutamine võib olla eriti huvitav kasutajate jaoks, kellel on piirangud salvestusmahule. Praegu peab täisnoodil olema peaaegu 600 GB ainult plokiahela salvestamiseks. Kärbitud sõlme puhul võib vajalik salvestusruum piirduda kuni 550 MB-ga. Kuigi see kasutab vähem kettaruumi, säilitab kärbitud sõlme verifitseerimise ja valideerimise taseme, mis sarnaneb täisnoodiga. Seega pakuvad kärbitud sõlmed oma kasutajatele rohkem usaldust võrreldes kergete sõlmedega (SPV).