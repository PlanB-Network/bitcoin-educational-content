---
name: Wallet of Satoshi - Tự quản lý
description: Tìm hiểu cách cấu hình chế độ tự quản lý của danh mục đầu tư Wallet of Satoshi
---

![cover](assets/cover.webp)



***“Không phải chìa khóa của bạn, không phải tiền của bạn” không chỉ là một câu nói, mà còn là một nguyên tắc cơ bản của Bitcoin, có nghĩa là nếu bạn không kiểm soát **khóa riêng tư** để mở khóa bitcoin của mình, bạn thực sự không sở hữu chúng.



Nhiều người dùng thường bắt đầu với **wallet lưu ký**, sau đó chuyển sang **wallet tự lưu ký**, nơi họ tự kiểm soát khóa riêng của mình.


Trong hướng dẫn này, chúng tôi sẽ không giới thiệu cho bạn một chiếc wallet tự quản lý mới. Thay vào đó, chúng tôi sẽ giới thiệu cho bạn một tính năng mới của ***Wallet of Satoshi*** wallet: **chế độ tự quản lý**.



Mục tiêu của sự tích hợp mới này là cho phép người dùng giữ quyền kiểm soát khóa riêng tư của họ đồng thời được hưởng lợi từ sự đơn giản và trải nghiệm người dùng mượt mà.



Trước khi đi vào vấn đề chính, chúng ta hãy dành chút thời gian để xem xét chế độ tự quản lý đặc biệt mà Wallet of Satoshi (WoS) cung cấp.



## Đặc điểm đặc biệt của chế độ tự quản lý



Sự đơn giản và linh hoạt của chế độ tự quản lý của WoS loại bỏ sự phức tạp của việc mở kênh Lightning, quản lý các node... Nhưng điều này làm sao có thể?



Chế độ tự quản lý của Wallet of Satoshi được cung cấp bởi **Spark**. Đây là giải pháp Layer 2 dành cho Bitcoin, được tạo ra bởi Lightspark, sử dụng công nghệ **statechains**.



Do đó, bạn không thực hiện giao dịch trực tiếp trên Lightning Network. Sự tương tác giữa mạng **LN** và **Spark** diễn ra thông qua **trao đổi nguyên tử**.



Ví dụ, Bob muốn thanh toán hóa đơn Lightning bằng WoS. Anh ta chuyển các satoshi của mình, nhưng ở phía sau, các chuyển khoản này được chuyển đến một **Nhà cung cấp dịch vụ Spark (SSP)** trên Spark, nơi sẽ thực hiện thanh toán trên mạng Lightning.



Ngược lại, Alice muốn nhận tiền trực tiếp từ danh mục đầu tư WoS của mình. Trong trường hợp này, **SSP** nhận được sats thông qua LN và ngay lập tức ghi có vào danh mục đầu tư của Alice.



Vì vậy, điều quan trọng cần lưu ý là để tận dụng sự đơn giản và linh hoạt của WoS, bạn cần phụ thuộc vào máy chủ của Spark. Tuy nhiên, về mặt bảo mật, nếu một SSP trở nên độc hại hoặc không khả dụng, bạn có cơ chế **thoát đơn phương**, một biện pháp bảo mật cho phép bạn khôi phục tiền của mình trên Bitcoin on-chain (mặc dù điều này có thể chậm và tốn kém), đảm bảo trải nghiệm tự quản lý tương đương với một node Lightning riêng tư.



Sau khi xem xét tất cả các thông số này, bạn có thể quyết định lượng sats mà bạn muốn giữ lại trong kho WoS của mình.



Nếu bạn mới sử dụng Wallet of Satoshi, tất nhiên bạn sẽ cần tải xuống ứng dụng di động wallet. Tuy nhiên, nếu bạn đã sử dụng ứng dụng này và muốn biết cách sử dụng **chế độ tự quản lý**, vui lòng chuyển thẳng đến phần **Cấu hình chế độ tự quản lý** trong hướng dẫn này.



## Bắt đầu với Wallet of Satoshi



Vào cửa hàng ứng dụng của bạn và tải xuống WoS.



![screen](assets/fr/03.webp)



Mở ứng dụng sau khi quá trình tải xuống hoàn tất và nhấn **Bắt đầu**.



![screen](assets/fr/04.webp)



Bạn sẽ được chuyển hướng đến giao diện chính của ứng dụng. Trên thực tế, khi bạn truy cập WoS lần đầu tiên, danh mục đầu tư đã hoạt động và tự động mở ở chế độ lưu ký theo mặc định.



![screen](assets/fr/05.webp)



Ngay cả khi bạn không muốn sử dụng WoS ở chế độ quản trị, chúng tôi vẫn khuyên bạn nên cấu hình nó trước. Để làm điều đó, hãy tham khảo hướng dẫn này.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Chúng ta hãy chuyển sang phần cấu hình WoS ở chế độ tự quản lý.



## Cấu hình chế độ tự quản lý



Nhấp chuột vào biểu tượng menu ba gạch (biểu tượng hamburger) ở góc trên bên phải giao diện chính.



![screen](assets/fr/06.webp)



Sau đó, trong menu hiện ra, hãy nhấp vào menu phụ **Mở Tự Giữ Quyền Nuôi Con Wallet**.



![screen](assets/fr/07.webp)



WoS ngay lập tức thông báo cho bạn rằng *chế độ tự quản lý đi kèm với một cụm từ khôi phục. Ngoài ra, bạn hoàn toàn chịu trách nhiệm về sự an toàn của tiền của mình*.



![screen](assets/fr/08.webp)



Chọn nút "**Tôi hiểu**" (1), sau đó nhấn nút **Mở Tự giám hộ Wallet** (2), nút này sẽ hiện lên màu vàng sáng.



![screen](assets/fr/09.webp)



### Xây dựng danh mục đầu tư tự quản lý



Sau khi nhấp vào nút **Mở mẫu Wallet Tự Giữ Quyền Nuôi Con**, hãy nhấp vào nút **Tạo mẫu Wallet Mới**.



![screen](assets/fr/10.webp)



WoS sẽ tạo một danh mục đầu tư tự quản lý cho bạn, cũng trong cùng một ứng dụng. Bạn có thể chuyển đổi giữa chế độ **quản lý** (có sẵn ở một số khu vực) và chế độ **tự quản lý** bất cứ lúc nào và theo ý muốn của mình.



![screen](assets/fr/11.webp)



Sau khi tạo xong, bạn sẽ được chuyển hướng đến giao diện tự quản lý chính của WoS. Bạn sẽ nhận thấy không có sự khác biệt nào giữa tổng quan và giao diện của danh mục lưu ký WoS và danh mục tự quản lý WoS.



### Lưu cụm từ ghi nhớ của bạn



Nhấn vào biểu tượng **Móc khóa + Sao lưu Wallet** nằm ở phía trên cùng của màn hình, giữa tên Wallet of Satoshi và biểu tượng menu ba gạch ngang.



![screen](assets/fr/12.webp)



WoS cung cấp hai cách khác nhau để lưu 12 từ (cụm từ ghi nhớ) của bạn: **sao lưu qua Google Drive** và **sao lưu thủ công**.



Mặc dù chúng tôi khuyên bạn nên sao lưu thủ công vì đây là phương pháp an toàn nhất, nhưng chúng tôi cũng sẽ hướng dẫn bạn cách sao lưu thông qua Google Drive.



#### Sao lưu qua Google Drive



Nhấp vào nút **Sao lưu Google Drive**.



![screen](assets/fr/13.webp)



Nếu bạn chọn sao lưu bằng Google Drive, có nguy cơ cao tài khoản Google của bạn sẽ bị xâm phạm. Kẻ xấu có thể truy cập vào tập tin chứa 12 từ khóa của bạn và do đó có thể chiếm quyền truy cập vào wallet của bạn.



Việc thêm mật khẩu để mã hóa tệp chứa 12 từ của bạn chắc chắn là một cách tốt để tăng thêm lớp bảo mật.



Vì vậy, hãy kích hoạt nút **Mã hóa bằng mật khẩu** trong tùy chọn nâng cao.



![screen](assets/fr/14.webp)



Trên giao diện mới hiện ra, hãy đặt mật khẩu mạnh, sau đó xác nhận lại một lần nữa.



![screen](assets/fr/15.webp)



Điều quan trọng cần nhớ là một khi bạn đã chọn mật khẩu, bạn không được quên nó hoặc làm mất phương tiện mà bạn đã ghi mật khẩu đó. Nếu bạn quên hoặc làm mất nó, bạn sẽ không bao giờ có thể truy cập lại 12 từ khóa của mình, và do đó, mất luôn cả tiền của mình.



Sau khi chọn mật khẩu, hãy chọn tài khoản Google để sao lưu, sau đó cấp quyền truy cập cần thiết cho WoS.



![screen](assets/fr/16.webp)



![screen](assets/fr/17.webp)



Chờ vài giây. Tuyệt vời! Quá trình sao lưu đã hoàn tất thành công.



![screen](assets/fr/18.webp)



Bạn luôn có tùy chọn tạo thêm bản sao lưu bằng cách chọn phương pháp sao lưu thứ hai: sao lưu thủ công.


#### Sao lưu thủ công



Nếu bạn chọn sao lưu thủ công, chúng tôi đặc biệt khuyên bạn nên tham khảo hướng dẫn này, hướng dẫn này sẽ trình bày các phương pháp tốt nhất để sao lưu cụm từ ghi nhớ của bạn một cách an toàn, để bạn không bị mất quyền truy cập vào bitcoin của mình.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270

Nhấn nút **Sao lưu thủ công**.



![screen](assets/fr/19.webp)



Trên giao diện tiếp theo, WoS nhắc nhở bạn một vài biện pháp phòng ngừa an toàn cần lưu ý trước khi tiến hành sao lưu thủ công.



Kích hoạt nút **Tôi hiểu** và nhấn nút **Tiếp theo**.



![screen](assets/fr/20.webp)



Sau đó, bạn sẽ thấy 12 từ của mình. Hãy lưu chúng lại, rồi nhấn vào nút **Tiếp theo**.



![screen](assets/fr/21.webp)



Trên giao diện mới này, hãy nhấn vào các từ theo đúng thứ tự.



![screen](assets/fr/22.webp)



Cuối cùng, hãy nhấp vào nút **Tiếp theo**. Chúc mừng! Quá trình sao lưu của bạn đã hoàn tất.



![screen](assets/fr/23.webp)



## Khôi phục danh mục đầu tư tự quản lý



Khi bạn muốn khôi phục hoặc lấy lại quyền giám hộ WoS wallet sau khi đổi điện thoại hoặc vì bất kỳ lý do nào khác, hãy làm theo các bước sau.



Để mở danh mục đầu tư WoS, hãy nhấp vào biểu tượng menu ba gạch ngang ở góc trên bên phải giao diện chính.


Trong menu hiện ra, hãy nhấp vào menu con **Mở Tự Giữ Hộ Hộ Wallet**.


Trên giao diện mới hiện ra, hãy nhấn nút **Khôi phục Wallet hiện có**.



![screen](assets/fr/24.webp)



Hãy chọn phương pháp phục hồi và tiến hành bước tiếp theo.



![screen](assets/fr/25.webp)



### Khôi phục thông qua Google Drive



1. Nhấn vào nút **Khôi phục từ Google Drive**.


2. Chọn một tài khoản Google và cho phép WoS truy xuất dữ liệu phục hồi đã lưu trên Google Drive của bạn.


3. Sau đó, nhập mật khẩu mã hóa của bạn (nếu bạn đã thiết lập trước đó) từ tệp chứa 12 từ của bạn.


4. Chờ một lát để quá trình khôi phục có hiệu lực, sau đó bạn sẽ có thể truy cập lại vào danh mục đầu tư của mình.



### Phục hồi thủ công



1. Nhấn nút **Khôi phục thủ công**.


2. Sau đó, nhập 12 từ của cụm từ ghi nhớ của bạn, viết mỗi từ trước số thứ tự của nó.


3. Chờ một lát để quá trình khôi phục có hiệu lực, sau đó bạn sẽ có thể truy cập lại vào danh mục đầu tư của mình.




### Chuyển bitcoin giữa tài khoản lưu ký WoS và tài khoản tự lưu ký WoS



Khi bạn có bitcoin (sats) trong tài khoản lưu ký WoS wallet và tạo thêm tài khoản tự lưu ký WoS wallet, bạn sẽ không bị mất tiền. Hơn nữa, bạn có thể chuyển chúng sang danh mục đầu tư tự lưu ký của mình và ngược lại.



Để làm như vậy:


Bạn có thể sao chép địa chỉ tự quản lý Lightning WoS hoặc hóa đơn mà bạn đã tạo.



![screen](assets/fr/26.webp)



Bây giờ hãy mở hộp đựng wallet của bạn và nhấn nút **Envoyer**.



Sau đó dán địa chỉ hoặc hóa đơn. Nhấn **Envoyer** lần thứ hai.



Hãy quay lại danh mục đầu tư tự quản lý của bạn và bạn sẽ thấy rằng mình đã nhận được tiền.



![screen](assets/fr/27.webp)



## Gửi và nhận bitcoin



Đối với việc gửi và nhận bitcoin ở chế độ tự quản lý, cũng giống như tổng quan và giao diện, chúng không khác gì việc gửi và nhận bitcoin thông qua thiết bị lưu ký WoS wallet.



Vui lòng tham khảo hướng dẫn cơ bản về cách sử dụng Wallet of Satoshi trên mạng Plan₿.



https://planb.academy/tutorials/wallet/mobile/wallet-of-satoshi-39149d86-e42b-4e8f-ae9f-7e061e7784f7

Giờ đây, bạn có thể tự cấu hình và vận hành Wallet of Satoshi ở chế độ tự quản lý.



Nếu bạn thấy hướng dẫn này hữu ích, vui lòng để lại biểu tượng ngón tay cái màu xanh lá cây bên dưới. Cảm ơn rất nhiều!