---
term: OP_IF (0X63)

---
Utfører følgende del av skriptet hvis verdien øverst i stakken ikke er null (true). Hvis verdien er null (false), hoppes disse operasjonene over og går direkte til operasjonene etter `OP_ELSE`, hvis den er til stede. `OP_IF` gjør det mulig å starte en betinget kontrollstruktur i et skript. Den bestemmer kontrollflyten i et skript basert på en betingelse som oppgis på tidspunktet for transaksjonens kjøring. `OP_IF` brukes sammen med `OP_ELSE` og `OP_ENDIF` på følgende måte:

```text
<condition>
OP_IF
<operations if the condition is true>
OP_ELSE
<operations if the condition is false>
OP_ENDIF
```