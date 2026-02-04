---
term: Gap limit
definition: Maximaal aantal opeenvolgende ongebruikte adressen voordat het zoeken naar transacties wordt gestaakt.
---

Een parameter die gebruikt wordt in Bitcoin Wallet software om het maximum aantal opeenvolgende ongebruikte adressen naar generate te bepalen, voordat het zoeken naar extra transacties wordt gestopt. Het aanpassen van deze parameter is vaak nodig bij het herstellen van een Wallet om er zeker van te zijn dat alle transacties worden gevonden. Een te lage Gap Limiet kan resulteren in het missen van enkele transacties als adressen werden overgeslagen tijdens de afleidingsfasen. Door de Gap Limit te verhogen, kan de Wallet verder in de Address reeks zoeken, om alle bijbehorende transacties te herstellen.


Een enkele `xpub` kan theoretisch meer dan 4 miljard ontvangende adressen afleiden (zowel interne als externe adressen). Wallet software kan ze echter niet allemaal afleiden en controleren op gebruik zonder enorme operationele kosten. Daarom worden ze in indexvolgorde uitgevoerd, omdat dit normaal gesproken de volgorde is waarin alle Wallet software adressen genereert. De software registreert elke gebruikte Address voordat het naar de volgende gaat en stopt met zoeken wanneer het een aantal opeenvolgende lege adressen tegenkomt. Dit aantal wordt de Gap Limit genoemd.


Als bijvoorbeeld de Gap Limit is ingesteld op `20`, en de Address `m/84'/0'/0'/0/15/` is leeg, dan zal de Wallet adressen afleiden tot `m/84'/0'/0/34/`. Als dit adresbereik ongebruikt blijft, stopt het zoeken daar. Bijgevolg zou een transactie die gebruik maakt van Address `m/84'/0'/0'/0/40/` in dit voorbeeld niet worden gedetecteerd.