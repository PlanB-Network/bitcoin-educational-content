---
name: Firefox
description: Wie konfiguriere ich Firefox, um meine Privatsphäre zu schützen?
---

![cover](assets/cover.webp)



## Einführung



Wir alle verbringen Stunden im Internet, oft ohne zu wissen, was unser Browser über uns preisgibt. Jeder Klick, jede Suche, jede Website, die wir besuchen, nährt eine riesige Industrie zur Sammlung persönlicher Daten.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*Marktanteil der Webbrowser: Chrome dominiert mit 65 % des Marktes, gefolgt von Safari und Edge. Quelle: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



Wie diese Grafik zeigt, dominiert Google Chrome mit einem Anteil von über 65 % an der weltweiten Nutzung massiv. Diese Hegemonie bedeutet, dass die Mehrheit der Internetnutzer ihre Surfdaten Google anvertraut, einem Unternehmen, dessen Geschäftsmodell auf gezielter Werbung beruht. Firefox, mit nur 3 % Marktanteil, stellt eine Alternative dar, die von Mozilla entwickelt wurde, einer gemeinnützigen Organisation, die kein kommerzielles Interesse an der Ausbeutung Ihrer Daten hat.



Doch die Entscheidung für Firefox ist nur der erste Schritt. Auch Firefox erfordert standardmäßig Anpassungen, um Ihren Schutz zu maximieren. Dieser Leitfaden führt Sie Schritt für Schritt von den einfachsten bis zu den fortgeschrittensten Einstellungen, um Firefox in ein wahres Schutzschild gegen Tracking zu verwandeln und gleichzeitig ein angenehmes Surferlebnis zu bewahren.



### Warum Firefox?





- Frei und quelloffen** (Gecko-Engine): überprüfbarer, transparenter Code
- Gemeinnützige Organisation**: Mozilla Foundation, Aufgabe von allgemeinem Interesse
- Eingebaute Schutzfunktionen**: Erweiterter Verfolgungsschutz (ETP), Total Cookie Protection (TCP), State Partitioning, reiner HTTPS-Modus, DNS über HTTPS (DoH)
- Erweiterte Anpassungsmöglichkeiten**: Im Gegensatz zu Chrome können Sie das Verhalten von Firefox tiefgreifend ändern



### Wichtige Grundsätze, bevor Sie beginnen





- Kein allgemeingültiges Rezept**: Je mehr Sie ändern, desto mehr riskieren Sie, aufzufallen (Fingerabdruck). Ziel ist es, besser geschützt zu sein, ohne sich von der Masse abzuheben.
- Schrittweiser Fortschritt**: Ändern Sie eine Einstellung, testen Sie Ihre üblichen Websites und fahren Sie dann fort. Es ist nicht nötig, alles auf einmal zu ändern.
- Persönliches Gleichgewicht**: Finden Sie IHREN Kompromiss zwischen Privatsphäre und Benutzerfreundlichkeit.



## Schnelle Installation



![Téléchargement Firefox](assets/fr/02.webp)



**Offizieller Download:** Gehen Sie zu [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/). Wählen Sie auf dieser Seite Ihr Betriebssystem aus (Windows, macOS, Linux), um die entsprechende Download-Seite mit spezifischen Installationsanweisungen aufzurufen.





- Windows**: Laden Sie das Installationsprogramm `.exe` herunter, doppelklicken Sie darauf und folgen Sie dem Installationsassistenten
- macOS**: laden Sie die `.dmg`-Datei herunter, öffnen Sie sie und ziehen Sie Firefox in den Ordner "Programme"
- Linux**: mehrere Optionen verfügbar - Paket `.deb`/`.rpm`, Flatpak (Flathub), Snap, oder über Paketmanager (apt, dnf, pacman). Bevorzugen Sie die offiziellen Mozilla-Quellen.



**Tipp:** Nach der Installation sollten Sie über Hilfe → **Über Firefox** nach Updates suchen (wichtig für Sicherheitspatches).



![Configuration initiale Firefox](assets/fr/03.webp)


*Erster Bildschirm beim Starten von Firefox: Legen Sie Firefox als Standardbrowser fest, fügen Sie ihn zu Ihren Verknüpfungen hinzu und klicken Sie dann auf "Speichern und weiter "*



![Création compte Firefox](assets/fr/04.webp)


*Optionaler Schritt: Erstellen Sie ein Firefox-Konto oder melden Sie sich dort an. Sie können diesen Schritt überspringen, indem Sie unten rechts auf "Nicht jetzt" klicken*



![Page d'accueil Firefox](assets/fr/05.webp)


*Firefox-Startbildschirm nach Abschluss der Konfiguration. Beachten Sie das ☰-Menü oben rechts, das Zugriff auf Einstellungen und Erweiterungen zur Anpassung von Firefox* bietet



## Schutzmaßnahmen bereits standardmäßig aktiviert (beruhigend)





- Standortisolierung (Fission)**: bei progressiver Bereitstellung. Diese Funktion führt jede Website in einem separaten Prozess aus, um zu verhindern, dass eine bösartige Registerkarte auf die Daten einer anderen zugreift. Überprüfen Sie den Status dieser Funktion über `about:support` (suchen Sie nach "Fission"). Wenn sie nicht aktiviert ist, können Sie sie manuell in `about:config` mit `fission.autostart = true` aktivieren.
- Total Cookie Protection (TCP)**: standardmäßig aktiviert. Cookies und andere Speichermedien sind auf die Website des Erstanbieters beschränkt (ein "Glas" pro Website), was das Cross-Site-Tracking neutralisiert. Vorübergehende Ausnahmen werden bei Bedarf über die Speicherzugriffs-API gemacht (integrierte Anmeldeschaltflächen).
- Schutz vor Bounce/Redirect-Tracking**: Firefox erkennt und bereinigt automatisch Cookies, die von Bounce-Seiten (Links, die Sie über einen Tracker vor dem Ziel umleiten) hinterlassen werden, und reduziert so diesen Tracking-Kanal ohne Ihr Zutun.



## Stufe 1 - Wesentlich (≤ 10 Minuten)



Ziel: großer Gewinn an Privatsphäre, ohne das Netz zu zerstören. Für 90 % der Nutzer.



Um auf die Einstellungen zuzugreifen, klicken Sie auf das Menü ☰ oben rechts, dann **"Einstellungen "**:



![Paramètres généraux](assets/fr/07.webp)


*Firefox-Einstellungsseite - Registerkarte "Allgemein". Hier konfigurieren Sie die meisten Ihrer Datenschutzoptionen*



**Verfolgungsschutz (ETP)**




- Schalten Sie **ETP** auf **Strict** um. Sie blockieren mehr Tracker (seitenübergreifende Cookies, Fingerabdrücke, Kryptomining, soziale Widgets ...).
- Wenn eine Seite nicht mehr funktioniert (Video, Login-Button...), deaktivieren Sie den Schutz nur für diese Seite über das 🛡️ Schild und aktualisieren Sie dann die Registerkarte.



Hier sind die verschiedenen ETP-Sicherheitsstufen:




- Standard** (ausgeglichen, maximale Kompatibilität)
  - Blockiert: soziale Tracker, seitenübergreifende Cookies (alle Fenster), Verfolgung von Inhalten beim privaten Surfen, Kryptowährungs-Miner, Fingerabdruck-Detektoren.
  - Enthält **Total Cookie Protection** (TCP): eine Dose pro Website.
- Streng** (empfohlen für Vertraulichkeit)
  - Blockiert auch Tracking-Inhalte in allen Fenstern + bekanntes und vermutetes Fingerprinting.
  - Kann einige Websites beschädigen; verwenden Sie das 🛡️ Schild für eine lokale Ausnahme.
- Benutzerdefiniert** (fortgeschritten)
  - Feinabstimmung: Cookies, Tracking-Inhalte, Minderjährige, Fingerprinting (bekannt/verdächtig).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**Cookies und Website-Daten




- Aktivieren Sie **"Cookies und Websitedaten beim Schließen löschen "**, um bei jedem Neustart einen sauberen Neustart durchzuführen.
- Fügen Sie **Ausnahmen** für 2-3 wichtige Seiten hinzu, wenn Sie dies wünschen (E-Mail, Bank).


**Automatische Dateneingabe, Vorschläge und Homepage**




- Deaktivieren Sie **auto-fill** (IDs, Adressen, Karten). Verwenden Sie stattdessen einen Passwort-Manager.
- Suche**: Deaktivieren Sie **"Suchvorschläge anzeigen "**.
- Address-Leiste**: Schneiden Sie **"Gesponserte Vorschläge "** und **"Kontextbezogene Vorschläge "** aus.
- Home**: Deaktivieren Sie **Pocket** und **gesponserte Inhalte**.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**Nur HTTPS**




- Aktivieren Sie **"HTTPS-Modus nur in allen Fenstern "**.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**Telemetrie und Werbemessung




- Deaktivieren Sie unter "Datenerfassung durch Firefox" **alle**.
- Deaktivieren Sie **"Datenschutzfreundliche Werbemaßnahmen "** (PPA).
- Sicheres Browsen**: Lassen Sie es aktiviert (empfohlen). Firefox prüft Websites anhand von Hash-Abfragen und lokalen Prüfungen gegen Bedrohungslisten und schützt so vor Phishing und Malware mit minimalen Auswirkungen auf die Privatsphäre.



**Globale Datenschutzkontrolle (optional)**




- Aktivieren Sie die **GPC**, um zu signalisieren, dass Sie den Verkauf/die Weitergabe von Daten ablehnen.



**Suchmaschine




- Wechseln Sie zu **DuckDuckGo**, **Startpage**, **Qwant** oder **Brave Search** (Einstellungen → Suche).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**Private Navigation**




- Private Fenster (Strg/Cmd+Umschalt+P) für einmalige Sitzungen (Geschenke, Zweitkonten...). Vermeiden Sie den Modus "immer privat": Erweiterungen können inaktiv sein und Cookie-Ausnahmen sind weniger nützlich.



**Wesentliche Erweiterungen** (aus dem offiziellen Katalog installieren)




- uBlock Origin**: blockiert Werbung und aktuelles Tracking, leichtgewichtig.
- Privacy Badger**: Lernt zu blockieren, was Ihnen folgt; sendet Do Not Track / GPC.
- ClearURLs** (optional): Firefox (ETP Strict) und uBO bereinigen bereits eine Menge; behalten Sie diese Option bei, wenn Sie immer noch "schmutzige" URLs sehen (utm, fbclid).
- Firefox Multi-Account-Container**: **Isoliert Cookies/Sessions und Speicher pro Container; parallele Multi-Accounts; weniger Cross-Site-Tracking**. Offizielle Erweiterung: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**Passwörter und 2FA**




- Verwenden Sie einen speziellen Passwortmanager** (Bitwarden, KeePassXC). **Vermeiden Sie die Speicherung von Passwörtern im Browser. **Aktivieren Sie 2FA** wo immer möglich.



## Stufe 2 - Verstärkt (Kompartimentierung und Netzwerk)



Ziel: Abschottung der Aktivitäten und Verringerung von Lecks im Netz.



**DNS über HTTPS (DoH)**




- Standardstatus**: In einigen Regionen (USA, Kanada, Russland, Ukraine) automatisch aktiviert. In anderen Regionen ist eine manuelle Aktivierung erforderlich.
- Konfiguration**: Einstellungen → Allgemein → Netzwerkeinstellungen → **DoH aktivieren** → **Cloudflare** oder **Quad9** → **Maximaler Schutz**.
- Maximaler Schutz = nur TRR** (kein Rückgriff auf System-DNS). Wenn ein Firmen-/Hotelnetzwerk blockiert, wechseln Sie zurück zu **Standard** oder deaktivieren Sie DoH.
- Redundanz**: Wenn Sie bereits ein vertrauenswürdiges VPN mit einem eigenen sicheren DNS verwenden, kann DoH redundant sein.
- Verifizierungstest**: unter "https://www.dnsleaktest.com/" sollte nur der gewählte DoH-Anbieter angezeigt werden.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**Aufteilung mit Containern und Profilen




- Multi-Account-Container**: Erstellen Sie Bereiche (Persönlich, Arbeit, Finanzen, Soziale Netzwerke, Einkaufen, Einweg). Konfigurieren Sie **"Immer in diesem Container öffnen "** für Ihre wiederkehrenden Seiten. Offizielle Erweiterung: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- Warum sie verwenden?
  - Starke Isolierung** von Cookies/Sitzungen/Speichern nach Raum.
  - Weniger Cross-Site-Tracking**: Beschränken Sie sich auf die Giganten (Facebook, Google).
  - Gleichzeitige Nutzung mehrerer Konten** für denselben Dienst.
  - Geringeres Risiko von CSRF/XSS** zwischen segmentierten Identitäten.
  - Tipp: Mindestens eigene Container für Soziale Netzwerke/Google, Arbeit, Finanzen.
- Facebook Container** (optional): eine vereinfachte Version für FB/Instagram.
- Separate Profile**: über `about:profiles` (Hauptprofil, minimales "ultra-sicheres" Profil, Testprofil). Vollständige Kompartimentierung von Daten und Erweiterungen.



**Erweiterte Erweiterungen** (zu reservieren)




- Cookie AutoDelete**: löscht die Cookies einer Website, sobald die Registerkarte geschlossen wird (nützlich, wenn Firefox lange Zeit geöffnet ist).
- LocalCDN**: stellt aktuelle Bibliotheken lokal bereit (reduziert Aufrufe an Google/Microsoft). Teilweise Kompatibilität.



**Mobil (Android)**




- Firefox Android + uBlock Origin**: ähnlicher Schutz für unterwegs.



## Stufe 3 - Experte (about:config & Arkenfox)



Ziel: erweiterte Härtung mit akzeptierten Kompromissen. Empfohlen für ein **separates Profil**.



Wählen Sie nur einen der beiden folgenden Ansätze:



**Ansatz A - Manuelle Änderungen**: Ein paar gezielte Anpassungen über `about:config` (einfachere, genauere Kontrolle)


**Ansatz B - Arkenfox user.js**: Vollständig automatisierte Konfiguration (komplexer, maximaler Schutz)



➡️ **Arkenfox enthält bereits ALLE unten genannten about:config-Änderungen** + Hunderte mehr. Wenn Sie Arkenfox wählen, ignorieren Sie den Abschnitt about:config.



### Ansatz A: Manuelle Änderungen über about:config



Tippen Sie `about:config` in die Address-Leiste → Risiko akzeptieren.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- Widerstandsfähigkeit gegen Fingerabdrücke (vom Tor-Browser geerbt)


```text
privacy.resistFingerprinting = true
```


Auswirkungen: UTC-Zeitzone, **letterboxing** (Standard-Fenstergrößen), standardisierte User-Agent/Richtlinien, Canvas/WebGL/AudioContext-Einschränkungen. Mehr Einheitlichkeit, aber ein paar "Macken" (Zeitverschiebung, manchmal ein bisschen Englisch).





- WebRTC deaktivieren (vermeidet IP-Lecks; bricht Webvisio)


```text
media.peerconnection.enabled = false
```





- Referent plus kompatibel (Standard)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


Strenge Option (kann Zahlungen/SSO unterbrechen):


```text
network.http.referer.XOriginPolicy = 2
```





- Begrenzung von plappernden APIs und Spekulationen


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



Goldene Regel: Wenn etwas kaputt geht, gehen Sie zur letzten Änderung zurück.



### Ansatz B: Arkenfox user.js (Vollständig automatisierte Konfiguration)



Das **Arkenfox**-Projekt stellt eine von der Community gepflegte Datei "user.js" zur Verfügung, die automatisch Hunderte von datenschutz- und sicherheitsorientierten Firefox-Einstellungen übernimmt. Beim Neustart liest Firefox diese Datei aus Ihrem Profil und wendet diese Einstellungen an.





- Worin liegt der Sinn? Von einer **konsistenten, gefestigten Basis** ausgehen, ohne "überall herumzuklicken"; Versäumnisse reduzieren; Zeit sparen.
- Was ändert sich (Beispiele): Telemetrie gekürzt, Cookies/Cache/Referrer/HTTPS verstärkt, **RFP** + Letterboxing, **WebRTC deaktiviert**, DoH/TLS Anpassungen, Chat-APIs eingeschränkt.
- Wann sollte man es verwenden: wenn man Firefox in 10 Minuten abgehärtet haben möchte und ein paar Ausnahmen akzeptiert (DRM/Streaming, Webvisio, SSO/Zahlungen).
- Vorteile: schnell, konsistent, **aktualisiert** (ESR-angepasst), sehr gut **dokumentiert** (Wiki + Kommentare), **anpassbar** über Overrides.
- Einschränkungen: Kompatibilität (einige Webanwendungen), Komfort (UTC, Fenstergrößen), und eine Erinnerung: **Es ist nicht Tor** (keine Netzwerkanonymität).



Installation (idealerweise auf einem **eigenen Profil**)


1. Profil/Favoriten speichern und Ihre Websites mit Cookie-Ausnahmen auflisten.


2. Laden Sie `user.js` von `https://github.com/arkenfox/user.js` herunter (ESR/stable Version).


3. Finden Sie Ihren Profilordner über `about:profiles`:




   - Windows: "%APPDATA%/Mozilla/Firefox/Profiles/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/Library/Application Support/Firefox/Profiles/...`


4. Schließen Sie Firefox und verschieben Sie "user.js" in das Stammverzeichnis des Profilordners.


5. Neustart; Anpassung über `about:config` oder eine Overrides-Datei.



Aktualisierungen




- Folgen Sie den Arkenfox-Releases (ESR-angepasst), ersetzen Sie die `user.js`, starten Sie Firefox neu; lesen Sie die Release Notes.



**Anpassung über Overrides**



Arkenfox ist absichtlich restriktiv voreingestellt. Um bestimmte Einstellungen an Ihre Bedürfnisse anzupassen (Streaming, Visio, bestimmte Websites), können Sie eine Datei "user-overrides.js" im selben Ordner wie "user.js" erstellen. Diese Datei ermöglicht es Ihnen, bestimmte Arkenfox-Einstellungen zu "überschreiben", ohne die Hauptdatei zu verändern.



Erstellen Sie `user-overrides.js` und fügen Sie Ihre Anpassungen hinzu:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



Bewährte Praktiken




- Verwenden Sie ein separates **"Arkenfox"-Profil** und behalten Sie aus Komfortgründen ein "normales" Profil.
- Minimieren Sie Erweiterungen (uBlock Origin OK), um die Angriffsfläche und die Einzigartigkeit zu begrenzen.
- Fügen Sie bei Bedarf Ausnahmen für jede einzelne Website hinzu (Schutzschild 🛡️, uBO, NoScript, falls verwendet).
- Testen Sie nach jeder Änderung: WebRTC/DNS-Lecks, Cover Your Tracks, CreepJS.



## Bewährte Praktiken





- Aktualisierungen**: Firefox und Erweiterungen auf dem neuesten Stand.
- Verlängerungen**: vernünftig und zuverlässig; achten Sie auf "dubiose" Einlösungen.
- Downloads**: Vorsicht; prüfen Sie sensible Dateien auf VirusTotal.
- Passwörter**: **Dedicated Manager** (Bitwarden, KeePassXC); **2FA** aktiviert; Speicherung im Browser vermeiden.
- Hygiene**: Google/Facebook auf Container beschränken; regelmäßig schließen/öffnen, um den Kontext "zurückzusetzen".



## Grenzen und Alternativen





- Ein gehärteter Browser ≠ Anonymität im Netz: Ohne **VPN** bleibt Ihre IP sichtbar; auch damit bleibt eine Zuordnung möglich.
- Wenn Sie zu viel ändern, können Sie **einzigartig** werden. **RFP** standardisiert; Tools zur Randomisierung (z. B. Chameleon) können... Sie von anderen abheben. Testen, vergleichen, anpassen.
- Alternativen/Ergänzungen:
 - Tor Browser: Netzwerkanonymität über Tor; langsamer. Siehe unsere vollständige Installations- und Konfigurationsanleitung**:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



 - Mullvad Browser: "Tor ohne Tor", zu kombinieren mit VPN; standardisierter Fußabdruck. Finde heraus, wie du ihn installierst, in unserem speziellen Tutorial**:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- Empfohlene Kombinationen: Firefox (Level 2) + VPN für den täglichen Gebrauch; Tor/Mullvad für sensible Aktivitäten; getrennte Profile zur Abschottung.



## Schlussfolgerung



Wenn Sie diese Schritt-für-Schritt-Anleitung befolgen, haben Sie Firefox in ein wahres Bollwerk gegen digitale Überwachung verwandelt. Von grundlegenden Level-1-Einstellungen bis hin zu fortgeschrittenen Arkenfox-Konfigurationen - jede Änderung stärkt Ihre Privatsphäre, ohne Ihr Surferlebnis zu beeinträchtigen.



**Ihre Privatsphäre ist jetzt besser geschützt**: Werbe-Tracker blockiert, Cookies abgeschottet, IP Address-Lecks neutralisiert, Telemetrie deaktiviert. Firefox ist nicht mehr nur ein Browser, sondern ein digitales Widerstandswerkzeug, das auf Ihre Bedürfnisse zugeschnitten ist.



**Denken Sie daran: Vertraulichkeit ist nie eine Selbstverständlichkeit. Testen Sie Ihren Schutz regelmäßig, aktualisieren Sie Ihre Einstellungen, und zögern Sie nicht, Ihre Konfiguration anzupassen, wenn sich Ihre Gewohnheiten ändern. Ihre Online-Anonymität hängt ebenso sehr von Ihren Tools wie von Ihren Praktiken ab.



## Ressourcen



### Plan ₿ Network




- SCU 202 - Verbessern Sie Ihre persönliche digitale Sicherheit: Um mehr über die Konzepte der digitalen Sicherheit zu erfahren, die in diesem Tutorium behandelt werden**



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla-Dokumentation




- [Erhöhter Verfolgungsschutz](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): Offizieller Leitfaden zum verbesserten Verfolgungsschutz
- [State Partitioning](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): Technische Dokumentation über State Partitioning
- [MDN Web Security](https://developer.mozilla.org/docs/Web/Security): Vollständige Referenz zur Web-Sicherheit



### Arkenfox




- [Wiki und Installationsanleitung](https://github.com/arkenfox/user.js/wiki): Vollständige Arkenfox-Projektdokumentation
- [Hinterlegung und Freigaben] (https://github.com/arkenfox/user.js): Datei user.js herunterladen und Aktualisierungen verfolgen



### Reiseführer und Gemeinschaften




- [PrivacyGuides - Desktop-Browser](https://www.privacyguides.org/en/desktop-browsers/): Browser-Empfehlungen und Vergleiche
- Reddit**: r/firefox, r/privacy für Feedback und Unterstützung
- PrivacyGuides-Forum**: Ausführliche technische Diskussionen



### Prüfwerkzeuge




- [Cover Your Tracks (EFF)] (https://coveryourtracks.eff.org/): Digitale Fingerabdrücke und wirksamer Schutz vor Verfolgung
- [DNS-Leck-Test](https://www.dnsleaktest.com/): DNS-Lecktest und DoH-Effizienz
- [BrowserLeaks](https://browserleaks.com/): Vollständige Test-Suite (WebRTC, Canvas, Schriftarten, etc.)
- [BadSSL](https://badssl.com/): SSL/TLS-Zertifikat-Validierungstests
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): Erweiterte Analyse von mehr als 50 Fingerprinting-Vektoren
- [Cloudflare DNS Test](https://1.1.1.1/help): Prüfen, ob Cloudflare DoH richtig funktioniert
