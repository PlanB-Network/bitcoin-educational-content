---
name: WireGuard
description: Kuanzisha WireGuard VPN kwenye Debian na Windows
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Florian BURNEL yaliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## I. Uwasilishaji



Katika somo hili, tutajifunza jinsi ya kusanidi VPN kulingana na WireGuard, suluhu ya VPN isiyolipishwa ambayo huboresha utendaji bila kupuuza usalama.



WireGuard ni suluhisho la hivi majuzi, ambalo limepatikana kama toleo thabiti tangu Machi 2020, na imekuwa na heshima ya kuunganishwa moja kwa moja kwenye **Linux kernel tangu toleo la 5.6**. Hii haizuii kufikiwa kutoka kwa usambazaji wa zamani wa Linux ambao hutumia toleo tofauti la kernel. Ikilinganishwa na suluhu kama vile OpenVPN na IPSec, WireGuard ni rahisi kutumia na haraka zaidi, kama tutakavyoona mwishoni mwa makala haya.



Baadhi ya mambo muhimu kuhusu WireGuard:





- Rahisi, nyepesi na yenye ufanisi zaidi!
- Operesheni ya UDP pekee (ambayo inaweza kuwa shida wakati wa kuvuka ngome fulani)
- Hufanya kazi kwenye kielelezo cha rika-kwa-rika badala ya kielelezo cha seva-teja
- Uthibitishaji kwa ufunguo wa Exchange, kwa kanuni sawa na SSH yenye funguo za kibinafsi/za umma
- Matumizi ya algoriti kadhaa: usimbaji fiche linganifu na ChaCha20, uthibitishaji wa ujumbe na Poly1305, na vile vile zingine kama vile Curve25519, BLAKE2 na SipHash24.
- Inaauni IPv4 na IPv6
- Jukwaa nyingi: Windows, Linux, BSD, macOS, Android, iOS, OpenWRT (na kutekelezwa katika ProtonVPN)
- Laini 4,000 pekee za msimbo, ikilinganishwa na mamia ya maelfu kwa suluhu zingine



Kwa sehemu ya siri, algoriti mbalimbali zinazotumiwa huchaguliwa kwa mkono, kukaguliwa kwa njia kadhaa, na kuchunguzwa na watafiti wa usalama waliobobea katika nyanja hii.



Tovuti rasmi ya mradi: [wireguard.com](https://www.wireguard.com/)



Je, umesadikishwa na suluhisho hili baada ya kusoma utangulizi huu? Kilichobaki ni kusoma tu!



## II. Mchoro wa WireGuard wa Lab



Kabla sijawasilisha maabara yangu kwa ajili ya kusanidi WireGuard, unapaswa kujua kwamba unaweza kufikiria **kutumia WireGuard kuunganisha miundomsingi miwili ya mbali**, lakini pia **kuunganisha mteja wa mbali na miundombinu kama vile mtandao wa shirika au mtandao wako wa nyumbani**. Hii ni katika ari sawa na OpenVPN, kama tulivyoona hivi majuzi kwenye mafunzo "[OpenVPN on Synology](https://www.it-connect.fr/tuto-vpn-configurer-openvpn-server-sur-un-nas-synology/)".



Ikiwa WireGuard haijawekwa moja kwa moja kwenye kipanga njia au ngome, kama inavyowezekana kwa OpenWRT, utahitaji kusanidi usambazaji wa mlango ili mtiririko ufikie jozi ya WireGuard.



![Image](assets/fr/034.webp)



Sasa nitakuambia kuhusu maabara yangu na kile tunachoenda kuanzisha leo.



Nitatumia mashine ya Debian 11 kama seva ya WireGuard na mteja wa Windows kama mteja wa WireGuard VPN. Ingawa inapotosha kidogo kuzungumza kuhusu uhusiano wa seva ya mteja, kwa sababu **WireGuard hufanya kazi kwenye muundo wa "peer-to-peer"**. Hilo ni jina potofu kidogo unapojaribu kusanidi muunganisho wa "mteja-kwa-tovuti". Wacha tuseme badala yake kwamba nitakuwa na jozi mbili au ** sehemu mbili za unganisho za WireGuard ** ukipenda: moja chini ya Debian 11 na nyingine chini ya Windows.



Jozi hizi mbili zinaweza kuwasiliana kwa pande zote mbili, ikimaanisha kuwa kutoka kwa mashine yangu ya Windows naweza kufikia LAN ya mbali ya mashine ya Debian 11, na kinyume chake: yote inategemea usanidi wa handaki na firewall ya rika la WireGuard.



Katika mfano huu, nitazingatia kesi ifuatayo: **kutoka kwa Windows Peer 1 yangu iliyounganishwa kwenye mtandao wangu wa nyumbani, ninataka kufikia mtandao wangu wa shirika ili kufikia seva za kampuni kupitia njia ya VPN ya WireGuard**. Hii inatoa mchoro ufuatao:



![Image](assets/fr/035.webp)



Kwa upande wa anwani za IP, hii inatoa:





- Mtandao wa nyumbani**: 192.168.1.0/24
- Mtandao wa ushirika**: 192.168.100.0/24
- Mtandao wa handaki ya WireGuard**: 192.168.110.0/24


+ IP Address ya Peer 1 (Windows) kwenye handaki: 192.168.110.2/24


+ IP Address ya Peer 2 (Debian) kwenye handaki: 192.168.110.121/24



Hayo tu ndiyo yapo! Hebu tushuke kwenye usanidi!



**Kumbuka: kwa chaguomsingi, WireGuard hufanya kazi katika hali ya UDP kwenye **bandari 51820**.



## III Usakinishaji na usanidi wa seva ya WireGuard



Nitatumia maneno "mteja" kwa mashine ya Windows na "seva" kwa mashine ya Debian kwenye mafunzo haya, kwa sababu ingawa ni ya rika-rika, inaonekana kuwa na maana zaidi.



### A. Kusakinisha WireGuard kwenye Debian 11



Kifurushi cha usakinishaji cha WireGuard kinapatikana katika hazina rasmi ya Debian 11, kwa hivyo tunachotakiwa kufanya ni kusasisha kashe ya kifurushi na kukisakinisha:



```
sudo apt-get update
```



```
sudo apt-get install wireguard
```



![Image](assets/fr/022.webp)



Sehemu ya seva ya WireGuard itasakinishwa, pamoja na zana mbalimbali zinazotoa ufikiaji wa amri muhimu za kudhibiti usanidi.



### B. Kuweka Interface WireGuard



Kwa kutumia **amri "wg "** tunahitaji generate ufunguo wa faragha na ufunguo wa umma: muhimu kwa uthibitishaji kati ya jozi mbili, yaani seva na mteja (ambaye pia atahitaji jozi muhimu).



Tutaunda ufunguo wa faragha "**/etc/wireguard/wg-private.key**" na ufunguo wa umma "**/etc/wireguard/wg-public.key**" kwa mlolongo huu wa amri:



```
wg genkey | sudo tee /etc/wireguard/wg-private.key | wg pubkey | sudo tee /etc/wireguard/wg-public.key
```



![Image](assets/fr/023.webp)



Thamani ya ufunguo wa umma itarejeshwa kwenye kiweko. Katika faili ya usanidi ya WireGuard, tunahitaji **kuongeza thamani ya ufunguo wetu wa faragha**. Ili kupata thamani hii, ingiza amri hapa chini na unakili thamani:



```
sudo cat /etc/wireguard/wg-private.key
```



Ni wakati wa kuunda faili ya usanidi katika "**/etc/wireguard/**". Kwa mfano, tunaweza kutaja faili hii "**wg0.conf**", ikiwa tunafikiri kwamba mtandao wa Interface unaohusishwa na WireGuard utakuwa "wg0", kwa kanuni sawa na "eth0", kwa mfano.



```
sudo nano /etc/wireguard/wg0.conf
```



Katika faili hii, lazima kwanza tuongeze maudhui yafuatayo (tutarudi ili kuyakamilisha baadaye):



```
[Interface]
Address = 192.168.110.121/24
SaveConfig = true
ListenPort = 51820
PrivateKey = <clé privée du serveur>
```



Sehemu `[Interface]` inatumika kutangaza sehemu ya seva. Hapa kuna habari fulani:





- Address**: IP Address ya Interface WireGuard ndani ya handaki ya VPN (subnet tofauti na LAN ya mbali)
- SaveConfig**: usanidi unahifadhiwa (na kulindwa) kwa muda mrefu kama Interface inafanya kazi.
- ListenPort**: Lango la kusikiliza la WireGuard. Katika kesi hii, 51820 ndio bandari chaguo-msingi, lakini unakaribishwa kuibinafsisha
- Ufunguo wa Kibinafsi**: thamani ya ufunguo wa faragha wa seva yetu (*wg-private.key*)



Hifadhi faili na uifunge. Kwa amri ya "**wg-quick**", tunaweza kuanza Interface hii kwa kubainisha jina lake (wg0, kama faili inaitwa wg0.conf):



```
sudo wg-quick up wg0
```



Ukiorodhesha anwani za IP za seva yako ya Debian 11, utaona Interface mpya inayoitwa "wg0" na IP Address imefafanuliwa kwenye faili ya usanidi:



```
ip a
```



![Image](assets/fr/027.webp)



Kwa roho hiyo hiyo, tunaweza kuonyesha usanidi wa Interface "wg0" kupitia amri ya "wg show":



```
sudo wg show wg0
```



![Image](assets/fr/024.webp)



Hatimaye, tunahitaji kuwezesha kuanzisha kiotomatiki kwa Interface wg0 WireGuard yetu:



```
sudo systemctl enable wg-quick@wg0.service
```



Kwa sasa, tutaacha kando usanidi wa upande wa seva ya WireGuard.



### C. Wezesha Usambazaji wa IP



Ili mashine yetu ya Debian 11 iweze **kuelekeza pakiti kati ya mitandao tofauti (kama kipanga njia)**, yaani, kati ya mtandao wa VPN na mtandao wa ndani, tunahitaji kuwezesha [IP Forwarding](https://www.it-connect.fr/activer-lip-forwarding-sous-linux-ipv4ipv6/). Kwa chaguo-msingi, kipengele hiki kimezimwa.



Rekebisha faili hii ya usanidi:



```
sudo nano /etc/sysctl.conf
```



Ongeza maagizo yafuatayo hadi mwisho wa faili na uhifadhi:



```
net.ipv4.ip_forward = 1
```



Hayo ndiyo yote yaliyopo kwake.



### D. Washa Kinyago cha IP



Ili seva yetu iongoze pakiti kwa njia ipasavyo na ili LAN ya mbali iweze kufikiwa na mashine ya Windows, tunahitaji kuwezesha Kinyago cha IP kwenye seva yetu ya Debian. Hii ni aina ya kuwezesha NAT. Nitafanya usanidi huu kwenye ngome ya Linux kupitia UFW, ambayo nimezoea kutumia ([ufw mafunzo kwenye Debian](https://www.it-connect.fr/configurer-un-pare-feu-local-sous-debian-11-avec-ufw/)).



Ikiwa tayari huna UFW na unataka kuiweka (unaweza pia kutumia Nftables), anza kwa kusakinisha:



```
sudo apt install ufw
```



Kwanza kabisa, unahitaji kuwezesha SSH ili usipoteze udhibiti wa seva ya mbali (badilisha nambari ya bandari):



```
sudo ufw allow 22/tcp
```



Bandari ya 51820 katika UDP lazima pia iidhinishwe, tunapoitumia kwa WireGuard (tena, rekebisha nambari ya mlango):



```
sudo ufw allow 51820/udp
```



Ifuatayo, tutaendelea na usanidi ili kuwezesha kinyago cha IP. Ili kufanya hivyo, tunahitaji kurejesha jina la Interface iliyounganishwa kwenye mtandao wa ndani. Ikiwa hujui jina, endesha "ip a" ili kuona jina la kadi. Katika kesi yangu, ni kadi ya "**ens192**".



![Image](assets/fr/036.webp)



Tutatumia habari hii. Hariri faili ifuatayo:



```
sudo nano /etc/ufw/before.rules
```



Ongeza mistari hii mwishoni mwa faili ili **kuwezesha kinyago cha IP kwenye Interface en192** (badilisha jina la Interface) ndani ya safu ya POSTROUTING ya jedwali la NAT la ngome yetu ya karibu:



```
# NAT - IP masquerade
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -o ens192 -j MASQUERADE

# End each table with the 'COMMIT' line or these rules won't be processed
COMMIT
```



Picha inaonyesha:



![Image](assets/fr/037.webp)



Weka faili hii ya usanidi wazi na uendelee kwa hatua inayofuata. 😉



### Usanidi wa ngome ya E. Linux kwa WireGuard



Bado katika faili sawa ya usanidi, tutatangaza mtandao wa ushirika "192.168.100.0/24" ili tuweze kuwasiliana nayo. Hapa kuna sheria mbili za kuongezwa (ikiwezekana baada ya sehemu ya "*# ok icmp ya FORWARD*" kuweka kanuni pamoja):



```
# autoriser le forwarding pour le réseau distant de confiance (+ le réseau du VPN)
-A ufw-before-forward -s 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.100.0/24 -j ACCEPT
-A ufw-before-forward -s 192.168.110.0/24 -j ACCEPT
-A ufw-before-forward -d 192.168.110.0/24 -j ACCEPT
```



Ikiwa unataka kuidhinisha mwenyeji mmoja tu, kwa mfano "192.168.100.11", ni rahisi:



```
-A ufw-before-forward -s 192.168.100.11/32 -j ACCEPT
-A ufw-before-forward -d 192.168.100.11/32 -j ACCEPT
```



Sasa unaweza kuhifadhi faili na kuifunga. Kilichobaki ni kuwezesha UFW na kuanzisha upya huduma ili kutumia mabadiliko yetu:



```
sudo ufw enable
```



```
sudo systemctl restart ufw
```



Sehemu ya kwanza ya usanidi wa seva ya Debian sasa imekamilika.



## IV. Mteja wa WireGuard kwa Windows



Kiteja cha WireGuard kinapatikana kwa Windows, macOS, Android, n.k... Hizi ni habari njema. Vipakuliwa vyote vinapatikana kwenye ukurasa huu: [WireGuard Client](https://www.wireguard.com/install/). Katika mfano huu, nitaweka mteja kwenye Windows. Ili kusanidi mteja wa WireGuard kwenye Linux, fuata kanuni sawa na ya kuunda faili ya wg0.conf kwenye mashine ya Debian (bila NAT yote, nk).



### A. Kusakinisha kiteja cha Windows cha WireGuard



Mara tu unapopakua kifurushi kinachoweza kutekelezwa au cha MSI, usakinishaji ni moja kwa moja: zindua tu kisakinishi, na...voilà, imekamilika! 🙂



![Image](assets/fr/038.webp)



### B. Unda wasifu wa WireGuard



Anza kwa kufungua programu ili kuunda handaki mpya. Ili kufanya hivyo, bofya kwenye mshale ulio upande wa kulia wa kitufe cha "**Ongeza handaki **" na ubofye kitufe cha "**Ongeza handaki tupu **".



![Image](assets/fr/028.webp)



Dirisha la usanidi litafungua. Kila wakati usanidi mpya wa handaki unapoundwa, WireGuard hutengeneza jozi ya vitufe vya faragha/vya umma mahususi kwa usanidi huu. **Katika usanidi huu, tunahitaji kutangaza "rika", yaani seva ya mbali:



```
[Interface]
PrivateKey = <la clé privée du PC>
```



Tunahitaji kukamilisha usanidi huu, hasa kutangaza IP Address kwenye Interface hii (*Address*), lakini pia kutangaza seva ya mbali ya WireGuard kupitia kizuizi cha [Peer]. Picha iliyo hapa chini inapaswa kukukumbusha juu ya faili ya usanidi tuliyounda kwenye upande wa seva ya Linux.



Hebu tuanze na kizuizi cha `[Interface]`, na kuongeza IP Address "**192.168.110.2**"; kumbuka kuwa seva ina IP Address "**192.168.110.121**" kwenye sehemu hii ya mtandao. Hii inatoa:



```
[Interface]
PrivateKey = <la clé privée du PC>
Address = 192.168.110.2/24
```



Ifuatayo, tunahitaji kutangaza kizuizi cha "Rika" na mali tatu, na kusababisha usanidi huu:



```
[Peer]
PublicKey = 1D/Gf5yd3hUDoFyYQ3P1zayBHUJhJZq+k6Sv03HnJCQ=
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
Endpoint = <ip-serveur-debian>:51820
```



Katika picha:



![Image](assets/fr/029.webp)



**Maelezo machache kuhusu kizuizi cha [Peer]:





- PublicKey**: huu ndio ufunguo wa umma wa seva ya WireGuard Debian 11 (unaweza kupata thamani yake na amri ya "*sudo wg*")
- Inaruhusiwa**: hizi ni anwani za IP / subneti zinazofikiwa kupitia mtandao huu wa WireGuard VPN, katika hali hii subnet maalum ya WireGuard VPN yangu (*192.168.110.0/24*) na LAN yangu ya mbali (*192.168.100.0/24*)
- Mwisho**: hii ni IP Address ya seva pangishi ya Debian 11, kwa kuwa hii ndio sehemu yetu ya unganisho ya WireGuard (utahitaji kubainisha IP ya umma Address)



Hatimaye, weka jina katika sehemu ya "**Jina**" (bila nafasi) na unakili na ubandike ufunguo wa umma wa mteja, kwani tutahitaji kuutangaza kwenye seva. Bonyeza "**Jisajili**".



### C. Tangaza mteja kwenye seva ya WireGuard



Ni wakati wa kurudi kwenye seva ya Debian ili kutangaza "**Rika**", yaani, Kompyuta yetu ya Windows, katika usanidi wa WireGuard. Kwanza kabisa, tunahitaji **kuzuia Interface "wg0"** ili kurekebisha usanidi wake:



```
sudo wg-quick down wg0
# ou
sudo wg-quick down /etc/wireguard/wg0.conf
```



Ifuatayo, rekebisha faili ya usanidi iliyoundwa hapo awali:



```
sudo nano /etc/wireguard/wg0.conf
```



Katika faili hii, kufuatia kizuizi cha `[Interface]`, tunahitaji kutangaza kizuizi cha `[Mwenzake]`:



```
[Peer]
PublicKey = 0i2Pg8nwDW2j7yOG09ZXht18o8l8Erb9Y5F4xyAyQV8=
AllowedIPs = 192.168.110.2/32
```



Kizuizi hiki cha [Rika] kina ufunguo wa umma wa Kompyuta ya Windows 10 (**PublicKey**) na IP Address ya Interface ya Kompyuta (**AllowedIPs**): seva itawasiliana katika kichuguu hiki cha WireGuard ili tu kuwasiliana na mteja wa Windows, kwa hivyo thamani "**168.168.32.2/2".



Kilichobaki ni kuhifadhi faili (*CTRL+O kisha Ingiza kisha CTRL+X kupitia Nano*). Zindua upya Interface "wg0":



```
sudo wg-quick up wg0
# ou
sudo wg-quick up /etc/wireguard/wg0.conf
```



Ili kuhakikisha kuwa tamko la rika linafanya kazi, unaweza kutumia amri hii:



```
sudo wg show
```



Mara tu seva pangishi ya mbali inapoweka muunganisho wake wa WireGuard, IP Address yake itasogezwa hadi thamani ya "mwisho".



![Image](assets/fr/033.webp)



Hatimaye, tutalinda faili za usanidi ili kupunguza ufikiaji wa mizizi:



```
sudo chmod 600 /etc/wireguard/ -R
```



### D. Muunganisho wa Kwanza wa WireGuard



Sasa kwa kuwa usanidi uko tayari, tunaweza kuianzisha kutoka kwa Windows PC. Ili kufanya hivyo, katika mteja wa "**WireGuard**", bofya kitufe cha "**Amilisha**": uunganisho utabadilika ** kutoka "Zima" hadi "On"**, lakini hiyo haimaanishi kuwa itafanya kazi. Yote inategemea ikiwa usanidi wako ni sahihi au la. **Muunganisho unapoanzishwa, mashine zetu mbili huwasiliana kupitia Interface WireGuard iliyosanidiwa kila upande!



![Image](assets/fr/030.webp)



Katika tukio la tatizo, hii itaonekana kwenye kichupo cha "**Logbook**". Wapangishi wawili watapakia Exchange mara kwa mara ili kuangalia hali ya muunganisho, kwa hivyo ujumbe wa "*Kupokea kifurushi cha keepalive kutoka kwa programu rika 1*".



![Image](assets/fr/031.webp)



Ikiwa kichupo cha "**Journal**" cha WireGuard kinaonyesha ujumbe kama ulio hapa chini, unahitaji kuangalia kama vitufe vya umma vilivyotangazwa pande zote mbili ni sahihi.



```
Handshake for peer 1 (<ip>:51820) did not complete after 5 seconds, retrying (try 2)
```



Kutoka kwa Kompyuta yangu ya mbali, ninaweza kubandika IP Address ya Interface WireGuard yangu kwenye upande wa seva, na vile vile mwenyeji kwenye LAN yangu ya mbali.



![Image](assets/fr/032.webp)



### E. Utendaji: OpenVPN dhidi ya WireGuard



Kutoka kwa Kompyuta yangu ya mbali iliyounganishwa kwenye WireGuard VPN yangu, niliweza kufikia seva ya faili na kuhamisha faili kupitia [SMB](https://www.it-connect.fr/le-protocole-smb-pour-les-debutants/), ili kuona kiwango cha uhamisho. **Nikiwa na WireGuard, ninashinda hadi 45 Mb/s, ambayo ni nzuri, kwa kuwa niko kwenye WiFi.



![Image](assets/fr/025.webp)



Chini ya hali sawa, lakini kupitia muunganisho wa OpenVPN (katika UDP) wakati huu, na operesheni sawa, upitishaji ni tofauti kabisa: karibu 3 MB/s. Tofauti ni dhahiri!



![Image](assets/fr/026.webp)



Hii ni ya kuvutia, kwa sababu ikiwa, kwa mfano, ukibadilisha kutoka kwa uunganisho wa WiFi hadi uunganisho wa 4G/5G, uunganisho huo utakuwa wa haraka sana kwamba usumbufu hautaonekana.



### F. Bonasi: handaki kamili WireGuard



Kwa usanidi wa sasa, sehemu ya trafiki hutiririka kupitia VPN, na iliyobaki kupitia muunganisho wa Mtandao wa mteja, ikijumuisha kuvinjari Mtandao. Ikiwa tunataka kubadili hadi kwa WireGuard **hali kamili ya handaki**, ili kila kitu kipitie njia ya VPN, tunahitaji kufanya mabadiliko machache kwenye usanidi wetu....



Kwanza, unahitaji kusanikisha kifurushi cha "resolvconf" kwenye:



```
sudo apt-get update
sudo apt-get install resolvconf
```



Mara hii imefanywa, unahitaji kurekebisha wasifu wa "wg0.conf" kwenye mashine ya Debian: simamisha Interface, urekebishe, na uanze upya.



```
sudo wg-quick down /etc/wireguard/wg0.conf
```



Kisha, **katika kizuizi cha `[Interface]`, tunaongeza seva ya DNS itakayotumika**. Kwa upande wangu, ni kidhibiti cha kikoa cha maabara yangu, lakini tunaweza pia kusakinisha Bind9 kwenye mashine ya Debian ili kuwa na kisuluhishi cha ndani.



```
DNS = 192.168.100.11
```



Hifadhi faili, kisha uanze tena Interface:



```
sudo wg-quick up /etc/wireguard/wg0.conf
```



Hatimaye, katika usanidi wa handaki kwenye kituo cha kazi cha Windows 10, unahitaji kurekebisha sehemu ya "AllowedIPs" ili kuonyesha kwamba kila kitu lazima kipite kwenye handaki. Badilisha:



```
AllowedIPs = 192.168.110.0/24, 192.168.100.0/24
```



Na:



```
AllowedIPs = 0.0.0.0/0
```



Unaweza kuona kwamba hii pia huwezesha chaguo la "**Ua swichi".



![Image](assets/fr/040.webp)



Hatimaye, nilichukua fursa ya handaki hili kamili kufanya mtihani mdogo wa mtiririko, ambao matokeo yake yameonyeshwa hapa chini:



![Image](assets/fr/039.webp)



Usanidi wa WireGuard ni rahisi sana na rahisi kuelewa, na juu ya yote kudumisha. **WireGuard inachukuliwa kuwa mustakabali wa VPN**, kwa hivyo ni bora tuifuatilie kwa karibu! Tunaweza pia kuona kwamba manufaa ni muhimu katika suala la utendakazi, ambayo ni faida kubwa kwa WireGuard ikilinganishwa na OpenVPN.



Nyaraka za ziada:





- [Man - Command wg](https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8)
- [Mwanadamu - Amri wg-quick](https://manpages.debian.org/unstable/wireguard-tools/wg-quick.8.en.html)



**WireGuard VPN yako iko na inafanya kazi! Hongera!