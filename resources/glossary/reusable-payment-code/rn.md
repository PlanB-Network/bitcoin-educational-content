---
term: Code de paiment réutilisable
definition: Ikimenyetso kidahinduka ca BIP47 cemera gukura ama aderesi adasanzwe ata gusubira gukoresha ama aderesi.
---

Muri BIP47, kode yo kwishura ishobora gusubirwamwo ni ikimenyetso kidahinduka kivuye kuri Bitcoin Wallet gishobora gutuma habaho ugutanga amakuru n’ugukura amaderesi yihariye. Ivyo bituma umuntu adasubira gukoresha amaderesi, ivyo bikaba bituma umuntu atakaza ubuzima bwiwe bwite, ataco akeneye gukura no gutanga amaderesi mashasha atakoreshwa ku bijanye n’ukwishura kwose. Muri BIP47, amakode yo kwishura ashobora gusubirwamwo yubatswe gutya:


- Byte 0 ihuye n’ivyo verisiyo;
- Byte 1 ni umwanya wo kwongerako amakuru mu gihe woba ukoreshwa;
- Byte 2 yerekana uburinganire bwa `y` bw'urufunguzo rwa bose;
- Kuva kuri byte 3 gushika kuri byte 34, uzosanga agaciro ka `x` k'urufunguzo rwa bose;
- Kuva kuri byte 35 gushika kuri byte 66, hariho chain code ifatanye n’urufunguzo rwa bose;
- Kuva kuri byte 67 gushika kuri byte 79, nta n’imwe igira.


Igice gisomwa n'umuntu (HRP) muri rusangi congerwako mu ntango y'itegeko ry'ukwishyura n'umubare wo gusuzuma ku mpera, hanyuma kigashirwa mu base58. Ubwubatsi bw’itegeko ry’ukwishura rero burasa cane n’ubw’urufunguzo rwagutse. Ehe kode yanje yo kwishura BIP47 muri base58 nk'akarorero:


```text
PM8TJSBiQmNQDwTogMAbyqJe2PE2kQXjtgh88MRTxsrnHC8zpEtJ8j7Aj628oUFk8X6P5rJ7P5qD
udE4Hwq9JXSRzGcZJbdJAjM9oVQ1UKU5j2nr7VR5
```


Mu gushirwa mu ngiro kwa PayNym kwa BIP47, amakode y’ukwishura arashobora kandi kugaragazwa mu buryo bw’ibimenyetso bifitaniye isano n’ishusho y’ururobo. Ehe ivyanje, nk’akarorero:


```text
+throbbingpond8B1
```


Ikoreshwa ry’amakode yo kwishura n’ugushirwa mu ngiro kwa PayNym ubu riboneka kuri Sparrow wallet kuri PC no kuri Samourai Wallet kuri telefone ngendanwa.