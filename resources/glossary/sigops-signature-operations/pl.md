---
term: SIGOPS (OPERACJE PODPISU)
---

Odnosi się do operacji podpisu cyfrowego niezbędnych do walidacji transakcji. Każda transakcja Bitcoin może zawierać wiele danych wejściowych, z których każda może wymagać jednego lub więcej podpisów, aby została uznana za ważną. Weryfikacja tych podpisów odbywa się poprzez użycie określonych kodów operacyjnych zwanych "sigops". W szczególności obejmuje to `OP_CHECKSIG`, `OP_CHECKSIGVERIFY`, `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY`. Operacje te nakładają pewne obciążenie na węzły sieci, które muszą je zweryfikować. Aby zapobiec atakom DoS poprzez sztuczną inflację liczby sigops, protokół nakłada limit na liczbę sigops dozwolonych na blok, aby zapewnić, że obciążenie walidacyjne pozostaje zarządzalne dla węzłów. Limit ten wynosi obecnie maksymalnie 80 000 sygops na blok. Aby policzyć, węzły przestrzegają następujących zasad:


W `scriptPubKey`, `OP_CHECKSIG` i `OP_CHECKSIGVERIFY` liczą się jako 4 sygops. Kody operacyjne `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` liczą się za 80 sigops. Rzeczywiście, podczas liczenia, operacje te są mnożone przez 4, gdy nie są częścią wejścia SegWit (dla P2WPKH, liczba sigops będzie zatem wynosić 1);


W `redeemscript`, kody operacyjne `OP_CHECKSIG` i `OP_CHECKSIGVERIFY` są również liczone jako 4 sigops, `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` są liczone jako `4n` jeśli poprzedzają `OP_n`, lub 80 sigops w przeciwnym wypadku;


Dla `witnessScript`, `OP_CHECKSIG` i `OP_CHECKSIGVERIFY` są warte 1 sigop, `OP_CHECKMULTISIG` i `OP_CHECKMULTISIGVERIFY` są liczone jako `n` jeśli są wprowadzone przez `OP_n`, lub 20 sigop w przeciwnym wypadku;


W skryptach Taproot sigops są traktowane inaczej niż w tradycyjnych skryptach. Zamiast bezpośrednio liczyć każdą operację podpisu, Taproot wprowadza budżet sigops dla każdego wejścia transakcji, który jest proporcjonalny do rozmiaru tego wejścia. Budżet ten wynosi 50 sigops plus rozmiar bajtu świadka wejścia. Każda operacja podpisu zmniejsza ten budżet o 50. Jeśli wykonanie operacji podpisu zmniejszy budżet poniżej zera, skrypt jest nieważny. Ta metoda pozwala na większą elastyczność w skryptach Taproot, przy jednoczesnym zachowaniu ochrony przed potencjalnymi nadużyciami związanymi z sigops, poprzez bezpośrednie powiązanie ich z wagą danych wejściowych. W związku z tym skrypty Taproot nie są objęte limitem 80 000 sigops na blok.