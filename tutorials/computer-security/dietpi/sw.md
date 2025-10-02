---
name: DietPi
description: Mfumo wa uendeshaji mwepesi ulioboreshwa kwa mashine zenye utendaji wa chini. Kwa upendeleo wa mwenyeji wa kibinafsi
---

![cover](assets/cover.webp)



Katika miduara isiyo ya kiufundi, chapa kama vile `Odroid`, `Raspberry Pi`, `Orange Pi` au `Radxa`, hazijulikani sana. Lakini mtu anapaswa kuangalia tu katika miduara ya kiteknolojia, ili kupata kwamba **SBC** kompyuta--iliyojengwa kwenye ubao mama mmoja, mara nyingi ni ndogo kwa ukubwa ikilinganishwa na kompyuta zinazotumika kawaida--zinakuwa muhimu sana, kama msaada kwa mradi wowote wa kibinafsi.



Hizi ni kompyuta zinazozalishwa katika aina mbalimbali za mifano. Wanapendelea ugawaji wa Linux, mara nyingi hubadilishwa ili kufanya kazi vizuri kwenye mashine hizi zisizo na nguvu.



**DietPi sio ubaguzi**: ni mfumo wa uendeshaji unaotegemea Debian, ulioboreshwa kuwa mwepesi iwezekanavyo na kufanya `SBC` inayofanya kazi kwa uchache zaidi kwa haraka sana. Imebadilishwa kutoka kwa Debian12 Bookworm hadi Debian13 Trixie jinsi mafunzo haya yalivyokuwa yakiandikwa, sasa yanatumia chanzo huria cha SBC za kichakataji cha `RISC-V`. DietPi ni ugunduzi wa kupendeza ambao unastahili kusoma zaidi.



## Nguvu



Hii sio "rudufu ya kawaida" ya Debian kwa bodi ndogo za aina ya Raspberry. DietPi ni:




- Imeboreshwa kwa kasi na wepesi**: [ulinganisho na usambazaji mwingine wa Debian kwa SBC](https://dietpi.com/blog/?p=888), DietPi ni nyepesi katika kila kitu. Picha ya DietPi ISO ina uzani wa chini ya GB 1, kwa ndogo zaidi kati ya zile zinazotolewa kwa mifano ya zamani ya Raspberry au Orange PI (kwa mfano). Mahitaji ya rasilimali za RAM na CPU ni ya chini sana, ili daima hupata bora kutoka kwa bodi, hata za zamani.
- Mitambo otomatiki na visakinishi vilivyojengewa ndani**: Mkusanyiko wa amri maalum husaidia watumiaji kufuatilia rasilimali za mfumo na vile vile kufanyia kazi kiotomatiki kusakinisha na kuzindua programu, kusasisha matoleo, kuweka nakala rudufu na kuangalia kumbukumbu zote.
- Jumuiya imara, yenye mwelekeo wa majaribio**: [mafunzo](https://dietpi.com/forum/c/community-tutorials/8) na miradi kutoka kwa jumuiya ya DietPi, ni bora kwa kupata msukumo wa programu unayoweza kusakinisha kwa mbofyo mmoja, shukrani kwa DietPi.



**Kubana kila sehemu kutoka kwa SBC yako haijawahi kuwa rahisi**.



## Otomatiki kwa upangishaji wa kibinafsi


Je, ungependa kufanya majaribio na seva yako mwenyewe ili kuendesha masuluhisho ya hali ya juu ya mtandao, au zana za kuboresha utaalamu wako wa Bitcoin? DietPi inaweza kuwa suluhisho ambalo umekuwa ukitafuta. Ingawa watu wengi wanajua jinsi ya kudhibiti miundombinu yao wenyewe na kuendesha seva zilizosanidiwa na kulindwa kikamilifu, DietPi ni hatua inayofaa kwa wale wanaotaka kuanza kutoka mwanzo.



Badala ya kufanya mwenyewe kazi zote ngumu ambazo kazi kama hiyo inahitaji, DietPi hukuruhusu kuziunda kwa `mchawi` na safu yake ya amri. Hapa unaweza kujaribu na wingu yako binafsi, udhibiti wa kifaa _smart home_, hifadhi rudufu za kiotomatiki na crontab, pamoja na suluhu za kina zaidi.



![img](assets/en/01.webp)



## Ufungaji



### Pakua



DietPi inatoa seti isitoshe ya picha za ISO, ili kuchoma mfumo wa uendeshaji kwa vifaa vingi tofauti. Baadhi hutumiwa tu: ISO ya Raspberry PI5 bado iko katika majaribio, kwa mfano, lakini unaweza kupata moja inayofaa kwa bodi yako.



Kwa mwongozo huu nilichagua kuisanikisha kwenye mteja mwembamba, kwa hivyo chaguo lilikwenda kwa _PC/VM_ na kisha kwa _Native PC_. Kuna picha mbili za ISO za vifaa hivi, ambazo hutofautiana katika kizazi cha bootloader. Mashine iliyotumika kwenye mafunzo ni ya zamani kabisa, kwa hivyo chaguo lilikwenda kwa toleo la _BIOS/CSM_. Ikiwa una mashine mpya zaidi, toleo sahihi linaweza kuwa `UEFI`.



![img](assets/en/02.webp)



Utatua kwenye ukurasa ambao una `picha ya kisakinishi`, `sha256` na `Saini`.



![img](assets/en/03.webp)



Andaa saraka katika `nyumbani` ya kompyuta yako ya kila siku, ili uweze kupakua faili zinazohitajika, na `wget`.



![img](assets/en/04.webp)



Ufunguo wa umma wa msanidi ulihitaji utafiti wa chini zaidi, lakini unaweza kuupata kwenye kiungo hiki: https://github.com/MichaIng.gpg.



![img](assets/en/05.webp)



Angalia yaliyomo kwenye saraka na `ls -la` na ulete kitufe cha MichaIng kwenye ufunguo wako, na `gpg --import`.



### Uthibitishaji na flash



Hatimaye, sehemu ninayopendekeza zaidi: hakikisha uhalisi wa mfumo wa uendeshaji ambao umepakua na unakaribia kusakinisha kwenye SBC yako.



![img](assets/en/06.webp)



Ikiwa pia umepata matokeo ya `Sahihi nzuri` na kidhibiti sawa cha Hash kwa amri ya sha256sum, unaweza kuendelea kuwaka ISO kwenye kijiti cha USB. Tumia programu kama vile Whale Etcher kufanya hivi.



![img](assets/en/07.webp)



## Ufungaji wa DietPi



![img](assets/en/09.webp)



Hamisha kiendeshi cha flash kwenye kifaa ambacho kitakuwa mwenyeji wa DietPi na uanze usakinishaji wa mfumo wa uendeshaji wa chokaa Green. Katika zoezi hili tunatumia mteja mwembamba aliye na GB 16 ya RAM, SSD ya GB 128 kwa mfumo wa uendeshaji, na diski ya data ya TB 1 ya pili. Ufungaji ulichukua chini ya dakika 30, lakini ikiwa utatumia Raspberry, kwa mfano, rasilimali inaweza kuwa ndogo na kuchukua muda mrefu. Utaonyeshwa maendeleo wakati wa usakinishaji.



![img](assets/en/08.webp)



Kwa kuwa imeundwa kwa ajili ya Raspberries na kadhalika, hali halisi ya DietPi ni ile inayoitwa usakinishaji `usio na kichwa`, bila mazingira ya picha na ufikiaji wa `shsh' asili. Katika mwongozo badala yake utaona mazingira ya picha, LXDE kuwa sahihi.



Katika hatua hii, utaulizwa pia kuamua ni kivinjari kipi ungependa kutumia kwa chaguomsingi, kati ya Chromium na Firefox. Wote wawili hufanya kazi vizuri; hakuna contraindications fulani kwa aidha, zaidi ya upendeleo wako binafsi.



Kuelekea mwisho, kisakinishi kinaweza kukuuliza ikiwa unataka kusakinisha programu zozote tayari, lakini hapa **nakushauri usipakie kitu chochote**. Unapaswa kujua kwamba baada ya hatua hii, utaulizwa kubadilisha nenosiri la msingi la watumiaji wawili, kwa sababu za usalama. Muhimu zaidi utahitajika **kuweka Nenosiri la Programu ya Ulimwenguni (GSP)`**, ambayo itahakikisha ufikiaji wa programu mbalimbali kwa njia iliyodhibitiwa. **Ukipakua programu yoyote wakati wa usakinishaji wa Mfumo wa Uendeshaji, bila seti ya `GSP`, zitasalia kuwa hazipatikani kabisa**. Utalazimika kuziondoa na kuzisakinisha tena baada ya kuweka `Nenosiri la Programu ya Ulimwenguni`: kwa hivyo, **usiweke chochote ndani ili kuepuka kufanya kazi maradufu**. (Usumbufu unawezekana, sio uhakika wa 100%).



Usakinishaji unaisha kwa ombi la kuwezesha DietPi-Survey, huduma ya kiotomatiki ya kukusanya data inayotumika kusaidia uundaji wa mfumo wa uendeshaji. Kulingana na tovuti, ukusanyaji wa data huwashwa unapopakua programu yoyote kutoka kwa otomatiki iliyotolewa na DietPi, au unapopata toleo jipya zaidi. Kila mtu ana chaguo la kuchagua kuingia (_Chagua KUINGIA_) au kuchagua kutoka (_Chagua OUT_).



![img](assets/en/23.webp)



Baada ya kukamilika kwa usakinishaji na kuwasha upya baadae, DietPi inaonekana kwenye skrini unapoisanidi. Kwa mafunzo, kama ilivyotajwa, nilichagua mazingira ya picha ya `LXDE`. Kwenye eneo-kazi nilipata njia ya mkato ya kuanza `htop` na terminal wazi.



![img](assets/en/10.webp)



### "Zana" kutoka kwa mfumo wa uendeshaji



Sahau programu nyingi unazotumia kwenye usambazaji wako wa Linux-DietPi imeboreshwa sana, umeacha chache. Kimsingi itabidi usakinishe amri nyingi kwa mikono, lakini ikiwa unajaribu tu, pinga majaribu na ujaribu kuweka otomatiki za DietPi chini ya majaribio.



Hakika ni terminal ambayo ni zana ya kwanza muhimu kwa ajili ya kuanza na mfumo wako mpya wa uendeshaji, na inafungua kiotomatiki kila wakati unapoiwasha.



![img](assets/en/11.webp)



Kwenye skrini ya terminal, utapata mfululizo wa amri ulioorodheshwa uliotanguliwa na `dietpi-` zinazowakilisha [zana](https://dietpi.com/docs/dietpi_tools/) za mfumo huu wa uendeshaji:




- `Dietpi-launcher`: kufikia mfumo wa uendeshaji, kidhibiti faili, n.k
- `Dietpi-Software`: ambayo inawakilisha zana ambayo unaweza kusakinisha programu zote tayari zinapatikana katika Suite
- `dietpi-config`: kufikia usanidi wa mfumo, hata ule wa hali ya juu zaidi.



![img](assets/en/14.webp)



### Hifadhi nakala



Kuhifadhi nakala rudufu ya seva ni utaratibu ambao msimamizi wa mfumo anapaswa kutarajia kutoka kwa uanzishaji wa kwanza.



Ukiwa na DietPi kuna amri ya `dietpi-Backup`, ambayo ninapendekeza utafute ili kupata suluhisho bora: hukuruhusu kusanidi nakala rudufu ya kawaida, ya kuongeza au la kutegemea programu zilizotumiwa, na chaguzi zote za kubinafsisha utaratibu.



![img](assets/en/22.webp)



Teua marudio ya chelezo, kwa mfano diski nyingine, kwa kuanza `dietpi-Drive_Manager` kupachika kiendeshi lengwa na kuitumia kwa utendakazi huu.



## Usanidi



Kujikaribisha ni jambo linalofaa kwa kila mtu, awe anadadisi au mwenye shauku tu. Walakini, kuvuta na kusanidi seva kunajumuisha changamoto kadhaa za kiteknolojia ambazo hazizingatiwi. Hapa ndipo **usahili wa DietPi** huingia, kukuruhusu kusanidi mfumo unaolingana na mahitaji yako kwa hatua chache rahisi.



![img](assets/en/24.webp)



Mipangilio ya msingi na ya juu, yote kiganjani mwako katika Interface moja inayopatikana kwa amri:



```dietpi-config


sudo dietpi-config


```

Che cosa si può fare ora? Automatizzare i processi da avviare all'accensione del server, configurare il `Locale` e tutte le impostazioni correlate alla Time Zone, impostare le schede di rete, le password e le periferiche audio/video, ad esempio.

## I Pacchetti Software

Tra le caratteristiche di semplicità di DietPi, vi è anche la dettagliata pagina dei Software che - oltre all'elenco delle applicazioni - mostra i primi passi da compiere per installarli e interagire con loro. Prendiamo ad esempio il caso di **Docker**:

![img](assets/en/15.webp)

Cliccando sulla sua "icona" compare in alto una finestra, dove è possibile cliccare i link che portano a una spiegazione di massima. La finestra mostra dove si trovano i file più importanti, come accedere all'interfaccia web e tanti altri suggerimenti per un'installazione fluida.

![img](assets/en/16.webp)

Le applicazioni che prevedono l'interazione dell'utente hanno un'interfaccia web pensata per questo scopo, accessibile all'indirizzo IP che va sempre sotto la sintassi `indirizzo-IP-localhost:porta`. Anche l'URL dell'interfaccia web la trovi se hai cliccato _View_.

Tutti [i software disponibili con DietPi](https://dietpi.com/dietpi-software.html), si installano da terminale, digitando:

```


sudo dietpi-programu


```