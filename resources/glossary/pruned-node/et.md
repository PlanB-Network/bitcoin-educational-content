---
term: KÄRPITUD SÕLM
---

Kärbitud sõlm, inglise keeles "Pruned Node", on täissõlm, mis teostab plokiahela kärpimist. See hõlmab vanimate plokkide järkjärgulist eemaldamist pärast nende nõuetekohast kontrollimist, jättes alles ainult kõige uuemad plokid. Säilitamise limiit on määratletud `bitcoin.conf` failis läbi `prune=n` parameetri, kus `n` on plokkide poolt hõivatud maksimaalne suurus megabaitides (MB). Kui selle parameetri järel on märgitud `0`, siis kärpimine on keelatud ja sõlm säilitab plokiahela tervikuna.

Kärbitud sõlmi peetakse mõnikord täissõlmedest erinevateks sõlmetüüpideks. Kärbitud sõlme kasutamine võib olla eriti huvipakkuv kasutajatele, kes seisavad silmitsi salvestusvõimsuse piirangutega. Praegu peab täissõlm plokiahela salvestamiseks omama peaaegu 600 GB vaba ruumi. Kärbitud sõlm võib vajaliku salvestusruumi piirata kuni 550 MB-ni. Kuigi see kasutab vähem kettaruumi, säilitab kärbitud sõlm täissõlmega sarnase kontrollimise ja valideerimise taseme. Seega pakuvad kärbitud sõlmed oma kasutajatele võrreldes kerge sõlmedega (SPV) suuremat usaldusväärsust.