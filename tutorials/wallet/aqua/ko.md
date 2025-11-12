---
name: Aqua
description: Bitcoin, 라이트닝, Liquid를 하나의 Wallet으로 통합한 제품
---
![cover](assets/cover.webp)


Aqua은 모바일 애플리케이션으로 Bitcoin와 Liquid를 위한 Hot Wallet을 쉽게 생성할 수 있으며, 통합 스왑 덕분에 복잡한 노드 관리 없이 라이트닝을 사용할 수 있는 가능성을 제공합니다. 또한 다양한 네트워크에서 USDT 스테이블코인을 관리할 수 있습니다.


삼손 모우의 지시에 따라 JAN3 회사에서 개발한 Aqua 앱은 처음에는 라틴 아메리카 사용자의 요구를 위해 특별히 설계되었지만, 전 세계 모든 사용자에게 적합합니다. 특히 초보자나 매일 Bitcoin를 결제에 사용하는 사용자에게 유용합니다.


이 튜토리얼에서는 Aqua의 다양한 기능을 사용하는 방법을 알아보겠습니다. 하지만 그 전에 Bitcoin에서 Sidechain이 무엇인지, Liquid이 어떻게 작동하는지 잠시 이해하여 Aqua의 가치를 충분히 파악해 보겠습니다.


![AQUA](assets/fr/01.webp)


## Sidechain란 무엇인가요?


Bitcoin 프로토콜은 네트워크의 탈중앙화를 유지하고 모든 사용자에게 보안을 분산시키는 데 도움이 되는 의도적인 기술적 제한이 있습니다. 그러나 이러한 제한은 때때로 사용자를 불편하게 만들 수 있으며, 특히 많은 양의 동시 트랜잭션으로 인해 혼잡한 상황에서는 더욱 그렇습니다. Bitcoin의 확장성에 대한 논쟁은 특히 블록사이즈 전쟁 기간 동안 커뮤니티를 오랫동안 분열시켰습니다. 이 에피소드 이후, Bitcoin 커뮤니티 내에서는 두 번째 Layer 시스템에서 off-chain 솔루션으로 확장성을 보장해야 한다는 것이 널리 인식되고 있습니다. 이러한 솔루션에는 사이드체인이 포함되는데, 이는 Lightning Network과 같은 다른 시스템에 비해 아직 상대적으로 잘 알려지지 않았고 거의 사용되지 않았습니다.


Sidechain은 메인 Blockchain과 병렬로 작동하는 독립적인 Blockchain입니다. "*양방향 페그*"라는 메커니즘 덕분에 Bitcoin를 계정 단위로 사용합니다. 이 시스템을 사용하면 비트코인을 메인 체인에 고정하여 원래 비트코인이 뒷받침하는 토큰의 형태로 유통되는 Sidechain에서 가치를 재생산할 수 있습니다. 이러한 토큰은 일반적으로 메인 체인에 잠긴 비트코인과 동등한 가치를 유지하며, 이 과정을 역으로 진행하여 Bitcoin에서 자금을 회수할 수 있습니다.


사이드체인의 목적은 더 빠른 거래, 낮은 수수료, 스마트 콘트랙트 지원과 같은 추가 기능이나 기술적 개선을 제공하는 것입니다. 이러한 혁신은 탈중앙화나 보안을 훼손하지 않으면서 Bitcoin Blockchain에 직접 구현할 수 있는 것은 아닙니다. 따라서 사이드체인을 사용하면 Bitcoin의 무결성을 유지하면서 새로운 솔루션을 테스트하고 탐색할 수 있습니다. 그러나 이러한 프로토콜은 선택한 거버넌스 모델과 합의 메커니즘에 따라 특히 탈중앙화 및 보안 측면에서 타협이 필요한 경우가 많습니다.


## Liquid란 무엇인가요?


Liquid은 거래 속도, 개인 정보 보호 및 기능을 개선하기 위해 블록스트림에서 개발한 Bitcoin을 위한 연합 Sidechain 오버레이입니다. 이는 페더레이션에 구축된 양방향 앵커링 메커니즘을 사용하여 비트코인을 메인 체인에 고정하고 그 대가로 Liquid 비트코인(L-BTC)을 생성하며, 토큰은 원래 비트코인의 지원을 유지하면서 Liquid에서 순환합니다.


![AQUA](assets/fr/02.webp)


Liquid Network는 블록을 검증하고 양측 페깅을 관리하는 Bitcoin 생태계의 공인된 기관으로 구성된 참여자 연합에 의존합니다. Liquid은 L-BTC 외에도 USDT 스테이블코인 및 기타 암호화폐와 같은 다른 디지털 자산을 발행할 수 있습니다.


![AQUA](assets/fr/03.webp)


## Aqua 애플리케이션 설치


첫 번째 단계는 물론 Aqua 애플리케이션을 다운로드하는 것입니다. 애플리케이션 스토어로 이동합니다:



- [Android용](https://play.google.com/store/apps/details?id=io.aquawallet.android);
- [Apple용](https://apps.apple.com/us/app/Aqua-Wallet/id6468594241).

![AQUA](assets/fr/04.webp)


Android 사용자의 경우, '.apk' 파일[해당 깃허브에서 다운로드 가능](https://github.com/AquaWallet/Aqua-Wallet/releases)을 통해 애플리케이션을 설치할 수도 있습니다.


![AQUA](assets/fr/05.webp)


애플리케이션을 실행한 다음 "*서비스 약관 및 개인정보처리방침을 읽고 동의했습니다*" 상자에 체크합니다.


![AQUA](assets/fr/06.webp)


## Aqua에서 Wallet 만들기


"*Wallet* 만들기" 버튼을 클릭합니다.


![AQUA](assets/fr/07.webp)


그리고 짜잔, Wallet이 이미 생성되었습니다!


![AQUA](assets/fr/08.webp)


하지만 우선, 이것은 자기 보관 Wallet이므로 Mnemonic를 물리적으로 백업하는 것이 필수적입니다. **이 Mnemonic는 모든 비트코인에 대한 완전한 무제한 액세스를 제공합니다**. 이 Mnemonic를 소유한 사람은 휴대폰에 물리적으로 접근하지 않더라도 자금을 훔칠 수 있습니다.


휴대폰 분실, 도난 또는 파손 시 비트코인에 대한 액세스를 복원할 수 있습니다. 따라서 디지털이 아닌 물리적 매체에 신중하게 저장하고 안전한 장소에 보관하는 것이 매우 중요합니다. 종이에 적어두거나 보안을 강화하기 위해 대형 Wallet의 경우 스테인리스 스틸 지지대에 새겨 화재, 홍수, 붕괴의 위험으로부터 보호하는 것이 좋습니다(소량의 비트코인을 보호하도록 설계된 Hot의 경우 간단한 종이 백업으로 충분할 수 있습니다).


이렇게 하려면 설정 메뉴를 클릭합니다.


![AQUA](assets/fr/09.webp)


그런 다음 "*seed 구문 보기*"를 클릭합니다. 이 12단어 문구를 물리적으로 백업합니다.


![AQUA](assets/fr/10.webp)


동일한 설정 메뉴에서 애플리케이션 언어와 사용되는 법정화폐를 변경할 수도 있습니다.


![AQUA](assets/fr/11.webp)


Wallet에서 첫 비트코인을 받기 전에 **빈 복구 테스트를 수행할 것을 강력히 권장합니다**. Xpub 또는 처음 받은 Address과 같은 몇 가지 참조 정보를 메모한 다음, 아직 비어 있는 상태에서 Aqua 앱에서 Wallet을 삭제하세요. 그런 다음 종이 백업을 사용하여 Aqua에서 Wallet을 복원해 보세요. 복원 후 생성된 쿠키 정보가 원래 기록했던 쿠키 정보와 일치하는지 확인하세요. 일치한다면 종이 백업이 신뢰할 수 있는 것이니 안심해도 됩니다. 테스트 복구를 수행하는 방법에 대해 자세히 알아보려면 이 다른 튜토리얼을 참조하세요:


https://planb.academy/tutorials/wallet/backup/recovery-test-5a75db51-a6a1-4338-a02a-164a8d91b895

에뮬레이터를 사용 중이라 화면에는 보이지 않지만 설정에서 생체 인증 시스템으로 앱을 잠글 수 있는 옵션을 찾을 수 있습니다. 이 보안 기능이 없으면 잠금 해제된 휴대폰에 액세스할 수 있는 사람이 비트코인을 훔칠 수 있으므로 이 기능을 활성화하는 것을 강력히 권장합니다. IOS에서는 Face ID를, Android에서는 지문을 사용할 수 있습니다. 인증 중에 이러한 방법으로 인증에 실패하더라도 휴대폰의 PIN 코드를 사용해 앱에 액세스할 수 있습니다.


## Aqua에서 비트코인 받기


이제 Wallet이 설정되었으니 첫 번째 Sats를 받을 준비가 되었습니다! "*Wallet*" 메뉴에서 "*수신*" 버튼을 클릭하기만 하면 됩니다.


![AQUA](assets/fr/12.webp)


온체인, Liquid 또는 라이트닝을 통해 비트코인을 받을 수 있습니다.


![AQUA](assets/fr/13.webp)


온체인 트랜잭션의 경우, Aqua은 Address를 받을 수 있는 특정 수신 Sats을 generate로 지정합니다.


![AQUA](assets/fr/14.webp)


마찬가지로 Liquid를 선택하면 Aqua이 Liquid Address을 제공합니다.


![AQUA](assets/fr/15.webp)


Lightning을 통해 자금을 받으려면 먼저 원하는 금액을 지정해야 합니다.


![AQUA](assets/fr/16.webp)


그런 다음 "*generate Invoice*"를 클릭합니다.


![AQUA](assets/fr/17.webp)


Aqua은 라이트닝 Wallet에서 자금을 받기 위해 Invoice을 생성합니다. 온체인 및 Liquid 옵션과 달리, Aqua은 라이트닝 노드가 아니므로 라이트닝을 통해 받은 자금은 볼츠 도구를 사용해 Liquid에서 L-BTC로 자동 변환된다는 점에 유의하시기 바랍니다. 이 과정을 통해 라이트닝을 통해 자금을 주고받을 수 있지만, 비트코인을 라이트닝에 저장하지 않아도 됩니다.


![AQUA](assets/fr/18.webp)


개인적으로는 라이트닝을 통해 비트코인을 Aqua로 전송하는 것부터 시작하겠습니다. 제공된 Invoice로 거래가 완료되면 확인을 받습니다.


![AQUA](assets/fr/19.webp)


스왑 진행 상황을 확인하려면 Wallet의 홈 페이지로 돌아가서 "*L2 Bitcoin*" 계정을 클릭하면 라이트닝(스왑을 통해) 및 Liquid 거래가 나열되어 있습니다.


![AQUA](assets/fr/20.webp)


여기에서 거래 내역과 L-BTC 잔액을 확인할 수 있습니다.


![AQUA](assets/fr/21.webp)


## Bitcoin와 Aqua 교체


이제 Aqua Wallet에 자산이 있으므로 앱에서 직접 교환하여 기본 Bitcoin Blockchain 또는 Liquid으로 전송할 수 있습니다. 비트코인을 USDT 스테이블코인(또는 다른 코인)으로 전환할 수도 있습니다. 그러려면 "*마켓플레이스*" 메뉴로 이동하세요.


![AQUA](assets/fr/22.webp)


"*스왑*"을 클릭합니다.


![AQUA](assets/fr/23.webp)


"*이체 대상*" 상자에서 거래하고자 하는 자산을 선택합니다. 현재 저는 L-BTC만 보유하고 있으므로 이를 선택합니다.


![AQUA](assets/fr/24.webp)


"*이체 대상*" 상자에서 스왑 대상 자산을 선택합니다. 저는 Liquid Network에서 USDT를 선택했습니다.


![AQUA](assets/fr/25.webp)


전환하려는 금액을 입력합니다.


![AQUA](assets/fr/26.webp)


"*계속*"을 클릭하여 확인합니다.


![AQUA](assets/fr/27.webp)


스왑 설정이 마음에 드는지 확인한 다음 화면 하단의 '*스왑*' 버튼을 드래그하여 확인합니다.


![AQUA](assets/fr/28.webp)


이제 스왑이 확정되었습니다.


![AQUA](assets/fr/29.webp)


Wallet을 되돌아보면, 이제 Liquid에 USDT가 있음을 알 수 있습니다.


![AQUA](assets/fr/30.webp)


## Aqua로 비트코인 보내기


이제 Aqua Wallet에 비트코인이 있으니 전송할 수 있습니다. "*송금*" 버튼을 클릭합니다.


![AQUA](assets/fr/31.webp)


송금할 자산을 선택하거나 거래를 진행할 네트워크를 선택합니다. 저는 라이트닝을 통해 비트코인을 보내려고 합니다.


![AQUA](assets/fr/32.webp)


다음으로 송금에 필요한 정보를 입력합니다. 온체인 또는 Liquid 비트코인의 경우 수신 Address를 입력해야 하고, 라이트닝의 경우 Invoice이 필요합니다. 이 정보를 제공된 필드에 직접 붙여넣거나 QR코드 아이콘을 사용하여 카메라를 열고 Address 또는 Invoice을 스캔할 수 있습니다. 그런 다음 "*계속*"을 클릭합니다.


![AQUA](assets/fr/33.webp)


모든 정보가 올바른 것 같으면 "*계속*"을 다시 클릭합니다.


![AQUA](assets/fr/34.webp)


그러면 Aqua에서 거래 요약이 표시됩니다. 목적지 Address, 요금 및 금액을 포함한 모든 정보가 정확한지 확인하세요. 거래를 확인하려면 화면 하단의 "*슬라이드하여 보내기*" 버튼을 밉니다.


![AQUA](assets/fr/35.webp)


그러면 배송 확인을 받게 됩니다.


![AQUA](assets/fr/36.webp)


이제 Aqua 앱을 사용하여 하나의 Interface에서 Bitcoin, Lightning 및 Liquid로 자금을 받고 사용하는 방법을 알게 되었습니다.


이 튜토리얼이 유용했다면 아래에 Green 엄지손가락을 남겨주시면 감사하겠습니다. 이 글을 소셜 네트워크에 자유롭게 공유해 주세요. 정말 감사합니다!


또한 Blockstream Green 모바일 앱의 또 다른 종합 튜토리얼인 Liquid Wallet 설정에 대한 또 다른 흥미로운 솔루션인 이 튜토리얼을 확인해 보시기 바랍니다:


https://planb.academy/tutorials/wallet/mobile/blockstream-app-liquid-b3e4fb82-902e-4782-ad2b-a61ab05a543a