---
name: Nerdminer
description: 0에 가까운 승리 확률로 Mining Bitcoin을 시작합니다
---

![cover](assets/cover.webp)

## NerdMiner v2 구성하기


이 튜토리얼에서는 Bitcoin Mining 전용 하드웨어 장치(ESP-32 S3)인 NerdMiner_v2를 설정하는 데 필요한 단계를 안내해 드립니다.

물론 이러한 장치의 컴퓨팅 성능은 아마추어 또는 전문 채굴자의 ASIC과 경쟁할 수 없습니다. 그럼에도 불구하고 NerdMiner는 Bitcoin Mining를 가시화할 수 있는 완벽한 교육 도구입니다. 운이 좋다면 블록과 그에 따른 보상을 찾을 수도 있습니다. 궁금하신 분들은 [당첨 확률 추정](#estimation-de-la-probabilite-de-gain) 섹션에서 확인하실 수 있습니다. 전력 소비량 측면에서 NerdMiner는 0.5W를 소비하며, 비교를 위해 LED 램프는 평균 20배 더 많이 소비합니다.


여러 단계를 진행하기 전에 만드는 데 필요한 장비를 나열해 보겠습니다:



- a [릴리고 T-디스플레이 S3](https://lilygo.cc/products/t-display-s3)
- a [USB-C 전원 Supply](https://amzn.eu/d/gIOot90)
- 3D 케이스: 3D 프린터가 있는 경우 [3D 파일](https://www.printables.com/model/501547-nerdminer-v2-click-case-w-buttons)을 다운로드할 수 있으며, 그렇지 않은 경우 [실렉체험 온라인 스토어](https://silexperience.company.site/NerdMiner_V2-p544379757)에서 구매할 수 있습니다.
- 크롬 브라우저가 설치된 PC
- 인터넷 연결
- gW-8 Address


다음과 같은 여러 리셀러를 통해 사전 조립된 NerdMiner 키트를 구입할 수도 있습니다:



- [데쿠브르비트코인](https://shop.decouvrebitcoin.com/products/nerd-Miner?_pos=1&_psq=nerd&_ss=e&_v=1.0)
- [비트메이커](https://bitronics.store/shop/)


먼저 ESP-32 S3에 소프트웨어를 플래시하는 방법을 살펴본 다음 재부팅하여 와이파이 네트워크를 변경하는 방법을 살펴보겠습니다. 이 단계는 Windows 사용자를 위한 것으로, Linux OS를 사용하는 경우 시스템에서 ESP-32 S3를 인식할 수 있도록 [예비 단계](#etapes-preliminaires-pour-utilisateurs-linux)를 수행하시기 바랍니다.


웹플래셔를 사용하면 **NerdMiner_v2 소프트웨어 설치**가 크게 간소화됩니다.


## 1단계: 웹플래셔 준비하기


먼저 [온라인 NM2 플래셔](https://bitmaker-hub.github.io/diyflasher/)로 이동해야 합니다.


그런 다음 ESP-32에 해당하는 펌웨어를 선택합니다. 대부분의 경우 기본 펌웨어인 T-Display S3가 사용됩니다. 그런 다음 "플래시"를 클릭합니다.


**Note⚠️ :** 기본적으로 플래시 사용과 USB 포트 액세스를 허용하므로 Chrome 브라우저를 사용하는 것이 중요합니다.


![image](assets/webflasher.webp)


## 2단계: ESP-32 연결하기


웹플래셔가 실행되면 브라우저에서 인식하는 다양한 USB 포트가 표시된 팝업 창이 열립니다.

그런 다음 ESP-32를 연결하면 새 포트가 표시됩니다(이 경우 ttyACM0 포트). 그런 다음 해당 포트를 선택하고 "연결"을 클릭해야 합니다.


![image](assets/flasher-port-serial.webp)


그러면 소프트웨어가 몇 초 만에 ESP32에 다운로드됩니다.


![image](assets/NM2-sucessfully-installed.webp)


## 3단계: NerdMiner 구성


NerdMiner의 구성은 스마트폰이나 컴퓨터를 통해 이루어집니다.

WiFi를 활성화하고 로컬 NerdMinerAP 네트워크에 연결합니다. 스마트폰을 사용하는 경우 구성 포털이 자동으로 열립니다. 그렇지 않은 경우 브라우저에 Address 192.168.4.1을 입력합니다.

그런 다음 'WiFi 구성'을 선택합니다.


이제 NerdMiner를 구성할 수 있습니다.

먼저, 네트워크 이름을 선택하고 연결된 비밀번호를 입력하여 WiFi 네트워크에 연결합니다.


그런 다음 참여하고자 하는 Mining pool을 선택할 수 있습니다. 실제로 Bitcoin Mining 업계에서는 컴퓨팅 파워를 풀링하여 Exchange에서 블록을 찾을 확률을 높이고 제공된 Hashrate에 비례하여 보상을 공유하는 것이 일반적입니다.

너드마이너의 경우, 이러한 풀 중 하나에 연결하도록 선택할 수 있습니다:


| Pool URL          | Port  | URL                        | Status                                   |
| ----------------- | ----- | -------------------------- | ---------------------------------------- |
| public-pool.io    | 21496 | https://web.public-pool.io | Default Solo and open-source mining pool |
| pool.nerdminer.io | 3333  | https://nerdminer.io       | Maintained by CHMEX                      |
| pool.vkbit.com    | 3333  | https://vkbit.com/         | Maintained by djerfy                     |

풀을 선택한 후에는 (예외적으로) 블록이 발견될 경우 보상을 받으려면 Bitcoin Address을 입력해야 합니다.


또한, 시간대를 선택하여 NerdMiner가 시간을 올바르게 표시할 수 있도록 하세요.

이제 '저장'을 클릭하면 됩니다.


![image](assets/wifi-configuration.webp)


축하합니다, 이제 Bitcoin Mining 네트워크의 일원이 되셨습니다!


## 너드마이너 운영


NerdMinerv2 소프트웨어에는 화면 오른쪽의 상단 버튼을 클릭하여 액세스할 수 있는 3개의 다른 화면이 있습니다:



- 메인 화면에서 NerdMiner의 통계에 액세스할 수 있습니다.
- 두 번째 화면에서는 시간, Hashrate, Bitcoin의 가격, 블록 높이를 확인할 수 있습니다.
- 세 번째 화면에서는 글로벌 Bitcoin Mining 네트워크에 대한 통계에 액세스할 수 있습니다.

![image](assets/NM2-screens.webp)


예를 들어 와이파이 네트워크를 변경하기 위해 NerdMiner를 재부팅하려면 상단 버튼을 5초간 눌러야 합니다.


하단 버튼을 한 번 누르면 NerdMiner가 꺼집니다. 두 번 클릭하면 화면 방향이 회전합니다.


### Linux 사용자를 위한 사전 단계


다음은 Chrome이 Linux에서 직렬 포트를 감지하는 단계입니다.


1. 연결된 포트를 식별합니다:



- ESP-32를 컴퓨터에 연결합니다.
- 터미널을 엽니다.
- 다음 명령을 입력하여 모든 포트를 나열합니다:
  - `dmesg | grep tty`
  - 또는 `ls /dev/tty*`
- 포트를 확인하려면 ESP-32를 연결하지 않은 상태에서 명령을 반복하여 제거할 수 있습니다.


2. 연결된 포트의 권한을 변경합니다:



- 기본적으로 직렬 포트에 액세스하려면 루트 권한이 필요할 수 있으므로 사용자를 `다이얼아웃` 그룹에 추가하여 사용할 수 있도록 합니다.
  - sudo usermod -a -G dialout YOUR_USERAME`에서 `YOUR_USERAME`을 사용자 아이디로 바꿉니다.
  - 를 클릭한 다음 로그아웃했다가 이 사용자로 다시 로그인하거나 시스템을 다시 시작하여 그룹 변경 사항이 적용되는지 확인합니다.


이제 ESP-32가 시스템에서 인식되었으므로 [첫 번째 단계](#etape-1-preparation-du-webflasher)로 돌아가서 소프트웨어를 설치할 수 있습니다.


## 결론


이제 끝났습니다! 이제 NerdMiner_v2가 구성되었으며 사용할 준비가 되었습니다.


Mining를 축하하며 행운이 함께하길 바랍니다!


### 당첨 확률 추정하기


Block reward 당첨 확률을 재미있게 추정해 보겠습니다. 이 추정치는 대략적인 것이며 확률의 크기 순서만 구하려고 합니다.

너드마이너가 연결할 수 있는 풀은 "단독 Mining pool"으로, 연결된 모든 마이너의 Hashrate을 상호화하지 않고 단순히 코디네이터 역할을 하는 풀입니다.

이제 NerdMiner의 Hashrate이 약 45kH/s라고 가정해 보겠습니다.


총 Hashrate가 약 450 EH/s(또는 초당 4.5 x 10^20 해시)라는 점을 감안하면 다음 블록을 찾을 확률은 1,000억 분의 1이라고 볼 수 있으며, 이는 매우 희박한 확률입니다. 따라서 너드마이너는 교육 도구이자 호기심의 대상일 뿐만 아니라, 0.5W의 한계 전기 비용으로 Bitcoin Mining의 복권 역할을 할 수 있지만, 방금 살펴본 것처럼 당첨 확률은 터무니없이 낮습니다. 하지만 행운에 도전해 보시는 건 어떨까요?


### 추가 정보


이 주제에 대해 더 자세히 알아보고 싶으시다면 다음 링크를 참조하세요:



- [NerdMiner_v2 프로젝트 페이지](http://github.com/BitMaker-hub/NerdMiner_v2)
- [너드마이너의 전체 문서](https://docs.bitwater.ch/nerd-Miner-v2/)