---
name: Hinzufügen von Bildungsmaterialien
description: Wie fügt man neue Bildungsmaterialien im PlanB Netzwerk hinzu?
---
![event](assets/cover.webp)

Die Mission von PlanB ist es, führende Bildungsressourcen über Bitcoin in möglichst vielen Sprachen bereitzustellen. Alle Inhalte, die auf der Seite veröffentlicht werden, sind Open-Source und werden auf GitHub gehostet, was es jedem ermöglicht, an der Bereicherung der Plattform teilzunehmen.

Neben Tutorials und Schulungen bietet das PlanB Netzwerk auch eine umfangreiche Bibliothek mit vielfältigen Bildungsinhalten über Bitcoin, die für jeden zugänglich sind, [im Abschnitt "BET" (_Bitcoin Educational Toolkit_)](https://planb.network/resources/bet). Diese Datenbank umfasst Bildungsposter, Memes, humorvolle Propagandaposter, technische Diagramme, Logos und andere Werkzeuge für Nutzer. Das Ziel dieser Initiative ist es, Einzelpersonen und Gemeinschaften, die weltweit über Bitcoin lehren, durch Bereitstellung der notwendigen visuellen Ressourcen zu unterstützen.

Möchten Sie an der Bereicherung dieser Datenbank teilnehmen, wissen aber nicht wie? Dieses Tutorial ist für Sie!

*Es ist zwingend erforderlich, dass alle in die Seite integrierten Inhalte frei von Rechten sind oder die Lizenz der Quelldatei respektieren. Außerdem werden alle auf dem PlanB Netzwerk veröffentlichten Visuals unter der [CC-BY-SA](https://creativecommons.org/licenses/by-sa/4.0/) Lizenz zur Verfügung gestellt.*
![event](assets/01.webp)
- Zuerst müssen Sie ein Konto auf GitHub haben. Wenn Sie nicht wissen, wie Sie ein Konto erstellen, haben wir ein detailliertes Tutorial erstellt, um Sie zu führen.

https://planb.network/tutorials/others/create-github-account


- Gehen Sie zu [dem GitHub-Repository von PlanB, das den Daten gewidmet ist](https://github.com/PlanB-Network/bitcoin-educational-content/tree/dev/resources/bet) im Abschnitt `resources/bet/`:
![event](assets/02.webp)
- Klicken Sie oben rechts auf den Button `Add file`, dann auf `Create new file`:
![event](assets/03.webp)
- Wenn Sie noch nie zu den Inhalten des PlanB Netzwerks beigetragen haben, müssen Sie Ihren Fork des Original-Repositorys erstellen. Ein Repository zu forken bedeutet, eine Kopie dieses Repositorys auf Ihrem eigenen GitHub-Konto zu erstellen, was es Ihnen ermöglicht, am Projekt zu arbeiten, ohne das Original-Repository zu beeinflussen. Klicken Sie auf den Button `Fork this repository`:
![event](assets/04.webp)
- Sie gelangen dann zur GitHub-Bearbeitungsseite:
![event](assets/05.webp)
- Erstellen Sie einen Ordner für Ihren Inhalt. Um dies zu tun, schreiben Sie in das Feld `Name your file...` den Namen Ihres Inhalts in Kleinbuchstaben mit Bindestrichen anstelle von Leerzeichen. In meinem Beispiel, sagen wir, ich möchte ein PDF-Visual der 2048-Wort-BIP39-Liste hinzufügen. Also werde ich meinen Ordner `bip39-wordlist` nennen: ![event](assets/06.webp)
- Um die Erstellung des Ordners zu bestätigen, fügen Sie einfach einen Schrägstrich nach dem Namen in dasselbe Feld ein, zum Beispiel: `bip39-wordlist/`. Das Hinzufügen eines Schrägstrichs erstellt automatisch einen Ordner anstelle einer Datei:
![event](assets/07.webp)
- In diesem Ordner erstellen Sie eine erste YAML-Datei mit dem Namen `bet.yml`:
![event](assets/08.webp)
- Füllen Sie diese Datei mit Informationen zu Ihrem Inhalt anhand dieser Vorlage aus:

```yaml
builder: 
type: 
links:
  download: 
  view: 
    - en: 
tags:
  - 
  - 
contributors:
  - 
```
- **`builder`**: Geben Sie den Identifikator Ihrer Organisation im PlanB-Netzwerk an. Wenn Sie noch keinen "builder"-Identifikator für Ihr Unternehmen haben, können Sie einen mit diesem Tutorial erstellen.

https://planb.network/tutorials/others/add-builder

 Wenn Sie keinen haben, können Sie einfach Ihren Namen, Ihr Pseudonym oder den Namen Ihres Unternehmens verwenden, ohne ein Builder-Profil erstellt zu haben.
- **`type`**: Wählen Sie die Art Ihres Inhalts aus den folgenden zwei Optionen aus:
	- `Educational Content` für Bildungsinhalte.
	- `Visual Content` für andere Arten von diversen Inhalten.

- **`links`**: Geben Sie Links zu Ihren Inhalten an. Sie haben zwei Möglichkeiten:
	- Wenn Sie sich entscheiden, Ihren Inhalt direkt auf PlanBs GitHub zu hosten, müssen Sie die Links zu dieser Datei in den folgenden Schritten hinzufügen.
	- Wenn Ihre Inhalte anderswo gehostet werden, wie auf Ihrer persönlichen Website, geben Sie die entsprechenden Links hier an:
	    - `download`: Ein Link zum Herunterladen Ihres Inhalts.
	    - `view`: Ein Link, um Ihren Inhalt anzusehen (kann der gleiche wie der Download-Link sein). Wenn Ihr Inhalt in mehreren Sprachen verfügbar ist, fügen Sie einen Link für jede Sprache hinzu.

- **`tags`**: Fügen Sie zwei Tags hinzu, die mit Ihrem Inhalt in Verbindung stehen. Beispiele:
	- bitcoin
	- technologie
	- wirtschaft
	- bildung
	- meme...

- **`contributors`**: Erwähnen Sie Ihren Beitragenden-Identifikator, falls Sie einen haben.

Zum Beispiel könnte Ihre YAML-Datei so aussehen:

```yaml
builder: PlanB-Network
type: Educational Content
links:
  download: https://workspace.planb.network/s/fojeJa7ZbftQTwo
  view:
- In meinem Beispiel werde ich die Links vorerst leer lassen, da ich mein PDF direkt auf GitHub hinzufügen werde:
![event](assets/09.webp)
- Sobald Ihre Änderungen an dieser Datei abgeschlossen sind, speichern Sie sie, indem Sie auf den `Commit changes...`-Button klicken:
![event](assets/10.webp)
- Fügen Sie einen Titel für Ihre Änderungen hinzu sowie eine kurze Beschreibung:
![event](assets/11.webp)
- Klicken Sie auf den grünen `Propose changes`-Button:
![event](assets/12.webp)
- Sie gelangen dann auf eine Seite, die alle Ihre Änderungen zusammenfasst:
![event](assets/13.webp)
- Klicken Sie oben rechts auf Ihr GitHub-Profilbild und dann auf `Your Repositories`:
![event](assets/14.webp)
- Wählen Sie Ihren Fork des PlanB Network-Repositorys aus:
![event](assets/15.webp)
- Sie sollten eine Benachrichtigung am oberen Rand des Fensters mit Ihrem neuen Branch sehen. Er heißt wahrscheinlich `patch-1`. Klicken Sie darauf:
![event](assets/16.webp)
- Sie befinden sich jetzt auf Ihrem Arbeitsbranch (**stellen Sie sicher, dass Sie sich auf dem gleichen Branch wie Ihre vorherigen Änderungen befinden, das ist wichtig!**):
![event](assets/17.webp)
- Gehen Sie zurück zum `resources/bet/`-Ordner und wählen Sie den Ordner Ihres Inhalts aus, den Sie im vorherigen Commit erstellt haben:
![event](assets/18.webp)
- Klicken Sie im Ordner Ihres Inhalts auf den `Add file`-Button, dann auf `Create new file`:
![event](assets/19.webp)
- Benennen Sie diesen neuen Ordner `assets` und bestätigen Sie dessen Erstellung, indem Sie am Ende ein Slash `/` setzen:
![event](assets/20.webp)
- In diesem `assets`-Ordner erstellen Sie eine Datei mit dem Namen `.gitkeep`: ![event](assets/21.webp)
- Klicken Sie auf den `Commit changes...` Button: ![event](assets/22.webp)- Belassen Sie den Commit-Titel als Standard und stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, dann klicken Sie auf `Commit changes`: ![event](assets/23.webp)
- Kehren Sie zum `assets` Ordner zurück: ![event](assets/24.webp)
- Klicken Sie auf den `Add file` Button, dann auf `Upload files`: ![event](assets/25.webp)
- Eine neue Seite wird geöffnet. Ziehen Sie ein Thumbnail, das Ihren Inhalt repräsentiert, in den Bereich. Dieses Bild wird auf der PlanB Network Seite angezeigt: ![event](assets/26.webp)
- Es kann eine Vorschau, ein Logo oder ein Icon sein: ![event](assets/27.webp)
- Sobald das Bild hochgeladen ist, stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, dann klicken Sie auf `Commit changes`: ![event](assets/28.webp)
- Achten Sie darauf, dass Ihr Bild `logo` benannt sein muss und im `.webp` Format vorliegen muss. Der vollständige Dateiname sollte daher `logo.webp` sein: ![event](assets/29.webp)
- Kehren Sie zu Ihrem `assets` Ordner zurück und klicken Sie auf die Zwischendatei `.gitkeep`: ![event](assets/30.webp)
- Einmal bei der Datei, klicken Sie auf die drei kleinen Punkte oben rechts und dann auf `Delete file`: ![event](assets/31.webp)
- Stellen Sie sicher, dass Sie immer noch auf dem gleichen Arbeitszweig sind, dann klicken Sie auf den `Commit changes` Button: ![event](assets/32.webp)
- Fügen Sie einen Titel und eine Beschreibung zu Ihrem Commit hinzu, dann klicken Sie auf `Commit changes`: ![event](assets/33.webp)
- Kehren Sie zum Ordner Ihres Inhalts zurück: ![event](assets/34.webp)
- Klicken Sie auf den `Add file` Button, dann auf `Create new file`: ![event](assets/35.webp)
- Erstellen Sie eine neue YAML-Datei, indem Sie sie mit dem Indikator Ihrer Muttersprache benennen. Diese Datei wird für die Inhaltsbeschreibung verwendet. Wenn ich zum Beispiel meine Beschreibung auf Englisch schreiben möchte, benenne ich diese Datei `en.yml`: ![event](assets/36.webp)
- Füllen Sie diese YAML-Datei mit dieser Vorlage aus:

```yaml
name: 
description: |
  
```

- Für den Schlüssel `name` können Sie den Namen Ihres Inhalts hinzufügen;
- Für den Schlüssel `description` müssen Sie einfach einen kurzen Absatz hinzufügen, der Ihren Inhalt beschreibt. Die Beschreibung muss in der gleichen Sprache wie der Dateiname sein. Sie müssen diese Beschreibung nicht in alle unterstützten Sprachen auf der Website übersetzen, da dies von den PlanB-Teams mit ihrem Modell gemacht wird.
Zum Beispiel könnte Ihre Datei so aussehen:

```yaml
name: BIP39 WORDLIST
description: |
  Vollständige und nummerierte Liste der 2048 englischen Wörter aus dem BIP39-Wörterbuch, die zur Kodierung von mnemonischen Phrasen verwendet werden. Das Dokument kann auf einer einzigen Seite ausgedruckt werden.
```

![event](assets/37.webp)
- Klicken Sie auf den `Commit changes...` Button:
![event](assets/38.webp)
- Stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, fügen Sie einen Titel hinzu, dann klicken Sie auf `Commit changes`:
![event](assets/39.webp)
- Ihr Inhaltsordner sollte jetzt so aussehen:
![event](assets/40.webp)
*Wenn Sie es vorziehen, den Inhalt nicht auf GitHub hinzuzufügen und Sie die Links bereits in der `bet.yml`-Datei in den vorherigen Schritten notiert haben, können Sie diesen Abschnitt überspringen und direkt zum Teil übergehen, der die Erstellung des Pull Requests betrifft.*
- Kehren Sie zum Ordner `/assets` zurück:
![event](assets/41.webp)
- Klicken Sie auf den Button `Add file`, dann auf `Upload files`:
![event](assets/42.webp)
- Eine neue Seite wird sich öffnen. Ziehen Sie den Inhalt, den Sie teilen möchten, in das vorgesehene Feld:
![event](assets/43.webp)
- Zum Beispiel habe ich die PDF-Datei der BIP39-Liste hinzugefügt:
![event](assets/44.webp)
- Sobald der Inhalt hochgeladen ist, stellen Sie sicher, dass das Kästchen `Commit directly to the patch-1 branch` angekreuzt ist, dann klicken Sie auf `Commit changes`:
![event](assets/45.webp)
- Kehren Sie zu Ihrem `/assets`-Ordner zurück und klicken Sie auf die Datei, die Sie gerade hochgeladen haben:
![event](assets/46.webp)
- Ermitteln Sie die Zwischen-URL Ihrer Datei. Zum Beispiel ist in meinem Fall die URL:

```url
https://github.com/tutorial-pandul/bitcoin-educational-content/blob/patch-1/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Behalten Sie nur den letzten Teil der URL ab `/resources`:

```url
/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

- Fügen Sie an die Basis der URL folgende Informationen hinzu, um den korrekten Link zu erhalten:

```url
https://github.com/DiscoverBitcoin/bitcoin-educational-content/blob/dev/resources/bet/bip39-wordlist/assets/BIP39-WORDLIST.pdf
```

Was wir hier tun, ist die zukünftige Verlinkung Ihrer Datei zu antizipieren, sobald Ihr Vorschlag in das Quellrepository des PlanB-Netzwerks eingegliedert wurde.
- Gehen Sie zurück zu Ihrer `bet.yml`-Datei und klicken Sie auf das Stiftsymbol: ![event](assets/47.webp)
- Fügen Sie dort Ihren Link hinzu:
![event](assets/48.webp)
- Sobald Ihre Änderungen abgeschlossen sind, klicken Sie auf den Button `Commit changes...`:
![event](assets/49.webp)
- Fügen Sie einen Titel für Ihre Änderungen hinzu sowie eine kurze Beschreibung:
![event](assets/50.webp)
- Klicken Sie auf den grünen Button `Commit changes`:
![event](assets/51.webp)

---

- Wenn alles für Sie gut aussieht, kehren Sie zur Wurzel Ihres Forks zurück:
![event](assets/52.webp)
- Sie sollten eine Nachricht sehen, die darauf hinweist, dass Ihr Branch geändert wurde. Klicken Sie auf den Button `Compare & pull request`:
![event](assets/53.webp)
- Fügen Sie einen klaren Titel und eine Beschreibung für Ihren PR hinzu:
![event](assets/54.webp)
- Klicken Sie auf den Button `Create pull request`:
![event](assets/55.webp)
Herzlichen Glückwunsch! Ihr PR wurde erfolgreich erstellt. Ein Administrator wird ihn nun überprüfen und, wenn alles in Ordnung ist, in das Hauptrepository des PlanB-Netzwerks mergen. Ihr BET sollte einige Tage später auf der Website erscheinen.

Stellen Sie sicher, dass Sie den Fortschritt Ihres PR verfolgen. Ein Administrator kann einen Kommentar hinterlassen, der um zusätzliche Informationen bittet. Solange Ihr PR nicht validiert ist, können Sie ihn im Tab Pull requests im GitHub-Repository des PlanB-Netzwerks einsehen:
![event](assets/56.webp)
Vielen Dank für Ihren wertvollen Beitrag! :)
