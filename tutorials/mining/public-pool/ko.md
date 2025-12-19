---
name: Public Pool
description: 공용 풀 소개
---

![signup](assets/cover.webp)


**공개 풀**은 단순한 풀이 아니라 **솔로 풀**이라고도 합니다. Miner가 Mining 블록에서 성공하면 풀의 다른 참여자나 풀 자체와 공유되지 않는 전체 Block reward을 수집하게 됩니다.


*퍼블릭 풀**은 **Miner에 **블록 템플릿**만 제공하므로 **Bitcoin 노드**와 Miner와 통신하는 소프트웨어가 없어도 작업을 수행할 수 있습니다. 여러분의 컴퓨팅 파워를 다른 참여자들의 컴퓨팅 파워와 합치는 것이 아니기 때문에, 블록을 성공적으로 Mining할 확률은 매우 낮으며, 이는 복권 시스템과 비슷하게 가끔 운이 좋은 개인이 잭팟을 터뜨리는 것과 비슷합니다.


![signup](assets/1.webp)


공개 풀**의 **대시보드**에는 풀의 **총 Hashrate**와 같은 통계와 풀에 연결된 다양한 유형의 채굴자 분포도 확인할 수 있습니다.


![signup](assets/2.webp)


처음 몇 줄에서, 총 649TH/s를 위해 1323개의 **Bitaxe**가 연결된 **Bitaxe**를 볼 수 있습니다. **Bitaxe**는 **오픈 소스** 프로젝트로, **오픈 소스** 전자 보드에서 **Antminer S19**와 같은 **ASIC**의 칩을 간단히 재사용하여 15W의 0.5TH/s의 초소형 Miner을 만들 수 있게 해줍니다. 이 튜토리얼에서 예제로 사용할 Miner입니다.


## 작업자** 추가하기 👷‍♂️


![signup](assets/cover.webp)


페이지 상단에서 Address **stratum+tcp://public-pool.io:21496** 풀을 복사할 수 있습니다.


다음으로 **사용자** 필드에 소유하고 있는 **Bitcoin** Address을 입력합니다.


채굴자가 여러 명인 경우, 모든 채굴자에 대해 동일한 Address를 입력하면 해당 채굴자의 **해시레이트**가 합쳐져 하나의 Miner로 표시되도록 할 수 있습니다. 또한 각각에 고유한 이름을 추가하여 구분할 수도 있습니다. 이렇게 하려면 **Bitcoin** Address 뒤에 **.workername**을 추가하기만 하면 됩니다.


마지막으로 **비밀번호** 필드에 **'x'**를 입력합니다.


예시: 예를 들어 **Bitcoin** Address이 **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'**이고 Miner의 이름을 **"Brrrr"**로 지정하려는 경우 Miner의 Interface에 다음 정보를 입력하면 됩니다:



- URL**: stratum+tcp://public-pool.io:21496
- USER**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- 비밀번호**: **'x'**

Miner가 **비택스**인 경우 필드는 약간 다르지만 정보는 동일하게 유지됩니다:


- URL**: public-pool.io (여기서는 포트 필드에 보고되는 **'stratum+tcp://'** 앞부분과 **':21496'** 끝부분을 제거해야 합니다.)
- Port**: 21496
- User**: **‘bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv.Brrrr’**
- 비밀번호**: **'x'**


![signup](assets/3.webp)


Mining을 시작하고 몇 분 후에 **퍼블릭 풀** 웹사이트에서 Address을 검색하여 데이터를 확인할 수 있습니다.


## 대시보드


![signup](assets/4.webp)


퍼블릭 풀**에 연결되면 **사용자** 입력란에 입력한 **Bitcoin** Address로 검색하여 **대시보드**에 접속할 수 있습니다. 여기서는 **'bc1q2ed8zxq8njqsznkp7gj84n0xwl9dp224uha2fv'**입니다.


대시보드**에는 데이터와 네트워크에 대한 다양한 정보가 표시됩니다.


![signup](assets/5.webp)


네트워크 Hash 요금**은 **Bitcoin** 네트워크의 총 작동 전력에 해당하는 요금입니다.


네트워크 난이도**는 블록을 검증하기 위해 도달해야 하는 난이도를 나타냅니다.


그리고 **최고 난이도**는 여러분이 도달한 가장 높은 난이도입니다. 우연히 🍀 네트워크 난이도에 도달하면, 100블록 후에 Block reward... 전체를 획득하게 됩니다. 블록을 사용하기 전에 100블록을 기다려야 합니다.


또한 **블록 높이**는 마지막으로 채굴된 블록의 수와 무게로 표시되는 WU로, 최대값은 4,000,000입니다.


아래에서 **사용자** 필드에 **Bitcoin** Address 뒤에 **.name**을 추가하여 고유한 이름을 지정한 경우 각 디바이스의 모든 통계를 개별적으로 확인할 수 있습니다.