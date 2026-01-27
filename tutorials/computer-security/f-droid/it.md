---
name: F-Droid
description: Il catalogo delle applicazioni libere e open-source.
---

![cover](assets/cover.webp)

Nell'era digitale, le grandi aziende e le istituzioni stanno lavorando per rendere Internet più centralizzato, portando il controllo nelle proprie mani e ostacolando così la privacy e la libertà di tutti gli utenti. Non è un'utopia, sta già accadendo. Come bitcoiner, la decentralizzazione, il rispetto della privacy e delle libertà individuali sono principi che ti stanno a cuore, soprattutto negli strumenti che utilizzi quotidianamente. Android, a differenza di iOS, ha permesso per anni la coesistenza di diversi app store all'interno del suo ecosistema, dandoti la libertà di trovare e installare applicazioni dalle tue fonti preferite.

In questa guida daremo un'occhiata a F-droid, una directory di applicazioni che rappresenta un'alternativa ai negozi di applicazioni come Google Play Store e Microsoft Store.


## Come iniziare con F-Droid

F-Droid è uno store di applicazioni e strumenti che consente di installare applicazioni gratuite e open-source sulla piattaforma Android. F-droid è un progetto open source avviato nel 2010 da Ciaran Gultnieks e altri collaboratori. L'obiettivo principale del progetto è quello di rendere accessibili le applicazioni open source e di consentire ai promotori di progetti open source di trovare una piattaforma dove pubblicare i propri strumenti senza dover fare riferimento al Google Play Store.

Purtroppo F-Droid non è un'applicazione disponibile su iOS e contiene molti strumenti progettati per i sistemi Android.

È possibile scaricare F-droid dal [sito ufficiale](https://f-droid.org/) in formato APK e installarla manualmente sul proprio telefono Android.

![download](assets/fr/02.webp)

Su Android, assicurati di concedere i permessi di installazione per il browser da cui hai scaricato F-Droid.

Una volta completata l'installazione, F-Droid avvierà un aggiornamento degli elenchi di applicazioni Open Source per 'arricchire' le applicazioni presenti nello store.

![repositories](assets/fr/03.webp)

Ora è possibile installare applicazioni sul telefono senza passare per il Google Play Store.


## La libreria F-Droid

Nell'Application Store troverai diverse categorie di applicazioni adatte alle tue esigenze. Nella scheda **Categorie** troverai oltre 20 tipi di applicazioni, dai browser agli editor di testo libero, e tutte richiedono il minimo di informazioni da parte tua.

Desideri installare un'applicazione specifica? Fai clic sul pulsante **Ricerca**, quindi inserisci il nome dell'applicazione che stai cercando.

![search](assets/fr/04.webp)

F-Droid fornisce informazioni complete su ogni applicazione che si desidera installare.

Cliccando sull'applicazione, troverai, tra le altre cose:

- Caratteristiche e modifiche aggiunte nell'ultima versione disponibile
- Una descrizione dettagliata dell'applicazione, delle sue caratteristiche, delle ragioni del suo utilizzo e della comunità Open Source che sta dietro al progetto.

![features](assets/fr/05.webp)

- La licenza utilizzata dal progetto, i link al codice sorgente e ai problemi riscontrati nell'utilizzo dell'applicazione
- Permessi richiesti dall'applicazione

![permissions](assets/fr/06.webp)

Per saperne di più, consulta il nostro tutorial su Thunderbird:

https://planb.academy/tutorials/computer-security/communication/thunderbird-91d02325-0361-4641-b152-8975890284a8

F-Droid fornisce tutte le informazioni necessarie per decidere se l'utilizzo di un'applicazione protegge i tuoi dati e migliora la tua privacy. Esamina tutte le applicazioni che desideri utilizzare, quindi fai clic sul pulsante **Installa** per scaricare e installare l'applicazione.

Concedi i diritti di installazione di F-Droid abilitando l'opzione nelle impostazioni.

![settings](assets/fr/07.webp)


## Exchange delle tue applicazioni

F-Droid incoraggia la pratica dell'open source e il contributo della comunità, in particolare attraverso l'opzione **Near By** Exchange. Collegati agli utenti intorno a te tramite:

- Rilevamento Bluetooth;
- La stessa rete Wi-Fi;
- Codice QR o IP:PORT Address da inserire nel browser.

Con questa opzione, è possibile condividere e ricevere le applicazioni installate sul telefono Android con amici e familiari in pochi passaggi.

![swap](assets/fr/08.webp)


## Aggiornamenti

Nella scheda **Aggiornamento**, consulta l'elenco degli aggiornamenti disponibili e assicurati di leggere anche le informazioni sulle nuove versioni di ciascuna applicazione per conoscere eventuali modifiche importanti alla versione in uso.

![updates](assets/fr/09.webp)

È inoltre possibile aggiornare l'elenco delle applicazioni disponibili aggiornando la pagina (scorri verso il basso).


## Aggiungere le proprie applicazioni

F-Droid è un progetto Open Source che incoraggia i contributi alle applicazioni che danno priorità alla privacy degli utenti. È possibile aggiungere la propria applicazione mobile Android allo store attraverso i contributi al codice sorgente di F-Droid GitLab.

L'applicazione deve essere open source, con il codice sorgente pubblicamente disponibile su GitHub o GitLab, ad esempio.

È quindi necessario preparare un file YAML (i metadati) che descriva la propria applicazione, includendo tutte le informazioni e i permessi necessari per il suo utilizzo, seguendo il [metadata template](https://f-droid.org/docs/Build_Metadata_Reference/) proposto da F-Droid.

Nella sezione **Sviluppatori** della [documentazione](https://f-droid.org/en/docs/), troverai tutte le risorse necessarie per pubblicare e mantenere le tue applicazioni su F-Droid.

### Integrità e sicurezza

Inserire un'applicazione open source è spesso sinonimo di maggiore sicurezza, ma anche di notevoli rischi. Come si può garantire che non vi siano alterazioni dannose nel codice sorgente di un'applicazione disponibile su F-Droid?

F-Droid compila le applicazioni sui propri server, sulla base del codice sorgente e delle istruzioni di compilazione ufficiali. Ogni applicazione pubblicata viene ricostruita e verificata per garantire che non sia stata compromessa. Ciò garantisce che l'APK offerto sia fedele al codice sorgente pubblicato dagli sviluppatori. Inoltre, ogni applicazione installata tramite F-Droid viene firmata digitalmente e l'impronta digitale della firma viene confrontata con quella annunciata dagli sviluppatori dell'applicazione sul sito web ufficiale o sul repository Git.

Se ti è piaciuto questo tutorial, scopri di più sul nostro corso di sicurezza informatica e gestione dei dati:

https://planb.academy/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1
