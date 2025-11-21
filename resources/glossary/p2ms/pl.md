---
term: P2MS
---

P2MS to skrót od *Pay to Multisig*, co tłumaczy się jako "zapłać za wiele podpisów". Jest to standardowy model skryptu używany do ustalania warunków wydawania na UTXO. Pozwala on na blokowanie bitcoinów za pomocą wielu kluczy publicznych. Aby wydać te bitcoiny, wymagany jest podpis z predefiniowaną liczbą powiązanych kluczy prywatnych. Na przykład, `P2MS 2/3` obejmuje `3` klucze publiczne z `3` powiązanymi tajnymi kluczami prywatnymi. Aby wydać bitcoiny zablokowane za pomocą tego skryptu P2MS, wymagany jest podpis z co najmniej `2` z `3` kluczy prywatnych. Jest to progowy system bezpieczeństwa.


Skrypt ten został wymyślony w 2011 roku przez Gavina Andresena, gdy przejął on opiekę nad głównym klientem Bitcoin. Obecnie P2MS jest tylko marginalnie wykorzystywany przez niektóre aplikacje. Zdecydowana większość współczesnych multisignature używa innych skryptów, takich jak P2SH lub P2WSH. W porównaniu do nich, P2MS jest niezwykle trywialny. Klucze publiczne, z których się składa, są ujawniane po otrzymaniu transakcji. Korzystanie z P2MS jest również droższe niż w przypadku innych skryptów wielopodpisowych.


> *P2MS są często nazywane "bare-Multisig", co można przetłumaczyć jako "naked multisignature" lub "raw multisignature". Na początku 2023 r. skrypty P2MS znalazły się w centrum kontrowersji z powodu ich niewłaściwego wykorzystania w protokole Stamps. Zwrócono szczególną uwagę na ich wpływ na zestaw UTXO*