---
term: SPEEDY TRIAL

---
Metode for å aktivere en myk gaffel som opprinnelig ble konseptualisert for Taproot tidlig i 2021 av David A. Harding basert på en idé av Russell O'Connor. Prinsippet er å bruke BIP8-metoden med en `LOT`-parameter satt til `falsk`, samtidig som aktiveringsperioden reduseres til bare 3 måneder. Denne forkortede avstemningsperioden muliggjør en rask verifisering av gruvearbeidernes godkjenning. Hvis den nødvendige godkjenningsterskelen nås i løpet av en av periodene, låses den myke gaffelen. Den vil bli aktivert flere måneder senere, slik at utvinnerne får nødvendig tid til å oppdatere programvaren sin.

Suksessen med denne metoden for Taproot, som det var bred enighet om i Bitcoin-samfunnet, garanterer imidlertid ikke at den er effektiv for alle oppdateringer. Selv om Speedy Trial-metoden muliggjør raskere aktivering, uttrykker noen utviklere bekymring for fremtidig bruk. De frykter at det kan føre til en for rask rekke av soft forks, noe som potensielt kan true stabiliteten og sikkerheten til Bitcoin-protokollen. Sammenlignet med BIP8 med parameteren `LOT=true`, er Speedy Trial-metoden mye mindre truende for utvinnere. Ingen UASF er planlagt automatisk. Denne aktiveringsmetoden har ennå ikke blitt formalisert i en BIP.

> ► *Begrepet "Speedy Trial" er lånt fra juridisk terminologi som indikerer en "fremskyndet rettssak" Dette henspiller på det faktum at forbedringsforslaget raskt bringes inn for gruvearbeidernes domstol for å fastslå deres intensjoner. Det er vanlig å bruke det engelske begrepet direkte på fransk*