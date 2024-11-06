---
name: Hinzufügen eines Podcasts zum PlanB Netzwerk
description: Wie fügt man einen neuen Podcast zum PlanB Netzwerk hinzu?
---
![podcast](assets/cover.webp)

Die Mission von PlanB ist es, erstklassige Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Website veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was es jedem ermöglicht, an der Bereicherung der Plattform teilzunehmen.

Möchten Sie einen Bitcoin-Podcast zum PlanB Netzwerk hinzufügen und die Sichtbarkeit Ihrer Show erhöhen, wissen aber nicht wie? Dieses Tutorial ist für Sie!
![podcast](assets/01.webp)
- Zuerst benötigen Sie ein GitHub-Konto. Wenn Sie nicht wissen, wie man eines erstellt, haben wir ein detailliertes Tutorial erstellt, um Sie anzuleiten.

https://planb.network/tutorials/others/create-github-account


- Gehen Sie zu [dem GitHub-Repository von PlanB, das den Daten gewidmet ist](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/podcasts) im Abschnitt `resources/podcasts/`:
![podcast](assets/02.webp)
- Klicken Sie oben rechts auf den Button `Add file`, dann auf `Create new file`:
![podcast](assets/03.webp)
- Wenn Sie noch nie zum Inhalt des PlanB Netzwerks beigetragen haben, müssen Sie Ihren Fork des Original-Repositorys erstellen. Ein Repository zu forken bedeutet, eine Kopie dieses Repositorys auf Ihrem eigenen GitHub-Konto zu erstellen, was es Ihnen ermöglicht, am Projekt zu arbeiten, ohne das Original-Repository zu beeinflussen. Klicken Sie auf den Button `Fork this repository`:
![podcast](assets/04.webp)
- Sie gelangen dann zur GitHub-Bearbeitungsseite:
![podcast](assets/05.webp)
- Erstellen Sie einen Ordner für Ihren Podcast. Um dies zu tun, schreiben Sie in das Feld `Name your file...` den Namen Ihres Podcasts in Kleinbuchstaben mit Bindestrichen anstelle von Leerzeichen. Zum Beispiel, wenn Ihre Show "Super Podcast Bitcoin" heißt, sollten Sie `super-podcast-bitcoin` schreiben:
![podcast](assets/06.webp)
- Um die Erstellung des Ordners zu bestätigen, fügen Sie einfach einen Schrägstrich nach dem Namen Ihres Podcasts in dasselbe Feld ein, zum Beispiel: `super-podcast-bitcoin/`. Das Hinzufügen eines Schrägstrichs erstellt automatisch einen Ordner anstatt einer Datei:
![podcast](assets/07.webp)
- In diesem Ordner erstellen Sie eine erste YAML-Datei mit dem Namen `podcast.yml`:
![podcast](assets/08.webp)
- Füllen Sie diese Datei mit Informationen über Ihren Podcast anhand dieser Vorlage aus:

```yaml
name: 
host: 
language: 
links:
  podcast: 
  twitter: 
  website: 
description: |
  
tags:
  - 
  - 
contributors:
  - 
```

Hier sind die Details, die für jedes Feld ausgefüllt werden müssen:

- **`name`**: Geben Sie den Namen Ihres Podcasts an.
- **`host`**: Listen Sie die Namen oder Pseudonyme der Sprecher oder des Gastgebers des Podcasts auf. Jeder Name sollte durch ein Komma getrennt werden.
- **`language`**: Geben Sie den Sprachcode der Sprache an, in der Ihr Podcast gesprochen wird. Zum Beispiel für Englisch, notieren Sie `en`, für Italienisch `it`...

- **`links`**: Stellen Sie Links zu Ihrem Inhalt bereit. Sie haben zwei Optionen:
	- `podcast`: der Link zu Ihrem Podcast,
	- `twitter`: der Link zum Twitter-Profil des Podcasts oder der Organisation, die ihn produziert,
	- `website`: der Link zur Website des Podcasts oder der Organisation, die ihn produziert.
- **`description`**: Fügen Sie einen kurzen Absatz hinzu, der Ihren Podcast beschreibt. Die Beschreibung muss in der gleichen Sprache sein, wie im Feld `language:` angegeben.
- **`tags`**: Fügen Sie zwei Tags hinzu, die mit Ihrem Podcast in Verbindung stehen. Beispiele:
    - `bitcoin`
    - `technologie`
    - `wirtschaft`
    - `bildung`...

- **`contributors`**: Erwähnen Sie Ihre Mitwirkenden-ID, falls Sie eine haben.

Zum Beispiel könnte Ihre YAML-Datei so aussehen:

```yaml
name: Super Podcast Bitcoin
host: Rogzy, JohnOnChain, Lounes, Fanis, Ajlex, Guillaume, Pantamis, Sosthene, Loic
language: en
links:
  podcast: https://podcasts.apple.com/us/podcast/decouvrebitcoin-replay/id1693844092
  twitter: https://twitter.com/decouvrebitcoin
  website: https://decouvrebitcoin.fr
description: |
  Super Podcast Bitcoin ist eine technische LIVE-Sitzung, die einmal pro Woche auf Twitter stattfindet, um tief in das Bitcoin-Protokoll, Layer-Zwei-Lösungen und alles, was den Verstand begeistert, einzutauchen. Unsere Gastgeber Lounes, Pantamis, Loïc und Sosthene werden Ihre Fragen beantworten und die technischste Show über Bitcoin weltweit bieten.

tags:
  - bitcoin
  - technologie
contributors:
  - rabbit-hole
```

![podcast](assets/09.webp)

- Sobald Sie mit den Änderungen an dieser Datei fertig sind, speichern Sie diese, indem Sie auf den `Commit changes...`-Button klicken:
![podcast](assets/10.webp)
- Fügen Sie einen Titel für Ihre Änderungen hinzu sowie eine kurze Beschreibung:
![podcast](assets/11.webp)
- Klicken Sie auf den grünen `Propose changes`-Button:
![podcast](assets/12.webp)
- Sie gelangen dann auf eine Seite, die alle Ihre Änderungen zusammenfasst:
![podcast](assets/13.webp)
- Klicken Sie oben rechts auf Ihr GitHub-Profilbild und dann auf `Your Repositories`:
![podcast](assets/14.webp)
- Wählen Sie Ihren Fork des PlanB Network-Repositorys aus:
![podcast](assets/15.webp)
- Sie sollten eine Benachrichtigung am oberen Fensterrand mit Ihrem neuen Branch sehen. Er heißt wahrscheinlich `patch-1`. Klicken Sie darauf:
![podcast](assets/16.webp)
- Sie befinden sich jetzt auf Ihrem Arbeitsbranch:
![podcast](assets/17.webp)
- Gehen Sie zurück zum Ordner `resources/podcast/` und wählen Sie den Podcast-Ordner aus, den Sie im vorherigen Commit erstellt haben: ![podcast](assets/18.webp)
- Klicken Sie in Ihrem Podcast-Ordner auf den `Add file`-Button und dann auf `Create new file`:
![podcast](assets/19.webp)
- Benennen Sie diesen neuen Ordner `assets` und bestätigen Sie dessen Erstellung, indem Sie am Ende ein Schrägstrich `/` hinzufügen:
![podcast](assets/20.webp)
- Erstellen Sie in diesem `assets`-Ordner eine Datei mit dem Namen `.gitkeep`:
![podcast](assets/21.webp)
- Klicken Sie auf den `Commit changes...`-Button:
![podcast](assets/22.webp)
- Belassen Sie den Commit-Titel wie vorgegeben und stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, dann klicken Sie auf `Commit changes`:
![podcast](assets/23.webp)
- Kehren Sie zum `assets`-Ordner zurück:
![podcast](assets/24.webp)
- Klicken Sie auf den `Add file`-Button und dann auf `Upload files`:
![podcast](assets/25.webp)
- Eine neue Seite wird geöffnet. Ziehen Sie Ihr Podcast-Logo in den Bereich. Dieses Bild wird auf der PlanB Network-Seite angezeigt: ![podcast](assets/26.webp)
- Achten Sie darauf, dass das Bild quadratisch sein muss, um am besten auf unsere Website zu passen:
![podcast](assets/27.webp)
- Sobald das Bild hochgeladen ist, überprüfen Sie, ob das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, dann klicken Sie auf `Commit changes`:
![podcast](assets/28.webp)
- Achten Sie darauf, dass Ihr Bild `logo` benannt sein muss und im `.webp` Format vorliegen muss. Der vollständige Dateiname sollte daher lauten: `logo.webp`:
![podcast](assets/29.webp)
- Kehren Sie zu Ihrem `assets` Ordner zurück und klicken Sie auf die Zwischendatei `.gitkeep`:
![podcast](assets/30.webp)
- Einmal bei der Datei, klicken Sie auf die drei kleinen Punkte oben rechts und dann auf `Delete file`:
![podcast](assets/31.webp)
- Überprüfen Sie, dass Sie immer noch auf dem gleichen Arbeitsbranch sind, dann klicken Sie auf den `Commit changes` Button:
![podcast](assets/32.webp)
- Fügen Sie einen Titel und eine Beschreibung zu Ihrem Commit hinzu, dann klicken Sie auf `Commit changes`:
![podcast](assets/33.webp)
- Gehen Sie zurück zur Wurzel Ihres Repositories:
![podcast](assets/34.webp)
- Sie sollten eine Nachricht sehen, die darauf hinweist, dass Ihr Branch Änderungen erfahren hat. Klicken Sie auf den `Compare & pull request` Button:
![podcast](assets/35.webp)
- Fügen Sie einen klaren Titel und eine Beschreibung zu Ihrem PR hinzu:
![podcast](assets/36.webp)
- Klicken Sie auf den `Create pull request` Button:
![podcast](assets/37.webp)
Herzlichen Glückwunsch! Ihr PR wurde erfolgreich erstellt. Ein Administrator wird ihn nun überprüfen und, wenn alles in Ordnung ist, in das Hauptrepository von PlanB Network mergen. Sie sollten Ihren Podcast einige Tage später auf der Website sehen.

Bitte stellen Sie sicher, dass Sie den Fortschritt Ihres PR verfolgen. Ein Administrator kann einen Kommentar hinterlassen, der nach zusätzlichen Informationen fragt. Solange Ihr PR nicht validiert ist, können Sie ihn im `Pull requests` Tab im PlanB Network GitHub-Repository sehen:
![podcast](assets/38.webp)
Vielen Dank für Ihren wertvollen Beitrag! :)
