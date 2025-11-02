---
name: BLOCKSTREAM Entdecker
description: Erkundung der wichtigsten Layer von Bitcoin und Liquid Network
---

![cover](assets/cover.webp)



Der BLOCKSTREAM Explorer ist ein Projekt, das die Erforschung von Transaktionen und Global State des Bitcoin-Protokolls sowie des von der Firma BLOCKSTREAM entwickelten [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) Liquid erleichtert.



Der 2014 von BLOCKSTREAM, einem von Adam Back gegründeten Unternehmen, ins Leben gerufene [BLOCKSTREAM.info](https://BLOCKSTREAM.info)-Explorer zielt darauf ab, eine robuste Infrastruktur für Bitcoin bereitzustellen, die Interoperabilität und Transaktionsverfolgung zwischen den Schichten (On-Chain und Liquid) gewährleistet und gleichzeitig die Sicherheit und den Datenschutz der Nutzer verbessert.



In diesem Tutorial stellen wir vor, was es auszeichnet, welche Dienste es bietet und wie es eine nahtlose Überwachung des Betriebs und des Status der Bitcoin-Schichten On-Chain und Liquid ermöglicht.



## Erste Schritte mit BLOCKSTREAM



### Navigieren im Hauptkanal



Wenn Sie den BLOCKSTREAM.info-Explorer aufrufen, ist auf dem "**Dashboard**" standardmäßig der Hauptprotokollkanal Bitcoin ausgewählt. Von diesem Interface aus haben Sie einen Überblick über :





- Größe der Hauptkette: Kürzlich abgebaute Blöcke.



![blocks](assets/fr/01.webp)



Dieser Abschnitt enthält Informationen über die zuletzt geschürften Blöcke, die Timestamp, die Anzahl der in jedem BLOCK enthaltenen Transaktionen, die Größe in Kilobytes (kB) und die Messung jedes BLOCK in Gewichtseinheiten (**WU** = *Weight Units*). Die letztgenannte Messung ist von Interesse, da sie es uns ermöglicht, die Optimierung der BLOCK zu bewerten, da jede BLOCK der Hauptkette auf "4.000.000 WU" oder "4.000 kWU" begrenzt ist.





- Jüngste Transaktionen.



![transactions](assets/fr/02.webp)



Der Transaktionsabschnitt enthält Informationen über den eindeutigen Bezeichner der Transaktion, den Bitcoin-Wert, die Größe in virtuellen Bytes (vB) - die die Summe aller Daten (Eingabe und Ausgabe) darstellt - und den entsprechenden Gebührensatz. Eine Transaktion mit einer Größe von 153 vB und einer Rate von 2 Sat/vB würde beispielsweise 306 Satoshis kosten.



### Erforschung von Flüssigkeiten



Über das Menü "**Blöcke**" können Sie die Geschichte der gesamten Hauptkette bis zum letzten abgebauten BLOCK zurückverfolgen.



![blocs](assets/fr/03.webp)



Wenn Sie auf einen bestimmten BLOCK klicken, erhalten Sie weitere Einzelheiten über die darin enthaltenen Informationen und Transaktionen. Zum Beispiel für BLOCK 919330: Sie haben die Hash der BLOCK. Sie können auch zum vorherigen BLOCK navigieren, da jeder abgebaute BLOCK (mit Ausnahme von Genesis) mit dem vorherigen verknüpft ist und den Hash seines Vorgängers beibehält.



![metadata](assets/fr/04.webp)



Wenn Sie auf die Schaltfläche **"Details "** klicken, erhalten Sie weitere Informationen zu diesem BLOCK, wie z. B. seinen Status, der bestätigt, dass er der zurückgehaltenen und propagierten Hauptkette hinzugefügt wurde. Sie erhalten auch die Schwierigkeit, mit der dieses BLOCK abgebaut wird: Diese Schwierigkeit stellt die Rechenleistung dar, die erforderlich ist, um das kryptografische Problem von Mining zu lösen, und wird alle 2016 Blöcke (etwa 2 Wochen) angepasst.



![details](assets/fr/05.webp)



Unter diesem Abschnitt mit den Details finden Sie alle Transaktionen, die in diesem BLOCK enthalten sind.



Die allererste Transaktion im BLOCK wird **Transaktionscoinbase** genannt. Sie wird verwendet, um die Mining-Belohnung des Miner zu verteilen (alle Gebühren im Zusammenhang mit den Transaktionen, die im BLOCK und dem BLOCK Grant enthalten sind). Die durch diese Transaktion erzeugten Bitcoins können erst ausgegeben werden, wenn weitere 100 aufeinanderfolgende Blöcke gemined wurden. Mit anderen Worten, um sie nutzen zu können, muss der Miner auf die Produktion des BLOCK **919430** warten. Dies wird als [*"Fälligkeitsperiode "*] bezeichnet (https://planb.network/fr/resources/glossary/maturity-period).



Die Coinbase ist eine besondere Transaktion: Sie ist die einzige, die keinen wirklichen Input hat, da sie keine Bitcoins aus einer vorherigen Transaktion ausgibt.




![coinbase](assets/fr/06.webp)



Alle anderen Transaktionen sind in zwei Abschnitte unterteilt: Inputs und Outputs.



Damit Bitcoins als Input für eine neue Transaktion verwendet werden können, muss der Initiator der Transaktion seinen Besitz durch eine Signatur nachweisen, die einem bestimmten Skript entspricht. Jedes Stück Bitcoins (UTXO) enthält ein Skript, das im Allgemeinen eine bestimmte Signatur erfordert, die nur der private Schlüssel des Inhabers liefern kann. Diese Skripte heißen ***scriptSig*** (in ASM), sind in Bitcoin Script geschrieben und können von unterschiedlicher Art sein. In diesem Beispiel sehen wir, dass die verwendeten UTXOs vom Typ P2SH zu einer Ausgabe vom Typ P2WPKH (*Pay-to-Witness-Public-Key-Hash*) gehören.



Sie können die Geschichte eines bestimmten UTXO mit Hilfe von Heuristiken zurückverfolgen. Wir laden Sie ein, die verschiedenen Bitcoin-Heuristiken zu entdecken und zu erfahren, wie Sie die Vertraulichkeit Ihrer Bitcoin-Transaktionen stärken können:



https://planb.network/courses/65c138b0-4161-4958-bbe3-c12916bc959c

![trxs](assets/fr/07.webp)



Nehmen wir das Beispiel der ausgehenden Ausgaben dieser Transaktion. Wenn wir auf die Transaktionskennung klicken, werden wir zum Abschnitt **Transaktionen** auf der Seite mit den Transaktionsdetails weitergeleitet.



![transaction](assets/fr/08.webp)



Auf dieser Seite können Sie herausfinden, in welchem BLOCK die Transaktion enthalten war. Je nach Art des verwendeten Address kann die Transaktion ihre Daten (*virtuelle Bytes*) optimieren und somit weniger Transaktionsgebühren zahlen. Bei dieser Transaktion wurden beispielsweise 53 % an Gebühren eingespart, indem ein natives SegWit BECH32 Address-Format verwendet wurde, das mit "bc1q" beginnt.



![trx_details](assets/fr/09.webp)



## Liquid-Beschichtung



Liquid Network ist eine [*Sidechain*](https://planb.network/en/resources/glossary/Sidechain) und eine Open-Source-Lösung der Stufe 2 für das Bitcoin-Protokoll. Es ermöglicht insbesondere schnellere und vertraulichere Bitcoin-Transaktionen.



Klicken Sie im BLOCKSTREAM.info-Explorer auf die Schaltfläche **"Liquid"**, um zum Liquid Network zu wechseln.



![liquid](assets/fr/10.webp)



Wenn wir auf eine der Transaktionen klicken, die wir verfolgen wollen, sehen wir, dass die Beträge der Bitcoin-Stücke durch die Worte "**Vertraulich**" ersetzt werden. In diesem Netzwerk können Transaktionen vertraulich sein, so dass wir die Beträge der einzelnen UTXO nicht sehen können, weder innerhalb noch außerhalb der Transaktion.



![liquid_trx](assets/fr/11.webp)



Wir stellen jedoch fest, dass die Grundsätze und Mechanismen des Layer des Bitcoin-Protokolls dieselben sind: Bitcoin Sperrskripte und UTXO Rückverfolgbarkeit.



![liquid_details](assets/fr/12.webp)



Die Liquid Network bietet auch nicht deponierte digitale Vermögenswerte, die von Organisationen genutzt werden können. Im Menü **"Assets "** finden Sie eine Liste der registrierten Assets, ihre Gesamtsumme und den Bereich, auf den sie sich beziehen.



![assets](assets/fr/13.webp)



Für jeden Vermögenswert können Sie die Historie der Ausgabe- und Verbrennungstransaktionen verfolgen (wobei der Gesamtumlauf gelöscht wird).



![assets_trxs](assets/fr/14.webp)




## Mehr Optionen



Der BLOCKSTREAM.info-Explorer umfasst auch Visualisierungen und die Verfolgung von Transaktionen auf Testnet, Bitcoin, On-Chain und Liquid Network.



![testnet](assets/fr/15.webp)



Wenn Sie zum Testnet-Netzwerk wechseln, verwenden Sie keine echten Bitcoins, aber Sie haben alle oben beschriebenen Funktionen.



![liquid_testnet](assets/fr/16.webp)



Dieses Netz verfügt über eine andere Kettenlänge, an die Sie die Bitcoin- und Liquid-Mechanismen anschließen und deren Funktion testen können.





- Der Bereich API ist für alle gedacht, die bestimmte Explorer-Funktionen in ihre eigene Anwendung integrieren möchten. Über diesen API können Sie die Hauptkette der verschiedenen Ebenen (On-Chain und Liquid) abfragen, Transaktionen verfolgen und beispielsweise die durchschnittlichen Gebühren für Transaktionen in einem BLOCK herausfinden.



![api](assets/fr/17.webp)



Sie sind nun bereit, das volle Potenzial des BLOCKSTREAM Explorers auszuschöpfen, um Blockchains auf den On-Chain und Liquid Schichten abzufragen. Wir hoffen, dass Sie dieses Tutorial informativ fanden, und empfehlen Ihnen unser Tutorial über einen anderen Bitcoin Explorer:



https://planb.network/tutorials/privacy/analysis/mempool-space-f3e468a1-92f1-43ce-b2e4-c3298fa0e02f