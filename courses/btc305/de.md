---
name: Bitcoin und BTCPay Server
goal: Installieren Sie BTCPay Server für Ihr Unternehmen
objectives:
  - Verstehen, was btcpayserver ist.
  - Selbst hosten und BTCPay Server konfigurieren.
  - btcpayserver im täglichen Geschäft nutzen.
---

# Bitcoin und BTCPay Server

Dies ist ein Einführungskurs zum BTCPay Server Operator, geschrieben von Alekos und Bas, der im Plan ₿-Kursformat von melontwist und asi0 angepasst wurde.

EINE UNVOLLENDETE GESCHICHTE

"Das ist Lüge, mein Vertrauen in dich ist gebrochen, ich werde dich überflüssig machen".

Produziert von der BTCPay Server Foundation

+++

# Einführung

<partId>59e43fe3-b494-5da6-b4b4-9df5bdf08916</partId>

## Kritische Anerkennung für den Autor von Bitcoin und BTCPay Server

<chapterId>e1fe6294-3c82-5203-9537-779f9087c35a</chapterId>

Lassen Sie uns damit beginnen, was BTCPay Server ist und woher er kommt. Wir schätzen Transparenz und bestimmte Standards, um Vertrauen im Bitcoin-Bereich zu bilden.
Ein Projekt in diesem Bereich brach diese Werte. Der leitende Entwickler von BTCPay Server, Nicolas Dorier, nahm dies persönlich und machte das Versprechen, sie überflüssig zu machen. Hier sind wir viele Jahre später und arbeiten täglich an dieser Zukunft, vollständig Open-Source.

> Das ist Lüge, mein Vertrauen in dich ist gebrochen, ich werde dich überflüssig machen.
> Nicolas Dorier

Nach den Worten von Nicolas war es an der Zeit, mit dem Aufbau zu beginnen. Viel Arbeit floss in das, was wir jetzt BTCPay Server nennen. Mehr Menschen wollten bei diesem Vorstoß helfen. Die bekanntesten sind r0ckstardev, MrKukks, Pavlenex und der erste Händler, der die Software nutzte, astupidmoose.

Was bedeutet Open Source und was steckt in einem solchen Projekt?

FOSS steht für Freie & Open-Source-Software. Ersteres bezieht sich auf Bedingungen, die es jedem erlauben, Versionen der Software zu kopieren, zu modifizieren und sogar zu verteilen (auch zu Profitzwecken). Letzteres bezieht sich auf das offene Teilen des Quellcodes, was die Öffentlichkeit ermutigt, einen Beitrag zu leisten und ihn zu verbessern.
Dies bringt erfahrene Benutzer, die begeistert sind, zu der Software beizutragen, die sie bereits nutzen und aus der sie Wert schöpfen, was sich im Laufe der Zeit als erfolgreicher erweist als proprietäre Software. Es entspricht dem Bitcoin-Ethos, dass „Informationen frei sein wollen“. Es bringt leidenschaftliche Menschen zusammen, die eine Gemeinschaft bilden, und macht einfach mehr Spaß. Wie Bitcoin ist FOSS unvermeidlich.

### Bevor wir beginnen

Dieser Kurs besteht aus mehreren Teilen. Viele davon werden von Ihrem Klassenlehrer übernommen, Demo-Umgebungen, zu denen Sie Zugang erhalten, ein gehosteter Server für Sie selbst und möglicherweise ein Domain-Name. Wenn Sie diesen Kurs selbstständig absolvieren, beachten Sie bitte, dass die als DEMO gekennzeichneten Umgebungen für Sie nicht verfügbar sein werden.
NB. Wenn Sie diesem Kurs im Klassenzimmer folgen, können sich die Servernamen je nach Ihrer Klassenzimmereinrichtung unterscheiden. Variablen in Servernamen könnten aufgrund dessen unterschiedlich sein.

### Kursstruktur

Jedes Kapitel hat Ziele und Wissensbewertungen. In diesem Kurs werden wir jedes dieser Elemente behandeln und eine Zusammenfassung der Schlüsselfunktionen bei jedem Lernblock (d. h. Kapitel) haben. Illustrationen werden verwendet, um visuelles Feedback zu geben und Schlüsselkonzepte visuell zu verstärken. Ziele werden zu Beginn jedes Lernblocks gesetzt. Diese Ziele gehen über eine Checkliste hinaus. Sie bieten Ihnen eine Anleitung zu einem neuen Fähigkeitsset. Wissensbewertungen stellen zunehmend herausforderndere Einrichtungen Ihres BTCPay Servers dar.

### Was erhalten die Studierenden mit dem Kurs?

Mit dem BTCPay Server-Kurs kann ein Student die grundlegenden Prinzipien, sowohl technisch als auch nicht-technisch, von Bitcoin verstehen. Die umfassende Schulung in der Verwendung von Bitcoin über den BTCPay Server ermöglicht es den Studenten, ihre eigene Bitcoin-Infrastruktur zu betreiben.

### Wichtige Webadressen oder Kontaktmöglichkeiten

Die BTCPay Server Foundation, die es Alekos und Bas ermöglicht hat, diesen Kurs zu schreiben, befindet sich in Tokio, Japan. Die BTCPay Server Foundation kann über die unten aufgeführte Website erreicht werden;

- https://foundation.btcpayserver.org
- Treten Sie den offiziellen Chat-Kanälen bei: https://chat.btcpayserver.org

## Einführung in Bitcoin

<chapterId>5c0bc234-c188-5b4a-94d5-adee87a120e2</chapterId>

### Bitcoin verstehen durch Klassenübungen

Dies ist eine Klassenübung, also wenn Sie diesen Kurs selbst machen, können Sie diese nicht durchführen, aber Sie können trotzdem diese Übung durchgehen. Um diese Aufgabe zu vervollständigen, liegt die Mindestanzahl der Personen zwischen 9 und 11.

Die Übung beginnt nach dem Ansehen der Einführung „Wie Bitcoin und die Blockchain funktionieren“ von der BBC.

![wie bitcoin und die blockchain funktionieren](https://youtu.be/mhE_vvwAiRc)

Für diese Übung sind mindestens neun Personen erforderlich. Diese Übung soll eine physische Vorstellung davon vermitteln, wie Bitcoin funktioniert. Indem jede Rolle im Netzwerk gespielt wird, haben Sie eine interaktive und spielerische Art zu lernen. Diese Übung beinhaltet nicht das Lightning Network.

### Beispiel; Erfordert 9 / 11 Personen

Die Rollen sind:

- 1 Kunde
- 1 Händler
- 7 bis 9 Bitcoin-Knoten

**Das Setup ist wie folgt:**

Kunden kaufen ein Produkt vom Geschäft mit Bitcoin.

**Szenario 1 - Traditionelles Bankensystem**

- Setup:
  - Siehe Diagramme/Erklärer im angehängten Figjam - [Aktivitäts-Schema](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
  - Drei Studentenfreiwillige übernehmen die Rollen von Kunde (Alice), Händler (Bob) und Bank.
- Ablauf der Ereignisse:
  - Kunde- durchstöbert den Online-Shop und findet einen Artikel für 25 $, den er kaufen möchte, und informiert den Händler über seinen Kaufwunsch
  - Händler- bittet um Zahlung.
  - Kunde- sendet Kartendaten an den Händler
  - Händler- leitet Informationen an die Bank weiter (identifiziert sowohl ihre eigene als auch die Identität/Informationen) und fordert Zahlung von
  - Bank sammelt Informationen über den Kunden und den Händler (Alice und Bob) und überprüft, ob das Guthaben des Kunden ausreichend ist.
  - Zieht 25 \$ von Alices Konto ab, fügt 24 \$ zu Bobs Konto hinzu, nimmt 1 \$ für den Service
  - Der Händler erhält das Go von der Bank und versendet den Artikel an den Kunden.
- Kommentare:
  - Bob und Alice müssen eine Beziehung zu einer Bank haben.
  - Bank sammelt identifizierende Informationen über Bob und Alice.
  - Bank nimmt eine Gebühr.
  - Bank muss jederzeit als Verwahrer des Geldes jedes Teilnehmers vertrauenswürdig sein.

**Szenario 2 - Bitcoin-System**

- Setup:
  - Siehe Diagramme/Erklärer im angehängten Figjam - [Aktivitäts-Schema](https://www.figma.com/file/ckmvMq02Jm2MegSsVCDFhc/Day-1-Classroom-Activity?type=whiteboard&node-id=0-1&t=KR31ofMaJX6S95UL-0).
- Ersetzen Sie die Bank durch neun Schüler, die die Rolle eines Computers (Bitcoin-Knoten/Miner) in einem Netzwerk übernehmen, um die Bank zu ersetzen. - Jeder der 9 Computer verfügt über einen vollständigen historischen Datensatz aller jemals getätigten Transaktionen (somit genaue Kontostände ohne Fälschungen) sowie über einen Satz von Regeln:
  - Überprüfen, ob die Transaktion ordnungsgemäß signiert ist (der Schlüssel passt ins Schloss)
  - Gültige Transaktionen im Netzwerk senden und empfangen, ungültige aussortieren (einschließlich solcher, die versuchen, dieselben Mittel zweimal auszugeben)
- Aktualisieren/Hinzufügen von Datensätzen in regelmäßigen Abständen mit neuen Transaktionen, die von einem "zufälligen" Computer empfangen wurden, vorausgesetzt, alle Inhalte sind gültig (Anmerkung: wir ignorieren vorerst die Proof-of-Work-Komponente, der Einfachheit halber), andernfalls diese ablehnen und wie zuvor fortfahren, bis der nächste "zufällige" Computer ein Update sendet
  - Die richtige Menge wurde belohnt, wenn die Inhalte gültig waren.
- Die Abfolge der Ereignisse darstellen:
  - Kunde- stöbert online im Laden und findet einen Artikel für 25 $, den er kaufen möchte, und teilt dem Händler mit, dass er kaufen möchte
  - Händler- bittet um Zahlung, indem er dem Kunden eine Rechnung/Adresse aus seiner Wallet sendet.
  - Kunde- erstellt eine Transaktion (sendet BTC im Wert von 25 $ an eine vom Händler bereitgestellte Adresse) und überträgt sie an das Bitcoin-Netzwerk.
- Computer- empfangen die Transaktion und überprüfen:
  - Es sind mindestens 25 $ in BTC in der gesendeten Adresse vorhanden
  - Die Transaktion ist ordnungsgemäß signiert ("entsperrt" vom Kunden)
  - Wenn dies nicht der Fall ist, wird die Transaktion nicht durch das Netzwerk verbreitet, und wenn doch, dann verbreitet sie sich und wird in Wartestellung gehalten.
  - Händler können überprüfen, dass die Transaktion aussteht und wartet.
- Ein Computer wird "zufällig" ausgewählt, um die vorgeschlagene Transaktion zu finalisieren, indem er "einen Block" mit ihr überträgt; wenn alles stimmt, erhalten sie eine BTC-Belohnung.
  - OPTIONAL/FORTGESCHRITTEN - anstatt einen Computer zufällig auszuwählen, simulieren Sie das Mining, indem Computer würfeln, bis ein vorher festgelegtes Ergebnis eintritt (z.B. der erste, der einen Doppelsechser würfelt, wird ausgewählt)
  - Es kann auch dargestellt werden, was passieren würde, wenn zwei Computer ungefähr gleichzeitig gewinnen, was zu einer Kettenaufteilung führt.
  - Computer überprüfen die Gültigkeit, aktualisieren/hinzufügen Datensätze in ihren Ledgern, wenn die Regeln erfüllt sind, und übertragen den Block an Peers.
  - Der zufällig ausgewählte Computer erhält eine Belohnung für das Vorschlagen eines gültigen Blocks.
  - Händler überprüft, dass die Transaktion abgeschlossen wurde; somit wurden die Mittel erhalten und der Artikel wurde an den Kunden gesendet.
- Kommentare:
  - Beachten Sie, dass keine vorbestehende Bankbeziehung erforderlich war.
  - Keine dritte Partei benötigt, ersetzt durch Code/Anreize.
  - Keine Datensammlung durch jemanden außerhalb des direkten Austauschs und nur die notwendige Menge muss zwischen den Teilnehmern ausgetauscht werden (z.B. Versandadresse).
  - Es ist kein Vertrauen zwischen den Personen erforderlich (außer dass der Händler den Artikel sendet), in vielerlei Hinsicht wie ein Barankauf.
  - Das Geld gehört direkt den Einzelpersonen.
  - Das Bitcoin-Ledger wird der Einfachheit halber in Dollar dargestellt, aber in Wirklichkeit ist es BTC.
  - Wir simulieren eine einzelne Transaktion, die übertragen wird, aber in Wirklichkeit sind mehrere Transaktionen im Netzwerk ausstehend, und Blöcke enthalten gleichzeitig Tausende von Transaktionen. Knoten überprüfen auch, ob doppelte Ausgaben-Transaktionen ausstehend sind (ich würde alle bis auf eine aussortieren, wenn dies der Fall wäre).
- Betrugsszenarien:
  - Was, wenn der Kunde keine 25 $ in BTC hätte?
    - Sie könnten die Transaktion nicht erstellen, weil "Entsperren" und "Eigentum" dasselbe sind, und Computer überprüfen, ob die Transaktion ordnungsgemäß signiert ist; andernfalls lehnen sie sie ab.
- Was passiert, wenn der zufällig ausgewählte Computer versucht, das "Ledger" zu ändern?
  - Der Block würde abgelehnt werden, da jeder andere Computer eine vollständige Historie besitzt und die Änderung bemerken würde, was eine ihrer Regeln verletzen würde.
  - Der zufällige Computer würde keine Belohnung erhalten, und keine Transaktionen aus ihrem Block würden finalisiert werden.

## Wissensbewertung

<chapterId>1461f064-933d-50ea-8935-324b68ec5d5f</chapterId>

### KA Klassendiskussion

Diskutieren Sie einige Vereinfachungen, die in der Klassenübung unter dem zweiten Szenario gemacht wurden, und beschreiben Sie, was das tatsächliche Bitcoin-System im Detail macht.

### KA Vokabelüberprüfung

Definieren Sie die folgenden Schlüsselbegriffe, die im vorherigen Abschnitt eingeführt wurden:

- Knoten
- Mempool
- Schwierigkeitsziel
- Block

**Diskutieren Sie die Bedeutung einiger zusätzlicher Begriffe als Gruppe:**

Blockchain, Transaktion, Doppelausgabe, Byzantinisches Generalsproblem, Mining, Proof of Work (PoW), Hash-Funktion, Blockbelohnung, Blockchain, Längste Kette, 51%-Angriff, Ausgabe, Ausgabesperre, Wechsel, Satoshis, Öffentlicher/Privater Schlüssel, Adresse, Public-Key-Kryptographie, Digitale Signatur, Wallet

# Einführung in den BTCPay Server

<partId>9c8a2d0c-9ba1-5c39-874c-f9eaf1bba663</partId>

## Verständnis des BTCPay Server-Anmeldebildschirms

<chapterId>14aad54c-9bd8-54f2-9455-178b8ae63408</chapterId>

### Arbeiten mit dem BTCPay Server

Das Ziel dieses Kursblocks wird es sein, ein allgemeines Verständnis der BTCPay Server-Software zu erlangen. In einer gemeinsamen Umgebung wird empfohlen, der Demonstration des Lehrers zu folgen und dem BTCPay Server-Kursbuch zu folgen, um dem Lehrer zu folgen. Sie werden lernen, wie man ein Wallet durch mehrere Methoden erstellt. Beispiele beinhalten Hot-Wallet-Einrichtungen und Hardware-Wallets, die durch den BTCPay Server Vault verbunden sind. Diese Ziele finden in der Demo-Umgebung statt, die vom Kursleiter angezeigt und zugänglich gemacht wird.

Wenn Sie diesem Kurs alleine folgen, finden Sie eine Liste von Drittanbieter-Hosts zu Demonstrationszwecken unter https://directory.btcpayserver.org/filter/hosts. Wir raten dringend davon ab, diese Drittanbieter-Optionen als Produktionsumgebungen zu verwenden, aber sie dienen den richtigen Zwecken für eine Einführung in die Nutzung von Bitcoin und BTCPay Server.

Als BTCPay Server-Rockstar-Trainee haben Sie möglicherweise bereits Erfahrung mit der Einrichtung eines Bitcoin-Knotens gesammelt. Dieser Kurs wird speziell auf den Software-Stack des BTCPay Servers zugeschnitten sein.

Viele der Optionen im BTCPay Server existieren in irgendeiner Form auch in anderer Bitcoin-Wallet-bezogener Software.

### BTCPay Server-Anmeldebildschirm

Wenn Sie in die Demo-Umgebung willkommen geheißen werden, werden Sie gebeten, sich 'Anzumelden' oder 'Ihr Konto zu erstellen'. Serveradministratoren könnten aus Sicherheitsgründen die Funktion zum Erstellen neuer Konten deaktivieren. BTCPay Server-Logos und Buttonfarben können geändert werden, da BTCPay Server Open-Source-Software ist. Ein Drittanbieter-Host kann die Software als White-Label-Produkt verwenden und das gesamte Erscheinungsbild ändern.

![image](assets/en/0.webp)

### Konto erstellen-Fenster

Das Erstellen von Konten auf dem BTCPay Server erfordert gültige E-Mail-Adressen; beispiel@email.com wäre eine gültige Zeichenfolge für E-Mail.

Das Passwort muss mindestens 8 Zeichen lang sein, einschließlich Buchstaben, Zahlen und Zeichen. Nachdem das Passwort einmal festgelegt wurde, müssen Sie das eingegebene Passwort überprüfen, um sicherzustellen, dass es korrekt zu dem im ersten Passwortfeld Eingegebenen ist.
Wenn sowohl die Felder für E-Mail als auch Passwort korrekt ausgefüllt sind, klicken Sie auf den Button „Konto erstellen“. Dadurch werden die E-Mail und das Passwort in der BTCPay Server-Instanz des Instruktors gespeichert.
![image](assets/en/1.webp)

**!Hinweis!**

Wenn Sie diesen Kurs eigenständig durchführen, wäre das Erstellen dieses Kontos etwas, das Sie möglicherweise bei einem Drittanbieter-Host tun würden; daher erwähnen wir erneut, diese niemals als Produktionsumgebungen, sondern nur zu Trainingszwecken zu verwenden.

### Kontoerstellung durch den BTCPay Server-Administrator

Der Administrator der BTCPay Server-Instanz kann ebenfalls Konten für den BTCPay Server erstellen. Der Administrator der BTCPay Server-Instanz kann auf „Servereinstellungen“ (1) klicken, auf den Tab „Benutzer“ (2) gehen und in der oberen rechten Ecke des Benutzer-Tabs auf den Button „+ Benutzer hinzufügen“ (3) klicken. Im Ziel (4.3) erfahren Sie mehr über die Administratorkontrolle der Konten.

![image](assets/en/2.webp)

Als Administrator benötigen Sie die E-Mail-Adresse des Benutzers und legen ein Standardpasswort fest. Es wird empfohlen, als Administrator den Benutzer zu informieren, dass er dieses Passwort ändern sollte, bevor er das Konto aus Sicherheitsgründen verwendet. Wenn der Administrator KEIN Passwort festlegt und SMTP auf dem Server eingerichtet wurde, erhält der Benutzer eine E-Mail mit einem Einladungslink, um sein Konto zu erstellen und das Passwort selbst festzulegen.

### Beispiel

Wenn Sie dem Kurs eines Instruktors folgen, folgen Sie dem vom Instruktor gegebenen Link und erstellen Ihr Konto in der bereitgestellten Demo-Umgebung. Stellen Sie sicher, dass Ihre E-Mail-Adresse und Ihr Passwort sicher gespeichert sind; diese Anmeldeinformationen benötigen Sie für den Rest der Demo-Ziele in diesem Kurs.

Ihr Instruktor hat möglicherweise im Voraus die E-Mail-Adresse gesammelt und vor dieser Übung einen Einladungslink gesendet. Falls angewiesen, überprüfen Sie Ihre E-Mails.

Wenn Sie den Kurs ohne Instruktor durchführen, erstellen Sie Ihr Konto mit der BTCPay Server-Demo-Umgebung; gehen Sie zu

https://mainnet.demo.btcpayserver.org/login.

Dieses Konto sollte nur zu Demonstrations-/Schulungszwecken verwendet und niemals für geschäftliche Zwecke genutzt werden.

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Wie man ein Konto auf einem gehosteten Server über die Schnittstelle erstellt.
- Wie ein Serveradministrator Benutzer manuell in den Servereinstellungen hinzufügen kann.

### Wissensbewertung

#### KA Konzeptuelle Überprüfung

Nennen Sie Gründe, warum die Verwendung eines Demo-Servers für Produktionszwecke eine schlechte Idee ist.

## Benutzerkonto(s) verwalten

<chapterId>b58ca6ee-b7fc-5e81-a6aa-c8ff212b4c55</chapterId>

### Kontoverwaltung auf dem BTCPay Server

Nachdem ein Ladenbesitzer sein Konto erstellt hat, kann er es unten links in der Benutzeroberfläche des BTCPay Servers verwalten. Unter dem Button „Konto“ finden sich mehrere Einstellungen auf höherer Ebene.

- Dunkel-/Hellmodus.
- Umschalter für das Ausblenden sensibler Informationen.
- Konto verwalten.

![image](assets/en/3.webp)

### Dunkel- und Hellmodus

Benutzer des BTCPay Servers können zwischen einer Dunkel- oder Hellmodus-Version der Benutzeroberfläche wählen. Kundenseiten ändern sich nicht. Sie verwenden die kundenspezifischen Einstellungen bezüglich Dunkel- oder Hellmodus.

### Umschalter für das Ausblenden sensibler Informationen

Der Button zum Ausblenden sensibler Informationen bietet eine schnelle und einfache Sicherheitsebene. Wann immer Sie Ihren BTCPay Server bedienen müssen, aber möglicherweise Personen in einem öffentlichen Raum über Ihre Schulter schauen, aktivieren Sie „Sensible Infos ausblenden“, und alle Werte im BTCPay Server werden ausgeblendet. Jemand könnte über Ihre Schulter schauen, kann aber die Werte, mit denen Sie arbeiten, nicht mehr sehen.

### Konto verwalten

Sobald das Benutzerkonto erstellt wurde, erfolgt hier die Verwaltung von Passwörtern, 2FA oder API-Schlüsseln.

### Konto verwalten - Konto

Optional können Sie Ihr Konto mit einer anderen E-Mail-Adresse aktualisieren. Um sicherzustellen, dass Ihre E-Mail-Adresse korrekt ist, ermöglicht es BTCPay Server, eine Verifizierungs-E-Mail zu senden. Klicken Sie auf speichern, wenn der Benutzer eine neue E-Mail-Adresse festlegt und bestätigt, dass die Verifizierung funktioniert hat. Der Benutzername bleibt derselbe wie die vorherige E-Mail.

Ein Benutzer kann sich entscheiden, sein gesamtes Konto zu löschen. Dies kann durch Klicken auf den Löschen-Button im Konto-Tab erfolgen.

![Bild](assets/en/4.webp)

**!Hinweis!**

Nach dem Ändern der E-Mail wird der Benutzername für das Konto nicht geändert. Die zuvor angegebene E-Mail-Adresse bleibt der Anmeldename.

### Konto verwalten - Passwort

Ein Student möchte möglicherweise sein Passwort ändern. Dies kann er tun, indem er zum Passwort-Tab geht. Hier muss er sein altes Passwort eingeben und kann es in ein neues ändern.

![Bild](assets/en/5.webp)

### Zwei-Faktor-Authentifizierung (2FA)

Um die Folgen eines gestohlenen Passworts zu begrenzen, können Sie die Zwei-Faktor-Authentifizierung (2FA) verwenden, eine relativ neue Sicherheitsmethode. Sie können die Zwei-Faktor-Authentifizierung über das Konto verwalten und den Tab für Zwei-Faktor-Authentifizierung aktivieren. Nach dem Einloggen mit Ihrem Benutzernamen und Passwort müssen Sie einen zweiten Schritt abschließen.

BTCPay Server ermöglicht zwei Arten der Aktivierung von 2FA, App-basierte 2FA (Authy, Google, Microsoft Authenticators) oder über Sicherheitsgeräte (FIDO2 oder LNURL Auth).

### Zwei-Faktor-Authentifizierung - App-basiert

Basierend auf dem Betriebssystem Ihres Mobiltelefons (Android oder iOS) können Benutzer zwischen den folgenden Apps wählen;

1. Laden Sie einen Zwei-Faktor-Authentifikator herunter;
   - Authy für [Android](https://play.google.com/store/apps/details?id=com.authy.authy) oder [iOS](https://apps.apple.com/us/app/authy/id494168017)
   - Microsoft Authenticator für [Android](https://play.google.com/store/apps/details?id=com.azure.authenticator) oder [iOS](https://apps.apple.com/us/app/microsoft-authenticator/id983156458)
   - Google Authenticator für [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=e%C2%80) oder [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605)
2. Nach dem Herunterladen und Installieren der Authenticator-App.
   - Scannen Sie den von BTCPay Server bereitgestellten QR-Code
   - Oder geben Sie den von BTCPay Server generierten Schlüssel manuell in Ihre Authenticator-App ein.
3. Die Authenticator-App wird Ihnen einen einzigartigen Code zur Verfügung stellen. Geben Sie den einzigartigen Code in BTCPay Server ein, um die Einrichtung zu überprüfen, und klicken Sie auf überprüfen, um den Vorgang abzuschließen.

![Bild](assets/en/6.webp)

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Konto-Verwaltungsoptionen und die verschiedenen Möglichkeiten, ein Konto auf einer BTCPay Server-Instanz zu verwalten.
- Wie man app-basierte 2FA einrichtet.

### Wissensbewertung

#### KA Konzeptuelle Überprüfung

Beschreiben Sie, wie app-basierte 2FA Ihr Konto sichert

## Einen neuen Store erstellen

<chapterId>463b3634-b49f-5512-a711-3b2e096fc2e0</chapterId>

### Erstellen Sie Ihren Store-Assistenten

Wenn sich ein neuer Benutzer bei BTCPay Server anmeldet, ist die Umgebung leer und benötigt einen ersten Store. Der Einführungswizard von BTCPay Server bietet dem Benutzer die Option, „Create your store“ (1) zu wählen. Ein Store kann als ein Zuhause für Ihre Bitcoin-Bedürfnisse angesehen werden. Ein neuer BTCPay Server Node beginnt mit dem Synchronisieren der Bitcoin Blockchain (2). Je nachdem, auf welcher Infrastruktur Sie BTCPay Server betreiben, kann dies von einigen Stunden bis zu einigen Tagen dauern. Die aktuelle Version der Instanz wird in der unteren rechten Ecke Ihrer BTCPay Server UI angezeigt. Dies ist nützlich als Referenz beim Troubleshooting.
![image](assets/en/7.webp)

### Create your store Wizard

Dieser Kurs beginnt mit einem leicht anderen Bildschirm als die vorherige Seite. Da Ihr Ausbilder die Demo-Umgebung vorbereitet hat, wurde die Bitcoin-Blockchain zuvor synchronisiert, und daher werden Sie den Synchronisierungsstatus der Nodes nicht sehen.

Ein Benutzer kann entscheiden, sein gesamtes Konto zu löschen. Dies kann durch Klicken auf den Lösch-Button im Account-Tab erfolgen.

![image](assets/en/8.webp)

**!Hinweis!**

BTCPay Server-Konten können unbegrenzt viele Stores erstellen. Jeder Store ist eine Wallet oder ein „Zuhause“.

### Beispiel

Beginnen Sie mit einem Klick auf "Create your store".

![image](assets/en/9.webp)

Dies wird Ihr erstes Zuhause und Dashboard für die Nutzung von BTCPay Server erstellen.

(1) Nachdem Sie auf "Create your store" geklickt haben, wird BTCPay Server Sie auffordern, den Store zu benennen; dies kann alles sein, was für Sie nützlich ist.

![image](assets/en/10.webp)

(2) Als Nächstes muss eine Standardwährung für den Store festgelegt werden, entweder eine Fiat-Währung oder in einem Bitcoin / Sats Standard. Für die Demo-Umgebung werden wir dies auf USD setzen.

![image](assets/en/11.webp)

(3) Als letzter Parameter bei der Einrichtung des Stores fordert BTCPay Server Sie auf, eine "Preferred price source" festzulegen, um den Preis von Bitcoin mit dem aktuellen Fiat-Preis zu vergleichen, damit Ihr Store den korrekten Wechselkurs zwischen Bitcoin und der vom Store festgelegten Fiat-Währung anzeigt. Wir werden im Demo-Beispiel bei der Standardeinstellung bleiben und dies auf die Kraken-Börse setzen. BTCPay Server verwendet die Kraken API, um die Wechselkurse zu überprüfen.

![image](assets/en/12.webp)

(4) Jetzt, da diese Store-Parameter festgelegt wurden, klicken Sie auf den Erstellen-Button, und BTCPay Server wird das Dashboard Ihres ersten Stores erstellen, wo der Wizard fortgesetzt wird.

![image](assets/en/13.webp)

Herzlichen Glückwunsch, Sie haben Ihren ersten Store erstellt, und damit ist diese Übung abgeschlossen.

![image](assets/en/14.webp)

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie gelernt:

- Store-Erstellung und Konfiguration einer Standardwährung kombiniert mit Preisquellen-Präferenzen.
- Jeder "Store" ist ein neues Zuhause, getrennt von anderen Stores in dieser Installation von BTCPay Server.

# Einführung in die Sicherung von Bitcoin-Schlüsseln

<partId>25da22d8-fd37-51c5-af2a-58b9f3b046b2</partId>

## Verständnis der Generierung von Bitcoin-Schlüsseln

<chapterId>d162735b-847b-578e-83b8-a044ab703ec5</chapterId>

### Was ist an der Generierung von Bitcoin-Schlüsseln beteiligt?

Bitcoin-Wallets erstellen bei der Einrichtung einen sogenannten "Seed". Im letzten Ziel haben Sie einen "Seed" erstellt. Die vorher generierte Serie von Wörtern ist auch als mnemonische Phrasen bekannt. Der Seed wird verwendet, um einzelne Bitcoin-Schlüssel daraus abzuleiten und Bitcoin zu senden oder zu empfangen. Seed-Phrasen sollten niemals mit Dritten oder nicht vertrauenswürdigen Peers geteilt werden.
Die Generierung von Seeds erfolgt entlang des in der Branche bekannten Standards, der als "Hierarchical Deterministic" (HD) Framework bezeichnet wird.
![image](assets/en/15.webp)

### Adressen

BTCPay Server wurde entwickelt, um eine neue Adresse zu generieren. Dies mildert das Problem der Wiederverwendung von öffentlichen Schlüsseln oder Adressen. Die Verwendung desselben öffentlichen Schlüssels erleichtert das Nachverfolgen Ihrer gesamten Zahlungshistorie erheblich. Schlüssel als Einweg-Gutscheine zu betrachten, würde Ihre Privatsphäre erheblich verbessern. Wir verwenden auch Bitcoin-Adressen, verwechseln Sie diese nicht mit öffentlichen Schlüsseln.

Eine Adresse wird aus dem öffentlichen Schlüssel durch einen „Hashing-Algorithmus“ abgeleitet. Die meisten Wallets und Transaktionen zeigen jedoch Adressen anstelle dieser öffentlichen Schlüssel an. Adressen sind im Allgemeinen kürzer als öffentliche Schlüssel und beginnen üblicherweise mit `1`, `3` oder `bc1`, während öffentliche Schlüssel mit `02`, `03` oder `04` beginnen.

- Adressen, die mit `1.....` beginnen, sind immer noch sehr verbreitete Adressen. Wie im Kapitel Erstellen eines neuen Stores erwähnt, handelt es sich hierbei um Legacy-Adressen. Dieser Adresstyp ist für P2PKH-Transaktionen gedacht. P2Pkh verwendet Base58-Codierung, was die Adresse groß- und kleinschreibungsempfindlich macht. Ihre Struktur basiert auf dem öffentlichen Schlüssel mit einer zusätzlichen Ziffer als Kennung.

- Adressen, die mit `bc1...` beginnen, werden langsam zu sehr verbreiteten Adressen. Diese sind als (native) SegWit-Adressen bekannt. Sie bieten eine bessere Gebührenstruktur als die anderen erwähnten Adressen. Native SegWit-Adressen verwenden Bech32-Codierung und erlauben nur Kleinbuchstaben.

- Adressen, die mit `3...` beginnen, werden häufig noch von Börsen für Einzahlungsadressen verwendet. Diese Adressen werden im Kapitel Erstellen eines neuen Stores als eingepackte oder verschachtelte SegWit-Adressen erwähnt. Sie können jedoch auch als "Multisig-Adresse" funktionieren. Wenn sie als SegWit-Adresse verwendet werden, gibt es wieder Einsparungen bei den Transaktionsgebühren, wenn auch weniger als bei Native SegWit. P2SH-Adressen verwenden Base58-Codierung. Dies macht sie groß- und kleinschreibungsempfindlich, wie die Legacy-Adresse.

- Adressen, die mit `2...` beginnen, sind Testnet-Adressen. Sie sind dazu gedacht, Testnet-Bitcoin (tBTC) zu erhalten. Sie sollten dies niemals verwechseln und Bitcoin an diese Adressen senden. Zu Entwicklungszwecken können Sie eine Testnet-Wallet generieren. Es gibt mehrere Faucets online, um Testnet-Bitcoin zu erhalten. Kaufen Sie niemals Testnet-Bitcoin. Testnet-Bitcoin wird gemined. Dies könnte ein Grund für einen Entwickler sein, stattdessen Regtest zu verwenden. Dies ist eine Spielumgebung für Entwickler, in der bestimmte Netzwerkkomponenten fehlen. Bitcoin ist jedoch zu Entwicklungszwecken sehr nützlich.

### Öffentliche Schlüssel

Öffentliche Schlüssel werden in der Praxis heute weniger verwendet. Im Laufe der Zeit haben Bitcoin-Nutzer sie durch Adressen ersetzt. Sie existieren jedoch immer noch und werden gelegentlich verwendet. Öffentliche Schlüssel sind im Allgemeinen viel längere Zeichenfolgen als Adressen. Wie bei Adressen beginnen sie mit einem spezifischen Kennzeichen.

- Zuerst sind `02...` und `03...` sehr standardmäßige öffentliche Schlüsselkennungen, kodiert im SEC-Format. Diese können verarbeitet und in Adressen zum Empfangen umgewandelt werden, für die Erstellung von Multi-Sig-Adressen verwendet oder zur Überprüfung einer Signatur genutzt werden. Frühe Bitcoin-Transaktionen verwendeten öffentliche Schlüssel als Teil von P2PK-Transaktionen.

- HD-Wallets verwenden jedoch eine andere Struktur. `xpub...`, `ypub...` oder `zpub...` werden als erweiterte öffentliche Schlüssel oder xpubs bezeichnet. Diese Schlüssel werden verwendet, um viele öffentliche Schlüssel abzuleiten, da sie Teil des HD-Wallets sind. Da Ihr xpub die Aufzeichnungen Ihrer gesamten Historie, also vergangene und zukünftige Transaktionen, enthält, teilen Sie diese niemals mit nicht vertrauenswürdigen Parteien.

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Die Unterschiede zwischen Adressen und öffentlichen Schlüsseldatentypen sowie die Vorteile der Verwendung von Adressen gegenüber öffentlichen Schlüsseln.

### Wissensbewertung

Beschreiben Sie den Vorteil der Verwendung von frischen Adressen für jede Transaktion im Vergleich zur Wiederverwendung von Adressen oder öffentlichen Schlüsselmethoden

## Sicherung von Schlüsseln mit einem Hardware-Wallet

<chapterId>c54a6d61-5a43-5fdb-93ae-c6750de9c612</chapterId>

### Speichern von Bitcoin-Schlüsseln

Nachdem eine Seed-Phrase generiert wurde, erfordert die Liste der 12 - 24 Wörter, die in diesem Buch generiert wurden, ordnungsgemäße Backups und Sicherheit, da diese Wörter der einzige Weg sind, um den Zugang zu einem Wallet wiederherzustellen. Die Struktur von HD-Wallets und wie sie Adressen deterministisch mit dieser einen Seed generiert, werden alle Ihre erstellten Adressen mit dieser einen Liste von mnemonischen Wörtern gesichert, die Ihre Seed- oder Wiederherstellungsphrase darstellen.

Halten Sie Ihre Wiederherstellungsphrase sicher. Wenn sie von jemandem, insbesondere mit böswilliger Absicht, zugegriffen wird, können sie Ihre Mittel bewegen. Die Seed sicher und gesichert zu halten, aber sie auch zu erinnern, ist einander gegenseitig. Es gibt mehrere Methoden, um Bitcoin-Private-Keys zu speichern, jede mit Vor- und Nachteilen, sei es in Sicherheit, Privatsphäre, Bequemlichkeit oder physischen Mitteln. Aufgrund der Bedeutung von privaten Schlüsseln tendieren Bitcoin-Nutzer dazu, diese Schlüssel in „Selbstverwahrung“ zu speichern und sicher aufzubewahren, anstatt „verwahrte“ Dienste wie Banken zu nutzen. Je nach Benutzer muss er entweder eine Cold-Storage-Lösung oder ein Hot-Wallet verwenden.

### Hot- und Cold-Speicherung von Bitcoin-Schlüsseln

Üblicherweise werden Bitcoin-Wallets in ein Hot-Wallet oder Cold-Wallet eingeteilt. Die meisten Kompromisse liegen in Bequemlichkeit, Benutzerfreundlichkeit und Sicherheitsrisiken. Jede dieser Methoden kann auch in einer Verwahrungslösung gesehen werden. Die Kompromisse hier sind jedoch meistens sicherheits- und datenschutzbezogen und gehen über den Rahmen dieses Kurses hinaus.

### Hot-Wallet

Hot-Wallets sind die bequemste Art, mit Bitcoin über mobile, Web- oder Desktop-Software zu interagieren. Das Wallet ist immer mit dem Internet verbunden, was es Benutzern ermöglicht, Bitcoin zu senden oder zu empfangen. Dies ist jedoch auch seine Schwäche, da das Wallet, da es immer online ist, jetzt anfälliger für Angriffe durch Hacker oder Malware auf Ihrem Gerät ist. In BTCPay Server speichern Hot-Wallets die privaten Schlüssel auf der Instanz. Jeder, der auf Ihren BTCPay Server-Store zugreift, könnte Mittel von dieser Adresse stehlen, wenn böswillig. Wenn BTCPay Server in einer gehosteten Umgebung läuft, sollten Sie dies immer in Ihrem Sicherheitsprofil berücksichtigen und vorzugsweise kein Hot-Wallet in einem solchen Fall verwenden. Wenn BTCPay Server auf eigener Hardware installiert ist, gesichert und von Ihnen vertraut, verringert sich das Risikoprofil erheblich, aber es verschwindet nie!

### Cold-Wallet

Individuen bewegen ihr Bitcoin in ein Cold-Wallet, weil es die privaten Schlüssel vom Internet isolieren kann. Die Entfernung der Internetverbindung aus der Gleichung reduziert das Risiko von Malware, Spyware und SIM-Swaps. Cold-Storage wird im Vergleich zu Hot-Storage für Sicherheit und Autonomie als überlegen angesehen, solange angemessene Vorsichtsmaßnahmen getroffen werden, um den Verlust der Bitcoin-Private-Keys zu vermeiden. Cold-Storage eignet sich am besten für große Mengen von Bitcoin, die aufgrund der Komplexität des Wallet-Setups nicht oft ausgegeben werden sollen.

Es gibt verschiedene Methoden, wie Bitcoin-Schlüssel im Cold-Storage gespeichert werden können, von Papier-Wallets über Brain-Wallets, Hardware-Wallets oder von Anfang an eine Wallet-Datei. Die meisten Wallets verwenden BIP 39, um die Seed-Phrase zu generieren. Jedoch wurde innerhalb der Bitcoin-Core-Software noch kein Konsens über dessen Verwendung erreicht. Bitcoin-Core-Software wird immer noch eine Wallet.dat-Datei generieren, die Sie an einem sicheren Offline-Ort speichern müssen.

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie gelernt:

- Die Unterschiede zwischen Hot- und Cold-Wallets in Bezug auf Funktionalität und ihre Kompromisse.

### Wissensbewertung Konzeptuelle Überprüfung

- Was ist eine Wallet?
- Was ist der Unterschied zwischen Hot und Cold Wallets?

- Beschreiben Sie, was mit "Generierung einer Wallet" gemeint ist?

## Verwendung Ihrer Bitcoin-Schlüssel

<chapterId>bff488de-5052-56e6-b696-97e896f762ae</chapterId>

### BTCPay Server Wallet

BTCPay Server besteht aus den folgenden Standard-Wallet-Funktionen:

- Transaktionen
- Senden
- Empfangen
- Rescan
- Pull-Zahlungen
- Auszahlungen
- PSBT
- Allgemeine Einstellungen

### Transaktionen

Administratoren können die ein- und ausgehenden Transaktionen für die mit diesem spezifischen Store verbundene On-Chain-Wallet in der Transaktionsansicht sehen. Jede Transaktion wird zwischen empfangen und gesendet unterschieden. Empfangene werden grün und ausgehende Transaktionen werden rot sein. Innerhalb der BTCPay Server Transaktionsansicht werden Administratoren auch eine Reihe von Standard-Labels sehen.

| Transaktionstyp | Beschreibung                                                           |
| --------------- | ---------------------------------------------------------------------- |
| App             | Zahlung wurde durch eine App erstellte Rechnung erhalten               |
| Rechnung        | Zahlung wurde durch eine Rechnung erhalten                             |
| Payjoin         | Nicht bezahlt, Rechnungstimer ist noch nicht abgelaufen                |
| Payjoin-exposed | UTXO wurde durch einen Payjoin-Vorschlag für eine Rechnung offengelegt |
| Zahlungsanfrage | Zahlung wurde durch eine Zahlungsanfrage erhalten                      |
| Auszahlung      | Zahlung wurde durch eine Auszahlung oder Rückerstattung gesendet       |

### Wie man sendet

Die Sendefunktion des BTCPay-Servers sendet Transaktionen von Ihrer BTCPay Server On-Chain-Wallet. BTCPay Server ermöglicht mehrere Wege, Ihre Transaktionen zu signieren, um Mittel auszugeben. Eine Transaktion kann signiert werden mit:

- Hardware-Wallet
- Wallets, die PSBT unterstützen
- HD-Privatschlüssel oder Wiederherstellungsseeds.
- Hot Wallet

#### Hardware-Wallet

BTCPay Server unterstützt Hardware-Wallets, sodass Sie Ihr Hardware-Wallet mit BTCPay Vault verwenden können, ohne Informationen an Drittanbieter-Apps oder -Server weiterzugeben. Die Integration von Hardware-Wallets in BTCPay Server ermöglicht es Ihnen, Ihr Hardware-Wallet zu importieren und die eingehenden Mittel mit einer einfachen Bestätigung auf Ihrem Gerät auszugeben. Ihre privaten Schlüssel verlassen niemals das Gerät, und alle Mittel werden gegen Ihren Vollknoten validiert, sodass keine Daten durchsickern.

#### Signieren mit einem Wallet, das PSBT unterstützt

PSBT (Partially Signed Bitcoin Transactions) ist ein Austauschformat für Bitcoin-Transaktionen, die noch vollständig signiert werden müssen. PSBT wird in BTCPay Server unterstützt und kann mit kompatiblen Hardware- und Software-Wallets signiert werden.

Die Erstellung einer vollständig signierten Bitcoin-Transaktion durchläuft die folgenden Schritte:

- Ein PSBT wird mit spezifischen Eingaben und Ausgaben, aber ohne Signaturen konstruiert
- Das exportierte PSBT kann von einem Wallet, das dieses Format unterstützt, importiert werden
- Die Transaktionsdaten können mit dem Wallet überprüft und signiert werden
- Die signierte PSBT-Datei wird vom Wallet exportiert und in BTCPay Server importiert
- BTCPay Server produziert die endgültige Bitcoin-Transaktion
- Sie überprüfen das Ergebnis und senden es ins Netzwerk

#### Signieren mit HD-Privatschlüssel oder mnemonischem Seed

Wenn Sie zuvor eine Wallet mit BTCPay Server erstellt haben, können Sie die Mittel ausgeben, indem Sie Ihren privaten Schlüssel in das entsprechende Feld eingeben. Stellen Sie einen korrekten "AccountKeyPath" in Wallet> Einstellungen ein; sonst können Sie nicht ausgeben.

#### Signieren mit einem Hot Wallet

Wenn Sie beim Einrichten Ihres Stores ein neues Wallet erstellt und es als Hot Wallet aktiviert haben, wird es automatisch den auf einem Server gespeicherten Seed verwenden, um zu signieren.

### RBF (Replace-By-Fee)

Replace-By-Fee (RBF) ist ein Bitcoin-Protokoll-Feature, das es Ihnen erlaubt, eine zuvor gesendete Transaktion (solange noch nicht bestätigt) zu ersetzen. Dies ermöglicht es, den Transaktions-Fingerabdruck Ihres Wallets zu randomisieren oder ihn durch eine höhere Gebührenrate zu ersetzen, um die Transaktion in der Bestätigungswarteschlange (Mining) nach oben zu verschieben. Dies wird effektiv die ursprüngliche Transaktion ersetzen, da die höhere Gebührenrate priorisiert wird und, einmal bestätigt, die ursprüngliche Transaktion ungültig macht (kein doppelter Ausgaben).

Drücken Sie den "Erweiterte Einstellungen"-Button, um die RBF-Optionen anzusehen;

![image](assets/en/16.webp)

- Randomisieren für höhere Privatsphäre, erlaubt es, die Transaktion automatisch zu ersetzen, um den Transaktions-Fingerabdruck zu randomisieren.
- Ja, Transaktion für RBF markieren und explizit ersetzen (Nicht standardmäßig ersetzt, nur durch Eingabe)
- Nein, das Ersetzen der Transaktion nicht zulassen.

### Coin-Auswahl

Die Coin-Auswahl ist ein fortgeschrittenes Feature zur Verbesserung der Privatsphäre, das es Ihnen ermöglicht, Münzen auszuwählen, die Sie beim Erstellen einer Transaktion ausgeben möchten. Zum Beispiel mit Münzen zu bezahlen, die frisch aus einem Conjoin-Mix stammen.

Die Coin-Auswahl funktioniert nativ mit der Wallet-Label-Funktion. Dies ermöglicht es Ihnen, eingehende Gelder zu kennzeichnen für ein reibungsloseres UTXO-Management und Ausgaben.

BTCPay Server unterstützt auch BIP-329 für das Label-Management. BIP-329 erlaubt Labels auf; wenn Sie von einem Wallet, das dieses spezielle BIP unterstützt, übertragen und Labels setzen, wird BTCPay Server diese erkennen und importieren. Beim Migrieren von Servern können diese Informationen auch exportiert und in die neue Umgebung importiert werden.

### Wie man erhält

Wenn man im BTCPay Server auf den Empfangsbutton klickt, generiert es eine unbenutzte Adresse, die zum Empfangen von Zahlungen verwendet werden kann. Administratoren können auch eine neue Adresse generieren, indem sie eine neue „Rechnung“ erstellen.

BTCPay Server wird immer darum bitten, die nächste verfügbare Adresse zu generieren, um Adresswiederverwendung zu vermeiden. Nachdem auf „Nächste verfügbare BTC-Adresse generieren“ geklickt wurde, generierte BTCPay Server eine neue Adresse und QR. Es ermöglicht Ihnen auch, direkt ein Label für die Adresse zu setzen, für ein besseres Management Ihrer Adressen.

![image](assets/en/17.webp)

![image](assets/en/18.webp)

#### Neu-Scan

Die Rescan-Funktion stützt sich auf Bitcoin Core 0.17.0’s „Scantxoutset“, um den aktuellen Zustand der Blockchain (genannt UTXO Set) nach Münzen zu durchsuchen, die zum konfigurierten Ableitungsschema gehören. Wallet-Rescan löst zwei Probleme, die BTCPay Server-Nutzer erfahren.

1. Gap-Limit-Problem - Die meisten Drittanbieter-Wallets sind Light-Wallets, die einen Knoten zwischen vielen Nutzern teilen. Light- und Full-Node-abhängige Wallets begrenzen die Anzahl (typischerweise 20) der Adressen ohne Guthaben, die sie auf der Blockchain verfolgen, um Leistungsprobleme zu verhindern. BTCPay Server generiert für jede Rechnung eine neue Adresse. Mit dem oben Gesagten, nachdem BTCPay Server 20 aufeinanderfolgende unbezahlte Rechnungen generiert hat, hört das externe Wallet auf, die Transaktionen abzurufen, in der Annahme, dass keine neuen Transaktionen stattgefunden haben. Ihr externes Wallet wird sie nicht anzeigen, sobald Rechnungen am 21., 22. usw. bezahlt werden. Andererseits verfolgt das BTCPay Server-Wallet jede von ihm generierte Adresse zusammen mit einem viel größeren Gap-Limit. Es ist nicht auf einen Drittanbieter angewiesen und kann immer ein korrektes Guthaben anzeigen.
2. Die Lösung des Gap-Limit-Problems - Wenn Ihr [externes/vorhandenes Wallet](https://docs.btcpayserver.org/WalletSetup/#use-an-existing-wallet) eine Gap-Limit-Konfiguration erlaubt, ist die einfache Lösung, es zu erhöhen. Allerdings erlauben die meisten Wallets dies nicht. Die einzigen Wallets, von denen wir wissen, dass sie eine Gap-Limit-Konfiguration erlauben, sind Electrum, Wasabi und Sparrow Wallet. Leider werden Sie wahrscheinlich bei vielen anderen Wallets auf Probleme stoßen. Für das beste Benutzererlebnis und Datenschutz, erwägen Sie, externe Wallets aufzugeben und das interne Wallet von BTCPay Server zu verwenden.

#### BTCPay Server verwendet „mempoolfullrbf=1“

BTCPay Server verwendet „mempoolfullrbf=1“; wir haben dies als Standard in Ihrem BTCPay Server-Setup hinzugefügt. Wir haben es jedoch auch als ein Fragment gemacht, das Sie selbst deaktivieren können. Ohne „mempoolfullrbf=1“, wenn ein Kunde eine Zahlung mit einer Transaktion, die RBF nicht signalisiert, doppelt ausgibt, würde der Händler dies erst nach der Bestätigung erfahren.

Ein Administrator möchte vielleicht auf diese Einstellung verzichten. Mit der folgenden Zeichenfolge können Sie den gesetzten Standard ändern.

```
BTCPAYGEN_EXCLUDE_FRAGMENTS="$BTCPAYGEN_EXCLUDE_FRAGMENTS;opt-mempoolfullrbf"
. btcpay-setup.sh -i**
```

### BTCPay Server Wallet-Einstellungen

Die Wallet-Einstellungen innerhalb von BTCPay Server bieten einen klaren und schnellen Überblick über die allgemeinen Einstellungen Ihres Wallets. Alle diese Einstellungen sind vorausgefüllt, wenn das Wallet mit BTCPay Server erstellt wurde.

![image](assets/en/19.webp)

Die Wallet-Einstellungen innerhalb von BTCPay Server bieten einen klaren und schnellen Überblick über die allgemeinen Einstellungen Ihres Wallets. Alle diese Einstellungen sind vorausgefüllt, wenn das Wallet mit BTCPay Server erstellt wurde. Die Wallet-Einstellungen von BTCPay Server beginnen mit dem Wallet-Status. Ist es ein Nur-Beobachten oder ein Hot Wallet? Je nach Wallet-Typ können die Aktionen variieren, von dem erneuten Scannen des Wallets nach fehlenden Transaktionen, dem Beschneiden alter Transaktionen aus der Historie, dem Registrieren des Wallets für Zahlungslinks oder dem Ersetzen und Löschen des aktuellen Wallets, das mit dem Store verbunden ist. In den Wallet-Einstellungen von BTCPay Server können Administratoren ein Label für das Wallet zur besseren Wallet-Verwaltung setzen. Hier kann der Administrator auch das Ableitungsschema, den Kontoschlüssel (xpub), den Fingerabdruck und den Keypath sehen. Zahlungen in den Wallet-Einstellungen haben nur 2 Hauptkonfigurationen. Eine Zahlung ist ungültig, wenn die Transaktion nicht innerhalb von (festgelegten Minuten) nach Ablauf der Rechnung bestätigt wird. Die Rechnung gilt als bestätigt, wenn die Zahlungstransaktion X Anzahl von Bestätigungen hat. Administratoren können auch einen Schalter setzen, um empfohlene Gebühren bei Zahlungen anzuzeigen oder ein manuelles Bestätigungsziel in der Anzahl der Blöcke festzulegen.

![image](assets/en/20.webp)

**!Hinweis!**

Wenn Sie diesen Kurs selbstständig durchführen, wäre das Erstellen dieses Kontos etwas, das Sie möglicherweise auf einem Drittanbieter-Host tun würden, daher erwähnen wir erneut, diese niemals als Produktionsumgebungen zu verwenden, sondern nur zu Trainingszwecken.

### Beispiel

#### Einrichten eines Bitcoin-Wallets in BTCPay Server

BTCPay Server ermöglicht zwei Arten der Wallet-Einrichtung. Eine Möglichkeit besteht darin, ein bereits vorhandenes Bitcoin-Wallet zu importieren. Der Import kann durchgeführt werden, indem ein Hardware-Wallet verbunden, eine Wallet-Datei importiert, ein erweiterter öffentlicher Schlüssel eingegeben, ein QR-Code des Wallets gescannt oder am wenigsten bevorzugt, ein zuvor erstellter Wallet-Wiederherstellungs-Seed von Hand eingegeben wird. In BTCPay Server ist es auch möglich, ein neues Wallet zu erstellen. Es gibt zwei mögliche Wege, BTCPay Server beim Generieren eines neuen Wallets zu konfigurieren.
Die Option für eine Hot Wallet in BTCPay Server ermöglicht Funktionen wie 'Payjoin' oder 'Liquid'. Es gibt jedoch einen Nachteil: Der für diese Wallet generierte Wiederherstellungsschlüssel (Recovery Seed) wird auf dem Server gespeichert, wo jeder, der Admin-Kontrolle hat, den Wiederherstellungsschlüssel abrufen könnte. Da Ihr privater Schlüssel von Ihrem Wiederherstellungsschlüssel abgeleitet wird, könnte ein böswilliger Akteur Zugang zu Ihren aktuellen und zukünftigen Geldern erhalten!
Um ein solches Risiko in BTCPay Server zu mindern, kann ein Admin in den Servereinstellungen > Richtlinien > "Nicht-Admins erlauben, Hot Wallets für ihre Geschäfte zu erstellen" auf nein setzen, wie es standardmäßig der Fall ist. Um die Sicherheit dieser Hot Wallets zu erhöhen, sollte der Serveradministrator die 2FA-Authentifizierung für Konten aktivieren, die Hot Wallets haben dürfen. Das Speichern privater Schlüssel auf einem öffentlichen Server ist gefährlich und birgt Risiken. Einige sind ähnlich den Risiken des Lightning-Netzwerks (siehe nächstes Kapitel für Risiken des Lightning-Netzwerks).

Die zweite Option, die BTCPay Server beim Erstellen einer neuen Wallet bietet, ist das Erstellen einer Nur-Beobachtungs-Wallet (Watch-Only Wallet). BTCPay Server generiert Ihre privaten Schlüssel einmalig. Nachdem der Benutzer bestätigt hat, dass er seinen Seed-Phrase aufgeschrieben hat, wird BTCPay Server die privaten Schlüssel vom Server löschen. Als Ergebnis hat Ihr Geschäft jetzt eine Nur-Beobachtungs-Wallet damit verbunden. Um die erhaltenen Gelder auf Ihrer Nur-Beobachtungs-Wallet auszugeben, siehe Kapitel Wie man sendet, entweder durch Verwendung von BTCPay Server Vault, PSBT (partiell signierte Bitcoin-Transaktion) oder, am wenigsten empfohlen, durch manuelles Bereitstellen Ihres Seed-Phrase.

Im letzten Teil haben Sie ein neues 'Geschäft' erstellt. Der Installationsassistent wird weiterhin fragen, ob Sie "Eine Wallet einrichten" oder "Einen Lightning-Knoten einrichten" möchten. In diesem Beispiel folgen Sie dem Prozess des Einrichtens einer Wallet (1).

![image](assets/en/21.webp)

Nachdem Sie auf "Eine Wallet einrichten" geklickt haben, wird der Assistent weiterhin fragen, wie Sie fortfahren möchten; BTCPay Server bietet nun die Option, eine vorhandene Bitcoin-Wallet mit Ihrem neuen Geschäft zu verbinden. Wenn Sie keine Wallet haben, schlägt BTCPay Server vor, eine neue zu erstellen. Dieses Beispiel wird den Schritten zum "Erstellen einer neuen Wallet" (2) folgen. Folgen Sie den Schritten, um zu erfahren, wie man "Eine vorhandene Wallet verbindet (1).

![image](assets/en/22.webp)

**!Hinweis!**

Wenn Sie diesen Kurs in einem Klassenzimmer nehmen, ist das aktuelle Beispiel und der generierte Seed nur zu Bildungszwecken. Es sollte nie irgendein substantieller Betrag außer dem für die Übungen erforderlichen auf diesen Adressen sein.

(1) Fahren Sie mit dem "Neue Wallet"-Assistenten fort, indem Sie auf den Button "Eine neue Wallet erstellen" klicken.

![image](assets/en/23.webp)

(2) Nachdem Sie auf "Eine neue Wallet erstellen" geklickt haben, gibt das nächste Fenster im Assistenten die Optionen "Hot Wallet" und "Nur-Beobachtungs-Wallet" an. Wenn Sie einem Lehrer folgen, ist Ihre Umgebung eine gemeinsame Demo, und Sie können nur eine Nur-Beobachtungs-Wallet erstellen. Beachten Sie den Unterschied zwischen den beiden untenstehenden Abbildungen. Da Sie in der Demo-Umgebung einem Lehrer folgen, erstellen Sie eine "Nur-Beobachtungs-Wallet" und fahren Sie mit dem "Neue Wallet"-Assistenten fort.

![image](assets/en/24.webp)

![image](assets/en/25.webp)

(3) Im Weiteren des neuen Wallet-Assistenten befinden Sie sich jetzt im Abschnitt "BTC Nur-Beobachtungs-Wallet erstellen". Hier können wir den "Adresstyp" der Wallet festlegen. BTCPay Server ermöglicht es Ihnen, Ihren bevorzugten Adresstyp auszuwählen; zum Zeitpunkt der Erstellung dieses Kurses wird immer noch empfohlen, bech32-Adressen zu verwenden. Erfahren Sie mehr im Detail über Adressen im ersten Kapitel dieses Teils.

- Segwit (bech32)
- Native SegWit sind Adressen, die mit `bc1q` beginnen.
  - Beispiel: `bc1qXXXXXXXXXXXXXXXXXXXXXX`
- Legacy
  - Legacy-Adressen sind Adressen, die mit der Zahl `1` beginnen.
  - Beispiel: `15e15hXXXXXXXXXXXXXXXXXXXX`
- Taproot (Für fortgeschrittene Nutzer)
  - Taproot-Adressen beginnen mit `bc1p`.
  - Beispiel: `bc1pXXXXXXXXXXXXXXXXXXXXXXXX`
- Segwit wrapped
  - Segwit wrapped sind Adressen, die mit `3` beginnen.
  - Beispiel: `37BBXXXXXXXXXXXXXXX`

Wählen Sie Segwit (empfohlen) als Ihren bevorzugten Wallet-Adresstyp.

![Bild](assets/en/26.webp)

(4) Beim Einstellen des Parameters für das Wallet ermöglicht es BTCPay Server den Benutzern, eine optionale Passphrase über BIP39 festzulegen. Stellen Sie sicher, dass Sie Ihr Passwort bestätigen.

![Bild](assets/en/27.webp)

(5) Nachdem Sie den Adresstyp des Wallets festgelegt und möglicherweise einige erweiterte Optionen eingestellt haben, klicken Sie auf Erstellen, und BTCPay Server generiert Ihr neues Wallet. Beachten Sie, dass dies der letzte Schritt vor der Generierung Ihres Seed-Phrases ist. Stellen Sie sicher, dass Sie dies nur in einer Umgebung tun, in der niemand Ihren Seed-Phrase durch Betrachten Ihres Bildschirms stehlen kann.

![Bild](assets/en/28.webp)

(6) Im folgenden Bildschirm des Assistenten zeigt Ihnen BTCPay Server den Wiederherstellungs-Seed-Phrase für Ihr neu generiertes Wallet; dies sind die Schlüssel zur Wiederherstellung Ihres Wallets und zum Signieren von Transaktionen. BTCPay Server generiert einen Seed-Phrase aus 12 Wörtern. Diese Wörter werden nach diesem Einrichtungsbildschirm vom Server gelöscht. Dieses Wallet ist speziell ein Nur-Ansicht-Wallet. Es wird empfohlen, diesen Seed-Phrase nicht digital oder durch fotografisches Bild zu speichern. Benutzer dürfen im Assistenten nur weitermachen, wenn sie aktiv bestätigen, dass sie ihren Seed-Phrase aufgeschrieben haben.

![Bild](assets/en/29.webp)

(7) Nachdem Sie auf Fertig geklickt und den neu generierten Bitcoin-Seed-Phrase gesichert haben, aktualisiert BTCPay Server Ihren Store mit dem angehängten neuen Wallet und ist bereit, Zahlungen zu empfangen. In der Benutzeroberfläche, im linken Navigationsmenü, beachten Sie, wie Bitcoin jetzt hervorgehoben und unter Wallet aktiviert ist.

![Bild](assets/en/30.webp)

### Beispiel: Einen Seed-Phrase aufschreiben

Dies ist ein sehr besonderer und sicherer Moment, um Bitcoin zu verwenden. Wie zuvor erwähnt, sollten nur Sie Zugang zu oder Kenntnis über Ihren Seed-Phrase haben. Wenn Sie zusammen mit einem Lehrer und einer Klasse folgen, sollte der generierte Seed nur in diesem Kurs verwendet werden. Zu viele Faktoren, neugierige Blicke von Klassenkameraden, unsichere Systeme und viele andere machen diese Schlüssel nur zu Bildungszwecken und nicht vertrauenswürdig. Die generierten Schlüssel sollten jedoch immer noch für Kursbeispiele gespeichert werden.

Die erste Methode, die wir in der aktuellen Situation verwenden werden, auch die am wenigsten sichere, besteht darin, den Seed-Phrase in der richtigen Reihenfolge aufzuschreiben. Eine Seed-Phrase-Karte ist im Kursmaterial enthalten, das dem Studenten zur Verfügung gestellt wird oder auf dem GitHub von BTCPay Server gefunden werden kann. Wir werden diese Karte verwenden, um die im vorherigen Schritt generierten Wörter aufzuschreiben. Stellen Sie sicher, dass Sie sie in der richtigen Reihenfolge aufschreiben. Nachdem Sie sie aufgeschrieben haben, überprüfen Sie sie mit dem, was von der Software gegeben wurde, um sicherzustellen, dass Sie sie in der richtigen Reihenfolge aufgeschrieben haben. Nachdem Sie es aufgeschrieben haben, klicken Sie das Kontrollkästchen an, das besagt, dass Sie Ihren Seed-Phrase ordnungsgemäß aufgeschrieben haben.

### Beispiel: Einen Seed-Phrase auf einem Hardware Wallet speichern

In diesem Kurs gehen wir darauf ein, einen Seed-Phrase auf einem Hardware Wallet zu speichern. Die Teilnahme an diesem Kurs unter Anleitung eines Lehrers schließt möglicherweise nicht immer ein solches Gerät ein. Im Kursmaterial sind Hardware Wallets aufgelistet, die für diese Übung geeignet wären.
Wir werden in diesem Beispiel den BTCPay Server Vault und ein Blockstream Jade Hardware-Wallet verwenden.
Sie können auch ein Video zur Referenz heranziehen, um zu sehen, wie ein Hardware-Wallet verbunden wird.
![BTCPay Server - Wie Sie Ihr Hardware-Wallet mit BTCPay Vault verbinden.](https://youtu.be/s4qbGxef43A)

BTCPay Server Vault herunterladen: https://github.com/btcpayserver/BTCPayServer.Vault/releases

Stellen Sie sicher, dass Sie die korrekten Dateien für Ihr System herunterladen. Windows-Nutzer sollten das Paket [BTCPayServerVault-2.0.5-setup.exe](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-2.0.5-setup.exe) herunterladen, Mac-Nutzer das [BTCPayServerVault-osx-x64-2.0.5.dmg](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-osx-x64-2.0.5.dmg) und Linux-Nutzer [BTCPayServerVault-Linux-2.0.5.tar.gz](https://github.com/btcpayserver/BTCPayServer.Vault/releases/download/Vault%2Fv2.0.5/BTCPayServerVault-Linux-2.0.5.tar.gz)

Nach der Installation von BTCPay Server Vault starten Sie die Software, indem Sie auf das Symbol auf Ihrem Desktop klicken. Wenn BTCPay Server Vault ordnungsgemäß installiert und zum ersten Mal gestartet wird, wird es die Erlaubnis anfordern, mit Webanwendungen verwendet zu werden. Es wird darum bitten, den Zugriff auf den spezifischen BTCPay Server, mit dem Sie arbeiten, zu gewähren. Akzeptieren Sie diese Bedingungen. BTCPay Server Vault wird nun nach dem Hardware-Gerät suchen. Sobald das Gerät gefunden wurde, wird BTCPay Server erkennen, dass Vault läuft und Ihr Gerät erfasst hat.

**!Hinweis!**

Geben Sie Ihre SSH-Schlüssel oder Server-Admin-Konto nicht an andere weiter, außer an Administratoren, wenn Sie ein Hot Wallet verwenden. Jeder, der Zugang zu diesen Konten hat, wird Zugang zu den Mitteln im Hot Wallet haben.

### Fähigkeiten Zusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Die Transaktionsansicht des Bitcoin-Wallets und seine verschiedenen Kategorisierungen.
- Verschiedene Optionen, die beim Senden aus einem Bitcoin-Wallet zur Verfügung stehen, von Hardware- bis zu Hot-Wallets.
- Das Gap-Limit-Problem, das bei den meisten Wallets auftritt, und wie man dieses korrigiert.
- Wie man ein neues Bitcoin-Wallet innerhalb von BTCPay Server generiert, einschließlich der Speicherung der Schlüssel in einem Hardware-Wallet und der Sicherung des Wiederherstellungsphrasen.

In diesem Ziel haben Sie gelernt, wie man ein neues Bitcoin-Wallet innerhalb von BTCPay Server generiert. Wir sind noch nicht darauf eingegangen, wie man diese Schlüssel sichert oder verwendet. In einer kurzen Übersicht dieses Ziels haben Sie gelernt, wie man den ersten Store einrichtet. Sie haben gelernt, wie man eine Bitcoin-Wiederherstellungsphrase generiert.

### Wissensbewertung Praktische Überprüfung

Beschreiben Sie eine Methode zur Generierung von Schlüsseln und ein Schema zu deren Sicherung, zusammen mit den Kompromissen/Risiken des Sicherheitsschemas.

## BTCPay Server Lightning Wallet

<chapterId>1bbece7e-0197-57e6-a93a-561cf384d946</chapterId>

Wenn ein Serveradministrator eine neue BTCPay Server-Instanz bereitstellt, kann er eine Lightning-Netzwerk-Implementierung einrichten, LND, Core Lightning oder Eclair; siehe Teil Konfigurieren von BTCPay Server für detailliertere Installationsanweisungen.
Wenn ein Klassenzimmer folgt, funktioniert das Verbinden eines Lightning-Knotens mit Ihrem BTCPay Server über einen benutzerdefinierten Knoten. Ein Benutzer, der kein Serveradministrator auf BTCPay Server ist, kann standardmäßig den internen Lightning-Knoten nicht nutzen. Dies dient dazu, den Serverbesitzer vor dem Verlust seiner Gelder zu schützen. Serveradministratoren können ein Plugin installieren, um Zugang zu ihrem Lightning-Knoten über LNBank zu gewähren; dies liegt außerhalb des Umfangs dieses Buches; lesen Sie mehr über LNBank auf der offiziellen Plugin-Seite.

### Internen Knoten verbinden (Serveradministrator)

Der Serveradministrator kann den internen Lightning-Knoten von BTCPay Server nutzen. Unabhängig von der Lightning-Implementierung ist die Verbindung zum internen Lightning-Knoten dieselbe.

Gehen Sie zu einem zuvor eingerichteten Store und klicken Sie im linken Menü auf das "Lightning"-Wallet. BTCPay Server bietet zwei Einrichtungsmöglichkeiten: Nutzung des internen Knotens (nur standardmäßig für Serveradministratoren) oder eines benutzerdefinierten Knotens (externe Verbindung). Serveradministratoren können auf die Option "Internen Knoten verwenden" klicken. Es ist keine weitere Konfiguration erforderlich. Klicken Sie auf den "Speichern"-Button und beachten Sie die Benachrichtigung, die besagt: "BTC Lightning-Knoten aktualisiert". Der Store hat nun erfolgreich Lightning-Netzwerk-Fähigkeiten erhalten.

### Externen Knoten verbinden (Serverbenutzer/Storebesitzer)

Da Storebesitzer standardmäßig nicht berechtigt sind, den Lightning-Knoten des Serveradministrators zu nutzen, muss die Verbindung zu einem externen Knoten hergestellt werden, entweder zu einem Knoten, der dem Storebesitzer vor der Einrichtung eines BTCPay Servers gehört, einem LNBank-Plugin, falls vom Serveradministrator zur Verfügung gestellt, oder einer Verwahrungslösung wie Alby.

Gehen Sie zu einem zuvor eingerichteten Store und klicken Sie im linken Menü unter Wallets auf "Lightning". Da Storebesitzer standardmäßig nicht berechtigt sind, den internen Knoten zu nutzen, ist diese Option ausgegraut. Die Nutzung eines benutzerdefinierten Knotens ist die einzige standardmäßig verfügbare Option für Storebesitzer.

BTCPay Server benötigt Verbindungsinformationen; die zuvor erstellte (oder Verwahrungslösung) liefert diese Informationen spezifisch für eine Lightning-Implementierung. Innerhalb des BTCPay Servers können Storebesitzer die folgenden Verbindungen nutzen;

- C-lightning über TCP oder Unix-Domain-Socket-Verbindung.
- Lightning Charge über HTTPS
- Eclair über HTTPS
- LND über den REST-Proxy
- LNDhub über die REST-API

![Bild](assets/en/31.webp)

Klicken Sie auf "Verbindung testen", um sicherzustellen, dass Sie die Verbindungsdetails korrekt eingegeben haben. Nachdem die Verbindung als gut bestätigt wurde, klicken Sie auf speichern, und BTCPay Server zeigt an, dass der Store mit einem Lightning-Knoten aktualisiert wurde.

### Internen Lightning-Knoten LND verwalten (Serveradministrator)

Nachdem der interne Lightning-Knoten verbunden wurde, werden Serveradministratoren neue Kacheln auf dem Dashboard speziell für Lightning-Informationen bemerken.

- Lightning-Guthaben
- BTC in Kanälen
  - BTC in öffnenden Kanälen
  - BTC lokales Guthaben
  - BTC entferntes Guthaben
  - BTC schließende Kanäle
- BTC On-Chain
  - BTC bestätigt
  - BTC unbestätigt
  - BTC reserviert
- Lightning-Dienste
  - Ride the Lightning (RTL).

Durch Klicken entweder auf das Ride the Lightning-Logo im Kachel "Lightning-Dienste" oder auf "Lightning" unter Wallets im linken Menü können Serveradministratoren RTL für die Verwaltung des Lightning-Knotens erreichen.

**Hinweis!**

Verbindung zum internen Lightning-Knoten schlägt fehl - Wenn die interne Verbindung fehlschlägt, bestätigen Sie:

1. Der Bitcoin On-Chain-Knoten ist vollständig synchronisiert
2. Der interne Lightning-Knoten ist unter "Lightning" > "Einstellungen" > "BTC Lightning-Einstellungen" als "Aktiviert" markiert
   Wenn Sie keine Verbindung zu Ihrem Lightning-Knoten herstellen können, versuchen Sie, Ihren Server neu zu starten, oder lesen Sie die offizielle Dokumentation des BTCPay Servers für weitere Details; https://docs.btcpayserver.org/Troubleshooting/ . Sie können keine Lightning-Zahlungen in Ihrem Geschäft akzeptieren, bis Ihr Lightning-Knoten als "Online" angezeigt wird. Versuchen Sie, Ihre Lightning-Verbindung zu testen, indem Sie auf den Link "Public Node Info" klicken.

### Lightning-Wallet

Innerhalb der Option Lightning-Wallet in der linken Menüleiste finden Serveradministratoren einen einfachen Zugang zu RTL, ihren Public Node Info und spezifischen Lightning-Einstellungen für ihren BTCPay Server Store.

#### Interne Knoteninformationen

Serveradministratoren können auf die internen Knoteninformationen klicken und einen Blick auf ihren Serverstatus (Online/Offline) und die Verbindungszeichenfolge für Clearnet oder Tor werfen.

![Bild](assets/en/32.webp)

#### Verbindung ändern

Wenn der Geschäftsinhaber entscheidet, Änderungen in den Lightning-Einstellungen - Verbindung ändern vorzunehmen.
Neben den Public Node-Informationen des Geschäfts können Eigentümer diese Option finden. Sie führt zurück zur anfänglichen Einrichtung für die externe Lightning-Knotenverbindung, füllen Sie die neuen Lightning-Knoteninformationen aus, klicken Sie auf speichern und aktualisieren Sie den Store mit den neuen Knoteninformationen.

![Bild](assets/en/33.webp)

#### Dienste

Wenn der Serveradministrator entscheidet, mehrere Dienste für die Lightning-Implementierung zu installieren, werden diese hier aufgelistet. Mit einer Standard-LND-Implementierung werden Administratoren Ride The Lightning (RTL) als Standardwerkzeug für das Knotenmanagement haben.

#### BTC Lightning-Wallet-Einstellungen

Nachdem der Lightning-Knoten in einem vorherigen Schritt zum Store hinzugefügt wurde, können Geschäftsinhaber innerhalb der Einstellungen der Lightning-Wallet entscheiden, diese für ihren Store zu deaktivieren, indem sie den Toggle oben in den Lightning-Einstellungen verwenden.

![Bild](assets/en/34.webp)

#### Lightning-Zahlungsoptionen

Geschäftsinhaber können Parameter für die folgenden Punkte festlegen, um das Lightning-Erlebnis für ihre Kunden zu verbessern.

- Anzeige von Lightning-Zahlungsbeträgen in Satoshis.
- Hinzufügen von Hop-Hinweisen für private Kanäle zur Lightning-Rechnung.
- Vereinheitlichung von On-Chain- und Lightning-Zahlungs-URL/QR-Codes beim Checkout.
- Festlegen einer Beschreibungsvorlage für Lightning-Rechnungen.

#### LNURL

Geschäftsinhaber können wählen, ob sie LNURL verwenden möchten oder nicht. Eine Lightning Network URL oder LNURL ist ein vorgeschlagener Standard für Interaktionen zwischen Lightning-Zahler und -Empfänger. Kurz gesagt, ist eine LNURL eine mit bech32 codierte URL, die mit lnurl beginnt. Die Lightning-Wallet soll die URL entschlüsseln, die URL kontaktieren und auf ein JSON-Objekt mit weiteren Anweisungen warten, insbesondere ein Tag, das das Verhalten der knurl definiert.

- LNURL aktivieren
- LNURL Classic-Modus
  - Für Wallet-Kompatibilität, Bech32 codiert (klassisch) vs. Klartext-URL (kommend)
- Dem Zahlungsempfänger erlauben, einen Kommentar zu übermitteln.

### Beispiel 1

#### Verbindung zu Lightning mit dem internen Knoten (Administrator)

Diese Option ist nur verfügbar, wenn Sie der Administrator dieser Instanz sind oder wenn der Administrator die Standardeinstellungen geändert hat, bei denen Benutzer den internen Lightning-Knoten verwenden können.

Als Administrator klicken Sie in der linken Menüleiste auf die Lightning-Wallet. BTCPay Server wird bitten, eine von zwei Optionen für die Verbindung eines Lightning-Knotens zu verwenden, einen internen Knoten oder einen benutzerdefinierten externen Knoten. Klicken Sie auf Internen Knoten verwenden und dann auf speichern.

#### Verwaltung Ihres Lightning-Knotens (RTL)

Nach der Verbindung zum internen Lightning-Knoten wird BTCPay Server aktualisieren und eine Benachrichtigung "BTC Lightning-Knoten aktualisiert" anzeigen, was bestätigt, dass Sie nun Lightning mit Ihrem Store verbunden haben.

Die Verwaltung des Lightning-Knotens ist eine Aufgabe für den Administrator des Servers. Dies beinhaltet:

- Transaktionsmanagement
- Liquiditätsmanagement
  - Eingehende Liquidität
  - Ausgehende Liquidität
- Verwaltung von Peers und Kanälen
  - Verbundene Peers
  - Kanalgebühren
  - Kanalstatus
- Häufige Sicherungen der Kanalzustände vornehmen.
- Routing-Berichte überprüfen
- Alternativ Dienste wie Loop nutzen.

Die Verwaltung aller Lightning-Knoten erfolgt standardmäßig mit RTL (vorausgesetzt, Sie verwenden eine LND-Implementierung). Administratoren können in ihrem BTCPay Server auf ihre Lightning-Wallet klicken und finden dort einen Button, um RTL zu öffnen. Das Haupt-Dashboard von BTCPay Server wird nun mit den Lightning Network Kacheln aktualisiert, einschließlich eines Schnellzugriffs auf RTL.

### Beispiel 2

#### Verbindung mit Lightning über Alby herstellen

Wenn eine Verbindung mit einem Verwahrer wie Alby hergestellt wird, sollten Ladenbesitzer zuerst ein Konto erstellen, besuchen Sie: https://getalby.com/

![Bild](assets/en/35.webp)

Nachdem Sie das Alby-Konto erstellt haben, gehen Sie zu Ihrem BTCPay Server-Shop.

Schritt 1: Klicken Sie auf 'Ein Lightning-Knoten einrichten' im Dashboard oder 'Lightning' unter Wallets.

![Bild](assets/en/36.webp)

Schritt 2: Geben Sie Ihre Wallet-Verbindungsinformationen ein, die von Alby bereitgestellt wurden. Klicken Sie im Dashboard von Alby auf Wallet. Hier finden Sie "Wallet-Verbindungsinformationen". Kopieren Sie diese Informationen. Fügen Sie die Anmeldeinformationen von Alby in das Verbindungskonfigurationsfeld im BTCPay Server ein.

![Bild](assets/en/37.webp)

Schritt 3: Nachdem Sie dem BTCPay Server die Verbindungsdetails bereitgestellt haben, klicken Sie auf den Button "Verbindung testen", um sicherzustellen, dass die Verbindung ordnungsgemäß funktioniert. Beachten Sie die Nachricht "Verbindung zum Lightning-Knoten erfolgreich" am oberen Bildschirmrand. Dies bestätigt, dass alles in Ordnung ist.

![Bild](assets/en/38.webp)

Schritt 4: Klicken Sie auf speichern, und Ihr Shop ist nun mit einem Lightning-Knoten von Alby verbunden.

![Bild](assets/en/39.webp)

**!Hinweis!**

Vertrauen Sie einer Verwahrer-Lightning-Lösung nie mehr Wert an, als Sie bereit sind zu verlieren.

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie gelernt:

- Wie man einen internen oder externen Lightning-Knoten verbindet
- Die Inhalte und Funktionen verschiedener Lightning-bezogener Kacheln im Dashboard
- Wie man eine Lightning-Wallet mit Voltage Surge oder Alby konfiguriert

### Wissensbewertung Praktische Überprüfung

Beschreiben Sie einige der verschiedenen Optionen, um eine Lightning-Wallet mit Ihrem Shop zu verbinden.

# BTCPay Server Interface

<partId>25e88b81-e1ab-515f-a035-09f2a3075556</partId>

## Dashboard-Übersicht

<chapterId>410ff28b-a272-5c91-93e0-48d5b28c53ab</chapterId>

BTCPay Server ist ein modulares Softwarepaket. Es gibt jedoch Standards, die jeder BTCPay Server haben wird und mit denen der Administrator/Benutzer interagieren wird. Beginnend mit dem Dashboard. Der Hauptzugangspunkt jedes BTCPay Servers nach dem Einloggen. Das Dashboard gibt einen Überblick darüber, wie Ihr Shop performt, den aktuellen Kontostand der Wallet und die letzten Transaktionen in den letzten 7 Tagen. Da es sich um eine modulare Ansicht handelt, können Plugins diese Ansicht für ihren Nutzen verwenden und ihre Kacheln auf dem Dashboard erstellen. In diesem Kursbuch werden wir nur über Standard-Plugins/Apps und ihre jeweiligen Ansichten im BTCPay Server sprechen.

### Dashboard-Kacheln

Innerhalb der Hauptansicht des BTCPay Server Dashboards gibt es einige Standardkacheln. Diese Kacheln sind dafür gedacht, dass der Ladenbesitzer oder Administrator seinen Shop schnell in einer Übersicht verwalten kann.

- Kontostand der Wallet
- Transaktionsaktivität
- Lightning-Kontostand (falls Lightning im Shop aktiviert ist)
- Lightning-Dienste (falls Lightning im Shop aktiviert ist)
- Jüngste Transaktionen.
- Jüngste Rechnungen
- Aktuell aktive Crowdfunds
- Shop-Performance / meistverkaufte Artikel.
  Das Kachel "Wallet-Balance" bietet einen schnellen Überblick über die Mittel und die Leistung Ihres Wallets. Es kann entweder in BTC oder in Fiat-Währung angezeigt werden, in einem wöchentlichen, monatlichen oder jährlichen Diagramm.
  ![image](assets/en/40.webp)

### Transaktionsaktivität

Neben der Kachel "Wallet-Balance" zeigt der BTCPay Server einen schnellen Überblick über ausstehende Auszahlungen, die Anzahl der Transaktionen in den letzten 7 Tagen und ob Ihr Geschäft irgendwelche Rückerstattungen ausgestellt hat. Durch Klicken auf den Button "Verwalten" gelangen Sie in die Verwaltung für ausstehende Auszahlungen (erfahren Sie mehr über Auszahlungen im BTCPay Server - Kapitel Zahlungen).

![image](assets/en/41.webp)

### Lightning-Balance

Dies ist nur sichtbar, wenn Lightning aktiviert ist.

Wenn der Administrator den Zugang zum Lightning-Netzwerk erlaubt hat, verfügt das Dashboard des BTCPay Servers nun über eine neue Kachel mit Informationen zu Ihrem Lightning-Node. Wie viel BTC in Kanälen ist, wie dies lokal oder remote (eingehende oder ausgehende Liquidität) ausgeglichen ist, ob Kanäle schließen oder öffnen und wie viel Bitcoin on-chain auf dem Lightning-Node gehalten wird.

![image](assets/en/42.webp)

### Lightning-Dienste

Dies ist nur sichtbar, wenn Lightning aktiv ist.

Neben der Anzeige Ihrer Lightning-Balance auf dem Dashboard des BTCPay Servers werden Administratoren auch die Kachel für Lightning-Dienste sehen. Hier können Administratoren schnelle Buttons für Tools finden, die sie zur Verwaltung ihres Lightning-Nodes verwenden; zum Beispiel ist Ride the Lightning eines der Standardtools mit BTCPay Server für die Verwaltung von Lightning-Nodes.

![image](assets/en/43.webp)

### Kürzliche Transaktionen

Die Kachel "Kürzliche Transaktionen" zeigt die neuesten Transaktionen Ihres Geschäfts. Mit einem Klick kann der Administrator der BTCPay Server-Instanz nun die neueste Transaktion sehen und feststellen, ob darauf geachtet werden muss.

![image](assets/en/44.webp)

### Kürzliche Rechnungen

Die Kachel "Kürzliche Rechnungen" zeigt die 6 neuesten vom BTCPay Server generierten Rechnungen, einschließlich Status und Rechnungsbetrag. Die Kachel enthält auch einen Button "Alle anzeigen", um einfach auf die vollständige Rechnungsübersicht zugreifen zu können.

![image](assets/en/45.webp)

### Point Of Sale und Crowdfunds

Da der BTCPay Server eine Reihe von Standard-Plugins oder Apps liefert, sind Point Of Sale und Crowdfund die beiden Haupt-Plugins des BTCPay Servers. Mit jedem Geschäft und Wallet kann ein BTCPay Server-Benutzer so viele Point Of Sales oder Crowdfunds generieren, wie er für richtig hält. Jedes wird eine neue Dashboard-Kachel erstellen, die die Leistung der Plugins zeigt.

![image](assets/en/46.webp)

Beachten Sie den leichten Unterschied zwischen einer Point of Sale- und einer Crowdfund-Kachel. Der Administrator sieht die meistverkauften Artikel in der Point of Sales-Kachel. In der Crowdfund-Kachel wird dies zu Top-Perks. Beide Kacheln haben schnelle Buttons, um die jeweilige App zu verwalten und kürzlich erstellte Rechnungen von Top-Artikeln oder Top-Perks anzusehen.

![image](assets/en/47.webp)

**!?Hinweis!?**

Bilanzdiagramme und kürzliche Transaktionen sind nur für eine On-Chain-Zahlungsmethode verfügbar. Informationen über Lightning Network-Bilanzen und Transaktionen stehen noch aus. Ab der BTCPay Server-Version 1.6.0 sind grundlegende Lightning Network-Bilanzen verfügbar.

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Das Kernlayout der Kacheln auf der Hauptlandeseite ist als Dashboard bekannt.
- Ein grundlegendes Verständnis des Inhalts jeder Kachel.

### Wissensbewertung Rückblick

Listen Sie so viele Kacheln wie möglich aus dem Gedächtnis auf, die Sie vom Dashboard kennen.

## BTCPay Server - Geschäftseinstellungen

<chapterId>e8faef7b-278d-550e-a511-bc3a442daf64</chapterId>
Innerhalb der BTCPay Server-Software kennen wir 2 Arten von Einstellungen. BTCPay Server spezifische Einstellungen für den Store, die über den Einstellungsbutton in der linken Menüleiste unter dem Dashboard gefunden werden können, und BTCPay Server-Einstellungen, die am unteren Ende der Menüleiste direkt über dem Konto gefunden werden. Die server-spezifischen Einstellungen von BTCPay Server können nur von Serveradministratoren eingesehen werden.
Die Store-Einstellungen bestehen aus vielen Tabs, um jede Einstellungsgruppe zu kategorisieren.

- Allgemein
- Kurse
- Checkout-Erscheinungsbild
- Zugriffstoken
- Benutzer
- Rollen
- Webhooks
- Auszahlungsprozessoren
- E-Mails
- Formulare

### Allgemein

Im Tab Allgemeine Einstellungen legen Store-Besitzer ihre Markenidentität und Zahlungsstandards fest. Bei der Ersteinrichtung des Stores wurde ein Store-Name vergeben; dieser wird in den allgemeinen Einstellungen unter Store-Name widergespiegelt. Hier kann der Store-Besitzer auch seine Website anpassen, um sie an die Markenidentität anzupassen und eine Store-ID festlegen, damit der Administrator ihn in der Datenbank erkennen kann.

#### Branding

Da BTCPay Server FOSS ist, kann ein Store-Besitzer ein individuelles Branding vornehmen, um es an seinen Store anzupassen. Setzen Sie die Markenfarbe, speichern Sie die Logos Ihrer Marke und fügen Sie benutzerdefiniertes CSS für öffentlich/kundenorientierte Seiten hinzu (Rechnungen, Zahlungsanforderungen, Pull-Zahlungen)

#### Zahlung

In den Zahlungseinstellungen legen Store-Besitzer die Standardwährung ihres Stores fest (entweder in Bitcoin oder in einer beliebigen Fiat-Währung).

#### Erlaube jedem, Rechnungen zu erstellen

Diese Einstellung ist für Entwickler oder Erbauer auf dem BTCPay Server gedacht. Mit dieser Einstellung für Ihren Store aktiviert, ermöglicht sie der Außenwelt, Rechnungen auf Ihrer BTCPay Server-Instanz zu erstellen.

#### Zusätzliche Gebühr (Netzwerkgebühr) zu Rechnungen hinzufügen

Eine Funktion innerhalb von BTCPay, um Händler vor Dust-Attacken zu schützen oder Kunden, die später hohe Gebühren verursachen, wenn der Händler viel Bitcoin auf einmal bewegen muss. Zum Beispiel hat der Kunde eine Rechnung über 20$ erstellt und sie teilweise bezahlt, indem er 1$ 20 Mal bezahlt hat, bis die Rechnung vollständig bezahlt war. Der Händler hat jetzt eine größere Transaktion, was die Mining-Kosten erhöht, falls der Händler diese Mittel später bewegen möchte. Standardmäßig wendet BTCPay eine zusätzliche Netzwerkgebühr auf den Gesamtrechnungsbetrag an, um diese Ausgabe für den Händler zu decken, wenn die Rechnung in mehreren Transaktionen bezahlt wird. BTCPay bietet mehrere Optionen, um dieses Schutzmerkmal anzupassen. Sie können eine Netzwerkgebühr anwenden:

- Nur wenn der Kunde mehr als eine Zahlung für die Rechnung leistet (Im obigen Beispiel, wenn der Kunde eine Rechnung über 20\$ erstellt und 1\$ bezahlt hat, beträgt der jetzt fällige Gesamtbetrag der Rechnung 19\$ + Netzwerkgebühr. Die Netzwerkgebühr wird nach der ersten Zahlung angewendet)
- Bei jeder Zahlung (einschließlich der ersten Zahlung, in unserem Beispiel wäre der Gesamtbetrag sofort 20\$ + Netzwerkgebühr, auch bei der ersten Zahlung)
- Niemals Netzwerkgebühr hinzufügen (deaktiviert die Netzwerkgebühr vollständig)

Während es vor Dust-Transaktionen schützt, kann es auch negativ auf Unternehmen wirken, wenn es nicht richtig kommuniziert wird. Kunden könnten zusätzliche Fragen haben und denken, dass sie übermäßig belastet werden.

#### Rechnung verfällt, wenn der volle Betrag nicht nach X bezahlt wurde?

Der Rechnungstimer ist standardmäßig auf 15 Minuten eingestellt. Der Timer ist ein Schutzmechanismus gegen Volatilität, da er den Bitcoin-Betrag gemäß den Bitcoin-zu-Fiat-Kursen fixiert. Wenn der Kunde die Rechnung nicht innerhalb der festgelegten Zeit bezahlt, gilt die Rechnung als abgelaufen. Die Rechnung gilt als "bezahlt", sobald die Transaktion in der Blockchain sichtbar ist (0-Bestätigungen), aber als "abgeschlossen", wenn sie die vom Händler definierte Anzahl an Bestätigungen erreicht hat (üblicherweise 1-6). Der Timer ist nach Minuten anpassbar.

#### Die Rechnung als bezahlt betrachten, auch wenn der bezahlte Betrag X% weniger als erwartet ist?

Wenn ein Kunde ein Exchange-Wallet verwendet, um direkt für eine Rechnung zu bezahlen, nimmt die Börse eine kleine Gebühr. Das bedeutet, dass eine solche Rechnung nicht als vollständig abgeschlossen gilt. Die Rechnung erhält den Status "teilweise bezahlt". Hier können Sie den Prozentsatz festlegen, falls ein Händler unterbezahlte Rechnungen akzeptieren möchte.

### Gebühren

Im BTCPay Server wird, wenn eine Rechnung erstellt wird, immer der aktuellste und genaueste Bitcoin-zu-Fiat-Preis benötigt. Beim Erstellen eines neuen Stores im BTCPay Server werden Administratoren gebeten, ihre bevorzugte Preisquelle festzulegen; nachdem der Store eingerichtet ist, können Store-Besitzer ihre Preisquelle jederzeit in diesem Tab ändern.

#### Fortgeschrittene Regeln zur Preisfestsetzung

Hauptsächlich von Power-Usern verwendet. Wenn aktiviert, können Store-Besitzer Skripte rund um das Preisverhalten und wie sie ihre Kunden berechnen erstellen.

#### Testen

Ein schneller Testbereich für Ihre bevorzugten Währungspaare. Dies beinhaltet auch eine Funktion, um Standardwährungspaare über eine REST-Anfrage zu überprüfen.

### Erscheinungsbild des Checkouts

Der Tab für das Erscheinungsbild des Checkouts beginnt mit rechnungsspezifischen Einstellungen und einer Standardzahlungsmethode und ermöglicht spezifische Zahlungsmethoden, wenn festgelegte Anforderungen erfüllt sind.

#### Rechnungseinstellungen

Standardzahlungsmethoden. BTCPay Server hat in einer Standardkonfiguration drei Optionen.

- BTC (on-chain)
- BTC (LNURL-pay)
- BTC (Off-chain & Lightning)

Wir können Parameter für unseren Store festlegen, bei denen ein Kunde nur mit Lightning interagiert, wenn der Preis weniger als X Betrag ist und umgekehrt für On-Chain-Transaktionen, wenn X größer als Y ist, immer die On-Chain-Zahlungsoption präsentieren.

![Bild](assets/en/48.webp)

#### Checkout

Mit der Veröffentlichung von BTCPay Server 1.7 wurde eine neue Checkout-Schnittstelle eingeführt, Checkout V2, wie sie genannt wird. Seit der Veröffentlichung 1.9 wurde standardisiert, Administratoren und Store-Besitzer können den Checkout immer noch auf die vorherige Version einstellen. Durch Verwendung des Umschalters "Use the classic checkout" kann ein Store-Besitzer den Store auf das vorherige Checkout-Erlebnis zurücksetzen. BTCPay Server hat auch eine Auswahl an Voreinstellungen für Online-Handel oder ein In-Store-Erlebnis.

![Bild](assets/en/49.webp)

Wenn ein Kunde mit dem Store interagiert und eine Rechnung generiert, gibt es eine Ablaufzeit für die Rechnung. Standardmäßig setzt BTCPay Server dies auf 5 Minuten, und der Administrator kann dies nach Belieben einstellen. Die Checkout-Seite kann weiter angepasst werden, indem die folgenden Parameter überprüft werden:

- Zahlung mit Konfetti feiern
- Kopfzeile des Stores anzeigen (Name und Logo)
- Den "In Wallet bezahlen"-Knopf anzeigen
- On-Chain- und Off-Chain-Zahlungen URL/QRs vereinheitlichen
- Lightning-Zahlungsbeträge in Satoshis anzeigen
- Sprache beim Checkout automatisch erkennen

![Bild](assets/en/50.webp)

Wenn die automatische Spracherkennung nicht eingestellt ist, wird BTCPay Server standardmäßig Englisch anzeigen. Ein Store-Besitzer kann diese Standardeinstellung in seine bevorzugte Sprache ändern.

![Bild](assets/en/51.webp)

Klicken Sie auf das Dropdown-Menü, und Store-Besitzer können einen benutzerdefinierten HTML-Titel festlegen, der auf der Checkout-Seite angezeigt wird.

![Bild](assets/en/52.webp)

Um sicherzustellen, dass der Kunde seine Zahlungsmethode kennt, kann ein Store-Besitzer explizit einstellen, dass sein Checkout immer verlangt, dass die Benutzer ihre bevorzugte Zahlungsmethode wählen. Wenn die Rechnung bezahlt ist, erlaubt BTCPay Server dem Kunden, zum Webshop zurückzukehren. Store-Besitzer können diese Weiterleitung nach der Zahlung des Kunden automatisch einstellen.

![Bild](assets/en/53.webp)

#### Öffentlicher Beleg

Innerhalb der Einstellungen für den öffentlichen Beleg kann ein Store-Besitzer die Belegseiten öffentlich machen und die Zahlungsliste auf der Belegseite sowie den QR-Code des Belegs anzeigen, damit der Kunde ihn digital leicht zugänglich machen kann.

### Zugriffstoken

Zugriffstoken werden verwendet, um eine Verbindung zu bestimmten E-Commerce-Integrationen oder benutzerdefinierten Integrationen herzustellen.

### Benutzer

Geschäftsbenutzer sind dort, wo der Geschäftsinhaber seine Mitarbeiter, deren Konten und den Zugang zum Geschäft verwalten kann. Nachdem die Mitarbeiter ihre Konten erstellt haben, kann der Geschäftsinhaber spezifische Benutzer als Gastbenutzer oder Eigentümer zum Geschäft hinzufügen. Um die Rolle des Mitarbeiters weiter zu definieren, siehe den nächsten Abschnitt zu „BTCPay Server Store-Einstellungen - Rollen“.

### Rollen

Ein Geschäftsinhaber findet die standardmäßigen Benutzerrollen möglicherweise nicht aussagekräftig genug. In den Einstellungen für benutzerdefinierte Rollen kann ein Geschäftsinhaber die genauen Anforderungen für jede Rolle in seinem Unternehmen definieren.

(1) Um eine neue Rolle zu erstellen, klicken Sie auf den Button „+ Rolle hinzufügen“.

(2) Geben Sie einen Rollennamen ein, zum Beispiel „Kassierer“.

(3) Konfigurieren Sie die individuellen Berechtigungen für die Rolle.

- Ihre Geschäfte ändern.
- Mit Ihren Geschäften verknüpfte Exchange-Konten verwalten.
  - Mit Ihren Geschäften verknüpfte Exchange-Konten anzeigen.
- Ihre Pull-Zahlungen verwalten.
- Pull-Zahlungen erstellen.
  - Nicht genehmigte Pull-Zahlungen erstellen.
- Rechnungen ändern.
  - Rechnungen anzeigen.
  - Eine Rechnung erstellen.
  - Rechnungen von den mit Ihren Geschäften verbundenen Lightning-Knoten erstellen.
- Ihre Geschäfte anzeigen.
  - Rechnungen anzeigen.
  - Ihre Zahlungsanforderungen anzeigen.
  - Webhooks der Geschäfte ändern.
- Ihre Zahlungsanforderungen ändern.
  - Ihre Zahlungsanforderungen anzeigen.
- Die mit Ihren Geschäften verbundenen Lightning-Knoten nutzen.
  - Mit Ihren Geschäften verbundene Lightning-Rechnungen anzeigen.
  - Rechnungen von den mit Ihren Geschäften verbundenen Lightning-Knoten erstellen.
- Mittel auf mit Ihren Geschäften verknüpfte Exchange-Konten einzahlen.
- Mittel von Exchange-Konten auf Ihr Geschäft abheben.
- Mittel auf den Exchange-Konten Ihres Geschäfts handeln.

Wenn die Rolle erstellt wird, ist der Name festgelegt und kann später im Bearbeitungsmodus nicht geändert werden.

### Webhooks

Innerhalb von BTCPay Server ist es ziemlich einfach, einen neuen „Webhook“ zu erstellen. Im Tab „BTCPay Server Store-Einstellungen - Webhooks“ kann ein Geschäftsinhaber einfach einen neuen Webhook erstellen, indem er auf „+ Webhook erstellen“ klickt. Webhooks ermöglichen es BTCPay Server, HTTP-Ereignisse, die sich auf Ihr Geschäft beziehen, an andere Server oder E-Commerce-Integrationen zu senden.

Sie befinden sich jetzt in der Ansicht zum Erstellen eines Webhooks. Stellen Sie sicher, dass Sie Ihre Payload-URL kennen und fügen Sie diese in Ihren BTCPay Server ein. Während Sie die Payload-URL eingefügt haben, wird darunter das Webhook-Geheimnis angezeigt. Kopieren Sie das Webhook-Geheimnis und stellen Sie es am Endpunkt zur Verfügung. Wenn alles eingestellt ist, können Sie in BTCPay Server die automatische Neuübermittlung umschalten. Wir versuchen, jede fehlgeschlagene Lieferung nach 10 Sekunden, 1 Minute und bis zu 6 Mal nach 10 Minuten erneut zu liefern. Sie können zwischen jedem Ereignis umschalten oder die Ereignisse nach Ihren Bedürfnissen spezifizieren. Stellen Sie sicher, dass Sie den Webhook aktivieren und klicken Sie auf Webhook hinzufügen, um ihn zu speichern.

Webhooks sind nicht dazu gedacht, mit der Bitpay API kompatibel zu sein. Es gibt zwei separate IPNs (in BitPay-Begriffen: „Instant Payment Notifications“) in BTCPay Server.

- Webhook
- Benachrichtigungen

Verwenden Sie nur die Benachrichtigungs-URL, wenn Sie Rechnungen über die Bitpay-API erstellen.

### Auszahlungsprozessoren

Auszahlungsprozessoren arbeiten zusammen mit dem Auszahlungskonzept im BTCPay Server. Ein Auszahlungsaggregator, um mehrere Transaktionen zu bündeln und diese auf einmal zu senden. Mit Auszahlungsprozessoren kann ein Ladenbesitzer die gebündelten Auszahlungen automatisieren. BTCPay Server bietet zwei Methoden für automatisierte Auszahlungen, On-Chain und Off-Chain (LN).

Der Ladenbesitzer kann beide Auszahlungsprozessoren separat konfigurieren. Ein Ladenbesitzer möchte möglicherweise den On-Chain-Prozessor nur alle X Stunden ausführen, während Off-Chain möglicherweise alle paar Minuten läuft. Für On-Chain können Sie auch ein Ziel festlegen, in welchem Block es enthalten sein soll. Standardmäßig ist dies auf 1 (oder den nächsten verfügbaren Block) gesetzt. Beachten Sie, dass die Einstellung des Off-Chain-Auszahlungsprozessors nur den Intervalltimer hat und kein Blockziel. Lightning-Netzwerk-Zahlungen sind sofortig.

![Bild](assets/en/62.webp)
![Bild](assets/en/63.webp)

Ladenbesitzer können den On-Chain-Prozessor nur konfigurieren, wenn sie eine Hot-Wallet mit ihrem Laden verbunden haben.

![Bild](assets/en/64.webp)

Nachdem Sie einen Auszahlungsprozessor eingerichtet haben, können Sie diesen schnell entfernen oder ändern, indem Sie zum Tab Auszahlungsprozessor in den BTCPay Server Laden-Einstellungen zurückkehren.

**!?Hinweis!?**

Auszahlungsprozessor On-Chain - Der On-Chain-Auszahlungsprozessor kann nur in einem Laden funktionieren, der mit einer verbundenen Hot-Wallet konfiguriert ist. Wenn keine Hot-Wallet verbunden ist, besitzt BTCPay Server nicht die Schlüssel zur Wallet und kann die Auszahlungen nicht automatisch verarbeiten.

### E-Mails

BTCPay Server kann E-Mails für Benachrichtigungen verwenden oder, wenn korrekt eingestellt, um Konten wiederherzustellen, die auf der Instanz erstellt wurden, da BTCPay Server standardmäßig keine E-Mail sendet, wenn das Passwort verloren geht, zum Beispiel.

![Bild](assets/en/65.webp)

Bevor ein Ladenbesitzer E-Mail-Regeln festlegen kann, die bei bestimmten Ereignissen seines Ladens ausgelöst werden, müssen wir einige grundlegende E-Mail-Einstellungen vornehmen. BTCPay Server benötigt diese Einstellungen, um E-Mails für Ereignisse basierend auf Ihrem Laden oder für Passwort-Resets zu senden.

BTCPay Server hat es einfacher gemacht, diese Informationen auszufüllen, indem die Option "Schnellbefüllung" verwendet wird:

- Gmail.com
- Yahoo.com
- Mailgun
- Office365
- SendGrid

Durch Verwenden der Schnellbefüllungsoption wird BTCPay Server die Felder für den SMTP-Server und Port vorab ausfüllen; jetzt muss der Ladenbesitzer nur noch seine Anmeldeinformationen in einer E-Mail-Adresse, Login (der in der Regel Ihrer E-Mail-Adresse entspricht) und Ihr Passwort ausfüllen. Die erweiterte Option, die BTCPay Server in den E-Mail-Einstellungen bietet, ist das Deaktivieren von TLS-Zertifikatssicherheitsprüfungen; standardmäßig ist dies Aktiviert.

![Bild](assets/en/66.webp)

Mit E-Mail-Regeln kann ein Ladenbesitzer spezifische Ereignisse festlegen, um E-Mails an spezifische E-Mail-Adressen auszulösen.

- Rechnung erstellt
- Rechnung hat Zahlung erhalten
- Rechnung wird bearbeitet
- Rechnung abgelaufen
- Rechnung beglichen
- Rechnung ungültig
- Rechnungszahlung beglichen

Wenn der Kunde eine E-Mail-Adresse angegeben hat, können diese Auslöser auch die Informationen an den Kunden senden. Ladenbesitzer können die Betreffzeile vorab ausfüllen, um klarzumachen, warum diese E-Mail erfolgte und welcher Auslöser sie verursacht hat.

![Bild](assets/en/67.webp)

### Formulare

Da BTCPay Server keine Daten sammelt, möchte ein Ladenbesitzer möglicherweise ein benutzerdefiniertes Formular zu seinem Checkout-Erlebnis hinzufügen; auf diese Weise kann der Ladenbesitzer zusätzliche Informationen von seinem Kunden sammeln. Der BTCPay Server Formular-Builder besteht aus zwei Teilen, einer visuellen und einer fortgeschritteneren Codeansicht der Formulare.
Beim Erstellen eines neuen Formulars öffnet der BTCPay Server ein neues Fenster, das grundlegende Informationen darüber anfordert, was Ihr neues Formular abfragen soll. Zunächst muss der Ladenbesitzer seinem neuen Formular einen eindeutigen Namen geben, dieser Name kann NACH dessen Festlegung NICHT geändert werden.
![Bild](assets/en/68.webp)

Nachdem der Ladenbesitzer dem Formular einen Namen gegeben hat, können Sie auch den Schalter für "Formular zur öffentlichen Nutzung zulassen" auf EIN umlegen, und er wird grün. Dies geschieht, damit das Formular an jedem kundenorientierten Ort verwendet werden kann. Wenn beispielsweise ein Ladenbesitzer eine separate Rechnung nicht über seinen Point Of Sale erstellt, möchte er möglicherweise dennoch die Informationen vom Kunden sammeln; dieses Umschalten auf EIN ermöglicht das Sammeln dieser Informationen.

![Bild](assets/en/69.webp)

Jedes Formular beginnt mit mindestens 1 neuem Formularfeld. Ein Ladenbesitzer kann auswählen, welcher Typ das Feld sein soll;

- Text
- Zahl
- Passwort
- E-Mail
- URL
- Telefonnummern
- Datum
- Versteckte Felder
- Fieldset
- Ein Textbereich für offene Kommentare.
- Optionsauswahl

Jeder Typ kommt mit seinen Parametern zum Ausfüllen. Der Ladenbesitzer kann es nach seinem Belieben einstellen. Unter dem ersten erstellten Feld können Ladenbesitzer diesem einen Formular neue Felder hinzufügen.

![Bild](assets/en/70.webp)

#### Fortgeschrittene benutzerdefinierte Formulare

BTCPay Server ermöglicht es Ihnen auch, Formulare im Code zu erstellen. Insbesondere JSON. Anstatt den Editor anzusehen, können Ladenbesitzer auf die CODE-Schaltfläche direkt neben dem Editor klicken und in den Code ihrer Formulare gelangen. In einer Felddefinition können nur die folgenden Felder festgelegt werden; die Werte der Felder werden in den Metadaten der Rechnung gespeichert:

| Feld                  | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .fields.constant      | Wenn wahr, muss der .value im Formulardefinition gesetzt werden, und der Benutzer wird nicht in der Lage sein, den Wert des Feldes zu ändern. (Beispiel: die Version der Formulardefinition)                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.type          | Der HTML-Eingabetyp Text, Radio, Checkbox, Passwort, Versteckt, Button, Farbe, Datum, Datumszeit-lokal, Monat, Woche, Zeit, E-Mail, Zahl, Bereich, Suche, URL, Auswahl, Tel                                                                                                                                                                                                                                                                                                                                                                                                               |
| .fields.options       | Wenn .fields.type Auswahl ist, die Liste der auswählbaren Werte                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| .fields.options.text  | Der für diese Option angezeigte Text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.options.value | Der Wert des Feldes, wenn diese Option ausgewählt ist                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.type=fieldset | Erstellt ein HTML-Fieldset um die Kinder .fields.fields (siehe unten)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| .fields.name          | Der JSON-Eigenschaftsname des Feldes, wie er in den Metadaten der Rechnung erscheinen wird                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.value         | Der Standardwert des Feldes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| .fields.required      | Wenn wahr, wird das Feld erforderlich sein                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| .fields.label         | Das Label des Feldes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| .fields.helpText      | Zusätzlicher Text, um eine Erklärung für das Feld zu bieten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| .fields.fields        | Sie können Ihre Felder hierarchisch organisieren, sodass untergeordnete Felder in den Metadaten der Rechnung eingebettet werden können. Diese Struktur kann Ihnen helfen, die gesammelten Informationen besser zu organisieren und zu verwalten, wodurch sie leichter zugänglich und interpretierbar werden. Wenn Sie beispielsweise ein Formular haben, das Kundeninformationen sammelt, können Sie die Felder unter einem übergeordneten Feld namens Kunde zusammenfassen. Innerhalb dieses übergeordneten Feldes könnten Sie untergeordnete Felder wie Name, E-Mail und Adresse haben. |

Der Feldname repräsentiert den JSON-Eigenschaftsnamen, der den vom Benutzer bereitgestellten Wert in den Metadaten der Rechnung speichert. Einige bekannte Namen können interpretiert werden und die Einstellungen der Rechnung ändern.

| Feldname         | Beschreibung             |
| ---------------- | ------------------------ |
| invoice_amount   | Der Betrag der Rechnung  |
| invoice_currency | Die Währung der Rechnung |

Sie können die Felder einer Rechnung automatisch vorab ausfüllen, indem Sie Abfragezeichenfolgen zur URL des Formulars hinzufügen, wie z.B. "?your_field=value".

Hier sind einige Anwendungsfälle für diese Funktion:

- Unterstützung der Benutzereingabe: Felder mit bekannten Kundeninformationen vorab ausfüllen, um es den Benutzern zu erleichtern, das Formular auszufüllen. Wenn Sie beispielsweise die E-Mail-Adresse eines Kunden bereits kennen, können Sie das E-Mail-Feld vorab ausfüllen, um ihnen Zeit zu sparen.
- Personalisierung: Anpassen des Formulars basierend auf Kundenpräferenzen oder -segmentierung. Wenn Sie beispielsweise verschiedene Kundenebenen haben, können Sie das Formular mit relevanten Daten vorab ausfüllen, wie z.B. ihrer Mitgliedsstufe oder spezifischen Angeboten.
- Tracking: Verfolgen Sie die Quelle von Kundenbesuchen mit Hilfe von versteckten Feldern und vorab ausgefüllten Werten. Sie können beispielsweise Links mit vorab ausgefüllten utm_media-Werten für jeden Marketingkanal (z.B. Twitter, Facebook, E-Mail) erstellen. Dies hilft Ihnen, die Wirksamkeit Ihrer Marketingbemühungen zu analysieren.
- A/B-Tests: Felder mit verschiedenen Werten vorab ausfüllen, um verschiedene Formularversionen zu testen, was Ihnen ermöglicht, das Benutzererlebnis und die Konversionsraten zu optimieren.

### Fähigkeiten Zusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Das Layout und die Funktionen der Tabs in den Store-Einstellungen
- Eine Vielzahl von Optionen zur Feinabstimmung der Behandlung von zugrundeliegenden Wechselkursen, Teilzahlungen, geringfügigen Unterzahlungen und mehr.
- Anpassen des Erscheinungsbilds des Checkouts, einschließlich preisabhängiger Hauptkette vs. Lightning-Aktivierung auf Rechnungen.
- Verwalten von Zugriffsebenen und Berechtigungen für verschiedene Rollen im Store.
- Konfigurieren von automatisierten E-Mails und deren Auslösern
- Erstellen von benutzerdefinierten Formularen zur Erfassung zusätzlicher Kundeninformationen beim Checkout.

### Wissensbewertungen

#### KA Review

Was ist der Unterschied zwischen Store-Einstellungen und Server-Einstellungen?

#### KA Hypothetisch

Beschreiben Sie einige Optionen, die Sie in Checkout Appearance > Invoice Settings auswählen könnten, und warum.

## BTCPay Server - Servereinstellungen

<chapterId>1dd858a2-49ea-586b-9bc1-75a65f508df6</chapterId>

BTCPay Server besteht aus zwei verschiedenen Einstellungsbereichen. Einer ist den Store-Einstellungen gewidmet und der andere den Server-Einstellungen. Letzterer ist nur verfügbar, wenn Sie ein Serveradministrator sind und nicht für Store-Besitzer. Serveradministratoren können Benutzer hinzufügen, benutzerdefinierte Rollen erstellen, den E-Mail-Server konfigurieren, Richtlinien festlegen, Wartungsaufgaben durchführen, alle an BTCPay Server angebundenen Dienste überprüfen, Dateien auf den Server hochladen oder Logs überprüfen.

### Benutzer

Wie im vorherigen Teil erwähnt, können Serveradministratoren Benutzer zu ihrem Server einladen, indem sie sie zum Benutzer-Tab hinzufügen.

### Serverweite benutzerdefinierte Rollen

BTCPay Server kennt zwei Arten von benutzerdefinierten Rollen, die spezifischen benutzerdefinierten Rollen des Stores und die serverweiten benutzerdefinierten Rollen in den BTCPay Server-Einstellungen. Beide verfügen über einen ähnlichen Satz von Berechtigungen; jedoch, wenn sie über die BTCPay Server-Einstellungen - Rollen-Tab festgelegt werden, wird die angewendete Rolle serverweit gelten und auf mehrere Stores angewendet. Beachten Sie ein "Serverweit"-Tag bei den benutzerdefinierten Rollen in den Servereinstellungen.

### Serverweite benutzerdefinierte Rollen

Serverweite benutzerdefinierte Rollenberechtigungen;

- Ändern Sie Ihre Stores.
- Verwalten Sie mit Ihren Stores verknüpfte Exchange-Konten.
  - Sehen Sie sich mit Ihren Stores verknüpfte Exchange-Konten an.
- Verwalten Sie Ihre Pull-Zahlungen.
- Erstellen Sie Pull-Zahlungen.
  - Erstellen Sie nicht genehmigte Pull-Zahlungen.
- Ändern Sie Rechnungen.
  - Sehen Sie sich Rechnungen an.
  - Erstellen Sie eine Rechnung.
  - Erstellen Sie Rechnungen von den mit Ihren Stores assoziierten Lightning-Knoten.
- Sehen Sie sich Ihre Stores an.
  - Sehen Sie sich Rechnungen an.
  - Sehen Sie sich Ihre Zahlungsanfragen an.
  - Ändern Sie die Webhooks der Stores.
- Ändern Sie Ihre Zahlungsanfragen.
  - Sehen Sie sich Ihre Zahlungsanfragen an.
- Nutzen Sie die mit Ihren Stores assoziierten Lightning-Knoten.
  - Sehen Sie sich die mit Ihren Stores assoziierten Lightning-Rechnungen an.
  - Erstellen Sie Rechnungen von den mit Ihren Stores assoziierten Lightning-Knoten.
- Einzahlen von Geldern auf mit Ihren Stores verknüpfte Exchange-Konten.
- Abheben von Geldern von Exchange-Konten auf Ihren Store.
- Handeln Sie mit Geldern auf den Exchange-Konten Ihres Stores.

**!?Hinweis!?**

Wenn die Rolle erstellt wird, ist der Name festgelegt und kann später im Bearbeitungsmodus nicht geändert werden.

### E-Mail

Die serverweiten E-Mail-Einstellungen ähneln denen der spezifischen E-Mail-Einstellungen für Stores. Diese Einrichtung behandelt jedoch nicht nur Auslöser für Stores oder Administratorprotokolle. Diese E-Mail-Einrichtung ermöglicht auch die Passwortwiederherstellung auf dem BTCPay Server beim Login. Sie funktioniert ähnlich wie die spezifischen Einstellungen für Stores; Administratoren können schnell ihre E-Mail-Parameter ausfüllen, ihre E-Mail-Zugangsdaten eingeben, und der Server kann nun E-Mails senden.

### Richtlinien

BTCPay Server-Politikadministratoren können einige Einstellungen zu Themen wie bestehende Benutzereinstellungen, neue Benutzereinstellungen, Benachrichtigungseinstellungen und Wartungseinstellungen festlegen. Diese sind dafür gedacht, neue Benutzer als Admin oder normale Benutzer zu registrieren oder sogar BTCPay Server durch Hinzufügen zu Ihrem Serverheader vor Suchmaschinen zu verbergen.

#### Einstellungen für bestehende Benutzer

Die hier verfügbaren Optionen sind von benutzerdefinierten Rollen getrennt. Diese zusätzlichen Berechtigungen könnten einen Store oder Store-Besitzer Angriffen aussetzen. Richtlinien, die bestehenden Benutzern hinzugefügt werden können:

- Nicht-Admins erlauben, den internen Lightning-Knoten in ihren Stores zu verwenden.
  - Dies würde es Store-Besitzern ermöglichen, den Lightning-Knoten des Serveradministrators und damit seine Gelder zu verwenden! Vorsicht, dies ist keine Lösung, um Zugang zu Lightning zu gewähren.
- Nicht-Admins erlauben, Hot Wallets für ihre Stores zu erstellen.
  - Dies würde jedem mit einem Konto auf Ihrer BTCPay Server-Instanz erlauben, Hot-Wallets zu erstellen und ihren Wiederherstellungsschlüssel auf dem Server des Administrators zu speichern. Dies könnte den Administrator haftbar machen, da er die Gelder Dritter hält!
- Nicht-Admins erlauben, Hot Wallets für ihre Stores zu importieren.
  - Ähnlich wie beim Erstellen von Hot-Wallets erlaubt diese Richtlinie das Importieren einer Hot-Wallet, mit den gleichen Gefahren, die im Abschnitt zum Erstellen von Hot-Wallets erwähnt wurden.

#### Einstellungen für neue Benutzer

Wir können einige wichtige Einstellungen festlegen, um neue Benutzer, die zum Server kommen, zu verwalten. Wir können eine Bestätigungs-E-Mail für neue Registrierungen einrichten, die Erstellung neuer Benutzer über den Anmeldebildschirm deaktivieren und den Zugang von Nicht-Admins zur Benutzererstellung über die API einschränken.

- Eine Bestätigungs-E-Mail für die Registrierung erforderlich machen.
  - Der Serveradministrator muss einen E-Mail-Server eingerichtet haben!
- Neue Benutzerregistrierung auf dem Server deaktivieren
- Zugang von Nicht-Admins zum API-Endpunkt für die Benutzererstellung deaktivieren.

Standardmäßig hat BTCPay Server die neue Benutzerregistrierung deaktiviert und den Zugang von Nicht-Admins zum API-Endpunkt für die Benutzererstellung ausgeschaltet. Dies geschieht aus Sicherheitsgründen, damit keine zufällige Person, die den BTCPay Login Ihres Servers gefunden haben könnte, Konten erstellen kann.

#### Benachrichtigungseinstellungen

![image](assets/en/76.webp)

#### Wartungseinstellungen

BTCPay Server ist ein Open-Source-Projekt, das auf GitHub lebt. Immer wenn BTCPay Server eine neue Version der Software veröffentlicht, können Administratoren benachrichtigt werden, dass eine neue Version verfügbar ist. Administratoren möchten möglicherweise auch Suchmaschinen (Google, Yahoo, DuckDuckGo) davon abhalten, den BTCPay Server-Domain zu indizieren. Da BTCPay Server FOSS ist, möchten Entwickler weltweit möglicherweise neue Funktionen erstellen; BTCPay Server verfügt über eine experimentelle Funktion, die bei Aktivierung einem Administrator ermöglicht, Funktionen zu nutzen, die noch nicht für die Produktion gedacht sind, rein zu Testzwecken.

- Überprüfen Sie Veröffentlichungen auf GitHub und benachrichtigen Sie, wenn eine neue BTCPay Server-Version verfügbar ist.
- Suchmaschinen davon abhalten, diese Website zu indizieren
- Experimentelle Funktionen aktivieren.

![image](assets/en/77.webp)

#### Plugins

BTCPay Server kann Plugins hinzufügen und seinen Funktionsumfang erweitern. Die Plugins werden standardmäßig aus dem BTCPay Server Plugin-Builder-Repository geladen. Ein Administrator kann jedoch wählen, Plugins in einem Pre-Release-Zustand zu sehen, und wenn der Plugin-Entwickler es erlaubt, kann der Serveradministrator nun Beta-Versionen von Plugins installieren.

![image](assets/en/78.webp)

##### Anpassungseinstellungen

Eine Standard-BTCPay Server-Installation wird über die bei der Installation festgelegte Domain erreichbar sein. Ein Serveradministrator kann jedoch die Root-Domain umleiten und eine der erstellten Apps aus einem bestimmten Store anzeigen. Der Serveradministrator kann auch spezifische Domains bestimmten Apps zuordnen.

- Zeige die App auf der Wurzel der Website
  - Zeigt eine Liste möglicher Apps, die auf der Root-Domain angezeigt werden sollen.

![image](assets/en/79.webp)

- Spezifische Domains bestimmten Apps zuordnen.
  - Wenn Sie klicken, um eine spezifische Domain für bestimmte Apps einzurichten, kann der Administrator so viele Domains wie nötig auf spezifische Apps ausrichten.

![image](assets/en/80.webp)

#### Block-Explorer

BTCPay Server kommt standardmäßig mit mempool.space als seinem Block-Explorer für Transaktionen. Wenn BTCPay Server eine neue Rechnung generiert und eine Transaktion damit verbunden ist, kann der Ladenbesitzer klicken, um die Transaktion zu öffnen; BTCPay Server wird standardmäßig auf mempool.space als Block-Explorer hinweisen; ein Serveradministrator kann dies nach seinen Vorlieben ändern.

![image](assets/en/81.webp)

### Dienste

Die BTCPay Server-Einstellungen: Der Dienste-Tab bietet einen Überblick über die Komponenten, die Ihr BTCPay Server verwendet. Die Dienste, die Ihr BTCPay Server bereitstellt, können je nach Bereitstellungsmethode variieren.

Ein BTCPay Server-Administrator kann auf „See information“ hinter jedem Dienst klicken, um ihn zu öffnen und spezifische Einstellungen vorzunehmen.

![image](assets/en/82.webp)

#### LND (gRPC)

BTCPay stellt LNDs gRPC-Dienst für den externen Gebrauch zur Verfügung; Sie finden hier Verbindungsinformationen; kompatible Wallets sind hier aufgelistet. BTCPay Server bietet auch einen QR-Code für die Verbindung zum Scannen und Anwenden im mobilen Wallet.

Serveradministratoren können weitere Details öffnen, um zu sehen;

- Host-Details
- Verwendung von SSL
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon
- GRPC SSL Cipher Suite (GRPC_SSL_CIPHER_SUITES)

#### LND (REST)

BTCPay stellt LNDs REST-Dienst für den externen Gebrauch zur Verfügung; Sie finden hier Verbindungsinformationen; kompatible Wallets sind hier aufgelistet. Zu den kompatiblen Wallets gehören Joule, Alby und ZeusLN. BTCPay Server bietet einen QR-Code für die Verbindung, scannen und anwenden im kompatiblen Wallet.

- REST Uri
- Macaroon
- AdminMacaroon
- InvoiceMacaroon
- ReadonlyMacaroon

#### LND Seed Backup

Das LND Seed Backup ist nützlich, um Mittel aus Ihrer LND-Wallet wiederherzustellen, falls Ihr Server beschädigt wird. Da der Lightning-Knoten eine Hot-Wallet ist, finden Sie die vertraulichen Seed-Informationen auf dieser Seite.

LND dokumentiert den Wiederherstellungsprozess. Siehe https://github.com/lightningnetwork/lnd/blob/master/docs/recovery.md für die Dokumentation.

#### Ride The Lightning

Ride the Lightning ist ein Verwaltungstool für Lightning-Knoten, das als Open-Source-Software entwickelt wurde. BTCPay Server verwendet RTL als Komponente zur Verwaltung von Lightning-Knoten in seinem Stack. BTCPay Server-Administratoren können RTL über die Servereinstellungen - Services-Tab oder durch Klicken auf die Lightning-Wallet erreichen.

#### Full node P2P

Server-Administratoren möchten vielleicht ihre Bitcoin-Node mit einer mobilen Wallet verbinden. Diese Seite bietet Informationen, um sich remote über das P2P-Protokoll mit Ihrer Full Node zu verbinden. Zum Zeitpunkt der Erstellung dieses Buches listet BTCPay Server Blockstream Green und Wasabi Wallet als kompatible Wallets auf. BTCPay Server gibt einen QR-Code für die Verbindung, scannen und in der kompatiblen Wallet anwenden.

#### Full node RPC

Diese Seite bietet Informationen, um sich remote über das RPC-Protokoll mit Ihrer Full Node zu verbinden.

#### SSH

SSH wird zu Wartungszwecken verwendet. BTCPay Server zeigt den anfänglichen Verbindungsbefehl, um Ihren Server zu erreichen, und SSH-öffentliche Schlüssel, die autorisiert sind, eine Verbindung zu Ihrem Server herzustellen. Server-Administratoren möchten SSH-Änderungen über die Benutzeroberfläche von BTCPay Server deaktivieren.

#### Dynamisches DNS

Dynamisches DNS ermöglicht es Ihnen, einen stabilen DNS-Namen zu haben, der auf Ihren Server zeigt, auch wenn sich Ihre IP-Adresse regelmäßig ändert. Dies wird empfohlen, wenn Sie BTCPay Server zu Hause hosten und einen Clearnet-Domainnamen haben möchten, um auf Ihren Server zuzugreifen.

Beachten Sie, dass Sie Ihre NAT und die BTCPay Server-Installation richtig konfigurieren müssen, um das HTTPS-Zertifikat zu erhalten.

### Theme

BTCPay Server kommt standardmäßig mit zwei Themes: Licht- und Dunkelmodus. Diese können umgeschaltet werden, indem man unten links auf Konto klickt und zwischen Dunkeltheme oder Lichttheme wechselt. BTCPay Server-Administratoren können ihr eigenes Theme hinzufügen, indem sie ein benutzerdefiniertes CSS-Theme bereitstellen.

Administratoren können das Licht-/Dunkeltheme erweitern, indem sie ihr eigenes benutzerdefiniertes CSS hinzufügen oder ihr benutzerdefiniertes Theme als vollständiges Custom festlegen.

![Bild](assets/en/83.webp)

#### Server Branding

Server-Administratoren können das BTCPay Server-Branding ändern, indem sie ein serverweites Branding Ihres Unternehmens einstellen. Da BTCPay Server FOSS ist, können Server-Administratoren die Software white labeln und das Aussehen an ihr Geschäft anpassen.

![Bild](assets/en/84.webp)

### Wartung

Als Server-Administrator erwarten Ihre Benutzer, dass Sie sich gut um den Server kümmern. Im Wartungstab von BTCPay Server kann der Admin einige grundlegende Wartungsarbeiten durchführen. Setzen Sie den Domainnamen auf die BTCPay Server-Instanz, starten Sie den Server neu oder führen Sie eine Bereinigung durch. Möglicherweise am wichtigsten, führen Sie Updates durch.

BTCPay Server ist ein Open-Source-Projekt und wird häufig aktualisiert. Jede neue Version wird entweder durch Ihre BTCPay Server-Benachrichtigungen oder auf den offiziellen Kanälen, über die BTCPay Server kommuniziert, angekündigt.

![Bild](assets/en/85.webp)

#### Domainname

Nachdem BTCPay Server eingerichtet wurde, möchte ein Administrator möglicherweise von seiner ursprünglichen Domain wechseln. Im Wartungstab kann der Administrator die Domain ändern. Nachdem die Bestätigung angeklickt und die entsprechenden DNS-Einträge auf der Domain eingerichtet wurden, aktualisiert und startet BTCPay Server neu, um zur neuen Domain zurückzukehren.

![Bild](assets/en/86.webp)

#### Neustart

Starten Sie BTCPay Server und zugehörige Dienste neu.

![Bild](assets/en/87.webp)

#### Bereinigung

BTCPay Server läuft mit Docker-Komponenten; bei Updates können Reste von Docker-Images, temporäre Dateien usw. übrig bleiben. Serveradministratoren können dies bereinigen und Platz in ihrer Umgebung zurückgewinnen, indem sie das Bereinigungsskript ausführen.
![Bild](assets/en/88.webp)

#### Update

Möglicherweise die wichtigste Option im Wartungs-Tab. BTCPay Server wird von der Community entwickelt, und daher sind seine Update-Zyklen häufiger als bei den meisten Softwareprodukten. Wenn BTCPay Server eine neue Version hat, werden Administratoren in ihrem Benachrichtigungszentrum informiert. Durch Klicken auf die Update-Schaltfläche überprüft BTCPay Server GitHub auf die neueste Version, aktualisiert den Server und startet ihn neu. Vor dem Update wird Serveradministratoren immer geraten, die Release-Notizen zu lesen, die über die offiziellen Kanäle von BTCPay Server verteilt werden.

![Bild](assets/en/89.webp)

### Logs

Ein Problem zu haben, macht nie Spaß. Dieses Dokument erklärt den häufigsten Workflow und die Schritte, um Ihr Problem effizient zu identifizieren und es selbst oder mit Hilfe der Community zu lösen.

Das Identifizieren des Problems ist entscheidend.

#### Das Problem replizieren

Zuerst und vor allem versuchen Sie zu bestimmen, wann das Problem auftritt. Versuchen Sie, das Problem zu replizieren. Versuchen Sie, Ihren Server zu aktualisieren und neu zu starten, um zu überprüfen, ob Sie Ihr Problem reproduzieren können. Wenn es Ihr Problem besser beschreibt, machen Sie einen Screenshot.

##### Den Server aktualisieren

Überprüfen Sie Ihre Version von BTCPay Server, ob sie viel älter ist als die [neueste Version](https://github.com/btcpayserver/btcpayserver/releases) von BTCPay Server. Das Aktualisieren Ihres Servers kann das Problem lösen.

##### Den Server neu starten

Ihren Server neu zu starten, ist eine einfache Möglichkeit, viele der häufigsten Probleme mit BTCPay Server zu lösen. Möglicherweise müssen Sie sich per SSH in Ihren Server einloggen, um ihn neu zu starten.

##### Einen Dienst neu starten

Für einige Probleme müssen Sie möglicherweise nur einen bestimmten Dienst in Ihrer BTCPay Server-Installation neu starten. Wie zum Beispiel den lets encrypt Container neu zu starten, um das SSL-Zertifikat zu erneuern.

```bash
sudo su -
cd btcpayserver-docker
docker restart letsencrypt-nginx-proxy-companion
```

Verwenden Sie docker ps, um den Namen eines anderen Dienstes zu finden, den Sie neu starten möchten.

#### Durch die Logs schauen

Logs können ein wesentliches Stück Information liefern. In den folgenden Absätzen werden wir beschreiben, wie Sie die Log-Informationen für verschiedene Teile von BTCPay erhalten.

##### BTCPay Logs

Seit v1.0.3.8 können Sie einfach auf BTCPay Server-Logs über das Frontend zugreifen. Wenn Sie Serveradmin sind, gehen Sie zu Servereinstellungen > Logs und öffnen Sie die Log-Datei. Wenn Sie nicht wissen, was ein bestimmter Fehler in den Logs bedeutet, erwähnen Sie ihn beim Troubleshooting.

Wenn Sie detailliertere Logs wünschen und eine Docker-Installation verwenden, können Sie Logs spezifischer Docker-Container über die Befehlszeile anzeigen. Sehen Sie diese [Anweisungen zum SSH-Zugriff](https://docs.btcpayserver.org/FAQ/ServerSettings/#how-to-ssh-into-my-btcpay-running-on-vp%C2%80) auf eine Instanz von BTCPay, die auf einem VPS läuft.

Auf der nächsten Seite eine allgemeine Liste der Containernamen, die für BTCPay Server verwendet werden.

Führen Sie die untenstehenden Befehle aus, um Logs nach Containername auszugeben. Ersetzen Sie den Containernamen, um andere Container-Logs anzusehen.

```bash
sudo su -
cd btcpayserver-docker
docker ps
docker logs --tail 100 generated_btcpayserver_1
```

| Logs für     | Containername                     |
| ------------ | --------------------------------- |
| BTCPayServer | generated_btcpayserver_1          |
| NBXplorer    | generated_nbxplorer_1             |
| Bitcoind     | btcpayserver_bitcoind             |
| Postgres     | generated_postgres_1              |
| proxy        | letsencrypt-nginx-proxy-companion |
| Nginx        | nginx-gen                         |
| Nginx        | nginx                             |
| c-lightning  | btcpayserver_clightning_bitcoin   |
| LND          | btcpayserver_lnd_bitcoin          |
| RTL          | generated_lnd_bitcoin_rtl_1       |
| Thunderhub   | generated_bitcoin_thub_1          |
| LibrePatron  | librepatron                       |
| Tor          | tor-gen                           |
| Tor          | tor                               |

###### Lightning Network LND - Docker

Es gibt einige Möglichkeiten, auf Ihre LND-Logs zuzugreifen, wenn Sie Docker verwenden. Melden Sie sich zunächst als Root an:

```bash
sudo su -
Navigieren Sie zum korrekten Verzeichnis:
cd btcpayserver-docker
# Finden Sie den Containernamen:
docker ps
Drucken Sie Logs nach Containernamen:
docker logs --tail 100 btcpayserver_lnd_bitcoin
```

Alternativ können Sie schnell Logs drucken, indem Sie die Container-ID verwenden (nur die ersten einzigartigen ID-Zeichen werden benötigt, wie die zwei am weitesten links stehenden Zeichen):

```bash
docker logs 'fügen Sie Ihre Container-ID hinzu'
```

Wenn Sie aus irgendeinem Grund mehr Logs benötigen

```bash
sudo su -
cd /var/lib/docker/volumes/generated_lnd_bitcoin_datadir/_data/logs/bitcoin/mainnet/
ls
```

Sie werden etwas wie folgendes sehen

```bash
lnd.log lnd.log.13 lnd.log.15 lnd.log.16.gz lnd.log.17.gz
```

Um auf unkomprimierte Logs dieser Logs zuzugreifen, verwenden Sie `cat lnd.log` oder wenn Sie einen anderen möchten, verwenden Sie `cat lnd.log.15`.

Um auf komprimierte Logs im `.gzip`-Format zuzugreifen, verwenden Sie `gzip -d lnd.log.16.gz` (in diesem Fall greifen wir auf `lnd.log.16.gz` zu). Dies sollte Ihnen eine neue Datei geben, in der Sie `cat lnd.log.16` machen können. Falls das oben Genannte nicht funktioniert, müssen Sie möglicherweise zuerst gzip mit `sudo apt-get install gzip` installieren.

###### Lightning Network c-lightning - Docker

```bash
sudo su -
docker ps
# Finden Sie die c-lightning Container-ID.
docker logs 'fügen Sie hier Ihre Container-ID ein'
```

alternativ verwenden Sie dies

```bash
docker logs --tail 100 btcpayserver_clightning_bitcoin
```

Sie können auch Log-Informationen mit dem c-lightning cli-Befehl erhalten.

```bash
bitcoin-lightning-cli.sh getlog
```

#### Bitcoin Node Logs

Zusätzlich zum [Betrachten der Logs](https://docs.btcpayserver.org/Troubleshooting/#2-looking-through-the-logs) Ihres Bitcoind-Containers können Sie auch eines der [bitcoin-cli-Befehle](https://developer.bitcoin.org/reference/rpc/index.html)

[(öffnet neues Fenster)](https://developer.bitcoin.org/reference/rpc/index.html) verwenden, um Informationen von Ihrem Bitcoin-Node zu erhalten. BTCPay beinhaltet ein Skript, das es Ihnen ermöglicht, einfach mit Ihrem Bitcoin-Node zu kommunizieren.

Innerhalb des btcpayserver-docker-Ordners erhalten Sie die Blockchain-Informationen mit Ihrem Node:

```bash
bitcoin-cli.sh getblockchaininfo
```

### Dateien

BTCPay Server verfügt über ein lokales Dateisystem und lädt Store (Produkt)-Assets, Logos und Branding direkt auf den Server hoch. Das Dateisystem des Servers ist nur für Serveradministratoren zugänglich; Ladenbesitzer können ihre Logos/Branding auf der Laden-Ebene hochladen.
Wenn der Serveradministrator im Reiter "Dateispeicher" ist, ist es möglich, direkt auf Ihren Server hochzuladen oder den Dateispeicheranbieter zu einem lokalen Dateisystem oder Azure Blob Storage zu wechseln.

![Bild](assets/en/90.webp)

![Bild](assets/en/91.webp)

### Fähigkeitszusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Der Unterschied zwischen Laden- und Servereinstellungen, insbesondere in Bezug auf Benutzer, Rollen und E-Mails
- Festlegen von serverweiten Richtlinien für die Verwendung und Erstellung von Lightning- oder Bitcoin-Hot-Wallets, neue Benutzerregistrierung und E-Mail-Benachrichtigungen.
- Wie man benutzerdefinierte Themen hinzufügt (anstatt der einfachen Hell/Dunkel-Optionen, die bereitgestellt werden) sowie benutzerdefinierte Logos erstellt
- Durchführung einfacher Serverwartungsaufgaben über die bereitgestellte GUI
- Probleme beheben, einschließlich der Beschaffung von Details für einen der Docker-Container oder Ihren Knoten
- Verwaltung des Dateispeichers

### Wissensbewertung

#### KA Konzeptuelle Überprüfung

Was ist der Unterschied in den Rollen, die über Server vs. Laden-Einstellungen zugewiesen werden, und was beschreibt einen möglichen Einsatz für die eine über die andere?

#### KA Praktische Überprüfung

Beschreiben Sie einige mögliche Anwendungsfälle, die im Reiter "Richtlinien" aktiviert sind.

#### KA Praktische Überprüfung

Beschreiben Sie einige Aktionen, die ein Administrator routinemäßig im Reiter "Wartung" durchführen könnte.

## BTCPay Server - Zahlungen

<chapterId>e2b71ff9-3f4f-5e71-9771-8e03fbbef00f</chapterId>

Eine Rechnung ist ein Dokument, das der Verkäufer an einen Käufer ausstellt, um Zahlung zu sammeln.

Im BTCPay Server stellt eine Rechnung ein Dokument dar, das innerhalb eines festgelegten Zeitintervalls zu einem festen Wechselkurs bezahlt werden muss. Rechnungen haben ein Ablaufdatum, weil sie den Wechselkurs innerhalb eines bestimmten Zeitrahmens fixieren, um den Empfänger vor Preisschwankungen zu schützen.

Das Kernstück des BTCPay Servers ist die Fähigkeit, als Bitcoin-Rechnungsverwaltungssystem zu fungieren. Eine Rechnung ist ein wesentliches Werkzeug für die Nachverfolgung und Verwaltung einer erhaltenen Zahlung.

Sofern Sie nicht eine integrierte [Wallet](https://docs.btcpayserver.org/Wallet/) verwenden, um Zahlungen manuell zu empfangen, werden alle Zahlungen innerhalb eines Ladens auf der Rechnungsseite angezeigt. Diese Seite sortiert Zahlungen kumulativ nach Datum und ist ein zentrales Element für die Rechnungsverwaltung und die Fehlersuche bei Zahlungen.

![Bild](assets/en/92.webp)

### Allgemein

#### Rechnungsstatus

Die untenstehende Tabelle listet die Standardrechnungsstatus in BTCPay auf und beschreibt sie, sowie schlägt häufige Aktionen vor. Aktionen sind nur Empfehlungen. Es liegt an den Benutzern, den besten Handlungsverlauf für ihren Anwendungsfall und ihr Geschäft zu definieren.

| Rechnungsstatus                     | Beschreibung                                                                                                                                    | Aktion                                                                                                                                                                                                      |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Neu                                 | Nicht bezahlt, Rechnungstimer ist noch nicht abgelaufen                                                                                         | Keine                                                                                                                                                                                                       |
| Neu (teilweise bezahlt)             | Bezahlt, nicht vollständig, Rechnungstimer ist noch nicht abgelaufen                                                                            | Keine                                                                                                                                                                                                       |
| Abgelaufen                          | Nicht bezahlt, Rechnungstimer abgelaufen                                                                                                        | Keine                                                                                                                                                                                                       |
| Abgelaufen (teilweise bezahlt) \*\* | Bezahlt, nicht in voller Höhe, und abgelaufen                                                                                                   | Kontaktieren Sie den Käufer, um eine Rückerstattung zu arrangieren oder bitten Sie ihn, den fälligen Betrag zu bezahlen. Optional Rechnung als beglichen oder ungültig markieren                            |
| Abgelaufen (spät bezahlt)           | Bezahlt, in voller Höhe, nachdem der Rechnungstimer abgelaufen ist                                                                              | Kontaktieren Sie den Käufer, um eine Rückerstattung zu arrangieren oder bearbeiten Sie die Bestellung, wenn späte Bestätigungen akzeptabel sind.                                                            |
| Abgerechnet (überbezahlt)           | Mehr als der Rechnungsbetrag bezahlt, abgerechnet, ausreichende Anzahl an Bestätigungen erhalten                                                | Kontaktieren Sie den Käufer, um eine Rückerstattung für den zusätzlichen Betrag zu arrangieren, oder warten Sie optional, bis der Käufer Sie kontaktiert.                                                   |
| In Bearbeitung                      | Vollständig bezahlt, aber nicht die erforderliche Anzahl an Bestätigungen gemäß den Einstellungen des Geschäfts erhalten                        | Kontaktieren Sie den Käufer, um eine Rückerstattung für den zusätzlichen Betrag zu arrangieren, oder warten Sie optional, bis der Käufer Sie kontaktiert.                                                   |
| In Bearbeitung (überbezahlt)        | Mehr als der Rechnungsbetrag bezahlt, nicht die erforderliche Anzahl an Bestätigungen erhalten                                                  | Warten Sie, bis die Zahlung abgerechnet ist, dann kontaktieren Sie den Käufer, um eine Rückerstattung für den zusätzlichen Betrag zu arrangieren, oder warten Sie optional, bis der Käufer Sie kontaktiert. |
| Abgerechnet                         | Vollständig bezahlt, ausreichende Anzahl an Bestätigungen im Geschäft erhalten                                                                  | Erfüllen Sie die Bestellung                                                                                                                                                                                 |
| Abgerechnet (markiert)              | Der Status wurde manuell von einem in Bearbeitung oder ungültigen Status auf abgerechnet geändert                                               | Der Geschäftsadministrator hat die Zahlung als abgerechnet markiert                                                                                                                                         |
| Ungültig\*                          | Bezahlt, aber nicht die erforderliche Anzahl an Bestätigungen innerhalb der im Geschäft festgelegten Zeit erhalten                              | Überprüfen Sie die Transaktion in einem Blockchain-Explorer, wenn sie ausreichende Bestätigungen erhalten hat, markieren Sie sie als abgerechnet                                                            |
| Ungültig (markiert)                 | Der Status wurde manuell von einem abgerechneten oder abgelaufenen Status auf ungültig geändert                                                 | Der Geschäftsadministrator hat die Zahlung als ungültig markiert                                                                                                                                            |
| Ungültig (überbezahlt)              | Mehr als der Rechnungsbetrag bezahlt, aber nicht die erforderliche Anzahl an Bestätigungen innerhalb der im Geschäft festgelegten Zeit erhalten | Überprüfen Sie die Transaktion in einem Blockchain-Explorer, wenn sie ausreichende Bestätigungen erhalten hat, markieren Sie sie als abgerechnet                                                            |

#### Rechnungsdetails

Die Seite mit den Rechnungsdetails enthält alle Informationen, die mit einer Rechnung zusammenhängen.

Rechnungsinformationen werden automatisch basierend auf dem Rechnungsstatus, Wechselkurs usw. erstellt. Produktinformationen werden automatisch erstellt, wenn die Rechnung mit Produktinformationen erstellt wurde, wie z.B. in der Point of Sale-App.

#### Rechnungsfilterung

Rechnungen können über die Schnellfilter neben dem Suchbutton oder die erweiterten Filter gefiltert werden, die durch Klicken auf den (Hilfe)-Link oben umgeschaltet werden können. Benutzer können Rechnungen nach Geschäft, Bestell-ID, Artikel-ID, Status oder Datum filtern.

#### Rechnungsexport

BTCPay Server-Rechnungen können im CSV- oder JSON-Format exportiert werden. Für weitere Informationen zum Rechnungsexport und zur Buchhaltung.

#### Eine Rechnung erstatten

Wenn Sie aus irgendeinem Grund eine Rückerstattung ausstellen möchten, können Sie einfach eine Rückerstattung aus der Rechnungsansicht erstellen.

#### Archivierung von Rechnungen

Aufgrund der Funktion "Keine Wiederverwendung von Adressen" des BTCPay Servers ist es üblich, viele abgelaufene Rechnungen auf der Rechnungsseite Ihres Geschäfts zu sehen. Um sie aus Ihrer Ansicht auszublenden, wählen Sie sie in der Liste aus und markieren Sie sie als archiviert. Archivierte Rechnungen werden nicht gelöscht. Zahlungen an eine archivierte Rechnung werden weiterhin von Ihrem BTCPay Server erkannt (Status bezahltSpät). Sie können die archivierten Rechnungen des Geschäfts jederzeit einsehen, indem Sie archivierte Rechnungen aus dem Suchfilter-Dropdown auswählen.

#### Standardwährung

Standardwährung des Geschäfts, diese wurde im Erstellungsassistenten des Geschäfts festgelegt

#### Jedem erlauben, eine Rechnung zu erstellen

Sie sollten diese Option aktivieren, wenn Sie der Außenwelt erlauben möchten, Rechnungen in Ihrem Geschäft zu erstellen. Diese Option ist nur nützlich, wenn Sie den Zahlungsbutton verwenden oder wenn Sie Rechnungen über API oder eine Drittanbieter-HTML-Website ausstellen. Die PoS-App ist vorautorisiert und benötigt dies nicht, damit ein zufälliger Besucher Ihren PoS-Store öffnen und eine Rechnung erstellen kann.

#### Zusätzliche Gebühr (Netzwerkgebühr) zur Rechnung hinzufügen

- Nur wenn der Kunde mehr als eine Zahlung für die Rechnung leistet
- Bei jeder Zahlung
- Niemals Netzwerkgebühr hinzufügen

#### Die Rechnung verfällt, wenn der Gesamtbetrag nicht nach .. Minuten bezahlt wurde.

Der Rechnungstimer ist standardmäßig auf 15 Minuten eingestellt. Der Timer ist ein Schutzmechanismus gegen die Volatilität, da er den Kryptowährungsbetrag gemäß den Krypto-zu-Fiat-Kursen sperrt. Wenn der Kunde die Rechnung nicht innerhalb des festgelegten Zeitraums bezahlt, gilt die Rechnung als abgelaufen. Die Rechnung gilt als "bezahlt", sobald die Transaktion auf der Blockchain sichtbar ist (0-Bestätigungen), aber als "abgeschlossen", wenn sie die vom Händler festgelegte Anzahl an Bestätigungen erreicht hat (üblicherweise 1-6). Der Timer ist anpassbar.

#### Betrachten Sie die Rechnung als bezahlt, auch wenn der bezahlte Betrag ..% weniger als erwartet ist.

In einer Situation, in der ein Kunde ein Exchange-Wallet verwendet, um direkt für eine Rechnung zu bezahlen, nimmt die Börse eine kleine Gebühr. Das bedeutet, dass eine solche Rechnung nicht als vollständig abgeschlossen gilt. Die Rechnung erhält den Status "teilweise bezahlt". Wenn ein Händler unterbezahlte Rechnungen akzeptieren möchte, können Sie hier den Prozentsatz festlegen.

### Anfragen

Zahlungsanfragen sind eine Funktion, die es BTCPay-Shopbesitzern ermöglicht, langfristige Rechnungen zu erstellen. Zahlungen an eine Zahlungsanfrage erfolgen zum Wechselkurs zum Zeitpunkt der Zahlung. Dies ermöglicht es Benutzern, Zahlungen nach ihrem Belieben zu tätigen, ohne Wechselkurse zum Zeitpunkt der Zahlung mit dem Shopbesitzer aushandeln oder überprüfen zu müssen.

Benutzer können Anfragen in Teilzahlungen bezahlen. Die Zahlungsanfrage bleibt gültig, bis sie vollständig bezahlt ist oder wenn der Shopbesitzer eine Ablaufzeit verlangt. Adressen werden niemals wiederverwendet. Bei jedem Klick auf Bezahlen wird eine neue Adresse generiert, um eine Rechnung für die Zahlungsanfrage zu erstellen.

Shopbesitzer können Zahlungsanfragen ausdrucken (oder Rechnungsdaten exportieren) zur Buchführung und Rechnungslegung. BTCPay kennzeichnet Rechnungen automatisch als Zahlungsanfragen in der Rechnungsliste Ihres Shops.

#### Passen Sie Ihre Zahlungsanfragen an

- Rechnungsbetrag - Festgelegten Zahlungsbetrag einstellen
- Nominale - Angeforderten Betrag in Fiat oder Kryptowährung anzeigen
- Zahlungsmenge - Nur Einzelzahlungen oder Teilzahlungen zulassen
- Ablaufzeit - Zahlungen bis zu einem Datum oder ohne Ablaufdatum zulassen
- Beschreibung - Texteditor, Datentabellen, Fotos & Videos einbetten
- Erscheinungsbild - Farbe und Stil mit CSS-Themen

![image](assets/en/93.webp)

#### Erstellen Sie eine Zahlungsanfrage

Gehen Sie im linken Menü zu Zahlungsanfrage und klicken Sie auf "Zahlungsanfrage erstellen".

![image](assets/en/94.webp)

Geben Sie den Anfragenamen, Betrag, Anzeige-Nominale, zugehörigen Shop, Ablaufzeit & Beschreibung (Optional) an

Wählen Sie die Option, dem Zahlenden zu erlauben, Rechnungen in ihrer Nominale zu erstellen, wenn Sie Teilzahlungen zulassen möchten.

Klicken Sie auf Speichern & Ansehen, um Ihre Zahlungsanfrage zu überprüfen.

BTCPay erstellt eine URL für die Zahlungsanfrage. Teilen Sie diese URL, um Ihre Zahlungsanfrage anzusehen. Benötigen Sie mehrere der gleichen Anfrage? Sie können Zahlungsanfragen mit der Klonoption im Hauptmenü duplizieren.

![image](assets/en/95.webp)

**WARNUNG**

Zahlungsanfragen sind shopabhängig, was bedeutet, dass jede Zahlungsanfrage bei der Erstellung einem Shop zugeordnet ist. Stellen Sie sicher, dass Sie ein Wallet mit Ihrem Shop verbunden haben, zu dem die Zahlungsanfrage gehört.

#### Bezahlt Anfrage

Der Zahlende und der Anfragende können den Status der Zahlungsanfrage nach dem Senden der Zahlung einsehen. Der Status wird als Abgerechnet angezeigt, wenn die Zahlung vollständig eingegangen ist. Wenn nur Teilzahlungen geleistet wurden, zeigt der Fällige Betrag den ausstehenden Saldo an.

![image](assets/en/96.webp)

#### Zahlungsanfragen anpassen

Der Beschreibungsinhalt kann mit dem Texteditor der Zahlungsanfrage bearbeitet werden. Beide Optionen sind verfügbar, wenn Sie zusätzliche Farbthemen oder benutzerdefinierte CSS-Stilisierung verwenden möchten.
Nicht-technische Benutzer können ein [Bootstrap-Theme](https://docs.btcpayserver.org/Development/Theme/#2-bootstrap-themes) verwenden. Weitere Anpassungen können durch das Bereitstellen zusätzlichen CSS-Codes erfolgen, wie unten gezeigt.

```css
:root {
  --btcpay-font-family-base: "Source Sans Pro", -apple-system,
    BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --btcpay-primary: #7d4698;
  --btcpay-primary-accent: #59316b;
  --btcpay-body-text: #333a41;
  --btcpay-body-bg: #fff;
  --btcpay-bg-tile: #f8f9fa;
}

#mainNav {
  color: white;
  background: linear-gradient(#59316b, #331840);
}

#mainNav .btn-link {
  color: white;
}
```

### Pull-Zahlungen

Traditionell teilt ein Empfänger seine Bitcoin-Adresse mit, um eine Bitcoin-Zahlung zu tätigen, und der Sender sendet später Geld an diese Adresse. Ein solches System wird als Push-Zahlung bezeichnet, da der Sender die Zahlung initiiert, während der Empfänger möglicherweise nicht verfügbar ist, und die Zahlung an den Empfänger "pusht".

Aber was ist mit der Umkehrung der Rolle?

Was ist, wenn statt eines Senders, der die Zahlung "pusht", der Sender dem Empfänger erlaubt, die Zahlung zu einem Zeitpunkt seiner Wahl zu "pullen"? Das ist das Konzept einer Pull-Zahlung. Dies ermöglicht mehrere neue Anwendungen, wie zum Beispiel:

- Ein Abonnementdienst (wo der Abonnent dem Dienst erlaubt, regelmäßig Geld zu "pullen")
- Rückerstattungen (wo der Händler dem Kunden erlaubt, das Rückerstattungsgeld in sein Wallet zu "pullen", wann immer es ihm passt)
- Zeitbasierte Abrechnung für Freiberufler (wo der Auftraggeber dem Freiberufler erlaubt, Geld in sein Wallet zu "pullen", sobald die Zeit erfasst wird)
- Mäzenatentum (wo der Mäzen dem Empfänger erlaubt, jeden Monat Geld zu "pullen", um ihre Arbeit weiter zu unterstützen)
- Automatischer Verkauf (wo ein Kunde einer Börse dieser erlaubt, jeden Monat automatisch Geld aus seinem Wallet zu "pullen" und zu verkaufen)
- Auszahlungssystem (wo ein Dienst mit hohem Volumen es Benutzern ermöglicht, Auszahlungen von ihrem Guthaben anzufordern, kann der Dienst dann leicht alle Auszahlungen an viele Benutzer in festen Intervallen bündeln)

### Auszahlungen

Die Auszahlungsfunktionalität ist in die [Pull-Zahlungen](https://docs.btcpayserver.org/PullPayments/) integriert. Diese Funktion ermöglicht es Ihnen, Auszahlungen innerhalb Ihres BTCPay zu erstellen. Diese Funktion ermöglicht es Ihnen, Pull-Zahlungen zu verarbeiten (Rückerstattungen, Gehaltsauszahlungen oder Abhebungen).

#### Beispiel 1: Rückerstattung

Beginnen wir mit dem Beispiel einer Rückerstattung. Der Kunde hat einen Artikel in Ihrem Geschäft gekauft, muss diesen aber leider zurückgeben. Er möchte eine Rückerstattung. Innerhalb von BTCPay können Sie eine [Rückerstattung](https://docs.btcpayserver.org/Refund/) erstellen und dem Kunden den Link zur Verfügung stellen, um seine Mittel zu beanspruchen. Sobald der Kunde seine Adresse angegeben und die Mittel beansprucht hat, wird dies in den Auszahlungen angezeigt.

Der erste Status, den es hat, ist Wartet auf Genehmigung. Ladenangestellte können überprüfen, ob mehrere ausstehend sind, und nach der Auswahl verwenden Sie die Schaltfläche Aktionen.

Optionen auf der Aktions-Schaltfläche

- Ausgewählte Auszahlungen genehmigen
- Ausgewählte Auszahlungen genehmigen & senden
- Ausgewählte Auszahlungen stornieren

Der nächste Schritt ist, die ausgewählten Auszahlungen zu genehmigen & zu senden, da wir den Kunden erstatten möchten. Überprüfen Sie die Adresse des Kunden, zeigt den Betrag an und ob wir möchten, dass Gebühren von der Rückerstattung abgezogen werden oder nicht. Sobald Sie die Überprüfungen durchgeführt haben, bleibt nur noch die Transaktion zu signieren.
Der Kunde wird jetzt auf der Seite "Ansprüche geltend machen" aktualisiert. Er kann der Transaktion folgen, da ihm ein Link zu einem Block Explorer und seiner Transaktion zur Verfügung gestellt wird. Sobald die Transaktion bestätigt wurde und der Status auf Abgeschlossen wechselt.

#### Beispiel 2: Gehalt

Nun kommen wir zur Gehaltsauszahlung, da diese intern im Geschäft und nicht auf Anfrage des Kunden gesteuert wird. Der zugrunde liegende Mechanismus ist derselbe; es werden Pull-Zahlungen verwendet. Aber anstatt eine Rückerstattung zu erstellen, werden wir eine [Pull-Zahlung](https://docs.btcpayserver.org/PullPayments/) vornehmen.

Gehen Sie zum Tab Pull-Zahlungen in Ihrem BTCPay-Server. Klicken Sie oben rechts auf den Button Pull-Zahlung erstellen.

Jetzt sind wir bei der Erstellung der Auszahlung, geben Sie ihr einen Namen und den gewünschten Betrag in der gewünschten Währung an, füllen Sie die Beschreibung aus, damit der Mitarbeiter weiß, worum es geht. Der nächste Teil ähnelt den Rückerstattungen. Der Mitarbeiter gibt die Zieladresse und den Betrag an, den er von dieser Auszahlung beanspruchen möchte. Er könnte sich entscheiden, dies in 2 separate Ansprüche aufzuteilen, an verschiedene Adressen oder sogar teilweise über Lightning zu beanspruchen.

Wenn mehrere ausstehende Auszahlungen vorhanden sind, können Sie diese zu einem Batch zusammenfassen, der signiert und versendet wird. Einmal signiert, wechseln die Auszahlungen zum Tab In Bearbeitung und zeigen die Transaktion an. Wenn sie vom Netzwerk akzeptiert wird, wechselt die Auszahlung zum Tab Abgeschlossen. Der Tab Abgeschlossen dient rein historischen Zwecken. Er enthält die verarbeiteten Auszahlungen und die dazugehörige Transaktion.

### Pull-Zahlungen

#### Konzept

Wenn ein Sender eine Pull-Zahlung konfiguriert, kann er eine Reihe von Eigenschaften festlegen:

- Name der Pull-Anfrage
- Ein Limitbetrag
- Eine Einheit (wie BTC, SAT, USD)
- Zahlungsmethoden
  - BTC On-Chain
  - BTC Off-Chain
- Beschreibung
- Benutzerdefiniertes CSS
- Enddatum (optional für Lightning Network BOLT11)

Danach kann der Sender die Pull-Zahlung mit einem Link mit dem Empfänger teilen, der es dem Empfänger ermöglicht, eine Auszahlung zu erstellen. Der Empfänger wird seine Auszahlung wählen:

- Welche Zahlungsmethode zu verwenden ist
- Wohin das Geld gesendet werden soll

Sobald eine Auszahlung erstellt wurde, wird sie auf das Limit der Pull-Zahlung für den aktuellen Zeitraum angerechnet. Der Sender wird dann die Auszahlung genehmigen, indem er den Kurs festlegt, zu dem die Auszahlung gesendet wird, und mit der Zahlung fortfährt.

Für den Sender bieten wir eine benutzerfreundliche Möglichkeit, die Zahlung mehrerer Auszahlungen aus dem [BTCPay Internen Wallet](https://docs.btcpayserver.org/Wallet/) zu bündeln.

#### Greenfield API

BTCPay Server bietet sowohl dem Sender als auch dem Empfänger eine vollständige API, die auf der `/docs`-Seite Ihrer Instanz dokumentiert ist. (oder auf der Dokumentationswebsite https://docs.btcpayserver.org)

Da unsere API die vollständigen Möglichkeiten von Pull-Zahlungen freilegt, kann ein Sender Zahlungen nach seinen eigenen Bedürfnissen automatisieren.

### Fähigkeitszusammenfassung

In diesem Abschnitt haben Sie Folgendes gelernt:

- Tiefgreifendes Verständnis der Rechnungsstatus von BTCPay Server sowie der Aktionen, die darauf ausgeführt werden können
- Anpassen und Verwalten von erweiterten Rechnungsmechanismen, bekannt als Anfragen.
- Die zusätzlichen flexiblen Zahlungsmöglichkeiten, die durch die einzigartige Pull-Zahlungsfunktion von BTCPay Server eröffnet werden, insbesondere wie man Rückerstattungen und Gehaltszahlungen handhabt.

### Wissensbewertung

#### KA Konzeptuelle Überprüfung

Was sind einige Unterschiede zwischen Rechnungen und Zahlungsanforderungen, und was könnte ein guter Grund sein, letztere zu verwenden?

#### KA Konzeptuelle Überprüfung

Wie erweitern Pull-Zahlungen das, was typischerweise On-Chain gemacht werden kann? Beschreiben Sie einige Anwendungsfälle, die sie ermöglichen.

## BTCPay Server Standard-Plugins

<chapterId>7d673dc4-bd5d-5411-819b-f135f1d86636</chapterId>

### Standard-Plugins und Apps

Der BTCPay-Server wird mit einem Standardset von Plugins (Apps) geliefert, die den BTCPay-Server zu einem E-Commerce-Zahlungsgateway machen können. Mit den Zusätzen eines Point of Sale, einer Crowdfunding-Plattform und einem einfachen Bezahlen-Knopf wird der BTCPay-Server zu einer leicht zu implementierenden Lösung.

### Point Of Sale

Eines der Standard-Plugins des BTCPay-Servers ist der Point of Sale (PoS). Mit dem PoS-Plugin kann ein Ladenbesitzer direkt vom BTCPay-Server aus einen Webshop erstellen, ohne dass er Drittanbieter-E-Commerce-Lösungen benötigt, um einen Webshop zu betreiben. Die webbasierte PoS-App ermöglicht es Benutzern mit physischen Geschäften, Bitcoin ohne Gebühren oder Dritte direkt in ihre Wallet zu akzeptieren. Der PoS kann leicht auf Tablets oder anderen Geräten, die das Surfen im Internet unterstützen, angezeigt werden. Benutzer können leicht eine Verknüpfung zum Startbildschirm erstellen, um schnell auf die Web-App zuzugreifen.

#### Wie man einen neuen Point of Sale erstellt

BTCPay-Server ermöglicht es Ladenbesitzern, schnell einen Point of Sale in mehreren Layouts zu erstellen. BTCPay-Server erkennt, dass nicht jeder Laden E-Commerce ist und nicht jeder Laden eine Bar oder ein Restaurant ist, und es kommt mit mehreren Standard-Setups für Ihren PoS.

Wenn der Ladenbesitzer in seiner linken Menüleiste auf "Point of Sale" klickt, wird BTCPay-Server nun nach einem Namen fragen; dieser Name wird in der linken Menüleiste sichtbar sein. Klicken Sie auf Erstellen, um den PoS zu erstellen.

![image](assets/en/97.webp)

#### Neu erstellten Point of Sale aktualisieren

Nachdem ein neuer PoS erstellt wurde, wird der folgende Bildschirm dazu dienen, Ihren Point of Sale zu aktualisieren und Artikel für Ihren Laden hinzuzufügen.

##### App-Name

Der hier Ihrem Point of Sale gegebene Name wird im Hauptmenü des BTCPay-Servers sichtbar sein.

##### Anzeigetitel

Die Öffentlichkeit wird den öffentlichen Titel oder Namen sehen, wenn sie Ihren Laden besucht. BTCPay-Server benennt Ihren Laden standardmäßig als „Teeladen“. Ersetzen Sie dies durch den Namen Ihres Ladens.

![image](assets/en/98.webp)

#### Point Of Sale-Stil wählen

BTCPay-Server kann seinen Point Of Sale auf mehrere Arten anzeigen.

- Produktliste
  - Eine Shopansicht, in der Kunden jeweils nur 1 Produkt kaufen können.
- Produktliste mit Warenkorb.
  - Eine Shopansicht, in der Kunden mehrere Artikel gleichzeitig kaufen können und eine Warenkorbübersicht rechts auf ihrem Bildschirm erhalten.
- Nur Tastenfeld
  - Keine Produktliste, nur ein Tastenfeld für direkte Rechnungsstellung.
- Druckanzeige (Druckbare Produktliste mit QR)
  - Wenn Sie Ihre Produktliste nicht immer digital anzeigen können, benötigen Sie eine "Offline"-Lösung für Produkte; BTCPay-Server verfügt über eine Druckanzeige, die als Offline-Laden fungiert.

![image](assets/en/99.webp)

#### Point Of Sale-Stil - Produktliste

![image](assets/en/100.webp)

#### Point Of Sale-Stil - Produktliste + Warenkorb

![image](assets/en/101.webp)

#### Point Of Sale-Stil - Nur Tastenfeld

![image](assets/en/102.webp)

#### Point Of Sale-Stil - Druckanzeige

![image](assets/en/103.webp)

#### Währung

Der Ladenbesitzer kann eine andere Währung für seinen Point of Sale festlegen als seine insgesamt festgelegte Standardwährung. Die Standardwährung des Ladens wird dieses Feld automatisch ausfüllen.

#### Beschreibung

Erzählen Sie der Welt von Ihrem Laden; was verkaufen Sie und zu welchem Preis? Alles, was Ihren Laden erklärt, gehört hierher.

#### Produkte

Wenn ein Point of Sale erstellt wird, fügt ein standardmäßiger BTCPay Server einige Artikel zum Shop als Referenz hinzu. Klicken Sie auf den Bearbeiten-Button bei einem der Standardartikel, um jede mögliche Option für einen Artikel besser zu verstehen.

Das Erstellen eines neuen Produkts in Ihrem Geschäft besteht aus den folgenden Feldern:

- Titel
- Preis (fest, minimal oder benutzerdefiniert)
- Bild-URL
- Beschreibung
- Lagerbestand
- ID
- Text des Kaufbuttons
- Aktivieren/Deaktivieren

Sobald der Ladenbesitzer alle Felder für das neue Produkt ausgefüllt hat, klicken Sie auf speichern, und Sie werden bemerken, dass der Produktbereich im Point of Sale nun gefüllt wird. Stellen Sie immer sicher, dass Sie oben rechts auf Ihrem Bildschirm speichern, um zu verhindern, dass Ladenbesitzer ihren Fortschritt beim Hinzufügen von Produkten verlieren.

Ladenbesitzer können auch den "Raw Editor" verwenden, um ihre Produkte zu konfigurieren. Der Raw Editor erfordert ein grundlegendes Verständnis von JSON-Strukturen.

#### Kasse

BTCPay Server ermöglicht eine kleine, PoS-spezifische Anpassung des Checkouts. Der Ladenbesitzer kann den Text "Kaufen für x" festlegen oder spezifische Kundendaten anfordern, indem er Formulare hinzufügt.

#### Trinkgelder

Nicht alle Geschäfte benötigen die Option für Trinkgelder bei ihren Verkäufen. Ladenbesitzer können dies nach Bedarf für ihren Laden aktivieren oder deaktivieren. Wenn das Geschäft Trinkgelder aktiviert hat, kann der Ladenbesitzer den Text im Feld für Trinkgelder nach Belieben festlegen. BTCPay Server Trinkgelder basieren auf einem prozentualen Betrag. Ladenbesitzer können mehrere Prozentsätze mit Kommatrennung hinzufügen.

#### Rabatte

Als Ladenbesitzer möchten Sie dem Kunden möglicherweise einen individuellen Rabatt an der Kasse gewähren; der Schalter für Rabatte wird an der Kasse Ihres Geschäfts verfügbar. Dies wird jedoch bei Selbstbedienungssystemen sehr abgeraten.

#### Benutzerdefinierte Zahlungen

Wenn die Option für benutzerdefinierte Zahlungen aktiviert ist, kann der Kunde seinen festgelegten Preis eingeben, der gleich oder höher als die ursprüngliche vom Laden generierte Rechnung ist.

#### Zusätzliche Optionen

Nachdem alles für Ihren Point of Sale eingestellt wurde, bleiben einige zusätzliche Optionen übrig. Ladenbesitzer können ihren PoS leicht durch ein Iframe einbetten oder einen Zahlungsbutton einbetten, der zu einem bestimmten Ladenartikel verlinkt. Um den gerade erstellten PoS-Laden zu gestalten, können Besitzer am Ende der zusätzlichen Optionen benutzerdefiniertes CSS hinzufügen.

#### Diese App löschen

Wenn der Ladenbesitzer den Point of Sale vollständig von seinem BTCPay Server löschen möchte, können Ladenbesitzer am Ende der Aktualisierung des PoS auf den Button "Diese App löschen" klicken, um ihre PoS-App vollständig zu zerstören. Beim Klicken auf "Diese App löschen" wird BTCPay Server um Bestätigung bitten, indem `DELETE` eingegeben und durch Klicken auf den Löschen-Button bestätigt wird. Nach dem Löschen kehrt der Ladenbesitzer zum BTCPay Server Dashboard zurück.

### BTCPay Server - Crowdfunding

Neben dem Point of Sale-Plugin bietet BTCPay Server die Möglichkeit, ein Crowdfunding zu erstellen. Wie bei jeder anderen Crowdfunding-Plattform können Ladenbesitzer ein Ziel festlegen, Belohnungen für Beiträge erstellen und es nach ihren Bedürfnissen anpassen.

#### Ein neues Crowdfunding einrichten

Klicken Sie im Hauptmenü Ihres BTCPay Servers links auf das Crowdfunding-Plugin, unter dem Abschnitt Plugin. BTCPay Server wird nun einen Namen für das Crowdfunding anfordern; dieser Name wird auch in der linken Menüleiste angezeigt.

#### Neu erstellten Point of Sale aktualisieren

Sobald der App ein Name gegeben wurde, wird der nächste Bildschirm sein, die App zu aktualisieren, um ihr Kontext zu geben.

#### App-Name

Der Ihrer Crowdfunding-Kampagne gegebene Name wird im Hauptmenü des BTCPay Servers sichtbar sein.

#### Anzeigetitel

Der Titel wird dem Crowdfunding für die Öffentlichkeit gegeben.

#### Slogan

Geben Sie dem Crowdfunding einen Einzeiler, um zu erkennen, worum es bei der Spendenaktion geht.

![Bild](assets/en/107.webp)

#### URL des Hauptbildes

Jedes Crowdfunding hat sein Hauptbild, das eine Banner, das man direkt erkennt. Dieses Bild kann auf Ihrem Server gespeichert werden, wenn Sie administrative Rechte haben, Admins können es unter den BTCPay Server-Einstellungen - Dateien hochladen. Wenn Sie ein Geschäftsinhaber sind, muss das Bild über einen Drittanbieter-Host ins Web hochgeladen werden (zum Beispiel imgur).

#### Crowdfunding öffentlich machen

Dieser Schalter macht Ihr Crowdfunding öffentlich und somit für die Außenwelt sichtbar. Zu Testzwecken oder um zu sehen, ob Ihr Thema korrekt angewendet wird, möchte man dies möglicherweise auf AUS setzen für die Zeit des Aufbaus des Crowdfundings.

#### Beschreibung

Erzählen Sie der Welt von Ihrem Crowdfunding, wofür sammeln Sie Geld? Alles, was Ihr Crowdfunding erklärt, kommt hierher.

![Bild](assets/en/108.webp)

#### Crowdfunding-Ziel

Setzen Sie ein Ziel für das, was die Spendenaktion für das Projekt verdienen soll und in welcher Währung das Ziel angegeben sein soll. Stellen Sie sicher, dass, wenn Ihre Ziele zwischen Daten festgelegt sind, diese Ziel- und Enddaten unter Ziele im Crowdfunding einbeziehen.

![Bild](assets/en/109.webp)

#### Vorteile

Vorteile helfen sehr bei Ihrem Crowdfunding. Dies liegt daran, dass Vorteile den Menschen eine Möglichkeit geben, an Ihrer Kampagne teilzunehmen. Sie sprechen sowohl egoistische als auch wohlwollende Motivationen an. Und sie ermöglichen Ihnen Zugang zu den Ausgaben Ihrer Unterstützer, nicht nur zu ihrem philanthropischen Geldbeutel – Sie können erraten, welches bedeutender ist.

Das Erstellen eines neuen Vorteils besteht aus den folgenden Feldern;

- Titel
- Preis (fest, minimal oder benutzerdefiniert)
- Bild-URL
- Beschreibung
- Inventar
- ID
- Text des Kaufbuttons
- Aktivieren/Deaktivieren

Sobald der Geschäftsinhaber alle Felder des neuen Vorteils ausgefüllt hat, klicken Sie auf speichern, und Sie werden bemerken, dass der Abschnitt Vorteile im Crowdfunding nun befüllt wird.

![Bild](assets/en/110.webp)

### BTCPay Server - Point Of Sale

#### Beiträge

Geschäftsinhaber können wählen, wie Vorteile angezeigt werden, wie sie sortiert oder sogar gegenüber anderen Vorteilen eingestuft werden. Sobald jedoch die Ziele des Crowdfundings erreicht sind, möchten Geschäftsinhaber möglicherweise verhindern, dass Spenden weiterhin zu dieser Spendenaktion fließen. Daher kann er umschalten auf "Keine zusätzlichen Beiträge nach Erreichen des Ziels zulassen". Dies wird verhindern, dass das Crowdfunding Spenden annimmt.

##### Verhalten des Crowdfundings

Standardmäßig zählt das Crowdfunding nur Rechnungen, die mit dem Crowdfunding erstellt wurden, zum Ziel. Es kann jedoch Fälle geben, in denen der Geschäftsinhaber möchte, dass alle in diesem Geschäft erstellten Rechnungen zum Crowdfunding zählen.

#### Zusätzliche Optionen zur Anpassung

BTCPay Server bietet einige zusätzliche Anpassungen. Fügen Sie Töne, Animationen oder sogar Diskussionsthreads zum Crowdfunding hinzu. Geschäftsinhaber können auch das Aussehen und Gefühl des Crowdfundings ändern, indem sie ihre eigene benutzerdefinierte CSS eingeben.

#### Diese App löschen

Wenn der Geschäftsinhaber sein Crowdfunding vollständig von seinem BTCPay Server löschen möchte, kann er am Ende der Aktualisierung des Crowdfunding-Geschäfts auf den Button „Diese App löschen“ klicken, um seine Crowdfunding-App vollständig zu zerstören. Beim Klicken auf „Diese App löschen“ wird BTCPay Server um Bestätigung bitten, indem `LÖSCHEN` eingegeben und durch Klicken auf den Lösch-Button bestätigt wird. Nach dem Löschen kehrt der Geschäftsinhaber zum BTCPay Server-Dashboard zurück.

### BTCPay Server - Zahlungsknopf

Leicht einbettbare HTML- und hochgradig anpassbare Zahlungsbuttons ermöglichen es Ladenbesitzern, Trinkgelder und Spenden zu erhalten. In der linken Menüleiste des BTCPay Servers, unterhalb des Abschnitts Plugins, können Ladenbesitzer auf den „Pay Button“ klicken und auf Aktivieren klicken, um einen Zahlungsbutton zu erstellen.

#### Allgemeine Einstellungen

Innerhalb der allgemeinen Einstellungen für den Zahlungsbutton können Ladenbesitzer festlegen

- Standardpreis
- Standardwährung
- Standardzahlungsmethode
  - Standard des Ladens verwenden
  - BTC on-chain
  - BTC Off-chain (Lightning)
  - BTC Off-chain (LNURL-pay)
- Beschreibung des Checkouts
- Bestell-ID

#### Anzeigeoptionen

Der Pay-Button des BTCPay Servers kann konfiguriert werden, um verschiedenen Stilen zu entsprechen. Buttons können einen festen oder benutzerdefinierten Betrag haben, entweder angezeigt mit einem Schieberegler oder Plus- und Minus-Umschaltern.

#### Modal verwenden

Beim Erstellen des Zahlungsbuttons können Ladenbesitzer sein Verhalten wählen, wenn ein Kunde darauf klickt, und es in einem Modal oder als neue Seite anzeigen.

**!?Hinweis!?**

Warnung: Der Zahlungsbutton sollte nur für Trinkgelder und Spenden verwendet werden

Die Verwendung des Zahlungsbuttons für E-Commerce-Integrationen wird nicht empfohlen, da bestellrelevante Informationen vom Benutzer geändert werden können. Für E-Commerce sollten Sie unsere Greenfield-API verwenden. Wenn dieser Laden kommerzielle Transaktionen abwickelt, raten wir Ihnen, einen separaten Laden zu erstellen, bevor Sie den Zahlungsbutton verwenden.

#### Zahlungsbutton-Text anpassen

Standardmäßig zeigt der Zahlungsbutton des BTCPay Servers "Mit BTCPay bezahlen" an. Ladenbesitzer können diesen Text nach Belieben festlegen und das BTCPay Server-Logo durch ihr eigenes ersetzen. Stellen Sie den Text ein, indem Sie den "Pay Button Text" verwenden und die Bild-URL unterhalb der "Pay Button Image URL" einfügen.

##### Bildgröße

Die Größe des Bildes im Button kann nur auf drei Standardwerte eingestellt werden.

- 146x40px
- 168x46px
- 209x57px

#### Button-Typ

Der BTCPay Server kennt drei Zustände für den Zahlungsbutton.

- Fester Betrag
  - Der zuvor festgelegte Preis befindet sich in den allgemeinen Einstellungen des Buttons.
- Benutzerdefinierter Betrag
  - Der Pay-Button des BTCPay Servers hat + und - Umschalter, um einen benutzerdefinierten Preis festzulegen.
  - Bei Verwendung des benutzerdefinierten Betrags wird der BTCPay Server ein Min, Max und wie allmählich es steigen soll, anfordern.
  - Buttons können auf „Einfachen Eingabestil verwenden“ eingestellt werden. Dies entfernt die +/- Umschalter.
  - Button inline einpassen, wo Button und Umschalter inline erscheinen.
- Schieberegler
  - Ähnlich wie der benutzerdefinierte Betrag, jedoch visuell anders, da er einen Schieberegler anstelle der +/- Umschalter hat.
  - Bei Verwendung des Schiebereglers wird der BTCPay Server ein Min, Max und wie allmählich es steigen soll, anfordern.

**!?Hinweis!?**

Das Löschen des Zahlungsbuttons kann oben in der Warnbeschreibung erfolgen.

#### Zahlungsbenachrichtigungen

Server IPN (Instant Payment Notification) ist für Webhooks gedacht und kann mit einer URL gefüllt werden, um Kaufdaten zu posten.

#### E-Mail-Benachrichtigungen

Immer wenn eine Zahlung erfolgt ist, kann der BTCPay Server den Ladenbesitzer benachrichtigen.

#### Browser-Weiterleitung

Wenn der Kunde den Kauf abschließt, wird er zu diesem Link weitergeleitet, wenn er vom Ladenbesitzer festgelegt wurde.

#### Erweiterte Optionen für den Zahlungsbutton

Geben Sie zusätzliche Query-String-Parameter an, die der Checkout-Seite hinzugefügt werden sollen, sobald die Rechnung erstellt ist. Zum Beispiel würde `lang=da-DK` die Checkout-Seite standardmäßig auf Dänisch laden.

#### App als Endpunkt verwenden

Verlinken Sie den Zahlungsbutton direkt mit einem Artikel in einer der PoS- oder Crowdfunding-Apps zuvor.
Ladenbesitzer können das Dropdown-Menü anklicken und ihre gewünschte App auswählen; sobald die App ausgewählt ist, kann der Ladenbesitzer den Artikel hinzufügen, der verlinkt werden muss.

#### Generierter Code

Da der Zahlungsbutton des BTCPay Servers leicht in HTML einbettbar ist, zeigt der BTCPay Server den generierten Code zum Kopieren in eine Webseite unten an, nachdem der Zahlungsbutton konfiguriert wurde.

Ladenbesitzer können den generierten Code in ihre Webseite kopieren, und der Zahlungsbutton vom BTCPay Server ist direkt auf ihrer Webseite aktiv.

#### Zahlungsbenachrichtigungen

Server IPN (Instant Payment Notification) ist für Webhooks gedacht und kann mit einer URL gefüllt werden, um Kaufdaten zu posten.

#### E-Mail-Benachrichtigungen

Immer wenn eine Zahlung erfolgt ist, kann der BTCPay Server den Ladenbesitzer benachrichtigen.

#### Browser-Weiterleitung

Wenn der Kunde den Kauf abschließt, wird er zu diesem Link weitergeleitet, wenn er vom Ladenbesitzer festgelegt wurde.

#### Erweiterte Optionen für den Zahlungsbutton

Geben Sie zusätzliche Query-String-Parameter an, die der Checkout-Seite hinzugefügt werden sollen, sobald die Rechnung erstellt ist. Zum Beispiel würde `lang=da-DK` die Checkout-Seite standardmäßig auf Dänisch laden.

#### App als Endpunkt verwenden

Verlinken Sie den Zahlungsbutton direkt mit einem Artikel in einer der PoS- oder Crowdfund-Apps zuvor. Ladenbesitzer können das Dropdown-Menü anklicken und ihre gewünschte App auswählen, sobald die App ausgewählt ist, kann der Ladenbesitzer den Artikel hinzufügen, der verlinkt werden muss.

#### Generierter Code

Da der Zahlungsbutton des BTCPay Servers leicht in HTML einbettbar ist, zeigt der BTCPay Server den generierten Code zum Kopieren in eine Webseite unten an, nachdem der Zahlungsbutton konfiguriert wurde. Ladenbesitzer können den generierten Code in ihre Webseite kopieren und der Zahlungsbutton vom BTCPay Server ist direkt auf ihrer Webseite aktiv.

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie gelernt:

- Wie man das integrierte PoS-Plugin des BTCPay Servers verwendet, um einfach einen individuellen Laden zu erstellen
- Wie man das integrierte Crowdfund-Plugin des BTCPay Servers verwendet, um einfach eine individuelle Crowdfund-App zu erstellen
- Generierung eines Codes für einen individuellen Zahlungsbutton mit dem Pay Button-Plugin

### Wissensbewertung

#### KA-Überprüfung

Was sind die drei integrierten Plugins, die standardmäßig mit dem BTCPay Server geliefert werden? Beschreiben Sie in wenigen Worten, wie jedes verwendet werden kann.

# BTCPay Server konfigurieren

<partId>ff38596c-7de3-5e5c-ba50-9b9edbbbb5eb</partId>

## Grundlegendes Verständnis der Installation von BTCPay Server in einer LunaNode-Umgebung

<chapterId>d0a28514-ffcf-529b-9156-29141f0b060a</chapterId>

### BTCPay Server auf gehostetem Env. (LunaNode) installieren

Diese Schritte bieten alle notwendigen Informationen, um mit der Nutzung von BTCPay Server auf LunaNode zu beginnen. Es gibt viele Optionen, wie die Software bereitgestellt werden kann.
Alle Details zum BTCPay Server finden Sie unter https://docs.btcpayserver.org.

#### Wo fangen wir an?

In diesem Teil werden Sie sich mit LunaNode als Hosting-Anbieter vertraut machen, die ersten Schritte zur Nutzung Ihres BTCPay Servers kennenlernen und erfahren, wie Sie mit dem Lightning Network vorgehen. Nachdem wir alle Schritte durchgegangen sind, können Sie einen Webshop oder eine Crowdfund-Plattform betreiben, die Bitcoin akzeptiert!

Dies ist einer von vielen Wegen, den BTCPay Server bereitzustellen. Lesen Sie unsere Dokumentation für weitere Details,

https://docs.btcpayserver.org.

### BTCPay Server - LunaNode-Bereitstellung

#### LunaNode-Bereitstellung

Zuerst gehen Sie auf die Website von LunaNode.com, wo wir ein neues Konto erstellen werden. Klicken Sie oben rechts auf "Sign Up" oder verwenden Sie den "Get Started"-Assistenten auf ihrer Homepage.
![image](assets/en/111.webp)

Nachdem Sie Ihr neues Konto erstellt haben, sendet LunaNode eine Verifizierungs-E-Mail. Sobald Sie das Konto verifiziert haben, im Vergleich zu Voltage, werden Sie sofort dazu aufgefordert, Ihr Kontoguthaben aufzuladen. Dieses Guthaben wird benötigt, um für den Serverplatz und die Hosting-Kosten zu bezahlen.

![image](assets/en/112.webp)

#### Fügen Sie Ihrem LunaNode-Konto Guthaben hinzu

Sobald Sie auf "Deposit credit" geklickt haben, können Sie festlegen, wie viel Sie Ihrem Konto hinzufügen möchten und wie Sie dafür bezahlen möchten. LunaNode und BTCPay Server kosten zwischen 10$USD und 20$USD pro Monat.
Im Vergleich zu Voltage.cloud erhalten Sie vollen Zugriff auf Ihren Virtual Private Server (VPS von nun an) und haben daher etwas mehr Kontrolle über Ihren Server. Nachdem Sie Ihr neues Konto erstellt haben, sendet LunaNode eine Verifizierungs-E-Mail.
Sobald Sie das Konto verifiziert haben, im Vergleich zu Voltage, werden Sie jetzt sofort dazu aufgefordert, Ihr Kontoguthaben aufzuladen. Dieses Guthaben wird benötigt, um für den Serverplatz und die Hosting-Kosten zu bezahlen.

#### Wie deployt man einen neuen Server?

In diesem Leitfaden werden wir den Setup-Prozess durchlaufen, indem wir einen Satz von API-Schlüsseln erstellen und den BTCPay Server Launcher von LunaNode verwenden.

In Ihrem LunaNode-Dashboard klicken Sie oben rechts auf API. Dies öffnet eine neue Seite. Wir müssen nur einen Namen für den API-Schlüssel festlegen. Der Rest wird von LunaNode übernommen und wird in diesem Leitfaden nicht behandelt. Klicken Sie auf den Button "Create API Credential".
Nachdem Sie die API-Zugangsdaten erstellt haben, erhalten Sie eine lange Zeichenkette aus Buchstaben und Zeichen. Dies ist Ihr API-Schlüssel.

![image](assets/en/113.webp)

#### Wie deployt man einen neuen Server?

Es gibt 2 Teile dieser Zugangsdaten, API-Schlüssel und API-ID; wir benötigen beide. Bevor wir zum nächsten Schritt übergehen, öffnen wir ein zweites Tab im Browser und gehen zu https://launchbtcpay.lunanode.com/

Hier werden Sie aufgefordert, Ihren API-Schlüssel und Ihre API-ID anzugeben. Dies dient dazu zu überprüfen, ob Sie es sind, der diesen neuen Server bereitstellt. Der API-Schlüssel sollte noch im vorherigen Tab geöffnet sein; wenn Sie in der Tabelle unten scrollen, finden Sie die API-ID.

Gehen Sie zurück zur Seite mit dem Launcher, füllen Sie die Felder mit Ihrem API-Schlüssel und Ihrer ID aus und klicken Sie auf Weiter.

![image](assets/en/114.webp)

Im nächsten Schritt können Sie einen Domainnamen angeben. Wenn Sie bereits eine Domain besitzen und diese für BTCPay Server verwenden möchten, stellen Sie sicher, dass Sie auch den DNS-Eintrag (genannt `A`-Eintrag) auf Ihrer Domain hinzufügen. Wenn Sie keine Domain besitzen, verwenden Sie stattdessen die von LunaNode bereitgestellte Domain (Sie können dies später in den BTCPay Server-Einstellungen ändern) und klicken Sie auf Weiter.

Lesen Sie mehr darüber, wie Sie einen DNS-Eintrag für BTCPay Server einrichten oder ändern; https://docs.btcpayserver.org/FAQ/Deployment/#how-to-change-your-btcpay-server-domain-name

#### Starten Sie BTCPay Server auf LunaNode

Nachdem wir die vorherigen Schritte durchgeführt haben, können wir alle Optionen für unseren neuen Server festlegen. Hier werden wir Bitcoin (BTC) als unsere unterstützte Währung auswählen; wir können eine E-Mail festlegen, um über die Erneuerung von Verschlüsselungszertifikaten informiert zu werden; dies ist nicht zwingend erforderlich.
Diese Anleitung zielt darauf ab, eine Mainnet-Umgebung einzurichten (reales Bitcoin); jedoch erlaubt LunaNode Ihnen auch, dies auf Testnet oder Regtest für Entwicklungsziele einzustellen. Wir werden für diese Anleitung die Mainnet-Option beibehalten.
Wählen Sie Ihre Lightning-Implementierung. LunaNode bietet zwei verschiedene Implementierungen, LND und Core Lightning. Für diese Anleitung werden wir LND wählen. Es gibt kleine, aber wahre Unterschiede zwischen beiden Implementierungen; für mehr dazu empfehlen wir, die umfangreiche Dokumentation zu lesen; https://docs.btcpayserver.org/LightningNetwork#getting-started-with-btcpay-server-and-core-lightning-cln

![Bild](assets/en/115.webp)

LunaNode bietet mehrere Virtual Machine (VM)-Pläne an. Diese unterscheiden sich in Preisbereichen und Spezifikationen des Servers. Für diese Anleitung wird ein m2-Plan ausreichen; jedoch, wenn Sie mehr als nur Bitcoin als Währung angekreuzt haben, sollten Sie mindestens einen m4 in Betracht ziehen.

Beschleunigen Sie die anfängliche Blockchain-Synchronisation; dies ist optional und hängt von Ihren Bedürfnissen ab. Es gibt fortgeschrittene Optionen wie das Setzen eines Lightning-Alias, das Verweisen auf eine spezifische GitHub-Veröffentlichung oder das Setzen von SSH-Schlüsseln; keine davon wird in dieser Anleitung behandelt.

Nachdem Sie das Formular ausgefüllt haben, müssen Sie auf VM starten klicken, und Lunanode wird beginnen, Ihre neue VM zu erstellen, einschließlich BTCPay Server darauf installiert. Dieser Prozess dauert ein paar Minuten; sobald Ihr Server bereit ist, gibt Ihnen LunaNode den Link zu Ihrem neuen BTCPay Server.

Nach dem Erstellungsprozess klicken Sie auf den Link zu Ihrem BTCPay Server; hier werden Sie gebeten, ein Administrator-Konto zu erstellen.

![Bild](assets/en/116.webp)

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie gelernt:

- Ein Konto bei LunaNode erstellen und aufladen
- Den BTCPay Server Launcher verwenden, um Ihren eigenen Server zu erstellen

### Wissensbewertung

#### KA Konzeptuelle Überprüfung

Beschreiben Sie einige der Unterschiede zwischen dem Betrieb einer Instanz von BTCPay Server auf einem VPS und dem Erstellen eines Kontos auf einer gehosteten Instanz.

## BTCPay Server auf einer Voltage-Umgebung installieren

<chapterId>11c7d284-b4d2-5542-872c-df9bd9c1491b</chapterId>

Sie werden mit Voltage.cloud als Hosting-Anbieter vertraut gemacht, erfahren über die ersten Schritte der Nutzung Ihres BTCPay Servers und lernen, wie man mit dem Lightning Network umgeht. Nachdem wir alle Schritte durchgegangen sind, können Sie einen Webshop oder eine Crowdfunding-Plattform betreiben, die Bitcoin akzeptiert!

Dies ist einer von vielen Wegen, um BTCPay Server zu deployen. Lesen Sie unsere Dokumentation für mehr Details,
https://docs.btcpayserver.org.

### BTCPay Server - Voltage.cloud Deployment

Gehen Sie zunächst auf die Website Voltage.cloud und melden Sie sich für ein neues Konto an. Bei der Erstellung eines Kontos können Sie sich für eine 7-tägige kostenlose Testversion anmelden. Klicken Sie entweder oben rechts auf "Anmelden" oder verwenden Sie die Option "Kostenlose 7-Tage-Testversion ausprobieren" auf ihrer Homepage.

![Bild](assets/en/117.webp)

Nachdem Sie ein Konto erstellt haben, klicken Sie auf den Button `NODES` in Ihrem Dashboard. Sobald wir Nodes ausgewählt und einen neuen Node erstellt haben, werden uns die möglichen Nodes präsentiert, die Voltage anbietet. Da dieser Leitfaden auch das LightningNetwork behandelt, müssen wir bei Voltage zuerst unsere Lightning-Implementierung wählen, bevor wir einen BTCPay Server erstellen. Klicken Sie auf LightningNode.

![Bild](assets/en/118.webp)
Hier müssen Sie auswählen, welche Art von Lightning-Node Sie möchten. Voltage bietet eine Vielzahl von Optionen für Ihre Beleuchtungseinrichtung. Dies unterscheidet sich von der Bereitstellung mit beispielsweise LunaNode. Für die Zwecke dieses Leitfadens reicht ein Lite Node aus. Lesen Sie mehr über die Unterschiede auf Voltage.cloud.
![image](assets/en/119.webp)

Geben Sie Ihrem Node einen Namen, setzen Sie ein Passwort und sichern Sie dieses Passwort. Wenn dieses Passwort verloren geht, verlieren Sie den Zugang zu Ihren Backups, und Voltage kann es nicht wiederherstellen. Erstellen Sie den Node, und Voltage zeigt Ihnen den Fortschritt. Voltage hat Ihren Lightning-Node erstellt. Wir können jetzt die BTCPay Server-Instanz erstellen und direkt auf das Lightning-Netzwerk zugreifen.

Klicken Sie in der oberen linken Ecke Ihres Dashboards auf Nodes. Hier können Sie den nächsten Teil Ihrer BTCPay Server-Instanz einrichten. Klicken Sie auf "neu erstellen", sobald Sie sich in der Node-Übersicht befinden. Sie erhalten einen ähnlichen Bildschirm wie zuvor. Jetzt wählen wir statt Lightning Node den BTCPay Server.

Voltage zeigt Ihnen die Geolokation Ihres BTCPay Servers, Voltage hostet in der US-West-Region. Hier sehen Sie auch die Kosten für das Hosting des Servers. Klicken Sie auf Erstellen und geben Sie Ihrem BTCPay Server einen Namen. Aktivieren Sie Lightning und Voltage zeigt Ihnen den im vorherigen Schritt erstellten Lightning-Node. Klicken Sie auf Erstellen, und Voltage wird eine BTCPay Server-Instanz erstellen.

![image](assets/en/120.webp)

Nachdem Sie auf Erstellen geklickt haben, präsentiert Ihnen Voltage den Standardbenutzernamen und das Passwort. Diese ähneln Ihrem zuvor in Voltage festgelegten Passwort. Klicken Sie auf den Button Login to Account, um zu Ihrem BTCPay Server weitergeleitet zu werden.

Willkommen bei Ihrer neuen BTCPay Server-Instanz. Da wir Lightning bereits im Erstellungsprozess eingerichtet haben, zeigt es Ihnen, dass Lightning bereits aktiviert ist!

### Fähigkeiten-Zusammenfassung

In diesem Kapitel haben Sie gelernt:

- Ein Konto auf Voltage.cloud zu erstellen
- Schritte, um BTCPay Server zusammen mit einem Lightning-Node auf dem Konto zum Laufen zu bringen

### Wissensbewertung

#### KA Konzeptuelle Überprüfung

Was sind einige Schlüsselunterschiede zwischen den Voltage- und LunaNode-Einrichtungen?

## BTCPay Server auf einem Umbrel-Node installieren

<chapterId>3298e292-6476-5fe0-836c-7fa021348799</chapterId>

Am Ende dieser Schritte können Sie Lightning-Zahlungen in Ihrem BTCPay-Store in Ihrem lokalen Netzwerk akzeptieren. Dieser Prozess gilt auch, wenn Sie einen Umbrel-Node in einem Restaurant oder Geschäft betreiben. Wenn Sie diesen Store mit einer öffentlichen Website verbinden möchten, folgen Sie der fortgeschrittenen Übung, um Ihren Umbrel-Node öffentlich zugänglich zu machen.

https://umbrel.com/

![image](assets/en/121.webp)

### BTCPay Server - Umbrel-Bereitstellung

Nachdem Ihr Umbrel-Node vollständig mit der Bitcoin-Blockchain synchronisiert wurde, gehen Sie zum Umbrel App Store und suchen Sie unter Apps nach BTCPay Server.

![image](assets/en/122.webp)

Klicken Sie auf BTCPay Server, um die App-Details zu sehen. Wenn die Details für BTCPay Server geöffnet sind, zeigt die untere rechte Ecke die Anforderungen für den ordnungsgemäßen Betrieb der App. Es zeigt, dass Bitcoin und Lightning-Node erforderlich sind. Wenn Sie den Lightning-Node auf Ihrem Umbrel noch nicht installiert haben, klicken Sie auf Installieren. Dieser Prozess kann einige Minuten dauern.

![image](assets/en/123.webp)

Nachdem Sie Ihren Lightning-Node installiert haben:

1. Klicken Sie in den App-Details oder auf der App im Umbrels-Dashboard auf Öffnen.
2. Klicken Sie auf einen neuen Node einrichten; Ihnen werden 24 Wörter für die Wiederherstellung Ihres Lightning-Nodes angezeigt.
3. Schreiben Sie diese auf.

![image](assets/en/124.webp)
Umbrel wird nach einer Verifizierung der gerade notierten Wörter fragen. Nachdem der Lightning-Node eingerichtet ist, kehren Sie zum Umbrel App Store zurück und suchen nach BTCPay Server. Klicken Sie auf den Installationsbutton, und Umbrel wird anzeigen, ob die erforderlichen Komponenten installiert sind und dass BTCPay Server Zugriff auf diese Komponenten benötigt. Nach der Installation klicken Sie oben rechts in den App-Details auf Öffnen oder öffnen Sie BTCPay Server über Ihr Umbrel-Dashboard.
Umbrel wird nach einer Verifizierung der gerade notierten Wörter fragen.

![Bild](assets/en/125.webp)

**!?Hinweis!?**

Stellen Sie sicher, dass Sie diese an einem geeigneten Ort aufbewahren, wie zuvor beim Speichern von Schlüsseln gelernt.

Nachdem der Lightning-Node eingerichtet ist, kehren Sie zum Umbrel App Store zurück und suchen nach BTCPay Server. Klicken Sie auf den Installationsbutton, und Umbrel wird anzeigen, ob die erforderlichen Komponenten installiert sind und dass BTCPay Server Zugriff auf diese Komponenten benötigt.

![Bild](assets/en/126.webp)

Nach der Installation klicken Sie oben rechts in den App-Details auf Öffnen oder öffnen Sie BTCPay Server über Ihr Umbrel-Dashboard.

![Bild](assets/en/127.webp)

### Fähigkeiten-Zusammenfassung

In diesem Abschnitt haben Sie gelernt:

- Schritte zur Installation von BTCPay Server mit Lightning-Funktionalität auf einem Umbrel-Node

### Wissensbewertung

#### KA Konzeptuelle Überprüfung

Wie unterscheidet sich die Einrichtung auf Umbrel von den vorherigen zwei gehosteten Optionen?

# Schlussfolgerung

<partId>d72e6fa5-0870-5f00-9143-9466ed22e2bd</partId>



## Bewerten Sie den Kurs
<chapterId>d90bb93d-b894-551e-9fd6-6855c739a904</chapterId>
<isCourseReview>true</isCourseReview>

## Kursabschluss

<chapterId>c07ac2a5-f97e-5c57-8a80-4955b48128d4</chapterId>

![Bild](assets/en/128.webp)

Sie sollten auch ein allgemeines Verständnis davon haben, was Bitcoin ist, wie es funktioniert und wie es mit zweiten Schichten wie dem Lightning-Netzwerk skalieren kann. In diesem Kurs haben wir ausführlich behandelt, wie jeder BTCPay Server nutzen kann, von der ersten Installation bis zur Erstellung von Geschäften und komplexem Rechnungsmanagement, um ein finanziell souveränes Individuum oder Händler zu werden.

Herzlichen Glückwunsch zum Abschluss dieses Kurses. Wir hoffen, dass Ihnen der Inhalt gefallen hat und Sie weiterhin BTCPay Server nutzen und erkunden werden und genauso gespannt auf die vielversprechende Zukunft sind, die Bitcoin und die wachsende Gemeinschaft von Entwicklern und Teilnehmern bringen wird, wie wir es sind.

> **FOSS ist unausweichlich.**

### Glossar

| Begriff                                        | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 51%-Angriff                                    | Die Handlung, absichtlich eine neue längste Kette von Blöcken zu erstellen, um Blöcke in der Blockchain zu ersetzen. Dies ermöglicht es Ihnen, Transaktionen, die in die Blockchain eingemint wurden, zu ersetzen. Diese Art von Angriff ist am einfachsten durchzuführen, wenn Sie die Mehrheit der Mining-Power haben, weshalb es als „Mehrheitsangriff“ oder „51%-Angriff“ bezeichnet wird.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| AccountKey                                     | Der Account-Schlüssel zum Rebasen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| AccountKeyPath                                 | Der Pfad vom Root zum Account-Schlüssel, der durch den Fingerabdruck des Master-Public-Key eingeleitet wird.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Adresse                                        | Bitcoin-Adressen kodieren kompakt die Informationen, die notwendig sind, um einen Empfänger zu bezahlen. Eine moderne Adresse besteht aus einer Reihe von Buchstaben und Zahlen, die mit bc1 beginnt und wie bc1qw508d6qejxtdg4y5r3zarvary0c5xw7kv8f3t4 aussieht. Eine Adresse ist eine Kurzform für das Sperrskript eines Empfängers, das von einem Sender verwendet werden kann, um Gelder an den Empfänger zu übertragen. Die meisten Adressen repräsentieren entweder den öffentlichen Schlüssel des Empfängers oder eine Form von Skript, das komplexere Ausgabebedingungen definiert. Das vorangehende Beispiel ist eine bech32-Adresse, die ein Zeugnisprogramm kodiert, das Gelder an den Hash eines öffentlichen Schlüssels sperrt (Siehe Pay-to-Witness-Public-Key-Hash). Es gibt auch ältere Adressformate, die mit 1 oder 3 beginnen und die Base58Check-Adresskodierung verwenden, um Hashes öffentlicher Schlüssel oder Skripthashes darzustellen.                           |
| Adresstyp                                      | Eine Adresse kann verschiedene Skripte repräsentieren. Adressen werden kodiert und mit einem Präfix versehen, um ihren Skripttyp zu übermitteln. Legacy-Adressen verwenden Base58, und wenn eine Legacy-Adresse der Hash eines öffentlichen Schlüssels ist, eine sogenannte P2PKH-Adresse, beginnt sie mit einer „1“. Weniger häufig ist eine Legacy-Adresse ein Hash eines Skripts, in diesem Fall beginnt sie mit einer „3“. Derzeit sind alle SegWit-Adressen in Bech32 kodiert und beginnen mit dem Präfix „bc1“.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| App                                            | BTCPay Server verfügt über Plugins, die als eigenständige Anwendung funktionieren können.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| BIP 329                                        | Export/Import von Wallet-Labels                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| BIP49                                          | Definiert das Ableitungsschema für HD-Wallets unter Verwendung des P2WPKH-nested-in-P2SH (BIP 141) Serialisierungsformats für Segregated Witness-Transaktionen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Bitcoin-Adresse                                | Alphanumerische Zeichenfolge, an die Sie Ihr Bitcoin senden, sodass es nun dort „lebt“. Ist ein Identifikator, der aus einer Zeichenfolge von etwa 33 Buchstaben und Zahlen besteht. In der aktuellen Protokollversion beginnt eine Adresse mit 1, 3 oder b. Das Vorhandensein der Adresse eines Empfängers ist ein notwendiger Teil, um eine Bitcoin-Transaktion zu initiieren. Bitcoin-Adressen werden aus öffentlichen Schlüsseln generiert, und aus einem Satz öffentlicher Schlüssel können mehrere Adressen generiert werden, um die Privatsphäre zu verbessern. Bitcoin-Adressen funktionieren genau wie E-Mail-Adressen, wenn Sie eine Nachricht senden möchten, müssen Sie wissen, wohin sie geht, dasselbe gilt für Bitcoin. Bevor Sie eine Bitcoin-Transaktion senden, müssen Sie sicherstellen, dass die Adresse des Empfängers korrekt ist, da Bitcoin-Transaktionen irreversibel sind und Sie möglicherweise Bitcoin an eine Adresse senden, die nicht dem Empfänger gehört. |
| bitcoin versus Bitcoin                         | Bitcoin ist das monetäre Netzwerk, und bitcoin (kleingeschrieben) ist eine Geldeinheit im Bitcoin-Netzwerk. Sie verwenden die Bitcoin-Währung oder ein Token, um auf einem Bitcoin-Netzwerk zu transagieren.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Block                                          | Ein Block ist eine Datenstruktur in der Bitcoin-Blockchain, die aus einem Header und einem Körper von Bitcoin-Transaktionen besteht. Der Block ist mit einem Zeitstempel markiert und bekennt sich zu einem spezifischen Vorgängerblock (Elternblock). Wenn der Blockheader gehasht wird, liefert er den Proof of Work, der die Blockchain probabilistisch unveränderlich macht. Blöcke müssen den Regeln folgen, die durch den Netzwerkkonsens durchgesetzt werden, um die Blockchain zu erweitern. Wenn ein Block an die Blockchain angehängt wird, gelten die enthaltenen Transaktionen als ihre erste Bestätigung.                                                                                                                                                                                                                                                                                                                                                                     |
| Block Explorer                                 | Ein Online-Tool, das es Ihnen ermöglicht, nach Echtzeit- und historischen Informationen über eine Blockchain zu suchen, einschließlich Daten zu Blöcken, Transaktionen, Adressen und mehr.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Block Hash                                     | Ein Block Hash ist der SHA-256 Hash der Blockdaten und wird normalerweise im hexadezimalen Format dargestellt. Ein Block Hash kann als eine sehr große Zahl interpretiert werden. Um die Anforderungen des Proof-of-Work zu erfüllen, muss ein Block Hash unterhalb einer bestimmten Schwelle liegen. Daher beginnen alle Block Hashes mit einer Reihe von Nullen, gefolgt von einer alphanumerischen Zeichenkette. Einige Blöcke haben bis zu zwanzig führende Nullen, während frühere Blöcke so wenige wie acht haben. Die Anzahl der erforderlichen Nullen zeigt ungefähr die Schwierigkeit des Minings zum Zeitpunkt der Veröffentlichung des Blocks an.                                                                                                                                                                                                                                                                                                                               |
| Block Height                                   | Jeder Block ist in aufsteigender Reihenfolge nummeriert, beginnend bei Null.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Block Reward                                   | Besteht aus der Blocksubvention (neu erstellte Bitcoin) und der Summe aller Transaktionsgebühren aus in dem Block enthaltenen Transaktionen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Block Size                                     | Jeder Block hat eine begrenzte Menge an Daten, die er aufnehmen kann. Die Daten, die nicht in einen bestimmten Block passen, werden in einem der folgenden Blöcke aufgezeichnet. Bei Bitcoin-Blöcken war die Blockgröße ursprünglich auf 1 MB beschränkt, jedoch kann nach einem Soft Fork die Blockgröße technisch bis zu 4 MB an Daten aufnehmen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Block Subsidy                                  | Die Menge an neuen Bitcoin, die in jedem Block geprägt wird. Jeder produzierte und zur Blockchain hinzugefügte Block ermöglicht es dem Ersteller des Blocks, eine bestimmte Menge neuer Bitcoin zu prägen. Die Subvention begann bei 50 BTC pro Block und wird alle 210.000 Blöcke oder ungefähr alle 4 Jahre halbiert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Blockchain                                     | Ein verteiltes Protokoll oder eine Datenbank aller Bitcoin-Transaktionen. Transaktionen werden in diskreten Aktualisierungen, sogenannten Blöcken, gruppiert, die bis zu 4 Millionen Gewichtseinheiten begrenzt sind. Blöcke werden ungefähr alle 10 Minuten durch einen stochastischen Prozess namens Mining produziert. Jeder Block beinhaltet einen rechenintensiven "Proof of Work". Die Proof-of-Work-Anforderung wird verwendet, um die Blockintervalle zu regulieren und die Blockchain gegen Angriffe zum Umschreiben der Geschichte zu schützen: Ein Angreifer müsste bestehende Proof-of-Work-Arbeiten übertreffen, um bereits veröffentlichte Blöcke zu ersetzen, wodurch jeder Block probabilistisch unveränderlich wird, da er unter nachfolgenden Blöcken begraben ist.                                                                                                                                                                                                      |
| BTCPAY Server Vault                            | Für eine optimale Balance zwischen Benutzerfreundlichkeit, Sicherheit und Privatsphäre wird empfohlen, BTCPay Server Wallet mit einem Hardware-Wallet zu verwenden. BTCPay Vault ist darauf ausgelegt, die Brücke zwischen dem Hardware-Wallet und dem BTCPay Server zu schlagen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Byzantine Generals' Problem                    | Ein spieltheoretisches Problem, das die Schwierigkeit beschreibt, die dezentralisierte Parteien bei der Konsensfindung haben, ohne sich auf eine vertrauenswürdige zentrale Partei zu verlassen. Der Name stammt vom Szenario mehrerer Generäle, die Byzanz belagern. Sie haben die Stadt umzingelt, müssen aber gemeinsam entscheiden, wann sie angreifen. Wenn alle Generäle gleichzeitig angreifen, werden sie gewinnen, aber wenn sie zu unterschiedlichen Zeiten angreifen, werden sie verlieren. Die Generäle haben keine sicheren Kommunikationskanäle untereinander, da alle Nachrichten, die sie senden oder empfangen, möglicherweise von den Verteidigern Byzanz’ abgefangen oder trügerisch gesendet wurden. Wie können die Generäle sich organisieren, um gleichzeitig anzugreifen?                                                                                                                                                                                           |
| Censorship                                     | Kontrolle darüber, welche Informationen an die Massen übermittelt werden können. Wenn es um Bitcoin geht, bezieht sich Zensur auf die Fähigkeit, die Transaktion durch Dritte zu stoppen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Change                                         | Der Teil der UTXOs, der an das Wallet des Senders zurückgegeben wird, normalerweise über eine andere Adresse. Entspricht der Summe der Eingänge minus dem ausgegebenen Betrag und der Transaktionsgebühr.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Child Pays For Parent (CPFP)                   | Eine Gebührenerhöhungstechnik, bei der ein Benutzer einen Ausgang einer unbestätigten Transaktion mit niedriger Gebührenrate in einer Kindtransaktion mit einer hohen Gebührenrate ausgibt, um Miner zu ermutigen, beide Transaktionen in einem Block einzuschließen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Coinbase Transaction                           | Die allererste Transaktion in jedem Block, die die Blockbelohnung und die Transaktionsgebühren an denjenigen verteilt, der den Block gemined hat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Coincidence of Wants                           | Ein wirtschaftliches Phänomen, bei dem zwei Parteien jeweils einen Gegenstand besitzen, den die andere Partei möchte, sodass sie diese Gegenstände direkt ohne ein monetäres Medium austauschen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cold Storage                                   | Eine Methode zur Datenverwaltung ohne Verbindung zum Internet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Cold Wallet                                    | Eine Art von Bitcoin-Wallet, die Ihre privaten Schlüssel offline sicher speichert, in der Regel auf einem physischen Gerät. Auch bekannt als Hardware-Wallet, schützt es Ihr digitales Bitcoin vor Online-Hackern, indem es ein gerät ähnlich einem USB-Stick verwendet, das nicht mit dem Internet verbunden ist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Command Line Interface (CLI)                   | Interaktion mit einem Gerät oder Computerprogramm mit Befehlen von einem Benutzer oder Client und Antworten von dem Gerät oder Programm in Form von Textzeilen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Commitment Transaction                         | Eine Commitment-Transaktion ist eine Bitcoin-Transaktion, die von beiden Kanalpartnern signiert wird und den neuesten Saldo eines Kanals kodiert. Jedes Mal, wenn eine neue Zahlung getätigt oder über den Kanal weitergeleitet wird, wird der Kanalsaldo aktualisiert und eine neue Commitment-Transaktion wird von beiden Parteien signiert. Wichtig ist, dass sowohl Alice als auch Bob in einem Kanal zwischen ihnen ihre eigene Version der Commitment-Transaktion besitzen, die auch von der anderen Partei signiert ist. Zu jedem Zeitpunkt kann der Kanal von entweder Alice oder Bob geschlossen werden, indem sie ihre Commitment-Transaktion an die Bitcoin-Blockchain übermitteln. Das Einreichen einer älteren (veralteten) Commitment-Transaktion gilt im Lightning Network als Betrug (d.h. ein Protokollverstoß) und kann von der anderen Partei bestraft werden, indem sie alle Gelder im Kanal für sich beansprucht, über eine Straftransaktion.                         |
| Confirmation                                   | Sobald eine Transaktion in einem Block enthalten ist, hat sie eine Bestätigung. Sobald ein weiterer Block auf der Blockchain gemined wird, hat die Transaktion zwei Bestätigungen, und so weiter. Sechs oder mehr Bestätigungen gelten als ausreichender Beweis dafür, dass eine Transaktion nicht umgekehrt werden kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Crowdfund (CF)                                 | Ein Standard-Plugin des BTCPay Servers, das es einem Ladenbesitzer ermöglicht, einfach eine typische Crowdfunding-Website zu erstellen. Sie können leicht ein Ziel setzen, Belohnungen für Beiträge erstellen und es nach ihren Bedürfnissen anpassen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Cryptography                                   | Ein spezielles System, bei dem die ursprüngliche Nachricht so verändert wird, dass nur die beabsichtigten Empfänger sie erhalten können.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Dashboard                                      | Die zentrale Startseite des BTCPay Servers. Sie bietet einen Überblick über alle Aktivitäten eines Ladens, angezeigt über eine Reihe von Zusammenfassungskacheln.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Demo                                           | Bezieht sich auf die virtuelle Umgebung, in der Software-Demos stattfinden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Deployment                                     | Software-Deployment umfasst alle Aktivitäten, die ein Softwaresystem zur Nutzung verfügbar machen. Der allgemeine Deployment-Prozess besteht aus mehreren miteinander verbundenen Aktivitäten mit möglichen Übergängen zwischen ihnen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Ableitungspfad                                 | Ein Datenelement, das einem hierarchischen deterministischen (HD) Wallet mitteilt, wie ein spezifischer Schlüssel innerhalb eines Schlüsselbaums abgeleitet wird. Ableitungspfade werden als Bitcoin-Standard verwendet und wurden mit HD-Wallets als Teil von BIP 32 eingeführt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Schwierigkeitsanpassung                        | Anpassung des Schwierigkeitsziels, alle 2016 Blöcke (ungefähr zwei Wochen), um zu versuchen, sicherzustellen, dass Blöcke durchschnittlich einmal alle 10 Minuten abgebaut werden. Es schafft daher eine konsistente Zeit zwischen den Blöcken und eine konsistente Ausgabe neuer Bitcoins in das Netzwerk (über die Blockbelohnung).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Schwierigkeitsziel                             | Wird beim Mining verwendet, es ist eine Zahl, unter der ein Blockhash liegen muss, damit der Block zur Blockchain hinzugefügt werden kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Digitale Signatur                              | Eine digitale Signatur ist ein mathematisches Schema zur Überprüfung der Authentizität und Integrität digitaler Nachrichten oder Dokumente. Sie kann als kryptografisches Commitment angesehen werden, bei dem die Nachricht nicht verborgen ist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Teilbar                                        | Die Eigenschaft eines Gutes, das in kleinere Mengen ohne Wertverlust aufgeteilt werden kann. Da wirtschaftliche Transaktionen häufig in unterschiedlichen Mengen stattfinden, muss eine Währung teilbar sein, um in einer Wirtschaft weit verbreitet eingesetzt zu werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Docker                                         | Software, die Software in standardisierte Einheiten namens Container verpackt, die alles enthalten, was die Software zum Ausführen benötigt, einschließlich Bibliotheken, Systemtools, Code und Laufzeit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Doppelausgabe                                  | Das Ergebnis, erfolgreiches Geld mehr als einmal auszugeben. Bitcoin schützt vor Doppelausgaben, indem überprüft wird, ob jede zur Blockchain hinzugefügte Transaktion den Konsensregeln entspricht; dies bedeutet die Überprüfung, ob die Eingaben für die Transaktion nicht zuvor ausgegeben wurden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Haltbar                                        | Eigenschaft von Geld, bei der die Währung ihren ursprünglichen Zustand über die Zeit beibehalten und wiederholte Verwendung aushalten kann. Eine haltbare Währung muss in der Lage sein, potenziellen Schäden zu widerstehen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Electrum                                       | Electrum ist eines der beliebtesten Bitcoin-Wallets, erstellt im Jahr 2011.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Erweiterter öffentlicher Schlüssel (Xpub)      | Erweiterter öffentlicher Schlüssel, auch bekannt als Xpub, ein öffentlicher Schlüssel, der als Elternteil für Schlüssel fungiert, die vom Xpub als Funktion des HD Wallet abgeleitet werden. Dieser Xpub ist ein Standard, der in BIP 32 eingeführt wurde. Wallets verwenden ihn hinter den Kulissen, um öffentliche Schlüssel abzuleiten. Das Teilen des Xpub wird nicht abgeraten, Ihre Gelder sind nicht direkt gefährdet, bewegt zu werden, da der Xpub keine privaten Schlüssel ableiten kann. Der Vorteil des Teilens eines Xpub könnte für Crowdfunding-Zwecke im BTCPay Server sein. Der Xpub wird über Online-Mittel geteilt, während die privaten Schlüssel offline auf einem HWW bleiben.                                                                                                                                                                                                                                                                                       |
| F.U.D.                                         | Abkürzung für Fear, Uncertainty and Doubt (Angst, Unsicherheit und Zweifel); Wird normalerweise absichtlich hervorgerufen, um einen Konkurrenten in einen Nachteil zu versetzen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Gebühr                                         | Im Kontext des Lightning-Netzwerks werden Knoten Routinggebühren für die Weiterleitung von Zahlungen anderer Benutzer berechnen. Einzelne Knoten können ihre eigenen Gebührenrichtlinien festlegen, die als Summe einer festen Basisgebühr und einer Gebührenrate berechnet werden, die von der Zahlungsmenge abhängt. Im Kontext von Bitcoin zahlt der Sender einer Transaktion eine Transaktionsgebühr an die Miner für das Einbeziehen der Transaktion in einen Block. Bitcoin-Transaktionsgebühren enthalten keine Basisgebühr und hängen linear vom Gewicht der Transaktion ab, jedoch nicht von der Menge.                                                                                                                                                                                                                                                                                                                                                                           |
| Fiat                                           | Von der Regierung ausgegebene Währung, die nicht durch eine Ware wie Gold gedeckt ist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Finite                                         | Bezieht sich auf die begrenzte Menge von Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Fork                                           | Eine Änderung eines Protokolls oder eines Codes. Forks werden in der Regel eingeführt, um ein Projekt zu aktualisieren. In der Open-Source-Gemeinschaft existieren Forks, weil viele Personen die gleiche Software zu unterschiedlichen Zeiten herunterladen und ausführen und nicht immer aktualisieren. Wenn zwei Benutzer Version 1 einer Software herunterladen und ausführen und nur ein Benutzer aktualisiert, wenn Version 2 veröffentlicht wird, führt der Benutzer, der aktualisiert hat, einen Fork von Version 1 aus.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Funding Transaction                            | Transaktion, die verwendet wird, um einen Zahlungskanal zu eröffnen. Der Wert (in Bitcoin) der Funding-Transaktion entspricht genau der Kapazität des Zahlungskanals. Der Output der Funding-Transaktion ist ein 2-von-2-Multisignatur-Script (Multisig), bei dem jeder Kanalpartner einen Schlüssel kontrolliert. Aufgrund seiner Multisig-Natur kann er nur durch gegenseitige Zustimmung zwischen den Kanalpartnern ausgegeben werden. Er wird letztendlich durch eine der Commitment-Transaktionen oder durch die Abschlusstransaktion ausgegeben.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Fungible                                       | Sein etwas (wie Geld oder eine Ware), das derart beschaffen ist, dass ein Teil oder eine Menge durch einen anderen gleichen Teil oder Menge zum Begleichen einer Schuld oder zum Ausgleichen eines Kontos ersetzt werden kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Gap Limit                                      | Bezieht sich auf die Standardanzahl öffentlicher Adressen, die auf Transaktionen in der Blockchain überprüft werden, um den Kontostand eines Kontos zu berechnen. Transaktionen, die auf einer Adresse jenseits des Address Gap Limits eingehen, werden nicht erkannt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Genesis Block                                  | Erster Block in der Bitcoin-Blockchain. Satoshi Nakamoto, der Schöpfer von Bitcoin, hat den Genesis-Block am 3. Januar 2009 gemined und den Schlagzeilentitel des Financial Times von diesem Tag, „Chancellor on brink of second bailout for banks“, eingefügt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Github                                         | Eine Plattform und Cloud-basierter Dienst für Softwareentwicklung und Versionskontrolle mit Git, der es Entwicklern ermöglicht, ihren Code zu speichern und zu verwalten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Gossip Protocol                                | LN-Knoten senden und empfangen Informationen über die Topologie des Lightning-Netzwerks durch Gossip-Nachrichten, die mit ihren Peers ausgetauscht werden. Das Gossip-Protokoll ist hauptsächlich in BOLT #7 definiert und legt das Format der node_announcement-, channel_announcement- und channel_update-Nachrichten fest. Um Spam zu verhindern, werden Node-Ankündigungsnachrichten nur weitergeleitet, wenn der Knoten bereits einen Kanal hat, und Kanalankündigungsnachrichten werden nur weitergeleitet, wenn die Funding-Transaktion des Kanals vom Bitcoin-Netzwerk bestätigt wurde. Normalerweise verbinden sich Lightning-Knoten mit ihren Kanalpartnern, aber es ist auch in Ordnung, sich mit jedem anderen Lightning-Knoten zu verbinden, um Gossip-Nachrichten zu verarbeiten.                                                                                                                                                                                            |
| Gresham's Gesetz                               | Gesetz, das besagt, dass „schlechtes Geld gutes Geld verdrängt“. Mit anderen Worten, in einer Wirtschaft, in der zwei Währungen verwendet werden, werden die Menschen das schlechte Geld, das ständig an Wert verliert, ausgeben und das gute Geld, das seinen Wert behält, halten. So wird das schlechte Geld in Bezug auf Umlauf und Verwendung im täglichen Geschäftsverkehr dominieren, während gutes Geld in Bezug auf Ersparnisse und langfristige Investitionen dominieren wird.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Halving                                        | Ein Ereignis, das die Ausgaberate von Bitcoin alle 210.000 Blöcke (ungefähr alle vier Jahre) halbiert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Hard Fork                                      | Eine Konsensänderung, die nicht rückwärtskompatibel ist. Rückwärtsinkompatibilität tritt auf, wenn ein zuvor ungültiges Verhalten gültig gemacht wird. Um den Konsens über einen Hard Fork aufrechtzuerhalten, müssen alle Knoten aktualisiert werden. Andernfalls werden alte Knoten Transaktionen oder Blöcke nach den alten Regeln als ungültig ablehnen, während aktualisierte Knoten sie als gültig akzeptieren. Aus diesem Grund werden Hard Forks in Bitcoin um jeden Preis vermieden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Hardware Wallet (HWW)                          | Eine spezielle Art von Bitcoin-Wallet, die die privaten Schlüssel des Benutzers in einem sicheren Hardware-Gerät speichert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Hash-Funktion                                  | Eine kryptografische Hash-Funktion ist ein mathematischer Algorithmus, der Daten beliebiger Größe auf eine Bitfolge fester Größe (einen Hash) abbildet und als Einwegfunktion konzipiert ist, das heißt, eine Funktion, die praktisch nicht umkehrbar ist. Die einzige Möglichkeit, die Eingabedaten aus dem Ausgang einer idealen kryptografischen Hash-Funktion zu rekonstruieren, besteht darin, eine Brute-Force-Suche nach möglichen Eingaben durchzuführen, um zu sehen, ob sie eine Übereinstimmung erzeugen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Hash-Rate                                      | Ein Maß dafür, wie viele Hashes Miner pro Sekunde im Bitcoin-Netzwerk insgesamt produzieren. Ein einzelner Hash ist ein Versuch, einen Proof-of-Work für einen Block zu erstellen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Hot Wallet                                     | Ein Gerät mit externen Verbindungen, insbesondere zum Internet. Eine Hot Wallet ist eine Bitcoin-Wallet, die mit dem Internet verbunden ist. Diese Wallets sind für den täglichen Gebrauch bequemer, aber nicht so sicher wie Cold-Storage-Optionen, da sie mit dem Internet interagieren.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Initial Block Download (IBD)                   | Der Prozess des Aufbaus der vollständigen Bitcoin-Blockchain von Grund auf. Wenn ein neuer Knoten eingerichtet wird und dem Netzwerk beitritt, verbindet er sich mit anderen Knoten und fragt sie nach Blöcken. Der neue Knoten verarbeitet diese Blöcke und baut die Blockchain auf, bis er aufgeholt hat und mit dem Netzwerk synchron ist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Rechnung                                       | Ein kommerzielles Dokument, das von einem Verkäufer an einen Käufer im Zusammenhang mit einer Verkaufstransaktion ausgestellt wird und die Produkte, Mengen und vereinbarten Preise für Produkte oder Dienstleistungen angibt, die der Verkäufer dem Käufer zur Verfügung gestellt hat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Know Your Customer (KYC)                       | Gesetze, die verhindern sollen, dass Finanzinstitutionen für illegale Geldtransfers genutzt werden, indem gefordert wird, dass alle Finanzkonten Personen oder Organisationen zugeordnet werden können.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Layer 2                                        | Ein Netzwerk, das auf einer Blockchain aufgebaut ist, z.B. das Lightning Network.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Legacy-Adresse                                 | Legacy-Adressen verwenden Base58, und wenn eine Legacy-Adresse der Hash eines öffentlichen Schlüssels ist, eine sogenannte P2PKH-Adresse, beginnt sie mit einer ‘1’.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Lightning Network                              | Ein Protokoll auf Bitcoin. Es schafft ein Netzwerk von Zahlungskanälen, das die vertrauenslose Weiterleitung von Zahlungen durch das Netzwerk mit Hilfe von HTLCs und Onion Routing ermöglicht. Weitere Komponenten des Lightning Network sind das Gossip-Protokoll, die Transportschicht und Zahlungsanfragen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Liquidität                                     | Maß für mehrere Merkmale des Orderbuchs eines bestimmten Vermögenswerts innerhalb eines gegebenen Marktes. Liquidität ist ein Indikator dafür, wie stark sich eine große Order auf den Preis eines Vermögenswerts auswirken wird. Ein Vermögenswert mit mehr Liquidität hat eine tiefere Orderbuchtiefe. Das bedeutet, dass er mehr Orders mit kleineren Preisbewegungen absorbieren kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Längste Kette                                  | Die Kette von Blöcken, die den größten Aufwand zu ihrer Erstellung benötigte. Sie wird so genannt, weil intuitiv eine Blockchain mit mehr Blöcken mehr Energie zu ihrer Erstellung benötigt hat als eine Kette mit weniger Blöcken, aber genauer ist es die Kette, die mehr Arbeit zur Produktion erforderte, sodass ein besserer Name "schwerste Kette" gewesen wäre.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Hauptkette                                     | Im Kontext des Lightning-Netzwerks bezieht sich dies auf das Bitcoin-Netzwerk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Tauschmittel                                   | Eine Art von Gut, das den Austausch anderer Güter und Dienstleistungen innerhalb einer Wirtschaft erleichtert. Historisch wurden Gegenstände wie Muscheln, Perlen und Gold als Tauschmittel verwendet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Mempool                                        | Kurz für "Speicherpool", ist es eine temporäre Speicherung für Transaktionen, die von einem Knoten empfangen wurden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Miner                                          | Ein Knoten, der am Prozess des Aufbaus der Blockchain durch Hinzufügen neuer Blöcke mittels Hashing beteiligt ist.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Mining                                         | Prozess des Erstellens eines Blocks aus kürzlichen Bitcoin-Transaktionen und dann das Lösen eines Rechenproblems als Nachweis der Arbeit. Es ist der Prozess, durch den das gemeinsame Bitcoin-Hauptbuch (d.h. die Bitcoin-Blockchain) aktualisiert wird und durch den neue Transaktionen in das Hauptbuch aufgenommen werden. Es ist auch der Prozess, durch den neues Bitcoin ausgegeben wird. Jedes Mal, wenn ein neuer Block erstellt wird, erhält der Mining-Knoten neues Bitcoin, das innerhalb der Coinbase-Transaktion dieses Blocks erstellt wurde.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Multisignatur (multisig)                       | Ein Skript, das mehr als eine Unterschrift zur Autorisierung einer Ausgabe benötigt. Zahlungskanäle werden immer als Multisig-Adressen codiert, die eine Unterschrift von jedem Partner des Zahlungskanals erfordern. Im Standardfall eines Zahlungskanals zwischen zwei Parteien wird eine 2-von-2-Multisig-Adresse verwendet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Knoten                                         | Ein Computer, der an einem Netzwerk teilnimmt. Insbesondere die Bitcoin- oder Lightning-Netzwerke.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Ausgabe                                        | Paket von Bitcoins, das in einer Bitcoin-Transaktion erstellt wurde.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Ausgabesperre                                  | Eine Reihe von Anforderungen, die an eine Ausgabe gestellt werden. Diese Anforderungen müssen erfüllt sein, um die Ausgabe in einer Transaktion verwenden zu können. Das häufigste Beispiel ist die einfache Anforderung, den privaten Schlüssel zu besitzen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| P2SH-Adresse                                   | P2SH-Adressen sind Base58Check-Codierungen des 20-Byte-Hashs eines Skripts. P2SH-Adressen beginnen mit einer "3". P2SH-Adressen verbergen die gesamte Komplexität, sodass der Sender einer Zahlung das Skript nicht sieht.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| P2WPKH-Adresse                                 | Das "native SegWit v0" Adressformat, P2WPKH-Adressen sind bech32-codiert und beginnen mit "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| P2WSH-Adresse                                  | Das "native SegWit v0" Skript-Adressformat, P2WSH-Adressen sind bech32-codiert und beginnen mit "bc1q".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Teilweise signierte Bitcoin-Transaktion (PSBT) | Ein Bitcoin-Standard, der die Portabilität von nicht signierten Transaktionen erleichtert, was es mehreren Parteien ermöglicht, leicht die gleiche Transaktion zu signieren. Dies ist besonders nützlich, wenn mehrere Parteien Inputs zur gleichen Transaktion hinzufügen möchten. PSBT wurde durch BIP 174 eingeführt und ermöglicht es Benutzern, Transaktionen einfacher auf einem Cold-Storage-Gerät zu signieren und dann die signierte Transaktion von einem Gerät, das mit dem Internet verbunden ist, zu übertragen.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Wegfindung                                     | Der Prozess des Findens eines Weges für eine Zahlung von der Quelle zum Ziel im Lightning-Netzwerk.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Pay-to-Public-Key-Hash (P2PKH)                 | P2PKH ist ein Typ von Ausgabe, der Bitcoin an den Hash eines öffentlichen Schlüssels bindet. Eine durch ein P2PKH-Skript gesperrte Ausgabe kann entsperrt (ausgegeben) werden, indem der öffentliche Schlüssel, der zum Hash passt, und eine digitale Signatur, die vom entsprechenden privaten Schlüssel erstellt wurde, vorgelegt werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Pay-to-Script-Hash (P2SH)                      | P2SH ist ein vielseitiger Ausgabetyp, der die Verwendung komplexer Bitcoin-Skripte ermöglicht. Bei P2SH wird das komplexe Skript, das die Bedingungen für die Ausgabe der Mittel (Erlösungsskript) festlegt, nicht im Sperrskript präsentiert. Stattdessen wird der Wert an den Hash eines Skripts gebunden, das vorgelegt und erfüllt werden muss, um die Ausgabe auszugeben.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pay-to-Taproot (P2TR)                          | Aktiviert im November 2021, ist Taproot ein neuer Ausgabetyp, der Bitcoin an einen Baum von Ausgabebedingungen oder eine einzelne Wurzelbedingung bindet.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Pay-to-Witness-Public-Key-Hash (P2WPKH)        | P2WPKH ist das SegWit-Äquivalent von P2PKH, das einen separaten Zeugen verwendet. Die Signatur, um eine P2WPKH-Ausgabe auszugeben, wird im Zeugenbaum anstelle des ScriptSig-Feldes platziert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pay-to-Witness-Script-Hash (P2WSH)             | P2WSH ist das SegWit-Äquivalent von P2SH, das einen separaten Zeugen verwendet. Die Signatur und das Skript, um eine P2WSH-Ausgabe auszugeben, werden im Zeugenbaum anstelle des ScriptSig-Feldes platziert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Payjoin                                        | Eine spezielle Art von Bitcoin-Transaktion, bei der sowohl der Sender als auch der Empfänger Beiträge leisten, um die gemeinsame Besitzannahme zu brechen, eine Annahme, die verwendet wird, um die Privatsphäre von Bitcoin-Nutzern zu untergraben.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Zahlungskanal                                  | Eine finanzielle Beziehung zwischen zwei Knoten im Lightning-Netzwerk, die mit einer Bitcoin-Transaktion erstellt wird, die eine Multisignatur-Adresse bezahlt. Die Kanalpartner können den Kanal nutzen, um Bitcoin hin und her zu senden, ohne alle Transaktionen auf der Bitcoin-Blockchain festzuhalten. In einem typischen Zahlungskanal werden nur zwei Transaktionen, die Finanzierungstransaktion und die Verpflichtungstransaktion, zur Blockchain hinzugefügt. Zahlungen, die über den Kanal gesendet werden, werden nicht in der Blockchain aufgezeichnet und gelten als "off-chain" erfolgt.                                                                                                                                                                                                                                                                                                                                                                                   |
| Zahlungsanforderung                            | Eine Funktion, die es BTCPay-Shopbesitzern ermöglicht, langfristige Rechnungen zu erstellen. Mittel, die an eine Zahlungsanforderung gezahlt werden, verwenden den Wechselkurs zum Zeitpunkt der Zahlung. Dies ermöglicht es Benutzern, Zahlungen nach ihrem Belieben zu tätigen, ohne Wechselkurse mit dem Shopbesitzer zum Zeitpunkt der Zahlung aushandeln oder überprüfen zu müssen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Auszahlung                                     | Die Auszahlungsfunktionalität ist in Pull-Zahlungen integriert. Diese Funktion ermöglicht es Ihnen, Pull-Zahlungen (Rückerstattungen, Gehaltsauszahlungen oder Abhebungen) zu verarbeiten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Plugin                                         | Ein Software-Add-on, das auf einem Programm installiert wird, um dessen Fähigkeiten zu erweitern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Point Of Sale (PoS)                            | Ein Standard-Plugin von BTCPay Server, das es einem Shopbesitzer ermöglicht, direkt aus dem BTCPay Server einen Webshop zu erstellen. Der Shopbesitzer benötigt keine Drittanbieter-E-Commerce-Lösungen, um einen Webshop zu betreiben.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Portabel                                       | Die Fähigkeit eines Gutes, leicht über Räume hinweg transportiert zu werden. Portabilität ist ein wichtiges Merkmal von stabilem Geld; damit eine Währung weit verbreitet und somit nutzbar wird, muss sie relativ einfach über Grenzen, zwischen Individuen und über lange Distanzen bewegt werden können.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Proof Of Work (PoW)                            | Daten, die bedeutende Rechenleistung zur Ermittlung benötigen und von jedem leicht überprüft werden können, um den Umfang der Arbeit nachzuweisen, der für ihre Erstellung erforderlich war. Bei Bitcoin müssen Miner eine numerische Lösung für den SHA-256-Algorithmus finden, die ein netzwerkweites Ziel, das Schwierigkeitsziel, erfüllt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pseudonym                                      | Ein falscher Name, den Personen verwenden, um ihre Identität zu schützen oder einen Ruf unabhängig von ihrer echten Identität aufzubauen. Öffentliche Schlüssel werden verwendet, um Bitcoin-Nutzern zu ermöglichen, Bitcoin zu empfangen, während sie in Bezug auf die Blockchain pseudonym bleiben.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Public-Key Kryptografie                        | Involviert ein Paar von Schlüsseln, bekannt als öffentlicher Schlüssel und privater Schlüssel, die mit einer Entität verbunden sind, die ihre Identität elektronisch authentifizieren oder Daten signieren oder verschlüsseln muss. Der öffentliche Schlüssel wird veröffentlicht und der entsprechende private Schlüssel wird geheim gehalten. Daten, die mit dem öffentlichen Schlüssel verschlüsselt wurden, können nur mit dem entsprechenden privaten Schlüssel entschlüsselt werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Öffentlicher/Privater Schlüssel                | Schlüsselpaar, das in der Public-Key Kryptografie verwendet wird. Der öffentliche Schlüssel wird offen mit anderen geteilt und kann als Kontonummer betrachtet werden, während der private Schlüssel geheim gehalten wird und als Passwort angesehen werden kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Pull-Zahlung                                   | Traditionell teilt ein Empfänger bei einer Bitcoin-Zahlung seine Bitcoin-Adresse mit und der Sender sendet später Geld an diese Adresse. Ein solches System wird als Push-Zahlung bezeichnet, da der Sender die Zahlung initiiert, während der Empfänger möglicherweise nicht verfügbar ist, und somit die Zahlung an den Empfänger "pusht". Anstatt des typischen Szenarios, in dem ein Sender die Zahlung "pusht", erlaubt der Sender dem Empfänger, die Zahlung zu einem Zeitpunkt vorzunehmen, den der Empfänger für geeignet hält.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Kaninchenloch                                  | Eine Anspielung auf "Alice im Wunderland", wo die Heldin ein Abenteuer beginnt, indem sie in ein Kaninchenloch steigt. Innerhalb von Bitcoin bezieht es sich auf die scheinbar endlosen Themen, die man erforscht und in einem neuen Licht sieht, sobald man begonnen hat, Bitcoin zu verstehen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Empfangen                                      | Der Prozess, Bitcoin an eine bereitgestellte Adresse gesendet zu bekommen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Registrieren                                   | Der Prozess der Erstellung eines Kontos oder der Anmeldung für einen Dienst, typischerweise durch Auswahl eines Benutzernamens und Passworts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Replace By Fee (RBF)                           | Eine Bitcoin-Transaktion kann als RBF gekennzeichnet werden, um dem Sender zu ermöglichen, diese Transaktion durch eine andere ähnliche Transaktion zu ersetzen, die eine höhere Gebühr zahlt. Dieser Mechanismus existiert, um Nutzern die Möglichkeit zu geben, zu reagieren, wenn das Netzwerk überlastet wird und die Gebühren unerwartet steigen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Repository                                     | In Versionskontrollsystemen ist ein Repository eine Datenstruktur, die Metadaten für eine Reihe von Dateien oder Verzeichnisstrukturen speichert. Je nachdem, ob das verwendete Versionskontrollsystem verteilt ist, wie Git oder Mercurial, oder zentralisiert, wie Subversion, CVS oder Perforce, kann das gesamte Informationsset im Repository auf jedem Benutzersystem dupliziert oder auf einem einzigen Server gepflegt werden. Einige der Metadaten, die ein Repository enthält, umfassen unter anderem eine historische Aufzeichnung der Änderungen im Repository, eine Reihe von Commit-Objekten und eine Reihe von Verweisen auf Commit-Objekte, genannt Heads.                                                                                                                                                                                                                                                                                                                 |
| Rescan                                         | Prozess des erneuten Scannens des aktuellen Zustands des UTXO-Sets nach Münzen, die zu einem zuvor konfigurierten Ableitungsschema gehören.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Revokation Key                                 | Jeder Widerrufbare Sequenzreifevertrag (Revocable Sequence Maturity Contract, RSMC) enthält zwei Widerrufsschlüssel. Jeder Kanalpartner kennt einen Widerrufsschlüssel. Wenn beide Widerrufsschlüssel bekannt sind, kann der Output des RSMC innerhalb des vordefinierten Zeitfensters ausgegeben werden. Während der Verhandlung eines neuen Kanalzustands werden die alten Widerrufsschlüssel geteilt, wodurch der alte Zustand "widerrufen" wird. Widerrufsschlüssel werden verwendet, um Kanalpartner davon abzuhalten, einen alten Kanalzustand zu übertragen.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Routing                                        | Der Prozess der Nutzung des Lightning Network-Pfades, um eine Zahlung durchzuführen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Routing Fees                                   | Im Lightning Network die Gebühren, die für die Weiterleitung von Zahlungen anderer Nutzer erhoben werden. Einzelne Knoten können ihre eigenen Gebührenrichtlinien festlegen, die als Summe einer festen Basisgebühr und einer Gebührenrate berechnet werden, die von der Zahlungssumme abhängt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Salability                                     | Die Leichtigkeit, mit der ein Gut auf dem Markt verkauft werden kann, wann immer sein Besitzer es wünscht, mit dem geringsten Verlust seines Preises.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Satoshi (sat)                                  | Ein Satoshi ist die kleinste Einheit (Stückelung) von Bitcoin, die auf der Blockchain aufgezeichnet werden kann. Ein Satoshi entspricht einem Hundertmillionstel (0,00000001) eines Bitcoin und ist nach dem Schöpfer von Bitcoin, Satoshi Nakamoto, benannt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Satoshi Nakamoto                               | Der Name, der von der Person oder Gruppe von Personen verwendet wurde, die Bitcoin entworfen und dessen ursprüngliche Referenzimplementierung erstellt haben. Im Rahmen der Implementierung haben sie auch die erste Blockchain-Datenbank konzipiert. Dabei lösten sie als Erste das Problem der doppelten Ausgaben bei digitaler Währung. Ihre wahre Identität bleibt unbekannt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Satoshi Per Byte                               | Eine Einheit zur Messung der Transaktionspriorität, definiert durch die Transaktionsgebühr in Satoshi geteilt durch die Größe der Transaktion in Bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Satoshi Per Verabyte                           | Ein ähnliches Konzept wie Satoshi Per Byte, aber für neuere Adressen, die Segwit verwenden. Entspricht der Transaktionsgröße in Gewichtseinheiten geteilt durch 4. Gewichtseinheiten werden berechnet, indem die Transaktionsgröße (ohne Zeugen) mal 3 genommen und zur Transaktionsgröße inklusive Zeuge addiert wird.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Scarcity                                       | Eigenschaft eines Gutes, das nicht kostenfrei repliziert werden kann. Knappheit hängt nicht von der Anzahl der vorhandenen Einheiten eines Gutes ab, sondern von den Kosten für die Produktion weiterer Einheiten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Script                                         | Bitcoin verwendet ein Skriptsystem für Transaktionen, genannt Bitcoin Script. Es ähnelt der Programmiersprache Forth, ist einfach, stapelbasiert und wird von links nach rechts verarbeitet. Es ist absichtlich Turing-unvollständig, ohne Schleifen oder Rekursion.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Seed Phrase                                    | Eine Liste von Wörtern, die alle Informationen speichern, die benötigt werden, um Bitcoin-Guthaben on-chain wiederherzustellen. Wallet-Software generiert typischerweise eine Seed Phrase und weist den Benutzer an, sie auf Papier niederzuschreiben. Wenn der Computer des Benutzers kaputt geht oder seine Festplatte beschädigt wird, kann er die gleiche Wallet-Software erneut herunterladen und das Papier-Backup verwenden, um seine Bitcoins zurückzubekommen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Segregated Witness (SegWit)                    | Segregated Witness (SegWit) ist ein Upgrade des Bitcoin-Protokolls, das 2017 eingeführt wurde und ein neues Zeugenfeld für Signaturen und andere Transaktionsautorisierungsnachweise hinzufügt. Dieses neue Zeugenfeld ist von der Berechnung der Transaktions-ID ausgenommen, was die meisten Klassen von Transaktionsmalleabilität durch Dritte löst. Segregated Witness wurde als Soft Fork implementiert und ist eine Änderung, die die Protokollregeln von Bitcoin technisch restriktiver macht.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Self-Sovereignty                               | Ein Modell zur Verwaltung digitaler Identitäten, bei dem Einzelpersonen oder Unternehmen das alleinige Eigentum über die Fähigkeit haben, ihre Konten und persönlichen Daten zu kontrollieren.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Send                                           | Der Prozess des Versendens von Bitcoin an eine Adresse.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Sensitivity Mode                               | Wird über einen Schalter in den Laden-Einstellungen aktiviert, führt die Aktivierung dazu, dass numerische Werte (z.B. Bitcoin-Betrag) in allen Ansichten verschleiert werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Server Settings                                | Einstellungen innerhalb des BTCPay Servers, die serverweit gelten (im Gegensatz zu Laden-Einstellungen, die auf einen einzelnen Laden beschränkt sind).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SHA-256                                        | Eine kryptografische Hash-Funktion. Ein Mitglied der Familie von Hash-Funktionen, die als Secure Hashing Algorithm (SHA) Funktionen bezeichnet werden.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Shopify                                        | Ein kanadisches multinationales E-Commerce-Unternehmen mit Hauptsitz in Ottawa, Ontario. Shopify ist der Name seiner proprietären E-Commerce-Plattform für Online-Shops und Einzelhandels-Verkaufssysteme.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SMTP                                           | Simple Mail Transfer Protocol ist ein Internetstandard-Kommunikationsprotokoll für die elektronische Mailübertragung.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Soft Fork                                      | Ein Protokoll-Upgrade, das sowohl vorwärts- als auch rückwärtskompatibel ist, sodass sowohl alte als auch neue Knoten die gleiche Kette weiterhin nutzen können.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Software Stack                                 | In der Informatik ist ein Lösungsstack oder Software-Stack eine Reihe von Software-Subsystemen oder Komponenten, die benötigt werden, um eine vollständige Plattform zu erstellen, sodass keine zusätzliche Software zur Unterstützung von Anwendungen benötigt wird.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Store                                          | Ein Laden innerhalb des BTCPay Servers kann als "Zuhause" für eine spezifische Bitcoin-Wallet angesehen werden, erweitert um alle Funktionen des BTCPay Servers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Store Settings                                 | Einstellungen innerhalb des BTCPay Servers, die spezifisch für einen Laden sind.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Taproot                                        | Upgrade für Bitcoin, das mehrere neue Funktionen einführen würde. Das Upgrade wird in den BIPs 340, 341 und 342 beschrieben und führt das Schnorr-Signaturschema, Taproot und Tapscript ein. Zusammen führen diese Upgrades neue, effizientere, flexiblere und privatere Wege der Bitcoin-Übertragung ein.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Thier's Law                                    | Gesetz, das besagt, dass gutes Geld schlechtes Geld verdrängen wird.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Third-Party Host                               | Wenn eine Website für eine Einzelperson oder ein Unternehmen auf Servern betrieben wird, die einem anderen Unternehmen gehören und von diesem verwaltet werden. Die Alternative besteht darin, Ihre Website auf Ihren eigenen Servern in Ihrem eigenen Rechenzentrum zu hosten.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Timelock                                       | Ein Timelock ist eine Art von Belastung, die das Ausgeben einiger Bitcoin bis zu einem bestimmten zukünftigen Zeitpunkt oder Blockhöhe einschränkt. Timelocks spielen in vielen Bitcoin-Verträgen eine prominente Rolle, einschließlich Zahlungskanälen und HTLCs.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Topologie                                      | Die Topologie des Lightning-Netzwerks beschreibt die Form des Lightning-Netzwerks als mathematischen Graphen. Knoten des Graphen sind die Lightning-Knoten (Netzwerkteilnehmer/Peers). Die Kanten des Graphen sind die Zahlungskanäle. Die Topologie des Lightning-Netzwerks wird mit Hilfe des Gossip-Protokolls öffentlich übertragen, mit Ausnahme von nicht angekündigten Kanälen. Das bedeutet, dass das Lightning-Netzwerk deutlich größer sein könnte als die angekündigte Anzahl von Kanälen und Knoten. Die Kenntnis der Topologie ist von besonderem Interesse im Prozess des source-based Routings von Zahlungen, bei dem der Sender eine Route entdeckt.                                                                                                                                                                                                                                                                                                                       |
| Transaktion                                    | Transaktionen sind Datenstrukturen, die von Bitcoin verwendet werden, um Bitcoin von einer Adresse zu einer anderen zu übertragen. Mehrere tausend Transaktionen werden in einem Block zusammengefasst, der dann (gemined) in der Blockchain aufgezeichnet wird. Die erste Transaktion in jedem Block, die Coinbase-Transaktion genannt wird, generiert neue Bitcoin.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Transaktions-ID                                | Eine Zeichenfolge aus Buchstaben und Zahlen, die eine spezifische Transaktion auf der Blockchain identifiziert. Die Zeichenfolge ist einfach der doppelte SHA-256-Hash einer Transaktion. Dieser Hash kann verwendet werden, um eine Transaktion auf einem Knoten oder Block-Explorer nachzuschlagen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Zwei-Faktor-Authentifizierung (2FA)            | Eine Sicherheitsmethode für Identitäts- und Zugriffsmanagement, die zwei Formen der Identifikation erfordert, um auf Ressourcen und Daten zuzugreifen, oft mit einem sekundären Gerät zusätzlich zum standardmäßigen Login-Passwort.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Unzensierbar                                   | Eigenschaft, dass keine Entität in der Lage ist, eine Bitcoin-Transaktion rückgängig zu machen oder eine Wallet oder Adresse auf eine schwarze Liste zu setzen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Unkonfiszierbar                                | Eigenschaft, dass keine Entität Bitcoin gegen den Willen einer Entität nehmen kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Unausgegebene Transaktionsausgänge (UTXO)      | Ausgänge, die noch nicht ausgegeben wurden und daher für neue Transaktionen verfügbar sind.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Benutzererfahrung (UX)                         | Wie ein Benutzer mit einem Produkt, System oder Dienst interagiert und es erlebt. Es umfasst die Wahrnehmungen einer Person bezüglich Nutzen, Benutzerfreundlichkeit und Effizienz.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Benutzeroberfläche (UI)                        | Der Punkt der Mensch-Computer-Interaktion und Kommunikation in einem Gerät.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Verifizierbar                                  | Eigenschaft eines Gutes, das leicht von Fälschungen und Nachahmungen unterschieden werden kann.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Virtuell                                       | Existiert auf oder wird auf einem Computer oder Computernetzwerk simuliert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Virtuelle Maschine (VM)                        | In der Informatik ist eine virtuelle Maschine die Virtualisierung oder Emulation eines Computersystems. Virtuelle Maschinen basieren auf Computerarchitekturen und bieten die Funktionalität eines physischen Computers. Ihre Implementierungen können spezialisierte Hardware, Software oder eine Kombination aus beidem umfassen.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Virtueller Privatserver                        | Ein virtueller Privatserver ist eine virtuelle Maschine, die als Dienstleistung von einem Internet-Hosting-Dienst verkauft wird. Der Begriff "virtueller dedizierter Server" hat eine ähnliche Bedeutung. Ein virtueller Privatserver führt seine eigene Kopie eines Betriebssystems aus, und Kunden können Superuser-Zugriff auf diese Betriebssysteminstanz haben, sodass sie fast jede Software installieren können, die auf diesem Betriebssystem läuft.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Volatilität                                    | Maß für das Ausmaß der Preisveränderung eines Vermögenswerts über die Zeit. Vermögenswerte, die regelmäßig große Preisänderungen erfahren, sind volatiler, während Vermögenswerte mit einem stabileren Preis weniger volatil sind.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Wallet                                         | Bitcoin-Wallets halten die Schlüssel eines Benutzers, die es ihm ermöglichen, Bitcoin zu empfangen, Transaktionen zu signieren und sein Kontoguthaben zu überprüfen. Die privaten und öffentlichen Schlüssel, die in einem Bitcoin-Wallet gehalten werden, erfüllen zwei unterschiedliche Funktionen, sind aber in ihrer Erstellung miteinander verbunden. Bitcoin-Wallets enthalten die Schlüssel eines Benutzers, nicht seine tatsächlichen Bitcoin. Konzeptionell ist ein Wallet wie ein Schlüsselbund, in dem Sinne, dass es viele Paare von privaten und öffentlichen Schlüsseln hält. Diese Schlüssel werden verwendet, um Transaktionen zu signieren, wodurch ein Benutzer nachweisen kann, dass er die Ausgänge von Transaktionen auf der Blockchain besitzt, d.h. seine Bitcoin. Alle Bitcoin werden in Form von Transaktionsausgängen auf der Blockchain aufgezeichnet.                                                                                                          |
| Wasabi Wallet                                  | Ein Open-Source, nicht-verwahrendes, auf Datenschutz fokussiertes Bitcoin-Wallet für Desktop, das trustless CoinJoin implementiert.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Watch-Only Wallet                              | Bitcoin-Wallets, die es Ihnen ermöglichen, Ihre Bitcoin in Cold Storage zu verfolgen, während die Möglichkeit, Mittel auszugeben, deaktiviert wird. Dies liegt daran, dass Watch-Only-Wallets keine privaten Schlüssel speichern oder verwenden und daher nicht in der Lage sind, Ausgaben im Namen des Benutzers zu autorisieren.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Whale                                          | Im Kontext von Bitcoin ist ein Whale jemand, der eine große Menge an Bitcoin besitzt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| White-Label                                    | Ein White-Label-Produkt ist ein Produkt oder Dienst, der von einem Unternehmen hergestellt wird, den andere Unternehmen umbranden, um es erscheinen zu lassen, als hätten sie es hergestellt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Whitepaper                                     | Stellt eine neue Idee oder ein Thema zur Diskussion vor. Das Bitcoin-Whitepaper führte Bitcoin als „Peer-to-Peer-Elektronisches Bargeldsystem“ ein, das „keine vertrauenswürdigen Drittparteien benötigt“. Satoshi Nakamoto veröffentlichte das Whitepaper am 31. Oktober 2008 an eine E-Mail-Liste von Kryptographen und Cypherpunks.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Wrapped Segwit                                 | Eine Designimplementierung, die in das SegWit-Upgrade aufgenommen wurde, um Wallets und andere Bitcoin-Software die Unterstützung von SegWit zu erleichtern. Um dies zu erreichen, werden die beiden nativen SegWit-Scripts, P2WPKH und P2WSH, als „redeemScript“ einer P2SH-Transaktion verwendet, was zu eingewickelten SegWit-Scripttypen von P2SH-P2WPKH und P2SH-P2WSH führt.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

![Bild](assets/en/129.webp)
