---
name: BTCPay Server - USDT
description: USDTプラグインを設定する手順
---

⚠️ **重大なセキュリティ警告（2026年8月7日）:** BTCPay Server に影響する重大な脆弱性が実際に悪用されており、資金の喪失につながるおそれがあります。直ちに `Admin Dashboard > Server > Maintenance > Update` から **バージョン 2.4.2** へ更新し、フッターに `2.4.2` と表示されていることを確認してください。すぐに更新できない場合は、BTCPay Server を停止してください。更新後は、macaroons および `macaroons.db` を完全に再生成し、その他の Lightning バックエンドの認証文字列もすべて完全に再生成する必要があります。また、BTCPay Server 内でホットな on-chain ウォレットを生成していた場合は、その資金を移動したうえでウォレットを作成し直してください。インテグレーターの方は NBXplorer もバージョン 2.6.10 へ更新してください。出典: [BTCPay Server 2.4.2 リリースノート](https://github.com/btcpayserver/btcpayserver/releases/tag/v2.4.2)。

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-update-7033a305-8404-4cba-8324-4c7eb679016b
![cover](assets/cover.webp)

このビデオでは、オンラインストア用にBTCPay ServerでUSDTプラグインを設定する方法を学びます。プラグインマネージャーを使用してプラグインをインストールする方法、専用ノードを使用してサーバー設定を最適化し利用可能性を向上させる方法、および安全に支払いを受け取るためにウォレットを設定する方法を学べます。

![BTCPay-Tether](https://youtu.be/hAymYr6YDMY)
