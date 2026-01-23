---
term: BIP0173

definition: Formát adresy bech32 pro SegWit V0 s předponou bc1q, nabízející lepší čitelnost a detekci chyb.
---
Zavedení formátu adresy bech32 pro adresy SegWit V0. Tento formát adres je charakterizován předponou `bc1q`. Formát bech32 nabízí několik výhod:


- Vyžaduje méně místa v kódech QR;
- Je pro člověka snáze interpretovatelný;
- Má inovativní mechanismus kontrolního součtu, který je účinnější a umožňuje detekci a případnou automatickou opravu překlepů.

Tyto funkce usnadňují používání přijímacích adres a zároveň minimalizují riziko chyb.