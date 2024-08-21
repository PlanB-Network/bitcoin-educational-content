---
term: VÕRGU KORRIGEERITUD AEG (NAT)
---

Universaalse aja hinnang, mis on määratud võrgusõlmede kellade põhjal. Iga sõlm arvutab oma NAT-i, võttes oma kohaliku kella (UTC) ja sellega ühendatud sõlmede kellade ajavahe mediaani, seejärel lisades sellele oma kohaliku kella aja. Mediaani lisatakse kuni maksimaalselt 70 minutit. Seega on võrgu korrigeeritud aeg kohalikult iga sõlme poolt arvutatud sõlmeaegade mediaan. See viitepunkt on seejärel kasutusel ploki ajatemplite kehtivuse kontrollimiseks. Tõepoolest, et sõlm ploki aktsepteeriks, peab selle ajatempel jääma viimase 11 kaevandatud ploki mediaanajale (MTP) ja NAT-ile lisatud 2 tunni vahele:

```text
MTP < Kehtiv Ajatempel < (NAT + 2h)
```