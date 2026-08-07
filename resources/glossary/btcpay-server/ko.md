---
term: BTCPay Server

definition: 중개자 없이 비트코인 결제를 수락할 수 있게 해주는 오픈 소스 결제 프로세서.
---

⚠️ **긴급 보안 경고(2026년 8월 7일):** BTCPay Server에 영향을 미치는 심각한 취약점이 현재 활발히 악용되고 있으며, 자금 손실로 이어질 수 있습니다. `Admin Dashboard > Server > Maintenance > Update`를 통해 즉시 인스턴스를 **version 2.4.2**로 업데이트한 뒤, 푸터에 `2.4.2`가 표시되는지 확인하십시오. 즉시 업데이트할 수 없다면 BTCPay Server를 종료하십시오. 업데이트 후에는 macaroons와 `macaroons.db`를 완전히 새로 발급하고, 다른 Lightning 백엔드의 인증 문자열도 모두 완전히 새로 발급해야 하며, BTCPay Server 내에서 핫 on-chain 지갑을 생성한 적이 있다면 해당 자금을 옮기고 지갑을 다시 생성하십시오. 통합 개발자는 NBXplorer도 version 2.6.10으로 업데이트해야 합니다. 출처: [BTCPay Server 2.4.2 릴리스 노트](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2).

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b

BTCPay 서버는 오픈 소스 결제 프로세서로, 판매자와 사용자가 거래 처리를 위해 제3자에 의존하지 않고도 Bitcoin 결제를 수락할 수 있도록 지원합니다.

2017년에 출시된 BTCPay 서버는 하드웨어 지갑, 청구 및 회계 도구 지원, Lightning Network와의 호환성 등의 고급 기능을 갖춘 전자상거래 사이트를 위한 Bitcoin 결제 통합 솔루션을 제공합니다.

니콜라스 도리에에 의해 개발이 시작되었는데, 그에 따르면 비트페이가 세그윗2x를 "진짜" Bitcoin로 홍보하여 사용자를 오도하는 행위에 대한 대응으로 시작되었습니다. 이러한 반대는 2017년 8월에 니콜라스 도리에가 올린 유명한 트윗에 요약되어 있습니다:


> "_이건 거짓말이야, 너에 대한 나의 신뢰가 깨졌어, 널 쓸모없게 만들 거야_"

