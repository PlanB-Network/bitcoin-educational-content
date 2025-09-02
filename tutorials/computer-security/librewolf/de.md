---
name: LibreWolf
description: Wie man den LibreWolf-Datenschutzbrowser benutzt
---

![cover](assets/cover.webp)



Jeder Klick, jede Suche, jede besuchte Website: Ihr Webbrowser ist zu einem raffinierten Spitzel geworden, der ein globales kommerzielles Überwachungssystem speist. Google Chrome, das von über 3 Milliarden Menschen genutzt wird, verwandelt Ihr tägliches Surfen in lukrative Daten für die Werbegiganten. Sogar Firefox, trotz seines Rufs als "ethischer" Browser, aktiviert standardmäßig Telemetriemechanismen, die Ihre Surfgewohnheiten an Mozilla übermitteln.



Diese Realität wirft eine wichtige Frage auf: Ist es noch möglich, frei im Internet zu surfen, ohne ständig ausspioniert zu werden und Profile zu erstellen? Glücklicherweise lautet die Antwort "ja", dank Gemeinschaftsprojekten, die den Nutzer wieder in den Mittelpunkt ihrer Überlegungen stellen.



LibreWolf verkörpert diese Philosophie des digitalen Widerstands. Dieser Browser wurde von einer Gemeinschaft unabhängiger Entwickler entwickelt und verwandelt Firefox in ein wahres Schutzschild gegen Online-Überwachung. Wo kommerzielle Browser versuchen, Ihre Aufmerksamkeit zu monetarisieren, macht LibreWolf das Gegenteil: Er macht Sie für Tracker unsichtbar und bewahrt gleichzeitig ein flüssiges, modernes Browsing-Erlebnis.



In diesem Tutorial werden wir entdecken, wie LibreWolf die Art und Weise, wie Sie im Internet surfen, verändern kann, indem es einen robusten Schutz gegen Tracking bietet, ohne die Leistung oder Webkompatibilität zu beeinträchtigen.



![LIBREWOLF](assets/fr/01.webp)


*Marktanteil der Webbrowser: Chrome dominiert mit 65 % des Marktes, gefolgt von Safari und Edge. Diese Vorherrschaft wirft Fragen zur Webvielfalt und zum Datenschutz auf*



## Wir stellen vor: LibreWolf



**FreeWolf** ist ein von Mozilla Firefox abgeleiteter Open-Source-Webbrowser, der von einer unabhängigen Gemeinschaft von Liebhabern freier Software entwickelt und gepflegt wird. Sein Hauptziel ist es, einen Browser anzubieten, der sich auf die Privatsphäre, Sicherheit und Freiheit des Nutzers konzentriert.



Konkret nutzt LibreWolf die Gecko-Engine von Firefox, allerdings mit einer völlig anderen Philosophie: Während Firefox ein Gleichgewicht zwischen Privatsphäre und Benutzerfreundlichkeit herstellen muss, setzt LibreWolf standardmäßig auf die Privatsphäre. Das Projekt entfernt alles, was Ihre Privatsphäre verletzen könnte (Telemetrie, Datensammlung, gesponserte Module) und integriert gleichzeitig erweiterte Sicherheitseinstellungen.



### Zielsetzung: Privatsphäre und Freiheit



LibreWolf zielt darauf ab, den Schutz vor Tracking und Fingerprinting zu maximieren und gleichzeitig die Browsersicherheit zu erhöhen. Seine wichtigsten Ziele sind:





- Beseitigen Sie alle Telemetrie und Datenerfassung** in Firefox
- Deaktivieren Sie Funktionen, die der Benutzerfreiheit** zuwiderlaufen, wie z. B. proprietäre DRM-Module
- Anwendung von Datenschutz-/Sicherheitseinstellungen** und spezifischen Patches von Anfang an
- Die gemeinschaftliche Entwicklung garantiert Transparenz und Unabhängigkeit** von kommerziellen Interessen



Kurz gesagt, LibreWolf präsentiert sich als "Firefox, wie er gewesen wäre, wenn der Datenschutz oberste Priorität hätte" - ein Browser, der Sie standardmäßig respektiert, ohne dass eine zusätzliche Konfiguration erforderlich ist.



### Hauptmerkmale



Von Anfang an bietet LibreWolf eine Reihe von datenschutzorientierten Funktionen:



**Keine Telemetrie oder Datensammlung:** Anders als Chrome oder Firefox, die bestimmte Nutzungsstatistiken senden, sammelt LibreWolf absolut nichts von Ihrem Surfverhalten. Keine Absturzberichte, keine Nutzerstudien, keine gesponserten Vorschläge.



**LibreWolf integriert von Haus aus die uBlock Origin-Erweiterung, einen der besten Werbeblocker und Tracker auf dem Markt. Standardmäßig filtert LibreWolf aggressiv alles heraus, was Sie online verfolgen könnte (aufdringliche Werbung, Tracking-Skripte, Kryptowährung Mining).



**Standardmäßig private Suchmaschine:** LibreWolf verwendet standardmäßig DuckDuckGo als erste Suchmaschine, die keinen Verlauf Ihrer Suchanfragen speichert. Andere datenschutzorientierte Alternativen (Searx, Qwant, Whoogle) sind ebenfalls verfügbar.



**Verstärkter Anti-Fingerprint-Schutz:** Fingerprinting ermöglicht es, einen Browser über seine Konfiguration eindeutig zu identifizieren, auch ohne Cookies. Um dem entgegenzuwirken, aktiviert LibreWolf die RFP-Technologie (Resist Fingerprinting) des Tor-Projekts, um Ihren Browser so generisch wie möglich zu machen. Tests zeigen, dass ein Standard-Firefox bei Tools wie coveryourtracks.eff.org zu ~90% eindeutig identifizierbar ist, während es bei LibreWolf nur ~10-20% sind (diese Zahlen sind Richtwerte und können je nach Software- und Hardwarekonfiguration und installierten Erweiterungen variieren).



![LIBREWOLF](assets/fr/07.webp)


*EFF-Testseite [Cover Your Tracks] (https://coveryourtracks.eff.org/) mit der Schaltfläche TEST YOUR BROWSER. Diese Seite wird verwendet, um den Schutz vor Trackern und Fingerabdrücken zu testen



![LIBREWOLF](assets/fr/08.webp)


*Cover Your Tracks Testergebnis. Die Meldung "Sie haben einen starken Schutz gegen Web-Tracking" wird angezeigt, was die Wirksamkeit des LibreWolf.*-Schutzes zeigt



**LibreWolf aktiviert standardmäßig die strengen Sicherheitseinstellungen. Der erweiterte Tracking-Schutz von Firefox wird auf die Stufe Streng gestellt, um Tausende von Trackern, Cookies von Drittanbietern und bösartige Inhalte zu blockieren. Er aktiviert auch die Isolierung von Websites und Cookies (*Total Cookie Protection*), um Daten für jede Domain zu partitionieren, und schränkt WebRTC ein (Begrenzung von *ICE-Kandidaten* und Weiterleitung über einen Proxy, wenn ein Proxy vorhanden ist), um das Risiko eines IP Address-Lecks zu verringern.



**Schnelle Engine-Updates:** Das Projekt verfolgt die Entwicklungen von Firefox sehr genau: LibreWolf basiert immer auf der neuesten stabilen Version von Firefox, und die Betreuer bemühen sich, eine neue Version innerhalb von 24 bis 72 Stunden nach jedem offiziellen Firefox-Release zu veröffentlichen.



## Vorteile und Nachteile



### Vorteile





- Keine Telemetrie oder unerwünschte Verbindungen:** LibreWolf überträgt keine Nutzungsdaten, so dass Ihre Privatsphäre vollständig geschützt ist.





- Open-Source und Community-basiert:** Das Projekt ist zu 100% Open-Source und wird von Freiwilligen gepflegt. Diese Unabhängigkeit garantiert, dass kein Werbemodell die Entwicklung beeinflussen wird.





- Vorkonfiguriert für den Datenschutz:** LibreWolf spart Ihnen wertvolle Zeit: Sie müssen nicht stundenlang Firefox-Einstellungen vornehmen, alles ist bereits erledigt.





- Nativer Werbeblocker/Tracker:** uBlock Origin ist standardmäßig integriert, sodass Sie nichts tun müssen, um sich vor Werbung und Fehlern zu schützen.





- Hervorragender Schutz vor Fingerabdrücken:** Dank RFP und zahlreicher Privatsphäre-Einstellungen reduziert LibreWolf Ihren einzigartigen digitalen Fußabdruck im Internet drastisch.





- Verbesserte Leistung und geringes Gewicht:** Durch das Entfernen von Telemetrie und bestimmten unwichtigen Funktionen kann LibreWolf etwas schneller und weniger stromhungrig sein als der Standard-Firefox.



### Nachteile und Einschränkungen





- Keine eingebauten automatischen Updates:** LibreWolf aktualisiert sich nicht selbst. Es liegt an Ihnen, neue Versionen zu installieren, sobald sie veröffentlicht werden, um sicher zu sein.





- Eingeschränkte Kompatibilität mit bestimmten Diensten:** Aufgrund seiner sehr strengen Einstellungen kann LibreWolf auf bestimmten Webseiten auf Probleme stoßen. Netflix und Disney+ Streaming-Plattformen werden nicht funktionieren, da LibreWolf Widevine DRM standardmäßig deaktiviert.





- Kein eingebautes anonymes Netzwerk:** Im Gegensatz zum Tor-Browser leitet LibreWolf den Datenverkehr nicht von sich aus über Tor oder ein VPN. Wenn Sie Netzwerkanonymität benötigen, müssen Sie manuell einen Proxy/VPN konfigurieren.





- Nicht persistente Cookies und Sitzungen (Standard):** Aus Gründen der Vertraulichkeit löscht LibreWolf Cookies, Verlauf und Daten der Seite jedes Mal, wenn Sie Ihren Browser schließen. Sie müssen sich jedes Mal neu in Ihre Konten einloggen.





- Keine mobile Version oder Cloud-Synchronisation:** LibreWolf ist nur auf dem Desktop verfügbar (Windows, Linux, macOS). Es gibt keine mobile Anwendung und daher keine Synchronisation von Konten oder Lesezeichen über eine Cloud.



## Installation von LibreWolf



**Offizielle Website:** [librewolf.net](https://librewolf.net)



LibreWolf ist für alle wichtigen Desktop-Betriebssysteme verfügbar: Linux, Windows und macOS. Um LibreWolf herunterzuladen, besuchen Sie die offizielle Website:



![LIBREWOLF](assets/fr/02.webp)


*Die LibreWolf-Homepage (librewolf.net) zeigt das Browser-Logo, einen blauen Installieren-Knopf und die Links zu Quellcode und Dokumentation. Ein großer blauer Pfeil zeigt auf die Schaltfläche Installieren*



Klicken Sie auf die Schaltfläche "Installation", um detaillierte Anweisungen für Ihr Betriebssystem aufzurufen:



![LIBREWOLF](assets/fr/03.webp)


*Betriebssystem-Auswahlseite für den LibreWolf.* Download



Die Installation hängt von Ihrem Betriebssystem ab:



### Unter Linux


LibreWolf bietet Builds für viele Distributionen an. Für Debian/Ubuntu und Derivate ist ein offizielles APT-Repository verfügbar. Alternativ dazu wird LibreWolf in Flatpak auf Flathub veröffentlicht:


```
flatpak install flathub io.gitlab.librewolf-community
```



### Unter Windows


Laden Sie das Installationsprogramm (.exe) von der offiziellen Website herunter oder verwenden Sie das:




- Chocolatey:** `choco install librewolf`
- WinGet:** `winget install librewolf`



### Unter macOS


LibreWolf ist als .dmg-Paket für Mac verfügbar. Laden Sie das Disk-Image von der offiziellen Website herunter und ziehen Sie die LibreWolf-Anwendung per Drag & Drop in Ihren Anwendungsordner. Alternativ können Sie es auch über Homebrew installieren.




## Konfiguration und erste Verwendung



Beim ersten Start werden Sie den vertrauten Firefox Interface bemerken, nur dass er etwas reduzierter ist: Die Startseite enthält nur die Suchleiste und keine gesponserten Vorschläge. Sie sehen das uBlock Origin-Symbol in der Symbolleiste - ein Zeichen dafür, dass der Blocker aktiv ist.



![LIBREWOLF](assets/fr/04.webp)


*LibreWolf-Startseite mit Erweiterungen und Menü. Ein blauer Pfeil in der oberen rechten Ecke zeigt das Menü-Symbol an (drei horizontale Balken)



LibreWolf lädt Ihre Seiten automatisch im "Strict"-Modus (Anti-Tracking), und die Standard-Suchmaschine ist DuckDuckGo. Sie können versuchen, eine Tracking-Testseite (z.B. amiunique.org) zu besuchen, um den exponierten Fußabdruck zu beobachten - er sollte viel generischer sein als bei einem Standardbrowser.



### Datenschutz-Einstellungen



LibreWolf ist bereits optimal für den Datenschutz konfiguriert. Unter Menü → Optionen → Datenschutz & Sicherheit sehen Sie, dass LibreWolf auf den Modus "Erweiterter Tracking-Schutz" eingestellt ist: Streng. Dieser Modus blockiert:




- Standortübergreifende Tracker
- Cookies von Dritten
- Bekannte Tracking-Inhalte
- Kryptomining
- Digitale Fingerabdruckdetektoren



![LIBREWOLF](assets/fr/05.webp)


*Die Registerkarte Sicherheit und Datenschutz zeigt die Sicherheitseinstellungen von LibreWolf.*



WebRTC ist deaktiviert (um IP-Lecks zu verhindern), und der vollständige Cookie-Schutz ist aktiviert. Telemetrie und Firefox-Umfragen sind vollständig deaktiviert.



### Cookie- und Verlaufsverwaltung



Standardmäßig löscht LibreWolf die Cookies und den lokalen Speicher jedes Mal, wenn er geschlossen wird. Wenn Sie dieses Verhalten stört, können Sie es unter Datenschutz & Sicherheit → Cookies und Standortdaten anpassen, indem Sie das Häkchen bei "Cookies und Standortdaten beim Schließen von LibreWolf löschen" entfernen.



![LIBREWOLF](assets/fr/06.webp)


*Dieselbe Seite etwas weiter unten, mit der Option, Cookies zu löschen, wenn der Browser geschlossen wird*



### Hinzufügen nützlicher Erweiterungen



Grundsätzlich rät LibreWolf davon ab, unnötige Erweiterungen hinzuzufügen, da jede Erweiterung ein Tracking-Vektor sein kann. Dennoch können einige seriöse Erweiterungen Ihre Erfahrung verbessern:




- Firefox Multi-Account Containers** (von Mozilla) für die Aufteilung des Browsens in verschiedene Bereiche
- Decentraleyes** oder **LocalCDN**, um gemeinsame Bibliotheken lokal zu bedienen



Vermeiden Sie insbesondere "kostenlose VPN"-Erweiterungen oder dubiose Proxys - uBlock Origin deckt bereits 99 % Ihrer Bedürfnisse ab.



## Alltäglicher Gebrauch



### Tägliches Surfen im Internet


Benutzen Sie LibreWolf für Ihre alltäglichen Internetaktivitäten. Der große Unterschied zu anderen Browsern ist, dass Sie viel weniger Werbespuren hinterlassen. Dank der Filterlisten von uBlock verschwinden "Accept cookie"-Banner auf vielen Websites.



### Verwenden Sie private Registerkarten zur Unterteilung


Auch wenn LibreWolf am Ende der Sitzung alles löscht, kann es nützlich sein, für bestimmte Aufgaben während der Sitzung ein privates Browserfenster (Strg+Umschalt+P) zu öffnen, um eine bestimmte Identität abzuschotten.



### Nutzen Sie die Vorteile von Multi-Account-Containern


Die Installation der Erweiterung Multi-Account Containers kann Ihnen helfen, Ihre Aktivitäten in wasserdichte Silos zu unterteilen. Sie können zum Beispiel einen "Banking"-Container für Ihre Bank-Websites definieren, einen "Social Networks"-Container für Facebook/Twitter usw. Jeder Container hat seine eigenen Cookies, Sitzungen und isolierten Speicher. Jeder Container verfügt über seine eigenen Cookies, Sitzungen und isolierten Speicherplatz.



### Feinabgestimmte Verwaltung von Berechtigungen nach Standort


Mit LibreWolf können Sie die Berechtigungen, die Sie Websites geben (Standort, Kamera, Mikrofon, Benachrichtigungen), von Fall zu Fall kontrollieren. Erteilen Sie Berechtigungen nur an Websites, denen Sie vertrauen und wo es notwendig ist.



## Bewährte Praktiken mit LibreWolf



1. **Halten Sie LibreWolf auf dem neuesten Stand:** Prüfen Sie die Seite regelmäßig auf neue Versionen, besonders nach einer stabilen Firefox-Version.



2. **Vermeiden Sie die Vermischung von persönlicher Identität und privatem Browsing:** Idealerweise sollten Sie sich nicht mit Ihren persönlichen Konten in derselben Sitzung anmelden, in der Sie sensible Recherchen durchführen.



3. **Überladen Sie LibreWolf nicht mit überflüssigen Erweiterungen:** Jede Erweiterung, die Sie installieren, kann Sicherheits- oder Fingerprinting-Risiken mit sich bringen.



4. **Benutzen Sie zusätzlich ein VPN oder einen Tor-Proxy:** LibreWolf macht Sie nicht anonym gegenüber Ihrem Internetanbieter. Für Anonymität im Netzwerk können Sie LibreWolf hinter einem vertrauenswürdigen VPN verwenden.



5. **Sichern Sie Ihre wichtigen Daten:** Lesezeichen, Passwörter, falls lokal gespeichert. Ziehen Sie einen externen Passwort-Manager (KeePassXC, Bitwarden) in Betracht, anstatt den grundlegenden Passwort-Manager des Browsers zu verwenden.



## Vergleich mit anderen Browsern



LibreWolf ist Teil des "Werkzeugkastens" der datenschutzorientierten Browser:



**LibreWolf vs. Firefox:** LibreWolf wird bereits gehärtet und ohne Telemetrie ausgeliefert. Firefox behält den Vorteil der Synchronisierung mehrerer Geräte und einer sehr großen Nutzerbasis, erfordert aber eine manuelle Konfiguration, um den Grad der Vertraulichkeit von LibreWolf zu erreichen.



**Brave verwendet Chrome/Chromium-Code und integriert ein Geschäftsmodell über sein optionales Werbeprogramm. LibreWolf, als Community Fork für Firefox, behält Mozillas freies Ökosystem bei und hat keine Verbindungen zu Google.



**LibreWolf vs. Tor-Browser:** Der Tor-Browser ist unersetzlich für die Anonymität im Angesicht starker Überwachung, aber er ist langsam und unkomfortabel im täglichen Gebrauch. LibreWolf, für das alltägliche Surfen im klassischen Web, ist viel schneller und praktischer.



**LibreWolf vs. Mullvad Browser:** Mullvad Browser geht sogar noch weiter in der Standardisierung, aber auf Kosten einer reduzierten Benutzerfreundlichkeit (es ist unmöglich, ein Login-Cookie zu behalten). LibreWolf schafft ein Gleichgewicht: sehr privat, aber im Alltag nutzbar.



## Schlussfolgerung



LibreWolf ist eine hervorragende Lösung für alle, die einen ultra-privaten "Alltags"-Browser suchen, ohne dabei die extreme Anonymität von Tor zu erreichen. Er ist die ideale Wahl für Aktivisten, Journalisten, Entwickler oder Power-User, die klassisch im Internet surfen wollen (schnell, kompatibel mit modernen Websites) und gleichzeitig dem Ad-Tracking und Big Tech entgehen wollen.



Trotz gewisser Einschränkungen (keine automatischen Updates, eingeschränkte Kompatibilität mit bestimmten Diensten) ist LibreWolf ein wertvolles Werkzeug für alle, die die Kontrolle über ihre digitale Privatsphäre zurückgewinnen wollen. Seine Benutzerfreundlichkeit und die Standardkonfiguration machen es zu einer klugen Wahl für datenschutzbewusste Benutzer.



## Ressourcen



### Offizielle Dokumentation




- [LibreWolf offizielle Website](https://librewolf.net)
- [Quellcode auf Codeberg](https://codeberg.org/librewolf)
- [Offizielle FAQ](https://librewolf.net/docs/faq)



### Leitfäden und Vergleiche




- [Privacy Guides](https://www.privacyguides.org/en/desktop-browsers/)
- [Vergleichende Tests zum Schutz der Privatsphäre] (https://privacytests.org)



### Unterstützung durch die Gemeinschaft




- [Subreddit r/LibreWolf](https://www.reddit.com/r/LibreWolf/)
- [Canal Matrix LibreWolf](https://matrix.to/#/#librewolf:matrix.org)