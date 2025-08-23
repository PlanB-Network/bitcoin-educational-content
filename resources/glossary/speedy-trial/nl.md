---
term: SNELLE PROEF
---

Methode om een Soft Fork te activeren, oorspronkelijk bedacht voor Taproot in het begin van 2021 door David A. Harding, gebaseerd op een idee van Russell O'Connor. Het principe is om de BIP8 methode te gebruiken met een `LOT` parameter ingesteld op `false`, terwijl de activatieperiode wordt teruggebracht tot slechts 3 maanden. Deze verkorte stemperiode maakt een snelle verificatie van de Miner goedkeuring mogelijk. Als de vereiste goedkeuringsdrempel wordt bereikt tijdens een van de periodes, wordt de Soft Fork vergrendeld. Het zal enkele maanden later geactiveerd worden, zodat mijnwerkers de nodige tijd hebben om hun software te updaten.


Het succes van deze methode voor Taproot, die brede consensus genoot binnen de Bitcoin gemeenschap, garandeert echter niet dat deze methode voor alle updates effectief is. Hoewel de Speedy Trial methode snellere activering mogelijk maakt, maken sommige ontwikkelaars zich zorgen over het toekomstig gebruik ervan. Ze vrezen dat het zou kunnen leiden tot een te snelle opeenvolging van Soft forks, wat mogelijk de stabiliteit en veiligheid van het Bitcoin protocol zou kunnen bedreigen. Vergeleken met BIP8 met de `LOT=true` parameter, is de Speedy Trial methode veel minder bedreigend voor mijnwerkers. Er is niet automatisch een UASF gepland. Deze activeringsmethode is nog niet geformaliseerd in een BIP.


> ► *De term "Speedy Trial" is ontleend aan juridische terminologie die een "versneld proces" aanduidt Dit verwijst naar het feit dat het verbeteringsvoorstel snel wordt voorgelegd aan de mijnwerkersrechtbank om hun bedoelingen te bepalen. Het is algemeen aanvaard om de Engelse term rechtstreeks in het Frans te gebruiken.*