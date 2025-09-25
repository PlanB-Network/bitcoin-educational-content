---
name: Canaan Avalon Nano 3S
description: 솔로마이닝 또는 Miner 풀링을 위해 ASIC Avalon 구성하기
---

![cover](assets/cover.webp)



이 튜토리얼에서는 가정에서 Miner를 쉽게 사용할 수 있도록 Canaan Avalon Nano 3S를 설정하는 방법을 살펴봅니다.



지금까지는 특정 작업을 수행하도록 특별히 설계된 ASIC(*응용 분야별 집적 회로*) 기계(이 경우 Bitcoin의 Miner 계산(SHA-256))는 특히 가정용으로 사용하기에 부적합했습니다. 소음과 발열로 인한 불편함, 그리고 이러한 장치의 막대한 전력을 지원하기 위해 전기 설비를 개조해야 한다는 점 때문에 대부분의 사람들이 참여하지 못했습니다.



오늘날 ASIC 기계의 주요 제조업체 중 하나인 Canaan은 비교적 조용하고 설치가 매우 쉬운(플러그 앤 플레이) 다양한 제품을 제공함으로써 가정에서 Miner을 원하는 개인용 시장을 공략하기로 결정했습니다.



이러한 장치는 **아발론 나노 3S(140W)**의 경우 보조 히터로, **아발론 미니 3**의 경우 출력 **800W**의 미니 라디에이터로 판매되고 있습니다.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7

대부분의 경우 동등한 전력의 기존 히터와의 가격 차이로 인해 재정적 이익을 얻을 수 없다는 점에 유의하세요. 무료(잉여) 또는 매우 저렴한 전기를 이용할 수 있는 경우가 아니라면 Mining의 활동으로 발생하는 사토시로 이 가격 차이를 보상할 수 없습니다.



제 생각에는 이러한 장치는 개인적인 이유로 집에서 Miner을 원하는 사람들을 위한 간단한 방법으로 간주되어야 합니다: *수능을 보지 않거나 / 솔로로 '복권'을 받거나 / Hashrate 탈중앙화 등에 참여하면서 겨울에 방을 난방하기 위해 발생하는 열을 **보너스로** 활용하는 것입니다. 그러나 적어도 대부분의 경우 (서구 국가에서는) 돈을 절약하는 방법은 아닙니다.



## 개봉 및 기능



먼저 Avalon Nano 3S 박스 안에 무엇이 들어 있는지 살펴봅시다.



![image](assets/fr/01.webp)




![image](assets/fr/02.webp)



상자를 열면 와이파이 수신기가 들어 있는 카드보드 슬리브가 들어 있는데, 나중에 살펴보겠지만 이 슬리브를 기기의 USB 포트에 꽂아야 로컬 네트워크에 연결할 수 있습니다. 또한 사용 설명서와 필요한 경우 장치를 공장 설정으로 초기화할 수 있는 금속 핀도 포함되어 있습니다.



![image](assets/fr/03.webp)




![image](assets/fr/04.webp)



모든 것이 상자에서 꺼내지면 기계 자체, 사용자 설명서, 와이파이 수신기, 앞서 언급한 금속 팁, 기기의 전원 Supply가 준비되어 있습니다. 제공된 신용 카드는 언급할 가치가 없다고 생각합니다.



![image](assets/fr/05.webp)



아래는 Nano 3S의 일반적인 기술 사양을 요약한 표입니다:



| Caractéristique                                      | Valeur                                                  |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Taux de hachage                                      | 6 Th/s +- 5%                                            |
| Consommation d'énergie                               | 140 W                                                   |
| Bruit                                                | 30 - 40 dB                                              |
| Plage de température de sortie d'air                 | 60-70°C (sous température ambiante 25°C)                |
| Exigences de température ambiante pour l'utilisation | de -5 à 30°C                                            |
| Plage d'entrée de l'appareil                         | 28V 5A continu                                          |
| Plage d'entrée de l'adaptateur                       | 110-240V AC 50/60Hz                                     |
| Taille de la machine                                 | Longueur: 205 mm /  Largeur: 115 mm / Hauteur:  58.5 mm |
| Poids de la machine                                  | 0.86 kg                                                 |

## 전원을 켜고 로컬 네트워크에 연결하기



포장을 풀고 나면 열이 순환할 수 있도록 Avalon Nano 3 S를 가능한 한 비교적 개방된 공간에 놓으세요. 그런 다음 아래 그림과 같이 소형 Wi-Fi 수신기 모듈을 삽입합니다:



![image](assets/fr/06.webp)


그런 다음 전원 Supply의 USB-C 플러그를 장치의 USB-C 포트에 꽂아 전원을 공급합니다.



![image](assets/fr/07.webp)


![image](assets/fr/08.webp)



기기가 부팅되고 Avalon Nano 로고가 화면에 표시된 후 '휴대폰' 로고와 함께 "Avalon Family 앱으로 네트워크를 구성하세요"라는 문구가 표시됩니다.



![image](assets/fr/09.webp)




![image](assets/fr/10.webp)



이렇게 하려면 모바일 애플리케이션 스토어로 이동하여 **아발론 패밀리** 애플리케이션을 검색하여 다운로드하세요.



![image](assets/fr/11.webp)


설치가 완료되면 오른쪽 상단의 '건너뛰기'를 클릭한 다음 '추가' 버튼을 클릭하고 마지막으로 '검색'을 클릭하여 엽니다. 디바이스 감지가 원활하게 이루어질 수 있도록 스마트폰에서 블루투스가 활성화되어 있는지 확인하세요.



![image](assets/fr/12.webp)


애플리케이션에서 디바이스가 감지되면 해당 디바이스를 클릭하고 '연결'을 선택합니다. 그러면 와이파이 연결 세부 정보를 입력할 수 있는 화면으로 이동합니다.


![image](assets/fr/13.webp)


장치가 로컬 네트워크에 연결되면 이제 화면이 다음과 같이 표시됩니다:



![image](assets/fr/14.webp)



아직 풀이 구성되지 않았으므로 '가상의' Hashrate와 디바이스의 시간, 날짜, 전원 및 IP Address이 표시되며, PC와 브라우저를 통해 디바이스의 Interface에 액세스하려는 경우 매우 유용합니다(자세한 내용은 나중에 설명합니다).



![image](assets/fr/15.webp)




## Mining pool에 연결



**이 부분은 공정이 완전히 동일하기 때문에 나노 3와 미니 3에 공통적으로 적용됩니다**.



"단독"을 원하든 Miner "풀"을 원하든, 우리는 Mining pool에 연결해야 합니다. 사실 우리 디바이스는 Bitcoin 네트워크에 대한 인식이 없는 Hash 제조업체에 불과합니다. 풀에 연결하면 Bitcoin 네트워크에 액세스할 수 있고 작업할 블록 템플릿을 받을 수 있습니다.



### 애플리케이션을 사용하여 Mining pool에 연결하기



Avalon Family 애플리케이션에서 아래 그림과 같이 기기를 선택합니다. 그러면 자동으로 기기의 관리자 비밀번호를 변경하라는 메시지가 표시됩니다. 변경하려면 '확인'을 클릭하고, 기본 액세스 비밀번호인 'admin'을 그대로 유지하려면 취소를 클릭합니다.


![image](assets/fr/16.webp)


그런 다음 '설정'을 선택한 다음 '풀 구성'을 선택하고 요청된 3개의 풀에 대한 매개변수를 입력합니다.


풀 #2와 #3은 둘 중 하나에 장애가 발생할 경우 백업 역할을 하므로 Miner가 무용지물이 되지 않도록 합니다. 기본적으로 Hashrate은 1번 풀을 가리키게 됩니다



저희의 경우 선택합니다:




- 1 - 공용 풀,
- 2 - CkPool,
- 3 - 바다.



![image](assets/fr/17.webp)



Mining pool에 연결하는 방법에 대한 자세한 내용은 이 튜토리얼 을 참조하세요:



https://planb.network/tutorials/mining/pool/public-pool-42b9e1b5-722d-471d-b1e3-9ca758065be1

https://planb.network/tutorials/mining/pool/ocean-pool-30c9e2c9-2364-44a1-bae0-2afbdb8b1c9c

요약하자면, 다음이 필요합니다





- 풀 Address, 일반적으로 **stratum+tcp://xxxxxx:port**.





- "작업자"의 이름은 *귀하의 Bitcoin Address*과 장치에 대해 선택한 *의사*로 구성되며, 두 개는 *점*으로 구분됩니다(예: **bc1qxxxxxxxxxxx.MonAvalonNano3S**)





- 비밀번호는 일반적으로 항상 "**x**"입니다



풀 정보를 입력했으면 '저장'을 클릭합니다.



![image](assets/fr/18.webp)


지시에 따라 장치를 다시 시작하고 Hashrate가 원하는 풀(1번)을 가리킬 때까지 몇 분간 기다립니다.



### 브라우저를 사용하여 Mining pool에 연결하기



Mining pool에 연결할 수도 있고, 더 일반적으로는 자주 사용하는 브라우저를 통해 기기의 Interface 관리 시스템에 액세스할 수도 있습니다.



이렇게 하려면 브라우저의 검색창에 아래 화면에 표시된 기기의 IP Address(예: **192.168.144.6**)을 입력합니다



![image](assets/fr/15.webp)



다음 페이지가 나타나면 Avalon Family 애플리케이션을 열고 애플리케이션에 표시된 QR 코드를 스캔하라는 메시지가 표시됩니다.



![image](assets/fr/20.webp)



애플리케이션을 열고 오른쪽 상단의 대시 3개를 클릭한 다음 스캔을 클릭합니다. 브라우저의 QR 코드를 스캔한 다음 애플리케이션의 관리자 비밀번호를 입력하고 확인을 클릭합니다.



![image](assets/fr/21.webp)



Avalon과 상호 작용할 수 있는 웹 페이지로 이동합니다. 이 페이지는 구성 수단이라기보다는 머신의 메트릭을 표시하는 대시보드에 가깝습니다.



하지만 풀 설정은 오른쪽 하단에 있는 **"풀 구성"**을 클릭하여 이 방법으로도 액세스할 수 있습니다.



![image](assets/fr/22.webp)



모바일 애플리케이션과 동일한 방식으로 여기에서 풀 매개변수를 입력할 수 있습니다.



![image](assets/fr/23.webp)



## Avalon Family 앱을 통해 디바이스 제어



이제 가정용 Miner를 로컬 네트워크에 연결하고 Hashrate를 채굴 풀로 향하게 했습니다. 이제 Avalon 패밀리 애플리케이션을 통해 머신의 필수 기능을 살펴보겠습니다.



Avalon 제품군 애플리케이션에서 Avalon Nano 3S에 해당하는 아이콘을 클릭합니다.


을 클릭하면 3개의 메뉴가 표시됩니다: "작업 모드", "조명 제어", "설정"입니다. 먼저 "작업 모드"를 클릭합니다. 그러면 머신에 대한 3가지 전원 모드가 제공됩니다.



**낮음**: 70W의 전력 소비로 약 3 Th/s의 Hashrate을 제공합니다


**중간**: 100W 전력 소비 시 약 4.5 Th/s의 Hashrate을 제공합니다


**높음**: 최대 소비 전력 140W에서 약 6 Th/s의 Hashrate을 제공합니다



![image](assets/fr/31.webp)


한 걸음 물러나서 '조명 제어' 메뉴를 살펴봅시다. 이것은 순전히 미용적인 기능입니다. 다양한 색상, 강도, 열, 야간에 기기의 LED 끄기 등 다양한 옵션을 사용할 수 있습니다. 직접 찾아보면 쉽게 알 수 있습니다.



![image](assets/fr/32.webp)


![image](assets/fr/33.webp)



![image](assets/fr/34.webp)



마지막으로 사용할 수 있는 메뉴는 Mining 풀에 연결할 때 이미 보았던 "설정" 메뉴입니다. 여기에서 풀을 관리하고, 디바이스의 관리자 비밀번호를 변경하고, 보증 만료일, 필터 청결도, 장애 발생 시 지원팀에 연락하는 방법 등 다양한 지표를 확인할 수 있습니다.



![image](assets/fr/35.webp)


유지 관리 및 필터를 최대한 깨끗하게 유지하려면 진공 청소기를 사용하고 공기 흡입구와 배출구를 정기적으로 진공 청소기로 청소하여 막힘을 방지하는 것이 좋습니다.



Avalon Nano 3 S를 로컬 네트워크에 연결하는 방법, Hashrate을 Mining 풀로 지정하는 방법, Avalon Family 애플리케이션을 사용하여 옵션 및 설정을 탐색하는 방법에 대해 알아본 이 튜토리얼의 마지막에 이르렀습니다.



자세한 내용은 아발론의 상위 버전인 미니 3에 대한 튜토리얼을 참조하세요.



https://planb.network/tutorials/mining/hardware/canaan-avalon-mini-f2185435-10a3-4d7b-b88f-f1a489babab7