---
term: Index (nyckel)
definition: Sekventiellt nummer som tilldelas en undernyckel (child key) för att skilja den från dess syskon i en HD-plånbok.
---

I samband med en HD-portfölj avses det löpnummer som tilldelas en underordnad nyckel som genereras från en överordnad nyckel. Detta index används i kombination med föräldranyckeln och föräldrasträngkoden för att på ett deterministiskt sätt härleda unika barnnycklar. Det möjliggör en strukturerad organisation och reproducerbar generering av flera par av systerbarnnycklar från en enda föräldranyckel. Det är ett 32-bitars heltal som används i härledningsfunktionen `HMAC-SHA512`. Detta nummer kan användas för att särskilja underordnade nycklar inom en HD-portfölj.