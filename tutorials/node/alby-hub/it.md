---
name: Hub Alby
description: Come si fa a lanciare facilmente il proprio nodo Lightning?
---
![cover](assets/cover.webp)

Alby Hub è l'ultimo software di Alby, l'azienda dietro la popolare estensione web Lightning. Alby Hub è un'interfaccia facile da usare per gestire i nodi Lightning.

In questo tutorial vedremo diversi modi di utilizzare Alby Hub per gestire il proprio nodo Lightning e come collegarlo ad Alby Go, l'applicazione mobile di Alby. Questo vi permetterà di spendere i vostri satelliti in movimento e di essere autonomi nella gestione del vostro nodo.

![ALBY HUB](assets/fr/01.webp)

## Che cos'è Alby Hub?

Nel 2024, Alby ha segnato un cambiamento strategico. Per anni ha offerto una serie di strumenti associati a Bitcoin e alla rete Lightning, tra cui l'iconica estensione Alby, che consente di gestire un portafoglio Lightning, custodiale o meno. Tuttavia, nel 2025, l'azienda prevede di interrompere il servizio di custodia condivisa e di concentrarsi esclusivamente sulle soluzioni di custodia autonoma. Alby Hub sarà il nuovo strumento di punta dell'ecosistema Alby. Questo software consente agli utenti di gestire facilmente il proprio nodo Lightning, mantenendo la proprietà delle chiavi (self-custody).

Alby Hub è uno strumento altamente adattabile. Può soddisfare le esigenze sia dei principianti che degli utenti avanzati. I principianti lo useranno per gestire facilmente un vero nodo Lightning da soli, senza doversi occupare della complessità sottostante. Per gli utenti più esperti, Alby Hub può essere utilizzato come interfaccia completa per la gestione avanzata di un nodo Lightning esistente.

A seconda delle esigenze, Alby Hub è disponibile in 4 configurazioni:


- Alby Hub Cloud :**

Ideale per i principianti, questa prima opzione è l'opzione cloud di Alby. Consente di implementare un nodo Lightning direttamente su un server gestito da Alby, accessibile tramite l'interfaccia di Alby Hub. Sebbene Alby gestisca il server, l'utente mantiene la sovranità sui propri fondi, poiché le chiavi sono crittografate con una password nota solo a lui. Tuttavia, per poter funzionare, le chiavi devono rimanere decifrate nella RAM, il che teoricamente le espone a rischi se qualcuno accede fisicamente al server. È un compromesso interessante per i principianti, ma è importante essere consapevoli dei rischi.

Il vantaggio principale di questa opzione è che si ottiene un nodo Lightning attivo e funzionante 24 ore su 24, 7 giorni su 7, senza dover gestire personalmente l'hosting. Inoltre, i backup del nodo Lightning sono semplificati e automatizzati, rispetto alle opzioni self-hosted in cui è necessario gestire personalmente i backup dei canali.

Alby offre questo servizio per 21.000 satelliti al mese (tariffa di dicembre 2024, soggetta a modifiche, [controllare i prezzi](https://albyhub.com/#pricing)). La tariffa viene detratta automaticamente dal vostro nodo tramite una fattura Lightning emessa da Alby. Questo avviene tramite una connessione NWC che configura il nodo per pagare automaticamente le fatture Alby relative all'abbonamento.


- Hub di Alby con un nodo esistente :**

Se avete già un nodo ospitato, ad esempio su Umbrel o Start9, Alby Hub può essere utilizzato come interfaccia di gestione avanzata, allo stesso modo di ThunderHub o RTL.


- Alby Hub locale :**

È anche possibile installare Alby Hub e il nodo direttamente sul PC, anche se questa opzione è meno pratica, in quanto il PC deve rimanere sempre attivo per accedere da remoto al nodo Lightning. Tuttavia, questa alternativa potrebbe essere adatta alle vostre esigenze specifiche.


- Alby Hub su un server personale :**

Per gli utenti avanzati, Alby Hub può essere distribuito su un server personale con un semplice comando. Questa opzione non è trattata in questo tutorial, ma potete trovare istruzioni dedicate [su GitHub di Alby](https://github.com/getAlby/hub?tab=readme-ov-file#docker).

Questo tutorial si concentra principalmente sull'interfaccia, che sarà la stessa indipendentemente dall'opzione scelta. Vedremo anche come distribuire Alby Hub con l'opzione cloud a pagamento e poi con l'opzione node-in-box (Umbrel o Start9).

![ALBY HUB](assets/fr/02.webp)

Per l'installazione locale sul PC, [scaricare e installare il software in base al sistema operativo](https://github.com/getAlby/hub/releases), quindi seguire le stesse istruzioni dell'interfaccia.

![ALBY HUB](assets/fr/03.webp)

## Creare un account Alby

Il primo passo è creare un account Alby. Sebbene non sia indispensabile per utilizzare Alby Hub, consente di sfruttare appieno le opzioni disponibili, compresa la possibilità di ottenere un indirizzo Lightning.

Andate su [il sito ufficiale di Alby] (https://getalby.com/) e cliccate sul pulsante "*Crea account*".

![ALBY HUB](assets/fr/04.webp)

Inserite un nickname e un indirizzo e-mail, quindi cliccate su "*Sign up*". Questo indirizzo e-mail verrà utilizzato per accedere al vostro account in seguito.

![ALBY HUB](assets/fr/05.webp)

Inserite il codice di verifica ricevuto via e-mail.

![ALBY HUB](assets/fr/06.webp)

Una volta effettuato l'accesso al proprio account online, fare clic sul pulsante "*Continua*".

![ALBY HUB](assets/fr/07.webp)

Fare nuovamente clic su "*Continua*".

![ALBY HUB](assets/fr/08.webp)

## L'opzione di cloud hosting

Dovrete quindi scegliere tra l'opzione self-hosted, che prevede l'hosting di un nodo Lightning sul vostro hardware, o l'opzione a pagamento che utilizza il cloud di Alby. Inizierò spiegando come procedere con l'opzione Cloud (si noti che si tratta di un'opzione a pagamento, si vedano i dettagli nella sezione precedente).

Fare clic su "*Aggiornamento*".

![ALBY HUB](assets/fr/09.webp)

Confermare cliccando su "*Iscriviti ora*".

![ALBY HUB](assets/fr/10.webp)

Cliccate su "*Lancia Alby Hub*".

![ALBY HUB](assets/fr/11.webp)

Attendere qualche istante mentre il nodo viene creato.

![ALBY HUB](assets/fr/12.webp)

E questo è tutto, il vostro Hub Alby è ora configurato. Nella prossima sezione vi mostrerò come installare Alby Hub su un nodo esistente. Se non ne avete bisogno, potete passare alla sezione successiva per configurare il vostro nodo.

![ALBY HUB](assets/fr/13.webp)

## L'opzione self-hosting

Se preferite usare Alby Hub come interfaccia per il vostro nodo Lightning esistente, avete diverse opzioni: installarlo su un server, localmente sul vostro computer o tramite un nodo-in-box (Umbrel o Start9). L'utilizzo di Alby Hub in queste configurazioni è gratuito. Ci concentreremo sull'opzione node-in-box, poiché ritengo che l'opzione server, senza accesso fisico, presenti rischi simili alla versione cloud, e l'installazione locale su un PC è spesso inadatta.

Per configurarlo su Umbrel (i passaggi per Start9 sono identici), occorre innanzitutto avere un nodo LND già configurato.

Accedere alla propria interfaccia Umbrel e andare al negozio di applicazioni.

![ALBY HUB](assets/fr/14.webp)

Cercate l'applicazione "*Alby Hub*".

![ALBY HUB](assets/fr/15.webp)

Installarlo sul nodo.

![ALBY HUB](assets/fr/16.webp)

L'interfaccia di Alby Hub è pronta. Potete seguire il resto del tutorial come se steste usando l'interfaccia cloud, ma senza le opzioni della versione a pagamento. Inoltre, a differenza della versione cloud, le chiavi sono memorizzate localmente sul vostro nodo, non sui server di Alby.

![ALBY HUB](assets/fr/17.webp)

## Avvio dell'hub di Alby

Fare clic sul pulsante "*Iniziare*".

![ALBY HUB](assets/fr/18.webp)

Alby Hub chiederà quindi di scegliere una password. Questa password è molto importante, perché verrà utilizzata per criptare il portafoglio. Nella versione cloud a pagamento, le chiavi vengono memorizzate sul server Alby, crittografate con questa password che solo voi conoscete, quindi decifrate e memorizzate solo nella RAM per firmare le transazioni quando necessario.

È quindi essenziale scegliere una password forte. Chiunque abbia questa password potrebbe potenzialmente accedere al vostro nodo. Assicuratevi anche di fare uno o più backup fisici di questa password su un pezzo di carta o, meglio ancora, su un pezzo di metallo per una maggiore sicurezza. **Se si perde questa password, sarà impossibile recuperare l'accesso ai bitcoin**, poiché Alby non ha modo di resettarla. La perdita di questa password comporta la perdita dei bitcoin.

Dopo aver scelto e salvato con cura la password, cliccare su "*Crea password*".

![ALBY HUB](assets/fr/19.webp)

Ora si ha accesso al nodo Lightning.

![ALBY HUB](assets/fr/20.webp)

La prima azione da compiere è salvare la frase di recupero, da cui derivano le chiavi. Questa frase vi permette di recuperare l'accesso al vostro portafoglio onchain e, con lo stato più recente dei vostri canali, alla vostra saturazione su Lightning. Per farlo, cliccate su "*Impostazioni*".

![ALBY HUB](assets/fr/21.webp)

Andare quindi alla scheda "*Backup*". Immettere la password per accedervi.

![ALBY HUB](assets/fr/22.webp)

A questo punto avrete accesso alla vostra frase di recupero di 12 parole. Fate uno o più back-up fisici di questa frase su carta o metallo e conservateli in un luogo sicuro.

![ALBY HUB](assets/fr/23.webp)

Una volta salvata la frase, spuntate la casella per confermare il salvataggio e fate clic su "*Continua*".

![ALBY HUB](assets/fr/24.webp)

## Come posso recuperare l'accesso ai miei bitcoin?

Prima di inviare fondi al vostro nodo, è importante capire come recuperarli in caso di problemi e quali informazioni sono necessarie per questo recupero. Il processo varia a seconda della natura dei fondi da recuperare e della modalità di hosting del nodo.

Per gli utenti del cloud a pagamento, il recupero completo dei bitcoin richiede tre elementi essenziali:


- La vostra frase di recupero;
- La vostra password (quella utilizzata per il vostro nodo) ;
- Accesso al vostro account Alby, per recuperare lo stato aggiornato dei vostri canali Lightning.

L'assenza di una di queste 3 informazioni renderebbe impossibile il recupero completo dei bitcoin.

Per chi ospita il proprio nodo, il processo di ripristino è identico a quello di qualsiasi nodo Lightning. Avrete bisogno di :


- La vostra frase di recupero;
- Lo stato aggiornato dei canali Lightning. Per proteggere queste informazioni, Umbrel offre [un'opzione](https://github.com/getumbrel/umbrel/blob/2b266036f62a1594aa60a8a3be30cfb8656e755f/scripts/backup/README.md) per crittografarle e salvarle in modo dinamico e anonimo tramite Tor.

## Acquistate il vostro primo canale Lightning

Ora potete seguire le istruzioni fornite da Alby Hub. Cliccate sul pulsante per aprire il vostro primo canale per i contanti in entrata.

![ALBY HUB](assets/fr/25.webp)

Selezionare "*Aprire un canale*". Se non intendete diventare un nodo di instradamento e non ne avete specificamente bisogno, vi consiglio di optare per i canali privati.

![ALBY HUB](assets/fr/26.webp)

Alby Hub genererà una fattura da pagare. Questo pagamento copre le spese di transazione necessarie per aprire il vostro canale e le spese di servizio dell'LSP (*Lightning Service Provider*) che aprirà un canale verso il vostro nodo, consentendovi di ricevere immediatamente i pagamenti.

![ALBY HUB](assets/fr/27.webp)

Una volta pagata la fattura e confermata la transazione, viene creato il primo canale Lightning.

![ALBY HUB](assets/fr/28.webp)

Nella scheda "*Nodo*", si può notare che ora si dispone di liquidità in entrata, che consente di ricevere pagamenti tramite Lightning.

![ALBY HUB](assets/fr/29.webp)

Per ricevere il pagamento, fare clic sulla scheda "*Portafoglio*" e poi su "*Ricevi*".

![ALBY HUB](assets/fr/30.webp)

Immettere un importo e aggiungere una descrizione, se necessario, quindi fare clic su "*Crea fattura*".

![ALBY HUB](assets/fr/31.webp)

Ho ricevuto il mio primo pagamento di 120.000 sats.

![ALBY HUB](assets/fr/32.webp)

Tornando alla scheda "*Portafoglio*", è possibile controllare il saldo del portafoglio. Si noti che Alby Hub accantona automaticamente 354 satelliti quando si effettua il primo pagamento. Per ogni canale Lightning aperto successivamente, Alby Hub accantonerà automaticamente una riserva equivalente all'1% della capacità del canale. Questa riserva è una misura di sicurezza che consente al vostro nodo di recuperare i fondi del canale in caso di tentativo di frode da parte del vostro pari. Ecco perché, nonostante abbia inviato 120.000 satelliti, nel mio bilancio sono indicati solo 119.646 satelliti.

![ALBY HUB](assets/fr/33.webp)

## Deposito di bitcoin onchain

Se volete avere contanti in uscita per effettuare pagamenti, potete anche aprire un canale voi stessi. Per farlo, è necessario disporre di bitcoin onchain nel proprio portafoglio.

Dalla scheda "*Nodo*", fare clic su "*Deposito*".

![ALBY HUB](assets/fr/34.webp)

Inviare bitcoin all'indirizzo visualizzato. Questo indirizzo deriva dalla frase di recupero precedentemente salvata.

![ALBY HUB](assets/fr/35.webp)

Ho inviato 72.000 satelliti. Ora sono visibili in "*Savings Balance*", che comprende tutti i fondi che possiedo su catena e non su Lightning.

![ALBY HUB](assets/fr/36.webp)

## Aprire un canale Lightning

Ora che si dispone di fondi onchain, è possibile aprire un nuovo canale Lightning. È consigliabile aprire più canali, con importi sufficienti a garantire che possiate sempre effettuare pagamenti senza vincoli. La maggior parte degli LSP (*Lightning Service Provider*) richiede un minimo di 150.000 satelliti per aprire un canale con voi.

Nella scheda "*Nodo*", fare clic su "*Aprire canale*".

![ALBY HUB](assets/fr/37.webp)

Selezionare la dimensione del canale. Vi consiglio di non aprire canali troppo piccoli, tenendo presente che si tratta di un nodo Lightning e che la macchina che ospita le vostre chiavi non offre lo stesso livello di sicurezza di un portafoglio hardware. Quindi fate attenzione alle quantità che scegliete di bloccare.

![ALBY HUB](assets/fr/38.webp)

Nel menu "*Opzioni avanzate*" è possibile scegliere con quale LSP aprire il canale o inserire manualmente un altro nodo Lightning.

![ALBY HUB](assets/fr/39.webp)

Quindi fare clic su "*Aprire il canale*".

![ALBY HUB](assets/fr/40.webp)

Attendete che il vostro canale venga confermato sulla catena.

![ALBY HUB](assets/fr/41.webp)

Il nuovo canale apparirà ora nella scheda "*Nodo*".

![ALBY HUB](assets/fr/42.webp)

## Collegare un'applicazione per le spese

Ora che avete un nodo Lightning funzionante, potete usarlo per ricevere e spendere i satelliti su base giornaliera. Sebbene l'interfaccia web di Alby Hub sia comoda per gestire il nodo, non è l'ideale per effettuare transazioni rapide in movimento. Per questo motivo, utilizzeremo un'applicazione per il portafoglio Lightning installata sul nostro smartphone.

In questa guida, vi consiglio di optare per Alby Go, che è molto facile da usare, ma potete anche utilizzare altre applicazioni compatibili come Zeus.

![ALBY HUB](assets/fr/43.webp)

Per installare Alby Go, accedere al negozio di applicazioni del proprio dispositivo:


- [Per Android](https://play.google.com/store/apps/details?id=com.getalby.mobile);
- [Per Apple](https://apps.apple.com/us/app/alby-go/id6471335774).

![ALBY HUB](assets/fr/44.webp)

Gli utenti Android possono anche installare l'applicazione tramite il file `.apk` [disponibile su GitHub di Alby](https://github.com/getAlby/go/releases).

![ALBY HUB](assets/fr/45.webp)

Una volta avviata l'applicazione, fare clic su "*Connect Wallet*".

![ALBY HUB](assets/fr/46.webp)

In Alby Hub, nella scheda "*Connessioni*", fare clic su "*Aggiungi connessione*".

![ALBY HUB](assets/fr/47.webp)

Assegnate un nome a questa connessione per identificarla facilmente nel vostro Hub e selezionate le autorizzazioni che desiderate concedere all'applicazione. Nel mio caso, ho scelto "*Accesso completo*" per avere pieno accesso ai fondi del mio nodo Lightning dal mio smartphone, ma è anche possibile limitare l'accesso con un budget massimo, selezionare le funzioni consentite o impostare una data di scadenza per queste autorizzazioni. Una volta configurati, fate clic su "*Avanti*".

![ALBY HUB](assets/fr/48.webp)

Alby Hub genererà quindi un segreto per stabilire la connessione.

![ALBY HUB](assets/fr/49.webp)

Tornare all'applicazione Alby Go, scansionare il codice QR o incollare il segreto.

![ALBY HUB](assets/fr/50.webp)

Fare clic su "Fine*".

![ALBY HUB](assets/fr/51.webp)

Ora è possibile accedere in remoto al proprio nodo Lightning dal proprio smartphone, semplificando la spesa e la ricezione dei satelliti durante gli spostamenti quotidiani.

![ALBY HUB](assets/fr/52.webp)

Se necessario, è possibile gestire le autorizzazioni per questa connessione direttamente su Alby Hub facendo clic su di essa.

![ALBY HUB](assets/fr/53.webp)

Per ricevere i satelliti, è sufficiente cliccare su "*Ricevi*".

![ALBY HUB](assets/fr/54.webp)

Modificare l'importo e la descrizione della fattura cliccando su "*Fattura*".

![ALBY HUB](assets/fr/55.webp)

Addebitare la fattura per ricevere i satelliti.

![ALBY HUB](assets/fr/56.webp)

Per inviare i satelliti, cliccare su "*Invio*".

![ALBY HUB](assets/fr/57.webp)

Eseguire la scansione della fattura che si desidera pagare.

![ALBY HUB](assets/fr/58.webp)

Quindi fare clic su "*Pagare*".

![ALBY HUB](assets/fr/59.webp)

La transazione è confermata.

![ALBY HUB](assets/fr/60.webp)

Facendo clic sulla piccola freccia, è possibile accedere alla cronologia delle transazioni.

![ALBY HUB](assets/fr/61.webp)

Queste transazioni sono visibili anche sul vostro Alby Hub.

![ALBY HUB](assets/fr/62.webp)

## Personalizzate il vostro indirizzo Lightning

Alby offre l'opzione di un indirizzo Lightning. Questo vi permette di ricevere pagamenti sul vostro nodo senza dover generare manualmente una fattura ogni volta. Per impostazione predefinita, Alby vi assegna un indirizzo Lightning, ma potete personalizzarlo. Accedete al vostro account online Alby, cliccate sul vostro nome nell'angolo in alto a destra, quindi selezionate "*Impostazioni*".

![ALBY HUB](assets/fr/63.webp)

Passare al menu "*Indirizzo del fulmine*".

![ALBY HUB](assets/fr/64.webp)

Modificate il vostro indirizzo, quindi confermate cliccando su "*Aggiorna il tuo indirizzo lightning*".

![ALBY HUB](assets/fr/65.webp)

Una volta che il vostro indirizzo è stato modificato, non vi appartiene più. Assicuratevi quindi di non inviargli mai più sati.

Ecco fatto, ora sapete come usare Lightning con il vostro nodo utilizzando lo strumento Alby Hub. Se avete trovato utile questa esercitazione, vi sarei molto grato se metteste un pollice verde qui sotto. Sentitevi liberi di condividere questo articolo sui vostri social network. Grazie mille!

Per comprendere nel dettaglio tutti i meccanismi di Lightning che abbiamo manipolato in questo tutorial, vi consiglio vivamente di scoprire la nostra formazione gratuita sull'argomento:

https://planb.network/courses/lnp201