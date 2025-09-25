---
name: Mullvad Browser
description: Wie man den Mullvad-Browser für den Datenschutz nutzt
---

![cover](assets/cover.webp)



In einer Welt, in der die digitale Überwachung allgegenwärtig ist, war der Schutz Ihrer Privatsphäre im Internet noch nie so wichtig wie heute. Unternehmen nutzen ausgeklügelte Techniken, um Sie zu verfolgen:





- **Cookies von Drittanbietern**: kleine Dateien, die von externen Websites hinterlegt werden, um Ihnen von einer Website zur anderen zu folgen
- **Fingerprinting**: sammelt einzigartige Merkmale Ihres Browsers und Geräts (Bildschirmauflösung, installierte Schriftarten, Plugins usw.), um Sie ohne Cookies zu identifizieren
- **Tracking-Skripte**: unsichtbare JavaScript-Codes, die Ihr Surfverhalten analysieren (Klicks, Scrollen, Verweildauer)
- **IP Address-Analyse**: geografischer Standort und Identifizierung Ihres Internetanbieters



Diese Daten werden dann kombiniert, um detaillierte Profile Ihres Online-Verhaltens zu erstellen und zu Geld zu machen, oft ohne Ihr Wissen. Diese Realität wirft eine grundlegende Frage auf: Wie können Sie im Internet surfen und gleichzeitig Ihre Anonymität und Vertraulichkeit wahren?



Die Antwort liegt weitgehend in der Wahl Ihres Webbrowsers. Dieses Werkzeug, das wir jeden Tag benutzen, um auf Informationen zuzugreifen, Einkäufe zu tätigen oder zu kommunizieren, spielt eine entscheidende Rolle beim Schutz unserer persönlichen Daten. Leider sind beliebte Browser wie Google Chrome (der etwa 65 % des Weltmarkts hält) auf Geschäftsmodelle ausgelegt, die auf der massiven Sammlung von Nutzerdaten basieren.



![MULLVAD BROWSER](assets/fr/01.webp)


*Mullvad Browser zeichnet sich durch eine außergewöhnlich effektive Tracker-Blockierung aus, die die von Consumer-Browsern weit übertrifft*



Angesichts dieser Herausforderung tauchen neue Anbieter auf, die eine andere Philosophie verfolgen: Sie stellen die Privatsphäre in den Mittelpunkt ihres Designs. Unter ihnen sticht Mullvad Browser als innovative Lösung hervor, die den besten Schutz der Privatsphäre mit einem flüssigen, zugänglichen Browsing-Erlebnis kombiniert.



Im Gegensatz zu herkömmlichen Browsern, die versuchen, Ihre Erfahrung durch das Sammeln Ihrer Daten zu personalisieren, verfolgt Mullvad Browser den gegenteiligen Ansatz: Er lässt alle seine Benutzer auf den Websites identisch erscheinen, was ein individuelles Tracking praktisch unmöglich macht.



In diesem Tutorial werden wir gemeinsam entdecken, wie Mullvad Browser die Art und Weise, wie Sie im Internet surfen, verändern kann und Ihnen einen robusten Schutz vor Überwachung bietet, ohne dass Sie auf Benutzerfreundlichkeit verzichten müssen.




## Einführung in den Mullvad Browser



**Der Mullvad Browser** ist ein auf Datenschutz ausgerichteter Webbrowser, der in Zusammenarbeit mit dem Tor-Projekt entwickelt und vom schwedischen Unternehmen Mullvad VPN kostenlos verteilt wird. Er wurde im April 2023 auf den Markt gebracht und präsentiert sich als **"Tor-Browser ohne das Tor-Netzwerk"**. Er wurde entwickelt, um Online-Tracking und Fingerabdrücke zu minimieren, während er es den Nutzern ermöglicht, über ein vertrauenswürdiges VPN und nicht über das Tor-Netzwerk zu surfen.



Mullvad Browser ist ein freier, quelloffener Browser, der auf Firefox ESR (der langlebigen Version von Mozilla Firefox) basiert und von Experten des Tor-Projekts gehärtet wurde. Konkret beinhaltet er die meisten **Schutzfunktionen des Tor-Browsers**, leitet aber **den Datenverkehr nicht über das Tor-Netzwerk**. Stattdessen können (und sollten) Nutzer ihn mit einem vertrauenswürdigen, verschlüsselten VPN verbinden, um ihre IP Address zu anonymisieren.



In Bezug auf die Benutzerfreundlichkeit ähnelt Mullvad Browser einem klassischen Browser und bietet eine flüssige Navigation. Er ist kostenlos für Windows, macOS und Linux verfügbar (keine mobile Version). Sie müssen kein Mullvad VPN-Abonnent sein, um ihn zu nutzen; allerdings bietet **die Nutzung von Mullvad Browser ohne Maskierung Ihrer IP keine vollständige Anonymität** - daher wird dringend empfohlen, ihn in Verbindung mit einem zuverlässigen VPN zu nutzen.



### Ziele: Datenschutz und Anti-Tracking



Der Mullvad-Browser wurde mit einem Hauptziel vor Augen entwickelt: **Schutz der Privatsphäre des Nutzers** im Internet und Bekämpfung gängiger Tracking- und Profiling-Techniken. Zu seinen Hauptzielen gehören:





- Verringern Sie drastisch die Verfolgung von Werbung und **Tracking** durch Websites und Werbeagenturen. Mullvad Browser blockiert standardmäßig Tracker von Drittanbietern, Tracking-Cookies und Fingerprinting-Skripte, die Sie identifizieren könnten.





- Standardisieren Sie den Fingerabdruck Ihres Browsers, um **"in der Masse unterzugehen"**. Der Fingerabdruck ist wie ein einzigartiger "Personalausweis", der durch die Kombination aller Merkmale Ihres Browsers erstellt wird. Mullvad Browser stellt sicher, dass alle seine Benutzer genau den gleichen "Personalausweis" haben, so dass es unmöglich ist, sie individuell zu unterscheiden.





- Bietet sofortigen Schutz ohne zusätzliche Erweiterungen. Mullvad Browser wird in einer "gebrauchsfertigen" Konfiguration geliefert: Der Benutzer muss weder eine Reihe von Erweiterungen installieren noch irgendwelche Einstellungen ändern, um geschützt zu sein.





- Verzichten Sie nicht mehr als nötig auf Leistung oder **Ergonomie**. Ohne Tor-Routing bietet Mullvad Browser ein viel schnelleres Surfen als Tor Browser und nähert sich der Leistung eines Standard-Browsers in Verbindung mit einem VPN.



### Die wichtigsten Merkmale von Mullvad Browser



Mullvad Browser enthält eine Reihe von **Sicherheits- und Datenschutzfunktionen**, die direkt vom Tor Browser inspiriert sind:





- **Privates Browsing zu jeder Zeit:** Der private Browsing-Modus ist standardmäßig aktiviert und kann nicht deaktiviert werden. **Es wird kein Verlauf, keine Cookies und kein Cache von einer Sitzung zur nächsten gespeichert**. Sobald Sie Mullvad Browser schließen, werden alle Browsing-Daten gelöscht.





- **Verbesserter Schutz vor Fingerabdrücken:** Der Browser wendet strenge Einstellungen an, um digitale Fingerabdrücke zu vereiteln. Dies beinhaltet:
- Standardisierung von **Benutzeragent** und Browserversion
- Zeitzone für alle Benutzer auf **UTC** eingestellt
- **Letterboxing**: eine Technik, die automatisch graue Ränder um Webseiten herum einfügt, um die Anzeigegröße zu standardisieren und eine Identifizierung anhand der Bildschirmabmessungen zu verhindern
- **Blockieren von Fingerprinting-APIs**: Die Technologien Canvas (2D-Zeichnen), WebGL (3D-Grafik) und AudioContext (Audioverarbeitung) sind deaktiviert, da sie einzigartige Details über Ihre Hardware preisgeben können
- Standardisierte Systemschriftarten, um eine Identifizierung durch installierte Schriftarten zu vermeiden





- **Blockieren von Trackern und Werbung:** Mullvad Browser integriert von Haus aus die Erweiterung **uBlock Origin** (vorinstalliert) mit zusätzlichen Schutzlisten zum Blockieren von **Drittanbieter-Trackern, Werbeskripten und anderen bösartigen Inhalten**. Dieser Schutz wird von der **First-Party-Isolation** begleitet: eine Technik, die Cookies in separaten "Töpfen" für jede Website speichert und so verhindert, dass eine Website die von einer anderen hinterlegten Cookies lesen kann.





- Schaltfläche zum Zurücksetzen der Sitzung: Wie die Schaltfläche "Neue Identität" von Tor Browser bietet Mullvad Browser eine Schaltfläche zum **schnellen Neustart des Browsers mit einer neuen, leeren Sitzung**.





- **Einstellbare Sicherheitsstufen:** Du kannst die Sicherheitsstufe (*Normal*, *Safer*, *Safest*) in den Einstellungen anpassen, genau wie im Tor Browser.



## Integrierte Erweiterungen als Standard



Mullvad Browser enthält **drei vorinstallierte Erweiterungen**, die den Kern seines Anti-Tracking-Schutzes bilden. **Es ist wichtig, sie niemals zu entfernen oder ihre Konfigurationen zu ändern**, da dies Sie unter den Mullvad Browser-Benutzern einzigartig machen würde:



### **uBlock Origin**


Diese Werbe- und Tracker-Blocker-Erweiterung kommt vorkonfiguriert mit **optimierten Filterlisten** zum Blockieren von:




- Aufdringliche Werbung
- Tracker von Drittanbietern, die Ihre Daten sammeln
- Bösartige Skripte
- Verhaltenskontrolle Elements



uBlock Origin in Mullvad Browser verwendet standardisierte Parameter, um sicherzustellen, dass alle Benutzer genau denselben Elements blockieren und so die Einheitlichkeit der digitalen Fußabdrücke bewahren.



### **NoScript**


NoScript läuft im Hintergrund, um die **Sicherheitsstufen** des Browsers zu verwalten. Diese:




- Steuert die Ausführung von JavaScript je nach ausgewählter Stufe (Normal/Most Secure/Most Secure)
- Filtert **XSS** (Cross-Site Scripting) Angriffe automatisch aus
- Blockiert **gefährliche** aktive Inhalte auf Nicht-HTTPS-Sites
- Das Symbol ist standardmäßig ausgeblendet, kann aber über "Symbolleiste anpassen" angezeigt werden



### *Erweiterung* **Mullvad Browser**


Diese Mullvad-spezifische Erweiterung bietet unterschiedliche Funktionalitäten, je nachdem, ob Sie Mullvad VPN-Kunde sind oder nicht:



#### **Ohne Mullvad VPN-Abonnement:**




- **Grundlegende Verbindungsprüfung**: zeigt Ihre aktuelle öffentliche IP-Adresse und einige Verbindungsinformationen an
- **Empfehlungen zum Datenschutz**: Tipps zur Verbesserung Ihrer Sicherheitseinstellungen (DNS, nur HTTPS, Suchmaschine)
- **WebRTC-Steuerung**: aktivieren/deaktivieren, um IP Address-Lecks zu verhindern
- Kann ohne Auswirkungen auf Ihren digitalen Fußabdruck gelöscht werden, wenn Sie Mullvad VPN nicht verwenden



#### **Mit Mullvad VPN-Abonnement:**


Die Erweiterung entfaltet ihr volles Potenzial mit erweiterten Funktionen:





- **Integrierter SOCKS5-Proxy**: Ein-Klick-Verbindung zum Mullvad VPN-Server-Proxy
- **Feste IP Address**: im Gegensatz zu einem VPN, das seine IP Address ändern kann, garantiert ein Proxy immer dieselbe Ausgangs-Address
- **Automatischer Kill Switch**: Wenn die VPN-Verbindung unterbrochen wird, wird der Browser-Verkehr sofort blockiert
- **IPv6-Unterstützung**: IPv6-Konnektivität, auch wenn Ihre VPN-Verbindung nicht aktiviert ist





- **Multihop (Doppel-VPN)**: Möglichkeit, den Proxy-Standort zu ändern, um einen Tunnel innerhalb des Tunnels zu erstellen
 - Ihr Datenverkehr durchläuft zunächst Ihren VPN-Server und "springt" dann zu einem anderen Mullvad-Server
 - Verwenden Sie eine andere Lokalisierung nur für den Browser





- **Erweiterte Verbindungsüberwachung**: Echtzeitüberwachung Ihres VPN-Status, des verbundenen Servers und Erkennung von DNS-Lecks





- Zugang zu **Mullvad Leta**: private Suchmaschine, die für Abonnenten reserviert ist (obwohl von Mullvad aus Gründen der Korrelation mit Ihrem Konto nicht empfohlen)



Diese drei Erweiterungen arbeiten zusammen, um ein kohärentes Ökosystem des Schutzes zu schaffen, in dem jeder Benutzer von genau denselben Schutzmaßnahmen profitiert, ohne die Möglichkeit der Anpassung, die die kollektive Anonymität gefährden würde.



## Vorteile und Nachteile von Mullvad Browser



### Vorteile





- **Hervorragender Standard-Datenschutz:** Mullvad Browser wendet von Anfang an sehr strenge Datenschutzeinstellungen an, ohne dass eine manuelle Konfiguration erforderlich ist.





- Bessere Leistung als Tor-Browser: Ohne Onion-Routing ist Mullvad-Browser **deutlich schneller und reaktionsschneller** als Tor-Browser für das klassische Web-Browsing.





- **Vertraute Interface Einfachheit:** Der Mullvad Browser basiert auf dem Interface von Firefox. Wenn Sie Firefox oder sogar Tor Browser gewohnt sind, werden Sie sich nicht fehl am Platz fühlen.





- **Vertrauensvolle Zusammenarbeit und geprüfter Code:** Mullvad Browser profitiert von der Expertise des Tor-Projekts, und der gesamte Quellcode ist für externe Prüfungen verfügbar.



### Benachteiligungen





- **Keine Netzwerkanonymität ohne VPN:** Der wichtigste Punkt ist, dass **Mullvad Browser Ihre IP Address nicht von selbst versteckt** (wie alle anderen Browser, außer Tor Browser). Deine IP Address ist wie deine "postalische Address" im Internet: sie verrät deinen Standort und deinen ISP. Daher **ist er stark auf ein VPN** (virtuelles privates Netzwerk) angewiesen, um diese wichtigen Informationen zu verbergen.





- **Keine mobile Version:** Bislang ist Mullvad Browser nur auf PC (Windows, Mac, Linux) verfügbar.





- **Inkompatibel mit bestimmten Gewohnheiten:** Der **permanente private Modus** bedeutet, dass Sie eine Sitzung nicht von einer Nutzung zur nächsten beibehalten können. Es ist unmöglich, von einer Sitzung zur nächsten mit einem Webkonto verbunden zu bleiben.





- **Eingeschränkte Funktionen:** Um die Einheitlichkeit der Fingerabdrücke zu bewahren, hat Mullvad Browser **eine Reihe von Funktionen** deaktiviert, die in Firefox vorhanden sind, und ist nicht für Anpassungen vorgesehen.



## Installation von Mullvad Browser



Mullvad Browser ist kostenlos für Windows, macOS und Linux erhältlich. Um ihn zu installieren, gehen Sie auf [die offizielle Mullvad-Website](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Offizielle Homepage von Mullvad Browser mit hervorgehobener Download-Schaltfläche*



![MULLVAD BROWSER](assets/fr/03.webp)



*Wählen Sie Ihr Betriebssystem auf der Mullvad Browser.* Download-Seite



Klicken Sie auf die Schaltfläche **"Download "**, die Ihrem Betriebssystem entspricht.



Für Linux können Sie je nach Distribution zwischen verschiedenen Formaten wählen. Sobald der Download abgeschlossen ist:



### Unter Windows


Führen Sie die heruntergeladene `.exe`-Datei aus und folgen Sie den Installationsanweisungen.



### Unter macOS


Öffnen Sie die heruntergeladene `.dmg`-Datei und ziehen Sie die Mullvad Browser-Anwendung in Ihren Anwendungsordner.



### Unter Linux


Entpacken Sie das `.tar.xz`-Archiv in ein Verzeichnis Ihrer Wahl und führen Sie die Datei `start-mullvad-browser.desktop` aus.



## Konfiguration und erste Verwendung



Wenn Sie Mullvad Browser zum ersten Mal starten, sehen Sie einen Interface, der dem von Tor Browser sehr ähnlich ist. Der Browser ist für den Datenschutz vorkonfiguriert und erfordert keine besonderen Änderungen.



![MULLVAD BROWSER](assets/fr/04.webp)



*Interface Mullvad-Browser-Startseite mit Erweiterungen, Besen-Symbol zu generate eine neue Identität und Anwendungsmenü oben rechts.*



**Wichtig:** Mullvad Browser maskiert Ihre IP Address standardmäßig nicht. Für einen vollständigen Schutz empfehlen wir dringend die parallele Verwendung eines VPN. Sie können Mullvad VPN oder jeden anderen vertrauenswürdigen VPN-Dienst verwenden.



Der Browser verfügt außerdem über **DNS-over-HTTPS (DoH)** unter Verwendung des DNS-Dienstes von Mullvad: Diese Technologie verschlüsselt Ihre DNS-Anfragen (Übersetzung von Website-Namen in IP-Adressen), um zu verhindern, dass Ihr Internetanbieter die von Ihnen besuchten Websites überwacht.



### Sicherheitseinstellungen



Sie können die Sicherheitsstufe anpassen, indem Sie auf das **Anwendungsmenü** (drei horizontale Balken) oben rechts klicken, dann auf **"Einstellungen "** und dann auf die Registerkarte **"Datenschutz und Sicherheit "**. Scrollen Sie nach unten zum Abschnitt **"Sicherheit "**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Auswahl der Sicherheitsstufen: die Pfeile zeigen den Weg vom Anwendungsmenü zur Registerkarte "Datenschutz & Sicherheit" zu den Sicherheitsoptionen*



Mullvad Browser bietet drei Sicherheitsstufen:





- **Normal** (aktuelle Standardstufe): Alle Browser- und Website-Funktionen aktiviert





- **Sicherer**: Deaktiviert häufig gefährliche Website-Funktionen, was bei einigen Websites zu Funktionseinbußen führen kann:
 - JavaScript ist für Nicht-HTTPS-Seiten deaktiviert
 - Einige Schriftarten und mathematische Symbole sind deaktiviert
 - Ton und Video (HTML5-Medien) sowie WebGL sind "click to play"





- **Die sicherste**: Erlaubt nur die Website-Funktionen, die für statische Websites und Basisdienste erforderlich sind:
 - JavaScript ist standardmäßig für alle Websites deaktiviert
 - Einige Schriftarten, Icons, Bilder und mathematische Symbole sind deaktiviert
 - Ton und Video (HTML5-Medien) sowie WebGL sind "click to play"



### Schaltfläche "Neue Sitzung



Um mit einer leeren Sitzung neu zu beginnen, ohne den Browser zu schließen, klicken Sie auf das Besensymbol oder verwenden Sie das Anwendungsmenü > **"Neue Sitzung "**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Funktion "Identität zurücksetzen", um den Browser mit einer völlig neuen Sitzung neu zu starten*



## Alltäglicher Gebrauch



### Normale Navigation



Mullvad Browser verhält sich wie ein klassischer Browser für das tägliche Surfen. Alle Websites sind wie gewohnt zugänglich, mit dem zusätzlichen Vorteil eines verbesserten Schutzes gegen Tracking.



### Cookie-Verwaltung und Anmeldung



Aufgrund des permanenten privaten Modus müssen Sie sich jedes Mal neu mit Ihren Konten verbinden, wenn Sie sich anmelden. Das ist der Preis, den Sie für maximale Vertraulichkeit zahlen.



### Erweiterungen



Mullvad Browser erlaubt Ihnen technisch gesehen, zusätzliche Erweiterungen aus dem Firefox-Katalog zu installieren, aber **es ist wichtig, die Auswirkungen zu verstehen**. Jede hinzugefügte Erweiterung verändert Ihren digitalen Fußabdruck und unterscheidet Sie von anderen Mullvad-Browser-Nutzern, was dem Grundprinzip des Browsers widerspricht: alle Nutzer identisch erscheinen zu lassen.



Wie Mullvad erklärt: *"Manchmal ist es besser, keine spezifische Verteidigung zu haben, als eine zu haben. Wenn Sie Ihre Online-Privatsphäre verbessern wollen, installieren Sie Erweiterungen, die Sie letztendlich noch sichtbarer machen. "*



Wenn Sie dennoch Erweiterungen installieren, sollten Sie sich bewusst sein, dass Sie damit einen eindeutigen Fingerabdruck erstellen, der dazu verwendet werden kann, Sie von Website zu Website zu verfolgen. Für maximalen Schutz sollten Sie sich an die drei vorinstallierten Erweiterungen halten, die für alle Benutzer identisch sind.



## Bewährte Praktiken mit Mullvad Browser



1. **Verwenden Sie immer ein VPN:** Mullvad Browser maskiert Ihre IP nicht. Ein VPN ist für vollständige Anonymität unerlässlich.



2. **Passen Sie den Browser nicht an**: Vermeiden Sie es, Einstellungen zu ändern oder Erweiterungen hinzuzufügen, da Sie dadurch identifizierbar werden könnten.



3. **Verwenden Sie die Schaltfläche "Neue Sitzung":** Zwischen verschiedenen Aktivitäten können Sie mit der Reset-Funktion Ihre Sitzungen aufteilen.



4. **Wählen Sie die Sicherheitsstufe, die Ihren Bedürfnissen am besten entspricht**:




- **Normal (empfohlen)**: Für das tägliche Surfen. Bietet bereits einen ausgezeichneten Schutz, ohne dass Websites beeinträchtigt werden. Dies ist für 95 % der Benutzer die beste Lösung.
- **Sicherer**: Wenn Sie unbekannte oder potenziell gefährliche Websites besuchen, oder für zusätzlichen Schutz in öffentlichen Wi-Fi-Netzwerken. Einige Websites können nicht richtig funktionieren.
- **Am sichersten**: Reserviert für Hochrisikosituationen (investigativer Journalismus, sensible Kommunikation, feindliche Umgebungen). Die meisten modernen Websites werden beschädigt sein, aber das ist der Preis für maximale Sicherheit.



5. **Regelmäßig nach Updates suchen**: Halten Sie Ihren Browser mit den neuesten Sicherheits-Patches auf dem neuesten Stand.



6. **Benutzen Sie datenschutzfreundliche Suchmaschinen**: Wählen Sie DuckDuckGo, Startpage oder Searx statt Google.



7. **Nur HTTPS-Modus aktivieren**: Stellen Sie in den Einstellungen sicher, dass der Modus "Nur HTTPS" aktiviert ist, um sichere Verbindungen zu erzwingen.



8. **Ändern Sie KEINE erweiterten Einstellungen**: Im Gegensatz zu anderen Browsern ist der Mullvad Browser so konzipiert, dass ALLE Benutzer genau die gleiche Konfiguration haben. Das Ändern von Einstellungen in `about:config` oder das Ändern von uBlock Origin/NoScript-Einstellungen würde Sie einzigartig machen und die Anonymität des Browsers komplett aufheben.



## Empfohlene DNS-Konfiguration



Mullvad Browser integriert automatisch Mullvad DNS-over-HTTPS. Wenn Sie Mullvad VPN verwenden, empfiehlt die Erweiterung, dass Sie **Mullvad DoH** deaktivieren, da es schneller ist, den DNS-Server Ihres VPN-Servers zu verwenden. Wenn Sie Mullvad VPN nicht verwenden, lassen Sie Mullvad DoH aktiviert, um DNS-Überwachung durch Ihren ISP zu vermeiden.



## Schlussfolgerung



Mullvad Browser ist eine hervorragende Lösung für alle, die ein datenschutzfreundliches Surfen im Internet ohne die Leistungseinschränkungen des Tor-Netzwerks suchen. In Kombination mit einem hochwertigen VPN bietet er einen robusten Schutz gegen Online-Tracking und Überwachung.



Trotz gewisser Einschränkungen (keine mobile Version, nicht persistente Sitzungen) ist Mullvad Browser ein wertvolles Werkzeug im Arsenal eines jeden, der die Kontrolle über seine digitale Privatsphäre zurückgewinnen möchte. Seine Benutzerfreundlichkeit und Standardkonfiguration machen ihn zu einer klugen Wahl für datenschutzbewusste Nutzer, egal ob Anfänger oder erfahren.



## Ressourcen



### Offizielle Dokumentation




- [Offizielle Website des Mullvad-Browsers](https://mullvad.net/fr/browser)
- [Mullvad Browser Download-Seite](https://mullvad.net/en/download/browser)
- [Detaillierte technische Daten](https://mullvad.net/en/browser/Hard-facts)
- [Mullvad Browser-Erweiterung](https://mullvad.net/en/help/mullvad-browser-extension)



### Leitfäden und Erläuterungen




- [Warum Privatsphäre wichtig ist] (https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor ohne Tor: Mullvad-Browser-Konzept] (https://mullvad.net/en/browser/tor-without-tor)
- [Wie man einen datenschutzfreundlichen Browser wählt](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Browser-Fingerprinting verstehen](https://mullvad.net/en/browser/browser-fingerprinting)



### Unterstützung und Hilfe




- [Mullvad Browser Help Center](https://mullvad.net/en/help/tag/mullvad-browser)
- [Erste Schritte zum Online-Datenschutz] (https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Ressourcen der Gemeinschaft




- [Mullvad Browser Guide - Leitfaden zum Datenschutz](https://www.privacyguides.org/en/desktop-browsers/)
- [Gemeinschaftsdiskussionen] (https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)