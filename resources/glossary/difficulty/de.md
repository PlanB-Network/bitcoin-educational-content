---
term: DIFFICULTY

---
Ein einstellbarer Parameter, der die Komplexität des Arbeitsnachweises bestimmt, der erforderlich ist, um einen neuen Block zur Blockchain hinzuzufügen und die damit verbundene Belohnung zu verdienen. Diese Schwierigkeit wird durch das Schwierigkeitsziel dargestellt, einen 256-Bit-Wert, der die Obergrenze festlegt, die der Hash-Wert des Block-Headers erfüllen muss, um als gültig zu gelten. Das Ziel ist, dass der Hash, der durch eine doppelte Ausführung von SHA256 (SHA256d) erreicht wird, kleiner oder gleich diesem Zielwert ist. Um diesen Hashwert zu erreichen, manipulieren die Schürfer die "nonce" im Blockkopf. Die Schwierigkeit wird alle 2016 Blöcke oder etwa alle zwei Wochen angepasst, um die durchschnittliche Blockerstellungszeit bei etwa 10 Minuten zu halten.