---
term: Fragmenti (lightning)
definition: Deo plaćanja koji se rutira odvojeno preko različitih Lightning ruta (MPP/AMP).
---

U kontekstu *Multi-Path Payments (MPP)* ili *Atomic Multi-Path Payments (AMP)*, Shard je frakcija globalnog plaćanja. Svaki Shard predstavlja deo ukupnog plaćanja, koji se rutira zasebno putem različite rute na Lightning-u.


U MPP-u, svi shardovi dele istu tajnu, dok u AMP-u, svaki Shard ima jedinstvenu delimičnu tajnu. Primalac grupiše shardove zajedno kako bi rekonstituisao i finalizovao celu uplatu. Ovaj mehanizam zaobilazi ograničenja likvidnosti na jednom kanalu.