---
name: Qubes
description: Mfumo wa uendeshaji salama kabisa.
---

![cover](assets/cover.webp)



Qubes OS ni mfumo wa uendeshaji usiolipishwa, wa chanzo huria ulioundwa kwa ajili ya watumiaji wanaoweka usalama juu ya vipaumbele vyao. Umaalumu wake unategemea wazo rahisi lakini kali: badala ya kuzingatia kompyuta kwa ujumla, inagawanya matumizi yake katika sehemu za kujitegemea zinazoitwa **_qubes_**.



Kila qube hufanya kazi kama **mazingira pepe yaliyotengwa**, yenye kiwango na utendaji mahususi wa uaminifu. Kwa hivyo hata kama maombi yataathiriwa, shambulio hilo linasalia tu kwenye eneo lake bila kuathiri mfumo mzima.



> Ikiwa una nia ya dhati kuhusu usalama, Qubes OS ndio mfumo bora wa uendeshaji unaopatikana leo. - **Edward Snowden**.

Hata hivyo, kufunga Qubes OS inahitaji maandalizi zaidi kuliko kufunga mfumo wa uendeshaji wa kawaida. Inahusisha kuangalia mahitaji fulani ya vifaa, kuelewa misingi ya virtualization na kukubali uzoefu tofauti, ambapo kila kazi ya kila siku inafikiriwa kwa suala la kujitenga. Lakini ikishapatikana, Qubes OS inatoa mfumo thabiti ambao unafafanua upya jinsi unavyoingiliana na kompyuta yako kila siku. Katika somo hili, tutaeleza jinsi Qubes OS inavyofanya kazi na jinsi ya kuisakinisha kwa urahisi kwenye mfumo wako.



## Je, Qubes OS inafanya kazi vipi?



Qubes OS inategemea kanuni ya compartmentalization. Badala ya kutumia mfumo mmoja, inategemea **Xen** hypervisor kuunda mashine pepe zilizotengwa, zinazoitwa qubes. Kila qube imejitolea kwa kazi maalum au kiwango cha uaminifu (kazi, kuvinjari kwa kibinafsi, benki, nk). Utengano huu unahakikisha kwamba maelewano yoyote katika qube moja hayawezi kuenea kwa mengine, yakifanya kazi kama kompyuta kadhaa zinazojitegemea ndani ya mashine moja.



Mtumiaji Interface inadhibitiwa na kikoa kikuu, salama kinachoitwa **dom0**. Kikoa hiki kimetengwa kabisa na Mtandao, na kuifanya kuwa moyo wa mfumo. Ingawa madirisha na menyu huonyeshwa na dom0, utekelezaji halisi wa programu hufanyika katika qubes husika.



## Aina tofauti za qubes



Karibu dom0 huzunguka aina tofauti za qube, kila moja ikiwa na jukumu mahususi la kutekeleza.





- **AppVM** hutumika kuendesha programu za kila siku: kwa hivyo mtumiaji anaweza kutenganisha barua pepe zake za kitaaluma na shughuli zake za kuvinjari mtandaoni au za benki, huku kila mazingira yakisalia kuwa huru kabisa na mengine.





- AppVM hizi zenyewe zinatokana na **TemplateVM**, ambazo hutumika kama violezo vya kati vya kusakinisha na kusasisha programu, hivyo basi kuondoa hitaji la kudhibiti kila qube kivyake.



Qubes OS pia huunganisha mashine pepe zilizobobea katika **huduma za mfumo**.





- **NetVM** inasimamia moja kwa moja **vifaa vya mtandao** na kuhakikisha muunganisho kwenye Mtandao. Mara nyingi huhusishwa na **FirewallVM**, ambayo huingilia **kuchuja trafiki** na kupunguza udhihirisho wa qubes zingine.





- ServiceVM zina jukumu sawa, kwa mfano katika usimamizi wa kifaa cha USB, kila wakati kwa mantiki sawa: tenga vipengele hatari zaidi ili kupunguza uso wa mashambulizi.



Hatimaye, kwa kazi za mara kwa mara au hatari, Qubes OS hutoa **DisposableVM**. Hizi ephemeral qubes huundwa kwa kuruka ili **kufungua hati inayotiliwa shaka** au **kutembelea tovuti yenye shaka**, kisha kutoweka kabisa inapofungwa, kufuta athari zote na kuzuia mashambulizi yoyote yanayoendelea.



### Utaratibu wa kunakili salama (qrexec)



Ubadilishanaji kati ya qubes unatokana na **qrexec**, mfumo wa mawasiliano kati ya VM ulioundwa kwa ajili ya usalama. Badala ya kuruhusu qubes kuwasiliana kwa uhuru, qrexec inaweka **sera mahususi**: faili iliyonakiliwa kutoka AppVM moja hadi nyingine, au maandishi yanayohamishwa kupitia ubao wa kunakili, hupitia kila mara kituo kinachofuatiliwa na kuthibitishwa na mfumo. Kwa njia hii, hata kitendo rahisi cha kunakili na kubandika kinadhibitiwa ili kuzuia kuenea kwa programu hasidi.



### Usimamizi wa diski



Qubes OS hutumia mfumo wa busara kwa usimamizi wa uhifadhi. TemplateVM zina msingi wa programu za kawaida, huku AppVM zinaongeza tu data zao za kibinafsi na faili mahususi. Hii inapunguza matumizi ya nafasi ya diski na kuwezesha masasisho ya kimataifa. DisposableVMs, kwa upande mwingine, hutumia viwango vya muda ambavyo hupotea kabisa wakati imefungwa. Mfano huu sio tu dhamana ya usalama zaidi, lakini pia usimamizi bora wa rasilimali.



## Kwa nini uchague Qubes OS?



Faida za Qubes OS ziko juu ya yote katika muundo wake wa kipekee wa usalama. Kiini cha mbinu hii ni ujumuishaji, ambao hulinda mtumiaji kwa kutenga kila kazi katika mashine tofauti za mtandaoni. Katika hali halisi, barua pepe iliyoambukizwa au tovuti hasidi inaweza tu kuhatarisha qube moja, na kuacha mfumo mzima na data yako ya kibinafsi ikilindwa kikamilifu. Usanifu huu unazuia kwa kiasi kikubwa mashambulizi magumu ambayo, kwa mfumo wa kawaida, yanaweza kueneza kwa uhuru.



Qubes OS pia hutoa uwazi na udhibiti kamili wa mazingira yako ya kidijitali. Unajua ni programu gani ina ufikiaji wa rasilimali gani, iwe ni mtandao, kifaa cha USB au vipengee vingine nyeti. Mfumo huu unajumuisha vipengele vya juu vya usalama kwa chaguomsingi, kama vile usimbaji fiche kamili wa diski, na kuwezesha matumizi ya huduma za kutokutambulisha kama vile mfumo wa uendeshaji wa Whonix.



https://planb.network/tutorials/computer-security/operating-system/whonix-06f9172c-2962-412e-9487-b665d8ca9f59

Badala ya kutafuta kuunda mfumo usiopenyeka, Qubes OS huzingatia uthabiti: hujumuisha uharibifu katika tukio la maelewano, na kupunguza hatari kwa mfumo wote. Mbinu hii ya kisayansi hufanya Qubes OS kuwa chaguo linalopendelewa kwa watumiaji walio na mahitaji ya juu ya usalama, au wanaotaka kudumisha udhibiti wa juu zaidi wa maisha yao ya kidijitali.



## Inasakinisha Qubes OS



Kabla ya kusakinisha Qubes OS, ni muhimu kuhakikisha kuwa maunzi yako yanakidhi mahitaji ya chini zaidi, kwani mfumo unategemea uboreshaji wa kuona ili kutenga qubes. Viungo kuu vya kuangalia ni:




- **Kichakataji**: Kichakataji cha biti 64 kinachooana na uboreshaji wa maunzi (Intel VT-x au AMD-V).
- RAM: kiwango cha chini cha GB 8 kinahitajika, lakini tunapendekeza RAM ya GB 16 au zaidi ili kuendesha qubes kadhaa kwa wakati mmoja.
- **Nafasi ya kuhifadhi**: kiwango cha chini cha GB 36, ikiwezekana GB 128 kwenye SSD kwa utendakazi bora.



Ili kusakinisha Qubes OS, pakua picha rasmi ya ISO kutoka kwa Qubes OS [tovuti rasmi](https://www.qubes-os.org/downloads/). Ni muhimu kuangalia uadilifu wa ISO kwa kutumia sahihi za GPG zilizotolewa, ili kuhakikisha kuwa faili haijaingiliwa na kwamba upakuaji ni salama.



https://planb.network/tutorials/computer-security/data/integrity-authenticity-21d0420a-be02-4663-94a3-8d487f23becc

![0_01](assets/fr/01.webp)



Mara baada ya ISO kuthibitishwa, unahitaji kuunda kati ya usakinishaji wa bootable, kwa kawaida fimbo ya USB. Ili kufanya hivyo, pakua na usakinishe programu kama vile **Rufus** kwenye Windows au **Etcher** kwenye Windows, Linux au macOS. Zana hizi hukuwezesha kunakili ISO kwenye fimbo ya USB ili iweze kuendeshwa.



Kabla ya kuanza usakinishaji, ni muhimu kusanidi **BIOS au UEFI** ya kompyuta yako ili **kuwezesha virtualization** na kuruhusu boot kutoka USB. Kulingana na muundo wa mashine yako, inaweza kuhitajika **kuzima Secure Boot**, kwani Qubes OS inaweza isiwashe ikiwa chaguo hili limewashwa.



![0_02](assets/fr/02.webp)



Mara tu masharti haya yametimizwa, fungua upya kompyuta yako na ufikie BIOS/UEFI kwa kubofya mara moja **Esc**, **Del**, **F9**, **F10**, **F11** au **F12** (kulingana na mtengenezaji). Katika menyu ya kuwasha, chagua kitufe cha USB kama kifaa cha kuwasha ili kuzindua usakinishaji wa Qubes OS.



**Skrini ya kuanza**


Unapoanzisha kutoka kwa fimbo ya USB, utachukuliwa moja kwa moja kwenye menyu ya **GRUB**, ambapo unaweza kuchagua kitendo cha kufanywa. Kwa kutumia vitufe vya mshale kwenye kibodi yako, chagua "Sakinisha Qubes OS" na ubonyeze "Ingiza".



![0_03](assets/fr/03.webp)



**Chaguo la lugha** :



Wakati usakinishaji unapoanza, hatua ya kwanza ni **kuchagua lugha** na **lahaja ya kieneo** inayofaa kwa usanidi wako. Hii inahakikisha kwamba mfumo na chaguo za usakinishaji zinaonyeshwa kwa usahihi katika lugha unayopendelea.



![0_04](assets/fr/04.webp)



**Mipangilio ya kigezo** :



Katika hatua hii, utahitaji kusanidi idadi ya Elements kabla ya kuzindua usakinishaji kwenye mashine yako.



![0_05](assets/fr/05.webp)



**Mpangilio wa kibodi** :



Bofya chaguo la **Kibodi**, kisha uchague **mpangilio unaofaa** wa kompyuta yako. Mara tu unapofanya chaguo lako, bofya **Imesimamishwa** ili kuendelea na hatua inayofuata.



**Chaguo la marudio** :



Teua chaguo la "Njia ya usakinishaji" ili kuchagua diski ambayo ungependa kusakinisha Qubes OS. Kwa chaguo-msingi, ugawaji hufanyika moja kwa moja, kukuwezesha kuondoa data zote kutoka kwenye diski na kufunga mfumo juu yake. Hata hivyo, unaweza kuchagua **Iliyobinafsishwa** au **Ubinafsishaji wa Hali ya Juu** ili kutekeleza ugawaji uliobinafsishwa. Kisha bonyeza "Imefanyika". Mfumo utakuuliza uweke **nenosiri**, ambalo hutumika kama Layer ya usalama ili kusimba data yako. Hakikisha kuchagua nenosiri ngumu na la kipekee.



![0_06](assets/fr/06.webp)



![0_07](assets/fr/07.webp)



**Chagua muundo wa tarehe na saa** :


Bofya chaguo la Muda na tarehe, kisha uchague eneo lako la kijiografia. Unaweza pia kuchagua umbizo la wakati unaopendelea: 24h au 12h.



![0_08](assets/fr/08.webp)



**Uundaji wa akaunti ya mtumiaji** :


Bofya kwenye **Unda mtumiaji** ili kuunda **akaunti yako ya kwanza**, ambayo itakuwezesha kuingia kwenye Qubes OS.



![0_09](assets/fr/09.webp)



**Wezesha akaunti ya mizizi** :


Unaweza pia **kuwezesha akaunti ya mizizi** kwa kuweka nenosiri tofauti kwa usimamizi.



![0_10](assets/fr/10.webp)



Mara tu mipangilio hii imefanywa, bofya kwenye **Anza usakinishaji** ili kuanza mchakato.



![0_11](assets/fr/11.webp)



Subiri **mwisho wa usakinishaji**, kisha ubofye kwenye **anzisha upya mfumo** ili kukamilisha usakinishaji na uanzishe Qubes OS.



![0_12](assets/fr/12.webp)



**Mipangilio ya ziada** :


Baada ya kuwasha upya, Qubes OS inakuomba ukamilishe **violezo chaguomsingi na usanidi wa qubes**. Ingiza nenosiri lililofafanuliwa ili kusimba diski kwa njia fiche.



![0_13](assets/fr/13.webp)



Ifuatayo, anza kwa kuchagua **TemplateVM** unayotaka kusakinisha. Chaguo za kawaida ni pamoja na **Debian 12 Xfce**, **Fedora 41 Xfce** na **Whonix 17**, ya mwisho ikipendekezwa kwa matumizi yanayohitaji **kutokujulikana na usalama wa mtandao**. Unaweza pia kufafanua **kiolezo chaguomsingi**, ambacho kitatumika kama msingi wa kuunda **AppVM** mpya.



![0_14](assets/fr/14.webp)



Katika sehemu ya **Usanidi Mkuu**, unaweza kuchagua kuunda kiotomatiki qubes muhimu za mfumo kama vile **sys-net**, **sys-firewall** na **chaguo-msingi ya DisposableVM**. Inashauriwa kuwezesha chaguo la kufanya **sys-firewall na sys-usb disposable**, ili kupunguza udhihirisho wa kifaa na mtandao katika tukio la maelewano. Unaweza pia kuunda **AppVM** chaguomsingi, kama vile **binafsi**, **kazi**, **isiyoaminika** na **vault**, ili kupanga shughuli zako kulingana na kiwango chao cha uaminifu.



![0_15](assets/fr/15.webp)



Qubes OS pia hukuruhusu kuunda **qube iliyoundwa kwa vifaa vya USB** (sys-usb) na usanidi **Whonix Gateway na Workstation qubes** ili kulinda mawasiliano yako kupitia mtandao wa Tor. Kwa watumiaji wa hali ya juu, sehemu ya **Usanidi wa hali ya juu** hukuruhusu kuunda **dimbwi nyembamba la LVM** ili kudhibiti vyema nafasi ya diski kati ya qubes.



Mara tu chaguo hizi zote zimesanidiwa, bofya kwenye **Kamilisha**, kisha kwenye **Maliza usanidi**. Subiri wakati mfumo unatumia mipangilio hii. Kisha utaombwa **kuingia katika akaunti yako ya mtumiaji**, na mazingira yako ya Qubes OS yatakuwa tayari kutumika, salama na yakitengwa ipasavyo kwa shughuli zako mbalimbali.



![0_17](assets/fr/17.webp)



Mfumo wako wa uendeshaji sasa umesakinishwa na uko tayari kutumika.



![0_18](assets/fr/18.webp)



## Unda qube kwenye mfumo wako



Ili kuunda qube, mchakato unasimamiwa na zana ya **Qube Manager**, inayopatikana kutoka kwa menyu ya Mwanzo. Katika dirisha la zana, bofya tu kwenye ikoni ya **Unda qube** ili kufungua dirisha jipya la usanidi. Kwanza, weka jina la qube yako, kama vile "mtandao wa kibinafsi" au "kazi", ili kutambua matumizi yake.



Ifuatayo, utachagua **Aina** yake, kwa kawaida **AppVM** kwa kazi za kawaida, au **DisposableVM** kwa matumizi ya muda. Ni muhimu kuchagua **Kiolezo** ambacho qube yako itategemea, kama vile "fedora-39" au "debian-12", kwa kuwa hii itatoa mfumo wa uendeshaji na programu. Pia utateua **NetVM**, ambayo ndiyo inayohusika na ufikiaji wa Mtandao, kwa chaguo-msingi **sys-firewall**.



Hatimaye, baada ya kurekebisha ukubwa wa hifadhi na RAM ikiwa ni lazima, bonyeza rahisi kwenye ** OK ** itazindua mchakato wa uumbaji. Mara tu mchakato utakapokamilika, qube yako mpya itaonekana kwenye orodha na tayari kutumika.



Kwa kumalizia, Qubes OS sio mfumo wa uendeshaji wa kawaida, lakini suluhisho la usalama la hali ya juu ambalo linafikiria upya usanifu wa kompyuta ya kibinafsi. Mtazamo wake, unaozingatia ugawaji na kutengwa kwa njia ya mtandaoni, hutoa ulinzi usio na kifani dhidi ya vitisho vya hali ya juu zaidi. Kwa kugawa mazingira ya kazi katika qubes maalum kwa kila kazi, inahakikisha kuwa programu hasidi haiwezi kuenea na kuhatarisha mfumo mzima.



Iwe unahitaji kuvinjari wavuti kwa usalama, kulinda taarifa nyeti au kufanya kazi kwa viwango tofauti vya uaminifu, Qubes OS hutoa mfumo thabiti na wa uwazi. Kwa kufuata mazoea mazuri na kutumia vipengele vyake kikamilifu, utakuwa na **ngome ya kidijitali** iliyorekebishwa kulingana na vitisho vya kisasa. Pata maelezo zaidi kuhusu kulinda data na faragha yako.



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1