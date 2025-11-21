---
term: BCH CODE
---

Eine Klasse von Fehlerkorrekturcodes, die zur Erkennung und Korrektur von Fehlern in einer Datenfolge verwendet werden. Mit anderen Worten: BCH-Fehlerkorrekturcodes werden verwendet, um zufällige Fehler in übertragenen Informationen zu finden und zu korrigieren, um sicherzustellen, dass sie unversehrt am Ziel ankommen. Das Akronym "BCH" steht für die Anfangsbuchstaben der Namen der Erfinder dieser Codes: Bose, Ray-Chaudhuri und Hocquenghem.


Dieses Werkzeug wird in vielen Bereichen der Datenverarbeitung eingesetzt, darunter SSDs, DVDs und QR-Codes. Dank dieser fehlerkorrigierenden Codes ist es beispielsweise selbst dann möglich, die kodierten Informationen abzurufen, wenn ein QR-Code teilweise verdeckt ist.


Als Teil von Bitcoin werden BCH-Codes für die Prüfsumme in den Address-Formaten Bech32 und Bech32m (post-SegWit) verwendet. Sie stellen einen besseren Kompromiss zwischen Prüfsummengröße und Fehlererkennungsfähigkeit dar als die einfachen Hash-Funktionen, die zuvor für Legacy-Adressen verwendet wurden. Im Kontext von Bitcoin werden BCH-Codes nur zur Fehlererkennung, nicht zur Fehlerkorrektur verwendet. Daher wird die Bitcoin-Portfolio-Software Fehler in einem empfangenden Address erkennen und dem Benutzer melden, aber den falschen Address nicht automatisch ändern. Der Grund für diese Entscheidung ist die Tatsache, dass die Integration der Fehlerkorrektur zwangsläufig die Fehlererkennungsfähigkeiten des Algorithmus beeinträchtigt.