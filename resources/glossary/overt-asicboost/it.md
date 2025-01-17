---
term: OVERT ASICBOOST

---
La versione aperta e trasparente di AsicBoost. AsicBoost è una tecnica di ottimizzazione algoritmica utilizzata nel mining di Bitcoin. I minatori che utilizzano la versione Overt manipolano il campo `nVersion` del blocco candidato e utilizzano questa modifica come nonce aggiuntivo. Questo metodo lascia invariato il campo `Nonce` effettivo del blocco durante ogni tentativo di hashing, riducendo così i calcoli necessari per ogni SHA256, mantenendo alcuni dati invariati tra i vari tentativi. Questa versione è rilevabile pubblicamente e non nasconde le sue modifiche al resto della rete, a differenza della versione Covert di AsicBoost.