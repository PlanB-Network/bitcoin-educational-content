---
name: Pi-Hole
description: Ein Werbeblocker für Ihr gesamtes Netzwerk
---
![cover](assets/cover.webp)



___



*Dieses Tutorial basiert auf Originalinhalten von Florian Duchemin, die auf [IT-Connect](https://www.it-connect.fr/) veröffentlicht wurden. Lizenz [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Am Originaltext können Änderungen vorgenommen worden sein.*



___



## I. Präsentation



Wir alle haben es getan, sobald wir unseren Lieblingsbrowser gestartet haben: Wir haben einen **Adblocker** (Werbeblocker) installiert. Wenn man jedoch den TV-Browser oder ein Android-Gerät usw. verwendet... Es ist ein bisschen schwieriger, etwas zu finden, das funktioniert. Und wenn es mehr als ein Gerät im Haus gibt, muss man den Vorgang für jeden Browser wiederholen!



In diesem Tutorial lösen wir ein einfaches Problem: Wir stellen einen Werbeblocker für alle Rechner in unserem Netzwerk bereit und verwalten ihn zentral



Dazu werden wir ein für diesen Zweck entwickeltes Tool verwenden: **Pi-Hole**



Pi-Hole ist ein DNS-Sinkhole. Es nutzt die DNS-Anfragen Ihrer Geräte, um den Datenverkehr zu bestätigen oder zu verweigern und schützt Sie so vor Adressen und Domänen, die bekanntermaßen Werbung, Malware usw. verbreiten.



DNS steht für Domain Name System. Was ist also ein Domänenname? Nun, "it-connect.fr" ist nur ein Beispiel. Ein Domänenname ist eine eindeutige Kennung für eine oder mehrere Ressourcen, die in der Regel von einer einzigen Stelle verwaltet wird.



Der Rechnername plus der Domänenname wird FQDN genannt, was für *Fully Qualified Domain Name* steht. Damit können Sie einen bestimmten Rechner erreichen, indem Sie ihn einfach "anrufen". Wenn Sie zum Beispiel "www.trucmachin.com" eingeben, rufen Sie den Rechner "www" auf, der zur Domäne "trucmachin.com" gehört.



Nur verstehen unsere Computer keine menschliche Sprache, sondern nur Binärzeichen, so dass sie eine IP Address benötigen, die einer Telefonnummer entspricht, um die Website zu erreichen.



Jedes Mal, wenn Sie also den Namen einer Website in Ihren Browser eingeben oder auf einen Link klicken, fragt Ihr Computer zunächst einen DNS-Server nach der IP Address, die diesem Namen entspricht.



**Pi-Hole prüft diese Anfragen (jeden Tag gibt es Hunderte davon!) und blockiert automatisch diejenigen, die bekanntermaßen Werbung oder sogar bösartige Dateien enthalten**



## II. Installation von Pi-Hole



Bei einem Namen wie Pi-Hole könnte man zu Recht annehmen, dass man einen Raspberry-Pi braucht... Aber das ist nicht ganz richtig. **Pi-Hole kann auf jedem Linux-Computer installiert werden (Debian, Fedora, Rocky, Ubuntu, etc.).**



Andererseits muss man bedenken, dass **dieses Gerät aus einem einfachen Grund 24 Stunden am Tag laufen muss: kein DNS, kein Internet!** Der Raspberry ist daher eine gute Idee, da er fast keine Energie verbraucht.



Zur Installation verbinden Sie sich einfach über SSH mit Ihrem Linux-Rechner und geben den folgenden Befehl als "*root*" ein:



```
curl -sSL https://install.pi-hole.net | bash
```



> **Hinweis**: Unter normalen Umständen ist es nicht ratsam, ein Skript zu "hacken", ohne vorher zu wissen, was es tut. Wenn Sie sich nicht sicher sind, rufen Sie die Seite mit einem Browser auf oder laden Sie den Inhalt als Datei herunter.
>


> **Hinweis: Auf Minimalversionen von Debian 11 ist Curl nicht installiert, daher müssen Sie es manuell mit dem Befehl** `apt-get install curl` **installieren, bevor Sie den obigen Befehl eingeben.**

Sobald das Skript ausgeführt wurde, wird eine Reihe von Tests durchgeführt, und die Installation selbst erledigt sich von selbst:



![Image](assets/fr/019.webp)



Installation von Pi-Hole



Sobald die Installation abgeschlossen ist, wird dieser Bildschirm angezeigt:



![Image](assets/fr/020.webp)



Pi-Hole-Startbildschirm



> **Hinweis**: Wenn Sie DHCP auf Ihrem Rechner verwenden, erhalten Sie eine entsprechende Warnmeldung. Für eine ordnungsgemäße Nutzung empfehlen wir natürlich dringend, dass Sie Ihrem Rechner eine feste IP zuweisen.

Nach diesem Bildschirm erhalten Sie einige Informationsmeldungen und werden dann zum Konfigurationsassistenten weitergeleitet, der Sie zunächst fragt, an welchen DNS-Server Pi-Hole Anfragen weiterleiten soll. Ich für meinen Teil habe Quad9 gewählt, der eine Charta zum Schutz der Privatsphäre der Nutzer hat.



![Image](assets/fr/021.webp)



DNS-Auswahl - Pi-Hole



> **Hinweis:** Wenn Sie in einem Unternehmen arbeiten, ist Ihr aktueller DNS-Server wahrscheinlich der Active Directory Domain Controller. Aber keine Sorge, Sie können später einen bedingten Redirector für eine Domäne Ihrer Wahl angeben. Normalerweise können Sie jede Anfrage, die Ihre lokale Domäne betrifft, an Ihren DNS-Server weiterleiten.

Sie werden feststellen, dass einige Optionen eine DNSSEC-Option enthalten. Grundsätzlich ist das DNS-Protokoll nicht sicher (es wurde seinerzeit nicht mit diesem Ziel entwickelt). DNSSEC löst dieses Problem, indem es durch Verschlüsselung und Signierung des Datenaustauschs ein Layer an Sicherheit hinzufügt, wie in dem entsprechenden Artikel erläutert wird: [DNS-Sicherheit](https://www.it-connect.fr/securite-dns-doh-quest-ce-le-dns-over-https/)



Jeder Werbeblocker ist auf eine oder mehrere Listen angewiesen, um seine Aufgabe zu erfüllen. Pi-Hole wird standardmäßig mit einer einzigen Liste geliefert, die Sie auswählen und später weitere hinzufügen können.



![Image](assets/fr/022.webp)



Kommen Sie die Frage über Interface Web, seine Installation ist optional, da das Tool hat seine eigene Kommandozeile für die Verwaltung und Visualisierung. Aber diese Interface ist ziemlich angenehm und gut gemacht, so empfehle ich, dass Sie es zur gleichen Zeit zu installieren:



![Image](assets/fr/023.webp)



Wenn Sie Pi-Hole auf einem Rechner installieren, der bereits einen Webserver hat, können Sie die folgende Frage mit "nein" beantworten. Bitte beachten Sie jedoch, dass PHP und verschiedene Module erforderlich sind, damit dies funktioniert. Ansonsten wird **lighttpd mit allen notwendigen Modulen** installiert.



![Image](assets/fr/024.webp)



Sie werden dann gefragt, ob Sie DNS-Anfragen aufzeichnen möchten. **Wenn Sie eine Historie aufbewahren möchten, setzen Sie dies auf "Ja", andernfalls setzen Sie dies auf "Nein", aber Sie verlieren dann einen Teil der Funktionalität** (siehe nächster Bildschirm).



![Image](assets/fr/025.webp)



Für sein Interface-Web verwendet Pi-Hole eine eigene Funktion namens FTLDNS, die eine API bereitstellt und Statistiken aus DNS-Anfragen erstellt. Diese Funktion kann einen "Datenschutz"-Modus enthalten, der die angeforderten Domänen, die Kunden hinter der Anfrage oder beides maskiert. Praktisch, wenn Sie eine Überwachung durchführen wollen, ohne die Privatsphäre von Personen zu verletzen, oder einfach, wenn Sie bei der Nutzung in einem öffentlichen Netz die entsprechenden Vorschriften einhalten wollen.



![Image](assets/fr/026.webp)



Wahl des privaten Lebensstils



Sobald diese letzte Frage beantwortet ist, wird das Skript tun, was es tun soll: die GitHub-Repositories herunterladen und Pi-Hole konfigurieren. Am Ende der Installation wird ein zusammenfassender Bildschirm mit den wichtigsten Informationen angezeigt:



![Image](assets/fr/027.webp)



Bildschirm mit Installationsübersicht



Notieren Sie sich das Interface-Web-Passwort und die Netzwerkinformationen. Nun ist es an der Zeit, den DHCP-Dienst an unserem aktuellen Standort zu konfigurieren.



## III. DHCP-Konfiguration



Damit Pi-Hole funktioniert, muss es DNS-Anfragen von Clients "auflösen", d. h. sie müssen wissen, dass es die richtige Adresse für sie ist. Es gibt mehrere Möglichkeiten, dies zu tun:





- Ändern Sie die DNS-Einstellungen in Ihrem DHCP-Server (z. B. Ihrer Box)
- Deaktivieren Sie diesen Server und verwenden Sie den von Pi-Hole bereitgestellten Server
- Manuelles Ändern jedes Geräts zur Verwendung von Pi-Hole als DNS



Ich persönlich wähle die erste Lösung. Die Chancen stehen gut, dass **Sie einen DHCP-Server haben, wo Sie sind** (normalerweise Ihre Box). Es gibt also keinen Grund, sich die Mühe zu machen.



Da es eine große Anzahl von Möglichkeiten gibt, zwischen den verschiedenen Boxen der Betreiber (die ich nicht alle kenne) und denen, die ihren eigenen Router haben, werde ich keinen Screenshot für diese Änderungen zur Verfügung stellen. In jedem Fall müssen Sie die DHCP-Einstellungen aufrufen und den Parameter "DNS" so ändern, dass er die IP Address Ihres Pi-Hole enthält.



Wenn die Geräte zuvor eingeschaltet waren, haben sie die alten Einstellungen beibehalten, so dass Sie die Konfigurationsabfrage neu starten müssen.



Auf Windows-Arbeitsplätzen mit einer Eingabeaufforderung:



```
ipconfig /renew
```



Auf einer Linux-Workstation:



```
dhclient
```



Bei allen anderen Geräten müssen sie aus- und wieder eingeschaltet werden.



Sie sollten also die richtigen Parameter erhalten, um sie zu überprüfen:



```
ipconfig /all
```



Im DNS-Feld sollten Sie die Address Ihres Pi-Lochs eintragen, in meinem Fall 192.168.1.42:



![Image](assets/fr/029.webp)



## IV. Verwendung des Interface web Pi-Hole



Um die Verwaltung zu erleichtern, verfügt **Pi-Hole** über ein gut gestaltetes Interface Web-Interface. Benutzerfreundlich und zugänglich, können Sie:





- Anzeige der Anzahl der Anfragen, der blockierten Anfragen usw. in Echtzeit.
- Verwalten Sie Ihre Whitelist und Blacklist
- Hinzufügen von statischen Einträgen, Aliasen usw.
- Listen hinzufügen
- Und viele andere Funktionen!



Ich für meinen Teil werde eine Blockierliste hinzufügen. Wie bereits erwähnt, wurde nur eine Liste zur gleichen Zeit wie Soft installiert. Es gibt viele Listen für Werbeseiten, aber es ist am besten, mindestens eine für das Land zu wählen, in dem Sie leben. Eine der bekanntesten Listen ist **EasyList**, und eine davon ist speziell für Frankreich: [EasyList-ListFR](https://raw.githubusercontent.com/deathbybandaid/piholeparser/master/Subscribable-Lists/ParsedBlacklists/EasyList-Liste-FR.txt)



Um sie hinzuzufügen, müssen Sie sich zunächst mit dem Interface-Admin verbinden: **http://<ip_du_PiHole>/admin**



Das Administrator-Passwort wurde bereits generiert (siehe Screenshot am Ende der Installation), so dass Sie es nur noch eingeben müssen, um auf Interface zuzugreifen:



![Image](assets/fr/030.webp)



Interface von Pi-Hole



Wir können z. B. sehen, dass zwei Kunden mit dem Pi-Hole verbunden sind, dass es 442 Anfragen bearbeitet hat und dass 8 davon blockiert wurden. Diese Diagramme können eine gute Informationsquelle sein, insbesondere in einem professionellen Kontext.



Um unsere Liste hinzuzufügen, gehen Sie zu den Menüs "**Gruppenverwaltung**" und "**Listen**":



![Image](assets/fr/031.webp)



Wir sehen unsere erste Liste "**StevenBlack**", um unsere hinzuzufügen, kopieren Sie den Link, den ich Ihnen oben gegeben habe und fügen Sie ihn in das Feld "**Address**" ein, für die Beschreibung wähle ich den Namen der Liste:



![Image](assets/fr/032.webp)



Hinzufügen einer Liste in Pi-Hole



Jetzt müssen Sie nur noch auf "**Hinzufügen**" klicken, um sie hinzuzufügen. Um sie zu aktivieren, müssen wir einen zusätzlichen Schritt durchführen, um Pi-Hole zu "warnen", diese Liste zu übernehmen. Um dies zu tun:





- Verwenden Sie entweder die integrierte Befehlszeile
- Entweder das Interface Web



Ich persönlich habe mich für die zweite Variante entschieden, denn wenn Sie genau hingesehen haben, befindet sich der Link zu dem PHP-Skript, das die Aktualisierung durchführt, direkt auf der Seite, auf der wir uns befinden (das Wort "online"). Sie brauchen also nur darauf zu klicken, und schon gelangen Sie auf eine Seite mit nur einer Option:



![Image](assets/fr/033.webp)



Die Seite zeigt das Ergebnis des Skripts an, sobald es abgeschlossen ist, was bedeutet, dass die Liste berücksichtigt wurde (es sei denn, es wird eine Fehlermeldung angezeigt).



Wie zu Beginn dieses Tutorials angekündigt, können Sie mit Pi-Hole auch **Domains blockieren, von denen bekannt ist, dass sie Malware verbreiten. Um diese Funktion zu verstärken, empfehle ich Ihnen, auch die von Abuse.ch** regelmäßig aktualisierte Domainliste hinzuzufügen, die die Sicherheit Ihres Netzwerks erheblich verbessern wird, verfügbar unter [diese Address] (https://urlhaus.abuse.ch/downloads/hostfile/).



Sie können natürlich weitere Listen hinzufügen, die Sie für wichtig halten, oder Ihre schwarze Liste manuell über das Menü "Schwarze Liste" verwalten.



## V. Pi-Loch-Tests



Nun, da alles eingerichtet ist, müssen Sie die Lösung nur noch testen, um sicherzustellen, dass sie ordnungsgemäß funktioniert.



Ich werde zum Beispiel versuchen, die Domain *http://admin.gentbcn.org/* zu erreichen, die auf der Liste von Abuse.ch steht, weil sie dafür bekannt ist, dass sie Malware enthält:



![Image](assets/fr/034.webp)



Offensichtlich bin ich irgendwo blockiert worden. Um sicherzugehen, dass es das Pi-Loch ist, das die Arbeit erledigt hat, können wir im Abfrageprotokoll im Interface-Web unter "Abfrageprotokoll" nachsehen, ob es sich um eine Blockierung durch einen Listeneintrag handelt:



![Image](assets/fr/035.webp)



## VI. Schlussfolgerung



In dieser Anleitung zeigen wir Ihnen, wie Sie einen DNS-Server einrichten, der nicht nur die meisten Werbeeinblendungen für Ihren Surfkomfort eliminiert, sondern auch **ein Layer an Sicherheit bietet, indem er Phishing- und Malware-verbreitende Domains** blockiert.



Alle sind kostenlos und sparsam, wenn sie auf einem Raspberry-Pi installiert sind (in Bezug auf den Stromverbrauch).