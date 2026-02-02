---
term: OP_TOALTSTACK (0X6B)

definition: Opcode, joka siirtää pääpinon huipun vaihtoehtoiseen pinoon.
---
Ottaa pääpinon (*main stack*) yläosan ja siirtää sen vaihtoehtopinoon (*alt stack*). Tätä op-koodia käytetään tietojen väliaikaiseen varastointiin myöhempää käyttöä varten skriptissä. Siirretty kohde poistetaan siten pääpinosta. `OP_FROMALTSTACK`:n avulla se asetetaan sitten takaisin pääpinon päälle.
