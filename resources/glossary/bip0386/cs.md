---
term: BIP0386

definition: Funkce tr() pro popis Taproot výstupů v deskriptorech.
---
Zavádí deskriptorové funkce pro Taproot. Definuje funkce `tr(KEY)` a `tr(KEY, TREE)` pro vyhledávání výstupů Taproot, kde `KEY` je vnitřní klíč a `TREE` je nepovinný strom cest ke skriptům. BIP386 byl implementován do jádra bitcoinu verze 22.0.