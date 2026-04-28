---
term: Anchors.dat

definition: Soubor Bitcoin Core, který ukládá IP adresy uzlů, ke kterým byl klient připojen před zastavením, aby se usnadnilo opětovné připojení při restartování.
---
Soubor používaný v klientovi Bitcoin Core k ukládání IP adres odchozích uzlů, ke kterým byl klient připojen před vypnutím. Soubor Anchors.dat se tedy vytváří při každém zastavení uzlu a odstraňuje se při jeho opětovném spuštění. Uzly, jejichž IP adresy jsou v tomto souboru obsaženy, slouží k rychlému navázání spojení při opětovném spuštění uzlu.