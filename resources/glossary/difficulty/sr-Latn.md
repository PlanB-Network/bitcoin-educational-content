---
term: TEŽINA
---

Podesivi parametar koji određuje složenost Proof of Work potrebnu za dodavanje novog bloka u Blockchain i zaradu povezane nagrade. Ova težina je predstavljena ciljem težine, 256-bitnom vrednošću koja postavlja gornju granicu koju Hash zaglavlja bloka mora ispuniti da bi se smatrao važećim. Cilj je da Hash, postignut dvostrukim izvršenjem SHA256 (SHA256d), bude manji ili jednak ovom cilju. Da bi dostigli ovaj Hash, rudari manipulišu `Nonce` u zaglavlju bloka. Težina se prilagođava svakih 2016 blokova, ili otprilike svake dve nedelje, kako bi se održalo prosečno vreme kreiranja bloka na oko 10 minuta.