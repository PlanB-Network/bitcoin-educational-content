---
term: FIRMA CIECA
---

Le firme cieche di Chaum sono una forma di firma digitale in cui l'emittente della firma non conosce il contenuto del messaggio che sta firmando. Tuttavia, la firma può essere verificata in seguito con il messaggio originale. Questa tecnica è stata sviluppata dal crittografo David Chaum nel 1983.

Considera l'esempio di un'azienda che desidera autenticare un documento confidenziale, come un contratto, senza rivelarne il contenuto. L'azienda applica un processo di mascheramento che trasforma crittograficamente il documento originale in modo reversibile. Questo documento modificato viene inviato a un'autorità di certificazione che applica una firma cieca senza conoscere il contenuto sottostante. Dopo aver ricevuto il documento firmato mascherato, l'azienda rimuove il mascheramento dalla firma. Il risultato è un documento originale autenticato dalla firma dell'autorità, senza che quest'ultima abbia mai visto il contenuto originale.

Quindi, le firme cieche di Chaum consentono la certificazione dell'autenticità di un documento senza conoscerne il contenuto, garantendo sia la riservatezza dei dati dell'utente sia l'integrità del documento firmato.

In Bitcoin, questo protocollo viene utilizzato nei sistemi delle banche Chaumiane come un overlay (Cashu, Fedimint, ecc.), ma soprattutto nei protocolli di coinjoin Chaumiani, per garantire che il coordinatore non sia in grado di collegare un input a un output.