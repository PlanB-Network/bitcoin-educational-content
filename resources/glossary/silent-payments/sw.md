---
term: MALIPO YA KIMYA
---

Mbinu ya kutumia anwani tuli za Bitcoin kupokea malipo bila kutumia tena Address, bila mwingiliano, na bila kiungo kinachoonekana cha On-Chain kati ya malipo tofauti na Address tuli. Mbinu hii huondoa hitaji la generate mpya, anwani za kupokea ambazo hazijatumika kwa kila shughuli, hivyo basi kuzuia mwingiliano wa kawaida katika Bitcoin ambapo mpokeaji lazima atoe Address mpya kwa mlipaji.


Kwa Malipo ya Kimya, mlipaji hutumia funguo za umma za mpokeaji (tumia ufunguo wa umma na uchanganue ufunguo wa umma) na jumla ya funguo zao za kibinafsi kama ingizo kwa generate Address mpya kwa kila malipo. Ni mpokeaji pekee, aliye na funguo zake za faragha, anayeweza kukokotoa ufunguo wa faragha unaolingana na malipo haya ya Address. ECDH (*Elliptic-Curve Diffie-Hellman*), algoriti ya ufunguo wa kriptografia ya Exchange, inatumiwa kuanzisha siri iliyoshirikiwa ambayo inatumiwa kupata Address inayopokea na ufunguo wa faragha (upande wa mpokeaji pekee). Ili kutambua Malipo ya Kimya yanayokusudiwa, wapokeaji lazima wachanganue Blockchain na wachunguze kila muamala unaolingana na vigezo vya itifaki. Tofauti na BIP47, ambayo hutumia miamala ya arifa kuanzisha njia ya malipo, Malipo ya Kimya huondoa hatua hii, ili kuhifadhi muamala. Hata hivyo, maafikiano ni kwamba mpokeaji lazima achanganue miamala yote inayowezekana ili kubaini, kwa kutumia ECDH, ikiwa inashughulikiwa kwao.


Kwa mfano, Address $B$ tuli ya Bob inawakilisha muunganisho wa ufunguo wake wa kuchanganua wa umma na ufunguo wake wa matumizi ya umma:


$$ B = B_{\text{scan}} \text{ ‖ } B_{\text{spend}} $$


Vifunguo hivi vinatolewa tu kutoka kwa njia ifuatayo:


```text
scan : m / 352' / 0' / 0' / 1' / 0
spend : m / 352' / 0' / 0' / 0' / 0
```


Address hii tuli imechapishwa na Bob. Alice anaipata ili kufanya Malipo ya Kimya kwa Bob. Anakokotoa malipo ya Bob Address $P_0$ kwa njia hii:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot a \cdot B_{\text{scan}} \text{ ‖ } 0) \cdot G $$


Wapi:


$$ \text{inputHash} = \text{Hash}(\text{outpoint}_L \text{ ‖} A) $$


Na:


- $B_{\text{scan}$: Ufunguo wa umma wa kuchanganua wa Bob (Address tuli);
- $B_{\text{spend}}$: Kitufe cha matumizi cha umma cha Bob (tuli Address);
- $A$: Jumla ya funguo za umma katika ingizo (tweak);
- $a$: Ufunguo wa faragha wa tweak, yaani, jumla ya jozi zote muhimu zinazotumiwa katika `scriptPubKey` ya UTXO zinazotumiwa kama maingizo katika shughuli ya Alice;
- $\text{outpoint}_L$: UTXO ndogo zaidi (kieleksikografia) inayotumika kama ingizo katika shughuli ya Alice;
- $\text{ ‖ }$: Muunganisho (operesheni ya kuunganisha uendeshaji mwisho hadi mwisho);
- $G$: Sehemu ya jenereta ya curve ya duaradufu `secp256k1`;
- $\text{Hash}$: Chaguo za kukokotoa za SHA256 Hash zilizowekwa alama ya `BIP0352/SharedSecret`;
- $P_0$: Ufunguo wa kwanza wa umma / Address ya kipekee kwa malipo kwa Bob;
- $0$: Nambari kamili inayotumiwa kwa generate anwani nyingi za kipekee za malipo.


Bob huchanganua Blockchain ili kupata Malipo yake ya Kimya kwa njia hii:


$$ P_0 = B_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0) \cdot G $$


Na:


- $b_{\text{scan}$: Ufunguo wa faragha wa Bob wa kuchanganua.


Akipata $P_0$ kama Address iliyo na Malipo ya Kimya aliyoelekezwa, atakokotoa $p_0$, ufunguo wa kibinafsi unaomruhusu kutumia pesa zilizotumwa na Alice hadi $P_0$:


$$ p_0 = (b_{\text{spend}} + \text{Hash}(\text{inputHash} \cdot b_{\text{scan}} \cdot A \text{ ‖ } 0)) \mod n $$


Na:


- $b_{\text{spend}}$: Ufunguo wa matumizi wa kibinafsi wa Bob;
- $n$: mpangilio wa curve ya duaradufu `secp256k1`.


Kando na toleo hili la msingi, lebo pia zinaweza kutumika kwa generate anwani kadhaa tofauti tuli kutoka kwa Address ya msingi sawa, kwa lengo la kutenganisha matumizi mengi bila kuzidisha kazi inayohitajika wakati wa kuchanganua bila sababu.