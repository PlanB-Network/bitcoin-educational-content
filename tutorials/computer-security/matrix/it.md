---
name: Matrice
description: Una guida alla comprensione, alla configurazione e all'utilizzo di Matrix, la piattaforma di comunicazione sicura, aperta e decentralizzata.
---

![cover](assets/cover.webp)



## Che cos'è Matrix?



Matrix è un **protocollo di comunicazione decentralizzato** progettato per consentire lo scambio di messaggi, file e chiamate audio/video tra utenti e applicazioni, senza dipendere da un'impresa centrale. A differenza delle piattaforme di messaggistica tradizionali, Matrix è un'infrastruttura **aperta**, paragonabile alla posta elettronica: chiunque può scegliere un server o gestirne uno in proprio, mantenendo la capacità di scambiare con il resto della rete.



Matrix si distingue per tre principi fondamentali:



### Un protocollo, non un'applicazione



Matrix non è un'applicazione come WhatsApp o Telegram.


È un linguaggio standardizzato che molte applicazioni possono utilizzare.


In altre parole, un'ampia varietà di software Element, FluffyChat, Cinny, Nheko e altri, forniscono accesso alla stessa rete Matrix.



Questo garantisce una libertà totale: cambio di applicazione senza perdita di contatti, diversità di interfacce, indipendenza da un unico fornitore.



![capture](assets/fr/03.webp)



### Una rete decentralizzata e federata



La struttura di Matrix si basa sulla **federazione**, un modello in cui diversi server indipendenti collaborano tra loro.


Ogni server (chiamato _homeserver_) può ospitare utenti, chat e sincronizzare i messaggi con gli altri server della rete.


Così :





- nessuna singola entità controlla l'intero sistema;
- un server può scomparire senza influenzare il resto della rete;
- ogni organizzazione o individuo può gestire il proprio spazio.



Questo modello garantisce una **alta resilienza** e riflette i valori della sovranità tecnologica.



![capture](assets/fr/03.webp)



### Un sistema sicuro e criptato



Matrix supporta la **crittografia end-to-end (E2EE)** per scambi privati e gruppi crittografati.


I messaggi possono essere letti solo dai partecipanti, non dai server intermedi.


Questo approccio consente di comunicare senza esporre il contenuto degli scambi a terzi, mantenendo la trasparenza del protocollo e la possibilità di ospitare un proprio server.



![capture](assets/fr/05.webp)



### Interoperabilità unica



Uno dei punti di forza di Matrix è la sua capacità di fungere da **ponte tra diversi sistemi di comunicazione**. Grazie ai _ponti_, è possibile collegare :





- Telegram
- WhatsApp
- Signal
- Messaggero
- Slack
- Discordia
- IRC, XMPP, ecc.



In questo modo è possibile unificare le comunità sparse su diverse piattaforme, mantenendo il controllo sull'infrastruttura.



![capture](assets/fr/06.webp)



## Come funziona Matrix?



Questa sezione presenta la struttura interna della rete Matrix per capire come utenti, server e applicazioni interagiscono all'interno di questo ecosistema decentralizzato. Matrix si basa su tre elementi essenziali: _homeserver_, identità e _clienti_ utilizzati per comunicare.



### Server: homeserver



Matrix viene eseguito su server indipendenti chiamati _homeserver_.


Ogni homeserver gestisce :





- gli account utente che ospita,
- conversazioni private e salotti a cui questi utenti partecipano,
- sincronizzazione con altri server di rete.



Tutti gli homeerver collegati alla rete Matrix si scambiano automaticamente messaggi ed eventi dai salotti condivisi. Ad esempio:





- un utente registrato sul server A può chattare con un utente sul server B,
- un salone può essere distribuito su decine di server,
- nessuno ha il controllo su un salone o su una comunità nel suo complesso.



Questo modello è altamente resiliente e consente a ogni organizzazione o individuo di gestire la propria infrastruttura.



### Identificatori della matrice



Ogni utente ha un identificatore unico, chiamato **MXID** (_Matrix ID_), che assomiglia a un indirizzo:



```bash
@nomdutilisateur:serveur.xyz
```



Si compone di :





- un nome utente, preceduto da **@**
- il nome del server su cui è stato creato l'account, preceduto da **:**



Esempi:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Questo identificatore consente di comunicare con qualsiasi altro utente di Matrix, indipendentemente dal server di origine.



### Client della matrice (applicazioni)



Per utilizzare Matrix, è necessario connettersi con un'applicazione chiamata **client Matrix**.



I più noti sono :





- Elemento (web, mobile, desktop)
- FluffyChat (mobile)
- Cinny (web/desktop minimalista)
- Nheko (desktop)



Queste applicazioni non sono altro che interfacce per :





- per visualizzare i messaggi,
- inviare testo, immagini o file,
- partecipare o creare fiere,
- effettuare chiamate audio/video.



Tutte le applicazioni comunicano con i server attraverso lo stesso protocollo standardizzato.



### Stanze e messaggi privati (DM)



In Matrix, gli scambi avvengono in **camere** :





- una stanza può essere pubblica o privata
- può contenere due persone o migliaia
- può essere condiviso tra più server
- ha un identificatore univoco che inizia con **!



I messaggi privati sono semplicemente delle chat con due partecipanti, spesso chiamate **DM (Direct Messages)**.



La sincronizzazione del salone avviene in tempo reale tra i server partecipanti, garantendo un'esperienza senza soluzione di continuità e mantenendo la decentralizzazione.



## Perché utilizzare Matrix?



Matrix non è solo un'alternativa ai sistemi di messaggistica centralizzati: è una tecnologia che risponde a esigenze reali in termini di sovranità digitale, sicurezza e interoperabilità. Sono molte le ragioni per cui sempre più persone, aziende e istituzioni scelgono questo protocollo per comunicare.



### Riprendete il controllo delle vostre comunicazioni



La maggior parte delle piattaforme di messaggistica opera secondo un modello centralizzato: un unico operatore controlla i server, l'accesso, i dati e le regole di utilizzo. Questo modello implica una dipendenza totale dal fornitore.


Matrix adotta un approccio diverso.


Chiunque può scegliere dove ospitare il proprio account, o addirittura distribuire il proprio server. Nessuna entità è in grado di bloccare un utente, di richiedere un'identificazione invasiva o di imporre un cambiamento di politica.


Questa architettura restituisce autonomia sia agli individui che alle organizzazioni. Le comunicazioni non si basano più sulla fiducia in un'azienda, ma su un protocollo aperto, documentato e verificabile.



### Comunicazione sicura e crittografata



Matrix supporta la crittografia end-to-end per le conversazioni private e i gruppi. Questo meccanismo garantisce che solo i partecipanti possano leggere i messaggi, anche se questi passano attraverso server di terze parti nella federazione.



Il protocollo utilizza l'algoritmo Megolm/Olm, progettato appositamente per garantire una forte sicurezza in ambienti distribuiti e multidispositivo.



In questo modo è possibile :





- proteggere le conversazioni sensibili,
- impedire l'accesso non autorizzato (anche dal server host),
- mantenere la riservatezza a lungo termine.



La crittografia non è un'opzione: è un componente fondamentale del protocollo.



### Non più dipendenti da un'unica applicazione



Matrix non è un'applicazione, ma un protocollo.



Questa diversità di clienti garantisce :





- una scelta adeguata alle esigenze individuali,
- la possibilità di utilizzare Matrix su qualsiasi tipo di dispositivo,
- nessuna dipendenza da un singolo software.



Se un cliente non è adatto o cessa di essere mantenuto, è sufficiente selezionarne un altro: il conto continua a funzionare normalmente.



### Federare e interconnettere diverse comunità



La federazione consente a diversi server di lavorare insieme pur essendo gestiti in modo indipendente.


Così :





- un'organizzazione può gestire il proprio homeserver,
- i singoli individui possono unirsi ai server pubblici,
- tutti possono comunicare tra loro come se fossero sulla stessa piattaforma.



Questa flessibilità permette di creare spazi di comunicazione adatti a ogni esigenza: team, associazioni, comunità, istituzioni o progetti open source.



Matrix è particolarmente popolare nei circoli tecnici, nei collettivi di attivisti, nei ricercatori, nei governi e, sempre più, nelle comunità Bitcoin.



### Interoperabilità unica nel panorama della messaggistica



Uno dei principali punti di forza di Matrix è la sua capacità di **estendere** gli scambi grazie a ponti in grado di collegare :





- WhatsApp
- Telegram
- Signal
- Slack
- Discordia
- IRC
- XMPP
- e molte altre piattaforme



Matrix diventa quindi uno strato unificante per le comunicazioni, che riunisce diverse comunità sparse in diverse applicazioni.



Questa interoperabilità riduce la frammentazione e semplifica la collaborazione.



### Un protocollo libero, aperto e sostenibile



Il protocollo Matrix è interamente open source e sviluppato in modo trasparente.


Questo garantisce diversi vantaggi:





- una continua evoluzione dello standard,
- la possibilità per chiunque di controllare il codice,
- indipendenza da cambiamenti commerciali o politici,
- resilienza a lungo termine.



A differenza dei sistemi di messaggistica proprietari, il futuro di Matrix non dipende da una singola azienda, ma da una comunità globale e da uno standard aperto.



## Come si crea un account Matrix?



La creazione di un account Matrix è semplice e non richiede competenze tecniche. Gli utenti possono unirsi a un server esistente, creare un login e iniziare a chattare immediatamente. Questa sezione illustra i passaggi essenziali.



### Scegliere un server (pubblico o privato)



Matrix è una rete federata: ci sono numerosi server (homeserver) gestiti da diverse organizzazioni, comunità o individui. La scelta del server determina solo il luogo in cui l'account è ospitato, ma non impedisce la comunicazione con l'intera rete.


**Sono disponibili due opzioni:**



### - Utilizzare un server pubblico



Questa è la soluzione più semplice.


Esempi di server popolari:





- _matrix.org_ (il più noto)
- _envs.net_
- server comunitari tematici (tecnologia, privacy, open-source...)



Questi server sono adatti agli utenti inesperti che vogliono registrarsi rapidamente.



### - Utilizzare un server privato



Ideale per :





- un'organizzazione,
- una famiglia,
- un progetto open source,
- un gruppo di lavoro,
- o per un uso sovrano e autonomo.



In questo caso, qualcuno deve amministrare il server (Synapse, Dendrite, Conduit...).


Indipendentemente dal server scelto, gli utenti possono parlare tra loro grazie alla federazione.



### Creare un account passo dopo passo



Poiché Matrix è un protocollo aperto, può essere utilizzato da diverse applicazioni.


Come descritto in precedenza, offrono interfacce e funzionalità diverse a seconda dei requisiti:





- Element**: il client più completo, disponibile su tutte le piattaforme.
- FluffyChat**: semplice, moderno e ideale per i cellulari.
- Nheko**: client leggero ed ergonomico per PC.
- SchildiChat**: Variante dell'elemento con miglioramenti ergonomici.
- NeoChat**: integrato nell'ecosistema KDE.



La scelta del client non ha alcun impatto sull'account: tutti funzionano con qualsiasi server Matrix.



### Passi classici :





- Aprire l'applicazione scelta. Nel nostro caso, lo faremo con [Element](app.element.io).
- Selezionare "Crea un account".



![cover-kali](assets/fr/10.webp)



Per semplicità, è possibile creare un account Matrix utilizzando **Google, Facebook, Apple, GitHub o GitLab**. Questi servizi sapranno solo che il loro account è stato usato per accedere a Matrix: si tratta di una **connessione sociale**.



Per una maggiore riservatezza, è possibile registrarsi anche manualmente scegliendo un **nome utente**, una **password** e un **indirizzo e-mail**.



A seconda del server scelto, potrebbe essere richiesto un **captcha** e l'accettazione dei **termini di utilizzo**.



Una volta convalidata la registrazione, viene inviata un'e-mail di conferma.


È sufficiente fare clic sul link per attivare il proprio account e accedere all'applicazione web (Element) per partecipare alle prime conversazioni Matrix.



![cover-kali](assets/fr/11.webp)



Ora avete un account e utilizzate la versione Web di Element.



## Aggiungere il primo contatto



Per comunicare con qualcuno su Matrix, è sufficiente conoscere il suo identificativo completo, chiamato **Matrix ID**.



Esempio:



`@alice:matrix.org @bened:monserveur.bj`



### Aggiungere un contatto



Per invitare gli amici alla chat di gruppo, fare clic sul cerchio "i" nell'angolo in alto a destra. Si apre il pannello di destra. Cliccate su "Persone" per visualizzare l'elenco dei membri della stanza: al momento dovreste essere gli unici presenti.



![cover-kali](assets/fr/12.webp)



Fare clic su "Invita in questa stanza" nella parte superiore dell'elenco delle persone e si aprirà una richiesta per invitare gli amici a unirsi a voi in Matrix. Se hanno già effettuato l'accesso a Matrix, inserite il loro ID Matrix. Se non lo sono, inserite il loro indirizzo e-mail e saranno invitati a unirsi a noi.



Non esiste un sistema di "amici": un contatto è semplicemente una persona con cui è stata aperta una conversazione.



![cover-kali](assets/fr/13.webp)



La persona invitata può accettare o rifiutare l'invito. Se accetta, dovrebbe entrare nella stanza. Più sono, meglio è!



![cover-kali](assets/fr/14.webp)



### Impostazione del proprio server



Matrix si rivela davvero efficace quando viene utilizzato insieme a un server personale.


La distribuzione del proprio homeserver consente di :





- mantenere il controllo completo sui dati,
- definire le proprie regole di utilizzo,
- ospitare più account (amici, squadra, comunità),
- e garantire la massima resilienza in caso di restrizioni o censure.



**Soluzioni disponibili





- Synapse**: l'implementazione storica e più completa.
- Dendrite**: più leggero, più potente e progettato per il futuro del protocollo.
- Conduit**: una variante minimalista facile da distribuire.



**Prequisiti:**





- un nome di dominio,
- una macchina o un VPS,
- competenze minime di amministrazione di sistema.



Anche se richiede un po' di configurazione, la gestione del proprio server trasforma Matrix in uno strumento sovrano e duraturo.



### Partecipare alle prime fiere



Matrix si basa molto sulle _camere_ (salotti).


Ci sono fiere pubbliche, private, comunitarie, tecniche, locali e internazionali.



**Tre modi per entrare a far parte di un salone



1. **Tramite un link di invito** (spesso sotto forma di URL `matrix.to`).


2. **Cercare il nome del salone** nell'applicazione.


3. **Inserendo l'ID completo dello spettacolo**, ad esempio :


`#bitcoin:matrix.org`


#communauté-bénin:monsrv.bj`



Una volta entrati, la chatroom si comporta come un classico newsgroup, con cronologia, crittografia, file, reazioni e chiamate audio/video, a seconda del client utilizzato.



![capture](assets/fr/09.webp)



## Andare oltre



Una volta acquisite le basi, Matrix offre una serie di possibilità avanzate. Se volete collegare altri sistemi di messaggistica, ospitare il vostro server o organizzare una comunità, l'ecosistema è molto ricco.



### Ponti (WhatsApp, Telegram, Signal, ecc.)



Un ponte collega Matrix ad altri sistemi di messaggistica.


Con esso è possibile inviare e ricevere messaggi da :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Discordia
- Slack**
- IRC** (IRC)
- e molti altri



### Cosa possono fare i ponti





- Centralizzare tutte le conversazioni in Matrix
- Fornire un'interfaccia aperta per l'interazione con i servizi proprietari
- Gestire una comunità multipiattaforma da un'unica postazione



Alcuni ponti sono ufficiali, altri sono a livello di comunità.


A seconda del dipartimento, possono richiedere :





- un server personale,
- una configurazione aggiuntiva,
- o l'utilizzo di un ponte pubblico esistente.



### Utilizzo di Matrix per un'organizzazione, una comunità o un progetto Bitcoin



Matrix non è solo uno strumento personale.


Può essere utilizzato per strutturare gruppi di lavoro, organizzare comunità locali o gestire la comunicazione di un progetto.



**Esempi di utilizzo:**





- Comunità open-source
- Progetti dell'ecosistema Bitcoin e Lightning
- Gruppi di studenti o sviluppatori
- Organizzazioni di cittadini
- Media indipendenti
- Gruppi e associazioni locali



**Perché è interessante?





- strumento 100% open-source**
- Comunicazione sovrana e decentralizzata**
- Spazi organizzati in **salotti**, **sottogruppi**, **salotti privati**, ecc.
- Integratevi con Nextcloud, GitLab, Mattermost o con bot personalizzati
- Gestione accurata dei permessi e della moderazione



Matrix diventa quindi un pilastro della comunicazione per qualsiasi struttura che desideri rimanere indipendente dalle grandi piattaforme centralizzate.



## Conclusione



Matrix rappresenta una soluzione moderna, aperta e sicura per la comunicazione in tempo reale, offrendo un'alternativa decentralizzata alle piattaforme tradizionali. Grazie alla sua architettura federata e ai protocolli di crittografia avanzati, consente agli utenti di mantenere il controllo dei propri dati e di godere di un'esperienza fluida e interoperabile. Che si tratti di uso personale, professionale o comunitario, Matrix offre una struttura robusta e scalabile per costruire ambienti di comunicazione adatti alle esigenze di oggi.



Per saperne di più e scoprire tutte le funzionalità offerte da Matrix, è possibile consultare la documentazione ufficiale disponibile qui:


[https://matrix.org/docs/](https://matrix.org/docs/)