---
term: BIP0383
definition: multi() en sortedmulti() functies voor het beschrijven van multisig scripts in descriptors.
---

Introduceert de functies `multi(NUM, KEY, ..., KEY)` en `sortedmulti(NUM, KEY, ..., KEY)` voor descriptors. Met deze functies kunnen scripts met meerdere handtekeningen worden beschreven in de descriptors, waarbij `sortedmulti` de openbare sleutels in lexicografische volgorde sorteert om compatibiliteit tijdens het importeren te garanderen. BIP383 is geïmplementeerd samen met alle andere Descriptor-gerelateerde BIP's (behalve BIP386) in versie 0.17 van Bitcoin core.