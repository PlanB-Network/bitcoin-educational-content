---
term: BIP141

---
Introduserte konseptet Segregated Witness (SegWit), som ga navn til SegWit soft fork. BIP141 introduserer en større modifikasjon av Bitcoin-protokollen som tar sikte på å løse problemet med transaksjonsforfalskning. SegWit skiller vitnet (signaturdata) fra resten av transaksjonsdataene. Dette skillet oppnås ved å sette inn vitnene i en egen datastruktur, som er forpliktet i et nytt Merkle-tre, som i seg selv refereres til i blokken via coinbase-transaksjonen, noe som gjør SegWit kompatibel med eldre versjoner av protokollen.