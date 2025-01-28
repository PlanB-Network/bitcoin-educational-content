---
term: BIP118

---
Forslag til forbedring av Bitcoin med sikte på å introdusere to nye SigHash Flag-modifikatorer: `SIGHASH_ANYPREVOUT` og `SIGHASH_ANYPREVOUTANYSCRIPT`. Disse funksjonene utvider mulighetene for Bitcoin-transaksjoner, spesielt når det gjelder smarte kontrakter og overlay-løsninger som Lightning Network. BIP118 vil særlig muliggjøre bruk av Eltoo. Den største fordelen med `SIGHASH_ANYPREVOUT` er å tillate gjenbruk av signaturer på tvers av flere transaksjoner, noe som gir mer fleksibilitet. Disse SigHashes tillater nemlig en signatur som ikke dekker noen av transaksjonens inndata.