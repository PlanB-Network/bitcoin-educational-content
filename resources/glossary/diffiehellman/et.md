---
term: DIFFIE-HELLMAN

---
Krüptograafiline meetod, mis võimaldab kahel osapoolel luua jagatud saladuse turvamata sidekanali kaudu. Seda saladust saab seejärel kasutada kahe osapoole vahelise suhtluse krüpteerimiseks. Diffie-Hellman kasutab modulaararitmeetikat, nii et isegi kui ründaja saab andmevahetust jälgida, ei saa ta ühist saladust tuletada ilma keerulise matemaatilise probleemi - diskreetse logaritmi - lahendamiseta. Bitcoinis kasutatakse mõnikord DH-varianti ECDH, mis kasutab elliptilist kõverat, eriti staatiliste aadressiprotokollide, nagu Silent Payments või BIP47 puhul.