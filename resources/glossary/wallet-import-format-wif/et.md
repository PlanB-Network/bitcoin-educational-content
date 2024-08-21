---
term: WALLET IMPORT FORMAT (WIF)
---

Meetod Bitcoin'i privaatvõtme kodeerimiseks viisil, mis võimaldab seda hõlpsamini importida või eksportida erinevate rahakottide vahel. WIF põhineb `Base58Check` kodeeringul, mis sisaldab teavet versiooni, vastava avaliku võtme kompressiooni ja trükivigade tuvastamiseks mõeldud kontrollsumma kohta. WIF privaatvõti algab tähemärkidega `5` tihendamata võtmete puhul või `K` ja `L` tihendatud võtmete jaoks ning sisaldab kõiki tähemärke, mis on vajalikud algse privaatvõtme taastamiseks. WIF formaat pakub standardiseeritud vahendit privaatvõtme ülekandmiseks erinevate rahakottide tarkvara vahel.