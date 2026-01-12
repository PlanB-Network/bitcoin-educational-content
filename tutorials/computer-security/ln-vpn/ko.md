---
name: LN VPN

description: 익명 및 온디맨드 VPN을 위해 Lightning으로 LN VPN을 설정하세요
---

![image](assets/cover.webp)


LN VPN은 라이트닝 결제만 허용하는 맞춤형 VPN 서비스입니다. 오늘은 인터넷 검색 시 흔적을 남기지 않고 사용하는 방법을 보여드리겠습니다.


많은 우수한 VPN 서비스 제공 업체가 있으며, 이 기사(하이퍼링크)에서 포괄적인 리뷰를 수행했습니다. 하지만 LN VPN이 눈에 띄어 소개할 기회를 놓칠 수 없었습니다.


ProtonVPN 및 Mullvad와 같은 대부분의 VPN 서비스 제공 업체는 비트코인으로 결제하는 옵션을 제공하지만 계정을 생성하고 장기 또는 단기 요금제를 구매해야 하므로 모든 사용자의 예산에 맞지 않을 수 있습니다.


LN VPN은 Lightning Network를 통해 Bitcoin 결제를 구현하여 1시간이라는 짧은 시간 동안 온디맨드 VPN을 사용할 수 있습니다. 즉각적이고 익명의 라이트닝 결제는 소액 결제의 가능성을 열어줍니다.


참고💡: **이 가이드는 Linux Ubuntu 22.04 LTS 시스템에서 LN VPN을 사용하는 방법을 설명합니다**


## 전제 조건: 와이어가드


간단히 말해서, Wireguard는 컴퓨터와 인터넷을 브라우징할 원격 서버 사이에 보안 터널을 만드는 데 사용됩니다. 이 가이드를 따라 Contract로 임대하는 기간 동안 이 서버의 IP Address가 사용자 소유로 표시됩니다.


공식 와이어가드 설치 가이드: https://www.wireguard.com/install/


```
Wireguard installation
$ sudo apt-get update
$ sudo apt install wireguard
```


## 전제 조건: 라이트닝 Bitcoin Wallet


아직 Lightning Bitcoin Wallet이 없더라도 걱정하지 마세요. 여기에 아주 간단한 가이드가 준비되어 있으니 참고하세요. (LN 튜토리얼 섹션에서 도움을 받으실 수 있습니다)


## 1단계: Contract 임대


Https://lnvpn.com 에서 VPN 터널의 출구 IP 국가와 기간을 선택해야 합니다. 이러한 매개변수가 설정되면 번개로 결제를 클릭합니다.


![image](assets/1.webp)


라이트닝 Invoice이 표시되며, 라이트닝 Wallet로 스캔하기만 하면 됩니다.


Invoice 결제가 완료되면 Wireguard 구성 설정이 생성될 때까지 몇 초에서 최대 2분까지 기다려야 합니다. 시간이 조금 더 걸리더라도 당황하지 마세요. 이 절차를 수십 번 수행했으며 때로는 시간이 조금 더 걸릴 수도 있습니다.

다음 텍스트는 원본 텍스트와 동일한 마크다운 레이아웃을 유지하면서 영어로 번역되었습니다:


다음 화면이 나타나면 '파일로 다운로드'를 클릭하기만 하면 구성 파일을 받을 수 있으며, 이 파일의 이름은 lnvpn-xx-xx.conf와 비슷하며 여기서 'xx'는 현재 날짜에 해당합니다.

![image](assets/2.webp)


## 2단계: 터널 활성화


먼저, 이전 단계에서 얻은 구성 파일의 이름을 변경하여 Wireguard에서 자동으로 인식할 수 있도록 해야 합니다.


터미널 창이나 파일 탐색기를 통해 다운로드 폴더로 이동하여 다음과 같이 lnvpn-xx-xx.conf 파일의 이름을 wg0.conf로 변경합니다:


```
$ sudo ln -s usrbin/resolvectl usrlocal/bin/resolvconf
$ sudo wg-quick up ~/Downloads/wg0.conf
```


이제 됐어요! 터널이 활성화되었습니다!


## 3단계: 확인


Whatismyip과 같은 온라인 서비스를 사용하여 방금 활성화한 VPN의 공인 IP Address가 현재 사용 중인지 확인하세요.


## 4단계: 비활성화


임대가 만료되면 인터넷에 다시 액세스하려면 연결을 비활성화해야 합니다. 그런 다음 LN VPN으로 임대를 설정하고 싶을 때마다 1~3단계를 반복하면 됩니다.


터널을 비활성화합니다:


```
$ sudo ip link delete dev wg0
```


이제 끝났습니다! 이제 독특한 VPN 서비스인 LN VPN을 사용하는 방법을 알게 되었습니다!