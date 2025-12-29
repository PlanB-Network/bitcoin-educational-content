---
name: Di sản
description: Danh mục đầu tư Bitcoin với cơ chế kế thừa tích hợp thông qua các tập lệnh Taproot.
---

![cover](assets/cover.webp)



Việc chuyển giao Bitcoin trong trường hợp qua đời hoặc mất khả năng quản lý là một thách thức lớn đối với bất kỳ người sở hữu tài sản tiền điện tử nào. Nếu không có kế hoạch thừa kế phù hợp, những tài sản này sẽ trở nên không thể thu hồi được đối với người thân của bạn.



Heritage đưa ra một giải pháp thanh lịch bằng cách triển khai cơ chế chuyển mạch tự động (dead-man switch) trực tiếp trên chuỗi khối Bitcoin. wallet mã nguồn mở này cho phép cấu hình các điều kiện kế thừa của on-chain: nếu chủ sở hữu không thực hiện thêm giao dịch nào trong một khoảng thời gian nhất định, các khóa thay thế được chỉ định trước có thể giải phóng số tiền.



## Di sản là gì?



Heritage là một danh mục đầu tư Bitcoin tích hợp cơ chế kế thừa thông qua các tập lệnh Taproot. Được phát triển theo giấy phép MIT bởi Jérémie Rodon, phần mềm mã nguồn mở này đảm bảo tính minh bạch và độ bền.



Heritage sử dụng các kịch bản Taproot được mã hóa trong địa chỉ Bitcoin. Mỗi UTXO tích hợp hai loại điều kiện chi tiêu:





- Đường dẫn chính**: Chủ sở hữu có thể chi tiêu bitcoin của mình bất cứ lúc nào bằng khóa chính của mình.
- Các phương án thay thế**: Đối với mỗi người thừa kế được chỉ định, một tập lệnh sẽ kết hợp khóa công khai của người đó với khóa thời gian.



Mỗi giao dịch mua bán bất động sản sẽ tự động hoãn ngày kích hoạt điều khoản thừa kế. Trong trường hợp không hoạt động trong thời gian dài (tử vong, mất năng lực), các điều kiện sẽ tự động được kích hoạt.



## Dịch vụ di sản (tùy chọn)



Heritage cung cấp hai lựa chọn sử dụng:



**Tự làm (miễn phí)**: Ứng dụng mã nguồn mở duy nhất. Bạn tự quản lý mọi thứ với node riêng của mình. Tùy chọn này cung cấp quyền truy cập sao lưu tích hợp, quyền thừa kế tích hợp và quyền kiểm soát độc quyền đối với bitcoin của bạn. Tuy nhiên, bạn cần tự tạo cảnh báo (lịch, nhắc nhở) để không quên gia hạn timelock, và không có thông báo tự động cho người thừa kế của bạn.



**Sử dụng dịch vụ (0,05% mỗi năm)**: Dịch vụ btc-heritage.com bổ sung các tính năng giúp đơn giản hóa việc quản lý:




- Nhận lời nhắc tự động trước khi hạn chót của bạn hết hạn.
- Thông báo tự động cho người thừa kế để hướng dẫn họ trong quá trình phục hồi.
- Hỗ trợ ưu tiên
- Quản lý mô tả được đơn giản hóa



Phí: 0,05% tổng số tiền quản lý mỗi năm, tối thiểu 0,5 mBTC/năm. Năm đầu tiên miễn phí.



Dịch vụ này vẫn duy trì tính bảo mật: khóa riêng tư của bạn không bao giờ rời khỏi thiết bị. Heritage không thể truy cập vào tiền của bạn.



## Di sản CLI



Đối với người dùng nâng cao ưa thích giao diện dòng lệnh, Heritage cung cấp công cụ dòng lệnh (CLI) để điều khiển chi tiết và vận hành máy móc không có kết nối mạng.



![Page Heritage CLI](assets/fr/03.webp)



Tài liệu hướng dẫn đầy đủ về CLI có tại [btc-heritage.com/heritage-cli](https://btc-heritage.com/heritage-cli). Tại đây, bạn sẽ tìm thấy hướng dẫn tải xuống, kết nối với dịch vụ, tạo ví (với Ledger hoặc khóa cục bộ), quản lý người thừa kế và giao dịch.



Hướng dẫn này tập trung vào ứng dụng dành cho máy tính để bàn, ứng dụng dễ sử dụng hơn với hầu hết người dùng.



## Máy tính để bàn cổ điển



Heritage Desktop là một ứng dụng đồ họa với giao diện trực quan, hướng dẫn người dùng qua từng bước của quá trình cấu hình.



### Tải xuống



Truy cập [btc-heritage.com](https://btc-heritage.com) và nhấp vào "Tải ứng dụng".



![Page d'accueil Heritage](assets/fr/01.webp)



Hãy chọn phiên bản tương ứng với hệ điều hành của bạn (Linux 64bit hoặc Windows 64bit). Các tệp nhị phân không được ký số, điều này có thể gây ra cảnh báo bảo mật.



![Page de téléchargement](assets/fr/02.webp)



### Cài đặt trên Linux



Trên Linux, ứng dụng được phân phối ở định dạng AppImage. Trước khi có thể chạy ứng dụng, bạn cần cài đặt thư viện phụ thuộc `libfuse2`:



```bash
sudo apt install libfuse2
```



![Installation libfuse2](assets/fr/04.webp)



Sau đó, cấp quyền thực thi cho tệp và chạy nó:



```bash
chmod +x Heritage-GUI-vX.X.X.AppImage
./Heritage-GUI-vX.X.X.AppImage
```



### Lần ra mắt đầu tiên



Khi khởi chạy lần đầu, trình hướng dẫn thiết lập ban đầu sẽ cung cấp cho bạn ba lựa chọn:



![Onboarding initial](assets/fr/05.webp)





- Thiết lập Heritage Wallet**: Tạo wallet mới với kế hoạch di sản
- Thừa kế Bitcoin**: Khôi phục Bitcoin với tư cách người thừa kế
- Tự mình khám phá**: Khám phá các chức năng mà không cần trợ giúp



Chọn "Thiết lập một chiếc Wallet cổ điển" để tạo chiếc wallet đầu tiên của bạn.



### Kết nối mạng Bitcoin



Chọn cách kết nối với mạng Bitcoin:



![Choix connexion](assets/fr/06.webp)





- Sử dụng Dịch vụ Di sản**: Cơ sở hạ tầng được quản lý, đơn giản hơn cho người thừa kế
- Sử dụng node của riêng tôi**: Kết nối với node Bitcoin Core hoặc Electrum của riêng bạn.



Trong hướng dẫn này, chúng ta sẽ sử dụng node riêng của mình.



### Quản lý khóa riêng tư



Chọn cách quản lý khóa riêng tư của bạn:



![Gestion des clés](assets/fr/07.webp)





- Với thiết bị phần cứng Ledger** : Độ an toàn tối đa với phần cứng wallet (khuyến nghị)
- Lưu trữ cục bộ có mật khẩu**: Khóa được lưu trữ cục bộ với mật khẩu bảo vệ
- Khôi phục wallet hiện có** : Khôi phục từ seed hiện có



### Cấu hình nút



Nếu bạn đang sử dụng node riêng, ứng dụng sẽ hướng dẫn bạn cấu hình. Hãy đảm bảo node Bitcoin hoặc Electrum của bạn được cấu hình như sau:




- Đã cài đặt và đang chạy
- Đồng bộ với mạng Bitcoin
- Được cấu hình để chấp nhận kết nối RPC (cho Bitcoin Core)



![Configuration nœud](assets/fr/08.webp)



Nhấp vào "Nút Bitcoin của tôi đã sẵn sàng hoạt động" khi nút của bạn đã sẵn sàng.



### Bảng trạng thái



Nhấp vào "Trạng thái" ở góc trên bên phải, sau đó nhấp vào "Mở cấu hình" để truy cập các thông số kết nối.



![Panneau Status](assets/fr/09.webp)



Đặt URL của máy chủ Electrum của bạn (ví dụ: `umbrel.local:50001` nếu bạn đang sử dụng Umbrel).



![Configuration Electrum](assets/fr/10.webp)



### Sự ra đời của wallet



Sau khi kết nối được thiết lập, hãy nhấp vào "Tạo Wallet" trong tab VÍ.



![Créer wallet](assets/fr/11.webp)



Một cửa sổ bật lên giải thích về kiến trúc phân chia của Heritage:



![Architecture split](assets/fr/12.webp)



1. **Nhà cung cấp khóa (ngoại tuyến)**: Quản lý khóa riêng tư của bạn và ký các giao dịch. Có thể là phần mềm Ledger hoặc wallet.


2. **Wallet trực tuyến**: Xử lý việc đồng bộ hóa với mạng Bitcoin, tạo địa chỉ và phát sóng giao dịch.



Điền vào mẫu tạo:



![Formulaire création wallet](assets/fr/13.webp)





- Tên Wallet**: Một tên duy nhất để nhận dạng wallet của bạn.
- **Nhà cung cấp khóa**: Chọn Lưu trữ khóa cục bộ cho hướng dẫn này.
- Mới/Khôi phục**: Chọn "Mới" để tạo generate mới.
- Số lượng từ**: Khuyến nghị 24 từ để đảm bảo an ninh tối đa.



Nhập mật khẩu mạnh và chọn các tùy chọn cho Wallet trực tuyến:



![Options Online Wallet](assets/fr/14.webp)





- Nút cục bộ**: Sử dụng nút lõi Electrum hoặc Bitcoin của riêng bạn.
- Dịch vụ Di sản**: Sử dụng dịch vụ Di sản (được khuyến nghị cho các chức năng thông báo)



Nhấp vào "Tạo Wallet" để hoàn tất quá trình tạo.



### Interface từ wallet



wallet của bạn đã được tạo thành công. Giao diện hiển thị như sau:



![Interface wallet](assets/fr/15.webp)





- Sự cân bằng
- Nút GỬI và NHẬN
- Lịch sử giao dịch
- Lịch sử cấu hình di sản
- Địa chỉ wallet



### Tạo người thừa kế



Vào mục "NGƯỜI THỪA KẾ" để tạo người thừa kế.



![Page Heirs](assets/fr/16.webp)



Cửa sổ thông tin bật lên giải thích:




- Người thừa kế là các khóa công khai Bitcoin được liên kết với từng cá nhân.
- Mỗi người thừa kế đều có cụm từ ghi nhớ riêng của mình.
- Người thừa kế đầu tiên nên là "người dự phòng" cho chính bạn (trong trường hợp mất chiếc wallet chính).



#### Tạo bản sao lưu người thừa kế



Nhấp vào "Tạo người thừa kế" và đặt tên là "Bản sao lưu".



![Création héritier Backup](assets/fr/17.webp)



Cửa sổ bật lên giải thích lý do tại sao một câu gồm 12 từ không chứa passphrase lại an toàn cho người thừa kế:


1. **Không thể truy cập ngay lập tức**: Người thừa kế không thể truy cập vào tiền cho đến khi thời gian khóa hết hạn.


2. **Phát hiện xâm nhập**: Nếu ai đó truy cập vào cụm từ, bạn có thể cập nhật cấu hình Heritage.


3. **Khả năng truy cập lâu dài**: Một chiếc passphrase có thể bị lãng quên sau nhiều năm.



Cấu hình người thừa kế:



![Configuration héritier](assets/fr/18.webp)





- Nhà cung cấp khóa**: Kho lưu trữ khóa cục bộ
- Mới**: Tạo seed mới
- Số lượng từ**: 12 từ



Hoàn tất quá trình tạo:



![Finalisation héritier](assets/fr/19.webp)





- Loại người thừa kế**: Khóa công khai mở rộng
- Xuất sang Dịch vụ**: Tùy chọn, cho phép tự động thông báo cho người thừa kế



Người thừa kế dự phòng đã được tạo:



![Héritier créé](assets/fr/20.webp)



#### Lưu giữ cụm từ ghi nhớ của người thừa kế



Nhấp vào Người thừa kế dự phòng rồi nhấp vào "Hiển thị Mnemonic" :



![Afficher mnemonic](assets/fr/21.webp)



**QUAN TRỌNG: Hãy ghi nhớ 12 từ này và giữ chúng ở nơi an toàn. Đây là chìa khóa để lấy lại tiền.**



![Phrase mnémotechnique](assets/fr/22.webp)



#### Gỡ bỏ seed khỏi ứng dụng



Sau khi đã ghi lại cụm từ, hãy truy cập vào các thông số của chúng (biểu tượng bánh răng):



![Paramètres héritier](assets/fr/23.webp)



Sử dụng chức năng "Xóa khóa thừa kế" để xóa khóa riêng tư khỏi ứng dụng. Xác nhận rằng bạn đã lưu cụm từ đó.



![Strip Heir Seed](assets/fr/24.webp)



Đây là một biện pháp bảo mật: chỉ có khóa công khai được lưu lại trong ứng dụng, đủ để cấu hình quyền thừa kế.



#### Tạo ra người thừa kế thứ hai



Lặp lại quy trình để tạo người thừa kế thứ hai (ví dụ: "Satoshi"). Bây giờ bạn sẽ có hai người thừa kế:



![Deux héritiers](assets/fr/25.webp)





- Sao lưu**: Chìa khóa khẩn cấp cá nhân của bạn
- Satoshi**: Người thừa kế được chỉ định



### Cấu hình kế thừa



Quay lại wallet của bạn và nhấp vào biểu tượng Cài đặt:



![Paramètres wallet](assets/fr/26.webp)



Trong mục "Cấu hình kế thừa", hãy nhấp vào "Tạo":



![Heritage Configuration](assets/fr/27.webp)



Đặt giới hạn thời gian cho mỗi người thừa kế:



![Configuration délais](assets/fr/28.webp)





- Sao lưu**: 180 ngày (6 tháng) - Ngày đáo hạn: 18/06/2026
- Satoshi**: 455 ngày (15 tháng) - Ngày đáo hạn: 2027-03-20



**Quan trọng**: Mỗi người thừa kế phải có thời gian trì hoãn lâu hơn người trước đó. Người thừa kế đầu tiên (Người dự phòng) sẽ được tiếp cận số tiền trước.



Ngoài ra, hãy cấu hình:



![Configuration finale](assets/fr/29.webp)





- Ngày tham chiếu**: Ngày bắt đầu tính toán thời gian giao hàng
- Thời gian trì hoãn tối thiểu sau giao dịch**: Thời gian trì hoãn tối thiểu sau giao dịch (khuyến nghị 10 ngày)



Nhấp vào "Tạo" để xác nhận cấu hình.



Cấu hình Heritage hiện đã được kích hoạt:



![Configuration active](assets/fr/30.webp)



Nó hiển thị cả hai người thừa kế cùng với thời hạn và ngày hết hạn tương ứng của họ.



### Lưu mô tả



**Quan trọng**: Hãy lưu giữ các mô tả wallet của bạn. Nếu không có chúng, ngay cả khi sử dụng cụm từ ghi nhớ, việc khôi phục quỹ cũng không thể thực hiện được.



Nhấp vào "Sao lưu mô tả":



![Bouton Backup](assets/fr/31.webp)



Lưu tệp JSON chứa các mô tả Bitcoin của bạn:



![Backup descripteurs](assets/fr/32.webp)



Tệp tin này nên được chuyển giao cho người thừa kế của bạn, cùng với các cụm từ ghi nhớ tương ứng của họ.



### Nhận bitcoin



Nhấp vào "NHẬN" để gửi địa chỉ nhận đến generate:



![Recevoir bitcoins](assets/fr/33.webp)



Chúc mừng! Thiết bị Heritage Wallet của bạn đã sẵn sàng nhận bitcoin. Mỗi địa chỉ được tạo tự động tích hợp các điều kiện Heritage của bạn.



Sau khi nhận được giao dịch, số dư của bạn sẽ được cập nhật:



![Solde mis à jour](assets/fr/34.webp)



Phần lịch sử hiển thị giao dịch và cấu hình Heritage liên quan.



---

## Sự phục hồi bởi người thừa kế



Sau khi thời gian quy định kết thúc, người thừa kế có thể nhận lại số tiền đó.



### Điều kiện tiên quyết



Người thừa kế cần:


1. Cụm từ ghi nhớ gồm 12 từ của anh ấy


2. Tệp sao lưu mô tả wallet gốc (JSON)



### Tạo dựng người thừa kế Wallet



Trong tab "THỪA KẾ", một cửa sổ bật lên sẽ nhắc nhở bạn về các điều kiện tiên quyết này:



![Page Heir Wallets](assets/fr/35.webp)



**Vui lòng lưu ý**: Nếu không có tệp sao lưu mô tả, việc truy cập vào số tiền là KHÔNG THỂ, ngay cả khi sử dụng cụm từ ghi nhớ chính xác.



Nhấp vào "Tạo người thừa kế Wallet":



![Créer Heir Wallet](assets/fr/36.webp)



Vui lòng điền vào mẫu đơn:



![Formulaire Heir Wallet](assets/fr/37.webp)





- Tên người thừa kế Wallet**: Một cái tên để xác định người thừa kế wallet này.
- Nhà cung cấp khóa**: Kho lưu trữ khóa cục bộ
- Khôi phục**: Chọn tùy chọn này để nhập cụm từ hiện có



Nhập 12 từ của cụm từ ghi nhớ của người thừa kế và cấu hình Nhà cung cấp Di sản:



![Entrée mnemonic](assets/fr/38.webp)





- Nhà cung cấp di sản**: "Cục bộ" để sử dụng nút của riêng bạn với tệp sao lưu



Tải tệp sao lưu JSON và nhấp vào "Tạo Heir Wallet":



![Chargement backup](assets/fr/39.webp)



### Interface Người thừa kế Wallet



Người thừa kế Wallet được tạo ra. Ban đầu, nếu thời hạn khóa chưa hết, sẽ không có quyền thừa kế nào khả dụng:



![Pas d'héritage disponible](assets/fr/40.webp)



Sau khi thời gian trì hoãn kết thúc và số tiền được đồng bộ hóa với mạng Bitcoin, chúng sẽ xuất hiện trong danh sách thừa kế:



![Héritage disponible](assets/fr/41.webp)



Giao diện hiển thị:




- Loại khóa và dấu vân tay
- Tổng số tiền thừa kế
- Số tiền hiện có thể chi tiêu (0 sat nếu thời hạn khóa chưa hết hạn)
- Ngày đáo hạn và ngày hết hạn



Khi đến ngày đáo hạn, nút "Chi tiêu" sẽ chuyển số bitcoin sang thiết bị wallet cá nhân của bạn.



---

## Thực tiễn tốt nhất



### Lưu mô tả



Các mô tả wallet rất cần thiết để khôi phục lại địa chỉ Heritage của bạn. **Nếu không có các mô tả này, ngay cả với cụm từ ghi nhớ, bạn cũng sẽ không thể tìm thấy tiền của mình.**



### Bảo mật chính





- Nếu có thể, hãy sử dụng Ledger làm khóa chính.
- Đừng bao giờ cất giữ bản án của người thừa kế ở cùng một nơi với bản án của chính bạn.
- Truyền tải thông tin trên nhiều phương tiện truyền thông và địa điểm khác nhau.



### Lưu trữ hồ sơ cho người thân yêu của bạn.



Hãy viết hướng dẫn rõ ràng giải thích từng bước của quy trình phục hồi. Người thừa kế của bạn có thể không quen thuộc với Bitcoin vào thời điểm quan trọng này.



## Các lựa chọn thay thế



Ngoài ra còn có các giải pháp khác để quản lý việc chuyển giao bitcoin của bạn, bao gồm Liana và Bitcoin Keeper. Bạn có thể tìm thấy hướng dẫn của chúng tôi bên dưới:



https://planb.academy/tutorials/wallet/desktop/liana-306ef457-700c-4fdd-b07a-8fb7a8a29f04

https://planb.academy/tutorials/wallet/backup/bitcoin-keeper-inheritance-c656a201-9587-4bf2-8cdb-acbd3c3631b4

## Phần kết luận



Heritage cho phép bạn lập kế hoạch kế nhiệm Bitcoin một cách độc lập thông qua ứng dụng trên máy tính để bàn. Việc thực hiện đòi hỏi sự cân nhắc kỹ lưỡng về khung thời gian phù hợp và bảo mật thông tin. Đừng quên truyền lại cho người thừa kế của bạn:




- Cụm từ ghi nhớ gồm 12 từ của họ
- Tệp sao lưu mô tả
- Hướng dẫn khôi phục



## Tài nguyên





- [Trang web chính thức của Heritage](https://btc-heritage.com)
- [Tài liệu CLI](https://btc-heritage.com/heritage-cli)
- [GitHub Heritage CLI](https://github.com/crypto7world/heritage-cli)
- [GitHub Heritage Desktop](https://github.com/crypto7world/heritage-gui)