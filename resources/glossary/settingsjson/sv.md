---
term: Settings.json
definition: Bitcoin Core-fil som lagrar inställningar för det grafiska användargränssnittet.
---

Fil som används i Bitcoin Core för att lagra inställningarna för den grafiska användaren Interface (GUI). Den innehåller information om användarkonfigurationer, som t.ex. öppna plånböcker. När Bitcoin Core startas om möjliggör den här filen automatisk återöppning av plånböcker som var aktiva innan programmet stängdes. Om en Wallet stängs via GUI tas den också bort från den här filen, och därför öppnas den inte automatiskt igen vid nästa start.