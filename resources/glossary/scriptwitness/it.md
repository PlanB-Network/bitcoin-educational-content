---
termine: SCRIPTWITNESS
---

Un elemento nelle voci di transazione SegWit che contiene le firme e le chiavi pubbliche necessarie per sbloccare i bitcoin inviati nella transazione. Simile allo `scriptSig` delle transazioni Legacy, lo `scriptWitness` non è però collocato nella stessa posizione. Infatti, è questa parte, denominata "testimone" (`*witness*` in inglese), che viene spostata in un database separato al fine di risolvere il problema della malleabilità delle transazioni. Ogni input SegWit ha il proprio `scriptWitness`, e tutti gli elementi `scriptWitness` insieme formano il campo `Witness` della transazione.

> ► *Fai attenzione a non confondere `scriptWitness` con `witnessScript`. Mentre lo `scriptWitness` contiene i dati testimone per qualsiasi input SegWit, il `witnessScript` definisce le condizioni di spesa di un UTXO P2WSH o P2SH-P2WSH e costituisce uno script a sé stante, simile allo `redeemScript` per un output P2SH.*