---
term: OP_CAT (0X7E)
definition: Inaktiverad opcode som tillåter sammanslagning av de två översta elementen på stacken.
---

Gör det möjligt att sammanfoga de två översta Elements på stacken (d.v.s. sammanfoga dem ända till ända). Denna opcode har inaktiverats, vilket gör att den för närvarande är omöjlig att använda. Den har dock nyligen kommit tillbaka i rampljuset. Vissa vill lägga till den i Tapscript för att möjliggöra kombinationen av objekt på stacken och därmed förbättra språkets uttrycksfullhet. Detta enkla tilläggsverktyg skulle kunna möjliggöra följande:


- Användning av Lamport-signaturer, som förmodligen är motståndskraftiga mot kvantattacker;
- Implementering av valv;
- Användningen av avtal;
- Eller till och med användningen av avtal som inte är av typen "non-equivocation".