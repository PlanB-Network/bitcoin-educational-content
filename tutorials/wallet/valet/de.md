---
name: Diener Bitcoin
description: Valet bringt den nicht verwahrten Lightning-Knoten in Ihre Tasche
---

![cover_valet](assets/cover.webp)



## Einführung


Valet ist ein leichtes, selbstverwaltendes Bitcoin- und Lightning-wallet-System, das Anfängern einen einfachen und bequemen Einführungsprozess bietet. Es wurde speziell für Bitcoin-Gemeinschaften und Kreislaufwirtschaften, insbesondere in abgelegenen Gebieten, entwickelt.


Es handelt sich um einen fork des **Einfachen Bitcoin Wallet (SBW)**, mit einer fortschrittlichen Hosted Lightning-Channel-Funktion namens **Fiat Channels**, die es jedem ermöglicht, Lightning-Zahlungen ohne Volatilitätsrisiken zu akzeptieren.


Valet ist derzeit nur für Android-Geräte verfügbar und kann von mehreren App-Stores mit offenem Quellcode heruntergeladen und installiert werden. Valet wird jedoch **nicht** im **Google Play Store** gehostet, da Entwickler Bedenken hinsichtlich des Datenschutzes und der KYC haben.



## Valet herunterladen und installieren


Valet kann als APK-Datei von der GitHub-Seite von Standard Sats heruntergeladen werden. [Standard Sats](https://standardsats.github.io/) ist das Unternehmen, das Valet entwickelt hat.


👉 Um Valet herunterzuladen, besuchen Sie die Standard-Sats [GitHub-Seite] (https://github.com/standardsats/valet/releases), und suchen Sie die **aktuellste** Version (dies ist oft die oberste).


👉 Gehen Sie zu **Assets** und klicken Sie auf die Datei mit der Erweiterung **.apk**. Ihr Download wird automatisch gestartet.


![Standard_Sats_GitHub_page_view](assets/en/001.webp)


sobald der Download abgeschlossen ist, gehen Sie zum **Dateimanager** > **Downloads** Ihres Geräts und wählen Sie die Valet apk-Datei aus.


![Select_valet_apk](assets/en/002.webp)


👉 Installieren Sie sie, und in wenigen Sekunden ist Ihre App fertig und erscheint auf Ihrem Startbildschirm.


![valet_icon_on_homescreen](assets/en/003.webp)


Alternativ können Sie Valet auch aus dem **F-Droid** App Store herunterladen. Wenn Sie die F-Droid-App nicht auf Ihrem Gerät haben, können Sie sie [hier] herunterladen und installieren (https://f-droid.org/en/).


öffnen Sie auf Ihrem Startbildschirm F-Droid und suchen Sie nach **Valet**. Wählen Sie die erste Option mit einem **lila-weißen Symbol** aus den beiden angezeigten Optionen aus und klicken Sie auf **Herunterladen**.


![F-Droid_icon_on_homescreen](assets/en/004.webp)


![search_and_download_Valet](assets/en/005.webp)


👉 Klicken Sie nach dem Herunterladen auf **Installieren** und folgen Sie den Anweisungen auf dem Bildschirm. Wenn die Installation abgeschlossen ist, können Sie Valet von F-Droid aus starten, indem Sie auf **Öffnen** klicken, oder es vom Startbildschirm Ihres Geräts aus starten.



## Erstellen eines Bitcoin Wallet


Sie können einen Bitcoin wallet auf Valet in zwei einfachen Schritten einrichten.


starten Sie Valet über den Startbildschirm Ihres Geräts oder über die F-Droid-App. Es wird ein wallet-Einrichtungsbildschirm mit zwei Optionen angezeigt: **Neues Wallet erstellen** und **Vorhandenes Wallet wiederherstellen**.


wählen Sie **Neues Wallet erstellen**, und sofort wird ein neues wallet erstellt, und Sie werden zur Startseite weitergeleitet.


![set_up_a\_new_wallet](assets/en/006.webp)



## Sichern Sie Ihre Seed-Phrase


👉 Klicken Sie auf der wallet-Startseite auf die **Green-Karte** mit der Aufschrift **"Tippen Sie hier, um die wallet-Wiederherstellungsphrase zu speichern, falls Sie Ihr Gerät einmal verlieren oder austauschen sollten".**


![seed_phrase_green_card](assets/en/007.webp)


👉 Eine Reihe von 12 englischen Wörtern wird angezeigt. Schreiben Sie sie in der Reihenfolge von 1 bis 12 auf und bewahren Sie sie auf.


![the_seed_phrase](assets/en/008.webp)


### Achtung ⚠️:


Achten Sie auf die folgenden Elemente:


- Wie Sie bereits wissen, ist Valet ein selbstverwahrender wallet, so dass Ihr seed-Satz der einzige Zugang zur Wiedererlangung Ihres Wallet ist.
- Wenn Sie Ihren seed-Satz jemals verlieren, werden Sie **niemals** Zugang zu Ihrem wallet erhalten.
- Wenn jemand Ihren seed-Satz erhält, kann er unwiederbringlich alle Ihre Bitcoin stehlen.


Sie müssen also Ihren seed-Satz mit 12 Wörtern aufschreiben und ihn an einem sicheren Ort aufbewahren. Sie sollten niemals einen Screenshot machen, ihn als Entwurf in Ihrer E-Mail speichern oder ihn auf einem elektronischen Gerät speichern, das jemals mit dem Internet verbunden war.


https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

## Empfangen und Versenden von Bitcoin auf Valet


Valet ist ein selbstverwahrender wallet mit on-chain- und Lightning-Bitcoin-Fähigkeit. Das bedeutet, dass Sie Bitcoin aus Valet entweder über eine **On-chain** oder über einen **Lightning Network** empfangen und senden können.


Um jedoch Bitcoin über Lightning empfangen oder senden zu können, müssen Sie einen Lightning-Kanal mit Ihren on-chain Bitcoin als Liquidity einrichten. Oder Sie können einige Lightning-Kanal Liquidität von Anbietern kaufen.



## Erzeugen eines On-chain Bitcoin Address


Um Bitcoin über on-chain zu empfangen, müssen Sie eine Bitcoin-Adresse erstellen.


auf der wallet-Startseite sehen Sie eine **Orange** und eine **Lila Karte**, die mit **Bitcoin** bzw. **Lightning** bezeichnet sind.


klicken Sie auf die orangefarbene Karte mit der Aufschrift **Bitcoin**. Sie werden zu einem Bildschirm mit einer Bitcoin-Adresse weitergeleitet.


![click_on_Bitcoin_card](assets/en/009.webp)


sie können die Adresse **kopieren** und sie an die Person senden, die Ihnen Bitcoins schickt, oder auf die Schaltfläche **freigeben** klicken, um den QR-Code über soziale Medien oder andere Kommunikationskanäle an die Person zu senden.


sie können auch auf die Schaltfläche **Bearbeiten** klicken, um die Anzahl der Bitcoin festzulegen, die an diese Adresse gesendet werden sollen.


**Achtung:** Wie bei einer Rechnung ist die Bearbeitungsfunktion in Szenarien nützlich, in denen Sie vielleicht eine bestimmte Menge an Bitcoin an eine Adresse zu einem bestimmten Zeitpunkt erhalten möchten; dies bedeutet jedoch nicht, dass die Adresse keine höheren oder niedrigeren Beträge erhalten kann.


👉Klicken Sie auf **Mehr frische Adressen**, um neue Zufallsadressen zu generieren.


![generating_a\_bitcoin_add](assets/en/010.webp)


sie können auch eine on-chain Bitcoin-Adresse generieren, indem Sie auf die Schaltfläche **Empfangen** unten auf Ihrer wallet-Startseite klicken. Wählen Sie dann **Empfangen an Bitcoin-Adresse**, und fahren Sie mit dem oben beschriebenen Verfahren fort.


![click_receieve_button](assets/en/011.webp)


![receive_to_bitcoin_address](assets/en/012.webp)



## Senden von Bitcoin über On-Chain


Das Senden von Bitcoin aus dem Valet wallet über on-chain ist eine einfache Aufgabe.


klicken Sie unten auf der Startseite Ihres wallet auf die Schaltfläche **Senden**, geben Sie die Bitcoin-Adresse ein, oder klicken Sie auf **Scannen**, um den QR-Code der Adresse zu scannen, und klicken Sie dann auf **Ok**.


![click_send_button](assets/en/013.webp)


![enter_bitcoin_add](assets/en/014.webp)


👉 Geben Sie den Bitcoin-Betrag ein, den Sie senden möchten. Sie können manuell einen Betrag in Sats oder in Fiat-Währung eingeben, oder Sie können auf **Max** klicken, um Ihr gesamtes on-chain-Guthaben zu verwenden.


sie können auch die Gebühren für die Transaktion anpassen, indem Sie auf das kleine grüne Kästchen mit der Aufschrift **Gebühr** klicken und dann den weißen Punkt nach rechts oder links schieben, um die Gebühren zu erhöhen bzw. zu verringern. Klicken Sie auf **Ok**, um die Transaktion zu senden.


![enter_amount_and_fee_rate](assets/en/015.webp)



## Einrichten eines Lightning Network-Kanals


Wie bereits erwähnt, handelt es sich bei Valet um ein selbstverwaltetes Bitcoin und Lightning wallet; um also Bitcoin über das Lightning-Netzwerk senden und empfangen zu können, müssen Sie zunächst einen Lightning-Kanal einrichten, indem Sie diese Schritte befolgen:


👉 Klicken Sie auf dem Startbildschirm auf die **Lila Karte** mit der Aufschrift **Blitz**. Sie werden zu einer Seite mit den folgenden Optionen weitergeleitet:



- QR-Knoten scannen
- Kaufen bei LNBIG.COM
- Kaufen bei BITREFILL.COM
- LN-Diagramm-Neusynchronisierung anfordern.


Wenn Sie **Kaufen Sie bei lnbig.com** oder **Kaufen Sie bei bitrefill.com** wählen, werden Sie zu den Websites dieser Unternehmen weitergeleitet, wo Sie eine eingehende Liquidität mit verschiedenen Kapazitäten erwerben können. Ignorieren Sie die letzte Option **LN Graphen-Neusynchronisierung anfordern** vorerst.


Unsere erste Wahl ist also **einen Knoten QR** scannen. Zu diesem Zeitpunkt müssen Sie den **QR-Code** des Knotens, zu dem Sie einen Kanal öffnen möchten, ermittelt haben. Sie können Kanäle zu jedem öffentlichen Knoten Ihrer Wahl öffnen. Rufen Sie [1ML] (https://1ml.com/) oder [Amboss] (https://amboss.space/) auf, wählen Sie einen öffentlichen Knoten Ihrer Wahl aus und scannen Sie den zugehörigen QR-Code des gewählten Knotens.


![channel_opening_options](assets/en/016.webp)


👉 Sie werden automatisch zur nächsten Seite weitergeleitet, auf der Sie nun Ihren Kanal finanzieren müssen. Auch hier erfordert die selbstverwaltete Lightning-Netzwerknutzung, dass Sie Ihre Bitcoin zur Finanzierung eines Channels verwenden. Das bedeutet, dass Sie Bitcoin in Ihrem on-chain wallet haben müssen, um den Lightning-Kanal zu finanzieren. Bitte lesen Sie diesen Artikel von [Hacken] (https://hacken.io/discover/lightning-network/), um mehr über das Lightning-Netzwerk zu erfahren.


![fund_channel](assets/en/017.webp)


geben Sie die **Anzahl** der Bitcoin ein, mit denen Sie den Kanal finanzieren möchten, oder klicken Sie auf **Max**, um Ihr gesamtes on-chain Bitcoin-Guthaben zu verwenden. Sie können die **Gebühr** anpassen oder die Standardeinstellung beibehalten und auf **Ok** klicken.


**Achtung:** Der Betrag, mit dem Sie den Kanal finanzieren, entspricht der Kapazität Ihres neuen Kanals (d. h. dem Gesamtvolumen von Sats, das zu und von diesem Kanal abgewickelt werden kann)


Es ist auch wichtig, dass Sie mehr als **100.000 Sats** als Finanzierungsbetrag verwenden, wenn Sie einen Kanal öffnen. Dies liegt daran, dass viele Blitzknoten eine Mindestkapazität von 100.000 Sats erfordern, um einen Kanal zu ihnen zu öffnen. Um also Fehlversuche zu vermeiden, verwenden Sie einfach höhere Beträge als diesen Bereich.


![enter_funding_amount](assets/en/018.webp)


![funding_approval](assets/en/019.webp)


wenn Sie zu diesem Zeitpunkt Ihre wallet-Homepage aufrufen, sehen Sie, dass Ihr Finanzierungsbetrag von der **Bitcoin-Karte** auf die **Lightning-Karte** übertragen wurde. In Ihrem Transaktionsverlauf sehen Sie, dass die Finanzierungstransaktion bearbeitet wird.


![channel_funding_processing](assets/en/020.webp)


wenn Sie auf die Lightning-Karte klicken, sehen Sie die Information, dass Ihr Lightning-Kanal geöffnet ist. Außerdem sehen Sie die **Channel-Finanzierungstransaktion** in Ihrer Liste der Transaktionen. Warten Sie, bis Ihre Finanzierungstransaktion auf der blockchain bestätigt wird, und Ihr Lightning-Kanal ist bereit.


![channel_opening](assets/en/021.webp)


sobald die Finanzierungstransaktion bestätigt ist, klicken Sie auf Ihrer Homepage auf die **Lightning-Karte**, und Sie erhalten die folgenden Informationen zu Ihrem Lightning-Kanal:



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Dies sind die IP-Adressen der Knotenpunkte. (IPV4 und IPV6, jeweils)
- KAPAZITÄT:** Dies ist das Gesamtvolumen von Sats, das über diesen Kanal gesendet und empfangen werden kann
- KANN SENDEN:** Dies ist die Menge an Sats, die Sie zu diesem Zeitpunkt aussenden können. Sie werden feststellen, dass dies fast die gleiche Zahl wie die **Kapazität** ist. Das liegt daran, dass Sie noch keine Zahlungen über den Kanal verschickt haben.
- KANN EMPFANGEN:** Dies ist die Anzahl der Sats, die Sie auf diesem Kanal im Moment empfangen können. (Sie wird zu diesem Zeitpunkt gering bis gar nicht sein, da Sie, um empfangen zu können, zuerst einige Sats aussenden müssen, um eine eingehende Liquidity zu erzeugen)
- ERSTATTUNGSFÄHIG:** Hier wird der Betrag angezeigt, der an Ihre on-chain-Adresse zurückgezahlt wird, wenn Sie Ihren Kanal schließen. Dies wird auch als **Lokalsaldo des Kanals** bezeichnet. Das liegt daran, dass Sie bei der Schließung eines Channels eine Gebühr für die Veröffentlichung der Schließungstransaktion auf dem blockchain entrichten müssen, genauso wie Sie es bei der Finanzierung des Channels getan haben. Das System hat also den ungefähren niedrigsten Betrag abgezogen, den Sie zahlen müssen)
- WERT IM FLUG:** Wenn jemand sats an Ihren Kanal sendet oder wenn Sie versuchen, sats an jemanden zu senden, und die Transaktion aus irgendeinem Grund verzögert wird, wird dies oft in diesem Feld angezeigt.


![channel_info](assets/en/022.webp)


## Senden von Sats durch Ihren Kanal


Das Senden von Sats über den Lightning Network ist eine einfache Aufgabe.


klicken Sie unten auf der Startseite auf **Senden**, und fügen Sie die Lightning-Rechnung (Sie müssen sie kopiert haben) in das dafür vorgesehene Feld ein, oder klicken Sie auf **Scannen**, um den QR-Code der Lightning-Rechnung zu scannen.


![click_send_or_scan](assets/en/023.webp)


Die meisten Lightning-Rechnungen enthalten einen bereits eingegebenen Betrag, der zu zahlen ist. In einigen wenigen Fällen kann es sich aber auch um eine offene Rechnung handeln, bei der Sie den Betrag selbst eingeben müssen.


👉 Geben Sie den Betrag in **Dollar** oder **Sats** ein, oder klicken Sie auf **Max**, um das gesamte Guthaben auf Ihrem Blitzkanal zu verwenden, und klicken Sie dann auf **Ok**. Sobald ein guter Pfad gefunden wurde, wird Ihre Zahlung gesendet und innerhalb weniger Sekunden abgeschlossen. Behalten Sie die Startseite im Auge, um zu sehen, ob die Zahlung abgeschlossen wurde. Sie erhält ein grünes Häkchen, wenn sie abgeschlossen ist.


![enter_the_amount](assets/en/024.webp)


## Empfang von Sats über Ihren Kanal


Der Empfang von Zahlungen über Ihren Lightning-Kanal hängt weitgehend davon ab, ob Sie eine eingehende Liquid-Liquidität haben oder nicht. Nachdem Sie einen Kanal eröffnet haben, können Sie erst dann Zahlungen empfangen, wenn Sie zumindest einige Sats gesendet haben, um am anderen Ende der Kanalverbindung **eingehende Liquidität** zu schaffen. Um festzustellen, ob Sie Sats empfangen können und wie viel Sats Sie empfangen können, überprüfen Sie das Feld **Kann empfangen** in Ihren Kanalinformationen. Dadurch wird Ihnen angezeigt, wie viele Sats Sie zu jedem Zeitpunkt empfangen können.


Nehmen wir an, Sie haben einige Sats von Ihrem Kanal ausgesendet, Sie haben nun eingehende Liquidität und können Sats empfangen.


Um über den Lightning-Kanal zu empfangen, müssen Sie eine Rechnung erstellen. Im Gegensatz zu Bitcoin on-chain, das Adressen verwendet, verwendet das Lightning-Netzwerk Rechnungen. Es gibt zwei Möglichkeiten, eine Rechnung auf Valet zu erstellen.


#### OPTION 1


👉 Klicken Sie unten auf der Startseite auf **Empfangen**, wählen Sie **Empfangen auf Blitzrechnung**. Geben Sie den zu erhaltenden Betrag in die Rechnung ein, und klicken Sie auf **Ok**. Kopieren Sie die Rechnung oder teilen Sie den QR-Code mit dem Zahlungspflichtigen.


![receive_to_channel](assets/en/025.webp)


![fill_invoice_amount](assets/en/026.webp)


![copy_invoice_or_share_QR](assets/en/027.webp)


#### OPTION 2


👉 Klicken Sie auf die lila Blitzkarte auf Ihrer wallet-Startseite. Tippen Sie irgendwo auf Ihren Kanal, und eine Liste mit Optionen wird angezeigt. Wählen Sie **Empfangen auf Kanal** und geben Sie den Betrag ein, den Sie erhalten (entweder in Sats oder in Dollar). Sie werden auch sehen, wie viele Sats Sie empfangen können (eingehende Kapazität), wenn Sie die Rechnung ausfüllen. Klicken Sie auf **Ok** und kopieren Sie die Rechnung oder teilen Sie den QR-Code mit dem Zahlungspflichtigen.


![receive_to_channel](assets/en/028.webp)


**Achtung:** Die erste Option ist eine universelle Option, d. h., wenn Sie mehr als einen aktiven Kanal haben und die erste Option verwenden, wählt das System automatisch einen Ihrer Kanäle für den Empfang des Sats aus.


In diesem Szenario ist also die zweite Option am besten geeignet, wenn Sie Sats für einen bestimmten Kanal empfangen möchten.


### Ihre Kanal-Pop-Up-Optionen erklärt


Wenn Sie auf Ihren Kanal tippen, werden die folgenden Optionsfelder angezeigt:


![channel_pop_ups](assets/en/029.webp)


**SHARE LIGHTNING CHANNEL DETAILS:** Damit können Sie Ihre Channel-Details teilen, wie z.B. Remote-Peer-ID, lokale Channel-ID, Funding-Transaktion, Erstellungsdatum, usw.


**KANAL ZUM WALLET SCHLIESSEN:** Sie können Ihren Blitzkanal jederzeit schließen. Um Ihren Kanal zu schließen, prüft das System den Bitcoin-Saldo, den Sie auf Ihrer eigenen Seite des Kanals haben (denken Sie an das Feld **"Can Send "**, auch bekannt als Ihr lokaler Saldo), und schickt ihn an Sie zurück. In Valet können Sie wählen, wohin der Bitcoin gesendet werden soll, wenn der Kanal geschlossen wird. So ist **Kanal zu wallet schließen** eine der beiden Optionen.


👉 Klicken Sie auf diese Option und wählen Sie **Bitcoin**. Die Schließung des Kanals wird eingeleitet, und der Saldo Ihres Kanals Bitcoin wird an die on-chain-Adresse Ihres wallet zurückgesendet.


![close_channel_to_wallet](assets/en/030.webp)


**KANAL AN ADDRESS SCHLIESSEN:** Dies ist die zweite Option zum Schließen eines Kanals. Wenn Sie diese Option wählen, werden Sie aufgefordert, eine wallet-Adresse einzugeben, an die der Bitcoin-Saldo Ihres Kanals gesendet werden soll. Bitte beachten Sie, dass Sie bei dieser Option nur den QR-Code der Bitcoin-Adresse scannen können, an die Sie den Kanal schließen möchten. Derzeit gibt es keine Option für das manuelle Einfügen der Adresse.


klicken Sie auf diese Option, scannen Sie die Bitcoin-Adresse, und klicken Sie auf **Ok**. Die Schließung des Kanals wird eingeleitet, und Ihr Lightning Bitcoin-Guthaben wird an die gescannte Adresse gesendet.


![scan_address_and_Ok](assets/en/031.webp)


**RECEIVE TO CHANNEL:** Dies ist dasselbe wie das Erstellen einer Rechnung, aber in einigen Fällen können Sie mehr als einen Kanal haben, einschließlich Fiat-Kanäle (eine einzigartige Art von Blitzkanal, der im Valet wallet erhältlich ist). Wenn Sie also mehrere Kanäle geöffnet haben, stellt diese Option sicher, dass Sie die Zahlung an einen bestimmten Kanal erhalten können.


**AUFFÜLLEN VON ANDEREN KANÄLEN:** Diese Option ist eine Funktion, die es Ihnen ermöglicht, einen Kanal aus anderen vorhandenen Kanälen aufzufüllen. Wenn Sie beispielsweise 2 verschiedene Lightning-Kanäle (A und B) haben und das Guthaben des Bitcoin auf Kanal A aufgebraucht ist, können Sie mit dieser Option das Guthaben von Kanal A einfach und automatisch von Kanal B auffüllen.


**DIREKT NICHT PRIVAT EMPFANGEN:** Dies ist auch eine Option, um eine Rechnung zu erstellen, um die Zahlung zu erhalten, aber wenn Sie diese Option verwenden, zahlt der Absender Sie direkt. Das bedeutet, dass die Zahlung nicht wie bei einer normalen Lightning-Zahlung über verschiedene Knotenpunkte läuft, bevor sie Sie erreicht. Der Absender weiß also im Wesentlichen, dass er Sie bezahlt hat, kennt Ihre Channel-ID usw. Diese Option kann häufig verwendet werden, wenn Sie eine Zahlung von einer vertrauenswürdigen Quelle erhalten und Ihre Privatsphäre nicht schützen müssen.


## Gehostete und Fiat-Kanäle


Wie viele andere Bitcoin wallet ist auch Valet ein einfaches, leichtes Bitcoin und Lightning wallet. Es verfügt jedoch über eine einzigartige Lightning-Funktion, die es von den meisten anderen Bitcoin wallet unterscheidet. Diese Funktion heißt **Hosted and Fiat Channels**.


Fiat-Kanäle sind eine Art von Lightning-Implementierung, die ein einfaches Onboarding und die Nutzung des Lightning-Netzwerks ermöglicht. Es handelt sich um eine Verwahrungslösung, die wie bei einem normalen Lightning-Kanal volle Anonymität ermöglicht. Die Fiat-Channel-Technologie ermöglicht auch die Erstellung von Bitcoin-Derivaten im Lightning-Netzwerk. Ein Beispiel: Mit Fiat-Kanälen können Händler Bitcoin-Zahlungen mit stabilem Wert akzeptieren, ohne sich um die Volatilität von Bitcoin sorgen zu müssen.


Die derzeitige Implementierung von Fiat-Kanälen auf Valet ermöglicht die Erstellung von stabilen synthetischen Fiat-Währungen, die durch Sats gesichert sind. Dabei wird eine Host-Client-Beziehung verwendet, wobei der Host ein beliebiger Lightning-Knoten ist, der diesen Dienst anbietet, und der Kunde der Valet-Nutzer ist. Es handelt sich um eine Verwahrungslösung, da sich alle Sats auf der Seite des Hosts befinden; die Rechnungserstellung, das Tor-Routing und die Erstellung von Vorabbildern erfolgen jedoch wie bei einem normalen Lightning-Kanal auf der Client-Seite.


Die Eröffnung eines Fiat-Kanals erfolgt auf die gleiche Weise wie die Eröffnung eines Lightning-Kanals. Der einzige wesentliche Unterschied besteht darin, dass der Kunde (Valet-Benutzer) in diesem Fall keine Liquidität on-chain zur Schaffung von Kanalkapazität bereitstellen muss. Der Host legt die Kanalkapazität fest und leitet alle Zahlungen für den Kunden weiter.


👉 Um einen Fiat-Kanal zu öffnen, klicken Sie auf die violette **Blitzkarte** auf Ihrer wallet-Startseite. Wählen Sie **Knoten QR scannen** (Zu diesem Zeitpunkt müssen Sie einen Host identifiziert haben, für den Sie einen Kanal öffnen möchten, und den QR des Knotens erhalten haben. Ein Beispiel für einen Host-Knoten, für den Sie einen Fiat-Kanal öffnen können, ist der SATM-Knoten des Standard-Sats)


**Achtung:** Es ist wichtig zu beachten, dass jeder ein Host sein kann. Alles, was Sie benötigen, ist ein Lightning-Knoten mit dem **Fiat-Channel-Plugin** und einem **Hedging-Dienst**. Fiat-Channels ist ein Open-Source-Projekt von *Standard Sats*. Lesen Sie mehr darüber [hier](https://github.com/standardsats/fiat-channels-rfc) und [hier](https://standardsats.github.io/).


SATM-Knoten QR unten:


![SATM_node_QR](assets/en/032.webp)


sobald Sie den QR-Code des Knotens gescannt haben, klicken Sie auf **Dollar-Fiat-Kanal anfordern** oder **Euro-Fiat-Kanal anfordern** (dies ist die Währung, in der Ihre Fiat-Guthaben angegeben werden). Wählen Sie zunächst USD, und klicken Sie auf **OK**. Der Kanal wird automatisch geöffnet, und Sie können sofort mit dem Empfang von Sats beginnen. Sie sehen, so einfach ist es!!!


![choose_fiat_denomination](assets/en/033.webp)


![channel_confirmation_prompt](assets/en/034.webp)


👉 Gehen Sie auf die Startseite Ihres wallet, dort sehen Sie eine **hellgrüne** Karte mit der Bezeichnung **USD**, das ist Ihr **Fiat-Kanal**.


![fiat_channel_card](assets/en/035.webp)


**Achtung:** Wenn Sie Sats über einen Fiat-Kanal empfangen, wird der Fiat-Wert des empfangenen Sats als stabiler Saldo festgeschrieben, während das Sats-Volumen mit dem Bitcoin-Preis schwankt. Diese Lösung wurde vor allem für Händler entwickelt, die Sats als Zahlungsmittel akzeptieren, sich aber nicht den Herausforderungen der Volatilität von Bitcoin stellen wollen. Dies hilft ihnen, jederzeit einen stabilen Wert aufrechtzuerhalten, während sie immer noch in der Lage sind, im Lightning-Netzwerk zu handeln und die globale Reichweite und die schnelle Abwicklung von Bitcoin als Tauschmittel im Lightning Network zu genießen.


Wenn Ihr Fiat-Kanal erstellt wird, sehen Sie die folgenden Wertefelder und deren Bedeutung:


![fiat_channel_info](assets/en/036.webp)



- RANDOM SET OF NUMBERS SEPARATED BY DOTS:** Dies sind die IP-Adressen der Knotenpunkte. (IPV4 und IPV6, jeweils)
- SERVER RATE:** Dies ist der Bitcoin-Marktpreis, zu dem der Hoster Ihnen die Dienste anbietet. Dieser Preis weicht oft geringfügig vom vorherrschenden Marktpreis ab, da ein Hoster einen kleinen Aufschlag erheben kann. Die Festlegung dieses Preises obliegt allein dem Hoster; daher kann er auch von Hoster zu Hoster variieren.
- FIAT BALANCE:** Dies ist der eingefrorene stabile Fiat-Wert jedes Sat, das Sie auf diesem Kanal empfangen. Denken Sie daran, dass, wie bereits erklärt, jedes Mal, wenn Sie Sats auf Ihrem Fiat-Kanal empfangen, der Fiat-Wert des Sats zum Zeitpunkt des Empfangs sofort als synthetischer stabiler Fiat-Wert in diesem Feld gespeichert wird. Ihr **Fiat-Guthaben** schwankt nicht mit dem Marktpreis des Bitcoin. Wann immer Sie Zahlungen über diesen Kanal tätigen wollen, können Sie nur den Sats-Gegenwert dieses Fiat-Guthabens senden. Betrachten Sie dies also als eine digitale Fiat-Währung, die durch Sats gedeckt ist.
- KAPAZITÄT:** Dies ist die Gesamtmenge des Sats, die über diesen Kanal gesendet und empfangen werden kann. (Dies wird ebenfalls vom Host eingestellt. Und im Gegensatz zu einem normalen Lightning-Kanal kann diese Kapazität vom Host je nach Bedarf angepasst werden)
- KANN SENDEN:** Dies ist die Menge an Sats, die Sie an jedem Punkt basierend auf Ihrem Fiat-Guthaben senden können. Dies ist völlig anders als in einem normalen Blitzkanal, weil dieser Wert mit dem Bitcoin-Preis schwankt. Was Sie hier sehen, ist also der Sats-Wert Ihres Fiat-Guthabens zu jedem Zeitpunkt, basierend auf dem **Serverkurs**.
- KANN EMPFANGEN:** Dies ist die Anzahl der Sats, die Sie auf diesem Kanal im Moment empfangen können. Nachdem Sie Ihren Kanal erstellt haben, sollte dieser Wert mit der Kanalkapazität übereinstimmen.
- WERT IM FLUG:** Wenn jemand sats an Ihren Kanal sendet oder wenn Sie versuchen, sats an jemanden zu senden, und die Transaktion aus irgendeinem Grund verzögert wird, wird dies oft in diesem Feld angezeigt.


Hier finden Sie wichtige Informationen über Fiat-Kanäle:



- Im Gegensatz zu einem normalen Lightning-Kanal können Sie, wenn Sie einen Fiat-Kanal öffnen, sofort Sats empfangen, aber nicht senden. Sie können erst dann Sats senden, wenn Sie Sats empfangen haben.
- Der Vermögenswert, der von und nach Sats gesendet wird, ist zu jeder Zeit Sats. Das *Fiat-Guthaben* ist lediglich eine synthetische IOU-Darstellung eines Bitcoin-Wertes, der zu einem beliebigen Zeitpunkt empfangen wird. Es handelt sich also nicht um eine token-Schöpfung oder eine neue Kryptowährung.
- Der Fiat-Kanal ist vor allem für Händler/Unternehmen nützlich, die aufgrund der Volatilität skeptisch gegenüber der Annahme von Bitcoin-Zahlungen sind. Er kann auch für Unternehmen nützlich sein, die die Gehälter ihrer Mitarbeiter in Bitcoin zahlen wollen, ohne die Folgen der Bitcoin-Volatilität zu tragen, die ihr Gehaltskapital instabil machen kann. Es kann auch für Einzelpersonen nützlich sein, die in einem Gebiet mit vorherrschender Bitcoin-Nutzung leben, aber feste Lebenshaltungskosten haben.
- Beachten Sie, dass es kein Feld mit der Bezeichnung **RÜCKERSTATTUNG** gibt. Das liegt daran, dass Sie einen Fiat-Kanal technisch gesehen nicht schließen können. Sie können die Nutzung eines Fiat-Kanals nur beenden, indem Sie sein Guthaben in Ihren normalen Blitz-Kanal ableiten.


### Ihre Fiat Channel Pop-Up Optionen erklärt


Wenn Sie auf Ihren Fiat Lightning Kanal tippen, werden die folgenden Felder angezeigt:


![fiat_channel_pop_up](assets/en/037.webp)


**SHARE HOSTED CHANNEL DETAILS:** Damit können Sie die Details Ihres Fiat-Kanals freigeben, z. B. Remote-Peer-ID, lokale Kanal-ID, Datum der Erstellung usw.


**EXPORT CHANNEL STATE:** Damit können Sie den Zustand eines Kanals zu einem beliebigen Zeitpunkt exportieren. Dies ist in der Regel bei der Behebung von Kanalfehlern nützlich, und ein Host kann Sie bitten, diesen Status mitzuteilen, wenn dies erforderlich ist.


**KANALSALANCE ABZIEHEN:** Wie bereits erwähnt, können Sie einen Fiat-Kanal technisch gesehen nicht schließen, aber Sie können die Balance Ihres Kanals in Ihren bestehenden normalen Lightning-Kanal abziehen. Dies verschiebt automatisch das Sat-Äquivalent deines Fiat-Guthabens in deinen normalen Blitz-Kanal.


**RECEIVE TO CHANNEL:** Dies ist dasselbe wie das Erstellen einer Rechnung, aber in einigen Fällen kann ein Benutzer mehr als einen Fiat-Kanal mit verschiedenen Hosts haben, einschließlich normaler Lightning-Kanäle. Wenn ein Nutzer also mehrere Kanäle geöffnet hat, stellt diese Option sicher, dass er die Zahlung an einen bestimmten Kanal erhalten kann.


**AUFFÜLLEN VON ANDEREN KANÄLEN:** Diese Option ist eine Funktion, die es dem Benutzer ermöglicht, einen Kanal aus anderen bestehenden Kanälen aufzufüllen. Mit dieser Option können Sie also Ihren Fiat-Kanal aus einem normalen Kanal oder aus anderen Fiat-Kanälen, die Sie haben, wieder auffüllen, genauso wie Sie ihn entleeren können.


**DIREKT NICHT PRIVAT EMPFANGEN:** Dies ist auch eine Option, um eine Rechnung zu erstellen, um die Zahlung zu erhalten, aber wenn Sie diese Option verwenden, zahlt der Absender Sie direkt. Das bedeutet, dass die Zahlung nicht durch verschiedene Knotenpunkte hüpft, bevor sie Sie erreicht. Der Absender weiß also im Wesentlichen, dass er Sie bezahlt hat, kennt Ihre Channel-ID usw. Diese Option kann häufig verwendet werden, wenn Sie eine Zahlung von einer vertrauenswürdigen Quelle erhalten und Ihre Privatsphäre nicht schützen müssen.


## Valet-Einstellungen:


Wie jede andere Anwendung hat auch Valet Einstellungen, die Sie nach Ihrem Geschmack anpassen können. Sie können die Einstellungsseite über den Startbildschirm aufrufen.


klicken Sie auf dem Startbildschirm auf das Symbol **Gear** in der oberen rechten Ecke des Bildschirms, um auf die Einstellungen zuzugreifen. Nachfolgend sind die Komponenten im Bereich Einstellungen aufgeführt.


![settings_icon](assets/en/038.webp)


**LOKALE KANALSICHERUNG IST AKTIVIERT:** Wenn dies sonst **Deaktiviert ist,** sollten Sie es aktivieren, da dies die einzige Möglichkeit ist, Ihre normalen Lightning-Kanäle wiederherzustellen, wenn Sie Valet deinstallieren und neu installieren. Wir werden dies später erklären. Klicken Sie also darauf und geben Sie Valet die Erlaubnis, auf Ihren **Medienspeicher** zuzugreifen, denn dort wird die Sicherungsdatei gespeichert.


![app_permissions](assets/en/039.webp)


![enable_media_access](assets/en/040.webp)


** WO LOKALE SICHERUNG ZU SPEICHERN:** Solange Sie Valet die Erlaubnis für Ihren Speicherplatz gegeben haben, wird dieses Feld automatisch so eingestellt, dass lokale Sicherungen in Ihrem Ordner **Downloads** gespeichert werden. Sie können dies jedoch ändern, indem Sie hier klicken und einen beliebigen Ordner Ihrer Wahl auswählen.


**MANAGE CHAIN WALLETS** Dies ist ein wenig technisch, und Sie brauchen sich nicht darum zu kümmern, wenn Sie nicht erfahren genug sind. Die Standardeinstellung ist hier völlig in Ordnung.


**ADD HARDWARE WALLET:** Sie sollten sich auch nicht darum kümmern, es sei denn, Sie haben ein Hardware-wallet, das Sie anschließen und überwachen möchten. Mit dieser Einstellung können Sie Ihr Hardware-wallet, z. B. eine Trezor- oder Cold-Karte, scannen und anschließen und seine Aktivitäten überwachen. Dies ist eine reine Überwachungsfunktion, d. h. Sie können von hier aus keine Transaktionen mit dem Hardware-wallet durchführen. Sie können nur die Aktivitäten, den Kontostand usw. des wallet beobachten und überwachen.


**SET CUSTOM ELECTRUM NODE:** Dies ist ebenfalls eine technische Frage, und wenn Sie sich nicht gut genug auskennen, sollten Sie sich nicht darum kümmern. Die Standardeinstellung ist gut genug.


**BITCOIN UNITS:** So soll Ihr Bitcoin-Saldo angezeigt werden. Die erste Option zeigt Ihren Kontostand in Satoshi Begriffen an, z.B. 1.000.000 Sats, während die zweite Option ihn in BTC Dezimalpunkten anzeigt, z.B. 0,01BTC


**PIN-AUTHENTIKATION VERWENDEN** Wenn Sie dieses Kontrollkästchen aktivieren, müssen Sie eine PIN oder einen Fingerabdruck einrichten, die Sie eingeben müssen, um sich bei Ihrem wallet anzumelden und Transaktionen zu authentifizieren.


**TOR-VERBINDUNG VERWENDEN:** Wenn Sie dieses Kontrollkästchen aktivieren, werden Ihre Transaktionen über das Tor-Netzwerk weitergeleitet. Dies bietet einen zusätzlichen Schutz der Privatsphäre, kann aber zu einem verzögerten Zahlungsdurchsatz führen, insbesondere bei Lightning-Zahlungen.


**BIP39 WIEDERHERSTELLUNGSPHRASE ANSEHEN:** Hier können Sie auf Ihre 12-Wort-seed-Phrase zur Sicherung zugreifen. Wenn Sie ihn also vorher nicht aufgeschrieben haben oder nicht mehr wissen, wo Sie ihn aufgeschrieben haben, können Sie ihn hierher kopieren, solange Sie noch Zugang zu Ihrem Wallet haben.


**NUTZUNGSSTATISTIK:** Dies zeigt Ihnen eine Zusammenfassung aller Ihrer Transaktionen und Aktivitäten seit der Erstellung des wallet


![usage_stats](assets/en/041.webp)


## Wallet Wiederherstellung


Valet ist ein nicht-verwahrender wallet. Wenn Sie also Ihr Gerät verlieren oder Ihre wallet-App deinstallieren, müssen Sie eine wallet-Wiederherstellung durchführen, um Ihre Bitcoins und Lightning-Kanäle zurückzubekommen. Zu Beginn dieses Tutorials haben wir erwähnt, wie wichtig es ist, Ihre **12-Wörter-seed-Phrase** aufzuschreiben, da sie der Schlüssel zur Wiederherstellung Ihres wallet ist. Es gibt keine Kundenbetreuer, die Ihnen dabei helfen können, Ihren wallet wieder zu aktivieren.


Für die Wiederherstellung Ihres Valet wallet sind zwei wichtige Hilfsmittel erforderlich, je nachdem, ob Sie einen aktiven Lightning-Kanal hatten oder nicht. Für einen Benutzer, der keinen aktiven normalen Lightning-Kanal hatte, ist alles, was er braucht, seine **12-Wort-seed-Phrase**, indem er die einfachen Schritte unten befolgt:


👉 Installieren Sie eine neue Valet-App und starten Sie die App.


👉 Wählen Sie **Vorhandene Wallet wiederherstellen**


![restore_existing_wallet](assets/en/042.webp)


👉 Wählen Sie **Nur Wiederherstellungsphrase**.


![select_recovery_phrase](assets/en/043.webp)


👉 Geben Sie Ihre 12-Wort-Wiederherstellungsphrase ein und klicken Sie auf **OK**.


![input_12_words](assets/en/044.webp)


Ihr wallet wird wiederhergestellt. In diesem Fall wird nur Ihr on-chain Bitcoin-Guthaben wiederhergestellt.


Wenn du jedoch einen aktiven normalen Blitz-Kanal hattest und deinen wallet nur mit der Wiederherstellungsphrase wiederherstellst, wird dein Blitz-Kanal zwangsweise geschlossen, und jegliches Bitcoin-Guthaben, das du darauf hast, wird automatisch zu deinem on-chain-Guthaben geschickt.


Die andere Möglichkeit, Ihren Valet wallet wiederherzustellen, insbesondere wenn Sie vor der Deinstallation von Valet einen normalen Lightning-Kanal geöffnet hatten, besteht darin, **die auf Ihrem Gerät gespeicherte lokale Sicherungsdatei zusammen mit Ihrer 12-Wörter-seed-Phrase** zu verwenden. Wenn Sie diese beiden Elemente verwenden, wird der Status Ihres Lightning-Kanals wiederhergestellt, sodass Ihr Lightning-Kanal nicht zwangsweise geschlossen wird.


Hier sind die Schritte:


👉 Installieren Sie eine neue Valet-App und starten Sie die App.


wählen Sie **Vorhandene Wallet wiederherstellen**.


👉 Wählen Sie den Satz **Sicherung + Wiederherstellung**.


![select_backup_and_recovery_seed](assets/en/045.webp)


wählen Sie die Sicherungsdatei im Dateimanager Ihres Telefons aus. (Sie wird standardmäßig immer in Ihrem Ordner **Downloads** gespeichert)


![local_backup_file_in_download_folder](assets/en/046.webp)


Sobald die richtige Sicherungsdatei ausgewählt ist, wird eine Aufforderung angezeigt, die bestätigt, dass eine **"Sicherungsdatei vorhanden ist "**, und Sie werden dann aufgefordert, Ihren seed-Satz mit 12 Wörtern einzugeben.


![enter_12_words](assets/en/047.webp)


👉 Geben Sie Ihren 12-Wörter-Wiederherstellungssatz ein und klicken Sie auf **OK**. Sie werden zu Ihrer wallet-Startseite weitergeleitet.


warten Sie, bis die Bitcoin-Netzwerksynchronisierung (**SYNC**) und die Lightning-Knotensynchronisierung (**LN Sync**) abgeschlossen sind, und Ihr wallet wird vollständig wiederhergestellt, einschließlich Ihrer Lightning-Kanäle.


![LN_sync](assets/en/048.webp)


## Schlussfolgerung


Valet ist eine aufregende wallet-Lösung mit Funktionen, die sie für die Einbindung neuer Benutzer geeignet machen. Sie verfügt auch über einen Fiat-Kanal, eine nicht mehr ganz neue Technologie, die die Integration von Fiat-geführten Unternehmen in den Bitcoin-Standard gewährleistet.


Laden Sie Valet noch heute herunter und probieren Sie es aus!!! 🧡