namn: LN VPN

beskrivning: Konfigurera din VPN
---

![image](assets/cover.jpeg)

# LN⚡VPN

LN VPN är en VPN-tjänst på begäran som endast accepterar betalningar med lightning. Idag visar jag dig hur du använder den och lämnar färre spår när du surfar på internet.

Det finns många kvalitativa VPN-tjänsteleverantörer, vi har faktiskt gjort en omfattande översyn i den här artikeln (länk) men LN VPN sticker ut och vi kunde inte låta bli att låta dig upptäcka den.

De flesta VPN-tjänsteleverantörer som ProtonVPN och Mullvad erbjuder möjligheten att betala med bitcoins men kräver att du skapar ett konto och köper ett abonnemang under en längre eller kortare tid, vilket inte nödvändigtvis passar alla budgetar.

LN VPN gör det möjligt att använda VPN på begäran under så kort tid som en timme tack vare sin implementation av betalningar med bitcoins via lightning-nätverket. Snabba och anonyma betalningar öppnar upp en värld av möjligheter när det gäller mikrobetalningar.

> 💡 Denna guide beskriver hur du använder LN VPN från ett Linux Ubuntu 22.04 LTS-system.

## Förutsättningar: Wireguard

Förenklat uttryckt används Wireguard för att skapa en säker tunnel mellan din dator och fjärrservern som du kommer att surfa på internet via. Det är IP-adressen för denna server som kommer att visas som din egen under den tid du kommer att använda den enligt denna guide.

Officiell installationsguide för Wireguard: https://www.wireguard.com/install/

```bash
$ sudo apt-get update
$ sudo apt install wireguard
```

## Förutsättningar: Bitcoin Lightning-plånbok

Om du ännu inte har en Bitcoin Lightning-plånbok, oroa dig inte, vi har skapat en mycket enkel guide för dig här. (avsnittet LN-tutorial kan hjälpa dig)

## Steg 1: Skaffa en konfiguration

På https://lnvpn.com måste du välja landet för IP-adressen för VPN-tunnelns utgång samt en tidsperiod. När dessa parametrar är inställda, klicka på "Betala med lightning".

![image](assets/1.jpeg)

En lightning-faktura visas, du behöver bara skanna den med din lightning-plånbok.

När fakturan är betald måste du vänta några sekunder till cirka två minuter för att dina Wireguard-konfigurationsparametrar ska genereras. Om det tar lite längre tid, oroa dig inte, vi har gjort denna procedur tiotals gånger, ibland kan det ta lite längre tid.

Nästa skärm visas och du behöver bara klicka på "Ladda ner som fil" för att få din konfigurationsfil, den kommer att ha ett namn som liknar lnvpn-xx-xx.conf där "xx" motsvarar dagens datum.

![image](assets/2.jpeg)

## Steg 2: Aktivera tunneln
Först måste du byta namn på konfigurationsfilen som du fick i föregående steg så att den automatiskt kan identifieras av Wireguard.
Gå till din nedladdningsmapp antingen i en terminal eller med filutforskaren och byt namn på filen lnvpn-xx-xx.conf till wg0.conf.

```bash
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```

Det är klart! Tunneln är aktiverad!

## Steg 3: Kontrollera

Använd en online-tjänst som whatismyip för att kontrollera att din publika IP-adress nu är den som tillhör VPN:en du just aktiverade.

## Steg 4: Avaktivera

När ditt avtal har löpt ut måste du avaktivera anslutningen för att återfå åtkomst till internet. Du kan sedan utan problem upprepa steg 1 till 3 varje gång du vill skapa ett avtal med LN VPN.

Avaktivera tunneln:

```bash
$ sudo ip link delete dev wg0
```

Det är klart! Nu kan du använda LN VPN, en unik VPN-tjänst!