---
name: Amboss
description: Lightning Network erforschen und analysieren
---

![cover](assets/cover.webp)



Lightning Network ist eine Layer des Bitcoin-Protokolls, das in erster Linie entwickelt wurde, um die Annahme von Bitcoin-Zahlungen im Alltag zu fördern, indem die Verarbeitungsgeschwindigkeit jeder Transaktion erhöht wird. Lightning Network basiert auf dem Prinzip der Dezentralisierung und besteht aus Knoten (Computern, auf denen eine Lightning-Implementierung läuft), die Peer-to-Peer kommunizieren und Daten (Zahlungen und Zahlungsüberprüfungen) aneinander weiterleiten.



https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

Genau wie auf der Hauptkette ist es wichtig, dass die Nutzer die Informationen und den Status des Netzes kennen, um die Verbindungen zwischen den Knoten zu erleichtern und das Liquiditätsproblem, das im Allgemeinen im Netz auftritt, zu minimieren. In der Tat empfehlen wir auf Lightning Network Kleinstzahlungen von relativ kleineren Beträgen als bei den Transaktionen auf der Bitcoin-Hauptkette.



Es ist wichtig zu wissen, dass nicht alle Lightning-Knoten auf der Amboss-Plattform verfügbar sind.



Wie [Mempool Space](https://Mempool.space), das nützliche Informationen über die Hauptkette des Bitcoin-Protokolls liefert, bietet seit 2022 [Amboss](https://amboss.space) Informationen über :





- Knotenpunkte auf dem Lightning Network
- Zahlungskanäle und ihre Zahlungskapazität
- Lightning Network Entwicklung im Laufe der Zeit
- Statistiken über die Gebühren für Ihre Zahlungen an die Relaisknoten.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f

In diesem Tutorial nehmen wir Sie mit auf einen Rundgang durch diese Plattform, die eine wesentliche Ressource für Lightning Network-Benutzer ist, für diejenigen, die ihren Knotenpunkt verbinden möchten, um das Netzwerk zu erweitern, usw.




## Paare finden



Eines der Ziele der Amboss-Plattform ist es, die verschiedenen Knotenpunkte des Netzwerks miteinander zu verbinden und Informationen auszutauschen. Auf der Startseite der Plattform können Sie direkt nach dem Namen eines Knotens suchen, den Sie bereits kennen, oder Knoten aus den beliebtesten Lightning-Portfolios finden, die Sie verwenden.



![home](assets/fr/01.webp)



![wallet](assets/fr/02.webp)



https://planb.academy/tutorials/wallet/mobile/blixt-04b319cf-8cbe-4027-b26f-840571f2244f

Auf der Startseite finden Sie auch Knotenpunkte, die nach :




- Kapazitätsentwicklung: die Menge an Bitcoin, die mit dem öffentlichen Schlüssel des Knotens verbunden ist, und die insgesamt in allen seinen Kanälen verfügbare Menge.
- Kanalentwicklung: die Anzahl der neuen Verbindungen zu anderen Knoten im Netz.
- Knotenpopularität: wie oft der Knoten verwendet wird.



![nodes](assets/fr/03.webp)



Bei der Auswahl des richtigen Knotens für die Verbindung müssen also folgende Kriterien berücksichtigt werden:





- Vergewissern Sie sich, dass der Knotenpunkt über eine ausreichende Menge an Bitcoins verfügt; je größer die Kapazität des Knotenpunkts ist, desto größer ist der Betrag an Bitcoins, den Sie bezahlen können.





- Stellen Sie sicher, dass der Knoten eine große Anzahl von Verbindungen und offenen Kanälen zu anderen Knoten im Netz hat.





- Vergewissern Sie sich, dass der Knoten aktiv ist und immer noch von seinen Kollegen geschätzt wird, indem Sie die Anzahl der neuen Kanäle überprüfen; je mehr neue Kanäle dieser Knoten geöffnet hat, desto mehr wird er von den anderen Knoten im Netzwerk geschätzt.



Wenn Sie den richtigen Knoten gefunden haben, klicken Sie auf seinen Namen, um zur Seite mit den Knoteninformationen weitergeleitet zu werden.



Auf diesem Interface erhalten Sie, indem Sie den Timestamp des neu erstellten Kanals überprüfen, einen Hinweis auf die Aktivität dieses Knotens. Sie finden dort auch Informationen über die Kapazität der Kanäle dieses Knotens: Diese Informationen sind wichtig, wenn Sie diesen Knotenpunkt aktiv für Ihre Zahlungen nutzen wollen.




![node_info](assets/fr/04.webp)



Im linken Bereich finden Sie weitere Informationen über den Standort dieses Knotens. Sie können zum Beispiel anzeigen:




- Der öffentliche Schlüssel: die Kennung direkt unter dem Knotennamen.
- Die geografische Position dieses Knotens.




![channels](assets/fr/05.webp)



Diese Interface teilt Ihnen die Verbindungs-Address für diesen Knoten mit: Sie hat die Form `pubkey@ip:port`. In unserem Beispiel wollen wir eine Verbindung zu dem Knoten herstellen, dessen :




- der öffentliche Schlüssel `pubkey` ist: `035e4ff418fc8b5554c5d9eea66396c227bd429a3251c8cbc711002ba215bfc226`
- iP Address: `170.75.163.209`
- Der Anschluss: `9735`



![geoinfo](assets/fr/06.webp)



Im Abschnitt **Kanäle** sehen Sie die Liste der offenen Kanäle und die Verbindungen des Knotens zu anderen Knoten im Netz. Auf dieser Interface sind mehrere Informationen wichtig, um zu bestätigen, dass dieser Knoten unseren Anforderungen entspricht oder zuverlässig ist:





- Eingehende Quote**: Der Betrag, den der Knoten für jede Million Satoshi, die er empfängt, in Rechnung stellt, abhängig vom gewählten Kanal.
- Das Verhältnis (Teile pro Million)** : Es stellt die Anzahl der Satoshi pro Million Einheiten dar, die der Knotenpunkt Ihnen in Rechnung stellt, wenn Sie sich entscheiden, eine Zahlung über einen seiner Kanäle vorzunehmen. Angenommen, Sie entscheiden sich, eine Zahlung von `10_000 Sats` über einen Kanal zu tätigen, dessen ppm-Verhältnis `500 Sats` ist, dann müssen Sie dem Knoten `10_000 * 500 / 1_000_000` Satoshis zahlen, was `5 Sats` entspricht.
- Das [HTLC](https://planb.academy/resources/glossary/htlc) Maximum** : Der Höchstbetrag, den dieser Knoten Ihnen erlaubt, über einen dieser Kanäle zu übertragen.



In der Tabelle in dieser Interface finden Sie alle diese Informationen auch über den Knoten, dem er zugeordnet ist.



![channels_info](assets/fr/07.webp)



Im Abschnitt **Kanalpläne** können Sie die Verteilung und Kapazität der verschiedenen Kanäle auf diesem Knoten sehen. Sie können die angezeigten Verteilungskriterien ändern, indem Sie eine der Optionen in der Dropdown-Liste auf der rechten Seite auswählen.



![cha_maps](assets/fr/08.webp)



Der Abschnitt **Geschlossene Kanäle** gruppiert alle ehemaligen Kanäle des Knotens nach der Art der Schließung:




- Gegenseitiges Schließen**: ist die Zustimmung beider Parteien, die mit ihrem privaten Schlüssel die Transaktion unterzeichnen, die das Schließen des Kanals und die Verteilung der Guthaben innerhalb des Kanals markiert
- Eine **erzwungene Schließung**: stellt die abrupte, einseitige Schließung eines Teils des Kanals dar. Diese Art der Schließung wird nicht empfohlen, da Lightning Network ein auf Bestrafung basierendes Protokoll ist: Wenn Sie versuchen, das Gleichgewicht eines Kanals zu betrügen, riskieren Sie, Ihr gesamtes verfügbares Gleichgewicht in diesem Kanal zu verlieren.



![closed](assets/fr/09.webp)



Informieren Sie sich über die Transitgebühren für die Weiterleitung Ihrer Zahlungen über einen Kanal an dem von Ihnen verwendeten Knotenpunkt



![fees](assets/fr/10.webp)



## Informationen zum Netzwerk



Amboss konzentriert sich nicht nur auf Informationen über die Netzwerkmitglieder, sondern auch auf den Zustand des Netzwerks selbst.



Im Bereich **Statistik** finden Sie unter dem linken Menüpunkt "Simulationen" eine Grafik, die die Wahrscheinlichkeit einer erfolgreichen Zahlung in Abhängigkeit vom Zahlungsbetrag darstellt.



Tatsächlich werden Sie feststellen, dass die Kurve abnimmt, denn je höher der Betrag Ihrer Zahlung ist, desto geringer ist die Chance, dass diese Zahlung auch tatsächlich erfolgt. Dies spiegelt das echte Liquiditätsproblem von Lightning Network wider. Zum Beispiel hat Ihre Zahlung von 10_000 Satoshis eine Wahrscheinlichkeit von 79 %, dass sie ausgeführt wird. Bei einer Zahlung von 3_000_000" Satoshis hingegen haben Sie eine Chance von weniger als 13%.



![network](assets/fr/11.webp)



Das Menü **Netzwerkstatistik** ermöglicht die grafische Anzeige von Statistiken für :




- Zahlungskanäle
- Knotenpunkte
- Kapazität
- Gebühren
- Kanalentwicklung.



![network_stat](assets/fr/12.webp)



Im Menü **Marktstatistiken** können Sie mit der Option **Auftragsdetails** die Nachfrage nach Liquidität auf der Lightning Network einsehen. Dieses Diagramm kann auch zeigen, welche Kanäle am stärksten nachgefragt werden und/oder welche eine hohe Kapazität haben.



![markets](assets/fr/13.webp)




## Werkzeuge



Amboss bietet eine Reihe von Tools, die Ihnen bei der Optimierung Ihrer Suchen und Aktionen helfen.



### Lightning Network Decoder



Dieses Tool ist hauptsächlich dafür verantwortlich, Ihnen Details über die Struktur eines Lightning Invoice, Lightning Address oder Lightning URL zu geben.



Übermitteln Sie auf der Startseite im Abschnitt **Tools** zum Beispiel Ihren Lightning Address.



![decoder](assets/fr/14.webp)



Mit diesem Decoder können Sie Informationen erhalten wie :




- den öffentlichen Schlüssel des Knotens, der mit Ihrem Lightning Address verbunden ist;
- Die Verfallszeit eines Invoice von Ihrem Address;
- Das Minimum und Maximum, das Sie senden können;
- Der mit Ihrem Address verbundene Nostr-Knoten, wenn Nostr auf diesem Knoten aktiviert ist.



![decode](assets/fr/15.webp)



### Magma IA



Entdecken Sie das neueste von Amboss vorgestellte Tool zur effizienten Verwaltung Ihrer Verbindungen zu Lightning Network-Knoten. Magma AI nutzt eine spezielle künstliche Intelligenz, um sich auf ein wichtiges Problem zu konzentrieren: eine gute Auswahl der Knoten, mit denen eine Verbindung hergestellt werden soll.



![magma](assets/fr/16.webp)



### Satoshi-Rechner



Ermitteln Sie den aktuellen Preis von Bitcoin in Ihrer Landeswährung (EUR / USD). Verwenden Sie auf der Startseite den Satoshi-Rechner, um den aktuellen Marktpreis zu ermitteln.



![calculator](assets/fr/17.webp)




Sie haben nun einen vollständigen Überblick über die Funktionen und Analysewerkzeuge der Plattform erhalten. Nachfolgend finden Sie unseren Artikel über den Bitcoin **Mempool.space**-Explorer.



https://planb.academy/tutorials/privacy/explorer/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f