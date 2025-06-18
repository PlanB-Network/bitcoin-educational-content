---
term: KÓD BCH
---

Třída kódů pro opravu chyb, které se používají k detekci a opravě chyb v datové posloupnosti. Jinými slovy, kódy pro opravu chyb BCH se používají k vyhledávání a opravě náhodných chyb v přenášených informacích, aby se zajistilo, že informace dorazí do cíle v neporušeném stavu. Zkratka "BCH" znamená iniciály jmen vynálezců těchto kódů: Bose, Ray-Chaudhuri a Hocquenghem.


Tento nástroj se používá v mnoha oblastech výpočetní techniky, včetně SSD, DVD a QR kódů. Díky těmto kódům opravujícím chyby je například možné načíst zakódované informace i v případě, že je QR kód částečně zakrytý.


V rámci Bitcoin se kódy BCH používají pro kontrolní součet ve formátech Bech32 a Bech32m (po SegWit) Address. Představují lepší kompromis mezi velikostí kontrolního součtu a schopností detekce chyb než jednoduché funkce Hash, které se dříve používaly na starších adresách. V kontextu Bitcoin se kódy BCH používají pouze pro detekci chyb, nikoli pro jejich opravu. Software portfolia Bitcoin tedy identifikuje a ohlásí uživateli případné chyby v přijímajícím kódu Address, ale automaticky nezmění chybný kód Address. Tato volba je motivována skutečností, že integrace opravy chyb nevyhnutelně ovlivňuje schopnosti algoritmu detekovat chyby.