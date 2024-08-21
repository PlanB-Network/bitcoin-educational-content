---
term: HD (HIERARCHICAL-DETERMINISTIC)
---

Odkazuje na Bitcoinovou peněženku, která používá unikátní kus informace (seed) k generování množství veřejných a soukromých klíčových párů sekvenčním a reprodukovatelným způsobem. Tento způsob správy klíčů je definován standardem BIP32. Hlavní výhodou HD peněženek je, že umožňují uživatelům mít množství různých klíčových párů, zejména k vyhnutí se opětovnému použití adres, přičemž je možné všechny je regenerovat z jediného kusu informace. Tato struktura je popisována jako hierarchická, protože umožňuje vytváření stromově organizovaných mnoha klíčů a adres z jediného seedu. A je deterministická v tom smyslu, že každý seed vždy generuje stejnou sekvenci klíčů v jakékoli peněžence, která je v souladu s tímto systémem.