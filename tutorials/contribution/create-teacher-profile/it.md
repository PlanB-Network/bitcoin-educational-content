---
name: Professore Plan ₿ Network
description: Come posso aggiungere o modificare il mio profilo di insegnante su Plan ₿ Network?
---
![cover](assets/cover.webp)

Se si intende contribuire a Plan ₿ Network scrivendo un nuovo tutorial o un nuovo corso, è necessario avere un profilo docente. Questo profilo vi consentirà di ricevere i crediti appropriati per i contenuti che contribuite alla piattaforma.

Chi ha già partecipato alla creazione di contenuti didattici su Plan ₿ Network probabilmente ha già un profilo di insegnante. Lo si può trovare nella cartella `/professori` [sul nostro repository GitHub] (https://github.com/PlanB-Network/Bitcoin-educational-content/tree/dev/professors). Se il vostro profilo esiste già, trovate il vostro login nel file `professor.yml`.

Per apportare modifiche al proprio profilo, andare alla sezione "Modifica del profilo del docente" alla fine di questa guida.

## Aggiungere un nuovo insegnante con il nostro software

Il modo più semplice per creare il vostro profilo di insegnante su Plan ₿ Network è utilizzare il nostro strumento Python integrato. Ecco come funziona.

### 1 - Configurare l'ambiente locale

È necessario disporre del proprio Fork da [repository Plan ₿ Network su GitHub](https://github.com/PlanB-Network/Bitcoin-educational-content).

Sincronizzare il ramo principale (`dev`) del proprio Fork con il repository dei sorgenti.

Aggiornare il clone locale.

```bash
# Cloner votre fork (si ce n'est pas déjà fait)
git clone https://github.com/<username>/bitcoin-educational-content.git
cd bitcoin-educational-content
# Ajouter le dépôt source en tant que remote upstream
git remote add upstream https://github.com/PlanB-Network/bitcoin-educational-content.git
# Récupérer les dernières modifications depuis le dépôt source
git fetch upstream
# Se positionner sur la branche principale 'dev'
git checkout dev
# Fusionner les modifications de la branche 'dev' du dépôt source dans votre fork
git merge upstream/dev
# Pousser les mises à jour vers votre fork sur GitHub
git push origin dev
```

### 2 - Creare un nuovo ramo

Assicurarsi di essere nel ramo `dev`. Creare un nuovo ramo con un nome descrittivo (per esempio, `add-professor-loic-morel`).

Pubblicate questo ramo sul vostro Fork online.

```bash
# Assurez-vous d’être sur la branche 'dev'
git checkout dev
# Créez une nouvelle branche avec un nom descriptif
git checkout -b add-professor-loic-morel
# Publiez cette branche sur votre fork en ligne
git push -u origin add-professor-loic-morel
```

### 3 - Creare il profilo dell'insegnante

Andare alla cartella `scripts/tutorial-related/data-creator/` sul clone locale. Assicurarsi di aver installato tutte le dipendenze necessarie per il software, avendo prima installato Python :

```bash
pip install -r requirements.txt
```

Avviare quindi il software con il comando :

```bash
python3 main.py
```

Una volta nella pagina iniziale, inserire il percorso locale del clone del repository, la lingua in cui si sta scrivendo e il proprio ID GitHub. Se si sta creando questo profilo per qualcun altro e si dispone già di un profilo Professore, inserire il proprio ID nel campo "*PBN Professor's ID*". Se si sta creando il proprio profilo, non si dispone ancora di un ID professore, poiché si è in procinto di crearne uno, quindi lasciare questo campo vuoto.

Quindi fare clic sul pulsante "*Nuovo professore*".

![Image](assets/fr/01.webp)

Compilare le informazioni richieste (si prega di notare che tutte queste informazioni saranno pubbliche sulla nostra piattaforma e su GitHub):


- Nome del file dell'insegnante (utilizzare nome e cognome o uno pseudonimo, in minuscolo) ;
- Il vostro nome o soprannome ;
- Generazione casuale del login ;
- Il vostro sito web e il vostro profilo X (facoltativo) ;
- Un Lightning Address per ricevere donazioni dai lettori (opzionale) ;
- Selezionare 2 o 3 etichette dall'elenco;
- Fare clic su "*Seleziona immagine*" per scegliere un'immagine del profilo dalle cartelle locali (è possibile utilizzare qualsiasi nome e formato per l'immagine, il software la adatterà automaticamente). Assicuratevi solo che l'immagine sia quadrata);
- Scrivete una breve descrizione del vostro profilo.

Completare la creazione cliccando su "*Crea professore*". In questo modo, tutti i file necessari per il vostro profilo verranno automaticamente inseriti in generate.

![Image](assets/fr/02.webp)

Salvare le modifiche localmente creando un commit con un messaggio esplicativo. Spingere le modifiche sul proprio Fork GitHub.

```bash
# Créez un commit avec un message descriptif
git commit -m "*new professor Loïc Morel*"
# Poussez vos modifications sur votre fork
git push origin add-professor-loic-morel
```

Una volta terminato, creare una richiesta di pull (PR) su GitHub per proporre l'integrazione delle modifiche. Aggiungere un titolo e una breve descrizione alla PR.

### 4 - Correzione di bozze e fusione

Attendere la convalida o il feedback di un amministratore. Se necessario, correggete e inviate nuovi commit.

```bash
# Créez un commit décrivant les corrections apportées
git commit -m "*Corrections suite à la revue du tutoriel green-wallet*"
# Poussez les corrections sur votre fork
git push origin add-professor-loic-morel
```

Una volta che il PR è stato unito, si può cancellare il ramo di lavoro.

## Modificare il profilo dell'insegnante

Se avete imparato a usare Git, modificate il vostro profilo docente creando un nuovo ramo e modificando il file corrispondente direttamente nella cartella esistente. Le modifiche possono essere fatte sia nel file `professor.yml` che nel file markdown, a seconda delle informazioni da correggere. Una volta apportate le modifiche a livello locale, inviarle al proprio Fork e inviare un PR.

Per i principianti, consiglio di effettuare la modifica direttamente tramite il web Interface di GitHub. Assicurarsi di avere un account GitHub. Se non si sa come crearne uno, seguire questo tutorial:

https://planb.network/tutorials/contribution/others/create-github-account-a75fc39d-f0d0-44dc-9cd5-cd94aee0c07c
Andare a [il repository Plan ₿ Network GitHub dedicato ai dati](https://github.com/PlanB-Network/Bitcoin-educational-content/graphs/contributors).

![Image](assets/fr/03.webp)

Fare clic sulla cartella "*professori*", quindi andare alla cartella personale.

![Image](assets/fr/04.webp)

Per modificare i metadati del profilo, come Lightning Address, il nome o i link, selezionare il file "*professor.yml*". Per modificare la vostra descrizione, fate clic sul file YAML della vostra lingua (ad esempio, "*en.yml*" o "*fr.yml*").

Se si modifica la descrizione, ricordarsi di rimuovere tutte le traduzioni obsolete. In seguito, si può provvedere a tradurre la descrizione nelle altre lingue con l'aiuto di un LLM, oppure lasciare solo la descrizione nella propria lingua madre e menzionare nella richiesta di pull che la descrizione richiede la traduzione da parte del nostro team.

![Image](assets/fr/05.webp)

Una volta arrivati al file che si desidera modificare, fare clic sull'icona della matita.

![Image](assets/fr/06.webp)

Se non si dispone già di un Fork dal repository Plan ₿ Network, GitHub suggerisce di crearne uno. Fare clic su "*Fork questo repository*".

![Image](assets/fr/07.webp)

Apportare le modifiche desiderate al file. Al termine, fare clic su "*Commetti modifiche*".

![Image](assets/fr/08.webp)

Inserire un messaggio che descriva la modifica, quindi selezionare "*Proponi modifiche*".

![Image](assets/fr/09.webp)

Verrà visualizzato un riepilogo delle modifiche apportate. Se si desidera apportare ulteriori modifiche al profilo, è possibile tornare alle cartelle ed eseguire ulteriori commit. Al termine, fare clic su "*Crea richiesta di pull*".

Una richiesta di pull è una richiesta fatta per integrare le modifiche dal proprio ramo nel ramo principale del repository Plan ₿ Network, consentendo la revisione e la discussione delle modifiche prima che vengano unite.

![Image](assets/fr/10.webp)

Assicurarsi, all'inizio del Interface, che il ramo di lavoro sia unito al ramo `dev' del repository Plan ₿ Network (che è il ramo principale).

Inserire un titolo che riassuma brevemente le modifiche che si desidera unire al repository sorgente. Aggiungere un breve commento che descriva queste modifiche, quindi fare clic sul pulsante Green "*Create pull request*" per confermare la richiesta di pull:

![Image](assets/fr/11.webp)

Il PR sarà quindi visibile nella scheda "*Pull Request*" del repository Plan ₿ Network principale. Ora non resta che attendere che un amministratore unisca la modifica.

![Image](assets/fr/12.webp)

Se incontrate difficoltà tecniche nell'inviare la vostra modifica, non esitate a chiedere aiuto su [il nostro gruppo Telegram dedicato ai contributi](https://t.me/PlanBNetwork_ContentBuilder). Grazie mille!