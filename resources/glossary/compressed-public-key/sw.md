---
term: UFUNGUO WA UMMA ULIOBANWA
---

Ufunguo wa umma hutumiwa katika hati (moja kwa moja kwa njia ya ufunguo wa umma au kama Address) kupokea na kulinda bitcoins. Ufunguo ghafi wa umma unawakilishwa na ncha kwenye mkunjo wa duaradufu, inayojumuisha viwianishi viwili (`x, y`) kila moja ya biti 256. Katika umbizo mbichi, ufunguo wa umma kwa hivyo hupima biti 512, bila kuhesabu baiti ya ziada ili kutambua umbizo. Ufunguo wa umma uliobanwa, kwa upande mwingine, ni uwakilishi wa ufunguo wa umma uliobana zaidi. Inatumia tu `x` kuratibu na kiambishi awali (`02` au `03`) ambacho kinaonyesha usawa wa kuratibu `y` (hata au isiyo ya kawaida).


Iwapo tutarahisisha hili kwa uga wa nambari halisi, ikizingatiwa mkunjo wa duaradufu una ulinganifu kwa heshima na mhimili wa x, kwa nukta yoyote $P$ (`x, y`) kwenye mkunjo, kuna uhakika $P'$ (`x, -y`) ambayo pia itakuwa kwenye mkunjo huu huu. Hii ina maana kwamba kwa kila `x`, kuna thamani mbili tu zinazowezekana za `y`, chanya na hasi. Kwa mfano, kwa abscissa `x` iliyotolewa, kungekuwa na alama mbili $P1$ na $P2$ kwenye mkunjo wa duaradufu, zikishiriki abscissa ile ile lakini na viratibu tofauti:


![](../../dictionnaire/assets/29.webp)

Ili kuchagua kati ya pointi mbili zinazowezekana kwenye ukingo, kiambishi awali kinachobainisha ni `y` ya kuchagua kinaongezwa kwa `x`. Njia hii inaruhusu kupunguza ukubwa wa ufunguo wa umma kutoka biti 520 hadi biti 264 pekee (biti 8 za kiambishi awali + biti 256 za `x`). Uwakilishi huu unajulikana kama aina iliyobanwa ya ufunguo wa umma.


Hata hivyo, katika muktadha wa kriptografia ya mkunjo wa mviringo, hatutumii nambari halisi, lakini sehemu yenye kikomo ya mpangilio `p` (nambari kuu). Katika muktadha huu, "ishara" ya `y` inaamuliwa kwa usawa wake, yaani, ikiwa `y` ni sawa au isiyo ya kawaida. Kiambishi awali `0x02` kisha kinaonyesha hata `y`, huku `0x03` ikionyesha `y` isiyo ya kawaida.


Fikiria mfano ufuatao wa ufunguo mbichi wa umma (nukta kwenye mkunjo wa duaradufu) katika heksadesimali:

```plaintext
K = 04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f
6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f
```


Tunaweza kutenga kiambishi awali, `x`, na `y`:

```plaintext
Prefix = 04
To determine the parity of `y`, we examine the last hexadecimal character of `y`:
```

Msingi wa 16 (heksadesimali): f

Msingi wa 10 (desimali): 15

y ni isiyo ya kawaida

```

The prefix for the compressed public key will be `03`. The compressed public key in hexadecimal becomes:
```

K = 03678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb6

```