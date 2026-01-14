---
name: Bitcoin Keeper
description: Bitcoin di động, wallet dùng cho mục đích an ninh và multi-sig
---

![cover](assets/cover.webp)



Việc quản lý Bitcoin một cách an toàn là một thách thức lớn đối với bất kỳ người nắm giữ nào nhận thức được tầm quan trọng của chủ quyền tài chính. Giữa sự đơn giản của wallet trên thiết bị di động và sự mạnh mẽ của giải pháp multi-sig, khoảng cách kỹ thuật có thể gây khó khăn cho nhiều người dùng. Bitcoin Keeper được định vị chính xác tại điểm giao nhau này, cung cấp một cách tiếp cận tiên tiến về bảo mật, đồng hành cùng người dùng trong quá trình phát triển của họ.



Bitcoin Keeper là một ứng dụng di động mã nguồn mở, dành riêng cho Bitcoin, được phát triển bởi nhóm BitHyve. Tham vọng của ứng dụng là giúp việc quản lý danh mục đầu tư nâng cao trở nên dễ tiếp cận, đặc biệt là các cấu hình đa chữ ký, đồng thời duy trì giao diện trực quan cho người mới bắt đầu. Ứng dụng sử dụng khẩu hiệu "Bảo mật hôm nay, Lập kế hoạch cho ngày mai", phản ánh triết lý hỗ trợ lâu dài của họ.



Không giống như các ví đa năng quản lý nhiều loại tiền điện tử, Bitcoin Keeper tập trung nghiêm ngặt vào Bitcoin. Cách tiếp cận chỉ dành cho Bitcoin này giúp giảm thiểu bề mặt tấn công tiềm tàng và đơn giản hóa đáng kể trải nghiệm người dùng. Ứng dụng này cũng nổi bật nhờ khả năng tích hợp nguyên bản với các ví phần cứng phổ biến nhất và các tính năng quản lý UTXO tiên tiến.



## Bitcoin Keeper là gì?



### Triết lý và mục tiêu



Bitcoin Keeper được thiết kế để đáp ứng nhu cầu cụ thể của những người dùng Bitcoin muốn giữ toàn quyền kiểm soát khóa riêng tư của họ. Dự án này hoàn toàn tuân thủ các nguyên tắc cơ bản của Bitcoin: mã nguồn mở và có thể kiểm toán, tôn trọng quyền riêng tư và chủ quyền của người dùng. Không cần đăng ký hoặc cung cấp thông tin cá nhân để sử dụng ứng dụng, và thậm chí nó có thể hoạt động ngoại tuyến cho các thao tác ký.



Mục tiêu chính là cung cấp một công cụ linh hoạt, có khả năng đáp ứng nhu cầu trong tương lai để lưu trữ BTC trong nhiều năm, thậm chí nhiều thế hệ, nhờ vào các chức năng kế thừa. Ứng dụng cho phép người dùng bắt đầu đơn giản với một thiết bị wallet di động, và sau đó dần dần nâng cấp lên các giải pháp đa chữ ký an toàn hơn.



### Kiến trúc ứng dụng



Bitcoin Keeper tổ chức quản lý quỹ dựa trên hai khái niệm riêng biệt. **Hot Wallet** là một wallet đơn giản với một chìa khóa duy nhất, được lưu trữ trên điện thoại, được thiết kế cho chi tiêu hàng ngày và số tiền nhỏ. **Vaults** là các két sắt đa chữ ký (đa chìa khóa) yêu cầu nhiều chìa khóa để ủy quyền chi tiêu, được thiết kế để lưu trữ an toàn lâu dài.



### Các tính năng chính



Bitcoin Keeper hỗ trợ hầu hết các ví phần cứng trên thị trường: Coldcard, Trezor, Ledger, Keystone, BitBox02, Jade, Seedsigner, Passport và Tapsigner của Coinkite. Quá trình tích hợp diễn ra thông qua các phương pháp khác nhau tùy thuộc vào thiết bị: quét mã QR, kết nối NFC hoặc nhập tập tin.



Ứng dụng này cũng cung cấp khả năng quản lý UTXO nâng cao với tính năng gắn nhãn giao dịch, kiểm soát tiền xu để chọn thủ công các đầu vào khi gửi và hỗ trợ định dạng PSBT cho các giao dịch được ký một phần.



## Cài đặt và cấu hình ban đầu



Bitcoin Keeper có sẵn miễn phí trên Android thông qua Google Play Store và trên iOS thông qua App Store. Nhà phát hành được ghi nhận là BitHyve. Trước khi cài đặt, hãy đảm bảo thiết bị của bạn không bị nhiễm phần mềm độc hại, đã được cập nhật và không bị root hoặc jailbreak.



Khi khởi chạy lần đầu, ứng dụng sẽ yêu cầu bạn tạo mã PIN bảo mật. Mã này bảo vệ quyền truy cập vào wallet của bạn và mã hóa dữ liệu nhạy cảm cục bộ. Hãy chọn một mã mạnh và ghi nhớ nó. Sau đó, bạn có thể kích hoạt xác thực sinh trắc học (vân tay hoặc nhận diện khuôn mặt) để mở khóa nhanh hơn.



![Installation et configuration du PIN](assets/fr/01.webp)



Ứng dụng sau đó hiển thị một số màn hình giới thiệu giải thích ba trụ cột của nó: tạo wallet để gửi và nhận bitcoin, quản lý khóa với khả năng tương thích phần cứng wallet, và lập kế hoạch kế thừa để chuyển giao bitcoin. Nhấn "Bắt đầu", sau đó chọn "Tạo mới" để tạo cấu hình mới.



![Écrans d'introduction](assets/fr/02.webp)



## Khám phá giao diện



Giao diện của Bitcoin Keeper được tổ chức xung quanh bốn tab chính, có thể truy cập từ thanh điều hướng phía dưới:



![Les quatre onglets de l'application](assets/fr/03.webp)



Tab **Ví** hiển thị các ví của bạn và số dư trong đó. Đây là nơi bạn truy cập ví để gửi và nhận bitcoin. Các thẻ "Hot Wallet" và "Khóa đơn" hoặc "Khóa đa" cho phép bạn nhanh chóng xác định loại của từng wallet.



Tab **Khóa** tập trung quản lý các khóa chữ ký của bạn. Tại đây, bạn sẽ tìm thấy Khóa Di động do ứng dụng tạo ra, cũng như tất cả các khóa được nhập từ ví phần cứng. Đây cũng là nơi bạn thêm các thiết bị ký mới.



Mục **Dịch vụ hỗ trợ** cung cấp các dịch vụ hỗ trợ: gửi câu hỏi đến nhóm hỗ trợ và kết nối với các cố vấn của Bitcoin để được hỗ trợ cá nhân hóa.



Tab **Thêm** (Tùy chọn khác) cho phép truy cập vào các cài đặt như kết nối máy chủ cá nhân, sao lưu khóa, tài liệu thừa kế, tùy chọn hiển thị và quản lý wallet.



## Kết nối với máy chủ của riêng bạn



Để tăng cường tính bảo mật, Bitcoin Keeper cho phép bạn kết nối ứng dụng với máy chủ Electrum của riêng bạn, thay vì sử dụng các máy chủ công cộng mặc định.



![Configuration du serveur Electrum](assets/fr/04.webp)



Từ tab Thêm, cuộn xuống để tìm cài đặt máy chủ. Nhấn "Thêm máy chủ" để cấu hình kết nối mới. Bạn có thể chọn giữa "Máy chủ công cộng" (các máy chủ công cộng được cấu hình sẵn) và "Electrum riêng tư" (máy chủ của riêng bạn).



Đối với máy chủ riêng, hãy nhập URL (ví dụ: umbrel.local cho nút Umbrel) và số cổng (thường là 50001). Kích hoạt SSL nếu máy chủ của bạn hỗ trợ. Bạn cũng có thể quét mã QR cấu hình. Sau khi nhập các thông số, nhấn "Kết nối với máy chủ".



Nếu bạn chưa có máy thắt nút Bitcoin, hãy xem hướng dẫn của chúng tôi về Umbrel, một cách đơn giản và tiết kiệm để tự tạo máy thắt nút:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

## Nhận bitcoin



Từ tab Ví, chọn wallet mà bạn muốn nhận tiền bằng cách nhấn vào đó. Màn hình wallet sẽ hiển thị số dư và ba nút hành động: Gửi Bitcoin, Nhận Bitcoin và Xem tất cả tiền điện tử.



![Réception de bitcoins](assets/fr/05.webp)



Nhấn "Nhận Bitcoin". Bitcoin Keeper sẽ tạo ra một địa chỉ nhận mới ở định dạng Bech32 (bắt đầu bằng bc1...), cùng với mã QR của địa chỉ đó. Bạn có thể thêm nhãn vào địa chỉ này để xác định nguồn tiền. Chia sẻ địa chỉ với người gửi bằng cách hiển thị mã QR hoặc sao chép địa chỉ dạng văn bản.



Ứng dụng tự động tạo địa chỉ mới cho mỗi lần nhận cuộc gọi, bảo vệ quyền riêng tư của bạn. Sử dụng chức năng "Nhận Address mới" để nhận địa chỉ trống nếu cần.



## Quản lý UTXO



Bitcoin Keeper cung cấp khả năng hiển thị đầy đủ UTXO (Các giao dịch chưa sử dụng) tạo nên số dư của bạn. Từ màn hình wallet, nhấn "Xem tất cả tiền xu" để truy cập trình quản lý góc.



![Gestion des UTXO](assets/fr/06.webp)



Màn hình "Quản lý tiền xu" hiển thị từng UTXO riêng lẻ với số lượng và nhãn của nó. Chế độ xem này cho phép bạn theo dõi nguồn gốc tiền xu của mình và sắp xếp chúng. Bạn có thể chọn các UTXO cụ thể thông qua "Chọn để gửi" để gửi kèm quyền kiểm soát tiền xu, do đó tránh việc trộn lẫn tiền xu từ các nguồn gốc khác nhau.



## Gửi bitcoin



Để gửi, hãy chọn danh mục nguồn và nhấn "Gửi Bitcoin". Nhập địa chỉ người nhận (dán hoặc quét qua mã QR) và tùy chọn thêm nhãn để xác định người nhận.



![Envoi de bitcoins](assets/fr/07.webp)



Màn hình tiếp theo cho phép bạn nhập số tiền cần gửi. Giao diện hiển thị số dư khả dụng và tỷ giá quy đổi tiền tệ. Chọn mức độ ưu tiên thanh toán: Thấp (tiết kiệm, ~60 phút), Trung bình hoặc Cao (ưu tiên). Cước phí ước tính tính bằng sats/vbyte được hiển thị theo thời gian thực. Nhấn "Gửi" để tiếp tục.



![Confirmation et envoi](assets/fr/08.webp)



Màn hình tóm tắt hiển thị tất cả các chi tiết: nguồn wallet, địa chỉ đích, độ ưu tiên giao dịch, phí mạng, số tiền đã gửi và tổng số tiền. Vui lòng kiểm tra kỹ thông tin này, vì giao dịch Bitcoin không thể đảo ngược. Nhấn "Xác nhận & Gửi" để gửi giao dịch.



Thông báo "Gửi thành công" hiện ra cùng với tóm tắt đầy đủ. Giao dịch hiển thị trong lịch sử "Giao dịch gần đây" với nhãn của nó.



## Hãy cất giữ chìa khóa của bạn



Sao lưu Khóa Khôi phục là một bước rất quan trọng. Từ tab Thêm, hãy vào phần "Sao lưu và Khôi phục" và nhấp vào "Khóa Khôi phục".



![Sauvegarde de la Recovery Key](assets/fr/09.webp)



Màn hình hiển thị trạng thái các bản sao lưu của bạn. Để xác minh bản sao lưu, ứng dụng sẽ yêu cầu bạn xác nhận một từ cụ thể trong cụm từ của bạn (ví dụ: từ thứ 7). Việc xác minh này đảm bảo rằng bạn đã nhập đúng cụm từ khôi phục của mình.



Từ mục "Cài đặt Khóa Khôi phục", bạn có thể xem toàn bộ cụm từ của mình thông qua mục "Xem Khóa Khôi phục" và xem Dấu vân tay người ký của khóa. Hãy giữ cụm từ 12 từ này trên giấy, ở nơi an toàn, tránh xa hơi ẩm và lửa. Tuyệt đối không lưu trữ nó trên thiết bị kết nối.



## Thêm khóa ngoài (phần cứng wallet)



Một trong những ưu điểm chính của Bitcoin Keeper là khả năng tích hợp ví phần cứng. Từ tab Khóa, nhấn "Thêm khóa" để thêm thiết bị ký điện tử mới.



![Ajout d'une clé hardware](assets/fr/10.webp)



Chọn "Thêm khóa từ phần cứng" để kết nối thiết bị phần cứng wallet. Ứng dụng hỗ trợ nhiều loại thiết bị: BitBox02, Coldcard, Blockstream Jade, Keystone, Krux, Ledger, Foundation Passport, TwentyTwo Portal, Seedsigner và Specter Solutions.



### Cấu hình Tapsigner



Tapsigner là một thẻ NFC của Coinkite đặc biệt phù hợp cho việc sử dụng trên thiết bị di động. Nếu bạn muốn tìm hiểu thêm, chúng tôi có một hướng dẫn chi tiết:



https://planb.academy/tutorials/wallet/hardware/tapsigner-ab2bcdf9-9509-4908-9a4a-2f2be1e7d5d2

Để thêm Tapsigner, hãy chọn nó từ danh sách ví phần cứng.



![Configuration du Tapsigner](assets/fr/11.webp)



Trước tiên, nhập mã PIN gồm 6-32 chữ số được in ở mặt sau thẻ (mặc định trên thẻ mới), hoặc mã PIN nếu bạn đã thiết lập trước đó. Nhấn "Tiếp tục", sau đó đưa thiết bị Tapsigner lại gần mặt sau điện thoại khi màn hình hiển thị "Sẵn sàng quét". Giao tiếp NFC sẽ tự động nhập khóa công khai. Sau đó, bạn có thể thêm mô tả (ví dụ: "Thẻ Métro") để xác định khóa này.



## Tạo danh mục đầu tư đa chữ ký



Sau khi thiết lập khóa, bạn có thể tạo wallet đa chữ ký bằng cách kết hợp nhiều thiết bị. Từ tab Ví, hãy nhấp vào "Thêm Wallet".



![Création d'un nouveau wallet](assets/fr/12.webp)



Bạn có ba lựa chọn: "Tạo Wallet" cho danh mục đầu tư mới, "Nhập Wallet" để khôi phục wallet hiện có hoặc "Wallet cộng tác" cho kho lưu trữ dùng chung. Chọn "Tạo Wallet" rồi chọn "Bitcoin Wallet".



![Sélection du type de wallet](assets/fr/13.webp)



Màn hình tiếp theo cung cấp các cấu hình khác nhau: "Một phím", "2 trong 3 phím", hoặc "3 trong 5 phím". Đối với multi-sig tùy chỉnh, hãy nhấn "Chọn thiết lập tùy chỉnh". Ví dụ, chọn "1 trong 2": cần một chữ ký duy nhất từ hai phím khả dụng.



Tiếp theo, hãy chọn các khóa sẽ tạo nên Kho tiền của bạn. Trong ví dụ này, chúng tôi kết hợp "Khóa di động" (khóa phần mềm điện thoại) với "TAPSIGNER" (Thẻ Metro). Cấu hình này cung cấp tính dự phòng: nếu một trong các khóa không thể truy cập được, bạn vẫn có thể sử dụng tiền của mình bằng khóa còn lại.



![Finalisation du wallet multisig](assets/fr/14.webp)



Đặt tên cho wallet của bạn (ví dụ: "Test PlanB"), thêm mô tả tùy chọn và chọn các khóa đã chọn. Nhấn "Tạo Wallet của bạn". Một thông báo xác nhận "Wallet đã được tạo thành công" sẽ hiện ra, nhắc bạn lưu tệp khôi phục wallet.



Thiết bị wallet đa chữ ký mới của bạn hiện đã xuất hiện trong tab Ví với thẻ "Multi-key" và chỉ báo "1 trong 2".



### Lưu tệp cấu hình



**Không giống như wallet thông thường, nơi chỉ cần cụm từ khôi phục là đủ để khôi phục quyền truy cập, wallet đa chữ ký cũng yêu cầu tệp cấu hình mô tả cấu trúc của két sắt (những khóa nào tham gia, cần bao nhiêu chữ ký). Nếu không có tệp này, ngay cả khi có đầy đủ các cụm từ khôi phục, bạn cũng không thể khôi phục lại wallet của mình.**



![Export du fichier de configuration](assets/fr/15.webp)



Để xuất tập tin này, hãy chọn thiết bị wallet multisig của bạn trong tab Ví, sau đó nhấn vào biểu tượng Cài đặt (hình bánh răng) ở góc trên bên phải. Trong "Cài đặt Wallet", hãy nhấp vào "Tập tin cấu hình Wallet". Có một số tùy chọn xuất:





- Xuất PDF**: tạo tài liệu PDF chứa tất cả thông tin về wallet.
- Hiển thị mã QR**: hiển thị mã QR có thể quét được để nhập cấu hình vào thiết bị khác.
- AirDrop / Xuất tập tin**: xuất tập tin thông qua các tùy chọn chia sẻ của điện thoại.
- NFC**: chia sẻ qua NFC với thiết bị tương thích



Hãy giữ tệp cấu hình này riêng biệt với các cụm từ khôi phục của bạn, tốt nhất là trên phương tiện được mã hóa hoặc bản in. Nếu bạn làm mất điện thoại, tệp này kết hợp với các cụm từ khôi phục cho mỗi khóa tham gia sẽ cho phép bạn khôi phục chữ ký đa chữ ký wallet trên Bitcoin Keeper hoặc bất kỳ phần mềm tương thích nào khác.



## Thực tiễn tốt nhất



### Tổ chức quỹ



Hãy phân bổ Bitcoin của bạn theo mục đích sử dụng: một khóa đơn wallet "nóng" cho các chi tiêu hiện tại với số lượng hạn chế, và một hoặc nhiều khóa đa Vaults cho mục đích tiết kiệm dài hạn. Việc gắn thẻ UTXO một cách có hệ thống sẽ giúp bạn theo dõi nguồn gốc tiền của mình, điều này đặc biệt hữu ích cho việc quản lý tính bảo mật và tránh trộn lẫn các loại tiền điện tử có nguồn gốc khác nhau.



Hãy bảo vệ điện thoại của bạn: kích hoạt khóa sinh trắc học, cập nhật hệ thống thường xuyên và luôn cảnh giác với các ứng dụng đã cài đặt. Và hãy luôn cập nhật Bitcoin Keeper với các bản vá bảo mật.



### Bảo mật sao lưu



Hãy giữ ít nhất hai bản sao của mỗi cụm từ khôi phục trên giấy, cất giữ ở các địa điểm khác nhau về mặt địa lý. Đối với số tiền lớn, hãy cân nhắc sử dụng kim loại khắc laser, có khả năng chống chịu thiên tai. Tuyệt đối không lưu trữ các cụm từ này trên thiết bị kết nối với Internet và không bao giờ chụp ảnh chúng.



Đối với multi-sig Vaults, hãy lưu cả tệp cấu hình (Tệp Khôi phục Wallet), chứa các khóa công khai tham gia và cấu trúc vault. Tệp này, kết hợp với các cụm từ khôi phục khóa, cho phép xây dựng lại wallet trên bất kỳ phần mềm tương thích nào như Sparrow hoặc Specter.



## Ưu điểm và hạn chế



### Điểm nổi bật





- Ứng dụng chỉ dành cho Bitcoin giúp giảm độ phức tạp và rủi ro.
- Tích hợp trực tiếp các Vault đa chữ ký với hướng dẫn từng bước.
- Hỗ trợ phần cứng mở rộng cho wallet (Tapsigner, Coldcard, Ledger, Jade, v.v.)
- Quản lý nâng cao UTXO và kiểm soát tiền xu
- Có thể kết nối với máy chủ Electrum cá nhân.
- Mã nguồn mở, có thể kiểm toán



### Các ràng buộc cần xem xét





- Interface chủ yếu bằng tiếng Anh
- Một số tính năng cao cấp (Sao lưu đám mây, Máy chủ hỗ trợ) yêu cầu nâng cấp.
- Cấu hình Multisig yêu cầu đào tạo ban đầu.



## Phần kết luận



Bitcoin Keeper nổi bật như một giải pháp có khả năng mở rộng để quản lý bitcoin của bạn. Cách tiếp cận tiên tiến của nó, từ wallet đơn giản đến các Vault đa chữ ký, có nghĩa là bảo mật có thể được nâng cấp khi nhu cầu thay đổi. Khả năng dễ dàng tích hợp các ví phần cứng như Tapsigner mở đường cho các cấu hình mạnh mẽ mà không quá phức tạp.



Việc chỉ sử dụng bitcoin, mã nguồn mở và tôn trọng quyền riêng tư khiến nó trở thành lựa chọn phù hợp với các giá trị cốt lõi của hệ sinh thái Bitcoin.



Hướng dẫn này bao gồm các tính năng thiết yếu của Bitcoin Keeper ở phiên bản miễn phí. Ứng dụng cũng cung cấp các tính năng cao cấp (Sao lưu đám mây, Sao lưu máy chủ hỗ trợ, Ví Canary) sẽ được đề cập trong một hướng dẫn riêng. Trong hướng dẫn sắp tới, chúng ta cũng sẽ khám phá tính năng Lập kế hoạch thừa kế, cho phép bạn chuẩn bị việc chuyển giao bitcoin cho người thân yêu, nhờ vào Kho lưu trữ nâng cao và các tài liệu đi kèm được tích hợp trong ứng dụng.



## Tài nguyên





- Trang web chính thức: [bitcoinkeeper.app](https://bitcoinkeeper.app)
- Trung tâm trợ giúp: [help.bitcoinkeeper.app](https://help.bitcoinkeeper.app)
- Mã nguồn: [github.com/bithyve/bitcoin-keeper](https://github.com/bithyve/bitcoin-keeper)
- Telegram : [t.me/BitcoinKeeper](https://t.me/BitcoinKeeper)
- Twitter/X: [@bitcoinkeeper_](https://x.com/bitcoinkeeper_)