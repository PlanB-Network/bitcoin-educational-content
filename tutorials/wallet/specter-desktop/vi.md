---
name: Máy tính để bàn Spectre
description: Quản lý danh mục đầu tư Bitcoin đa chữ ký của bạn trong quyền tự chủ hoàn toàn với nút riêng của bạn
---

![cover](assets/cover.webp)



Spectre Desktop là một ứng dụng mã nguồn mở (giấy phép MIT) được Cryptoadvance phát triển từ năm 2019, giúp bạn dễ dàng quản lý ví Bitcoin bằng ví phần cứng (Ledger, Trezor, Coldcard, BitBox02, Passport, v.v.) và cơ sở hạ tầng Bitcoin của riêng bạn (nút Bitcoin Core hoặc máy chủ Electrum). Ứng dụng này đặc biệt hiệu quả trong các cấu hình đa chữ ký, cho phép bạn bảo mật số tiền lớn bằng cách phân phối quyền ký giữa nhiều ví phần cứng độc lập.



**Trong hướng dẫn này, bạn sẽ học cách:**




- Cài đặt và cấu hình Spectre Desktop trên máy tính của bạn (Windows, macOS hoặc Linux)
- Kết nối Spectre với máy chủ Electrum (chúng tôi sẽ sử dụng Umbrel trong ví dụ này)
- Tạo wallet đơn giản với phần cứng wallet (Coldcard)
- Nhận và gửi bitcoin với chủ quyền hoàn toàn
- Thiết lập wallet đa chữ ký 2-on-3 với nhiều ví phần cứng
- Cài đặt Spectre trên máy chủ Umbrel (phần thưởng nâng cao)



Mọi giao dịch của bạn sẽ được xác thực cục bộ thông qua cơ sở hạ tầng của riêng bạn, không truyền bất kỳ thông tin nào đến máy chủ bên ngoài, đảm bảo tính bảo mật và chủ quyền tài chính của bạn. Luôn kiểm tra giao dịch trên màn hình phần cứng wallet trước khi ký.



## Tải xuống và cài đặt



Truy cập trang web chính thức của Spectre Desktop để tải ứng dụng.



![Page d'accueil Specter](assets/fr/01.webp)



Trên trang tải xuống, hãy chọn phiên bản tương ứng với hệ điều hành của bạn: macOS, Windows hoặc Linux.



![Téléchargement selon l'OS](assets/fr/02.webp)



Sau khi tải xuống, hãy cài đặt ứng dụng theo hướng dẫn thông thường của hệ điều hành. Đối với macOS, hãy kéo biểu tượng vào mục Ứng dụng. Đối với Windows, hãy chạy trình cài đặt. Đối với Linux, hãy làm theo hướng dẫn sử dụng.



## Cấu hình ban đầu



Khi khởi chạy lần đầu, Spectre Desktop sẽ yêu cầu bạn chọn loại kết nối. Bạn có thể kết nối với máy chủ Electrum hoặc với nút Bitcoin Core của riêng bạn.



![Choix du type de connexion](assets/fr/03.webp)



Trong ví dụ này, chúng tôi sẽ sử dụng kết nối tới máy chủ Electrum chạy trên Umbrel.



Để biết thêm thông tin, vui lòng tham khảo hướng dẫn về Umbrel của chúng tôi:



https://planb.academy/tutorials/node/bitcoin/umbrel-8b0e3b5b-d3cf-4a1e-8bb8-1ad2db4dd848

Tùy chọn này cung cấp khả năng đồng bộ hóa nhanh hơn Bitcoin Core. Nếu muốn, bạn có thể chọn "Bitcoin Core" và cấu hình kết nối đến nút cục bộ của mình. Các bước sau đây vẫn giữ nguyên bất kể bạn chọn gì.



Chọn "Kết nối Electrum" rồi chọn "Nhập của riêng tôi" để cấu hình máy chủ Electrum của riêng bạn.



![Configuration Electrum](assets/fr/04.webp)



Nhập địa chỉ máy chủ Electrum của bạn. Trong trường hợp của chúng tôi với Umbrel, địa chỉ sẽ là `umbrel.local` với cổng `50001`. Nhấp vào "Kết nối" để thiết lập kết nối.



Sau khi kết nối, màn hình chào mừng sẽ xuất hiện, kèm theo danh sách kiểm tra để bạn bắt đầu. Bây giờ, bạn cần thêm ví phần cứng của mình.



![Écran d'accueil](assets/fr/05.webp)



## Thêm phần cứng wallet



Trong menu bên trái, nhấp vào "Thêm thiết bị" để thêm phần cứng wallet của bạn.



Spectre Desktop hỗ trợ nhiều ví phần cứng: Trezor, Ledger, BitBox02, Coldcard, KeepKey, Keystone, Cobo Vault và nhiều ví khác.



Nếu bạn muốn tìm hiểu thêm, hãy xem hướng dẫn về phần cứng wallet của chúng tôi.



![Sélection du type de hardware wallet](assets/fr/06.webp)



Chọn phần cứng wallet của bạn. Trong ví dụ này, chúng tôi sử dụng Coldcard MK4.



Dưới đây bạn sẽ tìm thấy hướng dẫn của chúng tôi về phần cứng wallet này:



https://planb.academy/tutorials/wallet/hardware/coldcard-5d44dd94-423d-4e37-9a8c-3fc38b45ce59

Đối với Coldcard, bạn cần xuất khóa công khai từ phần cứng wallet thông qua kết nối USB hoặc thẻ nhớ microSD.



![Import des clés du Coldcard](assets/fr/07.webp)



Làm theo hướng dẫn hiển thị để xuất khóa từ Coldcard của bạn. Đặt tên cho phần cứng wallet (ở đây là "MK4 Tuto"). Sau khi nhập khóa, bạn có thể tạo wallet với một khóa duy nhất hoặc thêm các ví phần cứng khác cho wallet đa chữ ký.



![Dispositif ajouté](assets/fr/08.webp)



## Tạo danh mục đầu tư



Sau khi thêm phần cứng wallet, hãy nhấp vào "Tạo khóa đơn wallet" để tạo wallet có chữ ký đơn.



Đặt tên cho danh mục đầu tư của bạn (ví dụ: "Wallet for tuto") và chọn loại địa chỉ. Chọn "Segwit" để sử dụng địa chỉ bech32 gốc giúp tối ưu hóa chi phí giao dịch.



![Configuration du portefeuille](assets/fr/09.webp)



Sau khi danh mục đầu tư của bạn được tạo, Spectre sẽ đề nghị lưu một tệp PDF sao lưu chứa tất cả thông tin công khai cần thiết để khôi phục danh mục đầu tư của bạn (mô tả, khóa công khai mở rộng). Tệp này không chứa khóa riêng tư của bạn.



![Sauvegarde du portefeuille](assets/fr/10.webp)



## Nhận bitcoin



Để nhận bitcoin, hãy chọn wallet của bạn trong menu bên trái, sau đó nhấp vào tab "Nhận".



Spectre tự động tạo địa chỉ tiếp nhận mới bằng mã QR.



![Génération d'une adresse de réception](assets/fr/11.webp)



Bạn có thể sao chép địa chỉ hoặc quét mã QR. Luôn kiểm tra địa chỉ trên màn hình phần cứng wallet trước khi chuyển cho bất kỳ ai.



## Xem lịch sử và địa chỉ



Sau khi nhận được bitcoin, bạn có thể xem các giao dịch của mình trong tab "Giao dịch".



![Historique des transactions](assets/fr/12.webp)



Tab "Địa chỉ" cho phép bạn xem tất cả các địa chỉ được danh mục đầu tư của bạn tạo ra, cùng với trạng thái sử dụng và số tiền liên quan.



![Liste des adresses](assets/fr/13.webp)



## Gửi bitcoin



Để gửi Bitcoin, hãy nhấp vào tab "Gửi". Nhập địa chỉ người nhận, số tiền cần gửi và chọn tùy chọn nâng cao nếu bạn muốn tự tay chọn UTXO (kiểm soát tiền).



![Création d'une transaction](assets/fr/14.webp)



Nhấp vào "Tạo Giao dịch Chưa ký" để tạo giao dịch. Sau đó, Spectre sẽ yêu cầu bạn ký giao dịch bằng phần cứng wallet của bạn.



![Signature de la transaction](assets/fr/15.webp)



Nếu bạn đang sử dụng Coldcard, bạn có thể chọn ký qua USB hoặc sử dụng thẻ nhớ microSD (không kết nối mạng). Xác nhận giao dịch trên màn hình phần cứng wallet, kiểm tra kỹ địa chỉ nhận và số tiền.



Sau khi giao dịch được ký, bạn có thể phát nó trên mạng Bitcoin.



![Options de diffusion](assets/fr/16.webp)



Nhấp vào "Gửi giao dịch" để gửi giao dịch. Spectre sẽ xác nhận giao dịch của bạn đã được gửi và bạn có thể theo dõi trạng thái của giao dịch trong tab Giao dịch.



![Diffusion de la transaction](assets/fr/17.webp)



## Tạo và sử dụng danh mục đầu tư đa chữ ký



Một trong những lợi thế lớn của Spectre Desktop là khả năng đơn giản hóa việc quản lý danh mục đầu tư đa chữ ký. Một wallet đa chữ ký yêu cầu nhiều chữ ký để xác thực một giao dịch, do đó loại bỏ điểm lỗi đơn lẻ. Ví dụ: cấu hình 2-on-3 yêu cầu hai chữ ký từ ba ví phần cứng riêng biệt để xác thực bất kỳ khoản chi tiêu nào.



Để tạo wallet đa chữ ký, hãy bắt đầu bằng cách thêm tất cả các ví phần cứng ký thông qua "Thêm thiết bị". Trong ví dụ này, chúng tôi sẽ sử dụng ba ví phần cứng khác nhau: Coldcard MK4 (đã thêm trước đó), Passport và Ledger. Sự đa dạng hóa các nhà sản xuất này giúp tăng cường bảo mật bằng cách tránh sự phụ thuộc vào một chuỗi cung ứng hoặc phần mềm duy nhất.



Sau đây là các liên kết đến hướng dẫn về Ledger và Passport:



https://planb.academy/tutorials/wallet/hardware/ledger-nano-s-plus-75043cb3-2e8e-43e8-862d-ca243b8215a4

https://planb.academy/tutorials/wallet/hardware/passport-74e53858-3fa2-43f9-b866-573297546236

Thêm Passport bằng cách đặt tên cho phần cứng wallet (ví dụ: "Passport multi") và nhập khóa của nó qua thẻ nhớ microSD hoặc mã QR. Sau đó, nhấp vào "Tiếp tục" để tiếp tục.



![Ajout du Passport](assets/fr/23.webp)



Sau đó, thêm Ledger bằng cách kết nối qua USB và mở ứng dụng Bitcoin trên phần cứng wallet. Đặt tên (ví dụ: "ledger multi") và nhấp vào "Lấy qua USB" rồi "Tiếp tục" để nhập khóa công khai của nó.



![Ajout du Ledger](assets/fr/24.webp)



Sau khi đã đăng ký ba ví phần cứng của bạn trong Spectre, hãy nhấp vào "Thêm wallet" và chọn tùy chọn "Nhiều chữ ký" để tạo wallet nhiều chữ ký.



![Choix du type de wallet](assets/fr/25.webp)



Chọn ba ví phần cứng bạn muốn đưa vào nhóm đa chữ ký của mình: MK4 Tuto, Passport multi và Ledger multi. Nhấp vào "Tiếp tục" để chuyển sang bước tiếp theo.



![Sélection des hardware wallets pour le multisig](assets/fr/26.webp)



Chọn cấu hình đa chữ ký của bạn. Chọn "Segwit" làm loại địa chỉ để được hưởng mức phí tối ưu. Tham số "Chữ ký cần thiết để ủy quyền giao dịch (m/3)" cho phép bạn xác định ngưỡng: đối với cấu hình 2-on-3, cần có 2 chữ ký. Mỗi phần cứng wallet sẽ hiển thị khóa đa chữ ký tương ứng. Nhấp vào "Tạo wallet" để hoàn tất việc tạo.



![Configuration 2-sur-3 Segwit](assets/fr/27.webp)



Danh mục đa chữ ký "Multi tuto" của bạn hiện đã được tạo. Spectre ngay lập tức khuyên bạn nên lưu tệp PDF sao lưu có chứa mô tả danh mục. Nhấp vào "Lưu PDF sao lưu" để tải xuống tệp quan trọng này.



![Wallet multisig créé](assets/fr/28.webp)



Spectre cũng cho phép bạn xuất thông tin wallet sang từng ví phần cứng thông qua mã QR hoặc tệp. Điều này cho phép một số ví phần cứng nhất định (như Coldcard hoặc Passport) lưu trữ cấu hình đa chữ ký trực tiếp trong bộ nhớ của chúng.



Đối với Passport, hãy mở khóa thiết bị, sau đó vào "Quản lý Tài khoản" > "Kết nối Wallet" > "Specter" > "Multisig" > "Mã QR", rồi quét mã QR do Specter tạo ra. Passport sẽ yêu cầu bạn quét địa chỉ nhận từ wallet để xác thực cấu hình đa chữ ký.



Đối với MK4, hãy cắm nó vào PC và mở khóa. Sau đó, nhấp vào "Lưu tệp hướng dẫn MK4" và lưu tệp vào MK4 của bạn. Lần tới khi bạn ký phần cứng wallet, MK4 sẽ sử dụng tệp này để hoàn tất việc cấu hình đa chữ ký.



![Export vers les hardware wallets](assets/fr/29.webp)



Để bạn biết, bạn có thể truy cập bản sao lưu bất kỳ lúc nào từ tab "Cài đặt" trong danh mục đầu tư của mình, sau đó chọn "Xuất":



![Accès au backup PDF](assets/fr/30.webp)



Việc sử dụng hàng ngày vẫn tương tự như wallet đơn giản: bạn vẫn nhận địa chỉ generate như bình thường. Để gửi bitcoin, hãy vào tab "Gửi", nhập địa chỉ người nhận và số tiền, sau đó nhấp vào "Tạo Giao dịch Chưa ký".



![Création d'une transaction multisig](assets/fr/31.webp)



Spectre xây dựng một PSBT (Partially Signed Bitcoin Transaction) và hiển thị "Đã có 0 trong số 2 chữ ký". Bây giờ bạn phải ký bằng ít nhất hai trong ba ví phần cứng của mình. Nhấp vào ví phần cứng wallet đầu tiên (ví dụ: "MK4 Tuto") để ký bằng Coldcard của bạn, sau đó nhấp vào ví thứ hai (ví dụ: "Passport multi") để lấy chữ ký thứ hai cần thiết.



![Signature de la transaction](assets/fr/32.webp)



Sau khi có được 2 chữ ký cần thiết (giao diện hiển thị "Đã có 2 trong số 2 chữ ký" và "Giao dịch đã sẵn sàng để gửi"), hãy nhấp vào "Gửi giao dịch" để phát giao dịch trên mạng Bitcoin.



![Transaction prête à être diffusée](assets/fr/33.webp)



Phương pháp đa chữ ký này đặc biệt phù hợp với các công ty (cần có sự chấp thuận của nhiều nhà quản lý đối với chi tiêu), gia đình (bảo vệ tài sản thừa kế qua nhiều thế hệ) hoặc cá nhân quản lý số tiền lớn (phân bổ ví phần cứng theo khu vực địa lý để chống chịu được các thảm họa cục bộ).



### Tầm quan trọng của việc sao lưu đa chữ ký



**Xin lưu ý**: việc sao lưu danh mục đầu tư đa chữ ký về cơ bản khác với việc sao lưu một danh mục đầu tư đơn lẻ. Chỉ riêng cụm từ khôi phục (cụm từ seed) của bạn là không đủ để khôi phục danh mục đầu tư đa chữ ký. Bạn cũng phải sao lưu **output descriptor** (output descriptor), trong đó chứa thông tin cấu hình cho danh mục đầu tư đa chữ ký của bạn.



output descriptor bao gồm dữ liệu thiết yếu: khóa công khai mở rộng (xpub) của mỗi người đồng ký, ngưỡng chữ ký (2-on-3 trong ví dụ của chúng tôi), loại tập lệnh được sử dụng (Segwit gốc, lồng nhau hoặc cũ) và đường dẫn bỏ qua cho mỗi phần cứng wallet. Nếu không có bộ mô tả này, ngay cả khi bạn có hai trong ba cụm từ khôi phục, bạn sẽ không thể xây dựng lại wallet hoặc truy cập bitcoin của mình. Bộ mô tả này cho phép phần mềm của bạn biết cách kết hợp các khóa công khai với generate và các địa chỉ Bitcoin tương ứng với số tiền của bạn.



Spectre Desktop tự động tạo một tệp PDF sao lưu khi bạn tạo danh mục đầu tư đa chữ ký. Tệp PDF này chứa mô tả đầy đủ, dấu vân tay của từng phần cứng wallet và tất cả thông tin công khai cần thiết để khôi phục. **Tệp này không chứa khóa riêng tư của bạn** và do đó không cho phép bạn chi tiêu bitcoin, nhưng nó cho phép bất kỳ ai truy cập vào tệp đều có thể xem toàn bộ lịch sử giao dịch và số dư của bạn.



Để sao lưu cấu hình đa chữ ký của bạn một cách chính xác, hãy làm theo quy trình sau: sau khi tạo danh mục đầu tư, hãy nhấp vào tab "Cài đặt", sau đó chọn "Xuất" và chọn "Lưu PDF sao lưu". Tạo nhiều bản sao của PDF này: in ít nhất hai bản ra giấy và giữ một bản sao kỹ thuật số được mã hóa. Lưu trữ một bản sao của PDF với mỗi cụm từ khôi phục của bạn, ở các vị trí địa lý riêng biệt.



Khắc cụm từ khôi phục của bạn lên các tấm kim loại chống cháy và chống nước để đảm bảo độ bền của chúng. Đừng bao giờ đánh giá thấp tầm quan trọng của những bản sao lưu này: nếu bạn làm mất thư mục `~/.specter` trên máy tính VÀ làm mất một trong các ví phần cứng mà không có bản sao lưu mô tả, toàn bộ tiền của bạn sẽ bị mất vĩnh viễn, ngay cả khi cấu hình 2-on-3. Dự phòng đa chữ ký bảo vệ chống lại việc mất phần cứng wallet, nhưng chỉ khi bạn đã sao lưu mô tả wallet đúng cách.



## Ưu điểm và hạn chế của Spectre Desktop



**Lợi ích**: Bảo mật tối ưu với xác thực cục bộ hoàn chỉnh mà không cần máy chủ của bên thứ ba. Linh hoạt đa chữ ký cho các cấu hình nâng cao (doanh nghiệp, gia đình, cá nhân). Hỗ trợ phần cứng wallet mở rộng với khả năng tương tác đầy đủ (USB và air-gapped).



**Hạn chế**: Đường cong học tập đáng kể về các khái niệm Bitcoin nâng cao (UTXO, mô tả, đường dẫn suy diễn).



## Thực hành tốt nhất



Luôn kiểm tra địa chỉ và số tiền trên màn hình phần cứng wallet trước khi xác thực để bảo vệ bạn khỏi phần mềm độc hại.



Giữ bản sao lưu PDF tách biệt với dữ liệu gốc của bạn. Các mô tả công khai này có thể được lưu trữ trong kho lưu trữ ngân hàng hoặc đám mây được mã hóa, giúp phục hồi dễ dàng mà không làm lộ khóa riêng tư của bạn.



Kiểm tra khả năng phục hồi trên các khoản token trước khi sử dụng danh mục đầu tư với số tiền lớn. Tạo, kiểm tra, xóa và khôi phục để xác thực quy trình của bạn.



Luôn cập nhật Spectre và chương trình cơ sở dữ liệu của bạn. Phân bổ người đồng ký đa chữ ký theo vị trí địa lý (nhà riêng/văn phòng/gần đó) để ứng phó với các thảm họa cục bộ. Sử dụng nhãn mô tả để hỗ trợ việc kế toán và khai thuế.



## Phần thưởng: Cài đặt trên máy chủ Bitcoin (Umbrel, RaspiBlitz, Start9)



Nếu bạn đã sở hữu máy chủ Bitcoin như Umbrel, RaspiBlitz, MyNode hoặc Start9, bạn có thể cài đặt Spectre Desktop trực tiếp từ kho ứng dụng của họ. Cách tiếp cận này mang lại một số lợi thế đáng kể: ứng dụng tự động cấu hình với nút Bitcoin Core cục bộ của bạn, có thể truy cập 24/7 thông qua giao diện web từ bất kỳ thiết bị nào trên mạng của bạn, và bạn thậm chí có thể truy cập từ xa một cách an toàn qua Tor. Toàn bộ cơ sở hạ tầng Bitcoin của bạn được tập trung trên một máy chủ chuyên dụng duy nhất, giúp đơn giản hóa việc quản lý và tăng cường quyền tự chủ của bạn.



### Cài đặt từ Umbrel App Store



Từ giao diện Umbrel, hãy vào App Store và tìm kiếm Spectre Desktop. Nhấp vào "Cài đặt" để bắt đầu cài đặt.



![App Store Umbrel - Specter Desktop](assets/fr/18.webp)



Sau khi cài đặt hoàn tất, hãy mở Spectre Desktop trên Umbrel. Màn hình chào mừng sẽ yêu cầu bạn chọn loại kết nối. Nếu bạn đang sử dụng Spectre trên Umbrel, hãy nhấp vào "Cập nhật cài đặt" để cấu hình kết nối.



![Écran de bienvenue Specter sur Umbrel](assets/fr/19.webp)



Chọn "Kết nối USB Spectre từ xa" để cho phép sử dụng ví phần cứng USB được kết nối với máy tính cục bộ của bạn trong khi sử dụng Spectre trên máy chủ Umbrel từ xa.



![Configuration Remote Specter USB](assets/fr/20.webp)



Làm theo hướng dẫn hiển thị để cấu hình Cầu nối HWI. Bạn cần truy cập cài đặt cầu nối thiết bị và thêm tên miền `http://umbrel.local:25441` vào danh sách trắng. Nhấp vào "Cập nhật" để lưu cấu hình.



![HWI Bridge Settings](assets/fr/21.webp)



Nếu bạn cũng muốn sử dụng ví phần cứng USB từ máy tính cục bộ, hãy tải ứng dụng Spectre Desktop về máy và đặt thành "Có, tôi chạy Spectre từ xa". Nhấp vào "Lưu" để hoàn tất cấu hình.



![Configuration connexion remote dans l'app](assets/fr/22.webp)



## Phần kết luận



Spectre Desktop phổ biến các cấu hình Bitcoin tiên tiến, cho phép đa chữ ký mà không ảnh hưởng đến quyền tự chủ hoặc tính bảo mật của bạn. Đối với người dùng quản lý số tiền lớn, Spectre Desktop chuyển đổi các hoạt động của tổ chức thành các giải pháp có thể được triển khai bởi các cá nhân.



Mặc dù ứng dụng yêu cầu đầu tư ban đầu vào cơ sở hạ tầng và đào tạo, nhưng nó mang lại quyền tự chủ hoàn toàn: kiểm soát cơ sở hạ tầng xác thực, quyền sở hữu vật lý đối với khóa và giao dịch không bị giám sát bởi bên thứ ba. Cho dù bạn là cá nhân bảo mật khoản tiết kiệm, một gia đình tạo ra két an toàn cho nhiều thế hệ, hay một công ty quản lý dòng tiền, Spectre Desktop là công cụ tham chiếu để cân bằng giữa bảo mật tối đa và quyền tự chủ tuyệt đối.



## Tài nguyên



### Tài liệu chính thức




- [Trang web chính thức của Specter Desktop](https://specter.solutions/desktop/)
- [Mã nguồn GitHub](https://github.com/cryptoadvance/specter-desktop)
- [Tài liệu đầy đủ](https://docs.specter.solutions/)



### Cộng đồng và hỗ trợ




- [Nhóm cộng đồng Specter trên Telegram](https://t.me/spectersupport)
- [Diễn đàn thảo luận Reddit](https://reddit.com/r/specterdesktop/)
- [Báo cáo lỗi GitHub](https://github.com/cryptoadvance/specter-desktop/issues)