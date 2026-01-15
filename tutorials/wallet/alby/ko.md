---
name: Alby

description: Bitcoin 및 Lightning Network용 브라우저 확장 프로그램
---

![cover](assets/cover.webp)




비트코인으로 점점 더 간편하게 결제하는 것은 이 분야의 많은 기업이 직면한 과제입니다. Alby는 브라우저용 Alby wallet 확장 프로그램을 통해 이러한 문제를 해결하고 있습니다. 이 확장 프로그램은 주소를 자동으로 감지하고 마찰 없는 비트코인 결제를 가능하게 하는 유동적인 프레임워크를 설정하는 것을 목표로 합니다. 이 튜토리얼에서는 Alby 확장 프로그램을 살펴보고 브라우저에서 결제가 어떻게 원활하게 이루어지는지 테스트해봅니다.




![video](https://youtu.be/nd5fX2vHuDw)




## Alby 확장



Alby 확장 프로그램은 웹 브라우저가 Bitcoin 네트워크 및 해당 Lightning Network 계층과 쉽고 안전하게 상호 작용할 수 있게 해주는 도구입니다. 세 가지 측면이 특징입니다:




- Lightning Network wallet: Alby 노드 또는 계정을 연결하여 Lightning Network 계층을 통해 빠르고 저렴하게 비트코인을 주고받을 수 있습니다.
- 웹을 통한 유동적 결제: 라이트닝을 지원하는 웹사이트에서 비트코인 결제를 위해 QR 코드를 스캔하거나 애플리케이션 간에 전환할 필요가 없습니다. 한 번의 클릭으로 또는 예산을 설정한 경우 확인 없이도 원활하게 거래할 수 있습니다.
- Nostr 관리자: 이 확장 프로그램은 Nostr 키를 관리하여 모든 플랫폼에 개인 키를 노출하지 않고도 보안 서명자 역할을 하는 Nostr 애플리케이션에 쉽게 연결하고 상호 작용할 수 있도록 합니다.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## 확장 프로그램에 연결



이 튜토리얼에서는 Ubuntu 운영 체제에서 Firefox 브라우저의 Alby 확장 프로그램을 사용하겠습니다. 그러나 Windows 및 Chrome과 같은 브라우저에서도 사용할 수 있습니다.



Firefox] 확장 프로그램 스토어(https://addons.mozilla.org/fr/firefox/addon/alby/) 또는 [Chrome] 확장 프로그램 스토어(https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe)를 방문하여 브라우저에 Alby 확장 프로그램을 추가할 수 있습니다.



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ 확장 프로그램의 작성자가 실제로 Alby 공식 계정인지 확인하여 비트코인의 불법 복제나 도난을 방지하는 것이 중요합니다.



오른쪽 버튼을 클릭하여 브라우저에 확장 프로그램을 추가하세요.


확장 프로그램을 설치하고 사용하는 데 필요한 권한을 부여한 다음 확장 프로그램을 도구 모음에 고정하여 쉽게 검색할 수 있도록 합니다.



![pin](assets/fr/03.webp)



또한 잠금 해제 코드(매우 중요)를 정의해야 브라우저에서 Lightning wallet에 대한 안전한 액세스를 보장할 수 있습니다. 강력한 영숫자 비밀번호를 설정하는 것이 좋습니다.



ℹ️ 이 비밀번호는 변경은 가능하지만 검색은 불가능하므로 잊어버렸을 때 액세스할 수 있도록 안전한 곳에 저장해 두세요.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby은 두 가지 선택지를 제공함으로써 적응력을 입증합니다:




- 비트코인을 계속 관리하면서 애플리케이션을 즐기고 싶으시다면 Alby 계정을 계속 사용하세요.
- 확장 프로그램에서 이미 지원되는 wallet 또는 라이트닝 노드가 있는 경우 자체 wallet 또는 라이트닝 노드를 연결하세요.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


이 튜토리얼에서는 Alby 에코시스템의 기능을 활용하기 위해 Alby 계정을 계속 사용하기로 합니다.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Alby 계정에 로그인하거나 아직 계정이 없는 경우 계정을 만드세요.



![signup](assets/fr/05.webp)



## 첫 결제하기



로그인한 후 도구 모음에서 Alby 확장자를 클릭하면 포트폴리오에 액세스할 수 있습니다.



![buzzin](assets/fr/06.webp)



Alby 계정을 생성한 후에는 사토시를 사용하려면 wallet에 연결해야 합니다. 비트코인 wallet을 Alby 계정에 연결하려면 컴퓨터에 설정하거나 Alby에서 제공하는 요금제에 가입할 수 있는 Alby Hub 노드를 사용하는 것이 좋습니다.



![hubplan](assets/fr/13.webp)




이 튜토리얼에서는 Alby 계정을 컴퓨터에 로컬로 설치하여 지원합니다.


Alby 노드를 직접 구축하려면 Alby Hub 튜토리얼을 권장합니다.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

이 노드를 사용하면 자체 관리형 라이트닝 포트폴리오를 생성하고 라이트닝 채널을 효율적으로 관리하여 사토시를 주고받을 수 있습니다.



![channels](assets/fr/14.webp)



수신할 수 있는 총 사토시 수를 정의하는 수신 채널을 엽니다.



![receivechanal](assets/fr/15.webp)



비트코인 온체인 주소에서 사토시를 차단하여 송금 채널을 열 수 있습니다. 차단한 사토시에 따라 사용할 수 있는 총 사토시가 결정됩니다.



![spend](assets/fr/16.webp)



이제 Alby 확장 프로그램을 통해 사토시를 주고받을 수 있습니다.



![exchange](assets/fr/08.webp)



이 시점부터 Alby 확장 프로그램은 사용자가 방문하는 웹 페이지에서 사용 가능한 라이트닝 주소와 송장을 감지하여 확장 프로그램에서 직접 비트코인 또는 라이트닝으로 결제할 것을 제안합니다.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## 마스터 키로 복구 키 보호



Alby 확장 프로그램에서 제공하는 마스터 키는 기본 Bitcoin 네트워크 레이어(온체인)인 Nostr 시스템과 안전하게 통신할 수 있는 보호 오버레이 역할을 하며, Nostr 애플리케이션과 라이트닝 연결을 활성화할 수 있게 해줍니다.



![masterKey](assets/fr/11.webp)



이 마스터 키는 복구 문구와 유사한 12개의 단어 형태로 되어 있습니다. 따라서 언제든지 액세스할 수 있도록 안전한 방법을 사용하여 저장하는 것이 좋습니다.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



이제 Alby 확장을 통해 마찰 없는 비트코인 및 라이트닝 결제를 경험할 수 있습니다. 이 튜토리얼이 재미있으셨다면 Alby Hub 튜토리얼을 통해 나만의 Alby 노드를 설정하고 부드럽고 강력한 인터페이스에서 Alby 지갑의 모든 측면을 제어해 보시기 바랍니다.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a