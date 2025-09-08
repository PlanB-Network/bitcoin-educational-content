---
name: Lynis
description: Fanya ukaguzi wa usalama wa mashine ya Linux na Lynis
---
![cover](assets/cover.webp)



___



*Mafunzo haya yanatokana na maudhui asili ya Fares CHELLOUG iliyochapishwa kwenye [IT-Connect](https://www.it-connect.fr/). Leseni [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Huenda mabadiliko yamefanywa kwa maandishi asilia.*



___



## I. Uwasilishaji



**Katika somo hili, tutajifunza jinsi ya kufanya ukaguzi wa usalama kwenye mashine ya Linux kwa kutumia Lynis! Kwa wale ambao hamjui **Lynis,** ni matumizi madogo ya mstari wa amri ambayo yatachanganua usanidi wa seva yako na kutoa mapendekezo ya **kuboresha usalama wa mashine yako.**



Lynis ni zana huria kutoka kwa CISOFY, kampuni inayobobea katika **ukaguzi wa mfumo na ugumu**. Ikiwa unataka kufanya maendeleo katika ugumu wa Linux na huduma maarufu (SSH, Apache2, nk.), Lynis ni mshirika wako! Lynis sio tu anakuambia nini kinaendelea vibaya, lakini pia hutoa mapendekezo ili kukuelekeza kwenye mwelekeo sahihi (na kuokoa muda).



**Lynis** hufanya kazi na usambazaji mwingi wa Linux, ikijumuisha: **Debian, FreeBSD, HP-UX, NetBSD, NixOS, OpenBSD, Solaris**. Lynis inalenga watumiaji wa Linux / UNIX, lakini pia ni **macOS** sambamba. Haraka sana kusakinisha, hakuna usimamizi wa utegemezi katika kiwango cha kifurushi.



Inatumika kwa madhumuni anuwai:





- Ukaguzi wa usalama
- Jaribio la kufuata (PCI, HIPAA na SOX)
- Mipangilio ngumu zaidi ya mfumo
- Utambuzi wa hatari



Chombo hiki kinatumiwa sana na watumiaji mbalimbali, ikiwa ni pamoja na wasimamizi wa mfumo, wakaguzi wa IT na wapentesta. Kwa uchanganuzi, zana inategemea viwango kama vile **CIS Benchmark, NIST, NSA, OpenSCAP** na mapendekezo rasmi kutoka kwa **Debian, Gentoo, Red Hat**.



Mradi unapatikana katika Address hii kwenye **Github**:





- [GitHub - Lynis](https://github.com/CISOfy/lynis)
- [Pakua Lynis kutoka CISOFY](https://cisofy.com/lynis/#pakua)



Katika mafunzo haya ya hatua kwa hatua, nitatumia ** kutumia VPS inayoendesha Debian 12** na nitazingatia sehemu ya SSH, kwani ningependa kuangalia usanidi wake na kuiboresha.



## II. Pakua na usakinishe



Kuna njia kadhaa za kupakua na kusakinisha Lynis. Chagua unayopendelea kutoka kwenye orodha iliyo hapa chini.



### A. Usakinishaji kutoka kwa hazina za Debian



Hali hii ya usakinishaji hukuruhusu kutumia amri ya **lynis** kutoka mahali popote kwenye mfumo, tofauti na usakinishaji kutoka kwa chanzo, ambapo unahitaji kuwa iko kwenye saraka.



Unganisha kwa seva yako kupitia SSH na uweke amri zifuatazo ili kusakinisha Lynis:



```
sudo apt-get update
sudo apt-get install lynis -y
```



Hii ndio unayopata:



![Image](assets/fr/024.webp)



### B. Pakua kutoka kwa tovuti rasmi



Unaweza pia kuipakua kutoka kwa wavuti ya Cisofy:



```
sudo wget https://downloads.cisofy.com/lynis/lynis-3.0.9.tar.gz
```



Hii ndio unayopata:



![Image](assets/fr/032.webp)



Ifuatayo, tutafungua kumbukumbu kwa kutumia amri ifuatayo:



```
sudo tar -zxf lynis-3.0.9.tar.gz
```



Hii ndio unayopata:



![Image](assets/fr/020.webp)



Wacha tuhamie kwenye folda ya **lynis**:



```
cd lynis
```



Tunaweza kuangalia sasisho kwa amri ifuatayo:



```
./lynis update info
```



Hii ndio unayopata:



![Image](assets/fr/023.webp)



### C. Pakua kutoka GitHub



Tutapakua **Lynis** kutoka kwa hazina rasmi ya GitHub, kwa kutumia amri ifuatayo (*git* lazima iwepo kwenye mashine yako):



```
git clone https://github.com/CISOfy/lynis.git
```



Hii ndio unayopata:



![Image](assets/fr/060.webp)



## III. Kutumia Lynis



Lynis yupo kwenye mashine yetu, kwa hivyo hebu tujifunze jinsi ya kuitumia!



### A. Vidhibiti kuu na chaguzi



Ili kuonyesha amri zinazopatikana, ingiza tu amri ifuatayo:



```
sudo lynis
# Si vous avez récupéré Lynis depuis les sources, utilisez cette syntaxe:
./lynis
```



Hii ndio unayopata:



![Image](assets/fr/039.webp)



Na pia unapata chaguzi zifuatazo:



![Image](assets/fr/040.webp)



Ili kuonyesha amri zote zinazopatikana, ingiza amri ifuatayo:



```
sudo lynis show
```



Hii ndio unayopata:



![Image](assets/fr/022.webp)



Ikiwa ungependa kuonyesha chaguzi zote, lazima uweke:



```
sudo lynis show options
```



Hii ndio unayopata:



![Image](assets/fr/021.webp)



Katika mapumziko ya makala hii, tutajifunza jinsi ya kutumia chaguo fulani.



### B. Kufanya ukaguzi wa mfumo



Tutauliza **Lynis** kukagua mfumo wetu, kuangazia kile ambacho kimesanidiwa kwa usahihi na kinachoweza kuboreshwa. Ili kufanya hivyo, ingiza amri ifuatayo:



```
sudo lynis audit system
# ou
./lynis audit system
```



Kwa chaguo-msingi, ikiwa hujaingia kama mzizi unapoendesha amri hii, zana itaendesha na haki za mtumiaji aliyeingia kwa sasa. Baadhi ya majaribio hayataendeshwa katika muktadha huu:



![Image](assets/fr/052.webp)



Hapa kuna majaribio ambayo hayatafanywa katika hali hii:



![Image](assets/fr/051.webp)



Mara tu amri imetekelezwa, uchambuzi huanza. Subiri kidogo tu.



Mwisho wa ukaguzi, unapata hii (tunaweza kuona kwamba **Lynis** ametambua kwa usahihi mfumo wa **Debian 12** na atatumia ** programu-jalizi ya Debian ** kwa uchambuzi):



![Image](assets/fr/017.webp)



Ifuatayo, Lynis ataorodhesha seti ya alama zinazolingana na kila kitu ambacho ameangalia kwenye mfumo wetu. Hii imepangwa kwa kategoria, kama tutakavyoona. Inafaa pia kuzingatia kuwa nambari ya rangi hutumiwa kuangazia mapendekezo:





- Nyekundu** kwa Elements muhimu au mbinu bora zisizoheshimiwa (kifurushi kinachokosekana, kwa mfano), yaani, seva yako haiheshimu hatua hii.
- Njano** kwa mapendekezo au utiifu wa pendekezo kwa kiasi (tuseme ni nyongeza kutii hoja iliyoangaziwa na rangi hii (isiyo kipaumbele))
- Green** kwa pointi ambapo usanidi wa seva yako unatii
- Nyeupe**, wakati upande wowote



Hapa, tunaweza kuona kwamba Lynis anapendekeza kusakinisha **fail2ban**:



![Image](assets/fr/057.webp)



Katika sehemu ya "**Kuwasha na huduma**", tunaona kwamba ulinzi wa huduma kupitia *systemd* unaweza kuboreshwa. Kwa upande mzuri, Grub2 iko na hakuna shida na ruhusa kwenye:



![Image](assets/fr/029.webp)



Kisha unayo sehemu za "**Kernel**" na "**Kumbukumbu na Mchakato**":



![Image](assets/fr/037.webp)



Ifuatayo, sehemu ya "**Watumiaji, Vikundi na Uthibitishaji**". Zana inatufahamisha kuhusu onyo kuhusu ruhusa za saraka ya "**/etc/sudoers.d**". Kwa sasa, hatujui zaidi, lakini tutaweza kuona pendekezo ni nini mwishoni mwa uchanganuzi.



![Image](assets/fr/049.webp)



Hivi ndivyo unavyoweza kupata katika sehemu za "**Shells", "Files Systems", na "Vifaa vya USB "**. Miongoni mwa mambo mengine, tunaweza kuona kwamba kuna mapendekezo juu ya pointi za mlima na kwamba vifaa vya USB vinaruhusiwa kwa sasa kwenye mashine hii.



![Image](assets/fr/048.webp)



Kisha, sehemu: "**Huduma za majina", "Bandari na vifurushi", "Mitandao".** Inaonyesha hapa kwamba vifurushi ambavyo havitumiki tena vinaweza kusafishwa na kwamba hakuna huduma inayoweza kudhibiti masasisho ya kiotomatiki.



![Image](assets/fr/058.webp)



Tunaweza kuona kuwa firewall imewashwa (na ndio, kuna iptables!). Kwa kuongeza, tunaweza kuona kwamba imepata sheria zisizotumiwa na kwamba seva ya mtandao ya Apache imewekwa.



![Image](assets/fr/055.webp)



Hii inafuatwa na uchambuzi wa seva ya wavuti yenyewe, kwani huduma imetambuliwa.



Tunaweza kuona kwamba imepata faili za usanidi **Nginx**, na kwamba kwa sehemu ya SSL/TLS, **ciphers** zimesanidiwa kwa matumizi ya itifaki ambayo haitakuwa salama. Kwa upande mwingine, kulingana na Lynis, usimamizi wa logi ni sahihi.



![Image](assets/fr/038.webp)



Huduma ya SSH iko kwenye seva yangu ya VPS. Usanidi wake unachambuliwa na Lynis. Inapaswa kusemwa kuwa usalama wa SSH unaweza kuboreshwa kwa urahisi! Tutarudi kwenye eneo hili kwa undani mara tu tutakapopata mapendekezo.



![Image](assets/fr/026.webp)



Hapa kuna sehemu **"Msaada wa SNMP", "Hifadhi", "PHP", "Usaidizi wa Squid", "Huduma za LDAP", "Kuweka kumbukumbu na faili "**.



Kuna pendekezo moja muhimu sana kuhusu usimamizi wa kumbukumbu: inapendekezwa sana kwamba usihifadhi kumbukumbu tu ndani ya mashine yako. Ikiwa mashine iliharibiwa na mshambuliaji, kuna uwezekano kwamba angejaribu kufuta athari zake... Kwa hivyo tunahitaji kuweka kumbukumbu nje.



![Image](assets/fr/050.webp)



Hapa, tuna ukaguzi wa huduma zilizo katika mazingira magumu, usimamizi wa akaunti, kazi zilizopangwa na maingiliano ya NTP. inaonyeshwa kuwa kiwango ni cha chini kwenye sehemu ya bendera na kitambulisho: hii inaeleweka, ikiwa unaonyesha toleo la mfumo, linatoa dalili kwa mshambuliaji anayeweza. Huu ndio mpangilio chaguo-msingi.



Itapendeza kuamilisha **auditd** ili kuwa na kumbukumbu endapo kuna uchanganuzi wa **uchunguzi**. **NTP** pia imeangaliwa, kwa sababu ili kutafuta kumbukumbu kwa ufanisi, ni vyema kuwa na mifumo kwa wakati, ambayo hurahisisha utafutaji.



![Image](assets/fr/036.webp)



Lynis kisha anaangalia kriptografia Elements, uboreshaji, vyombo na mifumo ya usalama. Baadhi ya sehemu ni tupu kwa sababu hakuna mawasiliano na mashine iliyochanganuliwa. Hata hivyo, tunaweza kuona kwamba nina vyeti viwili vya SSL vilivyokwisha muda wake na sijawasha **SELinux**.



![Image](assets/fr/027.webp)



Hapa pia kuna nafasi ya kuboresha: hakuna kinza virusi au kichanganuzi cha kuzuia programu hasidi, na tuna mapendekezo juu ya ruhusa za faili.



![Image](assets/fr/028.webp)



Kisha, Lynis anaangazia kuimarisha usanidi wa kernel ya Linux (pamoja na sheria za runda la IPv4), pamoja na usimamizi wa saraka za "Nyumbani" za mashine ya Linux.



![Image](assets/fr/035.webp)



Tumefika mwisho wa uchanganuzi... Hoja hii ya mwisho inaonyesha kuwa tutapata kila kitu kutokana na kuwa na ClamAV kwenye mashine hii.



![Image](assets/fr/030.webp)



## IV. Mapendekezo



Baada ya ukaguzi, ni wakati wa kusoma na kuchambua mapendekezo. Hapa ndipo tunapata mapendekezo na maelezo kwa kila moja ya majaribio yaliyofanywa na Lynis.



Chukua mapendekezo ya SSH, kwa mfano. **Kwa kila pendekezo, utapata kigezo kilichopendekezwa na kiungo kitakachoeleza uhakika wa usalama ** Ni juu yako kuamua, kulingana na muktadha na matumizi yako.



Hebu tuangalie mifano michache ya mapendekezo ambayo yanaangazia moja kwa moja mambo yaliyoangaziwa katika ukaguzi wote...



### A. Mifano ya mapendekezo





- Kama tulivyoona hapo awali, NTP ni muhimu kwa magogo ya kugonga wakati:



![Image](assets/fr/043.webp)





- Lynis pia anapendekeza kusakinisha kifurushi cha **apt-listbugs** ili kupata taarifa kuhusu hitilafu muhimu wakati wa usakinishaji wa kifurushi kupitia **apt.**



![Image](assets/fr/041.webp)





- Zana inapendekeza tusakinishe **needrestart ili kuweza** kuona ni michakato gani inayotumia toleo la zamani la maktaba na inahitaji kuanzishwa upya.



![Image](assets/fr/054.webp)





- Pendekezo hili linapendekeza kusakinisha **fail2ban** ili kuzuia kiotomatiki wapangishi ambao wanashindwa kuthibitisha (hasa nguvu ya kinyama).



![Image](assets/fr/044.webp)





- Ili kuimarisha huduma za mfumo, anapendekeza tuendeshe amri ya bluu kwa kila huduma kwenye mashine yetu.



![Image](assets/fr/056.webp)





- Anapendekeza kuweka tarehe za mwisho wa matumizi ya nywila zote za akaunti zilizolindwa.



![Image](assets/fr/031.webp)





- Pendekezo hili linapendekeza kuweka thamani za chini na za juu zaidi kwa umri wa nenosiri. Miongoni mwa mambo mengine, hii itahakikisha kwamba nywila zinabadilishwa mara kwa mara.



![Image](assets/fr/042.webp)





- Tunapendekeza kutumia partitions tofauti, ili kupunguza athari za matatizo ya nafasi ya disk kwenye sehemu moja.



![Image](assets/fr/047.webp)





- Pendekezo hili linapendekeza kuzima hifadhi ya USB na firewire ili kuzuia kuvuja kwa data



![Image](assets/fr/033.webp)





- Ili kukidhi pendekezo hili, sakinisha tu na usanidi **uboreshaji usiotarajiwa**, kwa mfano.



![Image](assets/fr/053.webp)



### B. Kufunga vifurushi vinavyopendekezwa



Ili kuboresha usanidi wa mfumo, tutasakinisha vifurushi vingine kwenye mashine: vingine vilivyopendekezwa na Lynis, vingine ambavyo ninapendekeza kibinafsi.



Utakuwa na msingi mzuri wa kufanyia kazi, mradi tu utumie muda kidogo kuzisanidi. Ili kufanya hivyo, rejelea tovuti ya IT-Connect, makala nyingine kwenye Wavuti na nyaraka za zana.



```
sudo apt-get install debsums apt-listbugs needrestart apt-show-versions fail2ban unattended-upgrades clamav clamav-daemon rkhunter
```



Habari fulani kuhusu vifurushi vilivyosakinishwa:





- Clamav** ni antivirus.
- masasisho yasiyotarajiwa** yatakuwezesha kudhibiti masasisho yako kiotomatiki na hata kuwasha upya mashine au kusafisha kiotomatiki vifurushi vya zamani, inaweza kusanidiwa kikamilifu.
- rkhunter** ni anti-rootkit ambayo huchanganua mfumo wako wa faili.
- Fail2ban** itajikita kwenye faili zako za kumbukumbu kulingana na kile unachoipa kusoma na itafanya kazi na **iptables**, kwa mfano kupiga marufuku anwani za IP zinazojaribu "kulazimisha" seva yako katika SSH.



### C. Mapendekezo ya SSH



Wacha tuangalie mapendekezo ya SSH. Zimeorodheshwa hapa chini. Usijali, tutaelezea mara moja jinsi ya kuboresha usanidi.



![Image](assets/fr/034.webp)



Wacha tuangalie kwa karibu usanidi wangu wa sasa wa **SSH** katika:**/etc/ssh/sshd_config**



![Image](assets/fr/018.webp)



Usanidi uliopendekezwa hapa chini bado unaweza kuboreshwa, lakini hukupa msingi mzuri. *Tafadhali kumbuka kuwa nimeondoa maoni kadhaa ili yaweze kusomeka zaidi*.



Tutafanya:





- Badilisha mlango wa unganisho wa SSH (sahau chaguo-msingi 22)
- Ongeza kiwango cha vitenzi vya kumbukumbu, kutoka **INFO hadi VERBOSE**
- Weka **LoginGraceTime** hadi **dakika 2**



Ikiwa hakuna habari ya uunganisho imeingizwa ndani ya dakika mbili, uunganisho umekatika.





- Washa **Modi kali**



Inabainisha kama "sshd" inapaswa kuangalia modi na mmiliki wa faili za mtumiaji pamoja na saraka ya nyumbani ya mtumiaji kabla ya kuthibitisha muunganisho. Hii ni kawaida kuhitajika, kwa sababu wakati mwingine wanovices huacha saraka au faili zao kwa bahati mbaya kupatikana kwa kila mtu. Chaguo msingi ni "ndio".





- Weka **MaxAuthtries** hadi 3



Hii inawakilisha idadi ya majaribio yasiyofanikiwa ya uthibitishaji kabla ya mawasiliano kufungwa.





- Weka **MaxSessions** hadi 2



Hii inawakilisha idadi ya juu zaidi ya vipindi vya wakati mmoja.





- Washa uthibitishaji wa ufunguo wa umma



```
PubkeyAuthentication yes
```





- Hifadhi uthibitishaji wa nenosiri:



```
PasswordAuthentication yes
```



Kataza nenosiri tupu na **Kerberos** uthibitishaji, pamoja na **uthibitishaji wa mizizi moja kwa moja**



```
PermitEmptyPasswords no
PermitRootLogin no
```



Hakikisha una "**PermitRootLogin no", ikiwa ni sawa na "ndiyo", ni "mbaya kabisa"**.





- Kataza uelekezaji upya wa muunganisho wa TCP



```
AllowTcpForwarding no
```



Inaonyesha kama uelekezaji upya wa TCP unaruhusiwa, na "ndiyo" kama mpangilio chaguomsingi. Tafadhali kumbuka: kulemaza uelekezaji kwingine wa TCP hakuongezei usalama ikiwa watumiaji wanaweza kufikia shell, kwani bado wanaweza kusanidi zana zao za kuelekeza kwingine.





- Kataza uelekezaji upya wa X11



```
X11Forwarding no
```



Inaonyesha kama uelekezaji upya wa X11 unakubaliwa, na "hapana" kama mpangilio chaguomsingi. Tafadhali kumbuka: hata ikiwa uelekezaji upya wa X11 umezimwa, hii haiongezi usalama, kwani watumiaji bado wanaweza kusanidi waelekezi wao wenyewe. Uelekezaji upya wa X11 huzimwa kiotomatiki ikiwa **UseLogin** imechaguliwa.





- Weka muda wa mawasiliano kati ya mteja na sshd



```
ClientAliveInterval  300
```



Inafafanua muda wa muda kwa sekunde, baada ya hapo, ikiwa hakuna data iliyopokelewa kutoka kwa mteja, huduma ya sshd hutuma ujumbe unaoomba jibu kutoka kwa mteja. Kwa chaguo-msingi, chaguo hili limewekwa kuwa "0", kumaanisha kuwa ujumbe huu hautumwi kwa mteja. Toleo la 2 pekee la itifaki ya SSH ndilo linaloauni chaguo hili.



```
ClientAliveCountMax 0
```



Kulingana na [hati (*ukurasa wa mtu*) ya sshd](https://www.delafond.org/traducmanfr/man/man5/sshd_config.5.html), chaguo hili linamaanisha nini: "Huweka idadi ya ujumbe wa kusimamisha kazi (tazama hapo juu) kutumwa bila jibu kutoka kwa mteja kwa **sshd**. Ikiwa kipengee cha kusitisha ** kimefikiwa mteja na kusitisha kipindi Ni muhimu kutambua kuwa ujumbe huu wa kushikilia ni tofauti sana na chaguo la **KeepAlive** (hapa chini) Ujumbe wa kushikilia muunganisho hutumwa kupitia handaki iliyosimbwa kwa njia fiche, na kwa hivyo haiwezi kughushi muunganisho wa kiwango cha TCP unaowezeshwa na **KeepAlive** unaweza kughushi ikiwa uunganisho wa muunganisho unahitajika.





- Zuia ufichuaji wa habari kwa kuzima **motd, bango, lastlog**



```
PrintMotd no
```



Inabainisha ikiwa sshd inapaswa kuonyesha maudhui ya faili "/etc/motd" mtumiaji anapoingia katika hali ya mwingiliano. Kwenye baadhi ya mifumo, maudhui haya yanaweza pia kuonyeshwa na shell, kupitia /etc/profile au faili sawa. Thamani chaguo-msingi ni "ndiyo".



```
Banner none
```



Ni vyema kutambua kwamba katika baadhi ya maeneo, kutuma ujumbe kabla ya uthibitishaji inaweza kuwa sharti la ulinzi wa kisheria. Yaliyomo kwenye faili maalum hupitishwa kwa mtumiaji wa mbali kabla ya idhini ya uunganisho kutolewa. Chaguo hili linahitaji kusanidiwa, kwani kwa chaguo-msingi hakuna ujumbe utakaoonyeshwa.



Katika picha, hii inatoa:



![Image](assets/fr/019.webp)



### D. Alama ya ukaguzi



Hatimaye, tusisahau kuangalia **alama ya ukaguzi wa Lynis**! Tunaona kwamba **alama yangu ya Ugumu ni 63** na kwamba faili ya ripoti inaweza kutazamwa katika "**/var/log/lynis-report.dat**". Pia kuna faili "**/var/log/lynis.log**".



**Kwa maneno mengine, kadiri alama inavyokuwa juu, ndivyo inavyokuwa bora zaidi! Kwa hivyo unahitaji kufanyia kazi usanidi wako ili kufikia alama ya juu zaidi, huku ukiruhusu mashine yako na huduma zinazopangishwa kufanya kazi kama kawaida (ambayo inamaanisha kufanya majaribio ya utendakazi).



![Image](assets/fr/046.webp)



Hebu tuangalie matokeo kwenye seva yangu ya pili, ambapo nilitumia muda kidogo zaidi kufanya ugumu! Kwa hivyo ni kawaida kuwa alama ni ya juu (**76**).



![Image](assets/fr/045.webp)



## V. Lynis mipango ya kiotomatiki



**Lynis** pia inatoa chaguo la kuendesha ukaguzi wake kupitia kazi iliyoratibiwa. Kwa kweli kuna chaguo la **"--cronjob "**, ambalo litaendesha majaribio yote ya Lynis bila hitaji la uthibitishaji au hatua ya mtumiaji. Basi unaweza kuunda kwa urahisi hati ambayo itaendesha **Lynis** na kuweka pato katika faili iliyopigwa mhuri na jina la seva inayohusika. Hapa kuna faili ya aina hii ambayo unaweza kuweka kwenye folda ya */etc/cron.daily*:



```
#!/bin/sh
mkdir /var/log/lynis
NOM_AUDITEUR="tache_crontab"
DATE=$(date +%Y%m%d)
HOTE=$(hostname)
LOG_DIR="/var/log/Lynis"
RAPPORT="$LOG_DIR/rapport-${HOTE}.${DATE}"
DATA="$LOG_DIR/rapport-data-${HOTE}.${DATE}.txt"

cd /root/Lynis./Lynis -c --auditor "${NOM_AUDITEUR}" --cronjob > ${RAPPORT}
mv /var/log/lynis-report.dat ${DATA}
```



**"AUDITOR_NAME "** kigezo ni kigezo tu ambacho tutaweka katika **"--mkaguzi "** chaguo la **Lynis** ili jina hili lionyeshwe kwenye ripoti:



![Image](assets/fr/059.webp)



Pia tutaunda vianufa vichache vya muktadha ambavyo vitatusaidia kujipanga vyema, kama vile jina la mwenyeji na tarehe ya kutaja ripoti na kuiweka muhuri wa saa, na njia ya kuelekea kwenye folda ambayo tunataka kuweka ripoti zetu.



## VI. Hitimisho



Lynis ni zana inayotumika sana ambayo itakusaidia kuokoa muda na kuwa na ufanisi zaidi unapotaka kujua zaidi kuhusu hali ya usanidi wa seva ya Linux, hasa katika masuala ya usalama. Hata hivyo, usisahau kwamba kila urekebishaji lazima ujaribiwe kabla ya kutumiwa katika toleo la umma, kwa kuzingatia matumizi na muktadha wako.



Labda hutatumia usanidi sawa wa VPS iliyofichuliwa kwenye Wavu, ambapo unahitaji muunganisho mmoja tu wa SSH (kwa sababu wewe ndiye mtu pekee anayeunganisha), tofauti na **bastion** au **scheduler** ambayo itahitaji kuzidisha miunganisho ya **SSH.**



Mara tu unapopata usanidi unaokufaa katika suala la ugumu, inashauriwa kupitisha zana ya kiotomatiki ili usilazimike kufanya kazi tena kwa mikono, kwani hii inaweza kuchukua muda na kukabiliwa na makosa. Kwa mfano, unaweza kutumia **: Puppet, Mpishi, Ansible, nk...**



Usisahau kuwasiliana na timu zako kabla ya utekelezaji: unahitaji kuwafanya waelewe ni kwa nini unafanya mabadiliko haya, si kuwaambia tu kuwa unayafanya. Mwishowe, lengo litakuwa kupitisha mazoea mazuri, na hii itaongeza nafasi zako za kufaulu.



Hatimaye, unaweza pia kulinganisha ** Lynis ** na zana zingine, ambazo kuna kadhaa. Iwapo ungependa kuelekea kwenye usimamizi mkuu huku ukisalia kuwa chanzo huria, ninapendekeza zana ya [Wazuh] (https://wazuh.com/).



**Mafunzo haya yamekwisha, furahiya na Lynis!