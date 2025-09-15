---
name: NOSTR

description: Scopri e inizia a utilizzare NOSTR
---


![Un nuovo sfidante è arrivato](assets/1.webp)

*Alla fine di questa guida, comprenderai cos'è Nostr, avrai creato un account e sarai in grado di utilizzarlo.*

## Che cos'è Nostr?

Nostr è un protocollo che ha il potere di sostituire Twitter, Telegram e gli altri social media. Si tratta di un protocollo aperto, semplice e in grado di creare una volta per tutte una rete sociale globale resistente alla censura.

## Come funziona?

Nostr si basa su tre componenti: coppie di chiavi, client e relay.

Ogni utente ha una o più identità, ogni identità è determinata da una coppia di chiavi crittografiche.

Per accedere alla rete, è necessario utilizzare un software client e connettersi a dei relay per ricevere ed emettere contenuti.

![Sistema di chiavi](assets/2.webp)

## 1. Le chiavi crittografiche

A differenza di Facebook o Twitter, dove l'utente deve fornire un indirizzo email e una serie di informazioni a un'azienda privata, Nostr funziona in assenza di un'autorità centrale. L'utente genera una coppia di chiavi crittografiche, una chiave segreta (chiamata anche chiave privata) e una chiave pubblica.

La chiave segreta, nsec, conosciuta solo dall'utente, viene utilizzata per autenticarsi e pubblicare contenuti.

La chiave pubblica, npub, è un identificatore unico a cui è associato tutto il contenuto pubblicato da un utente. La tua chiave pubblica è una sorta di nome utente che consente agli altri utenti di trovarti e iscriversi al tuo feed Nostr.

## 2. I client

I client sono software che consentono di interagire con Nostr. I principali client sono:

- iOS: damus
- Android: amethyst
- Web: iris.to; snort.social; astral.ninja

I client consentono a un utente di generare una nuova coppia di chiavi (equivalente a creare un account) o autenticarsi con una coppia di chiavi preesistente.

## 3. I relay

I relay sono server semplici che puoi abbandonare in qualsiasi momento se non ti piace il contenuto che ti inviano. Puoi anche gestire il tuo relay, se lo desideri.

> 💡 Suggerimento da professionista: I relay a pagamento sono generalmente più efficaci nel filtrare lo spam e i contenuti indesiderati.

## Guida

Ora hai abbastanza conoscenze su Nostr per iniziare e creare la tua prima identità su questo protocollo.

Per questa guida, useremo iris.to (https://iris.to/) poiché questo client web funziona su qualsiasi piattaforma.

## Passaggio 1: Generazione delle chiavi

ris creerà per te un set di chiavi senza che tu debba fare altro che inserire un nome (reale o fittizio) per il tuo profilo. Clicca poi su GO e il gioco è fatto!

![Menu principale](assets/3.webp)

> ⚠️ Attenzione! Dovrai tenere traccia delle tue chiavi se vuoi poter accedere nuovamente al tuo profilo una volta chiusa la sessione. Ti mostrerò come fare, alla fine di questa guida.

## Passaggio 2: Pubblicare un contenuto

Per pubblicare un contenuto, niente di più semplice e intuitivo che scrivere qualche parola nel campo di pubblicazione.

![Pubblicazione](assets/4.webp)

Ecco fatto! Hai pubblicato il tuo primo post su Nostr.

![Post](assets/5.webp)

## Passaggio 3: Trovare un amico

Trova me su Nostr e non sarai più solo. Mi iscrivo anche io a tutti coloro che si iscrivono al mio feed. Per farlo, ti basterà inserire la mia chiave pubblica

npub1hartx53w6t3q5wv9xdqdwrk7h6r5866t8u775q0304zedpn5zgssasp7d3 nella barra di ricerca.

![Il mio profilo](assets/6.webp)

Clicca su "follow" e entro pochi giorni mi iscriverò anche io al tuo feed. Saremo amici. Sarà un piacere anche leggerti se vorrai scrivermi un messaggio.

Inoltre, assicurati di iscriverti anche al feed di Agora256 per ricevere una nota ogni volta che pubblichiamo qualcosa di nuovo: npub1ag0rawstycy7nanuc6sz4v287rneen2yapcq3fd06972f8ncrhzqx

## Passaggio 4: Personalizza il tuo profilo

Hai ancora un po' di lavoro da fare per personalizzare il tuo profilo. Per farlo, clicca sull'avatar che iris ha generato automaticamente per te nell'angolo in alto a destra dello schermo e poi clicca su "modifica profilo".

![Profilo](assets/7.webp)

Non ti resta che indicare a iris dove trovare la tua immagine e la tua immagine di copertina su internet. Ti consiglio di ospitare tu stesso i tuoi contenuti: proteggi ciò che ti appartiene.

![Altra opzione](assets/8.webp)

Se preferisci, puoi anche scaricare delle immagini, che saranno conservate per te da iris su nostr.build, un servizio gratuito di hosting di contenuti visivi per Nostr.

Come puoi vedere, puoi anche configurare il tuo client per essere in grado di ricevere e inviare sats. In questo modo potrai ricompensare gli autori dei contenuti che ti sono piaciuti o, ancora meglio, accumulare sats tu stesso per i fantastici contenuti che pubblicherai.

## Passaggio 5: Backup del set di chiavi

Questo passaggio è cruciale se vuoi mantenere l'accesso al tuo profilo una volta disconnesso dal client o quando la tua sessione sarà scaduta.
D'abord, clicca sull'icona "settings" rappresentata da un ingranaggio
![Setting](assets/9.webp)

Poi, copia e incolla uno dopo l'altro i tuoi npub, npub hex, nsec e nsec hex in un file di testo che terrai al sicuro. Ti consiglio di criptare questo file, se sai come farlo.

![Clef](assets/10.webp)

> ⚠️ Presta attenzione all'avviso che ti dà iris. Se puoi condividere la tua chiave pubblica senza preoccupazioni, non è lo stesso per la tua chiave privata. Chiunque la possieda potrà accedere al tuo account.

## Conclusion

Ecco fatto, piccola struzzo, hai fatto i tuoi primi passi su Nostr. Ora dovrai imparare a correre alla velocità della luce. Presto pubblicheremo delle guide che ti mostreranno come gestire le tue chiavi e come integrare lightning nella tua esperienza Nostr con l'aiuto di getalby.
