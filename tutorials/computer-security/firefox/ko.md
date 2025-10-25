---
name: Firefox
description: 개인 정보를 보호하도록 Firefox를 구성하는 방법은 무엇인가요?
---

![cover](assets/cover.webp)



## 소개



우리는 모두 온라인에서 몇 시간 동안 시간을 보내지만, 브라우저에서 자신에 대한 정보가 수집되고 있다는 사실을 깨닫지 못하는 경우가 많습니다. 우리가 클릭하고 검색하고 방문하는 모든 사이트는 방대한 개인 데이터 수집 산업에 먹이를 제공합니다.



![Statistiques navigateurs 2024](assets/fr/01.webp)


*웹 브라우저 시장 점유율: Chrome이 시장의 65%를 점유하고 있으며 Safari와 Edge가 그 뒤를 잇고 있습니다. 출처: [gs.statcounter.com](https://gs.statcounter.com/browser-market-share)*



이 그래프에서 볼 수 있듯이 Google 크롬은 전 세계 사용량의 65% 이상을 차지하며 압도적인 우위를 점하고 있습니다. 이러한 헤게모니는 대부분의 인터넷 사용자가 타겟 광고를 비즈니스 모델로 하는 Google에 자신의 검색 데이터를 맡긴다는 것을 의미합니다. 시장의 3%에 불과한 Firefox는 사용자 데이터 활용에 상업적 이해관계가 없는 비영리 단체인 Mozilla가 개발한 대안입니다.



하지만 Firefox를 선택하는 것은 첫 번째 단계일 뿐입니다. 기본적으로 Firefox도 보호 기능을 최대화하기 위해 조정이 필요합니다. 이 가이드는 가장 간단한 방법부터 가장 고급 방법까지 단계별로 안내하여 쾌적한 브라우징 환경을 유지하면서 Firefox를 진정한 추적 방지 방패로 전환할 수 있도록 도와드립니다.



### 왜 파이어폭스인가?





- 무료 오픈 소스**(Gecko 엔진): 감사 가능하고 투명한 코드
- 비영리 단체**: Mozilla 재단, 일반 관심사 미션
- 기본 제공 보호 기능**: 향상된 추적 보호(ETP), 전체 쿠키 보호(TCP), 상태 파티셔닝, HTTPS 전용 모드, DoH(DNS over HTTPS)
- 고급 사용자 지정**: Chrome과 달리 Firefox에서는 동작을 심층적으로 수정할 수 있습니다



### 시작하기 전 중요한 원칙





- 만능 레시피는 없습니다**: 더 많이 수정할수록 눈에 띄게 될 위험이 커집니다(핑거프린팅). 목표는 눈에 띄지 않으면서도 더 잘 보호받는 것입니다.
- 단계별 진행**: 설정을 변경하고 평소 사용하던 사이트를 테스트한 후 계속 진행하세요. 한 번에 모든 것을 변경할 필요는 없습니다.
- 개인 균형**: 개인 정보 보호와 사용 편의성 사이에서 나만의 타협점을 찾아보세요.



## 빠른 설치



![Téléchargement Firefox](assets/fr/02.webp)



**공식 다운로드: ** [firefox.com/browsers/desktop](https://www.firefox.com/en-US/browsers/desktop/)으로 이동합니다. 이 페이지에서 운영 체제(Windows, macOS, Linux)를 선택하여 구체적인 설치 지침이 있는 해당 다운로드 페이지에 액세스합니다.





- Windows**: '.exe' 설치 프로그램을 다운로드하고 더블클릭한 후 설치 마법사를 따릅니다
- macOS**: '.dmg' 파일을 다운로드하여 열고 Firefox를 응용 프로그램 폴더로 드래그합니다
- Linux**: 여러 옵션 사용 가능 - `.deb`/`.rpm` 패키지, Flatpak(Flathub), Snap 또는 패키지 관리자(apt, dnf, pacman)를 통해. 공식 Mozilla 소스를 선호합니다.



**팁: **설치 후 도움말 → **Firefox 정보**에서 업데이트를 확인하세요(보안 패치의 경우 중요).



![Configuration initiale Firefox](assets/fr/03.webp)


*Firefox 실행 시 첫 화면: Firefox를 기본 브라우저로 설정하고 바로가기에 추가한 다음 '저장하고 계속'*을 클릭합니다



![Création compte Firefox](assets/fr/04.webp)


*선택적 단계: Firefox 계정을 만들거나 로그인합니다. 오른쪽 하단의 '지금 안 함'을 클릭하면 이 단계를 건너뛸 수 있습니다*



![Page d'accueil Firefox](assets/fr/05.webp)


*구성이 완료된 Firefox 홈 화면. 오른쪽 상단의 ☰ 메뉴에서 설정 및 확장 프로그램*에 액세스하여 Firefox를 사용자 지정할 수 있습니다



## 기본적으로 이미 활성화된 보호 기능(안심)





- 사이트 격리(Fission)**: 점진적으로 배포 중입니다. 이 기능은 각 사이트를 별도의 프로세스에서 실행하여 하나의 악성 탭이 다른 탭의 데이터에 액세스하지 못하도록 합니다. 'about:support'를 통해 상태를 확인하세요("Fission" 검색). 활성화되어 있지 않은 경우 `about:config`에서 `fission.autostart = true`를 사용하여 수동으로 활성화할 수 있습니다.
- 전체 쿠키 보호(TCP)**: 기본적으로 활성화되어 있습니다. 쿠키 및 기타 저장소는 퍼스트 파티 사이트(사이트당 하나의 '항아리')로 제한되어 사이트 간 추적을 무력화합니다. 필요한 경우 스토리지 액세스 API를 통해 일시적인 예외가 발생합니다(통합 로그인 버튼).
- 바운스/리디렉션 추적 방지**: Firefox는 바운스 사이트(목적지 이전에 트래커를 통해 사용자를 리디렉션하는 링크)가 남긴 쿠키를 자동으로 감지하고 정리하여 사용자가 아무런 조치를 취하지 않아도 이 추적 채널을 줄입니다.



## 레벨 1 - 필수(10분 이내)



목표: 웹을 손상시키지 않고도 개인 정보를 크게 보호합니다. 90%의 사용자 대상.



설정에 액세스하려면 오른쪽 상단의 메뉴 ☰을 클릭한 다음 **"설정"**을 클릭합니다:



![Paramètres généraux](assets/fr/07.webp)


*Firefox 설정 페이지 - "일반" 탭. 여기에서 대부분의 개인정보 보호 옵션*을 구성할 수 있습니다



**추적 보호(ETP)**




- ETP**를 **엄격**으로 전환합니다. 더 많은 트래커(사이트 간 쿠키, 핑거프린팅, 크립토마이닝, 소셜 위젯...)를 차단합니다.
- 사이트가 중단되는 경우(동영상, 로그인 버튼 등) 🛡️ 방패를 통해 해당 사이트에 대해서만 보호를 비활성화한 다음 탭을 새로 고칩니다.



다양한 ETP 보안 수준은 다음과 같습니다:




- 표준**(균형 잡힌, 최대 호환성)
  - 차단: 소셜 트래커, 사이트 간 쿠키(모든 창), 비공개 브라우징의 콘텐츠 추적, 암호화폐 채굴기, 지문 탐지기.
  - 총 쿠키 보호**(TCP) 포함: 사이트당 하나의 항아리.
- 엄격** (기밀 유지에 권장)
  - 또한 모든 창에서 콘텐츠 추적 + 알려진 지문 및 의심되는 지문을 차단합니다.
  - 일부 사이트가 중단될 수 있으므로 로컬 예외를 위해 🛡️ 쉴드를 사용하세요.
- 사용자 지정** (고급)
  - 미세 조정: 쿠키, 콘텐츠 추적, 미성년자, 지문 인식(알려진/의심되는).



![Paramètres protection contre le pistage](assets/fr/06.webp)



**쿠키 및 사이트 데이터**




- "닫을 때 쿠키 및 사이트 데이터 삭제"**를 활성화하면 재시작할 때마다 깔끔하게 다시 시작할 수 있습니다.
- 원하는 경우 필수 사이트 2~3개(이메일, 은행)에 대해 **예외**를 추가하세요.


**자동 데이터 입력, 제안 및 홈 페이지**




- 자동 입력**(아이디, 주소, 카드)을 비활성화합니다. 대신 비밀번호 관리자를 사용하세요.
- 검색**: **"검색 제안 표시"**를 비활성화합니다.
- Address 바**: **"스폰서 추천"** 및 **"문맥 추천"**을 삭제합니다.
- 홈**: **포켓** 및 **스폰서 콘텐츠**를 비활성화합니다.



![Paramètres cookies et mots de passe](assets/fr/08.webp)



**HTTPS 전용**




- 모든 창에서 **"모든 창에서만 HTTPS 모드"**를 활성화합니다.


![Configuration DNS over HTTPS](assets/fr/09.webp)



**텔레메트리 및 광고 측정**




- "Firefox에 의한 데이터 수집"에서 **모두 선택 취소**합니다.
- "개인정보 친화적 광고 조치"**(PPA)를 비활성화합니다.
- 세이프 브라우징**: 계속 사용(권장). Firefox는 해시 쿼리와 로컬 검사를 통해 사이트를 위협 목록에서 확인하여 개인 정보에 미치는 영향을 최소화하면서 피싱 및 멀웨어로부터 보호합니다.



**글로벌 개인정보 관리(선택 사항)**




- 데이터 판매/공유 거부를 알리려면 **GPC**를 활성화하세요.



**검색 엔진**




- 덕덕고**, **스타트페이지**, **퀀트** 또는 **브레이브 검색**으로 전환합니다(설정 → 검색).



![Configuration moteur de recherche DuckDuckGo](assets/fr/11.webp)



**개인 탐색**




- 일회성 세션(선물, 보조 계정...)을 위한 비공개 창(Ctrl/Cmd+Shift+P). '항상 비공개' 모드는 피하세요. 확장 프로그램이 비활성 상태일 수 있으며 쿠키 예외의 유용성이 떨어질 수 있습니다.



**필수 확장 프로그램** (공식 카탈로그에서 설치)




- uBlock Origin**: 광고 및 현재 위치 추적을 차단하며 가볍습니다.
- 프라이버시 오소리**: 나를 팔로우하는 것을 차단하는 방법을 학습하고 추적 금지/GPC를 보냅니다.
- ClearURLs**(선택 사항): Firefox(ETP Strict)와 uBO는 이미 많은 부분을 정리하고 있으므로 여전히 "더러운" URL(utm, fbclid)이 표시되는 경우 이 옵션을 유지하세요.
- Firefox 다중 계정 컨테이너**: **컨테이너당 쿠키/세션 및 저장소 분리, 병렬 다중 계정, 사이트 간 추적 감소**. 공식 확장자: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.



![Extension Multi-Account Containers](assets/fr/12.webp)



**비밀번호 및 2FA**




- 전용 비밀번호 관리자(Bitwarden, KeePassXC)를 사용하세요. **브라우저에 비밀번호를 저장하지 마세요. **가능하면 2단계 인증**을 활성화합니다.



## 레벨 2 - 강화(구획화 및 네트워크)



목표: 활동을 구분하고 네트워크 누출을 줄입니다.



**DNS over HTTPS(DoH)**




- 기본 상태**: 일부 지역(미국, 캐나다, 러시아, 우크라이나)에서는 자동으로 활성화됩니다. 그 외 지역에서는 수동 활성화가 필요합니다.
- 구성**: 설정 → 일반 → 네트워크 설정 → **DoH 활성화** → **클라우드플레어** 또는 **Quad9** → **최대 보호**.
- 최대 보호 = **TRR 전용**(시스템 DNS로의 폴백 없음). 회사/호텔 네트워크가 차단되는 경우 **표준**으로 다시 전환하거나 DoH를 비활성화하세요.
- 중복성**: 자체 보안 DNS가 있는 신뢰할 수 있는 VPN을 이미 사용 중인 경우, DoH가 중복될 수 있습니다.
- 확인 테스트**: `https://www.dnsleaktest.com/`에는 선택한 DoH 공급자만 표시되어야 합니다.



![Sélection fournisseur DNS Cloudflare](assets/fr/10.webp)



**컨테이너 및 프로필을 통한 구획화**




- 다중 계정 컨테이너**: 스페이스(개인, 업무, 금융, 소셜 네트워크, 쇼핑, 일회용)를 만들 수 있습니다. 반복 사이트에 대해 **"이 컨테이너에서 항상 열기"**를 구성합니다. 공식 확장명: `https://addons.mozilla.org/fr/firefox/addon/multi-account-containers/`.
- 왜 사용하나요?
- 공간별로 쿠키/세션/저장소를 강력하게 격리**합니다.
- 교차 사이트 추적 감소**: 거대 기업(Facebook, Google)을 제한합니다.
- 동일한 서비스에서 동시 다중 계정**을 사용할 수 있습니다.
- 세그먼트화된 ID 간의 CSRF/XSS 위험이 적습니다.
  - 팁: 최소한 소셜 네트워크/구글, 업무, 금융 전용 컨테이너를 사용하세요.
- Facebook 컨테이너**(선택 사항): FB/인스타그램 전용으로 간소화된 버전입니다.
- 별도의 프로필**: 'about:프로필'을 통해(기본 프로필, 최소 '초보안' 프로필, 테스트 프로필). 전체 데이터 및 확장 프로그램 구획화.



**고급 확장 기능**(예약 예정)




- 쿠키 자동 삭제**: 탭을 닫는 즉시 사이트의 쿠키를 삭제합니다(Firefox가 장시간 열려 있는 경우 유용).
- LocalCDN**: 현재 라이브러리를 로컬에서 제공합니다(Google/Microsoft에 대한 호출 감소). 부분 호환성.



**모바일(안드로이드)**




- Firefox Android + uBlock Origin**: 이동 중에도 유사한 보호 기능을 제공합니다.



## 레벨 3 - 전문가(about:config & Arkenfox)



목표: 허용된 타협을 통한 고급 경화. 별도의 프로필**에서 권장됩니다.



다음 두 가지 방법 중 하나만 선택하세요:



**접근 방식 A - 수동 수정**: 약:설정`을 통한 몇 가지 대상 조정(더 간단하고 정밀한 제어)


**접근 방식 B - Arkenfox user.js**: 완전 자동화된 구성(더 복잡하고 최대한의 보호)



➡️ **아르켄폭스는 이미 아래에 언급된 모든 about:config 변경 사항을 포함하고 있습니다** + 수백 가지가 더 있습니다. Arkenfox를 선택하는 경우 about:config 섹션을 무시하세요.



### 접근 방법 A: about:config를 통한 수동 수정



Address 표시줄에 'about:config'를 입력합니다 → 위험 수락.



![Avertissement about:config](assets/fr/13.webp)



![Interface about:config](assets/fr/14.webp)



![Préférences about:config](assets/fr/15.webp)





- 지문 인식에 대한 내성 (토르 브라우저에서 상속됨)


```text
privacy.resistFingerprinting = true
```


효과: UTC 표준 시간대, **레터박스**(표준 창 크기), 표준화된 사용자 에이전트/정책, 캔버스/웹GL/오디오 컨텍스트 제한. 더 균일하지만 몇 가지 '특이점'(오프셋 시간, 때때로 약간의 영어)이 있습니다.





- WebRTC 비활성화(IP 유출 방지, 웹 가시성 중단)


```text
media.peerconnection.enabled = false
```





- 리퍼러 플러스 호환(기본값)


```text
network.http.referer.XOriginPolicy = 1
network.http.referer.trimOnCrossOrigin = true
```


엄격한 옵션(결제/SSO를 중단할 수 있음):


```text
network.http.referer.XOriginPolicy = 2
```





- 채터링 API 및 추측 제한하기


```text
dom.battery.enabled = false
device.sensors.enabled = false
beacon.enabled = false
geo.enabled = false
media.navigator.enabled = false
network.prefetch-next = false
browser.urlbar.speculativeConnect.enabled = false
network.http.speculative-parallel-limit = 0
```



황금률: 무언가가 깨지면 마지막 변경 사항으로 돌아가세요.



### 접근 방식 B: Arkenfox user.js(완전 자동화된 구성)



Arkenfox** 프로젝트는 수백 가지의 개인 정보 보호 및 보안 중심의 Firefox 환경 설정을 자동으로 적용하는 커뮤니티에서 관리하는 `user.js` 파일을 제공합니다. Firefox를 재시작하면 프로필에서 이 파일을 읽고 이러한 설정을 적용합니다.





- 요점은 무엇일까요? "여기저기 클릭"하지 않고도 **일관된 기반**에서 시작하고, 감독을 줄이고, 시간을 절약할 수 있습니다.
- 변경 내용(예시): 텔레메트리 차단, 쿠키/캐시/리퍼러/HTTPS 강화, **RFP** + 레터박싱, **웹RTC 비활성화**, DoH/TLS 조정, 채팅형 API 제한.
- 사용 시기: 10분 안에 Firefox를 강화하고 몇 가지 예외(DRM/스트리밍, 웹 비지오, SSO/결제)를 허용하고 싶은 경우.
- 장점: 빠르고, 일관성 있고, **업데이트**(ESR과 일치), 매우 잘 **문서화**(위키 + 댓글), 오버라이드를 통한 **사용자 정의 가능**.
- 제한 사항: 호환성(일부 웹 앱), 편의성(UTC, 창 크기), 알림 기능: **Tor가 아님**(네트워크 익명성 없음).



설치(**전용 프로필**에 설치하는 것이 이상적임)


1. 프로필/즐겨찾기를 저장하고 쿠키 예외가 있는 사이트를 나열하세요.


2. 'https://github.com/arkenfox/user.js'에서 `user.js`를 다운로드합니다(ESR/안정 버전).


3. 약:프로필`을 통해 프로필 폴더를 찾습니다:




   - Windows: `%APPDATA%/모질라/파이어폭스/프로필/...`
   - Linux: `~/.mozilla/firefox/...`
   - macOS: `~/라이브러리/응용 프로그램 지원/파이어폭스/프로필/...`


4. Firefox를 닫고 `user.js`를 프로필 폴더의 루트로 이동합니다.


5. 다시 시작; `about:config` 또는 오버라이드 파일을 통해 사용자 지정합니다.



업데이트




- Arkenfox 릴리스(ESR 정렬)를 따르고 `user.js`를 교체한 후 Firefox를 다시 시작하고 릴리스 노트를 읽습니다.



**오버라이드를 통한 사용자 지정**



Arkenfox는 기본적으로 의도적으로 제한적입니다. 특정 설정(스트리밍, 시각화, 특정 사이트)을 사용자의 필요에 맞게 조정하려면 `user.js`와 같은 폴더에 `user-overrides.js` 파일을 생성할 수 있습니다. 이 파일을 사용하면 기본 파일을 수정하지 않고도 특정 Arkenfox 환경설정을 "재정의"할 수 있습니다.



'user-overrides.js'를 생성하고 사용자 지정을 추가합니다:


```javascript
// DRM/streaming
user_pref("media.eme.enabled", true);

// Safe Browsing (si vous préférez le garder)
user_pref("browser.safebrowsing.phishing.enabled", true);
user_pref("browser.safebrowsing.malware.enabled", true);

// Historique moins restrictif
user_pref("places.history.expiration.max_pages", 200000);

// Synchronisation Firefox
user_pref("identity.fxaccounts.enabled", true);

// WebRTC (si visio nécessaire)
user_pref("media.peerconnection.enabled", true);

// Referer plus compatible
user_pref("network.http.referer.XOriginPolicy", 1);
user_pref("network.http.referer.trimOnCrossOrigin", true);
```



모범 사례




- 별도의 **"Arkenfox" 프로필**을 사용하고 "일반" 프로필은 편안함을 위해 유지하세요.
- 확장 프로그램을 최소화하여 공격 표면과 고유성을 제한합니다(uBlock Origin OK).
- 필요한 경우 사이트별 예외를 추가합니다(shield 🛡️, uBO, NoScript를 사용하는 경우).
- 변경할 때마다 테스트하세요: WebRTC/DNS 유출, 커버 유어 트랙, CreepJS.



## 모범 사례





- 업데이트**: Firefox 및 확장 프로그램 최신 버전.
- 연장**: 합리적이고 신뢰할 수 있으며, '의심스러운' 사용처를 주의하세요.
- 다운로드**: 주의; VirusTotal에서 민감한 파일을 테스트하세요.
- 비밀번호**: **전용 관리자**(Bitwarden, KeePassXC); **2FA** 활성화; 브라우저에 저장하지 마세요.
- 위생**: Google/Facebook을 컨테이너에 한정하고, 정기적으로 닫거나 열어 컨텍스트를 '초기화'합니다.



## 제한 사항 및 대안





- 강화된 브라우저 ≠ 네트워크 익명성: **VPN**이 없으면 사용자의 IP가 계속 표시되며, 사용하더라도 상관관계는 여전히 가능합니다.
- 너무 많이 수정하면 **독특**해질 수 있습니다. *랜덤화 도구(예: 카멜레온)를 사용하면 **차별화**할 수 있습니다. 테스트, 비교, 조정.
- 대안/보완 사항:
- 토르 브라우저: 토르를 통한 네트워크 익명성, 느림. 전체 설치 및 구성 가이드**를 참조하세요:



https://planb.network/tutorials/computer-security/communication/tor-browser-a847e83c-31ef-4439-9eac-742b255129bb



- 멀바드 브라우저: vPN과 결합된 "토르 없는 토르", 표준화된 설치 공간. 전용 튜토리얼**에서 설치 방법을 알아보세요:



https://planb.network/tutorials/computer-security/communication/mullvad-browser-a16c13d6-8bf9-4cb5-9aa0-85411a9cda0e



- 권장 조합: 일상적인 사용을 위한 Firefox(레벨 2) + VPN, 민감한 활동을 위한 토르/멀바드, 구획화를 위한 별도의 프로필.



## 결론



이 단계별 가이드를 따라 Firefox를 디지털 감시를 막는 진정한 보루로 바꾸세요. 필수 레벨 1 설정부터 고급 Arkenfox 구성까지, 모든 변경 사항은 브라우징 경험에 영향을 주지 않으면서 개인 정보 보호를 강화합니다.



**광고 추적기 차단, 쿠키 분리, IP Address 유출 무력화, 텔레메트리 비활성화 등 개인 정보 보호가 더욱 강화되었습니다. Firefox는 더 이상 단순한 브라우저가 아니라 사용자의 필요에 맞춘 디지털 저항 도구입니다.



**기밀은 절대 보장되지 않는다는 점을 기억하세요. 정기적으로 보호 기능을 테스트하고 설정을 업데이트하며 습관이 바뀌면 주저하지 말고 설정을 조정하세요. 온라인 익명성은 사용 방법만큼이나 사용 도구에 따라 달라집니다**



## 리소스



### Plan ₿ Network




- SCU 202 - 개인 디지털 보안 개선하기: 이 튜토리얼에서 다루는 디지털 보안 개념에 대해 자세히 알아보려면 다음과 같이 하세요



https://planb.network/courses/4ba0e3de-e67f-4ea1-a514-f111206810d1

### Mozilla 문서




- [강화된 추적 보호](https://support.mozilla.org/kb/enhanced-tracking-protection-firefox-desktop): 강화된 추적 보호 기능에 대한 공식 가이드
- [상태 파티셔닝](https://developer.mozilla.org/docs/Mozilla/Firefox/Privacy/State_Partitioning): 상태 파티셔닝에 대한 기술 문서
- [MDN 웹 보안](https://developer.mozilla.org/docs/Web/Security): 웹 보안에 대한 전체 참조 자료



### Arkenfox




- [위키 및 설치 가이드](https://github.com/arkenfox/user.js/wiki): 전체 Arkenfox 프로젝트 문서
- [입금 및 릴리스](https://github.com/arkenfox/user.js): User.js 파일 다운로드 및 업데이트 추적



### 가이드 및 커뮤니티




- [개인정보 보호 가이드 - 데스크톱 브라우저](https://www.privacyguides.org/en/desktop-browsers/): 브라우저 추천 및 비교
- Reddit**: 피드백 및 지원을 위한 r/firefox, r/privacy
- 개인정보 보호 가이드 포럼**: 심층적인 기술 토론



### 테스트 도구




- [커버 유어 트랙(EFF)](https://coveryourtracks.eff.org/): 디지털 지문 및 추적 방지 효과
- [DNS 누출 테스트](https://www.dnsleaktest.com/): DNS 누출 테스트 및 DoH 효율성
- [브라우저리크스](https://browserleaks.com/): 전체 테스트 제품군(WebRTC, 캔버스, 글꼴 등)
- [BadSSL](https://badssl.com/): SSL/TLS 인증서 유효성 검사 테스트
- [CreepJS](https://abrahamjuliot.github.io/creepjs/): 50개 이상의 핑거프린팅 벡터에 대한 고급 분석
- [Cloudflare DNS 테스트](https://1.1.1.1/help): Cloudflare DoH가 제대로 작동하는지 확인하기