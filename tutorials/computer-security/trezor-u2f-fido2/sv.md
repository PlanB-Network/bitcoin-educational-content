---
name: Trezor U2F & FIDO2
description: Stärk din säkerhet på nätet med Trezor
---
![cover](assets/cover.webp)



Trezor-enheter är hårdvaruplånböcker som ursprungligen utformades för att säkra en Bitcoin Wallet, men de har också avancerade alternativ för stark autentisering på webben. Tack vare att de är kompatibla med protokollen **U2F** och **FIDO2** kan du säkra åtkomsten till dina onlinekonton utan att enbart förlita dig på lösenord.



U2F-protokollet (*Universal 2nd Factor*) introducerades av Google och Yubico 2014 och standardiserades sedan av FIDO Alliance. Det gör det möjligt att lägga till en andra fysisk autentiseringsfaktor (2FA) när man loggar in. När den är aktiverad måste användaren, utöver det klassiska lösenordet, godkänna varje försök att ansluta till sitt konto genom att trycka på en knapp på sin Trezor. I det här sammanhanget fungerar Trezor på ett liknande sätt som en Yubikey.



Metoden bygger på asymmetrisk kryptografi: inga hemliga data överförs, vilket gör att nätfiske- eller avlyssningsattacker blir ineffektiva. U2F stöds nu av många onlinetjänster.



Förutom U2F, som möjliggör tvåfaktorsautentisering, stöder Trezors även FIDO2 (*Fast IDentity Online 2.0*), en utveckling av U2F. Detta är ett standardiserat autentiseringsprotokoll från 2018, som utökar logiken i U2F och syftar till att helt ersätta lösenord. Det är baserat på två komponenter: *WebAuthn* (webbläsarsidan) och *CTAP2* (sidan med den fysiska nyckeln). FIDO2 möjliggör "lösenordslös" autentisering: användare identifierar sig enbart via sin Trezor-enhet, som fungerar som en unik kryptografisk token, utan ytterligare lösenord. Detta protokoll är nu kompatibelt med ett antal onlinetjänster, särskilt sådana som är inriktade på företag.



Förutom "lösenordslös*" funktionalitet möjliggör FIDO2 även tvåfaktorsautentisering på liknande sätt som U2F.



FIDO2 introducerar också begreppet resident credentials, dvs. identifierare som lagras direkt i Trezor, som inkluderar både den privata nyckeln som möjliggör anslutning och användarens identifieringsinformation. Denna mekanism möjliggör en helt lösenordsfri autentisering: det är bara att koppla in Trezor och bekräfta åtkomsten utan att ange vare sig ID eller lösenord. Omvänt lagras endast den privata nyckeln i enheten med mer konventionella icke-residenta autentiseringsuppgifter, medan användar-ID:t lagras på serversidan och därför måste anges vid varje anslutning. Vi kommer att titta på hur du sparar dem med din Trezor senare.



I den här guiden får du veta hur du aktiverar U2F eller FIDO2 för tvåfaktorsautentisering och hur du konfigurerar FIDO2 för att komma åt dina konton utan lösenord, direkt med din Trezor.



**U2F är kompatibel med alla Trezor-modeller, men FIDO2 stöds endast av Safe 3, Safe 5 och Model T, inte Model One.



## Använda U2F/FIDO2 för 2FA på en Trezor



Innan du börjar ska du se till att du har konfigurerat din Bitcoin Wallet på din Trezor. Det är viktigt att spara din Mnemonic korrekt, eftersom nycklarna som används för U2F och FIDO2 i tvåfaktorsautentisering härrör från denna Mnemonic. Om din Trezor försvinner eller skadas kan du återfå åtkomst till dina nycklar genom att ange din Mnemonic-fras på en annan Trezor-enhet (observera att för FIDO2-referenser i "*lösenordslöst*"-läge räcker inte enbart seed, vilket vi kommer att se i nästa avsnitt).



Anslut din Trezor till din dator och lås upp den.



![Image](assets/fr/01.webp)



Gå till det konto som du vill säkra med tvåfaktorsautentisering. Till exempel kommer jag att använda ett Bitwarden-konto. Du hittar vanligtvis 2FA-alternativet i tjänsteinställningarna, under flikarna "*autentisering*", "*säkerhet*", "*inloggning*" eller "*lösenord*".



![Image](assets/fr/02.webp)



I avsnittet om tvåfaktorsautentisering väljer du alternativet "*Passkey*" (termen kan variera beroende på vilken webbplats du använder).



![Image](assets/fr/03.webp)



Du kommer ofta att bli ombedd att bekräfta ditt nuvarande lösenord.



![Image](assets/fr/04.webp)



Ge din säkerhetsnyckel ett namn så att du lätt kan känna igen den och klicka sedan på "*Läs nyckel*".



![Image](assets/fr/05.webp)



Dina kontouppgifter visas på Trezor-skärmen. Tryck på skärmen eller på knappen för att bekräfta. Du kommer också att bli ombedd att bekräfta din PIN-kod.



![Image](assets/fr/06.webp)



Registrera denna säkerhetsnyckel.



![Image](assets/fr/07.webp)



Från och med nu, när du vill ansluta till ditt konto, kommer du utöver ditt vanliga lösenord att bli ombedd att ansluta din Trezor.



![Image](assets/fr/08.webp)



Du kan sedan trycka på din Trezor-skärm för att bekräfta autentiseringen.



![Image](assets/fr/09.webp)



Fördelen med att använda en Hardware Wallet Trezor för tvåfaktorsautentisering är att du enkelt kan återställa dina nycklar tack vare Mnemonic-frasen. Utöver denna grundläggande säkerhetskopia kan du också använda en nödkod som tillhandahålls av varje tjänst där du har aktiverat 2FA. Med den här nödkoden kan du ansluta till ditt konto om du tappar bort din säkerhetsnyckel. Den ersätter därför 2FA för en anslutning vid behov.



På Bitwarden kan du t.ex. komma åt denna kod genom att klicka på "*Visa återvinningskod*".



![Image](assets/fr/10.webp)



Jag rekommenderar att du förvarar den här koden på en annan plats än där du förvarar ditt huvudlösenord, för att förhindra att de stjäls tillsammans. Om du till exempel sparar ditt lösenord i en lösenordshanterare ska du förvara din 2FA-nödkod på papper, separat.



Detta tillvägagångssätt ger dig två nivåer av säkerhetskopiering i händelse av förlust av din Trezor för 2FA-autentisering: en första säkerhetskopiering med Mnemonic-frasen för alla dina konton och en andra specifik för varje konto med nödkoderna. Det är dock viktigt att **inte förväxla Mnemonic:s roll med nödkodens** :




- Mnemonic-frasen på 12 eller 24 ord ger dig inte bara tillgång till de nycklar som används för 2FA på alla dina konton, utan också till dina bitcoins som är säkrade med din Trezor;
- Med nödkoden kan du tillfälligt kringgå 2FA-begäran endast på det berörda kontot (i det här exemplet endast på Bitwarden).



## Använda FIDO2 på en Trezor



Förutom tvåfaktorsautentisering möjliggör FIDO2 också "lösenordslös" autentisering, dvs. utan att behöva ange ett lösenord när du loggar in på en webbplats. Anslut helt enkelt din Trezor till din dator för att komma åt ditt säkra konto på detta sätt. Så här konfigurerar du den här funktionen.



Innan du börjar, se till att du har konfigurerat din Bitcoin Wallet på din Trezor. Det är viktigt att spara Mnemonic, eftersom FIDO2 "*passwordless*"-identifierarna är krypterade med din seed (vi kommer att ta reda på hur du sparar dessa identifierare korrekt i nästa avsnitt).



Anslut Trezor till din dator och lås upp den.



![Image](assets/fr/01.webp)



Gå in på det konto du vill säkra i läget "*lösenordslöst*". Jag använder ett Bitwarden-konto som exempel. Det här alternativet finns vanligtvis i tjänstens inställningar, ofta under fliken "*authentication*", "*security*" eller "*password*".



På till exempel Bitwarden finns alternativet under fliken "*Master password*". Klicka på "*Turn on*" för att aktivera autentisering via FIDO2.



![Image](assets/fr/11.webp)



Du kommer ofta att bli ombedd att bekräfta ditt lösenord.



![Image](assets/fr/12.webp)



Dina kontouppgifter visas på Trezor-skärmen. Tryck på skärmen eller på knappen för att bekräfta. Du måste också bekräfta din PIN-kod.



![Image](assets/fr/13.webp)



På webbplatsen lägger du till ett namn för att komma ihåg din säkerhetsnyckel och klickar sedan på "*Turn on*".



![Image](assets/fr/14.webp)



Du kommer sedan att bli ombedd att identifiera dig för att kontrollera att nyckeln fungerar som den ska.



![Image](assets/fr/15.webp)



Från och med nu är det inte längre nödvändigt att ange din e-post Address eller inloggning när du loggar in på ditt konto. Klicka bara på knappen för att autentisera dig med en fysisk nyckel i inloggningsformuläret.



![Image](assets/fr/16.webp)



Bekräfta anslutningen till din Trezor genom att ange din PIN-kod Hardware Wallet.



![Image](assets/fr/17.webp)



Du kommer att vara ansluten till ditt konto utan att behöva ange ditt lösenord.



![Image](assets/fr/18.webp)



**Observera att även om du aktiverar "*passwordless*"-autentisering via FIDO2 på din Trezor, kommer huvudlösenordet för ditt online-konto fortfarande att vara giltigt för inloggning**



## Spara dina FIDO2-inloggningsuppgifter (invånare med inloggningsuppgifter)



Om du använder FIDO2 eller U2F för tvåfaktorsautentisering, dvs. för att logga in på konton som kräver ett lösenord utöver 2FA-validering via din Trezor, kommer Mnemonic-frasen ensam att hämta åtkomst till dina nycklar. Men om du använder FIDO2 i "*lösenordslöst*" läge som beskrivs i föregående avsnitt, kommer det att vara nödvändigt att göra en kopia av dina FIDO-uppgifter utöver att säkerhetskopiera din Mnemonic-fras som krypterar dessa uppgifter.



För att göra detta behöver du en dator med Python installerat. Öppna en terminal och kör följande kommando för att installera den nödvändiga Trezor-programvaran:



```shell
pip3 install --upgrade trezor
```



Anslut din Trezor till datorn via USB och lås upp den med hjälp av din PIN-kod.



![Image](assets/fr/01.webp)



För att hämta listan över FIDO2-identifierare som lagrats på Trezor, kör följande kommando:



```shell
trezorctl fido credentials list
```



Bekräfta exporten på din Trezor.



![Image](assets/fr/19.webp)



Din FIDO2-inloggningsinformation kommer att visas på din terminal. Till exempel, för mitt Bitwarden-konto fick jag den här informationen:



```shell
WebAuthn credential at index 0:
Relying party ID:       vault.bitwarden.com
Relying party name:     Bitwarden
User ID:                6e315ebabc8b6945a253b1c50116538d
User name:              tutoplanbnetwork@proton.me
User display name:      PBN
Creation time:          2
hmac-secret enabled:    True
Use signature counter:  True
Algorithm:              ES256 (ECDSA w/ SHA-256)
Curve:                  P-256 (secp256r1)
Credential ID:          f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Kopiera och spara all denna information i en textfil. Det finns ingen betydande risk förknippad med denna säkerhetskopia, förutom att avslöja att du använder dessa tjänster med FIDO2. "*Credential ID*" krypteras med hjälp av din Wallet:s seed, vilket innebär att en angripare som får tag på den här säkerhetskopian inte skulle kunna ansluta till dina konton, utan bara märka att du använder dessa konton. För att dekryptera dessa ID:n behöver du seed i din Wallet.



Du kan därför skapa flera kopior av denna textfil och lagra dem på olika ställen, t.ex. lokalt på din dator, på en filhostingtjänst och på externa medier som t.ex. ett USB-minne. Tänk dock på att den här säkerhetskopian inte uppdateras automatiskt, så du måste förnya den varje gång du upprättar en ny "*passwordless*"-anslutning till din Trezor.



Låt oss nu föreställa oss att du har sönder din Trezor. För att hämta dina FIDO2-referenser måste du först återställa din Wallet med hjälp av din Mnemonic-fras på en ny FIDO2-kompatibel Trezor-enhet.



När återställningen är klar kan du importera dina FIDO2-identifierare till den nya enheten genom att köra följande kommando i terminalen:



```shell
trezorctl fido credentials add <CREDENTIAL_ID>
```



Ersätt helt enkelt `<CREDENTIAL_ID>` med en av dina identifierare. I mitt fall skulle detta till exempel ge :



```shell
trezorctl fido credentials add f1d00200a020a736356d0ceb7ce8b7655b39c399d8111b620bbbbfc78a51add31475e6acd9a68f77f0a6b12a20c7a41412c488787d41e6ee0bdbf3bb99973c9637d21d3a060808143dd228e0831bbb883fb3afedd3f70596a9f6b98f00703244b76260099a9c044346bf6266d3cb9d90db6fc7cde1142b11c5c8ea
```



Din Trezor kommer att uppmana dig att importera din FIDO2 identifierare. Bekräfta genom att trycka på på skärmen.



![Image](assets/fr/20.webp)



Din FIDO2-inloggning är nu i drift på din Trezor. Upprepa denna procedur för var och en av dina identifierare.



Grattis, du har nu kommit igång med att använda din Trezor med U2F och FIDO2! Om du tyckte att den här handledningen var användbar skulle jag vara mycket tacksam om du lämnar en Green-tumme nedan. Känn dig fri att dela denna handledning på dina sociala nätverk. Tack så mycket!



Jag skulle också rekommendera den här andra handledningen, där vi tittar på en annan lösning för U2F- och FIDO2-autentisering:



https://planb.network/tutorials/computer-security/authentication/security-key-61438267-74db-4f1a-87e4-97c8e673533e