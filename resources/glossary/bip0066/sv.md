---
term: BIP0066
definition: Standardisering av signaturformatet med strikt DER-kodning för att undvika avvikelser mellan system.
---

Införde en standardisering av signaturformatet i transaktioner. Denna BIP föreslogs som svar på en avvikelse i hur OpenSSL hanterade signaturkodning i olika system. Denna heterogenitet utgjorde en risk för att Blockchain skulle splittras. BIP66 standardiserade signaturformatet för alla transaktioner med hjälp av strikt DER-kodning (*Distinguished Encoding Rules*). Denna förändring krävde en Soft Fork. För sin aktivering använde BIP66 sedan samma mekanism som BIP34, vilket krävde att fältet "nVersion" ökades till version 3 och att alla block med version 2 eller lägre avvisades när tröskeln på 95 % Miner uppnåddes. Detta tröskelvärde passerades vid block nummer 363 725 den 4 juli 2015.