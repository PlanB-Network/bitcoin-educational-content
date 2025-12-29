---
name: Lightning Smoke Machine
description: ESP32를 통해 라이트닝 결제로 연기 기계를 트리거합니다.
---

![cover-lightning-smoke-machine](assets/cover.webp)



## 소개



기존 연기 기계를 Lightning Network을 통해 Bitcoin로 결제할 수 있는 장치로 변환합니다. 결제할 때마다 자동으로 연기가 분사됩니다!





- 레벨: 중급
- 예상 시간: 2~3시간
- 사용 사례 Bitcoin 이벤트, 예술 공연, 라이트닝 데모, 자동화된 무대 효과



## 전제 조건



### 지식





 - 기본 전자 장치(배선, 릴레이)
 - 용접(또는 듀폰 커넥터 사용)
 - 네트워크 구성(WiFi, 웹소켓)



### 필요한 계정





- BTCPay 서버: 기능적 인스턴스(자체 호스팅 또는 호스팅)
- Blink Wallet : 계정 + 액세스 API



### 액세스





- BTCPay 서버에 대한 관리자 액세스
- ESP32용 Wi-Fi 연결



## 필요한 자료



### 하드웨어 - 전자 부품





- 마이크로컨트롤러 1개 - ESP32-WROOM-32


*ESP32-WROOM-32는 전자 장치를 인터넷에 연결하고 원격으로 제어하기 위한 컴팩트한 저비용 WiFi/블루투스 마이크로 컨트롤러입니다*



![ESP32](assets/fr/1.webp)





- 1 릴레이 모듈 - 5V, 옵토커플러 포함


*릴레이는 ESP32가 작동하여 연기 기계를 켜거나 끌 수 있는 스위치와 같습니다*



![relay](assets/fr/2.webp)





- ~듀폰 케이블 최대 10개 - 수/수 및 수/암 케이블



![dupont-cables](assets/fr/3.webp)





- 1 ESP32용 전원 공급 장치 - 5V USB 또는 리튬 폴리머 배터리



![battery](assets/fr/4.webp)





- 마이크로 USB 케이블 1개 - ESP32와 전원 공급 장치 연결



![micro-usb-cables](assets/fr/5.webp)





- 12V 배터리 리모컨이 있는 220V 포그 머신 1개



![remote-and-smoke-machine](assets/fr/6.webp)





- 스모크 머신과 호환되는 액상 1병



### 하드웨어 - 도구





- 납땜 인두 + 주석(납땜하는 경우)
- 스크루 드라이버
- 멀티미터(권장)



### 소프트웨어





- 펌웨어 비트코인스위치 : **[https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)**
- WebSerial 호환 웹 브라우저(Chrome/Edge/Brave)
- BTCPay 서버 구성. BTCPay 서버 인스턴스 생성에 대한 자세한 내용은 이 튜토리얼(https://planb.academy/fr/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc)을 참조하세요



## 시스템 아키텍처



![architecture-lightning-smoke-machine](assets/fr/7.webp)



---


**⚠️** **안전 경고 - 계속하기 전에 읽어보세요** **⚠️**



이 프로젝트에는 **220V 주전원**에 연결된 포그 머신이 포함됩니다. 부적절하게 작동하면 **감전사** 또는 **화재**가 발생할 수 있습니다.



**협상 불가 규칙:**



1. **리모컨을 열거나 배선을 건드리기 전에 항상 연기 기기를 전원에서 분리하세요**


2. **취급하기 전에 리모컨에서 배터리를 분리**하세요(합선 및 부품 손상 위험)


3. **다시 연결하기 전에 모든 연결이 격리되어 있는지** 확인하세요


4. **리모컨 박스를 닫고 고정하기 전에는 절대로 220V**를 다시 연결하지 마세요



이런 종류의 취급에 익숙하지 않다면 경험이 있는 사람을 대동하세요.



---

## 파트 1: 하드웨어 조립



### 1단계: 리모컨 준비하기



목표: 리모컨의 ON/OFF 버튼에 릴레이를 연결합니다


1. 리모컨 열기




    - 식별 켜기/끄기 버튼
    - 케이스의 나사를 풀어 리모컨을 엽니다


2. 연결 찾기




 - 의 + 및 - 단자를 찾습니다
 - 멀티미터로 연속성 테스트(선택 사항)



![smoke-machine-remote](assets/fr/8.webp)



3. 버튼 배선(납땜 또는 커넥터)




    - 버튼의 - 단자에 검은색 케이블을 납땜합니다
    - 빨간색 케이블을 공통 + 단자에 납땜합니다



![smoke-machine-remote](assets/fr/9.webp)



### 2단계: 릴레이 모듈에 연결하기



**알림: 릴레이 용어



| **Terminal**         | **Description**           | **Fonction**                        |
| -------------------- | ------------------------- | ----------------------------------- |
| NO (Normally Open)   | Circuit ouvert par défaut | Se ferme quand le relais est activé |
| NC (Normally Closed) | Circuit fermé par défaut  | S'ouvre quand le relais est activé  |
| COM (Common)         | Terminal central          | Bascule entre NO et NC              |

**리모컨에서 릴레이 모듈까지 배선:**




- 켜기/끄기 버튼의 검은색 전선 **→** NO(상시 개방)
- 빨간색 와이어(공통) **→** COM(공통)



**논리:**


ESP32가 릴레이를 활성화하면 리모컨 버튼을 누르는 것과 똑같이 COM과 NO를 연결합니다.


ESP32가 릴레이를 차단하면 COM과 NO가 분리되며, 이는 버튼에서 손을 뗀 것과 동일합니다.



![remote-relay](assets/fr/10.webp)



### 3단계: ESP32를 릴레이 모듈에 연결하기



**배선도:**



| **ESP32** | **→** | **Module relais** |
| --------- | ----- | ----------------- |
| V5 (5V)   | **→** | VCC               |
| GND       | **→** | GND               |
| GPIO 21   | **→** | IN (Input)        |

**인증: **




- VCC 및 GND 잘 연결됨(극성)
- 제어 신호에 사용되는 GPIO 21
- 눈에 보이는 단락 없음



![relay-esp32](assets/fr/11.webp)



**체크포인트 하드웨어**


소프트웨어로 전환하기 전에 을 확인하세요:




- 올바르게 연결된 리모컨
- ESP32에 연결된 릴레이 모듈
- 다른 구성 요소에 노출된 전선이 닿지 않음
- 220V 항상 연결 해제



![relay-esp32](assets/fr/12.webp)





---


## 파트 2: 소프트웨어 구성



여기서는 *Blink*을 예로 들었지만, 다른 옵션을 선호하는 경우 *BTCPay 서버*는 *Strike, Breez 및 Boltz*도 제공합니다.



### 1단계: 플러그인, 설치 *비트코인스위치* + *Blink



1 - 관리자 계정으로 *BTCPay 서버* 인스턴스로 이동합니다



2 - 첫 번째 블라인드 만들기



3 - *BTCPay 서버*의 왼쪽에서 하단으로 스크롤하여 *"플러그인 관리"*로 이동합니다



![btcpay-plugins](assets/fr/13.webp)



4 - *비트코인스위치* 플러그인과 *Blink*을 설치합니다



![btcpay-plugins](assets/fr/14.webp)



5 - 플러그인 목록을 아래로 스크롤하여 *"설치"*를 클릭합니다: *비트코인스위치 및 Blink*(또는 선택 가능한 wallet)을 선택합니다



![btcpay-plugins](assets/fr/15.webp)



6 - 설치가 완료되면 *BTCPay 서버*를 다시 시작하고 인스턴스가 다시 시작될 때까지 1분간 기다립니다



![btcpay-plugins](assets/fr/16.webp)



7 - *"플러그인 관리"*로 돌아가면 두 플러그인이 모두 설치되었는지 확인합니다



![btcpay-plugins](assets/fr/17.webp)



### 2단계: 백엔드: *BTCPay 서버 + Blink* 구성



**1 - wallet *Blink*** 생성




- Https://www.blink.sv 방문하기
- 계정을 만듭니다. 튜토리얼을 참조하세요:



[https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd](https://planb.academy/en/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd)



**2 - API 키 생성 *Blink***




- API 인터페이스에 접속합니다: **[https://www.blink.sv/en/api](https://www.blink.sv/en/api)**에서 wallet *Blink*을 만들 때 사용한 것과 동일한 계정으로 로그인합니다



![blink-api](assets/fr/18.webp)





   - 연결되면 *API 키* 탭으로 이동합니다



![blink-api](assets/fr/19.webp)





   - ""를 클릭합니다 + "*"를 클릭하여 API 키 구성에 액세스합니다



![blink-api](assets/fr/20.webp)





   - API 키에 이름을 지정하고 기본 설정을 그대로 둡니다. 그런 다음 세 번째 단계에서 API 키에 `blink_mZ5KxxxxxxxxxxxNbmX`라는 한 번만 표시되는 메모를 작성합니다



![blink-api](assets/fr/21.webp)





   - 생성되면 활성 API 키 목록에 표시됩니다.



![blink-api](assets/fr/22.webp)



**3 - *Blink*을 *BTCPay 서버***에 연결합니다




- BTCPay 서버*를 엽니다
- 로 이동합니다: *Wallet* **→** *라이트닝*



![btcpay-server](assets/fr/23.webp)





- 사용자 지정 노드 사용*을 클릭합니다
- 다음 연결 문자열을 붙여넣습니다:



```
type=blink;server=https://api.blink.sv/graphql;api-key=blink_mZ5KxxxxxxxxNbmX;wallet-id=0a3fc465-082xxxxxxxxxx-2545595d856f
```



**⚠️** **중요** :




- 앞부분은 수정하지 마세요: 유형=블링크;서버=https://api.blink.sv/graphql`;
- 교체만 :
    - api-key= *API Blink* 키에 의해
    - wallet-id= *wallet Blink* ID 기준
- 그런 다음 *연결 테스트*를 클릭한 다음 *저장*을 클릭합니다



![btcpay-server](assets/fr/24.webp)





 - 연결이 설정되었는지 확인합니다(녹색 상태)



![btcpay-server](assets/fr/25.webp)



**4 - 판매 시점(PoS) 생성**




- BTCPay 서버에서 *플러그인* 탭으로 이동하여 *판매 시점*을 클릭합니다



![btcpay-server](assets/fr/26.webp)





- PoS의 이름을 지정하고 *생성*을 클릭합니다



![btcpay-server](assets/fr/27.webp)





- PoS 구성 :
    - POS 스타일 선택 = *인쇄 디스플레이*
    - 통화 = *SATS*
    - 저장*을 클릭합니다



![btcpay-server](assets/fr/28.webp)





- 제품 구성 :
    - 모든 기본 제품 삭제
    - 그런 다음 *항목 추가*를 클릭합니다



![btcpay-server](assets/fr/29.webp)



![btcpay-server](assets/fr/30.webp)





- 제품을 구성합니다:
    - 제목 : *연기 기계*
    - 가격 : *10 sats*
    - Bitcoin GPIO 스위치 : 21
    - Bitcoin 스위치 지속 시간(밀리초) : 5000
    - 닫기*를 클릭한 다음 *저장*을 클릭하여 새 제품을 저장합니다



![btcpay-server](assets/fr/31.webp)



### 3단계: 펌웨어: ESP32 플래싱하기



**1 - 플래시 사이트로 이동




- 로 이동합니다: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)



![bitcoinswitch-lnbits](assets/fr/32.webp)



**2 - Flash 비트코인스위치 펌웨어**




- USB/Micro-USB 케이블로 ESP32를 컴퓨터에 연결합니다
- 그런 다음 *장치에 연결*을 클릭합니다
- 창이 열리면 ESP32의 USB 포트를 선택한 다음 *연결*을 클릭합니다



![bitcoinswitch-lnbits](assets/fr/33.webp)





- ESP32가 연결되면 비트코인스위치 펌웨어를 플래시합니다. T-디스플레이* 섹션에서 *펌웨어 업로드*를 클릭하여 사용 가능한 최신 버전을 확인합니다(현재: *비트코인스위치 T-디스플레이 v1.0.1*)



![bitcoinswitch-lnbits](assets/fr/34.webp)





- 업로드가 완료될 때까지 기다렸다가 로그에 *"종료 중..."이라고 표시되면 프로세스가 완료된 것입니다. "*


![bitcoinswitch-lnbits](assets/fr/35.webp)





- ESP32의 플러그를 뽑습니다



**3 - 비트코인스위치 펌웨어 설치 확인




- 페이지 새로고침: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- USB/Micro-USB 케이블을 사용하여 ESP32를 컴퓨터에 다시 연결합니다
- 그런 다음 *장치에 연결하기를 클릭합니다
- ESP32에서 USB 포트를 선택한 다음 위에서 설명한 대로 *연결*을 클릭합니다
- 연결이 완료되면 ESP32의 **RESET** 버튼을 누릅니다
- 마지막 줄에 표시되는 로그를 확인합니다:



```
Welcome to BitcoinSwitch! (v1.0.1)
Config file does not exist.
Entering config mode. until we receive /config-done.
```



(이는 정상이며, 아직 구성이 없지만 펌웨어가 설치되었음을 의미합니다.)



![bitcoinswitch-lnbits](assets/fr/36.webp)



**4 - 웹소켓 LNURL** URL 생성



예상 최종 형식 :



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```



생성 단계 :




- BTCPay 서버 인스턴스를 연 다음 나중에 생성한 PoS로 이동합니다.
- 그런 다음 '보기'를 클릭하여 브라우저에서 PoS를 엽니다



![btcpay-server-https](assets/fr/37.webp)





- 페이지의 URL을 복사합니다(예: :



![btcpay-server-https](assets/fr/38.webp)



이 URL의 포장을 풀어보겠습니다:



```
https://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos
```





- `XXXXv` → BTCPay 서버 인스턴스의 도메인
- '46XXXXXXXXXXXXXXXXXXXXwFB` → 귀하의 PoS 고유 식별자
- pOS` → 판매 시점을 나타냅니다



변형하세요:




- Https://`를 `wss://`로 바꿉니다
- 끝에 `/bitcoinswitch`를 추가합니다



결과:



```
wss://XXXXv/apps/46XXXXXXXXXXXXXXXXXXXXwFB/pos/bitcoinswitch
```



향후 구성을 위해 이 URL을 보관해두면 ESP32가 BTCPay 서버와 실시간으로 통신할 수 있습니다. 웹소켓 프로토콜(`wss://`)은 둘 사이에 영구적인 연결을 설정합니다. PoS에서 라이트닝 결제가 확인되는 즉시 BTCPay는 해당 정보를 ESP32로 전송하고, 그러면 스모크 머신이 작동할 수 있습니다.



**5 - WiFi 및 웹소켓 구성하기




- 페이지로 돌아가기 eSP32가 연결된 상태에서 [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- 장치 구성* → *와이파이 설정*으로 이동합니다



알리다 :




- WiFi SSID: WiFi 네트워크 이름
- WiFi 비밀번호: WiFi 비밀번호



![bitcoinswitch-lnbits](assets/fr/39.webp)





- LNbits 디바이스 URL* 섹션에 이전 단계에서 생성한 웹소켓 URL을 붙여넣습니다
- 구성 업로드*를 클릭합니다



![bitcoinswitch-lnbits](assets/fr/40.webp)





- 업로드가 완료될 때까지 기다리면 로그에 방금 입력한 매개변수(SSID, 비밀번호 및 웹소켓 URL)가 표시됩니다



![bitcoinswitch-lnbits](assets/fr/41.webp)





- ESP32가 웹소켓 연결을 설정하는 동안 기다립니다. 가 표시되어야 합니다:



```
WiFi connection established!

[WebSocket] Connected to url: ...
```



![bitcoinswitch-lnbits](assets/fr/42.webp)





- 이제 ESP32의 연결을 해제할 수 있습니다



---
## 체크포인트 소프트웨어



최종 테스트 전에 을 확인하세요:





- BTCPay에 연결된 Blink
- 최소 1개 이상의 아이템으로 생성된 PoS
- 비트코인스위치로 플래시된 ESP32
- ESP32에 Wi-Fi 구성
- 웹소켓 URL이 올바릅니다
- 오류 없는 ESP32 로그



---

## 테스트 및 디버깅



### 최종 테스트 완료



1. 연기 기계(220V)에 플러그를 꽂고 전원을 켭니다


2. ESP32 전원 공급(배터리 또는 USB)


3. 브라우저에서 BTCPay PoS를 엽니다


4. "연기 기계" 항목 스캔


5. wallet 라이트닝(Blink 또는 기타 wallet)으로 결제하기


6. 관찰하세요:




 - 릴레이 클릭(소리 및 릴레이 LED 점등)
 - 연기 기계가 활성화되었습니다
 - 연기 발생!



### 공정성 문제 및 해결 방법



| **Problème**                        | **Cause probable**              | **Solution**                                                                                 |
| ----------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------------- |
| ESP32 ne se connecte pas            | Driver USB manquant             | Installer [CH340 drivers](https://learn.sparkfun.com/tutorials/how-to-install-ch340-drivers) |
| Relais ne clique pas                | Mauvais câblage GPIO            | Vérifier GPIO 21 → IN                                                                        |
| Smoke machine ne réagit pas         | Télécommande mal câblée         | Vérifier NO/NC/COM                                                                           |
| WebSocket timeout                   | URL incorrecte                  | Vérifier wss:// et /bitcoinswitch                                                            |
| WiFi ne se connecte pas             | SSID/Password erroné            | Re-flasher la config WiFi                                                                    |
| Paiement reçu mais rien ne se passe | ESP32 non connecté au WebSocket | Vérifier les logs RESET                                                                      |

## 리소스



### 유용한 링크





- 비트코인스위치 펌웨어: [https://bitcoinswitch.lnbits.com/](https://bitcoinswitch.lnbits.com/)
- BTCPay 서버 문서 : [https://docs.btcpayserver.org/](https://docs.btcpayserver.org/)
- Blink API : [https://dev.blink.sv/](https://dev.blink.sv/)
- ESP32 핀아웃 : [https://randomnerdtutorials.com/esp32-pinout-reference-gpios/](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)



### 커뮤니티 및 지원





- BTCPay 서버** : [chat.btcpayserver.org](https://chat.btcpayserver.org/) - 공식 사항
- BTCPay 서버 Telegram** : [t.me/btcpayserver](https://t.me/btcpayserver)
- LNbits** : [t.me/lnbits](https://t.me/lnbits) - 공식 Telegram, 활발한 커뮤니티
- 비트코인스위치(펌웨어 버그)**: [github.com/lnbits/bitcoinswitch/issues](https://github.com/lnbits/bitcoinswitch/issues)



### 소스 코드





- 비트코인스위치 펌웨어 소스 코드: [https://github.com/lnbits/bitcoinswitch](https://github.com/lnbits/bitcoinswitch)



---

**⚡** sats을 쌓고, 연기를 만들고, 즐기고, 겸손을 유지하세요! **⚡**