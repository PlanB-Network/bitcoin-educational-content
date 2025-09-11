---
name: LN VPN

description: Konfigurera LN VPN med Lightning för en anonym och skräddarsydd VPN
---

![image](assets/cover.webp)


LN VPN är en anpassningsbar VPN-tjänst som bara accepterar blixtbetalningar. Idag ska jag visa dig hur du använder den och lämnar färre spår när du surfar på interwebben.


Det finns många VPN-tjänsteleverantörer av hög kvalitet, och vi har genomfört en omfattande granskning i den här artikeln (hyperlänk). LN VPN sticker dock ut, och vi kunde inte missa chansen att presentera det för dig.


De flesta VPN-tjänsteleverantörer som ProtonVPN och Mullvad erbjuder möjligheten att betala med bitcoins men kräver att man skapar ett konto och köper en plan för en längre eller kortare period, vilket kanske inte passar allas budget.


LN VPN möjliggör VPN-användning på begäran under så kort tid som en timme, tack vare implementeringen av Bitcoin-betalningar via Lightning Network. Omedelbara och anonyma blixtbetalningar öppnar upp en värld av möjligheter för mikrobetalningar.


Obs💡: **Den här guiden beskriver hur du använder LN VPN från ett Linux Ubuntu 22.04 LTS-system


## Förutsättningar: Wireguard


Enkelt uttryckt används Wireguard för att skapa en säker tunnel mellan din dator och fjärrservern genom vilken du surfar på Internet. Det är IP Address för den här servern som kommer att visas som din under hela det hyresavtal som du Contract genom att följa den här guiden.


Officiell installationsguide för Wireguard: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## Förutsättningar: Blixt Bitcoin Wallet


Om du inte har en Lightning Bitcoin Wallet ännu, inga bekymmer, vi har skapat en mycket enkel guide för dig här. (avsnittet LN handledning kan hjälpa dig)


## Steg 1: Contract ett hyresavtal


Från https://lnvpn.com måste du välja land för VPN-tunnelns utgångs-IP och en varaktighet. När dessa parametrar är inställda klickar du på Betala med blixt.


![image](assets/1.webp)


En blixt Invoice kommer att visas och du behöver bara skanna den med din blixt Wallet.


När Invoice har betalats måste du vänta i några sekunder till upp till två minuter för att dina Wireguard-konfigurationsinställningar ska genereras. Om det tar lite längre tid, få inte panik, vi har gjort den här proceduren dussintals gånger, och ibland tar det bara lite längre tid.

Följande text har översatts till engelska med bibehållande av samma markdown-layout som originaltexten:


Nästa skärm visas och du behöver bara klicka på "Download as File" för att få din konfigurationsfil, som kommer att ha ett namn som ser ut som lnvpn-xx-xx.conf där "xx" motsvarar aktuellt datum.

![image](assets/2.webp)


## Steg 2: Aktivera tunneln


Först måste du byta namn på den konfigurationsfil som erhölls i föregående steg så att den automatiskt kan kännas igen av Wireguard.


Gå till din nedladdningsmapp, antingen i ett terminalfönster eller med filutforskaren, och byt namn på filen lnvpn-xx-xx.conf till wg0.conf så här:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


Så där ja! Tunneln är aktiverad!


## Steg 3: Verifiera


Använd en onlinetjänst som whatismyip för att verifiera att din offentliga IP Address nu är den från VPN som du just aktiverade.


## Steg 4: Inaktivera


När ditt leasingavtal löper ut måste du inaktivera anslutningen för att återfå åtkomst till internet. Du kan sedan upprepa steg 1 till 3 när du vill upprätta ett leasingavtal med LN VPN.


Inaktivera tunneln:


```
$ sudo ip link delete dev wg0
```


Där har du det! Du vet nu hur du använder LN VPN, en unik VPN-tjänst!