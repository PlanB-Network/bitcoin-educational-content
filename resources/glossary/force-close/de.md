---
term: FORCE CLOSE
---

Nicht-kooperativer Mechanismus zum Schließen von Lightning-Kanälen. Wenn zwei Nutzer einen Kanal mit einem Multisig 2/2 öffnen, kann jeder von ihnen den Kanal einseitig schließen, indem er den letzten Commitment Transaction sendet, der bereits signiert wurde, um seine Onchain-Bitcoins zurückzugewinnen. Dies wird als "Zwangsschließung" bezeichnet.


Diese Methode wird in der Regel verwendet, wenn einer der Teilnehmer nicht mehr reagiert oder wenn eine kooperative Schließung des Channels unmöglich ist. Wenn eine Zwangsschließung vermieden werden kann, ist dies die beste Methode, da es länger dauert, die Onchain-Gelder wiederzuerlangen, und sie in Bezug auf die Gebühren viel teurer sein kann.


Bei einem Force Close sendet einer der beiden Nutzer den Commitment Transaction, der den letzten bekannten Zustand des Lightning-Kanals wiedergibt. Es gibt dann eine Zeitsperre, bevor die Bitcoins auf der Kette abgerufen werden können, so dass die andere Partei Zeit hat, zu überprüfen, ob die Transaktion dem letzten Kanalstatus entspricht. Wenn ein Nutzer versucht zu betrügen, indem er einen veralteten Commitment Transaction veröffentlicht, kann die andere Partei das Widerrufsgeheimnis verwenden, um den Betrüger zu bestrafen und alle Gelder im Kanal wiederzuerlangen.