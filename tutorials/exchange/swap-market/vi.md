---
name: SwapMarket
description: Bộ tổng hợp dịch vụ hoán đổi Bitcoin và Lightning
---

![cover](assets/cover.webp)



Việc chuyển tiền giữa Bitcoin, on-chain và Lightning Network thường yêu cầu mở thủ công các kênh Lightning (mang tính kỹ thuật và tốn kém), hoặc sử dụng các nền tảng hoán đổi tập trung có KYC. SwapMarket cung cấp một giải pháp thay thế: hoán đổi nguyên tử không cần tin cậy thông qua các nhà cung cấp cạnh tranh, không cần KYC.



Đổi mới: mặc dù nhà cung cấp chỉ là trung gian, HTLC (*Hợp đồng Khóa Thời gian Hash*) đảm bảo về mặt toán học rằng tiền của bạn vẫn nằm trong tầm kiểm soát của bạn. Việc kết hợp nhiều nhà cung cấp (Boltz, ZEUS Swaps, Eldamar, Middle Way) tạo ra sự cạnh tranh về giá. Interface là nền tảng web mã nguồn mở, có thể tự lưu trữ.



## SwapMarket là gì?



SwapMarket, một nền tảng tổng hợp mã nguồn mở được ra mắt vào năm 2024, hoạt động như một công cụ so sánh các nhà cung cấp dịch vụ hoán đổi Bitcoin/Lightning. Người dùng ngay lập tức so sánh các điều kiện (phí, thanh khoản, hạn mức) và chọn nhà cung cấp tối ưu.



### Kiến trúc kỹ thuật



**Phía máy khách front-end**: 100% ứng dụng phía máy khách (Ứng dụng web fork Boltz) được lưu trữ trên GitHub Pages. Mã chạy trên trình duyệt mà không cần máy chủ back-end. Lịch sử được lưu trữ cục bộ (cookie/cache). Mã nguồn công khai và có thể kiểm tra.



**Khám phá nhà cung cấp**: Danh sách được mã hóa cứng trong `src/configs/mainnet.ts`. Các nhà cung cấp mới được thêm vào thông qua Pull Request hoặc email.



**Hệ thống backend độc lập**: Mỗi nhà cung cấp vận hành hệ thống backend Boltz riêng. Giao diện này sẽ truy vấn API theo thời gian thực để so sánh báo giá ngay lập tức.



**Hợp đồng hoán đổi nguyên tử HTLC**: Hợp đồng khóa thời gian Hash đảm bảo tính nguyên tử: hoặc hợp đồng hoán đổi được thực hiện, hoặc mỗi bên thu hồi được tiền của mình. Rủi ro đối tác được loại bỏ về mặt toán học.



### Triết lý



SwapMarket giảm thiểu sự tập trung bằng cách tạo ra sự cạnh tranh giữa các nhà cung cấp về phí và thanh khoản. Không cần KYC, mã nguồn mở tự lưu trữ, tăng cường số lượng nhà điều hành độc lập để tránh các điểm lỗi đơn lẻ.



## Các tính năng chính



### Thị trường nhà cung cấp



Giao diện hiển thị tất cả các nhà cung cấp đang hoạt động: tên nhà cung cấp, mức phí áp dụng (phần trăm và/hoặc cố định), số tiền tối thiểu/tối đa khả dụng và các loại hoán đổi được hỗ trợ. Ứng dụng trực tiếp truy vấn API của từng nhà cung cấp được tham chiếu trong tệp cấu hình để lấy báo giá theo thời gian thực. Sự cạnh tranh giữa các nhà cung cấp đảm bảo mức giá tối ưu, thường khoảng 0,5% cho các hoán đổi tiêu chuẩn.



### Hoán đổi hai chiều



**Swap-in (on-chain → Lightning)**: Chuyển đổi on-chain BTC thành Lightning satoshi. Trường hợp sử dụng: cung cấp năng lượng cho wallet Lightning di động, nhận dung lượng đầu vào trên một nút hoặc có thanh khoản tức thời.



**Hoán đổi (Lightning → on-chain)**: Chuyển đổi Lightning satoshi sang on-chain BTC. Trường hợp sử dụng: rút hết Lightning wallet sang ví lạnh hoặc cân bằng lại thanh khoản giữa các lớp.



### An toàn và phục hồi



**Hoán đổi nguyên tử Trustless**: HTLC đảm bảo rằng việc trao đổi hoặc được hoàn tất hoàn toàn, hoặc mỗi bên sẽ thu hồi được cổ phần của mình. Rủi ro đối tác được loại bỏ về mặt toán học.



**Cơ chế hoàn trả**: Mỗi lần hoán đổi đều có khóa thời gian. Nếu hoán đổi thất bại, tiền sẽ tự động được hoàn trả sau khi hết hạn. Người dùng luôn có quyền lấy lại bitcoin của mình.



**Khóa khôi phục**: SwapMarket cho phép bạn xuất khóa khôi phục cho các giao dịch hoán đổi đang diễn ra. Trong trường hợp có sự cố, các khóa này có thể được sử dụng để hoàn tất hoặc hủy giao dịch hoán đổi từ bất kỳ thiết bị nào.



## Cài đặt và truy cập



### Web Interface



SwapMarket không yêu cầu cài đặt. Truy cập qua trình duyệt bằng cách truy cập https://swapmarket.github.io. Để bảo mật tối đa, hãy sử dụng Brave, Firefox với tiện ích mở rộng chống theo dõi hoặc LibreWolf. Trình duyệt Tor được khuyến nghị để ẩn danh mạng.



Không cần đăng ký, email hoặc xác minh danh tính.



### Tự lưu trữ (tùy chọn)



Đối với người dùng kỹ thuật muốn loại bỏ mọi sự phụ thuộc vào tên miền GitHub Pages chính thức, SwapMarket có thể được chạy cục bộ:



**Thông qua npm**:


```
git clone https://github.com/SwapMarket/swapmarket.github.io.git
cd swapmarket.github.io
npm install
npm run dev
```



**Thông qua Docker**:


```
docker run -p 3000:80 ghcr.io/swapmarket/swapmarket:latest
```



Ứng dụng sẽ có thể truy cập tại `http://localhost:3000`. Tự lưu trữ đảm bảo quyền kiểm soát hoàn toàn giao diện, loại bỏ nguy cơ kiểm duyệt tên miền chính thức và cho phép kiểm tra mã nguồn trước khi thực thi.



### Cấu hình ban đầu



**Wallet Lightning**: Đảm bảo bạn có thiết bị wallet Lightning đang hoạt động (Phoenix, Zeus, BlueWallet, v.v.). Đối với việc đổi thiết bị, bạn sẽ cần hóa đơn Lightning generate. Đối với việc đổi thiết bị, bạn sẽ cần thanh toán hóa đơn Lightning.



**Wallet on-chain**: Đối với giao dịch hoán đổi, bạn cần có wallet Bitcoin on-chain để gửi tiền. Đối với giao dịch hoán đổi, hãy chuẩn bị địa chỉ nhận Bitcoin.



**Cấu hình tùy chọn**: SwapMarket lưu trữ lịch sử giao dịch và tùy chọn hoán đổi trong cookie của trình duyệt. Không cần tạo tài khoản.



## Truy cập vào cài đặt và Khóa cứu hộ



Trước khi thực hiện giao dịch hoán đổi đầu tiên, chúng tôi đặc biệt khuyên bạn nên tải xuống **Khóa Cứu Hộ**. Khóa khẩn cấp này cho phép bạn khôi phục tiền trong trường hợp xảy ra sự cố kỹ thuật hoặc mất quyền truy cập vào thiết bị.



### Tham số truy cập



Từ trang chính của SwapMarket, nhấp vào biểu tượng bánh răng (⚙️) ở góc trên bên phải của giao diện, bên cạnh biểu mẫu hoán đổi.



![Accès aux paramètres](assets/fr/01.webp)



### Cài đặt trang



Trang Cài đặt mở ra, hiển thị một số tùy chọn cấu hình:





- Mệnh giá**: Lựa chọn BTC hoặc sats
- Dấu phân cách thập phân**: Dấu phân cách thập phân (, hoặc .)
- Thông báo âm thanh/trình duyệt**: Thông báo âm thanh và trình duyệt
- Khóa cứu hộ**: Tải xuống khóa phục hồi
- Nhật ký**: Xem, tải xuống hoặc xóa nhật ký



![Page Settings](assets/fr/02.webp)



### Tải xuống Khóa cứu hộ



Nhấp vào nút **Tải xuống** bên cạnh "Khóa cứu hộ".



**Những điểm quan trọng**:




- Chìa khóa cứu hộ là **chìa khóa khẩn cấp một cửa** hoạt động cho tất cả các lần hoán đổi trong tương lai của bạn
- Giữ chìa khóa này ở nơi **an toàn và lâu dài** (trình quản lý mật khẩu, két an toàn kỹ thuật số)
- Trong trường hợp xảy ra sự cố hoán đổi (hết thời gian, lỗi kỹ thuật), khóa này cho phép bạn khôi phục tiền của mình



## Tạo một hoán đổi từng bước



### Thay thế: Lightning → Bitcoin



Ví dụ đầu tiên này cho thấy cách chuyển đổi Lightning satoshi thành on-chain bitcoin.



**Bước 1: Hoán đổi cấu hình



Từ trang chính, chọn biểu mẫu trao đổi:




- LIGHTNING** (trường phía trên): Nhập số tiền bạn muốn gửi trong sats Lightning (ví dụ: 30.000 sats)
- BITCOIN** (trường bên dưới): Số tiền bạn sẽ nhận được sẽ tự động hiển thị sau khi đã trừ phí (ví dụ: 29.320 sats)



Ở ô dưới cùng, hãy dán **địa chỉ nhận Bitcoin** của bạn vào nơi bạn muốn nhận tiền. Kiểm tra địa chỉ này cẩn thận.



Nhà cung cấp mặc định thường là Boltz Exchange. Phí mạng và phí nhà cung cấp được hiển thị rõ ràng.



![Configuration swap-out](assets/fr/03.webp)



**Bước 2: Lựa chọn nhà cung cấp**



Nhấp vào menu thả xuống của nhà cung cấp (mặc định: "Boltz Exchange") để hiển thị tất cả các nhà cung cấp thanh khoản có sẵn.



Một cửa sổ mô-đun mở ra, hiển thị bảng so sánh:




- Trạng thái**: Chỉ báo Green nếu nhà cung cấp đang hoạt động
- Biệt danh**: Tên nhà cung cấp (Boltz Exchange, Middle Way, Eldamar, ZEUS Swaps)
- Phí**: Phí do nhà cung cấp áp dụng (thường từ 0,49% đến 0,5%)
- Hoán đổi tối đa**: Số tiền tối đa được chấp nhận cho một lần hoán đổi



So sánh mức phí và số tiền tối đa, sau đó chọn nhà cung cấp theo ý muốn.



**Xin lưu ý**: Giao diện lựa chọn nhà cung cấp không hiển thị **số tiền tối thiểu** cho từng nhà cung cấp. Thông tin này chỉ xuất hiện trong giao diện tạo giao dịch hoán đổi, sau khi đã chọn nhà cung cấp. Số tiền tối thiểu và tối đa có thể khác nhau tùy theo nhà cung cấp và có thể thay đổi theo thời gian. **Luôn kiểm tra các giới hạn này tại thời điểm hoán đổi**: nếu số tiền bạn muốn hoán đổi nằm ngoài giới hạn của một nhà cung cấp, bạn có thể chọn nhà cung cấp khác phù hợp hơn cho giao dịch của mình.



![Sélection du provider](assets/fr/04.webp)



**Bước 3: Tạo Swap và thanh toán Lightning**



Nhấp vào nút màu vàng **"CREATE ATOMIC SWAP"**. SwapMarket sẽ tạo hóa đơn Lightning (BOLT11) để bạn thanh toán từ wallet Lightning của mình.



Trang này hiển thị:




- Swap ID**: Mã định danh swap duy nhất (ví dụ: J4ymFIMVR6Hm)
- Trạng thái**: "swap.created" (swap đã được tạo, đang chờ thanh toán)
- Mã QR**: Quét mã bằng wallet Lightning của bạn
- Invoice Lightning**: Chuỗi ký tự bắt đầu bằng "lnbc" (ví dụ: lnbc300u1p50whiv...gn5dk2szgqkvfkzc)



Thanh toán hóa đơn này bằng thẻ wallet Lightning (Phoenix, Zeus, BlueWallet, v.v.) của bạn. Số tiền chính xác cần thanh toán sẽ được hiển thị (ví dụ: 30.000 sats).



![Paiement Lightning](assets/fr/05.webp)



**Bước 4: Xác nhận và chấp nhận**



Sau khi thanh toán Lightning được xác nhận, SwapMarket sẽ ngay lập tức nhận được khoản thanh toán của bạn và nhà cung cấp sẽ phát giao dịch Bitcoin đến địa chỉ của bạn.



Trạng thái thay đổi thành **"invoice.settled "** (hóa đơn đã thanh toán) và thông báo xác nhận sẽ hiển thị.



Bitcoin on-chain của bạn sẽ có sẵn ngay sau khi giao dịch được xác nhận (thường mất vài phút đến vài giờ, tùy thuộc vào mức phí mining do nhà cung cấp lựa chọn).



![Confirmation swap-out](assets/fr/06.webp)



Bạn có thể nhấp vào **"MỞ GIAO DỊCH YÊU CẦU"** để xem giao dịch Bitcoin trên trình duyệt blockchain.



### Đổi vào: Bitcoin → Lightning



Ví dụ thứ hai này cho thấy cách chuyển đổi bitcoin on-chain thành satoshi Lightning.



**Bước 1: Hoán đổi cấu hình



Từ trang chính, chọn biểu mẫu trao đổi:




- BITCOIN** (trường phía trên): Nhập số tiền bạn muốn gửi vào sats Bitcoin (ví dụ: 63.400 sats)
- LIGHTNING** (trường dưới cùng): Số tiền bạn sẽ nhận được sẽ tự động hiển thị sau khi trừ phí (ví dụ: 62 884 sats)



Ở trường bên dưới, hãy dán hóa đơn Lightning** (BOLT11) được tạo từ wallet Lightning của bạn hoặc sử dụng địa chỉ LNURL nếu wallet của bạn hỗ trợ.



![Configuration swap-in](assets/fr/07.webp)



**Bước 2: Kiểm tra Khóa cứu hộ**



Sau khi nhấp vào **"CREATE ATOMIC SWAP "**, một cửa sổ sẽ xuất hiện, yêu cầu bạn xác minh Khóa cứu hộ của mình.



![Modal Rescue Key](assets/fr/08.webp)



**Khóa cứu hộ Boltz**: Vì bạn đã tải lên khóa khôi phục của mình trong quá trình cấu hình ban đầu (xem phần trước), hãy nhấp vào nút **"XÁC MINH KHÓA HIỆN CÓ"** để nhập khóa bạn đã lưu.



Chọn tệp Khóa Cứu Hộ đã tải xuống trước đó. Sau khi xác minh thành công, giao diện sẽ tự động chuyển sang bước tiếp theo.



**Bước 3: Địa chỉ gửi tiền Bitcoin**



SwapMarket hiện tạo một **địa chỉ Bitcoin duy nhất** chứa hợp đồng HTLC được liên kết với hóa đơn Lightning của bạn.



Trang này hiển thị:




- Swap ID**: Mã định danh duy nhất (ví dụ: 1kGmB6JyGqU4)
- Trạng thái**: "invoice.set" (hóa đơn đã được đặt, đang chờ thanh toán Bitcoin)
- Mã QR**: Địa chỉ kho Bitcoin
- Địa chỉ Bitcoin**: Thường bắt đầu bằng "bc1p..." (ví dụ: bc1p5mvtwxapjkds...9d4n9f)
- Cảnh báo màu vàng**: "Hãy đảm bảo giao dịch của bạn được xác nhận trong vòng ~24 giờ sau khi tạo giao dịch hoán đổi này!"



Khoảng thời gian ~24 giờ này là **thời gian chờ** của hợp đồng HTLC. Nếu giao dịch Bitcoin của bạn không được xác nhận trong khoảng thời gian này, giao dịch hoán đổi sẽ thất bại và bạn sẽ cần sử dụng Khóa Cứu hộ để khôi phục tiền.



![Adresse de dépôt Bitcoin](assets/fr/09.webp)



Bạn có thể sao chép địa chỉ bằng cách nhấp vào nút **"ĐỊA CHỈ"** hoặc quét mã QR trực tiếp từ wallet on-chain của bạn.



**Bước 4: Gửi bitcoin**



Từ wallet Bitcoin on-chain của bạn, gửi **chính xác** số tiền được chỉ định (ví dụ: 63.400 sats) đến địa chỉ được tạo.



**Quan trọng**: Sử dụng phí mining phù hợp để đảm bảo xác nhận nhanh chóng. Nếu phí quá thấp và giao dịch vẫn nằm trong mempool sau thời gian chờ (khoảng 24 giờ), việc hoán đổi sẽ thất bại.



Sau khi giao dịch được gửi, SwapMarket phát hiện giao dịch đó nằm trong mempool và hiển thị:




- Trạng thái**: "transaction.mempool
- Tin nhắn**: "Giao dịch đang ở trong mempool - Đang chờ xác nhận để hoàn tất việc hoán đổi"



![Transaction en mempool](assets/fr/10.webp)



**Bước 5: Xác nhận và tiếp nhận Lightning**



Ngay khi giao dịch Bitcoin nhận được xác nhận đầu tiên, nhà cung cấp sẽ tự động thanh toán hóa đơn Lightning của bạn. Bạn sẽ nhận được satoshi ngay lập tức trên ví wallet Lightning của mình.



Trạng thái thay đổi thành **"transaction.claim.pending "**, sau đó thông báo xác nhận sẽ hiển thị:



![Confirmation swap-in](assets/fr/11.webp)



Satoshi Lightning của bạn sẽ có sẵn ngay trong wallet.



## Ưu điểm và hạn chế



### Những lợi ích



**Cạnh tranh về giá**: Việc tập hợp các nhà cung cấp tạo ra sự cạnh tranh tự nhiên kéo mức phí xuống (từ 0,49% xuống 0,5%).



**Bảo mật**: Không cần KYC, 100% giao diện phía máy khách (không truyền dữ liệu cá nhân), tương thích với Trình duyệt Tor.



**Không lưu ký**: HTLC đảm bảo về mặt toán học quyền kiểm soát độc quyền đối với tiền của bạn. Hoặc là giao dịch hoán đổi thành công, hoặc bạn sẽ nhận lại được bitcoin của mình.



**Mã nguồn mở có thể tự lưu trữ**: mã công khai có thể kiểm tra, triển khai cục bộ để chống kiểm duyệt tối đa.



### Hạn chế



**Tính thanh khoản hạn chế**: Số lượng nhà cung cấp hoạt động hạn chế (Boltz, Eldamar, MiddleWay tùy theo thời kỳ). Số tiền tối đa có thể bị giới hạn.



**Thời gian hết hạn**: Thời gian chờ từ 24 giờ đến 48 giờ. Nếu giao dịch on-chain không được xác nhận trước khi hết hạn, cần phải khôi phục thủ công.



**Tập trung hóa Interface**: Mặc dù có thể tự lưu trữ, giao diện chính thức được lưu trữ trên GitHub Pages. Nếu GitHub kiểm duyệt kho lưu trữ, quyền truy cập qua swapmarket.github.io sẽ bị chặn (giải pháp: tự lưu trữ).



**Dấu vết on-chain**: Các tập lệnh HTLC có khả năng được xác định bằng phân tích blockchain nâng cao.



## Thực hành tốt nhất



### Cấu hình an toàn



**Tải xuống Khóa Cứu hộ**: Trước lần hoán đổi đầu tiên, hãy tải xuống Khóa Cứu hộ từ mục Cài đặt (xem phần chuyên dụng ở trên). Khóa duy nhất này sẽ hoạt động cho tất cả các lần hoán đổi trong tương lai của bạn, cho phép bạn khôi phục tiền trong trường hợp gặp sự cố.



**Sử dụng Trình duyệt Tor**: Để bảo mật tối đa, hãy truy cập SwapMarket qua Trình duyệt Tor để ẩn địa chỉ IP của bạn.



**Cân nhắc tự lưu trữ**: Đối với người dùng kỹ thuật, việc chạy phiên bản SwapMarket của riêng bạn sẽ loại bỏ sự phụ thuộc vào tên miền GitHub Pages chính thức.



### Tối ưu hóa hoán đổi



**Theo dõi mempool**: Kiểm tra mempool.space trước khi hoán đổi. Chọn thời điểm ít hoạt động để giảm thiểu chi phí mining.



**Kiểm tra địa chỉ**: Đối với các trường hợp đổi trả, vui lòng kiểm tra kỹ địa chỉ nhận hàng. Sử dụng chức năng sao chép và dán, đồng thời kiểm tra 5 ký tự đầu và 5 ký tự cuối.



**Thử nghiệm với lượng nhỏ**: Bắt đầu với lượng tối thiểu được phép (25.000 đến 50.000 sats). Tăng dần khi bạn đã thành thạo quy trình.



**Ghi chép lại các giao dịch hoán đổi của bạn**: Ghi lại ID, địa chỉ đổi và ngày hết hạn của mỗi giao dịch hoán đổi. Thông tin này giúp theo dõi và phục hồi dễ dàng hơn trong trường hợp xảy ra sự cố kỹ thuật.



### Chiến lược sử dụng



**Cân bằng dòng tiền của bạn**: Sử dụng SwapMarket để điều chỉnh phân bổ giữa on-chain (tiết kiệm, an ninh dài hạn) và Lightning (chi phí hàng ngày, thanh toán tức thì) theo nhu cầu thực tế của bạn.



**Tính toán lợi nhuận**: Đối với nhu cầu thanh khoản Lightning lâu dài, hãy so sánh chi phí tích lũy của các giao dịch hoán đổi lặp lại so với việc mở trực tiếp kênh Lightning. SwapMarket vượt trội về khả năng điều chỉnh một lần, không nhất thiết phải đáp ứng các dòng tiền lớn thường xuyên.



## SwapMarket và Boltz: Sự khác biệt là gì?



### Boltz: Công nghệ so với Dịch vụ



**Boltz là công nghệ nguồn mở** (`boltz-backend` trên GitHub) thực hiện hoán đổi nguyên tử thông qua HTLC giữa Bitcoin, Lightning và Liquid.



**Điểm quan trọng**: Tất cả các nhà cung cấp SwapMarket (Boltz Exchange, ZEUS Swaps, Eldamar, Middle Way) đều triển khai phiên bản riêng của nền tảng Boltz. Do đó, công nghệ nền tảng là giống hệt nhau. Một lỗ hổng trong nền tảng Boltz có khả năng ảnh hưởng đến tất cả các nhà cung cấp, nhưng bản chất mã nguồn mở của hệ thống cho phép cộng đồng kiểm tra.



**Boltz Exchange** là dịch vụ duy nhất do nhóm Boltz vận hành, trong khi **SwapMarket** tập hợp nhiều nhà cung cấp đều sử dụng công nghệ Boltz, tạo ra môi trường giá cả cạnh tranh.



Xem hướng dẫn hoán đổi Boltz và Zeus của chúng tôi để biết thêm chi tiết:



https://planb.academy/tutorials/exchange/centralized/boltz-34ad778e-6dc7-41c2-8219-e11e3361a43d

https://planb.academy/tutorials/exchange/centralized/zeus-swap-b6732907-b5d8-43ea-85e3-9dcd6e6abe47

### Sự khác biệt chính



| Khía cạnh     | Boltz Exchange       | SwapMarket                           |
| ------------ | -------------------- | ------------------------------------ |
| Tính chất     | Dịch vụ độc đáo      | Bộ tổng hợp đa nhà cung cấp          |
| Nhà cung cấp  | Chỉ Boltz            | Boltz, ZEUS, Eldamar, Middle Way     |
| Cạnh tranh    | Phí cố định          | Cạnh tranh tự do                     |
| Giao diện     | boltz.exchange       | swapmarket.github.io (tự lưu trữ)     |
| Bảo mật       | Non-custodial (HTLC) | Non-custodial (HTLC)                 |

**Lợi ích của SwapMarket**: Cạnh tranh về giá, đa dạng hóa các phiên bản phụ trợ, so sánh theo thời gian thực.



**Các giải pháp thay thế công nghệ** (không tương thích với SwapMarket): Lightning Loop (Lightning Labs), Muun Wallet, NLoop, Breez Wallet. Các giải pháp này sử dụng các triển khai hoán đổi ngầm riêng của họ.



**Khuyến nghị**: Sử dụng Boltz Exchange để đơn giản hóa hoặc SwapMarket để tối ưu hóa chi phí thông qua cạnh tranh. Cả hai đều tương đương về độ an toàn (HTLC không lưu ký).



## Phần kết luận



SwapMarket hỗ trợ các sàn giao dịch Bitcoin/Lightning bằng cách tập hợp nhiều nhà cung cấp vào một giao diện duy nhất. Kiến trúc HTLC đảm bảo tính phi lưu ký của các giao dịch hoán đổi, việc không cần KYC giúp bảo mật thông tin, và mã nguồn mở tự lưu trữ giúp tăng cường khả năng chống kiểm duyệt.



Sự cạnh tranh giữa các nhà cung cấp giúp cải thiện tỷ giá và tăng cường nguồn thanh khoản. Để tối ưu hóa quản lý hai lớp (tiết kiệm on-chain, chi phí Lightning), SwapMarket là một công cụ thiết thực giúp bảo vệ chủ quyền tài chính và tính bảo mật.



## Tài nguyên



### Tài liệu chính thức




- [SwapMarket - Ứng dụng web](https://swapmarket.github.io)
- [GitHub SwapMarket](https://github.com/SwapMarket/swapmarket.github.io)
- [Tài liệu kỹ thuật](https://docs.boltz.exchange/)
- [Hướng dẫn tự lưu trữ](https://github.com/SwapMarket/swapmarket.github.io/blob/main/README.md)



### Các dự án liên quan




- [Boltz Exchange](https://boltz.exchange) - Dịch vụ hoán đổi nguyên tử gốc
- [ZEUS Swaps](https://zeusln.com) - Nhà cung cấp dịch vụ hoán đổi Lightning