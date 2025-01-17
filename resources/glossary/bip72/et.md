---
term: BIP72

---
Täiendab BIP70 ja BIP71, määratledes Bitcoini URI laienduse (BIP21) täiendava parameetriga "r". See parameeter võimaldab lisada lingi turvalisele maksetaotlusele, mis on allkirjastatud kaupmehe SSL-sertifikaadiga. Kui klient klõpsab sellel laiendatud URI-l, võtab tema rahakott ühendust kaupmehe serveriga, et taotleda makse üksikasju. Need andmed täidetakse automaatselt rahakoti tehinguliideses ja klienti saab teavitada, et ta maksab allkirjastatud sertifikaadile vastava domeeni omanikule (näiteks "pandul.fr"). Kuna see täiustus on seotud BIP70-ga, ei ole seda kunagi laialdaselt kasutusele võetud.