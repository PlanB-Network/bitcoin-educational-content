---
term: TESTIMONE DI SCRIPT

---
Un elemento nelle voci delle transazioni SegWit che contiene le firme e le chiavi pubbliche necessarie per sbloccare i bitcoin inviati nella transazione. Simile allo `scriptSig` delle transazioni Legacy, lo `scriptWitness` non è tuttavia collocato nella stessa posizione. Infatti, è questa parte, denominata "testimone" (`*witness*` in inglese), che viene spostata in un database separato per risolvere il problema della malleabilità delle transazioni. Ogni ingresso SegWit ha il proprio `scriptWitness`, e tutti gli elementi `scriptWitness` insieme formano il campo `Witness` della transazione.

> ► *Fare attenzione a non confondere `scriptWitness` con `witnessScript`. Mentre il `scriptWitness` contiene i dati di testimonianza per qualsiasi ingresso SegWit, il `witnessScript` definisce le condizioni di spesa di un UTXO P2WSH o P2SH-P2WSH e costituisce uno script a sé stante, simile al `redeemScript` per un'uscita P2SH.*