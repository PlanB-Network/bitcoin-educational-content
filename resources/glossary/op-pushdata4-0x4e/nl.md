---
term: OP_PUSHDATA4 (0X4E)
definition: Opcode die zeer grote hoeveelheden gegevens op de stack pusht (zelden gebruikt).
---

Hiermee kan een zeer grote hoeveelheid gegevens naar de stack worden gepusht. Het wordt gevolgd door vier bytes (little-endian) die de lengte van de te pushen gegevens aangeven (tot ongeveer 4,3 GB). Deze opcode wordt gebruikt om zeer grote gegevens in scripts in te voegen, hoewel het gebruik ervan uiterst zeldzaam is vanwege praktische beperkingen op de transactiegrootte.