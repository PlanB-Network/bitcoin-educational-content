---
name: Misty Breez
description: 활이 없는 라이트닝 Wallet.
---

![misty-breez-cover](assets/cover.webp)



![video](https://youtu.be/mibKrTvtlyQ)


미스티 브리즈는 소프트웨어 개발 키트와 블록스트림이 개발한 **Liquid** 네트워크를 기반으로 브리즈에서 개발한 라이트닝 자체 보유 Wallet입니다.


이는 라이트닝 노드 없이 운영할 수 있는 완전히 새로운 접근 방식으로, Bitcoin 네트워크 간 전송에서 잠재적인 **게임 체인저**가 될 수 있습니다.


이 튜토리얼에서는 Wallet의 작동 방식과 전체 개요를 설명합니다.



## 미스티 브리즈는 어떻게 작동하나요?



미스티 브리즈는 백엔드로서 라이트닝 노드가 없는 구현입니다. Breez SDK와 Liquid를 기반으로 개발되었습니다.



Liquid은 Bitcoin 네트워크에 병렬로 연결된 Layer로, 속도와 거래 비용이 크게 개선되었습니다. 이 Layer을 통해 미스티 브리즈는 라이트닝 노드를 사용하지 않고 대신 **볼츠**와 같은 타사 Exchange 서비스를 사용하여 Liquid Network과 Lightning Network 간의 상호 운용성을 보장할 수 있습니다. 서두르지 마세요. 나중에 다시 설명하겠습니다.



지금은 미스티 브리즈 Wallet로 모험을 시작해 보겠습니다.



## 미스티 브리즈 시작하기



미스티 브리즈 모바일 앱은 구글 플레이 스토어(Android) 및 애플 스토어(iOS) 등의 공식 다운로드 플랫폼에서 다운로드할 수 있습니다. 공식 [미스티 브리즈] 웹사이트(https://breez.technology/misty/)에서도 해당 앱으로 이동할 수 있습니다.



⚠️ 미스티 브리즈와 브리즈 Wallet을 혼동하지 마세요.



⚠️ **중요**: 비트코인의 보안을 위해 공식 플랫폼에서 애플리케이션을 다운로드하여 진위 여부를 확인해야 합니다.



![download-misty-breez](assets/fr/01.webp)



이 튜토리얼에서는 Android 디바이스에서 시작하겠습니다. 하지만 이 섹션에서 설명하는 각 단계와 특정 기능은 iOS에도 적용됩니다.



설치 시 미스티 브리즈는 새 Wallet를 만들거나 복구 단어가 있는 이전 Lightning Wallet를 복원할 수 있는 옵션을 제공합니다.


이 튜토리얼에서는 새 Wallet를 만들기로 선택합니다.



⚠️Misty Breez는 현재 개발 단계에 있으므로 합리적인 금액으로 시작하는 것이 좋습니다.



![create-wallet](assets/fr/02.webp)


### 복구 단어를 저장합니다 :


새 Wallet을 만들 때 가장 먼저 해야 할 일 중 하나는 12개의 복구 단어를 백업하는 것입니다.


다음은 백업 문구를 백업하는 방법에 대한 몇 가지 팁입니다.



https://planb.network/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

문구를 백업하려면 **환경설정 > 보안** 메뉴를 선택한 다음 **백업 문구 확인** 옵션을 선택합니다.



![backup](assets/fr/03.webp)


보안을 강화하기 위해 **PIN 코드**를 생성하여 Wallet에 대한 액세스를 인증할 수도 있습니다.




미스티 브리즈에서 사용할 수 있는 다양한 통화에서 현지 통화를 찾아보세요. 환경설정 > 법정통화** 메뉴에서 통화를 설정한 다음 필요한 통화를 선택하세요.



![devises](assets/fr/04.webp)



### 첫 거래 만들기


이미 브리즈 Wallet에 익숙하다면 미스티 브리즈의 직관적인 Interface을 사용해도 전혀 거부감이 들지 않을 것입니다.



Interface **잔액** 메뉴에서 **수령** 옵션을 클릭하여 청구서를 생성하면 Wallet에서 비트코인을 수령할 수 있습니다.



⚠️ 미스티 브리즈는 휴대폰 설정에서 애플리케이션에 대한 알림을 활성화하여 라이트닝 Address를 받을 수 있도록 요청할 것입니다.



미스티 브리즈와 함께라면 :




- Lightning Network에서 **100 사토시**에서 최대 **25,000,000 사토시**까지 비트코인을 받을 수 있습니다.
- 25,000 사토시**로부터 Bitcoin 메인 네트워크에서 비트코인을 받습니다.



![transactions](assets/fr/05.webp)



미스티 브리즈의 마법이 시작되는 곳입니다.


라이트닝 노드를 제공하고 결제 채널 개설 및 폐쇄 비용을 직접 부담하도록 하는 Breez Wallet와 달리, 미스티 브리즈는 사용자에게 아무 것도 요구하지 않습니다. 앞서 언급했듯이 미스티 브리즈는 라이트닝 노드를 기반으로 작동하지도 않습니다.



그 비하인드 스토리를 자세히 살펴보겠습니다.



실제로 여러분은 미스티 브리즈 Wallet와 연결된 Liquid Wallet를 소유하고 있습니다. 논리적으로, 여러분은 Lightning Network과 상호 운용할 수 있는 타사 잠수함 사토시 변환 서비스와 관련된 고정 요금으로 L-BTC(Liquid Bitcoin)를 취급하게 됩니다.



미스티 브리즈 Wallet로 결제를 받으면 발신자는 사토시를 보내며, 이 사토시는 볼트(현재 미스티 브리즈에서 사용)와 같은 전환 서비스를 통해 전송된 사토시를 L-BTC로 전환하여 미스티 브리즈 Wallet(관련 Liquid Wallet)로 받게 됩니다.


다음은 이면의 프로세스를 간소화한 다이어그램입니다.



![lnswap-in](assets/fr/06.webp)



잔액** 메뉴에서 Interface를 클릭하고 **송금** 옵션을 클릭하여 라이트닝 Invoice을 결제합니다.


라이트닝 Invoice, 받는 사람의 라이트닝 Address를 삽입하거나 Invoice의 QR 코드를 스캔하여 결제하세요.



![send-bitcoins](assets/fr/07.webp)



뒤에서 미스티 브리즈 Liquid과 연결된 Wallet이 볼츠를 통해 L-BTC에 해당하는 금액을 사토시로 변환하도록 한 다음, 이 사토시를 수신자의 라이트닝 Wallet(Lightning Network에 있음)로 전송합니다.



![send-bitcoin-bts](assets/fr/08.webp)



미스티 브리즈 인프라의 이 기능을 통해 사용자는 미스티 브리즈가 오프라인 상태에서도 트랜잭션을 수행할 수 있습니다.



보다 숙련된 사용자를 위해 **환경설정 > 개발자** 메뉴에서 :




- Breez 소프트웨어 개발 키트 버전입니다.
- 미스티 브리즈 Wallet의 공개 키입니다.
- 차용인, 기본 공개 키에서 파생된 고유 식별자입니다.
- Wallet 잔액.
- 팁 Liquid, 소량의 L-BTC 전송용.
- 소량의 Bitcoin를 전송하기 위한 Bitcoin 팁입니다.



Liquid Network과 동기화, 키 백업, 활동 로그 공유, Liquid Network 재검색 선택과 같은 특정 작업을 수행할 수도 있습니다.



![dev-mode](assets/fr/09.webp)


축하합니다! 이제 미스티 브리즈 Wallet와 Bitcoin 네트워크 간 트랜잭션에 대한 기여도를 잘 이해하셨을 것입니다. 이 튜토리얼이 유용했다면 Green에 엄지손가락을 치켜주세요. 기꺼이 여러분의 의견을 듣고 싶습니다.



더 나아가 미스티 브리즈와 비슷한 방식으로 작동하는 Aqua Wallet에 대한 튜토리얼도 살펴볼 것을 권장합니다:



https://planb.network/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125