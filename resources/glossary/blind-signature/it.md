---
term: FIRMA CIECA

---
Le firme cieche di Chaum sono una forma di firma digitale in cui l'emittente della firma non conosce il contenuto del messaggio che sta firmando. Tuttavia, la firma può essere successivamente verificata con il messaggio originale. Questa tecnica è stata sviluppata dal crittografo David Chaum nel 1983.

Consideriamo l'esempio di un'azienda che vuole autenticare un documento riservato, come un contratto, senza rivelarne il contenuto. L'azienda applica un processo di mascheramento che trasforma crittograficamente il documento originale in modo reversibile. Il documento modificato viene inviato a un'autorità di certificazione che applica una firma cieca senza conoscere il contenuto sottostante. Dopo aver ricevuto il documento firmato e mascherato, l'azienda toglie la maschera alla firma. Il risultato è un documento originale autenticato dalla firma dell'autorità, senza che quest'ultima abbia mai visto il contenuto originale.

Le firme cieche di Chaum consentono quindi di certificare l'autenticità di un documento senza conoscerne il contenuto, garantendo sia la riservatezza dei dati dell'utente che l'integrità del documento firmato.

In Bitcoin, questo protocollo è utilizzato nei sistemi di banche chaumiane come overlay (Cashu, Fedimint, ecc.), ma soprattutto nei protocolli di coinjoin chaumiani, per garantire che il coordinatore non sia in grado di collegare un input a un output.