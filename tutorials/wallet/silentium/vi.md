---
name: Silentium
description: Web tiến bộ wallet hỗ trợ thanh toán im lặng (BIP-352)
---

![cover](assets/cover.webp)



Việc tái sử dụng địa chỉ Bitcoin là một trong những mối đe dọa trực tiếp nhất đến quyền riêng tư của người dùng. Khi người nhận chia sẻ một địa chỉ duy nhất để nhận nhiều khoản thanh toán, bất kỳ ai cũng có thể theo dõi tất cả các giao dịch liên quan và tái tạo lịch sử tài chính của họ. Vấn đề này đặc biệt ảnh hưởng đến những người tạo nội dung, các tổ chức từ thiện hoặc các nhà hoạt động muốn công khai địa chỉ quyên góp mà không làm ảnh hưởng đến quyền riêng tư của họ.



Silentium giải quyết vấn đề này bằng một giải pháp thanh lịch có thể truy cập trực tiếp từ trình duyệt của bạn. Ứng dụng web tiến bộ (PWA) mã nguồn mở này, được Louis Singer ra mắt vào tháng 5 năm 2024, triển khai Thanh toán im lặng (BIP-352): một địa chỉ tĩnh có thể tái sử dụng, trong đó mỗi khoản thanh toán được ghi vào một địa chỉ blockchain riêng biệt, không có tương tác trước đó hoặc liên kết có thể quan sát được giữa các giao dịch.



**Cảnh báo quan trọng**: Silentium là một dự án thử nghiệm đóng vai trò là *bằng chứng về tính khả thi* của ví điện tử nhẹ của Silent Payments. Không nên sử dụng nó như một wallet hàng ngày hoặc để lưu trữ số tiền lớn. Các nhà phát triển đã nêu rõ:



> Sử dụng với rủi ro của riêng bạn.

Lưu ý rằng wallet này có thể được sử dụng như một mạng thử nghiệm hoặc mạng đăng ký.



## Silentium là gì?



### Triết lý và mục tiêu



Silentium đóng vai trò là bản trình diễn kỹ thuật cho việc triển khai Thanh toán im lặng trên trình duyệt wallet nhẹ. Mặc dù nó cũng hỗ trợ các địa chỉ Bitcoin thông thường, trọng tâm vẫn là Thanh toán im lặng để người dùng có thể thử nghiệm công nghệ bảo mật này một cách dễ dàng.



### Thanh toán im lặng hoạt động như thế nào?



Thanh toán im lặng (BIP-352) sử dụng khóa Diffie-Hellman đường cong Elliptic Exchange (ECDH). Người nhận tạo ra một địa chỉ tĩnh (`sp1...` trên mainnet, `tsp1...` trên mạng thử nghiệm) bao gồm hai khóa công khai: một khóa quét để phát hiện các khoản thanh toán và một khóa chi tiêu để sử dụng chúng.



Người gửi kết hợp khóa đầu vào riêng tư của mình với khóa quét của người nhận để tính toán một khóa bí mật chung, tạo ra một "điều chỉnh" mật mã. Điều chỉnh này, khi được thêm vào khóa chi tiêu, sẽ tạo ra một địa chỉ Taproot duy nhất cho mỗi giao dịch. Người nhận tái tạo phép tính này với khóa quét riêng tư của mình để phát hiện và chi tiêu tiền mà không cần bất kỳ tương tác nào trước đó.



Ưu điểm: Tăng cường tính bảo mật cho người gửi và người nhận, không cần máy chủ bên thứ ba, giao dịch không thể phân biệt được với các khoản thanh toán Taproot thông thường. Nhược điểm chính: Quét chuỗi khối tốn nhiều công sức để phát hiện các khoản thanh toán.



Để tìm hiểu thêm về cơ chế hoạt động lý thuyết của Thanh toán im lặng, hãy xem phần cuối của khóa học BTC,204 về Plan ₿ Academy:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Các nền tảng được hỗ trợ



Silentium là một ứng dụng web tiến bộ (PWA) có thể truy cập từ bất kỳ trình duyệt hiện đại nào (di động hoặc máy tính). Bạn có thể sử dụng trực tiếp trên `app.silentium.dev`, cài đặt nó như một ứng dụng gốc thông qua trình duyệt của mình hoặc triển khai cục bộ. Việc cài đặt được thực hiện trực tiếp từ trình duyệt, không cần thông qua các cửa hàng ứng dụng chính thức.



## Sử dụng ứng dụng web



### Truy cập và lắp đặt



[Truy cập `https://app.silentium.dev/` từ trình duyệt của bạn](https://app.silentium.dev/). Ứng dụng sẽ tải ngay lập tức và hiển thị màn hình chính.



Để cài đặt Silentium như một ứng dụng gốc trên iOS, hãy nhấn vào nút chia sẻ (hình vuông có mũi tên hướng lên) rồi chọn "Trên màn hình chính". Trên Android, trình duyệt thường hiển thị thông báo "Thêm vào màn hình chính" trực tiếp. Sau khi cài đặt, Silentium sẽ xuất hiện với biểu tượng riêng và hoạt động như một ứng dụng gốc, nhưng cần kết nối internet để đồng bộ hóa các giao dịch.



![Installation de Silentium comme PWA sur iOS](assets/fr/01.webp)



### Tạo danh mục đầu tư



Khi khởi chạy lần đầu, hãy chọn "Tạo Wallet" để tạo một danh mục generate mới, hoặc "Khôi phục Wallet" để khôi phục từ cụm từ khôi phục hiện có.



Chọn "Tạo Wallet". Ứng dụng sẽ tạo ra một cụm từ gồm 12 từ mà bạn phải ghi lại cẩn thận. Cụm từ này là cách duy nhất để khôi phục tiền của bạn. Ngay cả trên mạng thử nghiệm, hãy áp dụng các biện pháp sao lưu an toàn. Nhấn "Tiếp tục" sau khi lưu cụm từ của bạn.



Ứng dụng sẽ yêu cầu bạn thiết lập mật khẩu để bảo mật quyền truy cập vào wallet. Hãy chọn một mật khẩu mạnh và xác nhận lại.



![Création d'un nouveau wallet avec phrase de récupération](assets/fr/02.webp)



Sau khi cụm từ xác nhận và mật khẩu được thiết lập, bạn sẽ được chuyển đến giao diện chính.



### Các thông số và đặc điểm chính của Interface



Giao diện chính hiển thị số dư của bạn tính bằng satoshi (ban đầu là 0 sats), với ba nút ở phía dưới:




- Đồng bộ hóa**: đồng bộ hóa wallet với blockchain
- Nhận**: để nhận tiền
- Gửi**: để gửi bitcoin



Truy cập Cài đặt thông qua biểu tượng ở góc trên bên phải (ba thanh ngang). Menu Cài đặt cung cấp một số tùy chọn:





- Giới thiệu**: thông tin ứng dụng
- Sao lưu**: sao lưu cụm từ phục hồi
- Trình khám phá**: chọn trình khám phá blockchain (mặc định là Mempool) và máy chủ Silentiumd
- Mạng**: lựa chọn mạng (mainnet/testnet)
- Mật khẩu**: thay đổi mật khẩu
- Nạp đạn**: nạp đạn cho wallet
- Đặt lại**: đặt lại hoàn toàn
- Chủ đề**: thay đổi chủ đề



![Interface principale et paramètres avec Explorer](assets/fr/03.webp)



Phần **Explorer** đặc biệt quan trọng: nó cho phép bạn chọn trình khám phá blockchain được sử dụng (mặc định là Mempool) và cũng hiển thị URL của máy chủ Silentiumd (`https://bitcoin.silentium.dev/v1` cho mainnet). Nếu bạn tự vận hành máy chủ Silentiumd hoặc muốn sử dụng mạng thử nghiệm (testnet), đây là nơi bạn cấu hình các tham số này.



### Nhận tiền



Từ giao diện chính, nhấn nút "Nhận". Theo mặc định, Silentium sẽ hiển thị địa chỉ Thanh toán Im lặng kèm mã QR. Địa chỉ này bắt đầu bằng `sp1...` trên mainnet hoặc `tsp1...` trên mạng thử nghiệm.



Bạn có thể chuyển đổi giữa địa chỉ Thanh toán im lặng và địa chỉ Bitcoin thông thường bằng cách sử dụng nút "Chuyển sang địa chỉ thông thường" / "Chuyển sang địa chỉ im lặng" ở cuối màn hình.



![Réception de fonds avec Silent Payment et adresse classique](assets/fr/04.webp)




Sau khi giao dịch được phát sóng, vui lòng chờ vài phút. Đối với Thanh toán im lặng, Silentium tự động quét chuỗi khối để tìm các giao dịch dành cho bạn. Các giao dịch sẽ hiển thị trạng thái "Chưa được xác nhận" trước khi được xác nhận dần dần.



### Gửi thanh toán



Từ giao diện chính, nhấn nút "Gửi". Màn hình gửi sẽ hỏi bạn:



1. **Address**: Dán địa chỉ Thanh toán im lặng (`sp1...` hoặc `tsp1...`) hoặc địa chỉ Bitcoin thông thường. Bạn có thể sử dụng biểu tượng quét mã QR để quét địa chỉ.


2. **Số tiền**: Nhập số tiền (tính bằng satoshi) bạn muốn gửi. Bàn phím số sẽ được hiển thị để dễ dàng nhập liệu. Số dư khả dụng của bạn sẽ được hiển thị ở phía trên để tham khảo.



![Envoi de fonds depuis Silentium](assets/fr/05.webp)



Sau khi nhập địa chỉ và số tiền, hãy nhấn "Tiếp tục" để hoàn tất. Ứng dụng sẽ yêu cầu bạn chọn mức phí mong muốn trước khi xác nhận giao dịch.



## Tự lưu trữ wallet



### Tại sao nên tự lưu trữ?



Dịch vụ lưu trữ cục bộ của Silentium cung cấp quyền tự chủ hoàn toàn, xác minh mã nguồn, môi trường phát triển và khả năng phục hồi khi trang web chính thức gặp sự cố.



### Điều kiện tiên quyết



Node.js (phiên bản 14 trở lên), npm hoặc yarn, Git và khoảng 500 MB dung lượng ổ đĩa.



### Cài đặt cục bộ



Sao chép kho lưu trữ và cài đặt:



```bash
git clone https://github.com/louisinger/silentium.git
cd silentium
yarn install
```



### Khởi chạy và sử dụng



Khởi chạy ứng dụng ở chế độ phát triển:



```bash
yarn start
```



Truy cập `http://localhost:3000` trong trình duyệt của bạn. Để có phiên bản sản xuất được tối ưu hóa:



```bash
yarn build
```



Các tệp được tạo trong thư mục `build/` có thể được phục vụ bằng nginx, Apache hoặc bất kỳ máy chủ web nào. Theo mặc định, Silentium kết nối với máy chủ công cộng `bitcoin.silentium.dev`. Hãy sửa đổi cài đặt này trong các tham số để sử dụng testnet hoặc máy chủ của riêng bạn.



## Máy chủ Silentiumd



### Vai trò và hoạt động



Silentium sử dụng máy chủ lập chỉ mục **Silentiumd** để tối ưu hóa việc phát hiện thanh toán. Việc quét tất cả các giao dịch Taproot sẽ quá phức tạp đối với trình duyệt hoặc điện thoại di động.



Silentiumd tính toán trước dữ liệu trung gian (các tinh chỉnh) cho mỗi giao dịch Taproot. wallet của bạn tải xuống các tinh chỉnh này (một vài byte cho mỗi giao dịch) và thực hiện tính toán cuối cùng cục bộ, xác minh quyền sở hữu khoản thanh toán. Máy chủ không bao giờ biết khóa của bạn hoặc có thể xác định các giao dịch của bạn, không giống như các máy chủ Electrum thông thường.



Bộ lọc BIP158 nhỏ gọn cho phép thiết bị wallet của bạn xác định các khối cần quét mà không tiết lộ địa chỉ của bạn, do đó bảo vệ tính bảo mật của bạn.



### Máy chủ công cộng



Máy chủ công cộng `bitcoin.silentium.dev` (mainnet), được tài trợ bởi Vulpem Ventures, cung cấp trải nghiệm đơn giản và nhanh chóng. Mặc dù tính bảo mật được đảm bảo, cách tiếp cận này ngụ ý sự tin tưởng tương đối vào cơ sở hạ tầng của bên thứ ba.



### Tự thiết lập máy chủ Silentiumd của riêng bạn



Để có quyền tự chủ hoàn toàn, hãy tự thiết lập máy chủ Silentiumd của riêng bạn. Điều kiện tiên quyết: Nút Bitcoin Core không ràng buộc với `txindex=1` và `blockfilterindex=1`, Go 1.21 trở lên, 10-20 GB dung lượng ổ đĩa, kỹ năng quản trị hệ thống.



**Hướng dẫn cài đặt:**



```bash
git clone https://github.com/louisinger/silentiumd.git
cd silentiumd
make build
./build/silentium-[OS]-[ARCH]
```



Cấu hình thông qua các biến môi trường (xem tệp `config.md` của kho lưu trữ để biết chi tiết). Máy chủ lập chỉ mục chuỗi khối và hiển thị một API mà wallet của bạn có thể truy vấn.



Hiện tại chưa có giải pháp trọn gói nào cho Umbrel hoặc Start9, điều này hạn chế khả năng tiếp cận đối với người dùng không chuyên về kỹ thuật.



## Ưu điểm và hạn chế



### Điểm nổi bật





- Khả năng truy cập tối đa**: sử dụng được trên mọi trình duyệt, không cần cài đặt phức tạp.
- Đa nền tảng**: hoạt động trên thiết bị di động (Android/iOS) và máy tính để bàn nhờ công nghệ PWA.
- Tự lưu trữ đơn giản**: có thể cài đặt cục bộ chỉ với một vài lệnh.
- Mã nguồn mở**: mã nguồn hoàn toàn minh bạch và có thể kiểm tra được trên GitHub
- **Tập trung vào quyền riêng tư**: không theo dõi, không phân tích dữ liệu, tính toán mã hóa cục bộ.
- Kiến trúc tách biệt**: sự tách biệt rõ ràng giữa wallet (máy khách) và máy chủ lập chỉ mục.
- Không cần tài khoản**: không cần đăng ký hoặc cung cấp thông tin cá nhân.



### Các ràng buộc cần xem xét





- Dự án thử nghiệm**: chỉ nhằm mục đích chứng minh tính khả thi, không dành cho sử dụng hàng ngày hoặc sản xuất.
- Không có gì đảm bảo**: rủi ro về lỗi phần mềm, lỗ hổng bảo mật, khả năng mất vốn.
- Hỗ trợ hạn chế**: ít tài liệu hướng dẫn người dùng, cộng đồng nhỏ, không có hỗ trợ chính thức**
- Yêu cầu máy chủ**: cần có máy chủ Silentiumd đang hoạt động (máy chủ công cộng hoặc tự lưu trữ)
- Quét chuyên sâu**: Phát hiện các giao dịch thanh toán ẩn tiêu tốn băng thông.
- **Chức năng bị hạn chế**: không có chức năng kiểm soát tiền xu, không có Lightning, không có chữ ký nhiều chữ ký



## Thực tiễn tốt nhất



### An toàn seed



Ngay cả trên mạng thử nghiệm, hãy luôn coi trọng cụm từ khôi phục của bạn. Hãy viết nó ra và cất giữ ở nơi an toàn. Sử dụng ví riêng biệt cho mạng thử nghiệm và mainnet: tuyệt đối không sử dụng seed thử nghiệm trên wallet dành cho tiền thật.



### Xác minh mã nguồn



Một trong những ưu điểm của việc tự lưu trữ là khả năng kiểm tra mã nguồn trước khi chạy. Nếu bạn dự định sử dụng Silentium với chi phí thực tế, hãy dành thời gian kiểm tra mã hoặc nhờ một nhà phát triển đáng tin cậy thực hiện việc này. Đồng thời, hãy so sánh mã băm (hash) của mã được triển khai trên `app.silentium.dev` với mã băm của kho lưu trữ GitHub để đảm bảo tính xác thực.



### Sao lưu và phục hồi



Việc khôi phục quỹ Thanh toán Im lặng yêu cầu một thiết bị wallet tương thích với giao thức BIP-352. Một thiết bị wallet tiêu chuẩn không thể quét chuỗi khối để khôi phục các khoản Thanh toán Im lặng UTXO của bạn. Hãy giữ Silentium được cài đặt hoặc đảm bảo bạn có quyền truy cập vào một thiết bị wallet tương thích khác (chẳng hạn như Cake Wallet hoặc các phiên bản triển khai trong tương lai) để khôi phục tiền của bạn nếu cần.



## Phần kết luận



Silentium cung cấp một môi trường thử nghiệm dễ tiếp cận để hiểu về Thanh toán im lặng mà không gặp trở ngại kỹ thuật. Như một minh chứng cho khái niệm này, nó cho thấy cách công nghệ bảo mật này có thể được tích hợp vào trình duyệt wallet trong khi vẫn duy trì quyền tự quản lý. Hãy thử nghiệm trên mạng thử nghiệm để khám phá bước đột phá đầy hứa hẹn này cho quyền riêng tư on-chain.



## Tài nguyên



### Tài liệu chính thức




- Kho lưu trữ Silentium GitHub (wallet): https://github.com/louisinger/silentium
- Kho lưu trữ GitHub của Silentiumd (máy chủ): https://github.com/louisinger/silentiumd
- Ứng dụng web: https://app.silentium.dev/
- Trang web cộng đồng Thanh toán im lặng: https://silentpayments.xyz
- Thông số kỹ thuật BIP-352: https://bips.dev/352



### Bài viết và tài liệu tham khảo




- Thông báo chính thức (Twitter): https://x.com/TheSingerLouis/status/1790824126472667227
- NoBS Bitcoin: https://www.nobsbitcoin.com/silentium-silent- Payments/
- Bitcoin Optech - Thanh toán im lặng: https://bitcoinops.org/en/topics/silent-payments/



### Công cụ Testnet




- Vòi Testnet: https://testnet-faucet.com/
- Trình thám hiểm mạng thử nghiệm Mempool: https://mempool.space/testnet