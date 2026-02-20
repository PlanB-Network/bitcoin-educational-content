---
name: Matrix
description: Ein Leitfaden zum Verständnis, zur Konfiguration und zur Verwendung von Matrix, der sicheren, offenen und dezentralen Kommunikationsplattform.
---

![cover](assets/cover.webp)



## Was ist Matrix?



Matrix ist ein **dezentralisiertes Kommunikationsprotokoll**, das den Austausch von Nachrichten, Dateien und Audio-/Videoanrufen zwischen Nutzern und Anwendungen ermöglicht, ohne von einem zentralen Unternehmen abhängig zu sein. Im Gegensatz zu herkömmlichen Messaging-Plattformen ist Matrix eine **offene Infrastruktur**, vergleichbar mit E-Mail: Jeder kann einen Server auswählen oder selbst betreiben und dabei die Fähigkeit zum Austausch mit dem Rest des Netzwerks beibehalten.



Matrix zeichnet sich durch drei grundlegende Prinzipien aus:



### Ein Protokoll, nicht eine Anwendung



Matrix ist keine Anwendung wie WhatsApp oder Telegram.


Es ist eine standardisierte Sprache, die von vielen Anwendungen verwendet werden kann.


Mit anderen Worten: Eine Vielzahl von Element-Software, FluffyChat, Cinny, Nheko und andere, bieten Zugang zum gleichen Matrix-Netzwerk.



Das garantiert völlige Freiheit: Wechsel der Anwendung ohne Kontaktverlust, Vielfalt der Schnittstellen, Unabhängigkeit von einem einzigen Lieferanten.



![capture](assets/fr/03.webp)



### Ein dezentrales, föderiertes Netzwerk



Die Struktur von Matrix basiert auf einer **Föderation**, einem Modell, bei dem mehrere unabhängige Server miteinander kooperieren.


Jeder Server (genannt _homeserver_) kann Benutzer beherbergen, Chaträume einrichten und Nachrichten mit anderen Servern im Netzwerk synchronisieren.


So :





- keine einzelne Stelle das gesamte System kontrolliert;
- ein Server verschwinden kann, ohne dass der Rest des Netzes beeinträchtigt wird;
- jede Organisation oder Einzelperson kann ihren eigenen Raum verwalten.



Dieses Modell gewährleistet eine **hohe Widerstandsfähigkeit** und spiegelt die Werte der technologischen Souveränität wider.



![capture](assets/fr/03.webp)



### Ein sicheres, verschlüsseltes System



Matrix unterstützt **Ende-zu-Ende-Verschlüsselung (E2EE)** für privaten Austausch und verschlüsselte Gruppen.


Die Nachrichten können nur von den Teilnehmern gelesen werden, nicht von den Zwischenservern.


Dieser Ansatz ermöglicht die Kommunikation, ohne dass der Inhalt des Austauschs für Dritte sichtbar ist, wobei die Transparenz des Protokolls und die Möglichkeit, einen eigenen Server zu hosten, erhalten bleiben.



![capture](assets/fr/05.webp)



### Einzigartige Interoperabilität



Einer der größten Vorteile von Matrix ist seine Fähigkeit, als **Brücke zwischen verschiedenen Kommunikationssystemen** zu fungieren. Dank der _Brücken_ ist es möglich, eine Verbindung zwischen :





- Telegram
- WhatsApp
- Signal
- Bote
- Slack
- Diskord
- IRC, XMPP, usw.



Dies ermöglicht die Zusammenführung von Gemeinschaften, die über mehrere Plattformen verstreut sind, wobei die Kontrolle über die Infrastruktur erhalten bleibt.



![capture](assets/fr/06.webp)



## Wie funktioniert Matrix?



In diesem Abschnitt wird die interne Struktur des Matrix-Netzwerks vorgestellt, um zu verstehen, wie Benutzer, Server und Anwendungen innerhalb dieses dezentralen Ökosystems interagieren. Matrix basiert auf drei wesentlichen Elementen: _Homeserver_, Identitäten und _Clients_, die zur Kommunikation verwendet werden.



### Server: Heimserver



Matrix läuft auf unabhängigen Servern, den sogenannten _Homeservern_.


Jeder Homeserver verwaltet :





- die Benutzerkonten, die es beherbergt,
- privatgespräche und Lounges, an denen diese Nutzer teilnehmen,
- synchronisierung mit anderen Netzwerkservern.



Alle an das Matrix-Netzwerk angeschlossenen Homeserver tauschen automatisch Nachrichten und Ereignisse aus gemeinsamen Wohnzimmern aus. Zum Beispiel:





- ein auf Server A registrierter Benutzer kann mit einem Benutzer auf Server B chatten,
- ein Salon kann auf Dutzende von Servern verteilt sein,
- niemand hat die Kontrolle über einen Salon oder eine Gemeinschaft als Ganzes.



Dieses Modell ist äußerst belastbar und ermöglicht es jeder Organisation oder Einzelperson, ihre eigene Infrastruktur zu verwalten.



### Matrix-Bezeichner



Jeder Nutzer hat eine eindeutige Kennung, die **MXID** (_Matrix ID_), die wie eine Adresse aussieht:



```bash
@nomdutilisateur:serveur.xyz
```



Es besteht aus :





- einen Benutzernamen, dem ein **@** vorangestellt ist
- der Name des Servers, auf dem das Konto erstellt wurde, mit vorangestelltem **:**



Beispiele:





- `@alice:matrix.org`
- `@bened:monserveur.bj`



Diese Kennung ermöglicht die Kommunikation mit jedem anderen Matrix-Benutzer, unabhängig vom Server, von dem sie stammt.



### Matrix-Kunden (Anwendungen)



Um Matrix zu nutzen, müssen Sie eine Verbindung mit einer Anwendung namens **Client Matrix** herstellen.



Die bekanntesten sind:





- Element (Web, Handy, Desktop)
- FluffyChat (mobil)
- Cinny (minimalistisches Web/Desktop)
- Nheko (Schreibtisch)



Diese Anwendungen sind lediglich Schnittstellen für :





- um Nachrichten anzuzeigen,
- text, Bilder oder Dateien senden,
- sich an Messen beteiligen oder solche gründen,
- audio-/Videoanrufe tätigen.



Alle Anwendungen kommunizieren mit den Servern über das gleiche standardisierte Protokoll.



### Räume und private Nachrichten (DM)



In Matrix findet der Austausch in **Räumen** statt:





- ein Raum kann öffentlich oder privat sein
- er kann zwei Personen oder Tausende aufnehmen
- sie kann von mehreren Servern gemeinsam genutzt werden
- er hat eine eindeutige Kennung, die mit **!** beginnt



Private Nachrichten sind einfach Chaträume mit zwei Teilnehmern, die oft als **DM (Direct Messages)** bezeichnet werden.



Die Synchronisierung der Salons findet in Echtzeit zwischen den teilnehmenden Servern statt, wodurch ein nahtloses Erlebnis bei gleichzeitiger Dezentralisierung gewährleistet wird.



## Warum Matrix verwenden?



Matrix ist nicht nur eine Alternative zu zentralisierten Nachrichtensystemen: Es ist eine Technologie, die echte Bedürfnisse in Bezug auf digitale Souveränität, Sicherheit und Interoperabilität erfüllt. Es gibt viele Gründe, warum immer mehr Menschen, Unternehmen und Institutionen dieses Protokoll für ihre Kommunikation wählen.



### Gewinnen Sie die Kontrolle über Ihre Kommunikation zurück



Die meisten Messaging-Plattformen arbeiten nach einem zentralisierten Modell: Ein einziger Anbieter kontrolliert Server, Zugang, Daten und Nutzungsregeln. Dieses Modell impliziert eine völlige Abhängigkeit vom Anbieter.


Matrix verfolgt einen anderen Ansatz.


Jeder kann wählen, wo sein Konto gehostet werden soll, oder sogar seinen eigenen Server einrichten. Keine Einrichtung ist in der Lage, einen Nutzer zu sperren, eine aufdringliche Identifizierung zu verlangen oder eine Änderung der Richtlinien durchzusetzen.


Diese Architektur gibt sowohl dem Einzelnen als auch den Organisationen ihre Autonomie zurück. Die Kommunikation basiert nicht mehr auf dem Vertrauen in ein Unternehmen, sondern auf einem offenen, dokumentierten und überprüfbaren Protokoll.



### Sichere, verschlüsselte Kommunikation



Matrix unterstützt die Ende-zu-Ende-Verschlüsselung für private Unterhaltungen und Gruppen. Dieser Mechanismus stellt sicher, dass nur die Teilnehmer Nachrichten lesen können, auch wenn sie über Server von Drittanbietern im Verbund laufen.



Das Protokoll verwendet den Megolm/Olm-Algorithmus, der speziell für hohe Sicherheit in verteilten Umgebungen mit mehreren Geräten entwickelt wurde.



Dadurch wird es möglich, :





- sensible Gespräche zu schützen,
- den unbefugten Zugriff zu verhindern (auch vom Host-Server aus),
- die Vertraulichkeit auf Dauer zu wahren.



Die Verschlüsselung ist keine Option, sondern eine Kernkomponente des Protokolls.



### Keine Abhängigkeit mehr von einer einzigen Anwendung



Matrix ist keine Anwendung, sondern ein Protokoll.



Diese Vielfalt an Kunden garantiert :





- eine an die individuellen Bedürfnisse angepasste Auswahl,
- die Möglichkeit, Matrix auf jeder Art von Gerät zu verwenden,
- keine Abhängigkeit von einer einzigen Software.



Wenn ein Kunde ungeeignet ist oder nicht mehr betreut wird, wählen Sie einfach einen anderen aus: Das Konto wird normal weitergeführt.



### Zusammenschluss und Vernetzung verschiedener Gemeinschaften



Federation ermöglicht die Zusammenarbeit verschiedener Server, die unabhängig voneinander verwaltet werden.


So :





- eine Organisation kann ihren eigenen Homeserver verwalten,
- einzelpersonen können öffentlichen Servern beitreten,
- können alle miteinander kommunizieren, als ob sie sich auf derselben Plattform befänden.



Diese Flexibilität ermöglicht es, Kommunikationsräume zu schaffen, die an jeden Bedarf angepasst sind: Teams, Vereine, Gemeinschaften, Institutionen oder Open-Source-Projekte.



Matrix ist besonders beliebt in technischen Kreisen, bei Aktivistenkollektiven, Forschern, Regierungen und zunehmend auch in Bitcoin-Gemeinschaften.



### Einzigartige Interoperabilität in der Messaging-Landschaft



Einer der Hauptvorteile von Matrix ist die Fähigkeit zur **Erweiterung** der Börsen dank der Brücken, die eine Verbindung zwischen :





- WhatsApp
- Telegram
- Signal
- Slack
- Diskord
- IRC
- XMPP
- und viele andere Plattformen



Matrix wird so zu einer vereinheitlichenden Ebene für die Kommunikation, die mehrere über verschiedene Anwendungen verstreute Gemeinschaften zusammenführt.



Diese Interoperabilität verringert die Fragmentierung und vereinfacht die Zusammenarbeit.



### Ein freies, offenes und nachhaltiges Protokoll



Das Matrix-Protokoll ist vollständig quelloffen und transparent entwickelt.


Dies garantiert mehrere Vorteile:





- eine kontinuierliche Weiterentwicklung der Norm,
- die Möglichkeit für jedermann, den Code zu überprüfen,
- unabhängigkeit von wirtschaftlichen oder politischen Veränderungen,
- langfristige Widerstandsfähigkeit.



Im Gegensatz zu proprietären Nachrichtensystemen hängt die Zukunft von Matrix nicht von einem einzigen Unternehmen ab, sondern von einer globalen Gemeinschaft und einem offenen Standard.



## Wie kann ich ein Matrix-Konto erstellen?



Die Erstellung eines Matrix-Kontos ist einfach und erfordert keine technischen Kenntnisse. Benutzer können einem bestehenden Server beitreten, ein Login erstellen und sofort mit dem Chatten beginnen. In diesem Abschnitt werden die wichtigsten Schritte beschrieben.



### Wählen Sie einen Server (öffentlich oder privat)



Matrix ist ein föderiertes Netzwerk: Es gibt zahlreiche Server (Homeserver), die von verschiedenen Organisationen, Gemeinschaften oder Einzelpersonen verwaltet werden. Die Wahl des Servers bestimmt nur, _wo_ das Konto gehostet wird, verhindert aber nicht die Kommunikation mit dem gesamten Netzwerk.


**Zwei Optionen sind verfügbar:**



### - Verwenden Sie einen öffentlichen Server



Dies ist die einfachste Lösung.


Beispiele für beliebte Server:





- _matrix.org_ (die bekannteste)
- _envs.net_
- thematische Gemeinschaftsserver (Technik, Datenschutz, Open-Source...)



Diese Server sind für Anfänger geeignet, die sich schnell anmelden wollen.



### - Verwenden Sie einen privaten Server



Ideal für :





- eine Organisation,
- eine Familie,
- ein Open-Source-Projekt,
- ein Arbeitsteam,
- oder für die souveräne, selbstgehostete Nutzung.



In diesem Fall muss jemand den Server verwalten (Synapse, Dendrite, Conduit...).


Unabhängig davon, für welchen Server Sie sich entscheiden, können die Benutzer dank der Föderation miteinander kommunizieren.



### Schritt für Schritt ein Konto erstellen



Da Matrix ein offenes Protokoll ist, können mehrere Anwendungen darauf zugreifen.


Wie oben beschrieben, bieten sie je nach Bedarf unterschiedliche Schnittstellen und Funktionalitäten:





- Element**: der umfassendste Client, der auf allen Plattformen verfügbar ist.
- FluffyChat**: einfach, modern und ideal für Handys.
- Nheko**: leichter, ergonomischer Client für PCs.
- SchildiChat**: Element-Variante mit ergonomischen Verbesserungen.
- NeoChat**: integriert in das KDE-Ökosystem.



Die Wahl des Clients hat keinen Einfluss auf das Konto: alle funktionieren mit jedem Matrix-Server.



### Klassische Schritte :





- Öffnen Sie die gewählte Anwendung. In unserem Fall werden wir dies mit [Element](app.element.io) tun.
- Wählen Sie "Ein Konto erstellen".



![cover-kali](assets/fr/10.webp)



Der Einfachheit halber können Sie ein Matrix-Konto über **Google, Facebook, Apple, GitHub oder GitLab** erstellen. Diese Dienste wissen nur, dass ihr Konto für den Zugriff auf Matrix verwendet wurde: Dies wird als **soziale Verbindung** bezeichnet.



Für mehr Vertraulichkeit können Sie sich auch manuell registrieren, indem Sie einen **Benutzernamen**, ein **Passwort** und eine **E-Mail-Adresse** wählen.



Je nach gewähltem Server kann ein **Captcha** erforderlich sein, ebenso wie die Akzeptanz der **Nutzungsbedingungen**.



Sobald die Anmeldung bestätigt wurde, wird eine Bestätigungs-E-Mail versandt.


Klicken Sie einfach auf den Link, um Ihr Konto zu aktivieren und auf die Webanwendung (Element) zuzugreifen, um an Ihren ersten Matrix-Gesprächen teilzunehmen.



![cover-kali](assets/fr/11.webp)



Sie haben jetzt ein Konto und verwenden die Web-Version von Element.



## Fügen Sie Ihren ersten Kontakt hinzu



Um mit einer Person in Matrix zu kommunizieren, müssen Sie nur deren vollständige Kennung, die **Matrix-ID**, kennen.



Beispiel:



`@alice:matrix.org @bened:monserveur.bj`



### Einen Kontakt hinzufügen



Um Freunde zu Ihrem Gruppenchat einzuladen, klicken Sie auf den Kreis "i" in der oberen rechten Ecke. Dadurch öffnet sich das rechte Fenster. Klicken Sie auf "Personen", um die Liste der Mitglieder in diesem Raum anzuzeigen: Sie sollten die einzigen sein, die im Moment anwesend sind.



![cover-kali](assets/fr/12.webp)



Klicken Sie oben in der Personenliste auf "In diesen Raum einladen". Daraufhin öffnet sich eine Aufforderung, mit der Sie Ihre Freunde in Matrix einladen können. Wenn sie bereits bei Matrix eingeloggt sind, geben Sie ihre Matrix-ID ein. Ist dies nicht der Fall, geben Sie ihre E-Mail-Adresse ein und sie werden eingeladen, sich uns anzuschließen.



Es gibt kein "Freundes"-System: Ein Kontakt ist einfach eine Person, mit der ein Gespräch eröffnet wurde.



![cover-kali](assets/fr/13.webp)



Die Person, die Sie eingeladen haben, kann die Einladung annehmen oder ablehnen. Wenn sie annimmt, sollten Sie sehen, dass sie dem Raum beitritt. Je mehr, desto besser!



![cover-kali](assets/fr/14.webp)



### Einrichten eines eigenen Servers



Matrix kommt erst richtig zur Geltung, wenn es in Verbindung mit einem persönlichen Server eingesetzt wird.


Die Einrichtung eines eigenen Homeservers ermöglicht es Ihnen, :





- die vollständige Kontrolle über die Daten zu behalten,
- ihre eigenen Nutzungsregeln festlegen,
- mehrere Konten hosten (Freunde, Team, Gemeinschaft),
- und ein Höchstmaß an Belastbarkeit im Falle von Beschränkungen oder Zensur zu gewährleisten.



**Verfügbare Lösungen:**





- Synapse**: die historische und vollständigste Implementierung.
- Dendrite**: Leichter, leistungsfähiger und für die Zukunft des Protokolls konzipiert.
- Conduit**: eine minimalistische Variante, die einfach zu implementieren ist.



**Voraussetzungen:**





- einen Domänennamen,
- eine Maschine oder einen VPS,
- mindestkenntnisse in der Systemverwaltung.



Auch wenn es ein wenig Konfiguration erfordert, macht die Verwaltung eines eigenen Servers Matrix zu einem souveränen und dauerhaften Werkzeug.



### Teilnahme an Ihren ersten Fachmessen



Matrix stützt sich stark auf _Räume_ (Wohnräume).


Es gibt öffentliche, private, kommunale, technische, lokale und internationale Fachmessen.



**Drei Möglichkeiten, einem Salon beizutreten:**



1. **Über einen Einladungslink** (oft in Form einer URL "matrix.to").


2. **Suchen Sie in der Anwendung nach dem Namen des Salons**.


3. **Durch Eingabe der vollständigen Show-ID**, z. B. :


#bitcoin:matrix.org"


#communauté-bénin:monsrv.bj



Nach dem Beitritt verhält sich der Chatraum wie eine klassische Newsgroup, mit Verlauf, Verschlüsselung, Dateien, Reaktionen und Audio-/Videoanrufen, je nach verwendetem Client.



![capture](assets/fr/09.webp)



## Weiter gehend



Sobald Sie die Grundlagen beherrschen, bietet Matrix eine Vielzahl von fortgeschrittenen Möglichkeiten. Ganz gleich, ob Sie andere Nachrichtensysteme anschließen, Ihren eigenen Server hosten oder eine Gemeinschaft organisieren möchten, das Ökosystem ist sehr umfangreich.



### Brücken (WhatsApp, Telegram, Signal, usw.)



Eine Bridge verbindet Matrix mit anderen Nachrichtensystemen.


Mit diesem Programm können Sie Nachrichten von :





- WhatsApp
- Telegram**
- Signal**
- Facebook Messenger
- Diskord
- Slack**
- IRC** (IRC)
- und viele andere



### Was Brücken leisten können





- Zentralisieren Sie alle Ihre Unterhaltungen in Matrix
- Bereitstellung einer offenen Schnittstelle für die Interaktion mit proprietären Diensten
- Verwalten Sie eine plattformübergreifende Community von einem einzigen Standort aus



Einige Brücken sind offiziell, andere auf kommunaler Ebene.


Je nach Abteilung können sie verlangen:





- einen persönlichen Server,
- eine zusätzliche Konfiguration,
- oder die Nutzung einer bestehenden öffentlichen Brücke.



### Verwendung von Matrix für eine Bitcoin-Organisation, eine Gemeinde oder ein Projekt



Matrix ist nicht nur ein persönliches Werkzeug.


Es kann verwendet werden, um Arbeitsgruppen zu strukturieren, lokale Gemeinschaften zu organisieren oder die Projektkommunikation zu verwalten.



**Verwendungsbeispiele:**





- Open-Source-Gemeinschaften
- Bitcoin und Lightning-Ökosystemprojekte
- Studenten- oder Entwicklergruppen
- Bürgerliche Organisationen
- Unabhängige Medien
- Lokale Gruppen und Verbände



**Warum ist das interessant?





- 100% Open-Source**-Werkzeug
- Souveräne und dezentralisierte** Kommunikation
- Die Räume sind in **Lounges**, **Untergruppen**, **private Lounges**, usw. unterteilt.
- Integration mit Nextcloud, GitLab, Mattermost oder benutzerdefinierten Bots
- Feinabgestimmte Verwaltung von Berechtigungen und Moderation



Matrix wird so zu einem Kommunikationspfeiler für jede Struktur, die unabhängig von den großen zentralen Plattformen bleiben will.



## Schlussfolgerung



Matrix stellt eine moderne, offene und sichere Lösung für die Echtzeitkommunikation dar und bietet eine dezentrale Alternative zu herkömmlichen Plattformen. Dank seiner föderierten Architektur und fortschrittlicher Verschlüsselungsprotokolle können die Nutzer die Kontrolle über ihre Daten behalten und gleichzeitig eine flüssige, interoperable Erfahrung genießen. Ob für den privaten, beruflichen oder gemeinschaftlichen Gebrauch, Matrix bietet einen robusten und skalierbaren Rahmen für den Aufbau von Kommunikationsumgebungen, die den heutigen Anforderungen entsprechen.



Um mehr zu erfahren und alle Funktionen von Matrix zu entdecken, können Sie die offizielle Dokumentation konsultieren, die hier verfügbar ist:


[https://matrix.org/docs/](https://matrix.org/docs/)