---
name: Umbrel Nostr
description: Konfiguration und Verwendung von Nostr-Anwendungen auf Umbrel
---

![cover](assets/cover.webp)



## Vorraussetzungen: Installation von Umbrella



Umbrel ist eine Open-Source-Plattform, mit der Sie Bitcoin-Anwendungen und andere Dienste einfach auf Ihrem eigenen Server hosten können. Es ist eine All-in-One-Lösung, die das Selbsthosten von Bitcoin-Knoten und dezentralen Anwendungen stark vereinfacht.



Vergewissern Sie sich, dass Sie Umbrel installiert haben, indem Sie unserer Installationsanleitung folgen:



https://planb.network/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Einführung in Nostr



**Nostr** ist ein offenes, dezentrales Netzwerkprotokoll, das für soziale Netzwerke entwickelt wurde. Sein Name steht für _"Notes and Other Stuff Transmitted by Relays"_. Es ermöglicht jedem, Nachrichten (Notizen) zu veröffentlichen, die als JSON-Ereignisse verwaltet werden, und sie über Relay-Server statt über eine zentrale Plattform zu verbreiten. Jeder Benutzer verfügt über ein Paar kryptografischer Schlüssel (privat/öffentlich), die als Identifikator dienen: der öffentliche Schlüssel (npub) identifiziert den Benutzer, und der private Schlüssel (nsec) ermöglicht die Signierung von Nachrichten. Dank dieser verteilten Architektur bietet **Nostr Zensurresistenz** und große Flexibilität: Sie können mehrere Clients verwenden und sich mit beliebig vielen Relays verbinden, ohne von einem einzigen Server abhängig zu sein.



Kurz gesagt ist Nostr ein dezentrales Kommunikationsprotokoll, bei dem **Client** (Benutzeranwendungen) Ereignisse über **Relayer** (Server) senden und empfangen. Dieses Protokoll ist seit 2023 bei der Bitcoin-Gemeinschaft besonders beliebt, da es auf Dezentralisierung und Datenhoheit setzt.



**Hinweis:** Um Nostr zu nutzen, benötigen Sie Ihren privaten Schlüssel (der von einem Nostr-Client oder über eine spezielle Erweiterung generiert wird). **Geben Sie Ihren privaten Schlüssel niemals weiter**, da sich sonst jemand als Sie ausgeben könnte. Bewahren Sie ihn an einem sicheren Ort auf und verwenden Sie sichere Schlüsselverwaltungstools (siehe Tipp unten).



## Umbrella-Anwendungen für Nostr



Umbrel bietet ein Ökosystem integrierter Anwendungen, um die Vorteile von Nostr auf Ihrem persönlichen Node voll auszuschöpfen. Wir werden die Nutzung der wichtigsten Nostr-bezogenen Anwendungen im Detail beschreiben: **Nostr Relay**, **noStrudel**, **Snort** und **Nostr Wallet Connect**. Jede von ihnen erfüllt einen bestimmten Bedarf: _Nostr Relay_ ist ein **privater Relay-Server**, _noStrudel_ und _Snort_ sind **Nostr-Clients** (Schnittstellen zum Lesen/Veröffentlichen von Notizen), während _Nostr Wallet Connect_ ein Werkzeug ist, um Ihr **Lightning-Portfolio** mit Nostr zu verknüpfen.



### Nostr Relay - Dein privates Relais auf Umbrel



![Page d'installation de Nostr Relay sur l'App Store Umbrel](assets/fr/01.webp)



**Nostr Relay** ist die offizielle Anwendung von Umbrel, mit der du dein **eigenes Nostr-Relay** auf deinem Node betreiben kannst. Das Hauptziel ist es, ein **privates** und zuverlässiges Relay zu haben, um all deine **Nostr-Aktivitäten** in Echtzeit zu **sichern**. Mit anderen Worten, indem du dieses persönliche Relais zusätzlich zu den öffentlichen Relais benutzt, stellst du sicher, dass alle deine Notizen, Nachrichten und Reaktionen nach Hause kopiert werden, sicher vor Zensur oder Datenverlust.



**Installation:** Aus dem Umbrel App Store (Kategorie _Social_) installieren Sie _Nostr Relay_. Einmal gestartet, läuft die Anwendung im Hintergrund (Docker-Service).



![Interface de Nostr Relay avec l'URL du relais](assets/fr/02.webp)



Über Umbrel sehen Sie sein Interface-Web: Es bietet grundlegende Informationen und vor allem die URL Ihres Relais (oben rechts), die Sie für die weitere Verwendung kopieren müssen. Eine Schaltfläche zur Synchronisierung (Globus-Symbol) ist ebenfalls verfügbar.



**Um die Vorteile Ihres Umbrel-Relais zu nutzen:**



**Fügen Sie das Relais zu Ihrem Nostr-Client hinzu:** Fügen Sie in Ihrer Client-Anwendung (z.B. Damus auf iOS, Amethyst auf Android, Snort oder noStrudel auf Umbrel, usw.) die URL Ihres privaten Relais hinzu, die Sie zuvor kopiert haben. Standardmäßig lauscht das Umbrel-Relay auf Port **4848**. Wenn Sie über das lokale Netz darauf zugreifen, ergibt dies eine URL wie: `ws://umbrel.local:4848` (oder verwenden Sie die lokale IP von Umbrel).



Wenn Sie Tailscale verwenden (siehe unten), können Sie sogar den MagicDNS-DNS-Alias (normalerweise `umbrel` oder einen automatisch generierten Namen) verwenden, um von überall her darauf zuzugreifen, immer auf Port 4848.



Wenn du Tor bevorzugst, hole dir den .onion Address von Umbrel und benutze ihn mit Port 4848 über einen Tor-kompatiblen Browser oder Client (siehe Abschnitt Tor)



Sobald die URL zur Relaiskonfiguration Ihres Nostr-Clients hinzugefügt wurde, verbinden Sie sich mit diesem Relais. Sie sollten in Ihrem Client sehen, dass das Umbrel-Relais verbunden ist (normalerweise durch einen Green-Punkt oder ähnliches angezeigt).



**Verlauf synchronisieren (optional)**: Im Interface-Web von _Nostr Relay_ auf Umbrel, klicken Sie auf das Symbol **Globus** 🌐 (oben auf der Seite). Diese Aktion zwingt Ihr Umbrel-Relais, sich mit Ihren anderen Relais (die in Ihrem Client konfiguriert sind) zu verbinden, um Ihre **alten öffentlichen** Aktivitäten zu importieren. Das bedeutet, dass frühere Notizen, die Sie über öffentliche Relays veröffentlicht oder gelesen haben, auch heruntergeladen und auf Ihrem privaten Relais gespeichert werden. Bitte warten Sie, bis die Synchronisierung stattgefunden hat.



**Nutzen Sie Nostr wie gewohnt:** Von nun an wird jede neue Aktivität (veröffentlichte Notizen, Reaktionen, verschlüsselte private Nachrichten usw.), die Sie auf Nostr durchführen, wie gewohnt an die öffentlichen Relays **und parallel dazu an Ihr Umbrel-Relay** weitergeleitet. Wenn Ihr Nostr-Client richtig konfiguriert ist, sendet er jedes Ereignis an alle Relays (einschließlich Ihres). Ihr privates Relais wird als Echtzeit-Backup fungieren. Selbst im Falle einer vorübergehenden Unterbrechung der Verbindung können Ihre Kunden dank dieses Relais die fehlenden Daten später erneut synchronisieren. So haben Sie die vollständige Kontrolle über Ihre Nostr-Daten



Im Hintergrund basiert Umbrel's _Nostr Relay_ auf dem Open-Source-Projekt **nostr-rs-relay** (Rust Protokollimplementierung). Es unterstützt das gesamte Nostr-Protokoll und zahlreiche Standard-NIPs (NIP-01, 02, 03, 09, 11, 12, 15, 16, 20, 22, 26, 28, 33, etc.), was eine maximale Kompatibilität mit den Kunden garantiert.



### noStrudel - Nostr-Client für Entdecker



![Page d'installation de noStrudel sur l'App Store Umbrel](assets/fr/03.webp)



**noStrudel** ist ein leistungsfähiger, benutzerorientierter Nostr-Webclient, der ideal ist, um das Nostr-Netzwerk im Detail zu verstehen und zu erkunden. Er ist eine Art Sandkasten, um Ereignisse und Relais zu untersuchen und mit den erweiterten Funktionen des Protokolls zu experimentieren. Interface ist in englischer Sprache verfasst und relativ technisch, was es ideal für erfahrene Benutzer macht, die neugierig auf die innere Funktionsweise von Nostr sind.



**Installation:** Installiere _noStrudel_ aus dem Umbrel App Store (Kategorie _Social_). Einmal gestartet, kann man über den Browser auf die Address von Umbrel zugreifen (z.B. `http://umbrel.local` oder über die .onion/Tailscale, siehe Abschnitt Externer Zugriff).



![Page d'accueil de noStrudel avec le bouton Setup Relays](assets/fr/04.webp)



**Relais konfigurieren:** Wenn Sie noStrudel öffnen, sehen Sie in der oberen rechten Ecke eine Schaltfläche "Relais einrichten". Klicken Sie darauf, um Ihre Relais zu konfigurieren.



![Page de configuration des relais dans noStrudel](assets/fr/05.webp)



Auf dieser Seite fügen Sie die URL Ihres Umbrel-Relais ein, die Sie zuvor kopiert haben. Sie können auch andere Relais hinzufügen, die standardmäßig von der Anwendung vorgeschlagen werden. Sobald Sie Ihre Relais konfiguriert haben, klicken Sie unten links auf "Anmelden", um fortzufahren.



![Options de connexion dans noStrudel](assets/fr/06.webp)



**Verbindung:** noStrudel bietet Ihnen mehrere Verbindungsoptionen an. In unserem Fall wählen wir "Privater Schlüssel" und fügen Ihren zuvor generierten privaten Nostr-Schlüssel ein. Wenn Sie noch keinen Schlüssel haben, können Sie die Erweiterung [Nostr Connect] (https://chromewebstore.google.com/detail/nostr-connect/ampjiinddmggbhpebhaegmjkbbeofoaj) installieren, um Ihre Nostr-Schlüssel zu erstellen und/oder zu speichern und so sicherer mit den verschiedenen Nostr-Anwendungen zu kommunizieren.



![Interface principale de noStrudel](assets/fr/07.webp)



Sobald Sie verbunden sind, können Sie noStrudel verwenden, um Ihre Notizen über Nostr zu teilen. Interface gibt Ihnen Zugang zu :





- Komplettes Nostr-Dashboard mit Zeitleiste für Notizen, Benachrichtigungen, Nachrichten, Profilsuche
- Relaismanagement und Verbindungsstatus
- Erweiterte Tools zur Untersuchung von Ereignissen und deren JSON-Inhalt
- Konfigurationsmöglichkeiten für Zeitleistenfilter und PINs



**Tipp:** Auf _noStrudel_ können Sie _Zeitlinienfilter_ einrichten oder verschiedene _NIPs (Nostr Implementation Possibilities)_ testen. Prüfen Sie zum Beispiel die Unterstützung für NIP-05 (dezentrale Identifikatoren) oder neuere Funktionen. Das macht _noStrudel_ zu einem hervorragenden Werkzeug für Experimente in einer kontrollierten Umgebung.



### Snort - Moderner Nostr-Kunde auf Umbrel



![Page d'installation de Snort sur l'App Store Umbrel](assets/fr/08.webp)



**Snort** ist ein weiterer Nostr-Webclient, der auf Umbrel verfügbar ist und eine moderne, schnelle und übersichtliche **Interface** für die Interaktion mit dem dezentralen sozialen Netzwerk bietet. Im Gegensatz zu noStrudel, das sich an Power-User richtet, zielt _Snort_ auf eine einfache Nutzung ab, ohne dabei auf Funktionalität zu verzichten. Es wurde in React entwickelt und bietet eine aufgeräumte UX, die an klassische soziale Netzwerke erinnert und somit für den täglichen Gebrauch geeignet ist.



**Installation:** Installieren Sie _Snort_ aus dem Umbrel App Store (Kategorie _Social_).



![Page d'accueil de Snort avec le bouton S'inscrire](assets/fr/09.webp)



Wenn Sie Snort öffnen, sehen Sie in der linken unteren Ecke eine Schaltfläche "Registrieren".



![Options de connexion dans Snort](assets/fr/10.webp)



Sie haben die Wahl, sich zu registrieren oder mit einem bestehenden Konto zu verbinden (was wir in diesem Lernprogramm tun werden).



![Méthodes de connexion dans Snort](assets/fr/11.webp)



Snort bietet mehrere Verbindungsmethoden an. Sie können die zuvor installierte Nostr Connect-Erweiterung oder andere verfügbare Methoden verwenden. Sobald Sie verbunden sind, können Sie die Anwendung in vollem Umfang nutzen.



Der Interface von _Snort_ bietet :





- Eine Anzeige **Beiträge/Konversationen/Global**, um zwischen Ihren Notizen, Diskussionssträngen oder dem globalen Feed zu navigieren
- Registerkarten für **Benachrichtigungen**, **Nachrichten** (DM), **Suche**, **Profil**, usw.
- Eine **+** oder _Schreiben_ Schaltfläche, um eine neue Notiz zu veröffentlichen
- Verwaltung von **Abonnements (folgende)** und **Listen**
- Menü für die Relaisverwaltung zum Hinzufügen/Entfernen von Relais und zur Überwachung ihrer Verfügbarkeit



**Empfohlene Relaiskonfiguration:** Um Ihr Umbrel-Relais hinzuzufügen, gehen Sie zu Einstellungen - Relays. Geben Sie die URL Ihres Relais (`ws://umbrel:4848` oder eine andere URL, abhängig von Ihrer Konfiguration) in die Liste der Relais von Snort ein. Auf diese Weise wird Snort Ihre Notizen auf Ihrem privaten Relais zusätzlich zu den öffentlichen veröffentlichen.



### Nostr Wallet Connect - Verbinden Sie Ihren Lightning Wallet mit Nostr



**Nostr Wallet Connect (NWC)** ist eine Anwendung, die **Ihren Umbrel (Lightning)**-Knoten mit kompatiblen Nostr-Anwendungen verbindet, um Lightning-Zahlungen zu tätigen (z.B. das Versenden von _zaps_, diesen Mikro-Zahlungen für das "Liken" von Inhalten). In diesem Tutorial schauen wir uns an, wie man noStrudel mit seinem Lightning-Knoten verbindet, um Zahlungen direkt vom Interface aus zu tätigen.



**Installation und Konfiguration:**



![Page d'installation de Nostr Wallet Connect sur l'App Store Umbrel](assets/fr/12.webp)



Installieren Sie _Nostr Wallet Connect_ aus dem Alby Store auf Umbrel.



![Configuration de NWC dans noStrudel - Étape 1](assets/fr/13.webp)



In noStrudel klickst du oben rechts auf dein Profil und dann auf die Schaltfläche "Verwalten".



![Configuration de NWC dans noStrudel - Étape 2](assets/fr/14.webp)



Klicken Sie auf "Lightning" und dann auf "Wallet verbinden".



![Configuration de NWC dans noStrudel - Étape 3](assets/fr/15.webp)



Wählen Sie unter den verfügbaren Verbindungsoptionen "Umbrel".



![Configuration de NWC dans noStrudel - Étape 4](assets/fr/16.webp)



Klicken Sie auf "Verbinden", um automatisch zu Ihrer Umbrel Nostr Wallet Connect-Sitzung weitergeleitet zu werden.



![Page de configuration des autorisations NWC](assets/fr/17.webp)



Auf der Seite Nostr Wallet Connect können Sie :




   - Legen Sie Ihr maximales Budget fest
   - Berechtigungen validieren
   - Legen Sie eine Ablaufzeit für die Verbindung fest


Klicken Sie auf "Verbinden", um den Vorgang abzuschließen.



![Confirmation de connexion dans noStrudel](assets/fr/18.webp)



Sie werden zu noStrudel mit einer Bestätigungsnachricht weitergeleitet: Sie können jetzt die ganze Welt von Ihrem Wallet/LND-Knoten aus zappen!



Dank NWC starten Ihre **Lightning-Zahlungen über Nostr** (Zaps zu Reward-Posts, _Value for Value_-Zahlungen usw.) von **Ihrem eigenen Knotenpunkt**. Sie müssen Ihre Transaktionen nicht mehr über externe Dienste leiten oder jedes Mal einen QR-Code von Ihrem Telefon scannen. Die Benutzererfahrung wird erheblich verbessert, während sie gleichzeitig _nicht verwahrend_ und datenschutzfreundlich bleibt.



Wenn du wissen willst, wie du deinen eigenen Lightning-Knoten auf Umbrel einrichten kannst, empfehle ich dir, dir dieses andere umfassende Tutorial anzusehen:



https://planb.network/tutorials/node/lightning-network/umbrel-lnd-b12e0b5b-12ff-45f1-978e-62f4b4a8ba16

## Erweiterte Konfiguration und Sicherheit



Der gemeinsame Einsatz von Umbrel und Nostr auf fortgeschrittenem Niveau erfordert besondere Aufmerksamkeit für **Sicherheit** und **Konnektivität**. Hier sind einige Tipps, wie Sie Ihre Konfiguration schützen und optimal darauf zugreifen können, egal wo Sie sich befinden.



### Sicherer externer Zugang: Tor und Tailscale



Aus Sicherheitsgründen ist dein Umbrel standardmäßig nur in deinem lokalen Netzwerk (und über Tor) zugänglich. Um mit Nostr außer Haus zu interagieren, hast du zwei bevorzugte Lösungen: **Tor** (anonymer Zugang über das Zwiebel-Netzwerk) und **Tailscale** (privates VPN-Netz).





- **Zugang über Tor:** Umbrel konfiguriert automatisch einen **Tor-Dienst (.onion)** für sein Interface Web und seine Anwendungen. Das bedeutet, dass du mit dem Tor-Browser von überall aus auf Interface Umbrel (einschließlich *noStrudel* oder *Snort*) zugreifen kannst, ohne deine öffentliche IP preiszugeben. *Mit Tor kannst du von außerhalb deines lokalen Netzwerks auf deine Umbrel-Dienste zugreifen, ohne dein Gerät dem Internet auszusetzen ([Tor auf deinem System einrichten - Anleitungen - Umbrel Community](https://community.umbrel.com/t/setup-tor-on-your-system/7509#:~:text=Official%20website%3A%20https%3A%2F%2Fwww)).* Um diese Option zu nutzen, gehe zu den Umbrel-Einstellungen und rufe die .onion-URL deines Umbrel ab (oder scanne den mitgelieferten QR-Code). Rufe mit einem Tor-Browser diese .onion Address auf: Du erhältst die gleiche Interface wie lokal.


**Nostr-Relay über Tor:** Wenn du möchtest, dass dein Nostr-Relay über Tor für deine Kunden (oder autorisierte Freunde) erreichbar ist, ist das möglich. Umbrel stellt die .onion Address des Servers nicht direkt zur Verfügung, aber da er auf Port 4848 läuft, kannst du entweder :





    - Verwenden Sie den .onion Address von UI Umbrel und konfigurieren Sie Ihren Client so, dass er sich über diesen Interface verbindet (unpraktisch für WebSocket),





- Oder den Port 4848 als separaten Onion-Dienst bereitstellen. Das erfordert ein wenig Fummelei an der Tor-Konfiguration auf Umbrel (reserviert für fortgeschrittene Nutzer, die mit SSH vertraut sind). Alternativ kannst du auch einen **Tor-Tunnel** auf einem anderen Server einrichten, der zu Umbrel umleitet: für den persönlichen Gebrauch ist es jedoch am einfachsten, Tailscale zu benutzen.





- Zugang über **Tailscale:** [Tailscale](https://tailscale.com/) ist eine Mesh-VPN-Lösung, die ein virtuelles privates Netzwerk zwischen Ihren Geräten und Umbrel schafft. Der Vorteil: es funktioniert wie in einem LAN, aber über das Internet, verschlüsselt und ohne komplexe Konfiguration. **Tailscale weist Ihrem Umbrel eine feste IP-Adresse und einen privaten Domainnamen zu, unabhängig von seinem Standort im Netzwerk** ([Tailscale | Umbrel App Store](https://apps.umbrel.com/app/tailscale#:~:text=Tailscale%20is%20zero%20config%20VPN,reviewed%20and%20trusted%20standard)). In der Praxis können Sie, sobald Sie Tailscale auf Umbrel installiert haben (im Umbrel App Store, Kategorie *Networking*) **und** auf Ihren Geräten (Handy, PC...), Umbrel über eine Address wie `100.x.y.z` (Tailscale IP) oder einen Namen wie `umbrel.tailnet123.


für Nostr_ ist Tailscale äußerst nützlich: Ihr Handy, wenn es Tailscale aktiviert hat, kann sich mit `ws://umbrel:4848` (dank MagicDNS) oder direkt mit der Tailscale IP und Port 4848 verbinden, um das Relais zu nutzen. Clients wie Damus oder Amethyst werden Ihren Umbrel sehen, als ob er sich im selben lokalen Netzwerk befände. **Tipp:** Aktivieren Sie die **MagicDNS**-Option in Tailscale, um den Hostnamen `umbrel` zu verwenden, anstatt sich die IP zu merken. Dies gewährleistet eine reibungslose Verbindung zu deinem Relais, auch wenn du unterwegs bist ([Nostr Relay | Umbrel App Store](https://apps.umbrel.com/app/nostr-relay#:~:text=client%20%28e,That%27s%20it%21%20Your%20past)).


Darüber hinaus ermöglicht Tailscale den Zugriff auf Interface Umbrel (und damit auf die _noStrudel/Snort_-Webclients) über einen einfachen Browser, der die private IP oder den zugewiesenen Domainnamen verwendet. Es wird kein Tor-Browser benötigt und die Datenübertragungsgeschwindigkeiten sind im Allgemeinen besser als über das Tor-Netzwerk.




**Hinweis: Tor und Tailscale schließen sich nicht gegenseitig aus. Sie können Tor für den anonymen Zugang oder bestimmte Dienste aktiv halten und Tailscale wegen seiner Einfachheit im Alltag nutzen. In beiden Fällen müssen Sie keinen Port auf Ihrem Router öffnen, was die Sicherheit erhöht.**



### Absicherung Ihres Nostr-Relais (empfohlene Verfahren)



Wenn Sie ein Nostr-Relais auf Umbrel hosten, insbesondere in einem fortgeschrittenen Kontext, sollten Sie einige gute Praktiken anwenden:





- Privates oder eingeschränktes Relais: Standardmäßig ist Ihr Umbrel-Relais privat (nicht öffentlich bekannt) und wenn Sie nur über Tailscale oder Ihr LAN darauf zugreifen, bleibt es für Fremde unzugänglich. **Behalten Sie den Link vertraulich** - Verbreiten Sie ihn nicht in öffentlichen Nostr-Netzwerken, es sei denn, Sie wollen freiwillig andere Nutzer aufnehmen, was ein ganz anderes Thema ist (Moderation, Bandbreite, etc.). Für den persönlichen Gebrauch empfehlen wir, den Zugang auf Sie selbst und, falls nötig, auf einige vertrauenswürdige Freunde und Familienmitglieder zu beschränken.





- **Whitelist/Auth**: Die nostr-rs-Relay-Implementierung unterstützt einen **NIP-42**-Authentifizierungsmechanismus sowie *Whitelists* von öffentlichen Schlüsseln. Indem du diese Optionen aktivierst, kannst du dein Relay so einschränken, dass es **nur Ereignisse akzeptiert, die mit bestimmten Schlüsseln (deinen) signiert sind**, oder dass Clients sich authentifizieren müssen, um zu veröffentlichen. Um dies einzurichten, musst du die Konfigurationsdatei des Relays in Umbrel bearbeiten (via SSH im Docker-Container). Es ist eine fortgeschrittene Manipulation, aber du kannst zum Beispiel die erlaubten Anzeigen auflisten (`pubkey_whitelist`). Auf diese Weise kann jemand, der dein Relais entdeckt, dort nichts veröffentlichen, wenn er nicht auf der Liste steht.





- **Updates und Wartung:** Halten Sie Ihr Umbrel und die *Nostr Relay* App auf dem neuesten Stand. Updates können Leistungsverbesserungen (z.B. bessere Spam-Behandlung) und Sicherheitskorrekturen beinhalten. Überprüfen Sie auf Umbrel regelmäßig den App Store auf Updates für *Nostr Relay* und wenden Sie diese bei Bedarf an.





- Überwachung und Grenzen: Behalten Sie im Auge, wie Ihr Relais genutzt wird. Wenn Sie es für andere öffnen, behalten Sie die Last (CPU/RAM-Speicher) auf Ihrem Umbrel im Auge, da ein Relais schnell eine Menge Daten ansammeln kann. nostr-rs-relay bietet konfigurierbare **Raten- und Speichergrenzen** (`Limits` in der Konfiguration, z.B. Anzahl der Ereignisse pro Sekunde, maximale Ereignisgröße, Löschen alter Ereignisse...). Für den privaten Gebrauch werden Sie diese wahrscheinlich nicht brauchen, aber seien Sie sich bewusst, dass diese Parameter existieren, wenn Sie sie brauchen ([nostr-rs-relay/config.toml at master - scsibug/nostr-rs-relay - GitHub](https://github.com/scsibug/nostr-rs-relay/blob/master/config.toml#:~:text=)).





- **Sichern von Nostr-Schlüsseln:** Dieser Punkt wurde bereits erwähnt, ist aber entscheidend: Geben Sie Ihre privaten Nostr-Schlüssel niemals in einen Interface ein, dem Sie nicht völlig vertrauen. Verwenden Sie stattdessen Browser-Erweiterungen oder externe Geräte (wie Nostr *signers* auf separaten Telefonen), um sensible Aktionen zu signieren. Auf Umbrel können Ihre Web-Clients wie *Snort* und *noStrudel* über NIP-07 arbeiten, ohne Ihren geheimen Schlüssel zu kennen. Nutzen Sie diese Gelegenheit, um Komfort und Sicherheit zu kombinieren.




Wenn Sie diese Tipps befolgen, wird Ihre Integration eines Umbrel-Knotens mit Nostr sowohl leistungsstark **als auch** sicher sein. Sie werden eine komplette Umgebung haben: einen Bitcoin Knoten für Lightning-Zahlungen, ein privates Nostr-Relay für Datenhoheit und leistungsstarke Nostr-Webclients, um in diesem neuen dezentralen sozialen Netzwerk zu navigieren. Viel Spaß beim Erkunden von Nostr mit Umbrel!