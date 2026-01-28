---
name: Dana Wallet
description: Danh mục đầu tư tối giản cho Thanh toán thầm lặng (BIP-352)
---

![cover](assets/cover.webp)



Việc tái sử dụng địa chỉ Bitcoin là một trong những mối đe dọa trực tiếp nhất đối với tính bảo mật của người dùng. Khi người nhận chia sẻ một địa chỉ duy nhất để nhận nhiều khoản thanh toán, bất kỳ người quan sát nào cũng có thể theo dõi tất cả các giao dịch liên quan và tái tạo lịch sử tài chính của họ. Vấn đề này đặc biệt ảnh hưởng đến những người sáng tạo nội dung, tổ chức từ thiện hoặc nhà hoạt động muốn công khai địa chỉ quyên góp mà không làm ảnh hưởng đến quyền riêng tư của họ hoặc của người quyên góp.



Dana Wallet giải quyết vấn đề này bằng một giải pháp tinh tế: Thanh toán Im lặng. wallet mã nguồn mở, tối giản này, ra mắt năm 2024, tạo ra một địa chỉ tĩnh có thể tái sử dụng, đồng thời đảm bảo mỗi khoản thanh toán nhận được sẽ được chuyển đến một địa chỉ riêng biệt trên blockchain. Người gửi không cần tương tác trước với người nhận, và không có bên quan sát bên ngoài nào có thể liên kết các giao dịch riêng lẻ với nhau. Trên blockchain, các khoản thanh toán này trông giống hệt như các giao dịch Taproot thông thường.



Dana Wallet hiện có sẵn trên Mainnet và Signet, nhưng các nhà phát triển vẫn coi đây là phiên bản thử nghiệm và khuyến nghị không nên nạp tiền nếu bạn không sẵn sàng mất tiền. Trong hướng dẫn này, chúng ta sẽ sử dụng phiên bản Signet để khám phá Thanh toán Im lặng mà không phải mạo hiểm bất kỳ khoản tiền thật nào.



## Dana Wallet là gì?



### Triết lý và mục tiêu



Dana Wallet áp dụng phương pháp "SP-first": wallet chỉ tạo địa chỉ Thanh toán Im lặng và chỉ chấp nhận loại hình thanh toán này. Bạn sẽ không thể tạo địa chỉ Bitcoin cổ điển (cũ, chuẩn SegWit hoặc Taproot) với ứng dụng này. Hạn chế cố ý này cho phép bạn tập trung hoàn toàn vào việc học giao thức BIP-352 mà không bị phân tâm bởi các tính năng khác. Giao diện gọn gàng chủ động ưu tiên tính dễ sử dụng hơn là quá nhiều tùy chọn, giúp công cụ dễ sử dụng ngay cả với những người dùng mới làm quen với các khái niệm bảo mật của on-chain.



Dự án hoàn toàn mã nguồn mở, được phát triển với Flutter cho giao diện di động và Rust cho logic mã hóa nội bộ. Kiến trúc này kết hợp trải nghiệm người dùng mượt mà với hiệu suất tối ưu cho các hoạt động quét chuyên sâu.



### Thanh toán im lặng hoạt động như thế nào?



Thanh toán Im lặng (BIP-352) dựa trên cơ chế mã hóa tinh vi sử dụng Khóa Diffie-Hellman Đường cong Elliptic Exchange (ECDH). Người nhận tạo một địa chỉ tĩnh (bắt đầu bằng `sp1...` trên mainnet hoặc `tsp1...` trên Signet) bao gồm hai khóa công khai riêng biệt: một khóa quét ($B_{scan}$) để phát hiện các khoản thanh toán đến và một khóa chi ($B_{spend}$) để chi tiền nhận được. Sự tách biệt này cho phép giữ khóa chi trên phần cứng wallet trong khi sử dụng khóa quét trên thiết bị được kết nối.



Khi người gửi muốn thực hiện thanh toán, wallet của người gửi sẽ kết hợp tổng khóa riêng của người gửi với khóa quét công khai của người nhận để tính toán một bí mật ECDH dùng chung. Bí mật này tạo ra một "điều chỉnh" mật mã, được thêm vào khóa chi tiêu của người nhận, tạo ra một địa chỉ Taproot duy nhất cho giao dịch đó.



Người nhận có thể tái tạo phép tính này bằng cách sử dụng khóa quét riêng và khóa công khai hiển thị trong giao dịch (thuộc tính toán học Diffie-Hellman). Điều này cho phép người nhận phát hiện và chi tiêu tiền mà không cần bất kỳ tương tác nào trước đó với người gửi.



Cách tiếp cận này mang lại một số lợi thế:




- Bảo mật người nhận**: mỗi khoản thanh toán sẽ được chuyển đến một địa chỉ khác nhau
- Bảo mật người gửi**: không có mã định danh cố định liên kết thanh toán
- Không có máy chủ của bên thứ ba**: giao thức hoạt động tự động
- Giao dịch không thể phân biệt được**: Thanh toán im lặng trông giống như các giao dịch Taproot thông thường



Nhược điểm chính là chi phí quét: người nhận phải phân tích từng giao dịch Taproot mới để phát hiện ra những giao dịch dành cho mình.



Nếu bạn muốn tìm hiểu thêm về hoạt động kỹ thuật của Thanh toán im lặng, chúng tôi khuyên bạn nên tham gia khóa học BTC204 về tính bảo mật trong Bitcoin, bao gồm một chương dành riêng cho Thanh toán im lặng:



https://planb.academy/courses/65c138b0-4161-4958-bbe3-c12916bc959c

## Nền tảng được hỗ trợ



Dana Wallet có sẵn dưới dạng ứng dụng Android. APK có thể được tải xuống thông qua kho lưu trữ F-Droid chuyên dụng do nhà phát triển cung cấp, thông qua Obtainium hoặc trực tiếp từ GitHub. Đối với người dùng Linux, về mặt kỹ thuật, có thể biên dịch ứng dụng Flutter cho máy tính để bàn.



Ứng dụng này không có sẵn trên iOS hoặc thông qua các cửa hàng chính thức (Google Play, App Store), điều này cho thấy ứng dụng vẫn đang ở trạng thái thử nghiệm và tập trung vào đối tượng kỹ thuật.



## Cài đặt



### Điều kiện tiên quyết cần thiết



Để cài đặt Dana Wallet trên Android, bạn cần thiết bị Android đã bật tùy chọn "Nguồn không xác định" trong cài đặt bảo mật. Không yêu cầu tài khoản hoặc đăng ký.



### Thêm tiền gửi F-Cold



Phương pháp được khuyến nghị là thêm kho lưu trữ F-Droid chuyên dụng của Dana Wallet. Truy cập `fdroid.silentpayments.dev`, tại đây bạn sẽ tìm thấy liên kết kho lưu trữ và mã QR để quét. Kho lưu trữ hiện cung cấp 3 ứng dụng: phiên bản Mainnet, Development và Signet.



![Page du dépôt F-Droid Dana Wallet avec QR code et lien](assets/fr/01.webp)



### Cài đặt thông qua F-Droid



Mở ứng dụng F-Droid trên thiết bị Android của bạn, sau đó truy cập Cài đặt thông qua biểu tượng ở góc dưới bên phải. Chọn "Kho lưu trữ" để quản lý nguồn ứng dụng. Nhấn nút "+" để thêm kho lưu trữ mới, sau đó quét mã QR hoặc dán liên kết `https://fdroid.silentpayments.dev/fdroid/repo`. Sau khi kho lưu trữ được thêm vào, bạn sẽ thấy ba phiên bản Dana Wallet khả dụng. Chọn "Dana Wallet - Bookmark" và nhấn "Cài đặt".



![Ajout du dépôt F-Droid et installation de Dana Wallet - Signet](assets/fr/02.webp)



## Cấu hình ban đầu



### Tạo danh mục đầu tư



Khi khởi chạy lần đầu, Dana Wallet hiển thị màn hình chào mừng giới thiệu sứ mệnh của ứng dụng: "Gửi và nhận quyên góp không qua trung gian". Nhấn "Bắt đầu" để tiếp tục. Màn hình tiếp theo trình bày ba lợi ích chính của ứng dụng:




- Quyên góp dễ dàng**: bắt đầu nhận quyên góp chỉ trong vài giây
- Quyền riêng tư theo mặc định**: không cần máy chủ hoặc cơ sở hạ tầng phức tạp
- Trải nghiệm giống như email**: gửi và nhận bitcoin đơn giản như email



Bạn có thể chọn "Khôi phục" để khôi phục danh mục hiện có hoặc "Tạo wallet mới" để tạo danh mục mới. Nhấn "Tạo wallet mới".



![Premier lancement de Dana Wallet et création du portefeuille](assets/fr/03.webp)



Sau đó, ứng dụng sẽ tạo ra một cụm từ khôi phục, bạn nên ghi chú cẩn thận trên một phương tiện vật lý. Ngay cả đối với các khoản tiền thử nghiệm không có giá trị thực, hãy áp dụng các biện pháp sao lưu hiệu quả.



### Interface và các thông số



Sau khi danh mục đầu tư được tạo, bạn sẽ được chuyển đến giao diện chính, được chia thành hai tab: "Giao dịch" và "Cài đặt".



Tab **Giao dịch** hiển thị số dư bitcoin của bạn (và tỷ giá chuyển đổi sang đô la), danh sách các giao dịch gần đây và hai nút hành động: "Thanh toán" để gửi tiền và nút nhận (biểu tượng tải xuống).



Tab **Cài đặt** cung cấp bốn tùy chọn:




- Hiển thị cụm từ seed**: hiển thị cụm từ khôi phục của bạn để giữ an toàn
- Thay đổi tiền tệ fiat**: thay đổi tiền tệ hiển thị (USD theo mặc định)
- Đặt url backend**: cấu hình URL máy chủ Blindbit (xem phần tiếp theo)
- Wipe wallet**: xóa hoàn toàn wallet khỏi thiết bị



![Interface principale Transact et menu Settings](assets/fr/04.webp)



### Máy chủ Blindbit



Dana Wallet sử dụng máy chủ lập chỉ mục có tên là **Blindbit** để phát hiện các khoản Thanh toán Im lặng của bạn. Việc hiểu cách thức hoạt động của nó rất quan trọng để đánh giá mô hình tin cậy của ứng dụng.



**Tại sao chúng ta cần máy chủ?



Để phát hiện Thanh toán Im lặng, về mặt lý thuyết, wallet của bạn phải quét tất cả các giao dịch Taproot trong mỗi khối và thực hiện phép tính mật mã (ECDH) cho từng giao dịch. Trên điện thoại di động, thao tác này sẽ tốn quá nhiều tài nguyên tính toán và băng thông.



Máy chủ Blindbit giải quyết vấn đề này bằng cách tính toán trước dữ liệu trung gian (gọi là "tweak") cho tất cả các giao dịch Taproot. Sau đó, wallet của bạn sẽ tải xuống các tweak này (33 byte cho mỗi giao dịch) và thực hiện phép tính cuối cùng **cục bộ** để kiểm tra xem khoản thanh toán có thuộc về bạn hay không.



**Bảo mật được giữ kín**



Không giống như máy chủ Electrum thông thường, nơi bạn phải tiết lộ địa chỉ, máy chủ Blindbit không biết khoản thanh toán nào thuộc về bạn. Nó cung cấp cùng một dữ liệu cho tất cả người dùng và điện thoại của bạn sẽ thực hiện xác minh cuối cùng. Do đó, tính bảo mật của bạn được bảo vệ trước máy chủ.



**Máy chủ mặc định



Dana Wallet sử dụng máy chủ công cộng `silentpayments.dev/blindbit/signet` (cho Signet) hoặc `silentpayments.dev/blindbit/mainnet` (cho Mainnet). Bạn có thể thay đổi URL này trong phần cài đặt nếu bạn tự lưu trữ máy chủ.



**Lưu trữ máy chủ Blindbit của riêng bạn**



Đối với người dùng muốn có toàn quyền quản lý, họ có thể tự lưu trữ máy chủ Oracle Blindbit của riêng mình. Điều này yêu cầu:




- Một nút lõi Bitcoin hoàn chỉnh **không được đánh dấu bằng eagle** (không phải pruned)
- Cài đặt Blindbit Oracle (có sẵn trên GitHub: `setavenger/blindbit-oracle`)
- Khoảng 10 GB dung lượng đĩa bổ sung
- Kỹ năng kỹ thuật (biên dịch Go, cấu hình máy chủ)



Hiện tại, chưa có ứng dụng đóng gói nào khả dụng cho Umbrel hoặc Start9. Việc cài đặt vẫn đang được thực hiện thủ công. Đây là một lĩnh vực đang phát triển mạnh mẽ và các giải pháp dễ tiếp cận hơn có thể sẽ xuất hiện trong tương lai.



## Sử dụng hàng ngày



### Nhận tiền



Để nhận bitcoin, hãy nhấn nút nhận (biểu tượng tải xuống) từ màn hình chính. Dana Wallet sau đó sẽ hiển thị địa chỉ Thanh toán Im lặng đầy đủ của bạn theo định dạng `tsp1q...` trên Bookmark. Giao diện cung cấp một số tùy chọn:




- Hiển thị mã QR**: hiển thị mã QR của địa chỉ của bạn để dễ dàng quét
- Chia sẻ**: chia sẻ địa chỉ thông qua các ứng dụng trên điện thoại của bạn
- Sao chép**: sao chép địa chỉ vào bảng tạm



Như hiển thị trên màn hình, bạn có thể chia sẻ địa chỉ này công khai trên mạng xã hội mà không ảnh hưởng đến quyền riêng tư.



![Affichage de l'adresse de réception Silent Payment](assets/fr/05.webp)



Để nhận khoản tiền thử nghiệm đầu tiên trên Signet, hãy sử dụng vòi Silent Payments chuyên dụng có thể truy cập tại `silentpayments.dev/faucet/signet`. Sao chép địa chỉ `tsp1...` của bạn, dán vào trường được cung cấp trên vòi, sau đó xác thực yêu cầu. Chờ một khối được khai thác (khoảng 10 phút trên Signet).



### Gửi thanh toán



Để gửi tiền, hãy nhấn nút "Thanh toán" từ màn hình chính. Màn hình "Chọn người nhận" sẽ xuất hiện với ba tùy chọn để chỉ định người nhận:




- Nhập thông tin thanh toán theo cách thủ công
- Dán từ bảng tạm**: dán địa chỉ từ bảng tạm
- Quét mã QR**: quét mã QR có chứa địa chỉ



Sau khi địa chỉ người nhận được xác thực, màn hình "Nhập số tiền" cho phép bạn nhập số tiền cần gửi (tính bằng satoshi). Số dư khả dụng của bạn sẽ được hiển thị để tham khảo. Nhấn "Tiến hành chọn phí" để tiếp tục.



![Envoi d'un paiement : sélection du destinataire et du montant](assets/fr/06.webp)



Màn hình tiếp theo hiển thị ba mức phí, tùy thuộc vào mức độ khẩn cấp cần thiết:




- Nhanh** (10-30 phút): phí cao hơn để xác nhận nhanh
- Bình thường** (30-60 phút): chi phí vừa phải
- Chậm** (hơn 1 giờ): phí tối thiểu cho các giao dịch không khẩn cấp



Sau khi chọn mức phí, màn hình xác nhận "Sẵn sàng gửi?" sẽ tóm tắt tất cả thông tin chi tiết: địa chỉ nhận, số tiền, thời gian ước tính và phí giao dịch. Vui lòng kiểm tra kỹ thông tin này, sau đó nhấn "Gửi" để gửi giao dịch.



Sau khi gửi, giao dịch sẽ hiển thị trong lịch sử của bạn với trạng thái "Chưa xác nhận" cho đến khi được đưa vào khối. Số dư của bạn sẽ được cập nhật tương ứng.



![Sélection des frais, confirmation et transaction envoyée](assets/fr/07.webp)



## Ưu điểm và hạn chế



### Điểm nổi bật





- Sư phạm**: giao diện đơn giản tập trung vào việc học Thanh toán im lặng
- Song hướng**: hỗ trợ cả gửi và nhận, không giống như các danh mục đầu tư khác
- Mã nguồn mở**: mã có thể kiểm tra đầy đủ trên GitHub
- Faucet** chuyên dụng: giúp dễ dàng nhận được tài trợ thử nghiệm hơn
- Không cần tài khoản**: không cần đăng ký hoặc dữ liệu cá nhân



### Những hạn chế cần xem xét





- Thử nghiệm**: phần mềm chưa được kiểm tra, sử dụng thận trọng trên Mainnet
- Nền tảng hạn chế**: chủ yếu là Android, không có phiên bản iOS
- Giảm chức năng**: không kiểm soát tiền xu, không có tài khoản phụ, không có Lightning
- Quét chuyên sâu**: phát hiện thanh toán tiêu tốn nhiều tài nguyên



## Thực hành tốt nhất



### An toàn seed



Ngay cả với các bài kiểm tra Signet có nền tảng không đáng tin cậy, hãy cẩn thận với cụm từ khôi phục của bạn. Sử dụng tùy chọn "Hiển thị cụm từ seed" trong phần cài đặt để ghi lại cẩn thận. Để thực hành tốt, hãy duy trì các ví hoàn toàn riêng biệt cho Signet và Mainnet: không bao giờ sử dụng seed được tạo để kiểm tra trên wallet với mục đích nhận tiền thật.



### Cảnh báo về tình trạng thử nghiệm



Dana Wallet vẫn được các nhà phát triển coi là phiên bản thử nghiệm. Họ đã nêu rõ: "Đừng sử dụng số tiền mà bạn không muốn mất". Để học hỏi, hãy chọn phiên bản Signet. Nếu bạn sử dụng phiên bản Mainnet, hãy giới hạn ở mức token.



### Sao lưu và phục hồi



Việc khôi phục quỹ Thanh toán Im lặng yêu cầu wallet tương thích với giao thức BIP-352. wallet tiêu chuẩn không thể quét blockchain để truy xuất UTXO Thanh toán Im lặng của bạn. Hãy giữ Dana Wallet được cài đặt hoặc sử dụng tùy chọn "Khôi phục" khi khởi chạy lần đầu để khôi phục wallet hiện có.



## So sánh với BIP-47 và PayJoin



| Critère | Silent Payments (BIP-352) | BIP-47 PayNyms | PayJoin (BIP-78) |
|---------|---------------------------|----------------|------------------|
| Adresse statique | Oui (`sp1...`) | Oui (code de paiement) | Non |
| Interaction requise | Aucune | Transaction de notification initiale | À chaque paiement |
| Empreinte on-chain | Aucune (transactions normales) | OP_RETURN visible | Transaction modifiée |
| Scan côté receveur | Intensif (chaque bloc) | Léger (après notification) | Aucun |
| Confidentialité expéditeur | Excellente | Limitée (lien après notification) | Bonne (brouillage) |

Thanh toán im lặng loại bỏ giao dịch thông báo BIP-47 với chi phí quét đắt hơn. PayJoin giải quyết một vấn đề khác (tương quan đầu vào) và có thể kết hợp với Thanh toán im lặng.



## Phần kết luận



Dana Wallet là một công cụ giáo dục hữu ích để tìm hiểu về Thanh toán Im lặng trong môi trường không rủi ro. Cách tiếp cận tối giản của nó cho phép bạn hiểu các cơ chế cơ bản của giao thức BIP-352 mà không bị phân tâm bởi các tính năng phụ. Bằng cách thử nghiệm với Signet, bạn sẽ có được hiểu biết thực tế về công nghệ đầy hứa hẹn này cho tính bảo mật giao dịch Bitcoin.



Thanh toán im lặng là một bước tiến đáng kể trong việc dung hòa giữa tính dễ sử dụng và tôn trọng quyền riêng tư. Sự nhiệt tình của cộng đồng và những tích hợp đầu tiên vào nhiều loại ví khác nhau (Cake Wallet, BitBox02, BlueWallet để gửi tiền) mở ra một tương lai mà việc công bố địa chỉ quyên góp sẽ không còn xâm phạm quyền riêng tư tài chính của chủ sở hữu.



## Tài nguyên



### Tài liệu chính thức




- Kho lưu trữ GitHub Dana Wallet: https://github.com/cygnet3/danawallet
- Tiền gửi F-Cold: https://fdroid.silentpayments.dev
- Trang web cộng đồng Silent Payments: https://silentpayments.xyz
- Thông số kỹ thuật BIP-352: https://bips.dev/352



### Công cụ kiểm tra Signet




- Faucet Thanh toán im lặng: https://silentpayments.dev/faucet/signet
- Signet Mempool Explorer: https://mempool.space/signet



### Máy chủ Blindbit (tự lưu trữ)




- Oracle Blindbit (GitHub): https://github.com/setavenger/blindbit-oracle