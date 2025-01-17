---
term: NVERSIONE

---
Il campo `nVersion` in una transazione Bitcoin è utilizzato per indicare la versione del formato di transazione utilizzato. Permette alla rete di distinguere tra le diverse evoluzioni del formato di transazione nel tempo e di applicare le regole corrispondenti. Questo campo non ha alcun impatto sulle regole di consenso. Ciò significa che qualsiasi valore assegnato a questo campo non comporta l'invalidazione della transazione. Tuttavia, il campo `nVersion` ha regole di standardizzazione che attualmente accettano solo i valori `1` e `2`. Per ora, questo campo è utile solo per l'attivazione del campo `nSequence`.