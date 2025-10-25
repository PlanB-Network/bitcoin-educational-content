---
name: Alias Vault
description: Potente tool per gestire password, autenticazione a due fattori e alias (con server email incorporato) - Anche self hosted!
---

![cover](assets/cover.webp)

La privacy e la sicurezza online sono un argomento che chiunque, a prescindere dalla propria attività,  dovrebbe tenere in grande considerazione.

Questi temi sono, inoltre, parte di un mondo in continuo fermento: sempre più sviluppatori partecipano all'argomento, portando implementazioni a soluzioni già consolidate e nuovi prodotti.

È il caso di **Leendert de Borst** e del suo `Alias Vault`, un rivoluzionario strumento (il primo nel suo genere) che consente di gestire e memorizare le password, usare i record delle stesse per autenticarsi ai servizi web, amministrare l'autenticazione a due fattori, ma soprattutto generare veri e propri _alias_, tutto in un'uninca interfaccia.

**Ma Alias Vault non si ferma qui**.

## Caratteristiche principali

Alias Vault lavora in cloud sui server dello sviluppatore o self-hosted nella propria infrastruttura, opzione per la quale sono disponibili file e immagine Docker da installare con uno scipt. Oltre all'interfaccia web, sono disponibili le estensioni per tutti i browser più utilizzati, nonché le app mobili per iOS e Android; quest'ultima si può scaricare anche da F-Droid, bypassando lo store ufficiale di Google.

In un'unica interfaccia Alias Vault è:
- **Free e open source**
- **Password Manager**, per memorizzare tutte le password complesse. Grazie all'estensione del browser, il password manager completa i login ai siti web
- **2FA**, per supportare l'autenticazione a due fattori
- **Alias manager con server email incorporato**: Alias Vault non crea alias che inoltrano email ad una casella dell'utente, bensì crea dei veri e propri alter-ego, con tanto di nome, cognome, gender, username, password e data di compleanno (qualora questo dato sia richiesto).

Fa parte del pacchetto un'ampia e accurata documentazione, che accompagnerà i nuovi arrivati alla scoperta di questo potente tool.

## Niente dati personali!

Si inizia, come sempre, dal sito web [aliasvault.net](aliasvault.net). Come detto, Alias Vault si può utilizzare sul proprio server, oppure dal cloud dello sviluppatore per iniziare a conoscerlo prima di passare alla soluzione self-hosted.

Il sito ha una grafica realmente accattivante e ben curata, ma il bello arriva se inizi a mettere le mani in pasta: **crea il tuo account**.

![img](assets/en/01.webp)

Con enorme sorpresa scoprirai che Alias Vault non chiede informazioni personali: per creare l'account basta un qualunque nickname, una parola a te familiare, purché sia disponibile. Accetta i Termini di Servizio, scegli la parola e prosegui.

![img](assets/en/02.webp)

Imposta adesso la **`master password`** che è il dato più importante di tutto il tuo nuovo sistema. Con quest'unica password, infatti, sarai l'unico a poter accedere/recuperare l'account, in quanto terrà il tuo `vault` criptato sul server che ospiterà le tue informazioni.

![img](assets/en/03.webp)

Fatto: hai creato il tuo password manager e gestore di alias, ma senza dare un tuo indirizzo email funzionante e privato.

![img](assets/en/04.webp)

Alias Vault ti da il benvenuto in uno spazio blindato, nuovo, personale ma anche vuoto. Ed ora iniziamo a popolarlo un po'.

Se hai già un password manager, puoi importare il file da quello in uso, per valutare le differenze con altro provider, o magari eliminare l'alias manager così da gestire tutto in un'unica applicazione.

![img](assets/en/05.webp)

Alias Vault è estremamente semplice: hai una pagina principale, che è la `Home`, con due menu:
- `Credentials`: che  ti permette di creare e poi gestire le identità e gli alias
- `Email`: una inbox dove potrai controllare i messaggiin arrivo per gli alias che hai generato.

![img](assets/en/06.webp)

È la creazione di un primo `alias` che ci interessa fare, pertanto vai nella parte superiore destra della pagina e clicca _+New Alias_.

![img](assets/en/07.webp)

Inizialmente il menu si presenta minimale, come da filosofia di Alias Vault. Per scoprire le caratteristiche di questa funzione, clicca su _Create via advanced mode_.

![img](assets/en/08.webp)

La parte superiore della prima schermata, puoi usarla per importare le credenziali con password che già usi per i servizi con cui hai un abbonamento, o che usi più spesso online.

Se hai attivato l'autentizazione a due fattori su qualcuno dei suddetti servizi (o tutti), con Alias Vault puoi gestire anche questo ulteriore livello di sicurezza, importando la `secret key`. Alias Vault creerà la `TOTP` necessaria per l'accesso.

![img](assets/en/09.webp)

**Attenzione**: nello spazio riservato all'indirizzo email, Alias Vault propone di default il proprio dominio; per poter utilizzare l'indirizzo corretto con cui hai precedentemente creato gli account, clicca su _Enter custom domain_, così da poter impostare il corretto dominio dopo `@`.

![img](assets/en/14.webp)

La parte inferiore di questa schermata è quella più divertente. Clicca su _Generate Random Alias_ e Alias Vault creerà per te identità separate per diverse necessità, ognuna delle quali con la propria casella d posta, password di livello molto robusto, integrate con altri dettagli come il gender, la data di nascita e un nickname adatto.

![img](assets/en/10.webp)

Da un apposto menu, puoi cambiare le impostazioni che riguardano la generazione delle password, scegliendo ad esempio solo lettere minuscole ed eliminando i caratteri che possono risultare ambigui.

![img](assets/en/11.webp)

Puoi usare l'email dell'alias suggerito da Alias Vault, o cambiare dominio se clicchi sul menu a tendina corrispondente.

![img](assets/en/12.webp)

Prima di usare questa email per un servizio di login puoi provarne la funzionalità, inviando un messaggio da un tuo indirizzo alla casella di posta elettronica appena nata.

![img](assets/en/13.webp)

**⚠️ ATTENZIONE**: La ricezione delle email è possibile grazie al server incorporato di Alias Vault, ma questo permette esclusivamente di ricevere email e non di rispondere, o usare la casella email con le funzioni "convenzionali" di un servizio `alias`. Si differenzia quindi molto da Simple Login, Addy ed altre piattaforme che si dedicano esclusivamente a questo tipo di servizio. Per l'esempio di Simple Login è possibile visionare il tutorial dedicato:

https://planb.network/tutorials/computer-security/communication/simple-login-c17a10d6-8f84-4f97-8d50-7a83428d0f41

Per cancellare un alias che hai creato a titolo di prova, non dovrai far altro che accedere alla tua `Home`, poi `Credentials` e cliccare sull'identità da cancellare. In alto a destra ti compare il comando _Delete_ per procedere.

![img](assets/en/16.webp)

## Estensione del browser

A seconda di quelle che sono le tue necessità, puoi ricorrere all'estensione del browser, che puoi trovare sui browser più utilizzati.

![img](assets/en/15.webp)

Si installa come già hai fatto con tutte le altre estensioni, non mi soffermerò su questo particolare.

L'estensione del browser è lì per facilitare le operazioni di login ai servizi online, o per creare nuovi alias all'occorrenza: se il servizio è memorizzato tra i tuoi record di Alias Vault, l'auto-fill fa quel che serve.

![img](assets/en/17.webp)

L'unica attenzione è verificare che Alias Vault sia attivo. L'applicazione ha infatti un'impostazione di default, per cui si mette in pausa dopo un periodo di inattività. È una funzione molto utile, **quando ti devi ad esempio allontanare dal computer ed evitare che qualcun altro possa accedere ai tuoi account**. Una procedura snella ti permetterà di accedere nuovamente immettendo la `master password`, se la sessione precedente è ancora nella cache. Il tempo per la disconnessione è uno dei parametri che puoi personalizzare, accorciandolo o allungandolo a seconda delle tue preferenze.

## App mobile

Come tutte le applicazioni di questo genere che si rispettino, Alias Vault ha la versione per dispositivi mobili, sia in ambiente Android sia iOS. Per Android è possibile scaricare l'app da [F-Droid](https://f-droid.org/packages/net.aliasvault.app/).

Al momento della stesura di questa guida (fine agosto 2025), l'app mobile considera l' `auto-fill` una feature sperimentale, non funziona se non con pochissimi siti. Finché non verrà implementata a tutti gli effetti, per usare Alias Vault in mobilità è necessario fare copia/incolla dei dati.

Una volta scaricata l'app dallo store, per fare login ti basterà inserire user e `master password` creati sulla web app.

![img](assets/en/18.webp)

Durante l'apertura del tuo `vault`, ti verrà chiesto se vuoi attivare l'accesso con controllo biometrico, un ulteriore livello di sicurezza per evitare che qualcun altro possa accedere alle tue password, se per caso ha in mano il tuo telefono.

![img](assets/en/19.webp)

Se decidi impostare il controllo biometrico, procedi. Se salti il passaggio e cambi idea, potrai configurarlo anche in seguito dal menu dei _Settings_.

Completato l'accesso, ritroverai sincronizzati i dati che hai già creato.

![img](assets/en/20.webp)

L'app per cellulare può essere instradata al collegamento verso il`vault` ospitato sul proprio server. 

![img](assets/en/22.webp)

Ed è appunto la versione self-hosted che affronteremo, brevemente, nel prossimo paragrafo.

## Self-Hosting: pieno controllo sui tuoi dati

Alias Vault, a onor del vero, non è il primo `password manager` che permette di implementare il servizio sulla tua infrastruttura. Ce ne sono altri, ma alcuni o hanno delle limitazioni o sono parzialmente closed source.

L'opportunità è unica: **fine della dipendenza da fornitori di servizi o cloud esterni, ma usare il tuo server locale per custodire e gestire le password, gli alias e le informazioni estremamente sensibili associate a tutto ciò**. Con Alias Vault puoi anche far puntare il servizio email verso il tuo server di posta elettronica, per una maggiore confidenzialità.

È il momento di ricorrere alla [documentazione](https://docs.aliasvault.net/installation/), per scoprire come procedere per self-hostare Alias Vault.

![img](assets/en/23.webp)

Alias Vault gira su Docker Compose, pertanto è richiesta una minima esperienza con Linux e Docker. Puoi iniziare con l'installazione base, per poi completare con le soluzioni più evolute.

Il tuo server deve girare su una macchina 64 bit, con distribuzione Linux, 1 GB di RAM e almeno 16 GB di memoria di archiviazione; la versione di Docker (CE) dev'essere almeno la 20.10 o superiore, mentre per Docker Compose è necessaria una release dalla 2.0 in su.

Io ho deciso di provare Alias Vault con un thin client, sul quale è istallata DietPi come distribuzione, una base Debian Bookworm, ottimizzata all'essenziale e su cui già girano `Docker` e `Docker Compose`.

Per prima cosa, al fine di avere un po' di ordine, crea una directory nella tua home, apri il `terminale` e incolla il comando per lanciare lo script di installazione.

```bash
curl -L -o install.sh https://github.com/lanedirt/AliasVault/releases/latest/download/install.sh
```

![img](assets/en/24.webp)

![img](assets/en/25.webp)

Al termine dell'installazione, troverai le tue credenziali per l'accesso:
```
  Admin Panel: https://localhost/admin
  Username: admin
  Password: yyy0xyx1yxy2zxx4
```

Controlla il contenuto della directory dopo l'installazione.

![img](assets/en/29.webp)

Per lanciare Alias Vault usa il comando:

``` Launch-Alias-Vault
./install.sh start
```

Alias Vault adesso gira sul tuo server personale.

![img](assets/en/30.webp)

Apri un browser e digita l'url: ti comparirà la pagina per fare login come `Admin` di Alias Vault.

![img](assets/en/26.webp)

Il più è fatto! Hai davanti a te il pannello per amministrare Alias Vault in maniera personalizzata.

![img](assets/en/27.webp)

Da questa interfaccia, potrai controllare quanti e quali utenti stanno utilizzando il servizio, limitarne l'uso, cancellare gli utenti (azione irreversibile) e soprattutto controllare tutti i `log`.

Se si tratta di una nuova installazione, non avrai altri utenti oltre ad `admin`; per crearne di nuovi, apri un'altra `tab` del browser e digita:

```
localhost/user/start
```

![img](assets/en/28.webp)

Da qui in poi, tutto procede come abbiamo visto in precedenza nella guida, con la differenza che adesso stai usando Alias Vault sul tuo server. Se la tua macchina è adeguatamente configurata e protetta, questo è un modo elegante e sicuro di gestire un tuo password e alias manager, senza servizi di terze parti.

Per fermare Alias Vault, torna al terminale e digita:

``` Stop-Alias-Vault
./install.sh stop

```

![img](assets/en/31.webp)

## Considerazioni su cifratura e sicurezza

![img](assets/en/32.webp)

Secondo quanto dichiara Lanedirt sul sito, nella documentazione e su Github, con Alias Vault **tutte le informazioni (componenti) che inserirai su Alias Vault, rimangono strettamente legate al dispositivo, cifrate e inaccessibili a chiunque non conosca la `master password`**.

La `master password`è dunque l'elemento fondamentale dell'intero `vault`. Dopo il suo inserimento, viene processata con l'algoritmo `Argon2id`, una funzione di derivazione di chiavi hard-memory, per impedire che il segreto esca dal dispositivo.

Tutto resta nascosto anche al gestore del cloud o del servizio di hosting. Infatti, dal pannello di amministrazione non si accede ai dettagli degli utenti, si può solo sapere se hanno creato alias, ricevuto email e poco altro.

Tutti i contenuti archiviati vengono cifrati e decifrati da chiavi crittografiche derivate dalla `master password`. **Sul server sono conservati solo i dati cifrati, niente compare in chiaro**. Se un utente dimentica o perde la sua `master password`, l'account ad essa collegato è irreversibilmente perso, in quanto il server non riesce ad avere accesso ai contenuti in chiaro.

Per la versione self-hosted esiste lo script che consente di azzerare la `master password`, ma questo non impedisce la perdita dei dati.

![img](assets/en/33.webp)

Essendo Alias Vault in fase _Beta_ potresti avere difficoltà di accesso in caso di cambio/aggiornamento della master password. Ti suggerisco di sceglierla robusta e complessa fin dall'inizio, in modo da poter sperimentare il servizio e, infine, decidere se utilizzarlo. In caso di difficoltà di accesso al cloud, a seguito dell'aggiornamento password, contatta il supporto di Alias Vault.

Per una completa comprensione dell'architettura e della sicurezza adottate da Alias Vault, ti consiglio vivamente di consultare [questa pagina](https://docs.aliasvault.net/architecture/), che contiene i dettagli della crittografia alla base del suo funzionamento.

## Roadmap
Le intenzioni degli sviluppatori sono di rendere Alias Vault maturo e stabile entro la fine del 2025, in modo da definirne le caratteristiche d'uso future.

Alias Vault è e rimarrà sempre open source e free, ma probabilmente non in maniera illimitata come in fase beta. Alcune feature a pagamento stanno per essere implementate, in quanto già annunciate.

Sono previsti piani per team/famiglie e il supporto alle chiavi hardware, queste ultime per l'autenticazione con FIDO2 o WebAuth.

## A chi serve Alias Vault

**Uno strumento così è ideale per tutti coloro che mettono la privacy online al centro dell'attenzione**.

La tua identità è, con tutta probabilità, il cuore dell'attività che svolgi online e va salvaguardata con ogni mezzo, per mettere **quei** dati al riparo da servizi, aziende e broker disposti a tutto pur di mettere le mani sui tuoi comportamenti online.

Alias Vault ti restituisce il completo controllo sulle credenziali, mitigando o eliminando del tutto la necessità di affidarsi a terze parti per la custodia e cifratura dei dati più sensibili.

L'architettura e l'impianto crittografico di Alias Vault sono ideali per individui sovrani, piccole e medie imprese, team di sviluppo e tutti gli appassionati di applicazioni **open source**. Se fai parte di una di queste categorie: buon divertimento alla scoperta di Alias Vault.
