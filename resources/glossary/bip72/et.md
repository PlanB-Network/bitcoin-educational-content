---
term: BIP72
---

Täiendab BIP70 ja BIP71, määratledes Bitcoin URI (BIP21) laienduse lisaparameetriga `r`. See parameeter võimaldab lisada lingi turvalisele maksepäringule, mille on allkirjastanud kaupmehe SSL sertifikaat. Kui klient klikib sellel laiendatud URI-l, võtab nende rahakott ühendust kaupmehe serveriga, et küsida makse üksikasju. Need üksikasjad täidetakse automaatselt rahakoti tehingu liideses ja klienti saab teavitada, et nad maksavad domeeni omanikule, kes vastab allkirjastamise sertifikaadile (näiteks "pandul.fr"). Kuna see täiustus on pakendatud koos BIP70-ga, ei ole see kunagi laialdaselt kasutusele võetud.