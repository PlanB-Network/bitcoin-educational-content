---
term: INDIRIZZO DI RICEZIONE

---
Informazioni utilizzate per ricevere bitcoin. Un indirizzo è solitamente costruito mediante l'hashing di una chiave pubblica, utilizzando `SHA256` e `RIMPEMD160`, e aggiungendo metadati a questo digest. Le chiavi pubbliche utilizzate per costruire un indirizzo di ricezione fanno parte del portafoglio dell'utente e sono quindi derivate dal suo seme. Ad esempio, gli indirizzi SegWit sono composti dalle seguenti informazioni:


- Un HRP per designare "bitcoin": `bc`;
- Un separatore: `1`;
- La versione di SegWit utilizzata: `q` o `p`;
- Il payload: il digest della chiave pubblica (o direttamente la chiave pubblica nel caso di Taproot);
- Il checksum: un codice BCH.

Tuttavia, un indirizzo di ricezione può rappresentare anche qualcos'altro, a seconda del modello di script utilizzato. Ad esempio, gli indirizzi P2SH sono costruiti utilizzando l'hash dello script. Gli indirizzi Taproot, invece, contengono direttamente la chiave pubblica modificata, senza ricorrere all'hash.

Un indirizzo di ricezione può essere rappresentato sotto forma di stringa alfanumerica o di codice QR. Ogni indirizzo può essere utilizzato più volte, ma è una pratica altamente sconsigliata. Infatti, per mantenere un certo livello di privacy, si consiglia di utilizzare ogni indirizzo Bitcoin una sola volta. Un nuovo indirizzo deve essere generato per ogni pagamento in entrata nel proprio portafoglio. Un indirizzo è codificato in `Bech32` per gli indirizzi SegWit V0, in `Bech32m` per gli indirizzi SegWit V1 e in `Base58check` per gli indirizzi Legacy. Da un punto di vista tecnico, ricevere bitcoin significa possedere la chiave privata associata a una chiave pubblica (e quindi a un indirizzo). Quando qualcuno riceve bitcoin, il mittente aggiorna il vincolo esistente sulla sua spesa in modo che solo il destinatario possa avere questo potere.

![](../../dictionnaire/assets/23.webp)