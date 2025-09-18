---
name: Bitaxe
description: BitAxe를 설정하는 방법은 무엇인가요?
---
![video](https://youtu.be/tvLSK8v0MK8)


### 소개


BitAxe는 Skot에서 만든 오픈 소스 프로젝트로, 비용 효율적인 Mining 실험을 할 수 있는 [GitHub에서 사용 가능](https://github.com/skot/bitaxe)입니다.


이 칩은 ASIC 시장의 선두주자인 Bitmain의 유명한 Antminer S19의 작동 방식을 리버스 엔지니어링하여 Bitcoin Mining에 특화된 기계입니다. 이제 새로운 오픈소스 프로젝트에서 이 강력한 칩을 사용할 수 있습니다. 너드마이너와 달리 비트액스는 Mining pool에 연결할 수 있는 충분한 컴퓨팅 파워를 갖추고 있어 정기적으로 사토시를 획득할 수 있습니다. 반면, 너드마이너는 복권처럼 작동하는 솔로풀에만 연결할 수 있으며, 전체 Block reward에 당첨될 확률은 희박합니다.


BitAxe에는 다양한 칩과 성능을 갖춘 여러 버전이 있습니다:


| Bitaxe Model Series      | ASIC Chip | Used On                     | Expected Hash Rate          | Ideal For                                                                                                  |
| ------------------------ | --------- | --------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Bitaxe Max (Series 100)  | 1 x BM1397| Antminer Series 17          | 400 GH/s (up to 450 GH/s)   | Bitcoin mining beginners, offering a solid hash rate with moderate power consumption.                      |
| Bitaxe Ultra (Series 200)| 1 x BM1366| Antminer S19 XP and S19k Pro| 500 GH/s (up to 550 GH/s)   | Serious miners aiming to balance efficiency and higher hash rate.                                          |
| Bitaxe Hex (Series 300)  | 6 x BM1366| Antminer S19k Pro and S19 XP| 3.0 TH/s (up to 3.3 TH/s)   | Miners seeking scalability and high performance without sacrificing efficiency.                             |
| Bitaxe Supra (Series 400)| 1 x BM1368| Antminer S21                | 600 GH/s (up to 700 GH/s)   | Serious enthusiasts seeking the highest hash rates and efficiency.                                         |

이 튜토리얼에서는 Antminer S19XP에 사용되는 BM1366 칩이 장착된 BitAxe Ultra 204를 사용하겠습니다. 이 제품은 소매점에서 이미 조립 및 플래싱된 제품입니다.


### [소매업체 목록은 이 페이지에서 확인할 수 있습니다](https://bitaxe.org/legit.html)


![signup](assets/2.webp)


일반적으로 전원 Supply가 함께 판매됩니다. 그렇지 않은 경우 5V 잭 케이블과 4A 이상의 전원 Supply를 구매해야 합니다.


![signup](assets/1.webp)


### 구성

BitAxe를 처음 연결하면 기본적으로 Wi-Fi 네트워크에 연결을 시도합니다. 다섯 번 시도하면 자체 Wi-Fi 네트워크의 이름이 표시되므로 해당 네트워크에 연결하여 구성할 수 있습니다.

이를 위해 모든 컴퓨터 또는 스마트폰을 사용할 수 있습니다. Wi-Fi 설정으로 이동하여 새 네트워크를 검색하면 Bitaxe_XXXX라는 Wi-Fi가 표시됩니다. 여기서는 'Bitaxe_A859'입니다. 이 Wi-Fi 네트워크에 연결하면 자동으로 창이 열립니다.


![signup](assets/3.webp)


이 창에서 왼쪽 상단에 있는 3개의 작은 가로 막대를 클릭한 다음 '설정'을 클릭합니다.


![signup](assets/4.webp)


자동 검색 시스템이 없으므로 Wi-Fi 네트워크 정보를 수동으로 입력해야 합니다.


![signup](assets/5.webp)


따라서 Wi-Fi의 SSID, 즉 네트워크 이름, 비밀번호 및 선택한 Mining pool의 정보를 표시하세요. 여기에서는 풀의 URL이 같은 방식으로 표시되지 않으니 주의하세요. 예를 들어, Braiins의 경우 제공된 풀 URL은 'stratum+tcp://eu.stratum.braiins.com:3333'입니다.


![signup](assets/6.webp)


화면에서 볼 수 있듯이 `stratum+tcp://`와 `:3333` 부분을 제거하고 `eu.stratum.braiins.com`만 남겨야 합니다. 그런 다음 `Port` 필드에 풀에서 제공한 URL 끝의 4자리 숫자를 입력하되 `:`를 빼고 입력합니다. 따라서 여기서는 `3333`입니다.


이 튜토리얼에서는 Braiins Mining pool을 사용하지만 다른 것을 자유롭게 선택하실 수 있습니다. Mining 풀에 대한 튜토리얼은 [PlanB 네트워크 웹사이트](https://planb.network/en/tutorials/Mining)에서 확인할 수 있습니다.


다음으로 `사용자`에 식별자를 입력한 다음 `비밀번호`를 입력합니다(일반적으로 `"x"` 또는 `"Anything123"`).


코어 전압` 설정은 기본적으로 `1200`으로 두어야 하며, `주파수`도 처음에는 기본값을 그대로 둡니다. 나중에 더 많은 컴퓨팅 성능을 얻기 위해 이 설정을 조정할 수 있습니다. 단, 비트액스는 과열 시 성능을 저하시키는 시스템이 없기 때문에 칩의 온도가 65~70°C를 넘지 않도록 하는 것이 중요합니다. 온도가 65°C를 너무 많이 초과하면 BitAxe가 손상될 수 있습니다.


![signup](assets/7.webp)


모든 설정을 올바르게 입력했으면 하단의 '저장' 버튼을 클릭한 다음 BitAxe를 분리했다가 다시 연결하기만 하면 다시 시작할 수 있습니다.

정보를 올바르게 입력했다면 기기가 Wi-Fi에 빠르게 연결되고 Mining pool에 연결되며 작은 화면에 일부 정보가 표시되기 시작합니다. Mining pool의 대시보드에 표시되는 데는 몇 분 정도 걸릴 수 있습니다.

### 대시보드 및 화면


세 개의 다른 디스플레이가 스크롤됩니다. 세 번째 페이지에는 대시보드에 연결할 수 있는 IP Address인 `IP` 정보가 표시됩니다. 여기서 Address은 `192.168.1.19`입니다.


![signup](assets/8.webp) ![signup](assets/9.webp) ![signup](assets/10.webp)


대시보드에 액세스하려면 인터넷 브라우저에 Address을 입력하기만 하면 됩니다.


대시보드에서 작은 화면에 표시되는 모든 정보를 확인할 수 있으며, 이제 자세히 살펴보겠습니다.


![signup](assets/11.webp)


| BitAxe Screen | Dashboard                                   | Description                                                                                                                                                                                                               |
| ------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gh            | Hashrate                                    | The current computing power, expressed in GigaHash/s                                                                                                                                                                      |
| W/THs         | Efficiency                                  | This is the efficiency of your BitAxe expressed in W/THs. It's the ratio between the electrical power consumed and the computing power produced.                                                                          |
| A/R           | Shares                                      | Quantity of `Shares` sent by your BitAxe to the pool, representing the amount of work provided.                                                                                                                          |
| UT            | Uptime                                      | Time since your BitAxe has been operating without interruption (available in the left menu under `Logs`).                                                                                                                |
| BD            | Best Difficulty                             | Maximum difficulty reached since the last restart. For comparison, the current network difficulty is about 85T.                                                                                                          |
| FAN           | FAN in the `Heat` box                       | Fan rotation speed, expressed in rotations per minute.                                                                                                                                                                    |
| Temp          | ASIC temperature in the `Heat` box          | Chip temperature, which should not exceed 65°C.                                                                                                                                                                           |
| Pwr           | Power                                       | Power in watts consumed. However, this information does not take into account the screen, the fan, or the power supply. For example, when it displays 11.7W, the total consumption is actually 15.8W.                    |
| mV mA         | Input Voltage Input Current                 | Voltage and current consumed by the machine. The power in watts is equal to the voltage multiplied by the current.                                                                                                        |
| FH            | Free Heap Memory (left menu -> `Logs`)      | The available memory.                                                                                                                                                                                                     |
| vCore         | ASIC Voltage (in the Performance box)       | Voltage measured on the ASIC chip.                                                                                                                                                                                        |
| IP            | NA                                          | IP Address.                                                                                                                                                                                                               |
| V2.1.0       | Version (left menu -> `Logs`)               | Firmware version.                                                                                                                                                                                                         |

Wi-Fi 또는 풀 설정은 언제든지 문제없이 변경할 수 있습니다.

환기 및 실내 온도에 따라 온도가 65°C를 넘지 않도록 성능을 높이거나 낮춰야 할 수도 있습니다. 성능을 높이면 더 많은 사토시를 획득할 수 있지만 BitAxe는 더 많은 전기를 소비하게 됩니다!