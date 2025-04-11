---
term: OP_CHECKHASHVERIFY (CHV)

---
En ny opcode foreslått i 2012 i BIP17 av Luke Dashjr som skulle tilby de samme funksjonene som `OP_EVAL` eller P2SH. Den skulle hashe slutten av `scriptSig`, sammenligne resultatet med toppen av stakken, og gjøre transaksjonen ugyldig hvis de to hashene ikke stemte overens. Denne opkoden ble aldri implementert.