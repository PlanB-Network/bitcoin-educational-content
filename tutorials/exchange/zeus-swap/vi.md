---
name: Zeus Swap
description: Dịch vụ Exchange không lưu ký giữa bitcoin On-Chain và Lightning Network
---

![cover](assets/cover.webp)



Hệ sinh thái Bitcoin thể hiện tính hai mặt: mạng chính (On-Chain) cung cấp bảo mật tối đa, trong khi Lightning Network cho phép giao dịch tức thời. Kiến trúc hai Layer này đặt ra một thách thức thực tế: làm thế nào để chuyển tiền hiệu quả giữa hai lớp này mà không cần trung gian tập trung?



Vấn đề rất cụ thể: bạn nhận được khoản thanh toán Lightning nhưng muốn lưu trữ nó trong kho lưu trữ Cold, hoặc ngược lại, bạn có Bitcoin On-Chain nhưng cần thanh khoản Lightning. Các giải pháp truyền thống liên quan đến việc mở/đóng thủ công các kênh Lightning (tốn kém và kỹ thuật) hoặc các nền tảng tập trung yêu cầu KYC.



Zeus Swap giải quyết vấn đề này bằng dịch vụ Exchange tự động, không cần lưu ký. Được phát triển bởi Zeus LSP, dịch vụ này cho phép bạn chuyển đổi Bitcoin On-Chain sang Lightning Satoshi theo hai chiều mà không cần ủy thác tiền của bạn cho bên trung gian. Quy trình này sử dụng hợp đồng nguyên tử (HTLC) đảm bảo rằng Exchange sẽ hoàn tất hoặc hủy bỏ.



Sự đổi mới nằm ở tính đơn giản: chỉ cần vài cú nhấp chuột là có thể sở hữu Exchange, giúp bạn bảo vệ quyền tự chủ tài chính mà không cần đăng ký hoặc KYC.



## Zeus Swap là gì?



Zeus Swap là dịch vụ thanh khoản Exchange do Zeus LSP phát triển, cho phép hoán đổi nguyên tử giữa mạng lưới chính Bitcoin và Lightning Network. Đây là một cơ sở hạ tầng kỹ thuật sử dụng hoán đổi ngầm và hoán đổi ngược để tạo điều kiện chuyển đổi hai chiều giữa On-Chain BTC và Lightning Satoshi, đồng thời vẫn duy trì tính chất phi lưu ký của hoạt động này.



### Kiến trúc kỹ thuật



Zeus Swap sử dụng công nghệ hoán đổi nguyên tử Bitcoin/Lightning mã nguồn mở của Boltz. Giao thức này sử dụng Hợp đồng Khóa Thời gian Hash (HTLC): hợp đồng khóa tiền với hai điều kiện giải phóng (tiết lộ bí mật mật mã hoặc hết hạn theo thời gian).



Đối với giao dịch hoán đổi ngầm (On-Chain → Lightning), người dùng gửi bitcoin đến Address tích hợp Hash của Lightning Invoice. Zeus LSP chỉ mở khóa số tiền này bằng cách thanh toán Invoice tương ứng, tiết lộ hình ảnh tiền mã hóa, tự động mở khóa bitcoin. Cơ chế này đảm bảo tính nguyên tử.



Đối với giao dịch hoán đổi ngược (Lightning → On-Chain), người dùng trả Lightning Invoice từ Zeus LSP, tiết lộ hình ảnh trước cho phép giải phóng giao dịch Bitcoin đã chuẩn bị đến đích Address.



Để biết thêm chi tiết về cách thức hoạt động của Lightning Network, hãy tham khảo khóa học chuyên sâu của chúng tôi:



https://planb.academy/courses/34bd43ef-6683-4a5c-b239-7cb1e40a4aeb

### Mô hình kinh doanh



Zeus LSP đóng vai trò là nhà tạo lập thị trường, duy trì tính thanh khoản của On-Chain và Lightning để đảm bảo thanh khoản cho các hợp đồng hoán đổi. Đối với các hợp đồng hoán đổi, Zeus áp dụng một mức phí biến đổi (thường từ 0,1% đến 0,5% tùy theo hướng và điều kiện) cộng với phí Mining của Bitcoin, được hiển thị minh bạch trước khi xác thực.



Là Nhà cung cấp dịch vụ Lightning, Zeus tối ưu hóa chi phí nhờ chuyên môn về mở kênh theo yêu cầu, định tuyến hiệu quả và các giải pháp thanh khoản tùy chỉnh.



### Tích hợp



Zeus Wallet tích hợp sẵn dịch vụ, cho phép hoán đổi mà không cần rời khỏi Interface Bitcoin/Lightning. Điều này giúp loại bỏ sự bất tiện khi sao chép và dán giữa các ứng dụng.



Web Interface độc lập vẫn có thể truy cập được đối với tất cả các ví, đảm bảo tính linh hoạt tối đa khi sử dụng.



## Các tính năng chính



### Hoán đổi hai chiều



Zeus Swap cung cấp hai loại Exchange:



**Hoán đổi tàu ngầm (On-Chain → Lightning)**: bơm thanh khoản Lightning từ nguồn dự trữ Bitcoin của bạn, hữu ích để cung cấp cho nút Wallet hoặc Lightning di động mà không cần mở kênh thủ công.



**Hoán đổi ngược (Lightning → On-Chain)**: chuyển đổi satoshi Lightning thành bitcoin On-Chain để lưu trữ lâu dài, tránh việc đóng kênh tốn kém.



### Giao diện người dùng



**Interface web** (swaps.zeuslsp.com): trải nghiệm đơn giản mà không cần đăng ký, quy trình hướng dẫn với hiển thị phí và trạng thái theo thời gian thực.



**Tích hợp Zeus Wallet**: hoán đổi trực tiếp từ ứng dụng, quản lý tự động hóa đơn và địa chỉ, loại bỏ lỗi xử lý.



### An toàn và phục hồi



Mỗi lần hoán đổi tạo ra một Contract duy nhất với các tham số bất biến: Hash Lightning, thời gian chờ, hoàn tiền Address. Trong trường hợp lỗi, chức năng tự động khôi phục thông qua Address được cung cấp, độc lập với Zeus LSP.



**Khóa Cứu Hộ Đổi Zeus**: Trong quá trình đổi On-Chain → Lightning, Zeus sẽ tự động tạo một khóa khôi phục chung thay thế các tệp hoàn tiền riêng lẻ cũ. Khóa duy nhất này hoạt động trên mọi thiết bị và cho tất cả các giao dịch đổi được tạo bằng khóa này. Việc tải xuống và lưu khóa này ở một nơi an toàn là rất quan trọng để có thể khôi phục tiền của bạn trong trường hợp hoán đổi bị lỗi.



### Tối ưu hóa mạng



Zeus Swap tự động điều chỉnh thời gian hết hạn và phí Mining theo điều kiện mạng. Người dùng Zeus được hưởng lợi từ các tùy chọn nâng cao: lựa chọn LSP, độ trễ tùy chỉnh, khả năng tương thích với các dịch vụ khác (Boltz).



## Cài đặt và sử dụng



### Phương pháp truy cập



**Interface web** (swaps.zeuslsp.com): giải pháp chung tương thích với mọi ví, không cần cài đặt, lý tưởng để sử dụng thỉnh thoảng.



**Ứng dụng Zeus** (iOS/Android): trải nghiệm tích hợp kết hợp Wallet và swap, phù hợp với người dùng thông thường.



Xem hướng dẫn Zeus của chúng tôi để tìm hiểu thêm về Wallet hoàn chỉnh này:



https://planb.academy/tutorials/wallet/mobile/zeus-embedded-c67fa8bb-9ff5-430d-beee-80919cac96b9

### Cấu hình web



**On-Chain → Lightning**: Quá trình bắt đầu bằng việc cấu hình swap trên web Zeus Swap của Interface. Người dùng có thể sử dụng mũi tên giữa các trường On-Chain và Lightning để đảo ngược hướng swap.



![Interface de création de swap](assets/fr/01.webp)



*Interface Zeus Swap: lựa chọn số tiền (Sats 50.000 → Sats 49.648 sau khi trừ phí) với hiển thị minh bạch về phí mạng (Sats 302) và dịch vụ Zeus (Sats 50).*



Trong quá trình này, Zeus cung cấp cho bạn tùy chọn tải xuống khóa khôi phục chung:



![Téléchargement de la Zeus Swaps Rescue Key](assets/fr/02.webp)



*Tải xuống hộp thoại để có Khóa cứu hộ Zeus Swaps - một khóa chung thay thế cho các tệp hoàn tiền riêng lẻ cũ*



Nếu bạn đã có khóa, Zeus cho phép bạn kiểm tra khóa đó:



![Vérification de la clé existante](assets/fr/03.webp)



*Interface để kiểm tra tính hợp lệ của Khóa cứu hộ Zeus Swaps hiện có*



Sau khi cấu hình, Zeus sẽ tạo kho Bitcoin Address và hiển thị hướng dẫn:



![Adresse de dépôt et instructions](assets/fr/04.webp)



*Trang hoàn tất hoán đổi: Mã QR và Bitcoin Address để gửi 50.000 Satss, kèm theo lời nhắc về ngày hết hạn sau 24 giờ*



Sau đó, quá trình hoán đổi sẽ chờ xác nhận của Bitcoin:



![Attente de confirmation](assets/fr/05.webp)



*Trạng thái "Giao dịch trong Mempool" - đang chờ xác nhận của Bitcoin để hoàn tất việc hoán đổi*



Sau khi xác nhận, việc hoán đổi sẽ tự động hoàn tất:



![Swap réussi](assets/fr/06.webp)



*Xác nhận thành công: Đã nhận được 49.648 Sats trên Lightning sau khi đã trừ phí mạng và dịch vụ*



### Sử dụng ứng dụng Zeus



**Lightning → On-Chain**: Ứng dụng Zeus cung cấp trải nghiệm tích hợp cho việc hoán đổi ngược (Lightning sang Bitcoin).



![Navigation vers les swaps dans Zeus](assets/fr/07.webp)



*Màn hình chính của Zeus hiển thị số dư Lightning (69.851 Sats) và On-Chain (38.018 Sats), truy cập vào các giao dịch hoán đổi thông qua menu bên*



![Configuration du swap reverse](assets/fr/08.webp)



*Tạo hoán đổi ngược Interface: 50.000 Sats Lightning → 49.220 Sats On-Chain, với phí mạng (530 Sats) và phí dịch vụ (250 Sats) được hiển thị rõ ràng. Người dùng có thể nhập thủ công Bitcoin nhận Address, hoặc tự động nhập generate từ Wallet Zeus thông qua nút "generate On-Chain Address".*



![Finalisation du swap mobile](assets/fr/09.webp)



*Màn hình hoàn tất: Màn hình thanh toán Lightning Invoice với dòng chữ "THANH TOÁN Invoice NÀY", xác nhận thanh toán Lightning thành công sau 9,96 giây và bảng sao kê số dư với 49.162 Sats đang chờ xác nhận*



### Giám sát và an ninh



Mỗi lần hoán đổi đều có mã định danh duy nhất với tính năng theo dõi thời gian thực. Hiển thị toàn bộ tiến độ, tự động cảnh báo ngày hết hạn. Tự động đề xuất phí theo điều kiện mạng.



## Ưu điểm và hạn chế



### Những lợi ích





- Đơn giản**: Chuyển đổi chỉ bằng vài cú nhấp chuột so với thao tác kênh thủ công
- Không lưu ký**: không KYC, không tài khoản, tiền không bao giờ được ủy thác cho bên thứ ba
- Minh bạch**: phí được hiển thị rõ ràng trước khi xác thực (0,1% đến 0,5% + mức tối thiểu tùy thuộc vào thử nghiệm của người dùng - kiểm tra phí hiện tại tại mỗi lần hoán đổi)
- Tích hợp di động**: trải nghiệm gốc trong Zeus Wallet



### Hạn chế





- Thời gian hết hạn**: tối đa 24-48 giờ, lỗi nếu Bitcoin không được xác nhận kịp thời
- Giới hạn số tiền**: tối thiểu 25.000 Sats, thanh khoản Zeus LSP có thể thay đổi tùy theo điều kiện
- Dấu vết On-Chain**: Các tập lệnh HTLC có khả năng được xác định bằng phân tích Blockchain
- Cần xác nhận**: tối thiểu 10 phút để xác thực Bitcoin



## Thực hành tốt nhất



### Thời gian và chi phí





- Theo dõi Mempool.space để biết thời gian ít tắc nghẽn
- Ưu tiên cuối tuần và giờ thấp điểm để giảm chi phí Mining
- Tính toán lợi nhuận: số lượng nhỏ so với mở kênh trực tiếp



### Bảo vệ





- Kiểm tra địa chỉ Bitcoin cẩn thận (khuyến nghị sao chép-dán)
- Sao lưu Khóa cứu hộ Zeus Swaps**: tải xuống và lưu trữ khóa khôi phục ở nơi an toàn
- Tài liệu: Contract ID, hoàn tiền Address, ngày hết hạn
- Sử dụng phí Mining phù hợp để xác nhận kịp thời



### Chiến lược sử dụng





- Cân bằng thanh khoản On-Chain/Lightning phù hợp với nhu cầu của bạn
- Zeus Swap cho các điều chỉnh một lần, kênh trực tiếp cho các nhu cầu lâu dài



## So sánh với các dịch vụ hoán đổi khác



### Zeus Swap so với Boltz Exchange



Zeus Swap sử dụng công nghệ nền tảng của Boltz nhưng có một số cải tiến quan trọng:



**Lợi ích của Zeus Swap**:




- Interface hợp nhất**: tích hợp gốc trong kỹ thuật web Zeus Wallet so với Interface Boltz
- API WebSocket**: cập nhật theo thời gian thực so với thăm dò thủ công
- Quản lý tự động**: thanh toán tự động và quản lý Address
- Hỗ trợ di động**: chỉ tối ưu hóa điện thoại thông minh so với máy tính để bàn
- Tài liệu Swagger**: API REST hoàn chỉnh dành cho nhà phát triển



**Boltz vẫn có lợi thế** vì tính độc lập hoàn toàn và có thể sử dụng với bất kỳ thiết lập Bitcoin/Lightning nào.



Zeus Swap chuyển đổi công nghệ Boltz đã được chứng minh thành trải nghiệm người dùng phổ biến, tương tự như sự khác biệt giữa một giao thức thô và một ứng dụng thân thiện với người dùng.



### Zeus Swap vs Phoenix/Breez (hoán đổi tích hợp)



Phoenix và Breez tích hợp các chức năng hoán đổi minh bạch, giúp người dùng cuối không phải bận tâm đến sự phức tạp về mặt kỹ thuật. Phoenix sử dụng hệ thống hoán đổi vào/ra tự động, trong đó người dùng không phân biệt rõ ràng giữa các lớp Bitcoin: họ "gửi đến Bitcoin Address" và ứng dụng sẽ xử lý việc hoán đổi ở chế độ nền.



Cách tiếp cận siêu đơn giản này hoàn toàn phù hợp với người mới bắt đầu, nhưng lại hạn chế khả năng hiểu và kiểm soát các thao tác. Zeus Swap áp dụng triết lý giáo dục hơn: người dùng hiểu rằng họ đang hoán đổi giữa hai lớp riêng biệt, dần dần phát triển hiểu biết của họ về hệ sinh thái hai Layer Bitcoin.



## So sánh chi tiết về phí và hạn mức (2024)



⚠️ **Cảnh báo**: Phí có thể thay đổi theo thời gian tùy thuộc vào điều kiện thị trường và cập nhật dịch vụ. Luôn kiểm tra phí hiển thị trên Interface trước khi xác nhận giao dịch hoán đổi.



| Service | Submarine Swap (BTC→LN) | Reverse Swap (LN→BTC) | Montant minimum |
|---------|-------------------------|----------------------|-----------------|
| **Zeus Swap** | ~0.1% + frais minage | 0.5% + frais minage | 25 000 sats |
| **Boltz** | 0.2% + frais minage | 0.5% + frais minage | 50 000 sats |
| **Phoenix** | Frais minage uniquement | 0.4% fixe | 10 000 sats |
| **Breez** | 0.25% + frais réseau | 0.5% + frais minage | 50 000 sats |

Zeus Swap mang lại sự cân bằng giữa tính dễ sử dụng và khả năng kiểm soát kỹ thuật: dễ tiếp cận hơn Boltz, linh hoạt hơn Phoenix/Breez, với phương pháp tiếp cận không giám sát chặt chẽ.



## Phần kết luận



Zeus Swap là một cải tiến đáng kể trong hệ sinh thái Bitcoin, giải quyết một cách khéo léo thách thức về khả năng tương tác giữa mạng chính và Lightning Network. Bằng cách kết hợp tính bảo mật mã hóa mạnh mẽ của hoán đổi nguyên tử với trải nghiệm người dùng dễ tiếp cận, dịch vụ này dân chủ hóa việc quản lý Bitcoin kép Layer mà không ảnh hưởng đến các nguyên tắc về chủ quyền tài chính.



Kiến trúc phi lưu ký của Zeus Swap, kế thừa công nghệ Boltz đã được kiểm chứng, đảm bảo tiền của bạn luôn nằm trong tầm kiểm soát độc quyền của bạn trong suốt quá trình hoán đổi. Cách tiếp cận này tôn trọng tinh thần của Bitcoin, đồng thời mang đến sự tiện lợi cần thiết cho người dùng khi áp dụng rộng rãi. Tính minh bạch về giá cả và việc không áp dụng quy trình KYC càng củng cố giá trị độc đáo này.



Đối với người dùng Bitcoin hiện đại, Zeus Swap là một công cụ chiến lược giúp tối ưu hóa việc phân bổ thanh khoản theo nhu cầu: On-Chain là nơi lưu trữ an toàn cho mục đích tiết kiệm dài hạn, Lightning là nơi sẵn sàng cho chi tiêu hàng ngày và các giao dịch nhỏ. Tính linh hoạt này biến việc quản lý Bitcoin từ một hạn chế kỹ thuật thành một lợi thế cạnh tranh.



Sự phát triển trong tương lai của Zeus Swap, được hỗ trợ bởi đội ngũ Zeus LSP giàu kinh nghiệm và cộng đồng nguồn mở Boltz, hứa hẹn sẽ tiếp tục cải thiện về chi phí, thời gian xử lý và trải nghiệm người dùng. Dịch vụ này là một phần của xu hướng toàn cầu hướng tới sự hoàn thiện của cơ sở hạ tầng Bitcoin, nơi sự tinh vi về kỹ thuật trở nên minh bạch đối với người dùng cuối.



## Tài nguyên



### Tài liệu chính thức




- [Zeus Swap - Cổng thông tin web](https://swaps.zeuslsp.com)
- [Zeus Wallet - Ứng dụng di động](https://zeusln.app)
- [Blog Zeus - Thông báo và hướng dẫn](https://blog.zeusln.com)
- [Tài liệu kỹ thuật của Zeus](https://docs.zeusln.app)



### Cộng đồng và hỗ trợ




- [Twitter Zeus (@zeusln)](https://twitter.com/zeusln)
- [Telegram Zeus](https://t.me/ZeusLN)
- [GitHub Zeus](https://github.com/ZeusLN)