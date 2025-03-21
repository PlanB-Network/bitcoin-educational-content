---
name: Leitfaden für den lokalen Betrieb der Plan ₿ Network-Plattform
description: Wie können Sie das Plan ₿ Network in einer lokalen Umgebung betreiben, um meinen Beitrag zu Inhalten oder das Korrekturlesen/Überprüfen von Bildungsinhalten auf dem Plan ₿ Network zu testen?
---
![github](assets/cover.webp)

## Zusammenfassung

Dieses Tutorial bietet eine schrittweise Anleitung zum Einrichten des Bitcoin-Lernmanagementsystems von Plan ₿ Network auf Ihrem lokalen Rechner unter Verwendung von Docker, Dummy-Schlüsseln und benutzerdefinierten Repository-Konfigurationen.

Falls Sie den obigen Teil nicht verstanden haben, keine Sorge - diese Anleitung ist für Sie!

---
## **Wie man Bitcoin Learning Management System lokal betreibt**

Dieses Tutorial enthält detaillierte Schritte zur Einrichtung der Plattform, zum Umgang mit Dummy-Schlüsseln und zur Anpassung von Repositories. Befolgen Sie die folgenden Schritte, um häufige Probleme zu vermeiden und Ihre lokale Umgebung richtig zu konfigurieren.

**1. Voraussetzungen**


- Linux-Rechner mit installiertem Docker und Docker Compose (es wurde berichtet, dass es auch unter Windows funktioniert).
- ausreichende "nodejs"-Version (getestet: 22.12.0)
- `pnpm` auf Ihrem System installiert haben.
- Git für das Klonen von Repositories konfiguriert.

**2. Klonen des Repositorys**

Klonen Sie das Repository auf Ihren lokalen Rechner:

git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-Lernmanagement-System

```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```

**3. Einrichten von Umgebungsvariablen**

1\. Duplizieren Sie die Datei `.env.example`:

```bash
cp .env.example .env
```

1. Bearbeiten Sie die Datei `.env` und löschen Sie den .example-Teil des Namens, jetzt müssen Sie Dummy-Schlüssel für die benötigten Variablen einfügen. Beispiel:

⚠️ Dies ist ein obligatorischer Schritt, dessen Überspringen zu Fehlern wie der Verweigerung der Verbindung zwischen einigen Containern führen kann.

Vergessen Sie nicht, auch Ihr spezielles Github PAT in die Datei einzufügen

```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```

---
**4. Abhängigkeiten installieren**

stellen Sie sicher, dass Sie eine geeignete Nodejs-Version installiert haben. Ab 2024-12 hat sich v22.12.0 (LTS) als funktionierend erwiesen.

⚠️ Ubuntu 22.04 Repository nodejs Version ist 12.22.9: zu alt, um pnpm installieren zu können

Um nodejs zu installieren, finden Sie Anweisungen [hier] (https://nodejs.org/en/download/package-manager); Sie können zum Beispiel die Installationsmethode `nvm` verwenden.

---
Bevor Sie mit der pnpm-Installationsphase der notwendigen Pakete beginnen, sollten Sie sicherstellen, dass alle Abhängigkeiten installiert sind. Dies können Sie erreichen, indem Sie den folgenden Befehl ausführen:

```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```

---
Führen Sie in Ihrem Ordner `../Bitcoin-learning-management-system/` den folgenden Befehl aus, um `pnpm` zu installieren

```bash
pnpm install
```

__TIP:__ Denken Sie daran, von Zeit zu Zeit sowohl die Abhängigkeiten als auch pnpm selbst zu aktualisieren

**5. Ausführen der Container**

Starten Sie die Entwicklungsumgebung mit Docker in Ihrem Ordner `../Bitcoin-learning-management-system/`:

```bash
docker compose up --build -V
```

Wenn Sie den nächsten Befehl auf diese Weise ausführen, werden Sie die Protokolle nicht in Ihrem Terminal sehen.

```bash
docker compose up -d --build -V
```

Dadurch werden alle erforderlichen Container von Docker erstellt und gestartet.

**6. Zugriff auf die Anwendung**

Sobald die Container in Betrieb sind, rufen Sie das Frontend unter auf:

\[<http://localhost:8181](http://localhost:8181)>

![Plan ₿ Network Local](assets/en/1.webp)

Hinweis: Die Anwendung wird automatisch neu geladen, wenn Sie die Quelldateien ändern.

**7.** Richten Sie Ihre Datenbank ein Schema

Beim ersten Lauf müssen Sie die DB-Migrationen durchführen.

Dazu führen Sie das Migrationsskript aus: "pnpm run dev:db:migrate"

```markdown
pnpm run dev:db:migrate
```

**8. Daten aus dem Repository importieren**

Um Daten in die Datenbank zu importieren, stellen Sie eine Anfrage an die API:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

**9. Sync-Volumen-Zugriffsprobleme beheben**

Wenn Sie Zugriffsprobleme mit den Volumes `cdn` und `sync` haben, führen Sie aus:

```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```

dann wieder:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

![Plan ₿ Network Local](assets/en/2.webp)

**10. Anpassen des Repositorys (optional)**

Wenn Sie einen Fork oder einen bestimmten Zweig verwenden müssen:

1. Bearbeiten Sie die Datei `.env`, um die folgenden Variablen zu aktualisieren:

```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```

2\. Starten Sie Docker neu:

```markdown
docker compose down -v
docker compose up --build -V
```

3\. Synchronisieren Sie die Repository-Daten erneut:

```markdown
curl -X POST http://localhost:3000/api/github/sync
```

Dieses Tutorial stellt sicher, dass die Plattform mit Dummy-Schlüsseln, installierten Abhängigkeiten und nach Bedarf angepassten Repositories korrekt eingerichtet ist. 🎉 Viel Erfolg bei Ihrer Einrichtung!

**Befehle für zusätzliche Hilfe**

alle Container anhalten

```
docker compose down
```

alle vorhandenen Container und Volumina beschneiden

```
docker container prune -f
docker volume prune --all
```

erstellen Sie die Container mit dem gleichen Befehl wie im offiziellen Leitfaden und dem Sync-Skript für das Mittagessen:

```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```
