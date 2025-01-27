
name: Nakamochi

description: Benutzerfreundlicher Node-Betrieb – Wie man die Nakamochi Bitcoin- und Lightning-Node einrichtet und nutzt.


Der Betrieb einer eigenen Bitcoin- und Lightning-Node ist längst keine komplexe Aufgabe mehr, die nur Personen mit technischen Kenntnisse vorbehalten ist. Traditionell erfordert die Einrichtung und der Betrieb von Nodes fundierte Kenntnisse in den Bereichen Kryptografie, Netzwerktechnologie und Softwareentwicklung. Nakamochi ändert das, indem es Nodes für jeden zugänglich macht.

Mit Nakamochi kann jeder eine Node von zu Hause aus einrichten und betreiben, und vollständige Privatsphäre und finanzielle Unabhängigkeit erreichen. Der Betrieb einer Full Node sichert nicht nur eigene Transaktionen, sondern trägt auch zur Stärkung des Bitcoin-Netzwerks bei. Ein dezentralisiertes und widerstandsfähiges Bitcoin-Netzwerk ist auf eine breites Netzwerk von Nodes angewiesen, um seine Sicherheit und Unabhängigkeit zu gewährleisten.

### Inhalt

- Was ist Nakamochi und wie funktioniert es?
- Nakamochi einrichten
- Über das Lightning Netzwerk
- Kanäle/Channels eröffnen und erste Transaktionen im Lightning Netzwerk machen



## Was ist Nakamochi und wie funktioniert es?

Nakamochi ist eine Bitcoin-only Full Node, die sowohl das Bitcoin- als auch das Lightning-Netzwerk unterstützt. Sie umfasst eine integrierte Bitcoin- und Lightning-Wallet, die es den Nutzern ermöglicht, eine eigene, sichere Bitcoin-Node zu betreiben und gleichzeitig von der Geschwindigkeit und den niedrigen Transaktionskosten des Lightning-Netzwerks zu profitieren.

Die Nakamochi Node wird über eine mobile Node Management App verwaltet, [BitBanana (Android)](https://bitbanana.app) und [Zeus (iOS)](https://bitbanana.app), die es dir ermöglicht, sie bequem von überall zu steuern. Diese Apps fungieren als Fernbedienung für deine Node und ermöglichen es dir, direkt mit Bitcoin oder Lightning zu bezahlen, Transaktionen zu verwalten, Kanäle zu öffnen oder zu schließen, Bilanzen zu überprüfen und deine Node mühelos zu überwachen.


## Nakamochi Einrichten in nur 5 Minuten

### 1. Schritt: 

1. Nakamochi einstecken und mit dem WLAN verbinden.
2. Auf **"Setup New Wallet"** klicken und die 24-Wörter Seed Phrase notieren.
3. Nakamochi mit einem Mobile Gerät verbinden, dazu einfach den QR Code in der Node Management App (Zeus or BitBanana) scannen.
4. Für mehr Sicherheit kann ein Bildschirm Pin eingerichtet werden.

![Gerät einstecken und Seed Phrase notieren](assets/de/01.webp)

![Warten, bis die Blockchain aufgeholt hat](assets/de/02.webp)

![Neue Lightning Wallet aufsetzen](assets/de/03.webp)

![QR Code mit Node Management App scannen](assets/de/04.webp)

![Für mehr Sicherheit Bildschirm Pin einrichten](asset/de/05.webp)

_Hinweis: Warten, bis die Nakamochi-Node die Blockchain synchronisiert hat. Dieser Prozess kann je nach Internetverbindung ein wenig Zeit in Anspruch nehmen._



## Über das Lightning Netzwerk

Das Bitcoin Lightning Network revolutioniert Bitcoin-Transaktionen, indem es sie schneller, billiger und effizienter macht. Es ist perfekt für den alltäglichen Gebrauch, da es nahezu sofortige Zahlungen mit minimalen Gebühren ermöglicht, ideal für Mikrotransaktionen wie den Kauf eines Kaffees oder die Abwicklung kleiner Zahlungen.
Durch den Betrieb außerhalb der Bitcoin-Blockchain ist Lightning skalierbar und unterstützt Tausende von Transaktionen pro Sekunde, ohne die Haupt-Bitcoin-Blockchain zu überlasten. Dies macht es zu einem Schlüsselakteur in der Entwicklung von Bitcoin zu einem praktischen, globalen Zahlungssystem.
Ein weiterer Vorteil ist der Schutz der Privatsphäre, da Transaktionen auf Lightning über private Zahlungskanäle, den Channels, geleitet werden, anstatt direkt auf der Blockchain aufgezeichnet zu werden. Dies gewährleistet eine diskretere Art und Weise, Transaktionen zu tätigen, während die robuste Sicherheit von Bitcoin erhalten bleibt.



#### Zahlungskanäle erklärt

Das Lightning Network funktioniert über Zahlungskanäle, d. h. über Verbindungen zwischen zwei Parteien, die mehrere Transaktionen ermöglichen, ohne direkt mit der Blockchain zu interagieren. Wenn ein Kanal geöffnet ist, wird der Saldo zwischen den beiden Parteien bei jeder Transaktion auf dieser Lightning-Lösung der zweiten Schicht aktualisiert, was schnelle und kostengünstige Zahlungen gewährleistet. Nur das Öffnen und Schließen des Kanals wird auf der Blockchain aufgezeichnet, wodurch die Überlastung der Bitcoin-Blockchain verringert wird. Dieses gewährleistet Skalierbarkeit und Datenschutz, da einzelne Transaktionen nicht im öffentlichen Hauptbuch aufgezeichnet werden.

**Beispiel:** Alice und Bob öffnen einen Kanal, in den sie Bitcoin einzahlen. Alice sendet Bitcoin an Bob, und ihre Off-Chain-Bilanz wird sofort aktualisiert, ohne dass ein On-Chain-Eintrag erforderlich ist. Wenn Alice dann Charlie bezahlt und Alice keinen direkten Kanal zu Charlie hat, kann die Zahlung über Bobs Kanal zu Charlie weitergeleitet werden. Das Routing über Zwischen-Nodes gewährleistet Zahlungen auch ohne direkte Verbindungen, wodurch das Netzwerk hochgradig effizient wird.



## Channels eröffnen und erste Transaktionen im Lightning Netzwerk machen

Sobald dein Nakamochi eingerichtet und mit einer Node-Management-App verbunden ist, kannst du mit der Nutzung des Lightning Network beginnen, indem du Kanäle öffnen und Transaktionen durchführen.

### Channels mit Zeus (iOS) öffnen:

1. Unten auf **“Channels”** Registerkarte klicken.
2. Auf **“+”** drücken um einen neuen Channel zu eröffnen.
3. Pubkey scannen oder einfügen.
4. Einen Betrag eingeben (mit einem Peer frei wählbar, oder den Minimalbetrag für eine öffentliche Node eingeben).
5. Auf **“Open Channel”** drücken.

![ZEUS Screenshot](asset/de/06.webp)


Mehr Informationen: [Channels | Zeus Documentation](https://zeusln.app)

### Channels mit BitBanana (Android) öffnen:

1. Menü links öffnen.
2. Auf **“Channels”** drücken.
3. Auf **“+”** klicken um einen neuen Channel zu eröffnen.
4. Pubkey scannen oder einfügen.
5. Einen Betrag eingeben (mit einem Peer frei wählbar, oder den Minimalbetrag für eine öffentliche Node eingeben).

![Bitbanana Screenshot](asset/de/07.webp)

Mehr Informationen: [BitBanana](https://bitbanana.com)

Sobald dein Kanal geöffnet ist, können Zahlungen durch ihn zu anderen Teilnehmern im Netzwerk weitergeleitet werden. Die Bilanzen werden Off-Chain angepasst, wodurch Transaktionen nahezu sofort erfolgen und minimale Gebühren anfallen.

Wenn du einen Kanal nicht mehr benötigst, kannst du ihn schließen. Diese Aktion begleicht die endgültige Bilanz zwischen dir und deinem Peer und zeichnet sie On-Chain auf. Idealerweise stimmen beide Parteien zu und sind online für einen “cooperative close”, einem gemeinsamen Abschluss (schneller und mit geringeren Gebühren im Vergleich zu einem „forced close", einem forcierten Abschluss, mit einem nicht reagierenden/offline Partner).

Im Allgemeinen empfehlen wir, Kanäle offen zu lassen, um Kosten zu senken und die Zuverlässigkeit sowie Effizienz des Netzwerks zu steigern. Indem Kanäle offen gehalten werden, werden On-Chain-Transaktionsgebühren minimiert, Ausfallzeiten bei der Kanalwiederherstellung vermieden und stabile Routing-Kapazität für nahtlose Zahlungsabwicklungen erhalten. Dieser Ansatz fördert ein robustes und widerstandsfähiges Netzwerk, verbessert die gesamte Benutzererfahrung und reduziert den betrieblichen Aufwand.


### Nützliche Links

- [Über Nakamochi](https://nakamochi.io/)
- [Newsletter abonnieren](https://90c7addc.sibforms.com/serve/MUIFAHG7H5YBPpm-kZ8G6TuS-nmL4uaq85rlpBfI__S79tZ5jheIJfF3kJYudycgs_6_RUdDBkt8Sd7OyNL_JDTTJvOb36ifF6vcQoabBXKp4cbefzh1DYqnok_jItexICcQL13ucd2aS581ngqy7jr0Q1H3HhxV3z2eWKE5-Z-YMasj-MMotQeDvdorMCSi0XgCWDqs8rEMQC7E)
