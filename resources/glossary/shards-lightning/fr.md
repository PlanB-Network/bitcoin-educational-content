---
term: SHARDS (LIGHTNING)
---

Dans le cadre des *Multi-Path Payments (MPP)* ou des *Atomic Multi-Path Payments (AMP)*, un shard est une fraction d'un paiement global. Chaque shard représente une partie du paiement total qui est acheminée séparément via une route différente sur Lightning.
Dans le cadre des MPP, tous les shards partagent le même secret, alors que dans les AMP, chaque shard dispose d'un secret partiel unique. Le destinataire regroupe les shards pour reconstituer et finaliser le paiement complet. Ce mécanisme permet de contourner les limitations de liquidité sur un canal unique.
