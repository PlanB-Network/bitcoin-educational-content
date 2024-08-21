---
term: DIFFIE-HELLMAN
---

Krüptograafiline meetod, mis võimaldab kahel osapoolel genereerida jagatud saladuse turvamata suhtluskanali kaudu. See saladus võib seejärel olla kasutatav suhtluse krüpteerimiseks kahe osapoole vahel. Diffie-Hellman kasutab modulaararitmeetikat nii, et isegi kui ründaja suudab vahetusi jälgida, ei saa ta jagatud saladust ilma keerulise matemaatilise probleemi lahendamiseta dedutseerida: diskreetne logaritm. Bitcoinis kasutatakse mõnikord DH varianti, mida nimetatakse ECDH-ks, mis kasutab elliptilist kõverat, eriti staatiliste aadressiprotokollide puhul nagu Silent Payments või BIP47.