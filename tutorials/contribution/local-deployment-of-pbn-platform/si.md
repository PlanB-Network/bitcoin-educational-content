---
name: Plan ₿ Network පළාපලය ස්ථානීයව ක්‍රියාත්මක කිරීමේ මාර්ගෝපදේශය
description: Kako lahko zaženete Plan ₿ Network v lokalnem okolju za testiranje mojega prispevka k vsebini ali lektoriranje/pregled izobraževalne vsebine na Plan ₿ Network?
---
![github](assets/cover.webp)


## සාරාංශයෙන්


මෙම උපකාරිකාව Docker, අතේකී යතුරු, සහ අභිරුචි ගබඩා වින්‍යාසයන් භාවිතා කරමින් ඔබේ දේශීය යන්ත්‍රය මත Plan ₿ Network සිට Bitcoin ඉගෙනුම් කළමනාකරණ පද්ධතිය පිහිටුවීම සඳහා පියවරෙන් පියවර උපදෙස් ලබා දේ.


Če zgornjega dela niste razumeli, ne skrbite—ta vadnica je za vas!


---

## **Bitcoin ඉගෙනුම් කළමනාකරණ පද්ධතිය ස්ථානීයව ක්‍රියාත්මක කිරීමේ ආකාරය**


මෙම උපකාරකය වේදිකාව පිහිටුවීම, අතුරු යතුරු කළමනාකරණය කිරීම, සහ ගබඩා අභිරුචිකරණය කිරීම සඳහා විස්තරාත්මක පියවර ලබා දේ. සාමාන්‍ය ගැටළු වලට මුහුණ නොදීමට සහ ඔබේ දේශීය පරිසරය නිවැරදිව වින්‍යාස කිරීම සඳහා පහත පියවර අනුගමනය කරන්න.



**1. අවශ්‍යතා**


- Linux යන්ත්‍රයක් Docker සහ Docker Compose ස්ථාපිත කර ඇත (මෙය Windows මතද ක්‍රියාත්මක වන බව වාර්තා වී ඇත).
- ප්‍රමාණවත් `nodejs` අනුවාදය (පරීක්ෂා කරන ලදී: 22.12.0)
- `pnpm` ඔබේ පද්ධතියට ස්ථාපනය කර ඇත.
- Git රිපොසිටරීස් පිටපත් කිරීම සඳහා වින්‍යාස කර ඇත.



**2. රිපොසිටරිය අනුපිටපත් කරන්න**

රෙපොසිටරිය ඔබේ දේශීය යන්ත්‍රයට පිටපත් කරන්න:


git clone [https://github.com/PlanB-Network/Bitcoin-learning-management-system](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd)

[cd](https://github.com/PlanB-Network/Bitcoin-learning-management-system￼cd) Bitcoin-learning-management-system


```bash
git clone https://github.com/PlanB-Network/bitcoin-learning-management-system
cd bitcoin-learning-management-system
```



**3. පරිසර විචල්‍ය සකසන්න**


1\. `.env.example` ෆයිල් එක පිටපත් කරන්න:


```bash
cp .env.example .env
```


1. `.env` ගොනුව සංස්කරණය කරන්න, නමෙන් .example කොටස මකන්න, දැන් ඔබට අවශ්‍ය විචල්‍ය සඳහා අනුමාන යතුරු ඇතුළත් කළ යුතුය. උදාහරණයක්:


⚠️ To je obvezen korak, njegovo preskakovanje bo povzročilo napake, kot je zavrnitev povezave med nekaterimi zabojniki.


ඔබගේ කැපවූ Github PAT ද 해당 파일යට එකතු කිරීමට අමතක නොකරන්න.



```markdown
# Dummy Keys for External Services
SBP_API_KEY=dummyApiKey
SBP_HMAC_SECRET=dummyHmacSecret
STRIPE_SECRET=sk_test_dummySecretKey12345
STRIPE_ENDPOINT_SECRET=dummyEndpointSecret12345
SENDGRID_KEY=dummySendgridKey
```


---

**4. අවශ්‍යතා ස්ථාපනය කරන්න**


`Be sure` ඔබට සුදුසු nodejs අනුවාදයක් ස්ථාපිත කර ඇති බව. 2024-12 වන විට, v22.12.0 (LTS) ක්‍රියාත්මක වන බව පරීක්ෂා කර ඇත.



⚠️ Ubuntu 22.04 ගබඩාවේ nodejs සංස්කරණය 12.22.9 වේ: pnpm ස්ථාපනය කිරීමට ඉඩ දීමට ඉතා පැරණි ය.



nodejs ස්ථාපනය කිරීමට, උපදෙස් [මෙතනින්](https://nodejs.org/en/download/package-manager) සොයන්න; උදාහරණයක් ලෙස ඔබට `nvm` ස්ථාපන ක්‍රමය භාවිතා කිරීමට තෝරා ගත හැක.


---

අවශ්‍ය පැකේජ සවි කිරීමේ pnpm ආරම්භ කිරීමට පෙර, සියලුම අනුයෝජිතා ස්ථාපනය කර ඇති බවට විශ්වාසවන්ත වන්න, ඔබට පහත විධානය ක්‍රියාත්මක කිරීමෙන් මෙය සාර්ථක කර ගත හැක:


```bash
sudo apt install libcairo2-dev libjpeg-dev libpango1.0-dev libgif-dev build-essential g++ libpixman-1-dev
```


---

`../Bitcoin-learning-management-system/` ෆෝල්ඩරය ඇතුළත, `pnpm` ස්ථාපනය කිරීමට පහත විධානය ක්‍රියාත්මක කරන්න.


```bash
pnpm install
```


__සටහන:__ ඔබේ අනුයෝජිතතා සහ pnpm යාවත්කාලීන කිරීමට කාලයෙන් කාලයට යාවත්කාලීන කිරීමට මතක තබා ගන්න.



**5. कन्टेनरहरू चलाउनुहोस्**

`../Bitcoin-learning-management-system/` ෆෝල්ඩරය තුළ, Docker සමඟ සංවර්ධන පරිසරය ආරම්භ කරන්න:


```bash
docker compose up --build -V
```

ඔබ මෙම ඊළඟ විධානය මෙහෙමත් ක්‍රියාත්මක කළහොත්, ඔබේ ටර්මිනල් එකේ ලොග්ස් නොපෙනේවි.

```bash
docker compose up -d --build -V
```


මෙය ඩොකර් වලින් අවශ්‍ය සියලුම කන්ටේනර් ගොඩනඟා ආරම්භ කරනු ඇත.


**6. යෙදුමට ප්‍රවේශ වන්න**

කන්ටේනර් ක්‍රියාත්මක වන විට, ඉදිරිපස අන්තර්ගතය ප්‍රවේශ වන්න:

\[<http://localhost:8181](http://localhost:8181)>


![Plan ₿ Network Local](assets/en/1.webp)


සටහන: ඔබ මූලාශ්‍ර ගොනු වෙනස් කළහොත් යෙදුම ස්වයංක්‍රීයව නැවත පූරණය වනු ඇත.



**7.** ඔබේ දත්ත සමුදාය Schema පිහිටුවන්න


පළමු වතාවට ක්‍රියාත්මක කිරීමේදී, ඔබ DB මයිග්‍රේෂන් ක්‍රියාත්මක කළ යුතුය.


Za to izvedbo zaženite skripto za migracijo: `pnpm run dev:db:migrate`


```markdown
pnpm run dev:db:migrate
```


**8. භණ්ඩාගාරයෙන් දත්ත ආයාත කරන්න**

දත්ත ගබඩාවට දත්ත ආයාත කිරීමට, API වෙත ඉල්ලීමක් කරන්න:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


**9. සින්ක් වොලුම් ප්‍රවේශ ගැටළු නිවැරදි කරන්න**

ඔබ `cdn` සහ `sync` පරිමාවන් සමඟ ප්‍රවේශ ගැටළු වලට මුහුණ දෙනවා නම්, ධාවනය කරන්න:


```markdown
docker exec --user=root bitcoin-learning-management-system-api-1 chmod 777 /tmp/{sync,cdn}
```


ඉතින් නැවත:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


![Plan ₿ Network Local](assets/en/2.webp)



**10. ගබඩාව අභිරුචිකරණය කරන්න (විකල්ප)**

Če morate uporabiti Fork ali določeno podružnico:

1. `.env` ගොනුව සංස්කරණය කර පහත විචල්‍යයන් යාවත්කාලීන කරන්න:


```markdown
DATA_REPOSITORY_URL=https://github.com/<your-username>/bitcoin-educational-content.git
DATA_REPOSITORY_BRANCH=<your-branch>
PRIVATE_DATA_REPOSITORY_URL=https://github.com/<your-username>/planB-premium-content.git
PRIVATE_DATA_REPOSITORY_BRANCH=<your-branch>
```


2\. Docker නැවත ආරම්භ කරන්න:


```markdown
docker compose down -v
docker compose up --build -V
```


3\. සංග්‍රහ දත්ත නැවත සමුද්‍රය කරන්න:


```markdown
curl -X POST http://localhost:3000/api/github/sync
```


මෙම උපකාරකය, මකා දැමූ යතුරු, අවශ්‍යතා ස්ථාපිත කර ඇති, සහ ගබඩා අවශ්‍ය ලෙස අභිරුචිකරණය කර ඇති පරිදි වේදිකාව නිවැරදිව පිහිටුවා ඇති බව සහතික කරයි. 🎉 ඔබේ පිහිටුවීම සඳහා සුභ පැතුම්!


**අමතර උපකාර සඳහා විධාන**


සියලුම කන්ටේනර් නවතා දමන්න


```
docker compose down
```


සියලුම පවතින කන්ටේනර් සහ පරිමාවන් කපා හරිනු.


```
docker container prune -f
docker volume prune --all
```


කන්ටේනර් නැවත සෑදීමට නිල මාර්ගෝපදේශයේ භාවිතා කරන එකම විධානය සහ සින්ක් ස්ක්‍රිප්ට් ආරම්භ කරන්න:


```
docker-compose up --build -V
curl -X POST http://localhost:3000/api/github/sync
```