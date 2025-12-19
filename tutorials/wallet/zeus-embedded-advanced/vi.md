---
name: Zeus Embedded - Nâng cao
description: Ví Lightning tự lưu ký đa nút
---

![Zeus](assets/cover.webp)


## Giới thiệu về ZEUS Wallet


ZEUS là ứng dụng quản lý nút Bitcoin Wallet di động có đầy đủ chức năng của Bitcoin Lightning Wallet giúp thanh toán Bitcoin trở nên đơn giản, giúp người dùng kiểm soát hoàn toàn tài chính của mình và cho phép người dùng nâng cao quản lý các nút Lightning của mình ngay trên lòng bàn tay.


### ZEUS dành cho ai?

Hiện tại ZEUS dành cho những người chạy các nút gia đình / doanh nghiệp của riêng mình với [Lightning Network Daemon (LND)](https://lightning.engineering/) hoặc [Core Lightning (CLN)](https://blockstream.com/lightning/) và quản lý chúng từ xa thông qua Zeus.


Các thương nhân sử dụng [BTCPay](https://btcpayserver.org/), [LNBits](https://lnbits.com/) hoặc [Alby](https://getalby.com/) (hoặc bất kỳ tài khoản LNDhub nào khác) cũng có thể kết nối, sử dụng và quản lý các nút / tài khoản của họ từ ZEUS.


[Bắt đầu từ v0.8](https://blog.zeusln.com/zeus-v0-8-0-open-beta/), ZEUS sẽ bắt đầu phục vụ người dùng phổ thông, những người chỉ muốn một cách đơn giản để thực hiện các khoản thanh toán bitcoin nhanh chóng và rẻ tiền từ thiết bị di động của họ, với một [nút Lightning di động tích hợp sẵn](https://docs.zeusln.app/category/embedded-node) cùng [Nhà cung cấp dịch vụ Lightning (LSP)](https://docs.zeusln.app/lsp/intro) tích hợp.


### Tài nguyên quan trọng của Zeus:


- Trang web chính thức của Zeus - [https://zeusln.app/](https://zeusln.app/)
- Tài liệu Zeus - [https://docs.zeusln.app/](https://docs.zeusln.app/)
- [Kho lưu trữ Github của Zeus](https://github.com/ZeusLN/zeus)
- [Nhóm hỗ trợ Zeus trên Telegram](https://t.me/ZeusLN)
- [Zeus trên NOSTR](https://iris.to/zeus@zeusln.app)
- [Thông báo Blog của Zeus](https://blog.zeusln.com)


### Tính năng của Zeus

#### Tính năng chung:


- Tự quản, Bitcoin và Lightning chỉ Wallet
- Không có phí xử lý, Không có KYC
- Mã nguồn mở hoàn toàn (APGLv3)
- Hỗ trợ nhiều nút/tài khoản (bạn có thể quản lý nút trang chủ của riêng mình, chạy nút LND nhúng, kết nối với nhiều tài khoản LNDhub)
- Menu hoạt động dễ sử dụng
- Mã hóa PIN hoặc passphrase, Chế độ riêng tư - ẩn dữ liệu nhạy cảm của bạn
- Sổ liên lạc, nhiều chủ đề, nhiều ngôn ngữ


#### Tính năng kỹ thuật


- Kết nối qua Tor
- Hỗ trợ LNURL đầy đủ (Thanh toán, rút tiền, xác thực, kênh), Gửi đến địa chỉ Lightning
- Quản lý kênh chiếu sáng chi tiết, hỗ trợ MPP/AMP, Keysend, quản lý phí định tuyến
- Hỗ trợ Replace-by-fee (RBF) và Con trả tiền cho cha mẹ (CPFP)
- Thanh toán và yêu cầu NFC, Ký và xác minh tin nhắn
- Hỗ trợ SegWit và Taproot
- Kênh Taproot đơn giản
- Địa chỉ sét tự lưu giữ (@zeuspay.com)
- Điểm bán hàng của Square (sắp mở PoS)


### Hướng dẫn và Video hướng dẫn

Để có thể sử dụng Zeus và quản lý các kênh Lightning, tính thanh khoản, phí, v.v., tốt hơn hết bạn nên đọc trước một số hướng dẫn quan trọng về Lightning Network.


#### Hướng dẫn:


- [LND - Tài liệu Lightning Network Daemon](https://docs.lightning.engineering/)
- [CLN - Tài liệu Core Lightning](https://lightning.readthedocs.io/index.html)
- [Hướng dẫn Lightning cho người mới bắt đầu](https://bitcoiner.guide/lightning/) – bởi Bitcoin Hỏi & Đáp
- [Quản lý Nút Lightning](https://www.lightningnode.info/) – bởi openoms
- [Mạng Lightning và phép ẩn dụ sân bay](https://darthcoin.substack.com/p/the-lightning-network-and-the-airport)
- [Quản lý thanh khoản Nút Lightning](https://darthcoin.substack.com/p/managing-lightning-node-liquidity)
- [Bảo trì Nút Lightning](https://darthcoin.substack.com/p/lightning-node-maintenance)


#### Video hướng dẫn của BTC Sessions


![Zeus Bitcoin Lightning Wallet - Mobile Node Management](https://youtu.be/hmmehTnV3ys)



## Hướng dẫn chi tiết cách bắt đầu sử dụng nút nhúng Zeus LN trên thiết bị di động của bạn


![Image](assets/en/01.webp)


Tôi dành tặng hướng dẫn này cho tất cả những người dùng Lightning Network (LN) mới muốn bắt đầu hành trình tự chủ mới bằng cách sử dụng nút tự lưu ký Wallet trên thiết bị di động của họ.


Hãy xem xét rằng bạn đã trải qua tất cả các ví LN lưu ký, nhưng bạn vẫn chưa sẵn sàng để bắt đầu chạy một nút định tuyến CÔNG KHAI LN, bạn chỉ muốn xếp chồng nhiều Sats hơn LN theo cách tự lưu ký hơn và thực hiện các khoản thanh toán thường xuyên của mình qua LN.


Đây là Zeus, bắt đầu với [phiên bản v0.8.0 được công bố trên blog của họ](https://blog.zeusln.com/new-release-zeus-v0-8-0/), hiện đang cung cấp một nút LND nhúng trong ứng dụng. Cho đến nay Zeus là một ứng dụng quản lý nút từ xa + tài khoản LNDhub. Nhưng bây giờ… nút nằm trong điện thoại!


![Image](assets/en/02.webp)


### Tóm tắt nhanh các tính năng chính của Zeus Node:



- **Nút LND riêng tư** - Điều đó có nghĩa là nút này sẽ KHÔNG thực hiện định tuyến công khai các khoản thanh toán khác thông qua nút của bạn. Nút và các kênh không được thông báo (riêng tư, không hiển thị trên biểu đồ LN công khai). Việc nhận và thực hiện thanh toán sẽ được thực hiện thông qua các đối tác LSP được kết nối của bạn. **NHỚ RẰNG**: Nút nhúng Zeus sẽ KHÔNG thực hiện định tuyến công khai!
- **Dịch vụ LND liên tục** - người dùng có thể kích hoạt tính năng này và giữ cho dịch vụ LND hoạt động liên tục như bất kỳ nút LN thông thường nào. Ứng dụng không cần phải mở, dịch vụ liên tục sẽ giữ cho mọi giao tiếp trực tuyến.
-   **Bộ lọc khối Neutrino** - việc đồng bộ khối được thực hiện bằng cách sử dụng [bộ lọc khối và giao thức Neutrino](https://bitcoinops.org/en/topics/compact-block-filters/) (không cung cấp bất kỳ thông tin nào về số dư on-chain của người dùng). Nhắc nhở: với các kết nối internet độ trễ cao / chậm, việc đồng bộ khối dựa trên Neutrino này đôi khi có thể thất bại. Thử chuyển sang máy chủ Neutrino gần đó có thể giúp khôi phục đồng bộ. Nếu không có đồng bộ này, nút LND của bạn sẽ không thể khởi động!
- **Kênh Taproot đơn giản** - Khi đóng các kênh này, người dùng sẽ phải chịu ít phí hơn và có nhiều quyền riêng tư hơn vì họ dường như thích bất kỳ khoản chi Taproot nào khác khi kiểm tra dấu chân On-Chain của mình.
- **Integrated LSP** - Olympus là nút LSP mới cho Zeus. Người dùng có thể nhận Sats qua LN ngay lập tức mà không cần thiết lập kênh LN trước đó. Chỉ cần tạo LN Invoice và thanh toán từ bất kỳ LN Wallet nào khác, với dịch vụ kênh Zeus 0-conf. Đọc thêm về Zeus LSP tại đây. LSP cũng cung cấp thêm quyền riêng tư cho người dùng của chúng tôi bằng cách cung cấp cho họ các hóa đơn được gói lại để che giấu khóa công khai của các nút của họ khỏi người thanh toán.
- **Sổ liên lạc** - bạn có thể lưu danh bạ theo cách thủ công hoặc nhập từ NOSTR để dễ dàng gửi thanh toán đến các địa chỉ thường xuyên của bạn.
- Hỗ trợ đầy đủ cho LNURL, LN Address gửi và nhận - giờ đây bạn có thể thiết lập LN Address tự quản lý của riêng mình với @zeuspay.com. Nhắc nhở: Bạn cũng có thể sử dụng Zeus cho LN-auth trên các trang web mà bạn có thể đăng nhập bằng xác thực LN. Rất tiện dụng.
- **Điểm bán hàng** - Bây giờ người dùng thương gia có thể thiết lập các mặt hàng sản phẩm của riêng họ và bán trực tiếp từ Zeus, với PoS tích hợp. Hiện tại có các nhu cầu cơ bản nhưng trong tương lai sẽ có các tính năng mở rộng.
- **Nhật ký LND** - người dùng có thể đọc nhật ký dịch vụ LND theo thời gian thực và sử dụng chúng để gỡ lỗi các sự cố có thể xảy ra (chủ yếu là kết nối kém)
- **Sao lưu tự động** - các kênh nút LN được sao lưu tự động trên máy chủ Olympus. Sao lưu tự động này được mã hóa bằng nút Wallet seed của bạn (không có seed thì hoàn toàn vô dụng). Người dùng cũng có thể xuất thủ công SCB (sao lưu kênh tĩnh) để phục hồi sau thảm họa.


### Cách tham gia Zeus LN Node (LND nhúng)


Trong hướng dẫn này tôi sẽ chỉ nói về nút LND tích hợp sẵn, chứ không phải về những cách khác để sử dụng ứng dụng tuyệt vời này (quản lý nút từ xa và tài khoản LNDhub). Đối với các loại kết nối khác, vui lòng tham khảo [trang tài liệu Zeus](https://docs.zeusln.app/category/getting-started), đã được giải thích rất rõ ràng và không cần viết một hướng dẫn riêng biệt.


#### BƯỚC 1 - THIẾT LẬP BAN ĐẦU


Do Zeus là một nút LND đầy đủ nên tôi sẽ có một số khuyến nghị ban đầu:



- Không sử dụng thiết bị cũ, điều đó có thể ảnh hưởng đến việc sử dụng ứng dụng mạnh mẽ này. Đặc biệt là trong thời gian đồng bộ hóa, ứng dụng có thể sử dụng CPU và RAM một cách chuyên sâu. Việc thiếu những thứ này thậm chí có thể khiến ứng dụng Zeus không thể sử dụng được.
- Sử dụng ít nhất Android 11 làm hệ điều hành di động và cập nhật nhiều nhất có thể. Đối với iOS cũng vậy, hãy thử sử dụng phiên bản hệ điều hành cao hơn nhiều.
- Bạn sẽ cần ít nhất 1GB dung lượng đĩa để lưu trữ dữ liệu. Theo thời gian có thể tăng thêm, nhưng có chức năng nén cơ sở dữ liệu xuống mức MB.
- KHÔNG cần sử dụng Zeus với dịch vụ Tor hoặc Orbot. Vui lòng không làm phức tạp mọi thứ hơn mức cần thiết. Trong trường hợp này, Tor sẽ không cung cấp cho bạn nhiều quyền riêng tư hơn mà chỉ khiến mọi thứ trở nên tệ hơn đối với quá trình đồng bộ ban đầu. Ngoài ra, hãy cẩn thận với các VPN bạn đang sử dụng và kiểm tra độ trễ của kết nối tới máy chủ neutrino. Hãy nhớ rằng, bộ lọc khối Neutrino không làm rò rỉ hoặc theo dõi danh tính thiết bị của bạn, chỉ phục vụ các khối. Lưu lượng truy cập LN cũng nằm sau LSP với các kênh riêng tư nên rất ít thông tin bị lộ ra ngoài, không có lý do gì để lo lắng về quyền riêng tư.
-   Hãy kiên nhẫn trong quá trình đồng bộ ban đầu, có thể mất vài phút. Cố gắng kết nối với mạng internet băng thông rộng có độ trễ tốt. Nếu bạn chạy node Bitcoin của riêng mình, [bạn có thể kích hoạt dịch vụ neutrino](https://docs.lightning.engineering/lightning-network-tools/lnd/enable-neutrino-mode-in-bitcoin-core) và kết nối Zeus của bạn với node riêng của bạn, thậm chí sử dụng LAN nội bộ, để đạt được tốc độ tối đa.


Sau khi bạn thiết lập loại kết nối “Nút nhúng”, ứng dụng sẽ bắt đầu đồng bộ hóa trong một thời gian. Hãy kiên nhẫn chờ hoàn tất phần đó, sau đó vào trang Cài đặt chính.


![Image](assets/en/03.webp)


Tóm lại, chúng ta hãy đi sâu vào từng phần Cài đặt và tìm hiểu một số tính năng chính trước khi bạn bắt đầu sử dụng Zeus:


**A - CÀI ĐẶT**


Đây là phần có các thiết lập chung cho toàn bộ ứng dụng


**1 - Lightning Service Provider (LSP)**


Sau đây là hai dịch vụ LSP:



- _Kênh Just in time_ - khi bạn không có kênh nào mở hoặc thanh khoản vào, nếu dịch vụ được kích hoạt, nó sẽ mở một kênh ngay lập tức cho bạn. Tùy chọn này có thể bị vô hiệu hóa nếu bạn không muốn mở thêm các kênh loại này.
- _Yêu cầu kênh trước_ - bạn có thể mua kênh truyền hình đến từ Olympus LSP trực tiếp trong ứng dụng với nhiều tùy chọn và số lượng (cho cả kênh truyền hình đến và kênh truyền hình đi).


LSP giúp kết nối người dùng với mạng Lightning bằng cách mở các kênh thanh toán đến các nút của họ. [Đọc thêm về LSP tại đây](https://medium.com/breez-technology/envisioning-lsps-in-the-lightning-economy-832b45871992). ZEUS có một LSP mới được tích hợp có tên là [OLYMPUS by ZEUS](https://mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581), có sẵn cho tất cả người dùng sử dụng nút tích hợp mới.


Trong phần này, theo mặc định là Olympus LSP (https://0conf.lnolymp.us), nhưng bạn cũng có thể thiết lập một 0conf LSP khác hỗ trợ giao thức này.


_Hãy ghi nhớ:_

_khi bạn mở kênh với Olympus LSP bằng cách sử dụng hóa đơn LN được gói lại, bạn cũng nhận được thanh khoản đầu vào là 100k! Đây thực sự là lựa chọn tốt trong trường hợp bạn cần nhận ngay thêm Sats._

_Ví dụ: bạn gửi 400k Sats để mở kênh LSP, sau đó LSP sẽ mở kênh dung lượng 500k Sats về phía nút Zeus của bạn và đẩy 400k Sats mà bạn gửi về phía mình._

_"Thanh khoản đầu vào" = nhiều “không gian” hơn trong kênh của bạn để tiếp nhận._


Trong tương lai, chúng tôi hy vọng có thể có nhiều LSP khác có thể tích hợp vào Zeus và sử dụng luân phiên từng cái. Chỉ là vấn đề thời gian cho đến khi các LSP mới áp dụng một tiêu chuẩn mở cho các kênh 0conf loại này.


Nếu bạn không muốn mở kênh mới ngay lập tức, bạn có thể tắt tùy chọn này.


Trong cùng phần này, bạn cũng có tùy chọn để chọn "yêu cầu Simple Taproot Channels" khi LSP sẽ mở một kênh hướng đến nút Zeus của bạn. Các Simple Taproot Channels này cung cấp quyền riêng tư On-Chain tốt hơn và phí đóng kênh thấp hơn. Chỉ có hai lý do khiến bạn không muốn sử dụng chúng:



- Chúng còn mới và vẫn có thể có lỗi trong LND khi sử dụng chúng.
- Đối tác của bạn không hỗ trợ chúng. Ngay cả các nút LND cũng phải lựa chọn rõ ràng cho đến thời điểm hiện tại.


**2 - Cài đặt thanh toán**


Tính năng này sẽ cung cấp cho bạn cách thiết lập mức phí ưa thích của riêng bạn cho các khoản thanh toán, qua LN hoặc onchain. Ngoài ra còn cung cấp tùy chọn tăng hoặc giảm thời gian chờ cho hóa đơn của bạn.


Nếu một số khoản thanh toán LN của bạn không thành công, bạn có thể tăng phí để tìm tuyến đường tốt hơn. Ngoài ra, nếu đang thực hiện giao dịch onchain, bạn có thể thiết lập một khoản phí cụ thể để giao dịch của bạn không bị kẹt trong Mempool trong thời gian dài, trong trường hợp phí cao.


**3 - Cài đặt hóa đơn**


Trong phần này có một số tùy chọn cho hóa đơn generate:



- Thiết lập một bản ghi nhớ chuẩn để hiển thị trong Invoice bạn generate
- Thời gian hết hạn tính bằng giây, trong trường hợp bạn muốn thời gian cụ thể, dài hơn hoặc ngắn hơn để thanh toán Invoice của bạn
- Bao gồm gợi ý tuyến đường - cung cấp thông tin để tìm các kênh không được quảng cáo hoặc riêng tư. Điều này cho phép định tuyến các khoản thanh toán đến các nút không hiển thị công khai trên mạng. Gợi ý tuyến đường cung cấp một tuyến đường một phần giữa nút riêng tư của người nhận và một nút công khai. Gợi ý tuyến đường này sau đó được bao gồm trong Invoice do người nhận tạo ra và cung cấp cho người trả tiền. Tôi đề xuất bật nó theo mặc định, nếu không các khoản thanh toán đến có thể không thành công (không tìm thấy tuyến đường).
- AMP Invoice - Thanh toán đa đường nguyên tử là một loại thanh toán Lightning mới được LND triển khai cho phép nhận Sats mà không cần Invoice cụ thể, bằng cách sử dụng [keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend). Về cơ bản là một mã thanh toán tĩnh. [Đọc thêm tại đây](https://docs.lightning.engineering/lightning-network-tools/LND/amp).
- Hiển thị trường tiền ảnh tùy chỉnh - chỉ sử dụng tùy chọn này trong những trường hợp rất cụ thể khi bạn thực sự muốn sử dụng các trường tùy chỉnh trong tiền ảnh. [Đọc thêm tại đây](https://Bitcoin.stackexchange.com/questions/90797/how-can-i-generate-preimage-for-lightning-network-Invoice-should-i).


Một tùy chọn khác trong phần này là cách thiết lập loại Address trên chuỗi mà bạn muốn sử dụng: SegWit lồng nhau, SegWit, Taproot.


![Image](assets/en/04.webp)


Nhấp vào nút bánh xe trên cùng và màn hình bật lên sẽ xuất hiện để chọn loại Address mong muốn. Sau khi bạn thiết lập, lần tiếp theo bạn nhấn nút nhận cho onchain, nó sẽ generate loại Address đã chọn. Bạn có thể thay đổi bất cứ lúc nào.


**4 - Cài đặt kênh**


Trong phần này bạn thiết lập trước một số tính năng mở kênh như:



- số lượng xác nhận
- Thông báo kênh (mặc định là tắt), nghĩa là sẽ có các kênh không được thông báo
- Kênh Taproot đơn giản
- Hiển thị nút mua kênh


**5 - Cài đặt quyền riêng tư**


Sau đây bạn sẽ tìm thấy một số cài đặt cơ bản để tăng thêm quyền riêng tư khi sử dụng ứng dụng Zeus:



- Block explorer để mở thông tin chi tiết về giao dịch (Mempool.space, blockstream.info hoặc thông tin cá nhân tùy chỉnh)
- Đọc clipboard - bật/tắt nút chuyển đổi nếu bạn muốn Zeus đọc clipboard của thiết bị bạn
- Chế độ Lurker - bật/tắt nếu bạn muốn ẩn thông tin nhạy cảm cụ thể khỏi ứng dụng Zeus của mình. Đây là một lựa chọn tốt khi bạn tạo bản demo hoặc ảnh chụp màn hình.
- Đề xuất phí Mempool - kích hoạt tùy chọn này nếu bạn muốn sử dụng mức phí được đề xuất từ [Mempool.space](https://Mempool.space/)


**6 - Bảo mật**


Phần này chỉ có hai tùy chọn để bảo mật ứng dụng khi mở: đặt mật khẩu hoặc mã PIN.


Sau khi bạn đặt mã PIN để mở ứng dụng, bạn cũng có thể đặt "mã PIN cưỡng bức". Mã PIN bổ sung bí mật này CHỈ được sử dụng trong trường hợp cưỡng bức, nếu bạn bị đe dọa. Nếu bạn đặt mã PIN này, toàn bộ cấu hình sẽ bị XÓA BỎ. Vì vậy, tốt hơn hết là bạn nên cập nhật bản sao lưu của mình. Bản sao lưu tự động được BẬT theo mặc định, nhưng cũng tốt nếu bạn có bản sao lưu của riêng mình, ngoài thiết bị.


**7 - Tiền tệ**


Bật hoặc tắt tùy chọn hiển thị chuyển đổi tiền tệ fiat trong ứng dụng Zeus. Hiện đang hỗ trợ hơn 30 loại tiền tệ fiat trên toàn thế giới.


**8 - Ngôn ngữ**


Bạn có thể chuyển đổi giữa nhiều ngôn ngữ dịch thuật, được cộng đồng Zeus đánh giá với người bản ngữ.


**9 - Hiển thị**


Trong phần này, bạn có thể cá nhân hóa màn hình Zeus của mình, chọn nhiều chủ đề màu sắc khác nhau, màn hình mặc định (bàn phím hoặc cân bằng), hiển thị bí danh nút của bạn, kích hoạt các nút bàn phím lớn, hiển thị nhiều chữ số thập phân hơn.


**10 - Điểm bán hàng**


Đây là tính năng đặc biệt để bật/tắt hệ thống PoS tích hợp vào Zeus. Bạn có thể chạy PoS độc lập hoặc liên kết với hệ thống PoS Square. Hiện đang hỗ trợ các chức năng cơ bản như PoS, nhưng đủ để bắt đầu tốt và có thể giúp những thương gia nhỏ (quán bar/nhà hàng, cửa hàng tạp hóa) bắt đầu chấp nhận BTC theo cách gốc.


Bên trong phần cài đặt này, bạn sẽ tìm thấy nhiều tùy chọn khác nhau để thiết lập PoS của mình:



- Loại thanh toán xác nhận: Chỉ LN, 0-conf, 1-conf
- Bật / tắt tiền boa cho nhân viên vận hành PoS
- Hiển thị / ẩn bàn phím
- Tỷ lệ thuế áp dụng cho vé
- Tạo sản phẩm và danh mục sản phẩm
- Một danh sách đơn giản của tất cả các doanh số bán hàng


Sau đây là video demo trực tiếp về cách sử dụng Zeus PoS:


**B - Wallet dự phòng**


Node nhúng trong ZEUS dựa trên LND và sử dụng [định dạng aezeed seed](https://github.com/lightningnetwork/LND/blob/master/aezeed/README.md). Định dạng này khác với [định dạng BIP39](https://github.com/Bitcoin/bips/blob/master/bip-0039.mediawiki) thông thường mà bạn thấy trong hầu hết các ví Bitcoin, mặc dù chúng có vẻ giống nhau. Aezeed bao gồm một số dữ liệu bổ sung bao gồm ngày sinh của Wallet sẽ giúp việc quét lại trong quá trình khôi phục diễn ra hiệu quả hơn.


Định dạng khóa aezeed phải tương thích với các ví di động sau: Blixt, BlueWallet và Breez. Lưu ý rằng chỉ riêng seed sẽ không đủ để khôi phục toàn bộ số dư của bạn nếu bạn có các kênh đóng mở hoặc đang chờ xử lý!


Tìm hiểu thêm về quy trình sao lưu và khôi phục trên [trang Zeus Docs](https://docs.zeusln.app/for-users/embedded-node/backup-and-recovery).


LỜI KHUYÊN VỀ POWER: Khi bạn lưu seed, vui lòng lưu cả khóa công khai của nút! Đôi khi tốt hơn là nên có nó trong tầm tay, cùng với seed và SCB (Sao lưu kênh tĩnh) trong trường hợp bạn cần xác minh quá trình khôi phục.


SCB chỉ cần thiết nếu bạn mở kênh LN. Trong trường hợp bạn chỉ có tiền trên chuỗi, thì không cần thiết.


Nếu bạn thấy rằng sau một thời gian dài vẫn không hiển thị lịch sử txs cũ, hãy vào Embedded node - Peers và vô hiệu hóa tùy chọn sử dụng danh sách các peer đã chọn (mặc định là btcd.lnolymp.us). Điều đó sẽ kích hoạt khởi động lại và sẽ kết nối với node neutrino khả dụng đầu tiên với thời gian phản hồi tốt hơn. Hoặc sử dụng các peer neutrino nổi tiếng khác được đề cập bên dưới.


Nếu bạn muốn xem thêm các tùy chọn khôi phục cho nút LND, [vui lòng đọc hướng dẫn trước đây của tôi](https://darth-coin.github.io/nodes/shtf-restore-LND-node-en.html), tại đó bạn có thể tìm thấy các bước để nhập aezeed seed vào Sparrow Wallet hoặc các phương pháp khác.


**C - Nút nhúng**


Trong phần này chúng ta sẽ tìm thấy một số công cụ cơ bản để quản lý nút tích hợp:



- _Khôi phục sau thảm họa_ - Sao lưu tự động và thủ công cho các kênh LN. Vui lòng đọc thêm về cách sử dụng tính năng này trên trang Zeus Docs.
- _Express Graph Sync_ - Ứng dụng Zeus sẽ tải xuống biểu đồ dữ liệu tin đồn LN từ máy chủ chuyên dụng, để đồng bộ hóa nhanh hơn và tốt hơn, cung cấp các đường dẫn thanh toán tốt nhất. Bạn cũng có thể chọn xóa dữ liệu biểu đồ trước đó khi khởi động.
- _Peers_ - phần quản lý các peer neutrino và peer 0-conf. Nếu bạn gặp sự cố với đồng bộ ban đầu, các kênh không trực tuyến, là do thiết bị của bạn có độ trễ cao với peer neutrino đã cấu hình. Hãy thử chuyển đổi danh sách các peer ưa thích hoặc thêm peer cụ thể mà bạn biết có độ trễ tốt hơn để đồng bộ. Các máy chủ neutrino nổi tiếng là:



 - btcd1.lnolymp.us | btcd2.lnolymp.us - dành cho khu vực Hoa Kỳ
 - sg.lnolymp.us - dành cho khu vực Châu Á
 - btcd-Mainnet.lightning.computer - dành cho khu vực Hoa Kỳ
 - uswest.blixtwallet.com (Seattle) - dành cho khu vực Hoa Kỳ
 - europe.blixtwallet.com (Đức) - dành cho khu vực EU
 - asia.blixtwallet.com - dành cho khu vực Châu Á
 - node.eldamar.icu - dành cho khu vực Hoa Kỳ
 - noad.sathoarder.com - dành cho khu vực Hoa Kỳ
 - bb1.breez.technology | bb2.breez.technology - dành cho khu vực Hoa Kỳ
 - neutrino.shock.network - khu vực Hoa Kỳ



- _Nhật ký LND_ - công cụ rất hữu ích để gỡ lỗi các sự cố nút LN của bạn và kiểm soát sâu hơn những gì đang diễn ra ở cấp độ kỹ thuật hơn.
- _Cài đặt nâng cao_ - nhiều công cụ hơn để kiểm soát việc sử dụng nút LND của bạn:



 - _Chế độ tìm đường_ - bimodal hoặc apriori, cách tìm đường đi tốt hơn cho các khoản thanh toán LN của bạn và cũng thiết lập lại thông tin định tuyến trước đó. Vui lòng đọc các hướng dẫn rất hay sau đây về tìm đường: [Tìm đường](https://docs.lightning.engineering/lightning-network-tools/LND/pathfinding) - của Docs Lightning Engineering và [Tìm đường thanh toán LN](https://voltage.cloud/blog/lightning-network-faq/understanding-payment-pathfinding-between-nodes-on-lightning-network/) - của Voltage
 - _Persistent LND_ - kích hoạt chế độ này nếu bạn muốn dịch vụ LND chạy liên tục ở chế độ nền và giữ cho nút của bạn trực tuyến 24/7. Điều này rất hữu ích nếu bạn sử dụng Zeus làm PoS trong một cửa hàng nhỏ hoặc bạn nhận được nhiều mẹo LN hơn LN Address.
 - _Quét lại ví_ - tùy chọn này sẽ kích hoạt khi khởi động lại quá trình quét toàn bộ tất cả các giao dịch trên chuỗi của Wallet của bạn. Chỉ kích hoạt tùy chọn này trong trường hợp bạn thiếu một số giao dịch trong Wallet của mình. Nhiệm vụ quét lại sẽ mất thời gian, vài phút nên hãy kiên nhẫn và luôn kiểm tra nhật ký để xem thêm chi tiết về tiến trình.
 - _Compact Database_ - tùy chọn này rất hữu ích nếu ứng dụng Zeus của bạn chiếm nhiều dung lượng thiết bị (xem chi tiết ứng dụng trong cài đặt thiết bị của bạn). Nếu bạn có nhiều hoạt động sử dụng Zeus, tôi khuyên bạn nên thực hiện nén này thường xuyên hơn. Khi bạn thấy rằng mình có hơn 1-1,5 GB dữ liệu cho ứng dụng Zeus, hãy thực hiện nén. Quá trình này sẽ khởi động lại và mất một thời gian, vì vậy hãy kiên nhẫn.
 - _Xóa các tệp Neutrino_ - tùy chọn này để xóa các tệp neutrino (bằng cách khởi động lại) sẽ giảm đáng kể việc sử dụng bộ nhớ dữ liệu. Việc giảm việc sử dụng dữ liệu cũng có tác động lớn đến việc sử dụng pin, giảm việc sử dụng pin, đặc biệt nếu bạn sử dụng Zeus ở chế độ liên tục.


**D - Thông tin nút**


Trong phần này, bạn sẽ tìm thấy thêm thông tin chi tiết về trạng thái của nút Zeus của bạn như sau:



- Biệt danh - ID nút ngắn
- Khóa công khai - khóa công khai đầy đủ cho nút của bạn, bắt buộc các nút khác phải tìm đường dẫn đến nút của bạn. Hãy nhớ rằng khóa công khai này KHÔNG hiển thị trên LN Explorers thông thường (Mempool, Amboss, 1ML, v.v.). Khóa công khai này CHỈ có thể truy cập được thông qua các kênh và đối tác LN được kết nối của bạn.
- Phiên bản triển khai LN
- Phiên bản ứng dụng Zeus
- Trạng thái Synced to chain và Synced to graph - rất quan trọng, hiển thị trạng thái chính xác của nút của bạn. Nếu hai trạng thái này không hiển thị "true" thì có nghĩa là nút của bạn vẫn đang đồng bộ hoặc đang gặp một số vấn đề khi đồng bộ. Vì vậy, bạn nên xem nhật ký LND của mình hoặc đợi thêm một chút.
- Chiều cao khối và Hash - hiển thị khối cuối cùng và Hash mà nút của bạn đã nhìn thấy và đồng bộ hóa.


**E - Thông tin mạng**


Phần này hiển thị thêm thông tin chi tiết về trạng thái chung của Lightning Network, được trích xuất từ dữ liệu đồng bộ biểu đồ của bạn: số kênh công cộng khả dụng, số nút, số kênh zombie (ngoại tuyến hoặc chết), đường kính biểu đồ, mức độ trung bình và tối đa cho biểu đồ.


Dữ liệu thông tin này có thể hữu ích để gỡ lỗi hoặc chỉ dùng cho mục đích thống kê.


**F - Tia sét Address**


Trong phần này, người dùng có thể thiết lập quyền tự quản của riêng mình LN Address @zeuspay.com.


ZEUS PAY tận dụng các băm tiền ảnh do người dùng tạo, hóa đơn HODL và chương trình chứng thực Zaplocker Nostr để cho phép người dùng không trực tuyến 24/7 nhận thanh toán vào một Address sét tĩnh. Người dùng chỉ cần đăng nhập vào ví ZEUS của họ trong vòng 24 giờ để yêu cầu thanh toán, nếu không, chúng sẽ được trả lại cho người gửi.


Nếu bạn kích hoạt “chế độ liên tục”, mọi khoản thanh toán cho LN Address của bạn sẽ được nhận ngay lập tức.


Tìm hiểu về cách thức thanh toán [Zaplocker](https://github.com/supertestnet/zaplocker#how-it-works) và thông tin thêm về [Phí ZeusPay tại đây](https://docs.zeusln.app/lightning-Address/fees).


**G - Địa chỉ Onchain**


Trong phần này, bạn có thể tham khảo địa chỉ onchain đã tạo của mình để kiểm soát tiền tốt hơn


**H - Liên hệ**


Một danh bạ mới đã được giới thiệu trong Zeus v 0.8.0 mà bạn có thể sử dụng để nhanh chóng gửi tiền cho bạn bè và gia đình, đồng thời có khả năng nhập danh bạ từ Nostr.


Chỉ cần nhập vào Nostr npub hoặc NIP-05 Address có thể đọc được bằng con người, và ZEUS sẽ truy vấn Nostr cho tất cả các liên hệ của bạn. Từ đó, bạn có thể gửi thanh toán nhanh cho một liên hệ hoặc nhập tất cả hoặc chọn các liên hệ vào sổ liên lạc cục bộ của bạn./<


Sau đây là video ngắn về cách cấu hình và sử dụng danh bạ Zeus của bạn:


**I - Công cụ**


Ở đây chúng tôi có nhiều tiểu mục với nhiều công cụ hơn:



- _Tài khoản_ - tại đây bạn có thể nhập tài khoản/ví bên ngoài, ví Cold, ví Hot để kiểm soát hoặc sử dụng làm nguồn tài trợ bên ngoài cho kênh nút Zeus của bạn. Tính năng này vẫn đang trong giai đoạn thử nghiệm.
- _Tăng tốc giao dịch_ - Tính năng này có thể hữu ích khi bạn có giao dịch bị kẹt trong Mempool và muốn tăng phí. Bạn sẽ cần cung cấp đầu ra giao dịch từ chi tiết giao dịch và chọn phí mới mong muốn mà bạn muốn sử dụng. Phải cao hơn phí trước đó và yêu cầu bạn phải có nhiều tiền hơn trong Wallet trên chuỗi của mình.


![Image](assets/en/05.webp)


Bạn phải đến giao dịch đang chờ xử lý và sao chép điểm ra txid. Sau đó đến phần này và dán nó, sau đó chọn mức phí mới mà bạn muốn sử dụng để tăng nó. Nó sẽ bật lên một màn hình mới với các mức phí được đề xuất tại thời điểm đó hoặc bạn có thể đặt một mức phí tùy chỉnh. Hãy nhớ rằng PHẢI cao hơn mức phí trước đó.


Luôn tốt hơn khi giữ UTXO với tối đa 100k Sats trong Zeus onchain Wallet của bạn để có thể sử dụng nó để tăng phí khi cần thiết.



- _Ký hoặc xác minh_ - Với tính năng này, bạn có thể ký một tin nhắn cụ thể bằng khóa Wallet của mình. Cũng có thể được sử dụng để xác minh tin nhắn để chứng minh rằng tin nhắn đó đến từ một khóa Wallet cụ thể.
- _Công cụ chuyển đổi tiền tệ_ - một công cụ đơn giản để tính tỷ giá chuyển đổi giữa BTC và các loại tiền tệ pháp định khác.


**J - Hàng hóa và Hỗ trợ**


Tại đây bạn sẽ tìm thấy thêm thông tin và liên kết về Zeus, cửa hàng trực tuyến, nhà tài trợ, phương tiện truyền thông xã hội.


**K - Trợ giúp**


Trong phần cuối cùng này, bạn sẽ tìm thấy các liên kết đến trang tài liệu của Zeus, các vấn đề trên Github (nếu bạn muốn đăng lỗi hoặc yêu cầu trực tiếp tới nhà phát triển ứng dụng), hỗ trợ qua email.



### BƯỚC 2 - BẮT ĐẦU SỬ DỤNG ZEUS NODE



Hãy nhớ rằng, Zeus chủ yếu được sử dụng như LN Wallet, để thanh toán dễ dàng và nhanh chóng qua LN. Chắc chắn, nó cũng chứa Wallet trên chuỗi, nhưng nó chỉ nên được sử dụng để mở/đóng kênh LN chứ không phải để thanh toán thông thường cho một cốc cà phê.


Vui lòng đọc hướng dẫn khác của tôi về [cách trở thành ngân hàng của riêng bạn bằng cách sử dụng 3 cấp độ của Stash](https://darth-coin.github.io/beginner/be-your-own-bank-en.html).


Hiện tại người dùng có 2 cách để bắt đầu sử dụng Zeus:



- Ngay trên LN, sử dụng kênh 0-conf từ Olympus LSP
- Trước tiên hãy gửi tiền vào Wallet trên chuỗi và sau đó mở kênh LN bình thường với đối tác mà bạn mong muốn.


#### Phương pháp A - Sử dụng Olympus LSP


Đây là cách rất dễ dàng và trực tiếp để đưa người dùng LN mới lên Zeus. Đó có thể là người dùng Bitcoin hoàn toàn mới không có Sats nào, được bạn bè đưa lên hoặc là một thương gia mới bắt đầu với khoản thanh toán LN đầu tiên của mình.


Theo mặc định, Zeus sẽ sử dụng LSP riêng của mình, Olympus. Nhưng sau đó bạn cũng có thể chuyển sang các LSP khác hỗ trợ giao thức 0-conf này để mở kênh.


Chỉ cần tạo Invoice trên Zeus của bạn (nhập số lượng và nhấp vào nút “yêu cầu”), bạn sẽ có thể nhận được Sats ngay lập tức.


Invoice của bạn generate sẽ được [gói](https://docs.zeusln.app/lsp/wrapped-invoices) và bạn sẽ được cung cấp các khoản phí liên quan đến dịch vụ nếu chúng được thanh toán. Invoice được gói này chứa các gợi ý về tuyến đường đến nút Zeus của bạn, do đó LSP có thể tìm nút mới của bạn và mở một kênh với số tiền mới mà bạn đang gửi.


![Image](assets/en/06.webp)


![Image](assets/en/07.webp)


Để nhận được kênh LN từ LSP với số tiền bạn muốn nhận lần đầu tiên, Invoice này phải được thanh toán từ LN Wallet khác và đợi vài phút cho đến khi LSP mở kênh tới nút Zeus của bạn, trừ phí và chuyển số tiền còn lại của khoản thanh toán về phía kênh của bạn.


Tất cả những gì bạn phải làm là thanh toán Invoice được tạo cho bạn trong ZEUS bằng một Wallet sét khác và kênh của bạn sẽ mở ngay lập tức. [Vui lòng tham khảo phí Zeus LSP](https://docs.zeusln.app/lsp/fees).


Một lợi ích khác khi trả tiền cho một kênh là định tuyến không mất phí. Điều đó có nghĩa là khi định tuyến thanh toán, lần chuyển đầu tiên qua OLYMPUS by ZEUS sẽ không mất phí định tuyến. Lưu ý rằng các lần chuyển tiếp vượt ra ngoài OLYMPUS by ZEUS vẫn sẽ tính phí bạn.


Khi kênh đã sẵn sàng, hãy nhấp vào nút bên phải ở cuối màn hình để hiển thị các kênh Zeus.


![Image](assets/en/08.webp)


Và bạn sẽ thấy một kênh như thế này, hiển thị số dư kênh của bạn:


![Image](assets/en/09.webp)


Bạn sẽ chi tiêu nhiều hơn từ kênh này, bạn sẽ có nhiều thanh khoản vào hơn. Bạn sẽ nhận được nhiều Sats hơn vào kênh này, bạn sẽ có ít không gian thanh khoản vào hơn.


Sau đây là một bản trình bày trực quan đơn giản (do Rene Pickhardt thực hiện) về cách thức hoạt động của kênh LN:


Vào thời điểm này, hãy xem xét màn hình demo của các kênh, hãy nhấp vào tên kênh và bạn sẽ thấy thêm thông tin chi tiết về kênh đó.


Bạn có một kênh duy nhất với Olympus, tổng dung lượng là 490 000 Sats, với số dư là 378k Sats ở phía bạn và 88k Sats ở phía Olympus. Điều đó có nghĩa là bạn có thể nhận được tối đa 88k Sats trong cùng một kênh.


Nếu bạn cần nhận hơn 88k Sats (thanh khoản đầu vào khả dụng trong trường hợp này), hãy nói rằng 500k Sats khác, chỉ cần tạo một LN Invoice mới với số lượng đó, sẽ kích hoạt yêu cầu kênh mới đến Olympus LSP. Vì vậy, bạn sẽ nhận được kênh thứ 2.


Đó là lý do tại sao, để tránh phải trả thêm phí khi mở nhiều kênh, bạn nên mở kênh lớn hơn lần đầu tiên, chẳng hạn như 1-2M Sats. Sau khi mở, bạn có thể hoán đổi sang phần onchain của Sats đó, chẳng hạn như 50%, bằng bất kỳ dịch vụ hoán đổi bên ngoài nào được mô tả trong hướng dẫn này.


Khi bạn hoán đổi từ kênh đó, giả sử là 50% và lấy lại Sats vào Zeus onchain Wallet của riêng bạn, bạn đã sẵn sàng chuyển sang phương pháp tiếp theo để mở kênh mới - từ số dư onchain.


#### Phương pháp B - Sử dụng số dư onchain của bạn


Với phương pháp này, bạn có thể mở kênh hướng đến bất kỳ nút LN nào khác, bao gồm cả Olympus LSP. Nhưng nếu bạn đã có kênh với Olympus thì nên mở thêm với một nút khác để có độ tin cậy cao hơn và cũng có thể sử dụng MPP (thanh toán nhiều phần).


![Image](assets/en/10.webp)


Trên đây là ví dụ về việc thanh toán LN Invoice bằng MPP. Như bạn có thể thấy ở cuối màn hình, bạn có "cài đặt" và đang mở một trang thả xuống với nhiều chi tiết hơn cho khoản thanh toán mà bạn sắp thực hiện. Trong màn hình đó, nếu bạn mở ít nhất 2 kênh, tính năng MPP sẽ được BẬT theo mặc định. Ngoài ra, bạn có thể kích hoạt AMP (đa đường dẫn nguyên tử) và thiết lập các phần cụ thể mà bạn muốn. Đây là một tính năng mạnh mẽ!


Đối với một nút riêng như Zeus, tôi khuyên bạn nên có 2-3 kênh tốt (tối đa 4-5), với các LSP tốt và tính thanh khoản tốt để đáp ứng mọi nhu cầu thanh toán hoặc nhận Sats qua LN. [Xem thêm lời khuyên về tính thanh khoản của nút LN trong hướng dẫn này](/nodes/managing-lightning-node-liquidity-en.html). Ngoài ra, đây là một [hướng dẫn chung khác về tính thanh khoản của LN](https://Bitcoin.design/guide/how-it-works/liquidity/) từ nhóm Thiết kế Bitcoin.


Tôi biết rằng việc lựa chọn đúng các đối tác không phải là một nhiệm vụ dễ dàng, ngay cả với những người dùng có kinh nghiệm. [Vì vậy, tôi sẽ cung cấp cho bạn một số tùy chọn để bắt đầu](https://github.com/ZeusLN/zeus/discussions/2265), đây là các nút đối tác mà tôi đã tự mình thử nghiệm bằng Zeus (tôi đã cố gắng chỉ kết nối với các nút LND để tránh các vấn đề không tương thích)


Đây cũng là danh sách các node peer được xác thực cho Zeus. Nếu bạn biết node peer nào tốt, bạn có thể thêm chúng vào danh sách đó.


Bạn có thể mở kênh trong Zeus bằng cách vào chế độ xem Kênh bằng cách nhấp vào biểu tượng kênh ở góc dưới bên phải của chế độ xem chính, sau đó nhấn biểu tượng + ở góc trên bên phải.


![Image](assets/en/11.webp)


Nếu bạn muốn mở một kênh với một nút cụ thể, hãy nhấp vào góc trên cùng (A) để quét mã QR nodeID của nút (trên Mempool, Amboss, 1ML, bạn có thể lấy mã QR đó) và tất cả thông tin chi tiết của đối tác sẽ được điền.


LỜI NHẮC NHỞ:


- Nút nhúng Zeus không sử dụng dịch vụ Tor! Vì vậy, vui lòng không thử mở kênh với các nút nằm dưới Tor! Bạn đang tự gây hại cho mình nhiều hơn là tăng thêm quyền riêng tư. Tor đối với LN không cung cấp thêm quyền riêng tư mà chỉ tăng thêm rắc rối.
- hãy lựa chọn đồng nghiệp của bạn một cách khôn ngoan, tốt hơn là nên là LSP tốt, các nút định tuyến tốt, chứ không phải các nút pleb ngẫu nhiên có thể đóng kênh của bạn và không thể cung cấp thanh khoản tốt. [Ở đây tôi đã viết một hướng dẫn chuyên dụng](https://darth-coin.github.io/nodes/managing-lightning-node-liquidity-en.html) về thanh khoản và ví dụ về các nút.


Nếu bạn nhấp trực tiếp vào nút “Mở kênh tới Olympus”, bạn sẽ điền vào các trường bắt buộc để mở kênh tới [OLYMPUS của ZEUS](https://Mempool.space/lightning/node/031b301307574bbe9b9ac7b79cbe1700e31e544513eae0b5d7497483083f99e581).


Không giống như các kênh LSP trả phí, kênh của bạn sẽ yêu cầu xác nhận On-Chain, sử dụng tiền trên chuỗi của bạn (bạn có thể chọn từ UTXO của mình trong chế độ xem kênh mở); kênh sẽ không mở ngay lập tức. Vui lòng tham khảo trước các khoản phí Mempool thực tế và điều chỉnh chúng cho phù hợp, tùy thuộc vào tốc độ bạn muốn mở kênh đó.


Trước khi nhấn nút để mở kênh, hãy trượt xuống các tùy chọn nâng cao:


![Image](assets/en/12.webp)


Bạn cũng cần đảm bảo rằng kênh không được thông báo (riêng tư). Theo mặc định, tùy chọn này bị tắt đối với các kênh được thông báo. Tùy chọn này không được khuyến nghị kích hoạt cho nút nhúng Zeus, chỉ hữu ích khi bạn sử dụng Zeus với nút từ xa của mình, như một nút định tuyến công khai.


Không giống như các kênh LSP trả phí, bạn sẽ không được hưởng lợi từ việc định tuyến không mất phí khi mở kênh bằng phương pháp này.


Và xong, chỉ cần nhấp vào nút “Mở kênh”, đợi giao dịch được xác nhận bởi thợ đào. Khi kênh mở, bạn có thể giao dịch theo ý muốn với Sats từ các kênh của mình.


Hãy nhớ rằng các kênh này sẽ có toàn bộ số dư ở phía BẠN, vì vậy bạn sẽ không có thanh khoản vào. Như tôi đã nói trước đó, hãy đổi hoặc chi một số Sats để mua đồ thay vì LN để "tạo thêm không gian" để nhận.


Hãy nghĩ về các kênh LN của bạn như một cốc nước. Bạn đổ một ít nước (Sats) vào một cốc rỗng (kênh của bạn) cho đến khi bạn đổ đầy. Bạn không thể đổ thêm nước cho đến khi bạn uống một ít (chi tiêu / trao đổi). Khi cốc gần hết, hãy đổ thêm nước (Sats) vào bằng cách sử dụng trao đổi. [Đọc thêm về các dịch vụ trao đổi bên ngoài tại đây](https://darth-coin.github.io/nodes/lightning-submarine-swaps-en.html).


Ngoài ra còn có các dịch vụ LSP khác bán cho bạn các kênh inbound: LNBig hoặc Bitrefill. Tôi nghĩ còn nhiều dịch vụ như thế này nữa nhưng hiện tại tôi không nhớ hết.


Vì vậy, nếu bạn thực sự cần một kênh LN trống (số dư là 100% ở phía ngang hàng ngay từ đầu), để nhận nhiều khoản thanh toán hơn mức bạn có thể xử lý trên các kênh hiện đã đầy của mình, thì đây có thể là một lựa chọn rất tốt. Bạn sẽ trả một khoản phí cụ thể để mở các kênh này và bạn sẽ có nhiều không gian đến.



## MẸO VÀ THỦ THUẬT


### Giới hạn dự trữ đến


Hiện tại, do một số hạn chế của mã LN nên không thể nhận được chính xác số tiền được hiển thị trong “Inbound”. Luôn nhớ rằng bạn nên lập hóa đơn với số tiền ít hơn một chút, tương ứng với số tiền “Channel Local Reserve”.


![Image](assets/en/13.webp)


Như bạn có thể thấy trong hình ảnh trên, “inbound” hiển thị rằng tôi vẫn có thể nhận được 5101 Sats, nhưng thực tế là tại thời điểm này không thể nhận được nhiều hơn. Và bạn có thể thấy rằng đó là cùng một số lượng với “Local reserve”.


Vì vậy, hãy nhớ rằng khi bạn lập hóa đơn để nhận, hãy xem xét tính thanh khoản của kênh và khấu trừ dự trữ cục bộ khỏi số tiền đó nếu bạn muốn đẩy số tiền phải thu lên mức giới hạn.


### Lời khuyên nhanh cho người dùng mới bắt đầu với Zeus node:



- Hãy nắm bắt đúng các kênh mới của bạn.


Ví dụ, nếu bạn biết rằng bạn sẽ nhận được trong một tuần, chẳng hạn như 1M Sats, hãy mở một kênh 2M Sats và hoán đổi sang Wallet trên chuỗi hoặc sang một tài khoản LN lưu ký (tạm thời) khác 50-60% thanh khoản ra của bạn. Luôn chuẩn bị sẵn sàng với nhiều thanh khoản hơn. Khi bạn cần nhiều thanh khoản hơn trong các kênh Zeus của mình, bạn có thể chuyển nó trở lại từ các tài khoản lưu ký.


Nếu bạn biết rằng bạn sẽ gửi 500k Sats/tuần, thì hãy mở một kênh Sats 1M. Theo cách này, bạn vẫn sẽ có một khoản dự trữ cho đến khi bạn lấp đầy lại.



- Nếu bạn là một thương gia và bạn sẽ luôn nhận được nhiều hơn số tiền bạn chi tiêu thường xuyên, hãy mua một kênh inbound chuyên dụng. Đây là cách rẻ nhất. Bạn trả một khoản phí tối thiểu và bạn sẽ có một kênh "trống".



- Đừng mở các kênh nhỏ vô nghĩa 50-100-300-500k Sats. Bạn sẽ lấp đầy chúng trong vài ngày, ngay cả khi bạn chỉ sử dụng chúng cho zap. Mở các kênh lớn hơn và khác nhau, KHÔNG chỉ một kênh.


Khi bạn mở một kênh lớn hơn, bạn luôn có thể sử dụng hoán đổi tàu ngầm bên ngoài để chuyển Sats vào ví onchain của bạn (bao gồm cả trở lại Zeus onchain). Giữ cân bằng giữa thanh khoản vào và ra là tốt và bạn cũng có thể "tái sử dụng" những Sats đó để mở thêm nhiều kênh nếu bạn thích.


### Invoice được bọc


Nếu bạn muốn thêm quyền riêng tư khi nhận, bạn có thể sử dụng phương pháp "gói Invoice". Lưu ý: để có thể thực hiện việc này, bạn cần một kênh có Olympus LSP. Hóa đơn được gói sẽ "ẩn" đích cuối cùng (nút Zeus của bạn) và hiển thị nút LSP của bạn làm đích đến cho người trả tiền.


Để có được Invoice đã bọc, hãy vào màn hình bàn phím chính, nhập số tiền và nhấn yêu cầu. Sẽ hiển thị mã QR bình thường cho Invoice của bạn. Bây giờ, hãy nhấp vào nút “X” ở trên cùng bên phải và bạn sẽ được chuyển hướng đến nhiều tùy chọn hơn cho Invoice.


![Image](assets/en/14.webp)


Bây giờ bạn sẽ phải kích hoạt tùy chọn đó ở trên cùng “Enable LSP” và nhấn nút “Create Invoice”. Tùy chọn đó sẽ tạo Invoice đã được gói lại và hãy nhớ rằng, sẽ tính một khoản phí nhỏ.


### Hóa đơn có gợi ý lộ trình


Đây là một tính năng rất hữu ích nếu bạn muốn quản lý tính thanh khoản của nhiều kênh đến. Trên thực tế, bạn có thể chỉ ra kênh đến nào bạn muốn nhận Sats từ Invoice.


Tính năng này cũng có thể được sử dụng để cân bằng lại vòng tròn khi bạn muốn chuyển thanh khoản từ kênh đầy sang kênh cạn kiệt khác.


Làm thế nào để tạo Invoice với gợi ý lộ trình?



- Trên màn hình chính, trượt ngăn kéo LN sang bên phải và nhấp vào "Nhận"
- Trong thiết lập Invoice, hãy đến phần dưới cùng và kích hoạt nút "Insert route hints", sau đó chọn tab "Custom". Nó sẽ mở một màn hình với tất cả các kênh có sẵn của bạn. Chọn kênh bạn muốn nhận.
- Điền đầy đủ các thông tin khác của Invoice, số tiền, ghi chú, v.v. và nhấp vào "tạo Invoice".
- Thanh toán Invoice sẽ đưa Sats vào kênh được chỉ định.


Nếu bạn muốn tự thanh toán cho mình khoản Invoice đó (tái cân bằng tuần hoàn), khi bạn thanh toán từ cùng một nút Zeus, trên màn hình thanh toán, hãy chọn kênh gửi đi (kênh có tính thanh khoản cao hơn) mà bạn muốn sử dụng để gửi thanh toán.


### Thanh toán bằng Keysend


Keysend là một tính năng bị đánh giá thấp của LN và người dùng nên sử dụng nó thường xuyên hơn.


[Keysend](https://docs.lightning.engineering/lightning-network-tools/LND/send-messages-with-keysend) cho phép người dùng trong Lightning Network gửi thanh toán cho người khác, trực tiếp đến khóa công khai của họ, miễn là nút của họ có kênh công khai và đã bật keysend. Keysend không yêu cầu người nhận thanh toán phải phát hành Invoice.


Vậy bạn có thể làm điều đó với Zeus như thế nào?


Chỉ cần quét hoặc sao chép nodeID đích (hoặc sử dụng danh bạ Zeus để lưu các node đích thông thường của bạn dưới dạng danh bạ) và sau đó từ màn hình Zeus chính, nhấp vào nút "Gửi". Trong màn hình đó, sau đó dán nodeID hoặc chọn từ danh bạ của bạn.


Nhập số lượng Sats, tin nhắn nếu cần (vâng, bạn cũng có thể sử dụng nó như một cuộc trò chuyện bí mật qua LN) và nhấp vào nút "Gửi". Xong!


![Image](assets/en/15.webp)


Nếu bạn có kênh trực tiếp với đối tác đích, sẽ KHÔNG mất phí.


Nếu bạn không có kênh trực tiếp với đối tác đích, thì thanh toán keysend sẽ thanh toán phí như một khoản thanh toán LN Invoice thông thường, được định tuyến trên một đường dẫn thông thường như bất kỳ khoản thanh toán nào khác. Chỉ có điều, hãy nhớ rằng, nó sẽ không còn dấu vết nào như một khoản thanh toán LN Invoice.


## Kết luận


Tôi khuyên bạn nên đọc hướng dẫn tiếp theo [Cách sử dụng Zeus nâng cao](https://darth-coin.github.io/wallets/zeus-node-advanced-usage-en.html) để biết thêm hướng dẫn và trường hợp sử dụng.


Và… thế là xong! Từ giờ trở đi, bạn chỉ cần sử dụng Zeus Node như một BTC/LN Wallet thông thường trên thiết bị di động của mình. Giao diện người dùng khá đơn giản và dễ sử dụng, trực quan cho mọi loại người dùng, tôi không nghĩ mình phải nhập thêm thông tin chi tiết về cách thực hiện và nhận thanh toán.


Tóm lại, đây là biểu đồ so sánh quyền riêng tư:


![Image](assets/en/16.webp)