---
name: Trezor Shamir Backup
description: Mnemonic-Sätze mit einem oder mehreren Anteilen auf Trezor
---
![cover](assets/cover.webp)



*Bildnachweis: [Trezor.io](https://trezor.io/)*



## Neue Sicherungsoptionen auf Trezor



Seit 2023 bietet Trezor ein neues Sicherungsformat mit der Bezeichnung ***Single-share Backup*** an, das nach und nach das klassische BIP39-basierte Konzept der meisten Portfolios ablöst. Im Gegensatz zu den traditionellen 12- oder 24-Wort-Mnemonic-Phrasen basiert dieses neue Format auf einer einzigen 20-Wort-Phrase, die von einem von SatoshiLabs entwickelten Standard abgeleitet ist: **SLIP39**. Ziel ist es, die Robustheit und Lesbarkeit von Backups zu verbessern und gleichzeitig eine reibungslose Migration zu einem verteilten Backup-Modell zu ermöglichen.



Dieses verteilte Modell wird ***Multi-Share Backup*** genannt. Es basiert auf demselben Prinzip, aber anstatt einen einzigen Mnemonic-Satz zu erzeugen, wird dieser in mehrere Fragmente, die sogenannten ***Anteile***, aufgeteilt, von denen jeder für sich ein Mnemonic-Satz ist. Um das Portfolio wiederherzustellen, muss eine bestimmte Anzahl dieser *Anteile* (definiert durch einen *Schwellenwert*) wieder zusammengeführt werden. Bei einem 3-von-5-Schema zum Beispiel können 3 *Anteile* von 5 das Portfolio wiederherstellen. Bitte beachten Sie, dass sich das verteilte Backup-System von Trezor von Multisig-Geldbörsen unterscheidet. Um Ihre Bitcoins auszugeben, ist nur Ihr Hardware Wallet Trezor erforderlich. Es ist nur eine Unterschrift erforderlich. Die Verteilung erfolgt nur auf der Ebene des Mnemonic-Satzes, d. h. des Backups.



![Image](assets/fr/01.webp)



Dieses System löst das Problem des Single Point of Failure des Mnemonic-Satzes ohne die Nachteile, die mit der Verwaltung eines Multisig oder passphrase BIP39 verbunden sind. Der Wiederherstellungsprozess basiert nicht mehr auf einer einzigen Information, sondern auf mehreren, mit dem zusätzlichen Vorteil der Verlusttoleranz dank der Schwelle.



Benutzer, die ein Portfolio mit *Single-Share Backup* erstellt haben, können jederzeit zu *Multi-Share Backup* wechseln, ohne ihr Portfolio migrieren zu müssen. Die Empfangsadressen und Konten bleiben identisch. Das *Multi-Share*-System wirkt sich nur auf das Backup aus, während der Rest des Portfolios unverändert bleibt.



Multi-Share Backup ist auf dem Trezor Model T, Safe 3 und Safe 5 verfügbar. Diese Funktion wird vom Trezor Model One nicht unterstützt.



**Wichtiger Hinweis:** Das *Multi-Share*-System von Trezor ist kryptografisch sicher, da es das *Shamir's Secret Sharing*-Schema für die Verteilung verwendet. Wir raten dringend davon ab, ein ähnliches System manuell anzuwenden, indem Sie eine klassische Mnemonic-Phrase selbst aufteilen. Das ist eine schlechte Praxis, die das Risiko des Diebstahls und des Verlusts Ihrer Bitcoins erheblich erhöht, also tun Sie es nicht. Eine klassische Mnemonic-Phrase wird in ihrer Gesamtheit gespeichert.



## Shamirs Geheimnis teilen in SLIP39



Der kryptographische Mechanismus, der den *Multi-Share*-Backups auf Trezor zugrunde liegt, ist das *Shamir's Secret Sharing Scheme* (SSSS). Das Prinzip ist wie folgt: Geheime Informationen (in diesem Fall die seed des Portfolios) werden in ein mathematisches Polynom umgewandelt. Anschließend werden mehrere Punkte dieses Polynoms berechnet, von denen jeder ein Anteil ist. Das ursprüngliche Geheimnis wird durch Polynominterpolation rekonstruiert, indem eine Mindestanzahl von Punkten (der Schwellenwert) ermittelt wird.



Aus einer Anzahl von Anteilen unterhalb des Schwellenwerts kann keine geheime Information abgeleitet werden, was eine perfekte theoretische Sicherheit der geheimen Information garantiert. Mit anderen Worten: Selbst ein Angreifer mit unbegrenzter Rechenleistung kann seed nicht erraten, wenn der Schwellenwert nicht erreicht wird.



SLIP39 verwendet dieses Schema, um das seed-Portfolio zu verteilen. Jeder Anteil ist ein Satz mit 20 Wörtern, der aus einer Liste von 1024 Wörtern gebildet wird (anders als die BIP39-Liste).



## Einrichten eines Multi-Share-Backups auf einer Trezor



Wenn Sie Ihr Portfolio auf Trezor erstellen, haben Sie drei verschiedene Möglichkeiten:




- Verwenden Sie einen klassischen BIP39 Mnemonic-Satz mit 12 oder 24 Wörtern;
- Verwenden Sie einen einteiligen Mnemonic-Satz (SLIP39);
- Konfigurieren Sie mehrere Mnemonic-Sätze in Multi-Share (SLIP39).



Wenn Sie sich für einen SLIP39 Mnemonic-Satz mit einem Anteil entscheiden, können Sie zu einem späteren Zeitpunkt auf einen Anteil mit mehreren Anteilen aufrüsten, ohne das Portfolio zurücksetzen zu müssen. Wenn Sie hingegen mit einem klassischen BIP39-Portfolio (12- oder 24-Wort-Satz) beginnen, können Sie es nicht direkt in ein Portfolio mit mehreren Anteilen umwandeln. Sie müssen ein neues Multi-Share-Portfolio von Grund auf neu erstellen und Ihre Mittel aus dem alten Portfolio in das neue Portfolio mittels einer oder mehrerer Bitcoin-Transaktionen übertragen. Dies ist ein komplexerer und kostspieliger Vorgang. Wenn Sie diese Umstellung vornehmen wollen, empfehle ich Ihnen, einen neuen Hardware Wallet Trezor zu kaufen, damit Sie Ihren seed nicht in eine Portfoliosoftware eingeben müssen.



In diesem Lernprogramm wird zunächst gezeigt, wie man eine Mehrfachaktie bei der Erstellung eines Portfolios einrichtet. In einem späteren Abschnitt wird dann erläutert, wie man eine Einfachaktie in eine Mehrfachaktie für ein bestehendes Portfolio umwandelt.



Wenn Sie Hilfe bei der Ersteinrichtung Ihres Geräts benötigen, haben wir für jedes Trezor-Modell eine ausführliche Anleitung:



https://planb.network/tutorials/wallet/hardware/trezor-safe-5-4413308a-a1b5-4ba4-bc49-72ae661cc4e0

https://planb.network/tutorials/wallet/hardware/trezor-safe-3-51d0d669-5d23-47c2-beb6-cc6fa0fb0ea0

https://planb.network/tutorials/wallet/hardware/trezor-model-one-5c250c49-ce3b-4c63-bd05-4600d7c11a02

### Über ein neues Portfolio



Sie haben nun die Erstkonfiguration Ihres Trezor abgeschlossen und können nun das Portfolio erstellen. Klicken Sie in der Trezor Suite auf die Schaltfläche "*Neues Wallet erstellen*".



![Image](assets/fr/02.webp)



Wählen Sie die Option "*Multi-Share Backup*" und klicken Sie dann auf "*Wallet erstellen*".



![Image](assets/fr/03.webp)



Akzeptieren Sie die Nutzungsbedingungen auf Ihrer Trezor und bestätigen Sie die Erstellung des Portfolios.



![Image](assets/fr/04.webp)



Klicken Sie in Trezor Suite auf "*Sicherung fortsetzen*".



![Image](assets/fr/05.webp)



Lesen Sie die Anweisungen sorgfältig durch, bestätigen Sie sie und klicken Sie dann auf "*Wallet-Sicherung erstellen*".



![Image](assets/fr/06.webp)



Für weitere Informationen über die richtige Art und Weise, Ihre Mnemonic-Sätze zu speichern und zu verwalten, empfehle ich Ihnen diesen anderen Lehrgang, besonders wenn Sie Anfänger sind:



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Wählen Sie auf dem Trezor die Gesamtzahl der Anteile, die Sie konfigurieren möchten. Die gebräuchlichsten Konfigurationen sind 2-de-3 und 3-de-5. Für dieses Beispiel werde ich ein 2-de-3 erstellen, also 3 Anteile auswählen. Jeder Anteil steht für einen Mnemonic-Satz mit 20 Wörtern.



*Bei Safe 5-Benutzern steht zwar auf dem Bildschirm "Tippen, um fortzufahren", aber Sie müssen zur Bestätigung nach oben wischen*



![Image](assets/fr/07.webp)



Bestätigen Sie dann den Schwellenwert, d. h. die Anzahl der Anteile, die erforderlich sind, um wieder Zugang zum Wallet und den darin enthaltenen Bitcoins zu erhalten.



![Image](assets/fr/08.webp)



Der Trezor erstellt Ihre verschiedenen Freigaben (Mnemonic-Phrasen) mit Hilfe seines Zufallszahlengenerators. Vergewissern Sie sich, dass Sie während dieses Vorgangs nicht beobachtet werden. Schreiben Sie die auf dem Bildschirm angezeigten Wörter auf ein physisches Medium Ihrer Wahl. Achten Sie darauf, dass die Wörter nummeriert sind und in der richtigen Reihenfolge stehen.



Ich empfehle Ihnen, jede Freigabe auf einem separaten Medium zu notieren und ihre Aufbewahrung sorgfältig zu verwalten, um zu vermeiden, dass mehrere an einem Ort zugänglich sind. Bei einer 2-von-3-Konfiguration wie der meinen wäre es beispielsweise möglich, eine Aktie bei mir zu Hause, eine weitere bei einem vertrauenswürdigen Freund und die letzte in einem Banksafe aufzubewahren. Die Wahl des Aufbewahrungsortes hängt von Ihrer persönlichen Sicherheitsstrategie ab.



Am oberen Rand des Bildschirms sehen Sie, welche Freigabe Sie gerade sehen.



natürlich dürfen Sie diese Wörter niemals im Internet weitergeben, wie ich es in diesem Tutorial tue. Dieses Beispiel Wallet wird nur auf dem Testnet verwendet werden und wird am Ende des Tutorials gelöscht werden.



![Image](assets/fr/09.webp)



Um zu den nächsten Wörtern zu gelangen, klicken Sie auf den unteren Rand des Bildschirms. Sie können rückwärts gehen, indem Sie nach unten rutschen. Wenn Sie alle Wörter aufgeschrieben haben, halten Sie den Finger auf dem Bildschirm, um zur nächsten Aktie zu gelangen, und wiederholen Sie den Vorgang.



![Image](assets/fr/10.webp)



Am Ende jeder Aufnahme werden Sie aufgefordert, die Wörter in Ihrem Mnemonic-Satz auszuwählen, um zu bestätigen, dass Sie sie richtig aufgeschrieben haben.



![Image](assets/fr/11.webp)



Das war's. Sie haben Ihr Portfolio erfolgreich mit der Option "Mehrfache Freigabe" gesichert. Sie können nun mit dem Rest der Konfigurationsanweisungen fortfahren.



### Bei einem bestehenden Einzelaktienportfolio



Wenn Sie bereits einen Trezor Wallet mit einem Single-Share-Backup besitzen (einen SLIP39 Mnemonic-Satz, nicht den klassischen BIP39-Satz) und die Verfügbarkeit und Sicherheit Ihres Wallet-Backups verbessern möchten, können Sie ein Multi-Share-System einrichten, ohne Ihre Bitcoins übertragen zu müssen.



Verbinden Sie dazu Ihr Hardware Wallet und entsperren Sie es. Gehen Sie in der Trezor Suite zu Einstellungen.



![Image](assets/fr/12.webp)



Gehen Sie auf die Registerkarte "*Gerät*".



![Image](assets/fr/13.webp)



Klicken Sie dann auf "*Multi-Share Backup erstellen*".



![Image](assets/fr/14.webp)



Lesen Sie die Anweisungen und klicken Sie dann auf "*Multi-Share Backup erstellen*".



![Image](assets/fr/15.webp)



Dann müssen Sie auf dem Trezor-Bildschirm Ihre aktuelle Mnemonic-Phrase (Single-Share) eingeben. Wählen Sie die Anzahl der Wörter (Standard ist 20).



![Image](assets/fr/16.webp)



Verwenden Sie dann die Bildschirmtastatur des Trezor, um jedes Wort Ihres aktuellen Mnemonic-Satzes einzugeben.



![Image](assets/fr/17.webp)



Sie können dann die Konfiguration Ihres Multi-Share-Backups auswählen, indem Sie die Anweisungen im vorherigen Abschnitt befolgen.



![Image](assets/fr/18.webp)



Sobald Sie Ihr Multi-Share-Backup erstellt haben, müssen Sie entscheiden, was mit Ihrem ursprünglichen Single-Share-Mnemonic-Satz geschehen soll. Da das Bitcoin-Portfolio das gleiche bleibt, wird diese einzelne Phrase immer den Zugriff darauf ermöglichen. Dies hängt von Ihrer Sicherheitsstrategie ab, aber im Allgemeinen ist es ratsam, diese Phrase zu zerstören, um diese einzige Schwachstelle zu beseitigen, was genau das Ziel von Multi-Share Backup ist. Wenn Sie sich entscheiden, sie zu zerstören, stellen Sie sicher, dass Sie dies auf sichere Weise tun, da **sie immer noch Zugang zu Ihren Bitcoins** ermöglicht.



Herzlichen Glückwunsch, Sie sind jetzt auf dem Laufenden, was die Verwendung von Single-Share- und Multi-Share-Backups auf Trezor-Hardware-Geldbörsen betrifft. Wenn Sie Ihre Wallet-Sicherheit noch einen Schritt weiter bringen möchten, sehen Sie sich dieses Tutorial über BIP39-Passphrasen an:



https://planb.network/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Wenn Sie diese Anleitung nützlich fanden, wäre ich Ihnen dankbar, wenn Sie unten einen Green-Daumen hinterlassen würden. Sie können diesen Artikel auch gerne in Ihren sozialen Netzwerken teilen. Ich danke Ihnen sehr!



## Zusätzliche Ressourcen





- [SLIP-0039: Shamir's Secret-Sharing für Mnemonic Codes] (https://github.com/satoshilabs/slips/blob/master/slip-0039.md);
- [Multi-share Backup auf Trezor](https://trezor.io/learn/a/multi-share-backup-on-trezor);
- [Wikipedia: Shamirs geheime Teilung] (https://en.wikipedia.org/wiki/Shamir%27s_secret_sharing).