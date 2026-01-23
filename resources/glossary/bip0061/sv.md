---
term: BIP0061
definition: Avvisningsmeddelande mellan noder som signalerar varför en transaktion eller ett block är ogiltigt. Borttaget i Bitcoin Core 0.20.0.
---

Införde ett avslagsmeddelande i kommunikationsprotokollet mellan noder. Målet med BIP61 är att lägga till en återkopplingsmekanism när en nod tar emot en transaktion eller ett block från en annan nod som den anser vara ogiltigt. Detta meddelande om avslag skulle göra det möjligt för en nod att signalera till avsändaren varför det avvisades. Denna typ av kommunikation var avsedd att förbättra interoperabiliteten mellan olika klienter och kommunikationen mellan fulla noder och SPV-klienter. De funktioner som BIP61 medförde övergavs så småningom från och med version 0.20.0 av Bitcoin Core, eftersom de ansågs onödiga samtidigt som de medförde ökade bandbreddsbehov.