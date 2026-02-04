---
term: Åtagandetransaktion
definition: Signerad transaktion som representerar det nuvarande tillståndet för fördelningen av medel i en Lightning-kanal.
---

I samband med en dubbelriktad kanal inom Lightning är Commitment Transaction en transaktion som båda parter skapar och signerar, utan att publicera den på huvudkedjan. Den representerar det aktuella tillståndet för fördelningen av medel mellan parterna i en kanal, där varje Lightning-betalning resulterar i en ny Commitment Transaction. Dessa transaktioner är giltiga men sänds endast när kanalen stängs ensidigt. De innehåller utdata för varje part, vilket återspeglar fördelningen av medel enligt de Lightning-betalningar som gjorts sedan kanalen öppnades. Straffmekanismer är kopplade för att avskräcka parter från att sända föråldrade tillstånd för kanalen, det vill säga gamla Commitment-transaktioner som återspeglar en felaktig fördelning av medel.