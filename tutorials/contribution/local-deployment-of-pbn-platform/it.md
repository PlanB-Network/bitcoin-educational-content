---
name: Guida all'esecuzione della piattaforma Plan ₿ Network a livello locale
description: Come è possibile eseguire il Plan ₿ Network in un ambiente locale per testare il mio contributo ai contenuti o la correzione/revisione dei contenuti didattici sul Plan ₿ Network?
---
![github](assets/cover.webp)

## In sintesi

Questo tutorial fornisce istruzioni passo passo per configurare il sistema di gestione dell'apprendimento Bitcoin da Plan ₿ Network sulla vostra macchina locale, utilizzando Docker, chiavi fittizie e configurazioni personalizzate dei repository.

Se non avete capito la parte precedente, non preoccupatevi: questo tutorial è per voi!

---
## **Come far funzionare il sistema di gestione dell'apprendimento Bitcoin a livello locale**

Questa guida fornisce i passi dettagliati per configurare la piattaforma, gestire le chiavi fittizie e personalizzare i repository. Seguite i passi seguenti per evitare problemi comuni e configurare correttamente il vostro ambiente locale.

**1. Prerequisiti**


- Macchina Linux con Docker e Docker Compose installati (è stato segnalato che funziona anche su Windows).
- versione sufficiente di `nodejs` (testata: 22.12.0)
- `pnpm` installato sul sistema.
- Git configurato per la clonazione dei repository.

**2. Clonare il repository**

Clonare il repository sul computer locale:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-sistema di gestione dell'apprendimento

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Impostazione delle variabili d'ambiente**

1\. Duplicare il file `.env.example':

```bash
cp .env.example .env
```

1. Modificare il file `.env`, eliminando la parte .example del nome, ora si devono includere chiavi fittizie per le variabili richieste. Esempio:

⚠️ Questo è un passaggio obbligatorio, saltarlo comporterà errori come il rifiuto della connessione tra alcuni contenitori.

Non dimenticate di aggiungere anche il vostro PAT dedicato a Github nel file

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Installare le dipendenze**

assicurarsi di aver installato una versione di nodejs adeguata. A partire dal 2024-12, è stato dimostrato che la versione 22.12.0 (LTS) funziona.

⚠️ La versione del repository Ubuntu 22.04 di nodejs è 12.22.9: troppo vecchia per consentire l'installazione di pnpm

Per installare nodejs, trovare le istruzioni [qui] (https://nodejs.org/en/download/package-manager); per esempio si può scegliere di usare il metodo di installazione `nvm`.

---
Prima di avviare la fase di installazione di pnpm dei pacchetti necessari, assicurarsi che siano installate tutte le dipendenze; è possibile ottenere questo risultato eseguendo il seguente comando:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Nella cartella `../Bitcoin-learning-management-system/`, eseguire il comando seguente per installare `pnpm`

```bash
pnpm install
```

__TIP:__ Ricordarsi di aggiornare di tanto in tanto sia le dipendenze che lo stesso pnpm

**5. Eseguire i contenitori**

Nella cartella `../Bitcoin-learning-management-system/`, avviare l'ambiente di sviluppo con Docker:

```bash
docker compose up --build -V
```

Se eseguite anche il comando successivo in questo modo, non vedrete i log nel vostro terminale.

```bash
docker compose up -d --build -V
```

Questo costruirà e avvierà tutti i contenitori necessari da docker.

**6. Accesso all'applicazione**

Una volta che i contenitori sono in esecuzione, accedere al frontend all'indirizzo:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Nota: l'applicazione si ricarica automaticamente se si modificano i file di origine.

**7.** Impostare il database Schema

Al primo avvio, è necessario eseguire le migrazioni del DB.

Per farlo, eseguire lo script di migrazione: `pnpm run dev:db:migrate`

```markdown
pnpm run dev:db:migrate
```

**8. Importare i dati dal repository**

Per importare i dati nel database, effettuare una richiesta all'API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Correzione dei problemi di accesso al volume di sincronizzazione**

Se si verificano problemi di accesso ai volumi `cdn` e `sync`, eseguire:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

poi di nuovo:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Personalizzazione del repository (opzionale)**

Se è necessario utilizzare un Fork o un ramo specifico:

1. Modificare il file `.env` per aggiornare le seguenti variabili:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Riavviare Docker:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Risincronizzare i dati del repository:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Questa esercitazione assicura che la piattaforma sia configurata correttamente con chiavi fittizie, dipendenze installate e repository personalizzati come necessario. 🎉 Buona fortuna con la configurazione!

**Comandi per un aiuto supplementare**

arrestare tutti i contenitori

```
docker compose down
```

potare tutti i contenitori e i volumi esistenti

```
docker container prune -f
docker volume prune --all
```

ricreare i contenitori con lo stesso comando usato nella guida ufficiale e lo script di sincronizzazione del pranzo:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
