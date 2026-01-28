---
name: DietPi
description: Leichtgewichtiges Betriebssystem, optimiert für leistungsschwache Rechner. Mit einer Vorliebe für Self-Hosting
---

![cover](assets/cover.webp)



In nichttechnischen Kreisen sind Marken wie "Android", "Himbeer Pi", "Orange Pi" oder "Radxa" kaum bekannt. Aber man muss sich nur in Tech-Kreisen umsehen, um festzustellen, dass **SBC**-Computer - die auf einer einzigen Hauptplatine aufgebaut sind und im Vergleich zu herkömmlichen Computern oft mikroskopisch klein sind - als Unterstützung für jedes persönliche Projekt unverzichtbar geworden sind.



Dies sind Computer, die in einer Vielzahl von Modellen hergestellt werden. Auf ihnen laufen vorzugsweise Linux-Distributionen, die oft so angepasst sind, dass sie auf diesen leistungsschwachen Rechnern reibungslos funktionieren.



**DietPi ist keine Ausnahme**: Es ist ein Debian-basiertes Betriebssystem, das darauf optimiert ist, so leicht wie möglich zu sein und selbst den leistungsschwächsten `SBC` sehr schnell zu machen. Es wurde von Debian12 Bookworm auf Debian13 Trixie umgestellt, gerade als dieses Tutorial geschrieben wurde, und unterstützt nun auch Open-Source-SBCs mit `RISC-V`-Prozessoren. DietPi ist eine angenehme Entdeckung, die eine weitere Untersuchung verdient.



## Stärken



Dies ist nicht das "übliche Duplikat" von Debian für kleine Raspberry-artige Boards. DietPi ist es:




- Optimiert für Geschwindigkeit und Leichtigkeit**: ein [Vergleich mit anderen Debian-Distributionen für SBC](https://dietpi.com/blog/?p=888), DietPi ist in allem leichter. Das DietPi-ISO-Image wiegt weniger als 1 GB, bei weitem das kleinste unter denjenigen, die für ältere Raspberry- oder Orange-PI-Modelle bestimmt sind (zum Beispiel). Der Bedarf an RAM- und CPU-Ressourcen ist sehr gering, so dass es immer das Beste aus den Boards herausholt, auch aus älteren.
- Integrierte Automatisierungen und Installationsprogramme**: Eine Reihe spezieller Befehle unterstützt die Benutzer bei der Überwachung der Systemressourcen sowie bei der Automatisierung von Aufgaben zur Installation und zum Start von Programmen, zur Aktualisierung von Versionen, zur Erstellung von Backups und zur Überprüfung aller Protokolle.
- Eine starke, experimentierfreudige Gemeinschaft**: die [Tutorials](https://dietpi.com/forum/c/community-tutorials/8) und Projekte der DietPi-Community sind ideal, um sich von Software inspirieren zu lassen, die Sie dank DietPi mit einem Klick installieren können.



**Noch nie war es so einfach, das Beste aus Ihrem SBC herauszuholen**.



## Automatisierungen für das Self-Hosting


Möchten Sie mit Ihrem eigenen Server experimentieren, um fortgeschrittene Netzwerklösungen zu betreiben, oder Tools, um Ihr Bitcoin-Fachwissen weiterzuentwickeln? DietPi könnte die Lösung sein, nach der Sie gesucht haben. Obwohl viele Menschen wissen, wie sie ihre eigene Infrastruktur verwalten und perfekt konfigurierte und geschützte Server betreiben, ist DietPi ein geeigneter Schritt für diejenigen, die bei Null anfangen wollen.



Anstatt all die komplexen Aufgaben, die eine solche Aufgabe erfordert, manuell auszuführen, ermöglicht DietPi es Ihnen, sie mit einem "Assistenten" und einer eigenen Befehlszeile zu erstellen. Hier können Sie mit Ihrer eigenen persönlichen Cloud, _smart home_ Gerätemanagement, automatisierten Backups und Crontab sowie fortgeschrittenen Lösungen experimentieren.



![img](assets/en/01.webp)



## Einrichtung



### Herunterladen



DietPi bietet eine Vielzahl von ISO-Images, um das Betriebssystem auf viele verschiedene Geräte zu brennen. Einige werden nur unterstützt: das ISO für den Raspberry PI5 ist zum Beispiel noch in der Testphase, aber Sie können bestimmt das passende für Ihr Board finden.



Für diesen Leitfaden habe ich mich für die Installation auf einem Thin Client entschieden, also ging die Wahl auf _PC/VM_ und dann auf _Native PC_. Für diese Geräte gibt es zwei ISO-Images, die sich in der Generation des Bootloaders unterscheiden. Der im Tutorial verwendete Rechner ist recht alt, daher fiel die Wahl auf die _BIOS/CSM_-Version. Wenn Sie einen neueren Rechner haben, könnte die richtige Version `UEFI` sein.



![img](assets/en/02.webp)



Sie werden auf der Seite landen, die das "Image des Installers", den "sha256" und die "Signaturen" enthält.



![img](assets/en/03.webp)



Bereiten Sie ein Verzeichnis im `home` Ihres täglichen Computers vor, damit Sie die notwendigen Dateien mit `wget` herunterladen können.



![img](assets/en/04.webp)



Der öffentliche Schlüssel des Entwicklers erforderte ein Minimum an Recherche, aber Sie können ihn unter diesem Link finden: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Prüfen Sie den Inhalt des Verzeichnisses mit `ls -la` und importieren Sie den MichaIng-Schlüssel mit `gpg --import` in Ihren Schlüsselbund.



### Verifizierung und Flash



Schließlich der Teil, den ich am meisten empfehle: Überprüfen Sie die Echtheit des Betriebssystems, das Sie heruntergeladen haben und auf Ihrem SBC installieren wollen.



![img](assets/en/06.webp)



Wenn Sie mit dem Befehl sha256sum ebenfalls das Ergebnis "Gute Signatur" und die gleiche Hash-Kontrolle erhalten haben, können Sie die ISO-Datei auf einen USB-Stick flashen. Verwenden Sie dazu Anwendungen wie Whale Etcher.



![img](assets/en/07.webp)



## DietPi-Installation



![img](assets/en/09.webp)



Übertragen Sie das Flash-Laufwerk auf das Gerät, das DietPi hosten wird, und beginnen Sie mit der Installation des Betriebssystems lime Green. In dieser Übung verwenden wir einen Thin Client mit 16 GB RAM, einer 128-GB-SSD für das Betriebssystem und einer zweiten 1-TB-Datenplatte. Die Installation dauerte weniger als 30 Minuten, aber wenn Sie z. B. einen Raspberry verwenden, können die Ressourcen geringer sein und länger dauern. Während der Installation werden Sie über den Fortschritt informiert.



![img](assets/en/08.webp)



Da DietPi für Raspberrys und ähnliche Geräte entwickelt wurde, ist die wahre Natur von DietPi die sogenannte "kopflose" Installation, ohne grafische Umgebung und mit nativem "shsh"-Zugriff. In der Anleitung werden Sie stattdessen eine grafische Umgebung sehen, LXDE, um genau zu sein.



In diesem Schritt werden Sie auch gefragt, welchen Webbrowser Sie standardmäßig verwenden möchten: Chromium oder Firefox. Beide funktionieren gut; es gibt keine besonderen Gegenargumente für einen der beiden, außer Ihrer persönlichen Vorliebe.



Gegen Ende fragt das Installationsprogramm Sie möglicherweise, ob Sie bereits Programme installieren möchten, aber hier **empfehle ich Ihnen, nichts vorzuinstallieren**. Sie sollten wissen, dass Sie nach diesem Schritt aufgefordert werden, die Standardkennwörter der beiden Benutzer aus Sicherheitsgründen zu ändern. Vor allem müssen Sie **das `Globale Software-Passwort (GSP)`** festlegen, das den kontrollierten Zugriff auf die verschiedenen Programme gewährleistet. **Wenn Sie während der Installation des Betriebssystems Software herunterladen, ohne das "GSP" zu setzen, bleibt diese praktisch unzugänglich**. Sie müssen sie deinstallieren und erneut installieren, nachdem Sie das `Globale Software-Passwort` gesetzt haben: **Deshalb sollten Sie nichts eintragen, um doppelte Arbeit zu vermeiden**. (Die Unannehmlichkeiten sind wahrscheinlich, aber nicht 100% sicher).



Die Installation endet mit einer Aufforderung zur Aktivierung von DietPi-Survey, einem automatischen Datenerfassungsdienst, der zur Unterstützung der Entwicklung des Betriebssystems eingesetzt wird. Laut der Website wird die Datenerfassung aktiviert, wenn Sie eine der Software aus der von DietPi bereitgestellten Automatisierung herunterladen oder wenn Sie auf die nächste Version aktualisieren. Jeder hat die Möglichkeit, sich einzuschalten (_Opt IN_) oder auszuschalten (_Opt OUT_).



![img](assets/en/23.webp)



Nach Abschluss der Installation und dem anschließenden Neustart erscheint DietPi auf dem Bildschirm, wie Sie es eingerichtet haben. Für das Tutorial habe ich, wie erwähnt, die grafische Umgebung "LXDE" gewählt. Auf dem Desktop fand ich die Verknüpfung zum Starten von `htop` und dem offenen Terminal.



![img](assets/en/10.webp)



### "Tools" aus dem Betriebssystem



Vergessen Sie die meisten Programme, die Sie auf Ihrer Linux-Distribution verwenden - DietPi ist so optimiert, dass Sie eine ganze Reihe davon weggelassen haben. Im Grunde müssten Sie viele Befehle manuell installieren, aber wenn Sie es nur ausprobieren wollen, widerstehen Sie der Versuchung und testen Sie die Automatisierungen von DietPi.



Das Terminal ist definitiv das erste nützliche Werkzeug für den Einstieg in Ihr neues Betriebssystem und öffnet sich automatisch, sobald Sie es einschalten.



![img](assets/en/11.webp)



Auf dem Terminalbildschirm finden Sie eine Reihe von Befehlen mit dem vorangestellten `dietpi-`, die für die [Werkzeuge](https://dietpi.com/docs/dietpi_tools/) dieses Betriebssystems stehen:




- `dietpi-launcher`: für den Zugriff auf das Betriebssystem, den Dateimanager, etc
- dietpi-Software": das Werkzeug, mit dem Sie alle bereits in der Suite vorhandenen Programme installieren können
- `dietpi-config`: um auf die Systemkonfigurationen zuzugreifen, auch auf die fortgeschrittensten.



![img](assets/en/14.webp)



### Sicherung



Die Sicherung eines Servers ist eine Routine, die der Systemadministrator von der ersten Inbetriebnahme an einplanen sollte.



Mit DietPi gibt es den Befehl `dietpi-Backup`, den ich Ihnen empfehle, zu erforschen, um die ideale Lösung zu finden: Er erlaubt Ihnen, ein regelmäßiges Backup einzurichten, inkrementell oder nicht, abhängig von den verwendeten Anwendungen, und alle Optionen, um die Routine anzupassen.



![img](assets/en/22.webp)



Wählen Sie das Ziel des Backups, z.B. eine andere Festplatte, indem Sie `dietpi-Drive_Manager` starten, um das Ziellaufwerk zu mounten und es für diese Funktion zu verwenden.



## Konfiguration



Self-Hosting ist eine empfehlenswerte Erfahrung für jeden, ob neugierig oder einfach begeistert. Das Aufstellen und Konfigurieren eines Servers ist jedoch mit nicht unerheblichen technischen Herausforderungen verbunden. Hier kommt **die Einfachheit von DietPi** ins Spiel, mit der Sie in wenigen Schritten ein auf Ihre Bedürfnisse zugeschnittenes System konfigurieren können.



![img](assets/en/24.webp)



Grundlegende und fortgeschrittene Einstellungen, die alle mit dem Interface-Befehl zur Verfügung stehen:



``dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-software


```