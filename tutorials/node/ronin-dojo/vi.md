---
name: RoninDojo

description: Cài đặt và sử dụng node Bitcoin RoninDojo của bạn.
---
***CẢNH BÁO:** Sau vụ bắt giữ các nhà sáng lập của Samourai Wallet và việc tịch thu máy chủ của họ vào ngày 24 tháng 4, một số tính năng của RoninDojo, như Whirlpool, không còn hoạt động. Tuy nhiên, có khả năng những công cụ này có thể được khôi phục hoặc ra mắt lại theo cách khác trong những tuần tới. Thêm vào đó, vì mã nguồn của RoninDojo được lưu trữ trên GitLab của Samourai, cũng đã bị tịch thu, hiện tại không thể tải mã nguồn từ xa. Các đội ngũ RoninDojo có khả năng đang làm việc để tái xuất bản mã nguồn.*

_Chúng tôi đang chú ý theo dõi sự phát triển của vụ việc này cũng như các công cụ liên quan. Hãy yên tâm rằng chúng tôi sẽ cập nhật hướng dẫn này khi có thông tin mới._

_Hướng dẫn này được cung cấp chỉ với mục đích giáo dục và thông tin. Chúng tôi không ủng hộ hoặc khuyến khích sử dụng những công cụ này cho mục đích phạm tội. Mỗi người dùng có trách nhiệm tuân thủ luật pháp tại quốc gia của họ._

_Hướng dẫn này dành riêng cho việc cài đặt RoninDojo v1. Để tận dụng những cải tiến và tính năng mới nhất, tôi rất khuyến khích bạn tham khảo hướng dẫn của chúng tôi dành riêng cho việc cài đặt trực tiếp RoninDojo v2 trên Raspberry Pi của bạn:_ https://planb.network/tutorials/node/bitcoin/ronin-dojo-v2-0ddb3854-6f38-4466-b4e2-f66c028e0dd8

---

Việc chạy và sử dụng node của riêng bạn là cần thiết để thực sự tham gia vào mạng lưới Bitcoin. Mặc dù việc chạy một node Bitcoin không mang lại lợi ích tài chính cho người dùng, nhưng nó cho phép họ bảo vệ quyền riêng tư, hành động độc lập và kiểm soát niềm tin của họ vào mạng lưới.

Trong bài viết này, chúng ta sẽ xem xét chi tiết về RoninDojo, một giải pháp tuyệt vời để chạy node Bitcoin của riêng bạn.

### Mục Lục:

- RoninDojo là gì?
- Chọn phần cứng nào?
- Cách cài đặt RoninDojo?
- Cách sử dụng RoninDojo?
- Kết luận

Nếu bạn không quen với cách hoạt động của một node Bitcoin và vai trò của nó, tôi khuyên bạn nên bắt đầu bằng cách đọc bài viết này: Node Bitcoin - Phần 1/2: Khái niệm Kỹ thuật.

![Samourai](assets/1.webp)

## RoninDojo là gì?

Dojo là một máy chủ node Bitcoin đầy đủ được phát triển bởi đội ngũ Samourai Wallet. Bạn có thể tự do cài đặt nó trên bất kỳ máy nào.

RoninDojo là một trợ lý cài đặt và công cụ quản lý cho Dojo và nhiều công cụ khác. RoninDojo mang lại bản triển khai gốc của Dojo và thêm vào nhiều công cụ khác, đồng thời làm cho việc cài đặt và quản lý trở nên dễ dàng hơn.

Họ cũng cung cấp một giải pháp phần cứng "plug-and-play", RoninDojo Tanto, với RoninDojo được cài đặt sẵn trên một máy được lắp ráp bởi đội ngũ của họ. Tanto là một giải pháp trả phí, phù hợp với những ai không muốn tự mình thực hiện.

Mã nguồn của RoninDojo là mã nguồn mở, vì vậy cũng có thể cài đặt giải pháp này trên phần cứng của riêng bạn. Lựa chọn này tiết kiệm chi phí nhưng đòi hỏi một chút thao tác nhiều hơn, đó là những gì chúng ta sẽ thực hiện trong bài viết này.

RoninDojo là một Dojo, vì vậy nó cho phép tích hợp dễ dàng Whirlpool CLI vào node Bitcoin của bạn để có trải nghiệm CoinJoin tốt nhất có thể. Với Whirlpool CLI, không chỉ bạn có thể để bitcoin của mình remix 24/7 mà không cần phải giữ máy tính cá nhân của mình bật, nhưng bạn cũng có thể cải thiện đáng kể quyền riêng tư của mình.
RoninDojo tích hợp nhiều công cụ khác phụ thuộc vào Dojo của bạn, như máy tính Boltzmann, xác định mức độ riêng tư của một giao dịch, máy chủ Electrum để kết nối các ví Bitcoin khác nhau của bạn với node của bạn, hoặc máy chủ Mempool để quan sát giao dịch của bạn một cách riêng tư. So với một giải pháp node khác như Umbrel, mà tôi đã giới thiệu cho bạn trong bài viết này, RoninDojo tập trung sâu vào các giải pháp và công cụ "On Chain" tối ưu hóa quyền riêng tư của người dùng. Do đó, RoninDojo không cho phép tương tác với Lightning Network.

RoninDojo cung cấp ít công cụ hơn so với Umbrel, nhưng những tính năng thiết yếu ít ỏi dành cho một Bitcoiner có mặt trên Ronin lại vô cùng ổn định.

Vì vậy, nếu bạn không cần tất cả các tính năng của một máy chủ Umbrel và chỉ muốn một node đơn giản và ổn định với một số công cụ thiết yếu như Whirlpool hoặc Mempool, thì RoninDojo có lẽ là một giải pháp tốt cho bạn.

Theo ý kiến của tôi, trọng tâm phát triển của Umbrel chủ yếu là vào Lightning Network và các công cụ đa năng. Nó vẫn là một node Bitcoin, nhưng mục tiêu là biến nó thành một mini-server đa nhiệm. Ngược lại, trọng tâm phát triển của RoninDojo hợp lý hơn với các đội ngũ tại Samourai Wallet và tập trung vào các công cụ thiết yếu cho một Bitcoiner, cho phép độc lập hoàn toàn và quản lý quyền riêng tư trên Bitcoin một cách tối ưu.

Xin lưu ý rằng việc thiết lập một node RoninDojo phức tạp hơn một chút so với node Umbrel.

Bây giờ chúng ta đã có thể mô tả về RoninDojo, hãy xem cách thiết lập node này cùng nhau.

## Máy chủ nào để chọn?

Để chọn máy chủ và chạy RoninDojo, bạn có một số lựa chọn.

Như đã giải thích trước đó, lựa chọn đơn giản nhất là đặt hàng Tanto, một máy plug-and-play được thiết kế đặc biệt cho mục đích này. Để đặt hàng của bạn, hãy vào đây: [link](https://shop.ronindojo.io/product-category/nodes/).

Vì các đội ngũ RoninDojo sản xuất mã nguồn mở, cũng có thể triển khai RoninDojo trên các máy khác. Bạn có thể tìm phiên bản mới nhất của trình hướng dẫn cài đặt trên trang này: [link](https://ronindojo.io/en/downloads.html), và phiên bản mới nhất của mã trên trang này: [link](https://code.samourai.io/ronindojo/RoninDojo).

Cá nhân tôi, tôi đã cài đặt nó trên một Raspberry Pi 4 8GB và mọi thứ hoạt động hoàn hảo.

Tuy nhiên, xin lưu ý rằng các đội ngũ RoninDojo chỉ ra rằng thường xuyên có vấn đề với vỏ và bộ chuyển đổi SSD. Do đó, không khuyến khích sử dụng vỏ có cáp cho SSD của máy bạn. Thay vào đó, nên sử dụng một thẻ mở rộng lưu trữ được thiết kế đặc biệt cho bo mạch chủ của bạn, như thẻ này: Raspberry Pi 4 Storage Expansion Card.

Dưới đây là một ví dụ về cách thiết lập node RoninDojo của riêng bạn:

- Một Raspberry Pi 4.
- Một vỏ có quạt.
- Một thẻ mở rộng lưu trữ tương thích.
- Một cáp nguồn.
- Một thẻ micro SD công nghiệp 16GB hoặc lớn hơn.
- Một SSD 1TB hoặc lớn hơn.
- Một cáp Ethernet RJ45, loại 8 được khuyến nghị.

## Cách cài đặt RoninDojo?

### Bước 1: Chuẩn bị thẻ micro SD khởi động.

Sau khi bạn đã lắp ráp máy của mình, bạn có thể bắt đầu cài đặt RoninDojo. Để làm điều này, bắt đầu bằng cách tạo một thẻ micro SD khởi động bằng cách ghi hình ảnh đĩa thích hợp vào nó.

Chèn thẻ micro SD của bạn vào máy tính cá nhân, sau đó truy cập trang web chính thức của RoninDojo để tải xuống hình ảnh đĩa RoninOS: https://ronindojo.io/en/downloads.html.
Tải xuống hình ảnh đĩa tương ứng với phần cứng của bạn. Trong trường hợp của tôi, tôi đã tải xuống hình ảnh "MANJARO-ARM-RONINOS-RPI4-22.03.IMG.XZ":
![Tải xuống hình ảnh đĩa RoninOS](assets/2.webp)

Sau khi hình ảnh được tải xuống, hãy xác minh tính toàn vẹn của nó bằng cách sử dụng tệp .SHA256 tương ứng. Tôi sẽ mô tả chi tiết cách làm điều này trong bài viết này: Làm thế nào để xác minh tính toàn vẹn của phần mềm Bitcoin trên Windows?

Hướng dẫn cụ thể để xác minh tính toàn vẹn của RoninOS cũng có sẵn trên trang này: https://wiki.ronindojo.io/en/extras/verify.

Để ghi hình ảnh này vào thẻ micro SD của bạn, bạn có thể sử dụng phần mềm như Balena Etcher, mà bạn có thể tải xuống tại đây: https://www.balena.io/etcher/.

Để làm điều này, chọn hình ảnh trong Etcher và ghi nó vào thẻ micro SD:

![Ghi hình ảnh đĩa với Etcher](assets/3.webp)

Khi quá trình hoàn tất, bạn có thể chèn thẻ micro SD khởi động được vào Raspberry Pi và bật máy.

### Bước 2: Cấu hình RoninOS.

RoninOS là hệ điều hành của nút RoninDojo của bạn. Đây là một phiên bản được chỉnh sửa của Manjaro, một bản phân phối Linux. Sau khi khởi động máy và chờ vài phút, bạn có thể bắt đầu cấu hình của nó.

Để kết nối từ xa với nó, bạn sẽ cần tìm địa chỉ IP của máy RoninDojo của mình. Để làm điều này, bạn có thể, ví dụ, kết nối với bảng điều khiển quản trị của hộp internet của bạn, hoặc bạn cũng có thể tải xuống phần mềm như https://angryip.org/ để quét mạng cục bộ của bạn và tìm địa chỉ IP của máy.

Một khi bạn đã tìm thấy IP, bạn có thể kiểm soát máy của mình từ một máy tính khác được kết nối với cùng một mạng cục bộ sử dụng SSH.

Từ một máy tính chạy macOS hoặc Linux, chỉ cần mở terminal. Từ một máy tính chạy Windows, bạn có thể sử dụng một công cụ chuyên biệt như Putty hoặc trực tiếp sử dụng Windows PowerShell.

Khi terminal được mở, gõ lệnh sau:

> ssh root@192.168.?.?

Chỉ cần thay thế hai dấu hỏi bằng IP của RoninDojo mà bạn đã tìm thấy trước đó.
Mẹo: Trong Shell, nhấp chuột phải để dán một mục.

Tiếp theo, bạn sẽ đến với bảng điều khiển Manjaro. Chọn bố cục bàn phím chính xác sử dụng các mũi tên để thay đổi mục tiêu trong danh sách thả xuống.

![Cấu hình Bàn phím Manjaro](assets/4.webp)

Chọn một tên người dùng và mật khẩu cho phiên của bạn. Sử dụng một mật khẩu mạnh và sao lưu an toàn. Bạn có thể tùy chọn sử dụng một mật khẩu yếu trong quá trình cài đặt, và sau đó dễ dàng thay đổi nó bằng cách "copy-paste" vào RoninUI. Điều này sẽ cho phép bạn sử dụng một mật khẩu rất mạnh mà không mất quá nhiều thời gian gõ nó một cách thủ công trong quá trình thiết lập Manjaro.

![Cấu hình Tên người dùng Manjaro](assets/5.webp)

Tiếp theo, bạn cũng sẽ được yêu cầu chọn một mật khẩu root. Đối với mật khẩu root, hãy nhập một mật khẩu mạnh trực tiếp. Bạn sẽ không thể thay đổi nó từ RoninUI. Ngoài ra, nhớ sao lưu mật khẩu root này một cách an toàn.

Sau đó nhập vị trí và múi giờ của bạn.

![Cấu hình Múi giờ Manjaro](assets/6.webp)

![Cấu hình Vị trí Manjaro](assets/7.webp)

Tiếp theo, chọn một tên máy chủ.

![Cấu hình Tên máy chủ Manjaro](assets/8.webp)

Cuối cùng, xác minh thông tin cấu hình Manjaro và xác nhận.

![Xác minh Thông tin Cấu hình ManjaroOS](assets/9.webp)

### Bước 3: Tải xuống RoninDojo.
Cấu hình ban đầu của RoninOS sẽ được thực hiện. Khi hoàn tất, như hình chụp màn hình ở trên, máy sẽ khởi động lại. Hãy chờ một vài phút, sau đó nhập lệnh sau để kết nối lại với máy RoninDojo của bạn:
> ssh tên_người_dùng@192.168.?.?

Chỉ cần thay thế "tên_người_dùng" bằng tên người dùng bạn đã chọn trước đó, và thay thế các dấu hỏi bằng địa chỉ IP của RoninDojo của bạn.

Sau đó nhập mật khẩu người dùng của bạn.

Trong terminal, nó sẽ trông như thế này:

![Kết nối SSH tới RoninOS](assets/10.webp)

Bây giờ bạn đã kết nối với máy của mình, hiện chỉ có RoninOS. Bây giờ bạn cần cài đặt RoninDojo trên đó.

Tải phiên bản mới nhất của RoninDojo bằng cách nhập lệnh sau:

> git clone https://code.samourai.io/ronindojo/RoninDojo

Việc tải xuống sẽ nhanh chóng. Trong terminal, bạn sẽ thấy điều này:

![Cloning RoninDojo](assets/11.webp)

Chờ cho đến khi việc tải xuống hoàn tất, sau đó cài đặt và truy cập giao diện người dùng RoninDojo bằng lệnh sau:

> ~/RoninDojo/ronin

Bạn sẽ được yêu cầu nhập mật khẩu người dùng của mình:

![Xác minh mật khẩu Node Bitcoin](assets/12.webp)

Lệnh này chỉ cần thiết lần đầu tiên bạn truy cập RoninDojo của mình. Sau đó, để truy cập RoninCLI qua SSH, bạn chỉ cần nhập lệnh [SSH tên_người_dùng@192.168.?.?] thay thế "tên_người_dùng" bằng tên người dùng của bạn và nhập địa chỉ IP của node của bạn. Bạn sẽ được yêu cầu nhập mật khẩu người dùng.

Tiếp theo, bạn sẽ thấy hoạt ảnh tuyệt vời này:

![Hoạt ảnh khởi chạy RoninCLI](assets/13.webp)

Sau đó bạn sẽ cuối cùng đến với giao diện người dùng CLI của RoninDojo.

### Bước 4: Cài đặt RoninDojo.

Từ menu chính, điều hướng đến menu "System" bằng cách sử dụng các phím mũi tên trên bàn phím của bạn. Nhấn phím enter để xác nhận lựa chọn của bạn.

![Menu điều hướng RoninCLI đến Hệ thống](assets/14.webp)

Sau đó đi đến menu "System Setup & Install".

![Menu điều hướng RoninCLI đến cài đặt hệ thống RoninDojo](assets/15.webp)

Cuối cùng, kiểm tra "System Setup" và "Install RoninDojo" sử dụng phím cách, sau đó chọn "Accept" để bắt đầu cài đặt.

![Xác nhận cài đặt RoninDojo](assets/16.webp)

Hãy để quá trình cài đặt diễn ra một cách nhẹ nhàng. Trong trường hợp của tôi, nó mất khoảng 2 giờ. Giữ terminal mở trong suốt quá trình.

Thỉnh thoảng kiểm tra terminal của bạn, vì bạn sẽ được yêu cầu nhấn một phím tại một số giai đoạn của quá trình cài đặt, như ở đây chẳng hạn:

![Quá trình cài đặt RoninDojo đang diễn ra](assets/17.webp)

Khi kết thúc quá trình cài đặt, bạn sẽ thấy các container khác nhau bắt đầu:

![Khởi động container Node](assets/18.webp)

Sau đó node của bạn sẽ khởi động lại. Kết nối lại với RoninCLI cho bước tiếp theo.

![Khởi động lại node Bitcoin](assets/19.webp)

### Bước 5: Tải xuống chuỗi proof-of-work và truy cập RoninUI.

Khi quá trình cài đặt hoàn tất, node của bạn sẽ bắt đầu tải xuống chuỗi proof-of-work của Bitcoin. Điều này được gọi là Initial Block Download (IBD). Thông thường mất từ 2 đến 14 ngày tùy thuộc vào kết nối internet và thiết bị của bạn.

Bạn có thể theo dõi tiến trình tải xuống chuỗi bằng cách truy cập giao diện web RoninUI.

Để truy cập từ mạng nội bộ, gõ vào thanh địa chỉ của trình duyệt:

- Hoặc trực tiếp nhập địa chỉ IP của máy của bạn (192.168.?.?)

- Hoặc nhập: ronindojo.local
Hãy nhớ tắt VPN của bạn nếu bạn đang sử dụng.

### Khả năng xảy ra

Nếu bạn không thể kết nối với RoninUI từ trình duyệt của mình, hãy kiểm tra sự hoạt động đúng đắn của ứng dụng từ Terminal của bạn đã kết nối với node qua SSH. Kết nối với menu chính bằng cách làm theo các bước trước:

- Gõ: SSH username@192.168.?.? thay thế bằng thông tin đăng nhập của bạn.

- Nhập mật khẩu người dùng của bạn.

Một khi đã vào menu chính, đi đến:

> RoninUI > Khởi động lại

Nếu ứng dụng khởi động lại đúng cách, đó là vấn đề với kết nối từ trình duyệt của bạn. Kiểm tra xem bạn không đang sử dụng VPN và đảm bảo bạn đang kết nối với cùng một mạng với node của mình.

Nếu việc khởi động lại xuất hiện lỗi, hãy thử cập nhật hệ điều hành và sau đó cài đặt lại RoninUI. Để cập nhật OS:

> Hệ thống > Cập nhật Phần mềm > Cập nhật Hệ điều hành

Sau khi cập nhật và khởi động lại hoàn tất, kết nối lại với node của bạn qua SSH và cài đặt lại RoninUI:

> RoninUI > Cài đặt lại

Sau khi tải lại RoninUI, hãy thử kết nối với RoninUI qua trình duyệt của bạn.

> Mẹo: Nếu bạn vô tình thoát khỏi RoninCLI và tìm mình ở terminal Manjaro, chỉ cần nhập lệnh "ronin" để trở lại trực tiếp menu chính của RoninCLI.

### Đăng nhập Web

Bạn cũng có thể đăng nhập vào giao diện web RoninUI từ bất kỳ mạng nào sử dụng Tor. Để làm điều này, lấy địa chỉ Tor của RoninUI của bạn từ RoninCLI:

> Thông tin đăng nhập > Ronin UI

Lấy địa chỉ Tor kết thúc bằng .onion và sau đó đăng nhập vào Ronin UI bằng cách nhập địa chỉ này vào trình duyệt Tor của bạn. Hãy cẩn thận không để lộ các thông tin đăng nhập khác nhau của bạn, vì chúng là thông tin nhạy cảm.

![Giao diện đăng nhập web RoninUI](assets/20.webp)

Một khi đã đăng nhập, bạn sẽ được yêu cầu mật khẩu người dùng của mình. Đó là cùng một mật khẩu bạn sử dụng để đăng nhập qua SSH.

![Bảng điều khiển quản lý giao diện web RoninUI](assets/21.webp)

Chúng ta có thể thấy tiến trình của IBD (Initial Block Download) ở đây. Hãy kiên nhẫn, bạn đang lấy tất cả các giao dịch được thực hiện trên Bitcoin kể từ ngày 3 tháng 1 năm 2009.

Sau khi tải xuống toàn bộ blockchain, indexer sẽ nén cơ sở dữ liệu. Thao tác này mất khoảng 12 giờ. Bạn cũng có thể theo dõi tiến trình của nó dưới mục "Indexer" trên RoninUI.

Node RoninDojo của bạn sẽ hoạt động đầy đủ sau này:

![Indexer đồng bộ hóa ở 100% node hoạt động](assets/22.webp)

Nếu bạn muốn thay đổi mật khẩu người dùng sang một cái mạnh hơn, bạn có thể làm điều đó ngay bây giờ từ tab "Cài đặt". Trên RoninDojo, không có lớp bảo mật bổ sung, vì vậy tôi khuyên bạn nên chọn một mật khẩu thực sự mạnh và chăm sóc việc sao lưu của nó.

## Làm thế nào để sử dụng RoninDojo?

Một khi chuỗi đã được tải xuống và nén, bạn có thể bắt đầu tận hưởng các dịch vụ được cung cấp bởi node RoninDojo mới của mình. Hãy xem cách sử dụng chúng.

### Kết nối phần mềm ví với electrs.

Tiện ích đầu tiên của node mới cài đặt và đồng bộ hóa của bạn sẽ là phát sóng các giao dịch của bạn lên mạng Bitcoin. Do đó, bạn có thể muốn kết nối các phần mềm quản lý ví khác nhau của mình với nó.

Bạn có thể làm điều này sử dụng Electrum Rust Server (electrs). Ứng dụng này thường được cài đặt sẵn trên node RoninDojo của bạn. Nếu không, bạn có thể cài đặt nó thủ công từ giao diện RoninCLI.

Chỉ cần đi đến:

> Ứng dụng > Quản lý Ứng dụng > Cài đặt Electrum Server

Để lấy địa chỉ Tor của Electrum Server của bạn, từ menu RoninCLI, đi đến:

> Thông tin đăng nhập > Electrs
Bạn chỉ cần nhập liên kết .onion vào phần mềm ví của bạn. Ví dụ, trong Sparrow Wallet, đi tới tab:
> File > Preferences > Server

Trong loại server, chọn "Private Electrum", sau đó nhập địa chỉ Tor của Electrum Server của bạn vào trường tương ứng. Cuối cùng, nhấn vào "Test Connection" để kiểm tra và lưu kết nối của bạn.

![Giao diện kết nối Sparrow Wallet với electrs](assets/23.webp)

### Kết nối phần mềm ví với Samourai Dojo.

Thay vì sử dụng Electrs, bạn cũng có thể sử dụng Samourai Dojo để kết nối phần mềm ví tương thích của bạn với nút RoninDojo của bạn. Ví dụ, Samourai Wallet cung cấp tùy chọn này.

Để thực hiện, bạn chỉ cần quét mã QR kết nối của Dojo. Để truy cập từ RoninUI, nhấn vào tab "Dashboard" và sau đó nhấn vào nút "Manage" trong hộp của Dojo của bạn. Bạn sẽ có thể thấy mã QR kết nối cho Dojo và BTC-RPC Explorer của bạn. Để hiển thị chúng, nhấn vào "Display values".

![Lấy mã QR kết nối với Dojo](assets/24.webp)

Để kết nối Samourai Wallet của bạn với Dojo, bạn sẽ cần quét mã QR này trong quá trình cài đặt ứng dụng:

![Kết nối với Dojo từ ứng dụng Samourai Wallet](assets/25.webp)

### Sử dụng Mempool Explorer của riêng bạn.

Một công cụ thiết yếu cho người dùng Bitcoin, explorer cho phép bạn kiểm tra các thông tin khác nhau về chuỗi Bitcoin. Với Mempool, ví dụ, bạn có thể kiểm tra theo thời gian thực các phí do người dùng khác áp dụng để điều chỉnh phí của mình cho phù hợp. Bạn cũng có thể kiểm tra trạng thái xác nhận của một giao dịch của mình hoặc xem số dư của một địa chỉ.

Các công cụ explorer có thể phơi bày bạn trước rủi ro về quyền riêng tư và yêu cầu bạn phải tin tưởng vào cơ sở dữ liệu của bên thứ ba. Khi bạn sử dụng công cụ trực tuyến này mà không thông qua nút của riêng mình:

- Bạn có nguy cơ rò rỉ thông tin về ví của mình.

- Bạn tin tưởng vào quản trị viên trang web về chuỗi proof-of-work mà họ lưu trữ.

Để tránh những rủi ro này, bạn có thể sử dụng thể hiện Mempool của riêng mình trên nút qua mạng Tor. Với giải pháp này, không chỉ bạn bảo vệ quyền riêng tư khi sử dụng dịch vụ, mà bạn cũng không cần phải tin tưởng vào nhà cung cấp vì bạn truy vấn cơ sở dữ liệu của riêng mình.

Để thực hiện, bắt đầu bằng cách cài đặt Mempool Space Visualizer từ RoninCLI:

> Applications > Manage Applications > Install Mempool Space Visualizer

Một khi đã cài đặt, lấy liên kết tới Mempool của bạn. Địa chỉ Tor sẽ cho phép bạn truy cập nó từ bất kỳ mạng nào. Tương tự, chúng ta lấy liên kết này qua RoninCLI:

> Credentials > Mempool

![Lấy địa chỉ Tor Mempool](assets/26.webp)

Chỉ cần nhập địa chỉ Tor Mempool của bạn vào trình duyệt Tor để tận hưởng thể hiện Mempool của riêng bạn, dựa trên dữ liệu của bạn. Tôi khuyên bạn nên thêm địa chỉ Tor này vào danh sách yêu thích để truy cập nhanh hơn. Bạn cũng có thể tạo một lối tắt trên màn hình desktop của mình.

![Giao diện Mempool Space](assets/27.webp)

Nếu bạn chưa có trình duyệt Tor, bạn có thể tải về tại đây: https://www.torproject.org/download/

Bạn cũng có thể truy cập từ điện thoại thông minh của mình bằng cách cài đặt Trình duyệt Tor và nhập cùng một địa chỉ. Từ bất cứ đâu, bạn có thể xem trạng thái của chuỗi Bitcoin sử dụng nút của riêng mình.

### Sử dụng Whirlpool CLI.

Nút RoninDojo của bạn cũng bao gồm WhirlpoolCLI, một giao diện dòng lệnh từ xa để tự động hóa các lần trộn Whirlpool.
Khi bạn thực hiện một CoinJoin với cài đặt Whirlpool, ứng dụng bạn đang sử dụng phải luôn mở để thực hiện các lần trộn và tái trộn. Quá trình này có thể gây phiền toái cho người dùng muốn có bộ anon cao, vì thiết bị chạy ứng dụng với Whirlpool phải luôn bật. Trên thực tế, điều này có nghĩa là nếu bạn muốn tham gia UTXOs của mình vào tái trộn 24/7, bạn sẽ cần phải giữ máy tính cá nhân hoặc điện thoại của mình luôn bật với ứng dụng mở.

Một giải pháp cho hạn chế này là sử dụng WhirlpoolCLI trên một máy tính được dự định để luôn bật, chẳng hạn như một node Bitcoin. Với cách này, UTXOs của chúng ta có thể được tái trộn 24/7 mà không cần phải giữ một máy khác ngoài node Bitcoin của chúng ta hoạt động.

WhirlpoolCLI được sử dụng với WhirlpoolGUI, một giao diện đồ họa được cài đặt trên máy tính cá nhân để quản lý Coinjoins một cách dễ dàng. Tôi sẽ giải thích chi tiết cách thiết lập Whirlpool CLI với dojo của riêng bạn trong bài viết này: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=dans%20cette%20partie.-,Tutoriel%20%3A%20Whirpool%20CLI%20sur%20Dojo%20et%20Whirlpool%20GUI.,-Si%20vous%20souhaitez).

Để tìm hiểu thêm về Coinjoin nói chung, tôi giải thích mọi thứ trong bài viết này: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin).

### Sử dụng Công cụ Thống kê Whirlpool.

Sau khi thực hiện CoinJoins với Whirlpool, bạn có thể muốn biết mức độ riêng tư thực sự của UTXOs đã trộn của mình. Công cụ Thống kê Whirlpool cho phép bạn dễ dàng làm điều này. Với công cụ này, bạn có thể tính điểm triển vọng và điểm hồi tưởng của UTXOs đã trộn của mình. Để tìm hiểu thêm về cách tính các Anon Sets và cách chúng hoạt động, tôi khuyên bạn đọc phần này: [link](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment).

Công cụ này được cài đặt sẵn trên RoninDojo của bạn. Hiện tại, nó chỉ có sẵn từ RoninCLI. Để khởi chạy nó từ menu chính, đi đến:

> Bộ công cụ Samourai > Công cụ Thống kê Whirlpool

Hướng dẫn sử dụng sẽ xuất hiện. Khi hoàn thành, nhấn bất kỳ phím nào để truy cập các dòng lệnh:

![Giao diện chính của phần mềm Công cụ Thống kê Whirlpool](assets/28.webp)

Cửa sổ terminal sẽ được hiển thị:

> wst#/tmp>

Để thoát khỏi giao diện này và quay lại menu RoninCLI, chỉ cần nhập lệnh:

> quit

Để bắt đầu, chúng ta sẽ thiết lập proxy trên Tor để trích xuất dữ liệu OXT một cách hoàn toàn riêng tư. Nhập lệnh:

> socks5 127.0.0.1:9050

Sau đó tải xuống dữ liệu từ hồ chứa giao dịch của bạn:

> download 0001
>
> Thay thế 0001 bằng mã định danh hồ chứa mà bạn quan tâm.

Các mã định danh hồ chứa như sau trên WST:

- Hồ 0.5 bitcoins: 05

- Hồ 0.05 bitcoins: 005

- Hồ 0.01 bitcoins: 001

- Hồ 0.001 bitcoins: 0001
![Tải dữ liệu từ hồ 0001 từ OXT](assets/29.webp)
Sau khi dữ liệu được tải xuống, hãy tải nó với lệnh:

> load 0001
>
> Thay thế 0001 bằng mã số của hồ bạn quan tâm.

![Tải dữ liệu từ hồ 0001](assets/30.webp)
Hãy để quá trình tải diễn ra, có thể mất vài phút. Sau khi tải dữ liệu, gõ lệnh score theo sau là TXID (mã định danh giao dịch) của bạn để nhận các Anon Sets:

> score TXID
>
> Thay thế TXID bằng mã định danh của giao dịch của bạn.

![In điểm số tiềm năng và điểm số hồi tưởng của TXID đã cho](assets/31.webp)

WST sau đó sẽ hiển thị điểm số hồi tưởng (Backward-looking metrics) theo sau là điểm số tiềm năng (Forward-looking metrics). Ngoài điểm số của các Anon Sets, WST cũng cung cấp cho bạn tỷ lệ lan truyền của output trong hồ dựa trên anon set.

Xin lưu ý rằng điểm số tiềm năng của UTXO của bạn được tính dựa trên TXID của lần trộn đầu tiên của bạn, không phải lần trộn cuối cùng. Ngược lại, điểm số hồi tưởng của một UTXO được tính dựa trên TXID của chu kỳ cuối cùng.

Một lần nữa, nếu bạn không hiểu những khái niệm này về Anon Sets, tôi khuyên bạn đọc phần này của bài viết của tôi về Coinjoin nơi tôi giải thích mọi thứ chi tiết với sơ đồ: [https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment](https://www.pandul.fr/post/comprendre-et-utiliser-le-coinjoin-sur-bitcoin#:~:text=perdre%20en%20confidentialit%C3%A9.-,Anon%20Sets.,-Comme%20expliqu%C3%A9%20pr%C3%A9c%C3%A9demment)

### Sử dụng máy tính Boltzmann.

Máy tính Boltzmann là một công cụ cho phép bạn dễ dàng tính toán các chỉ số tiên tiến trên một giao dịch Bitcoin, bao gồm mức độ entropy của nó. Tất cả dữ liệu này sẽ giúp bạn định lượng mức độ riêng tư của một giao dịch và phát hiện bất kỳ lỗi tiềm ẩn nào. Công cụ này được cài đặt sẵn trên nút RoninDojo của bạn.

Để truy cập nó từ RoninCLI, kết nối qua SSH, sau đó đi đến menu:

> Samourai Toolkit > Máy tính Boltzmann

Trước khi giải thích cách sử dụng nó trên RoninDojo, tôi sẽ giải thích những chỉ số này đại diện cho cái gì, chúng được tính toán như thế nào và chúng được sử dụng để làm gì.

Những chỉ số này có thể được sử dụng cho bất kỳ giao dịch Bitcoin nào, nhưng chúng đặc biệt thú vị khi nghiên cứu chất lượng của một giao dịch Coinjoin.

1. Chỉ số đầu tiên được phần mềm này tính toán là số lượng các kết hợp có thể. Nó được ghi trên máy tính là "nb combinations". Dựa trên giá trị của các UTXOs, chỉ số này đại diện cho số lượng ánh xạ có thể từ đầu vào đến đầu ra.

> Nếu bạn không quen với thuật ngữ "UTXO", tôi khuyên bạn đọc bài viết ngắn này: Cơ chế của một giao dịch Bitcoin: UTXO, đầu vào và đầu ra.

Nói cách khác, chỉ số này đại diện cho số lượng cách giải thích có thể cho một giao dịch cụ thể. Ví dụ, một cấu trúc Coinjoin Whirlpool 5x5 sẽ có số lượng kết hợp có thể bằng 1496:

![Sơ đồ của một giao dịch Coinjoin trên kycp.org](assets/32.webp)

Credit: KYCP
2. Chỉ số thứ hai được tính toán là entropy của một giao dịch. Do số lượng các tổ hợp có thể rất cao đối với một giao dịch, người ta có thể chọn sử dụng entropy thay thế. Entropy đại diện cho logarit nhị phân của số lượng các tổ hợp có thể có. Công thức của nó như sau:
- E: entropy của giao dịch.
- C: số lượng các tổ hợp có thể có cho giao dịch.

> E = log2(C)

Trong toán học, logarit nhị phân (cơ số 2) là hàm nghịch đảo của hàm lũy thừa của 2. Nói cách khác, logarit nhị phân của x là số mũ mà số 2 phải được nâng lên để thu được giá trị x.

Như vậy:

> E = log2(C)
> C = 2^E

Chỉ số này được biểu thị bằng bit. Ví dụ, đây là cách tính entropy của một giao dịch Coinjoin Whirlpool 5x5, với số lượng các tổ hợp có thể có được đề cập trước đó là 1496:

> C = 1496
>
> E = log2(1496)
>
> E = 10.5469 bit

Do đó, giao dịch Coinjoin này có entropy là 10.5469 bit, đây là một chỉ số rất tốt.

Chỉ số này càng cao, giao dịch càng có nhiều cách giải thích khác nhau, và do đó, giao dịch càng bảo mật.

Hãy xem một ví dụ khác. Đây là một giao dịch "cổ điển" có một đầu vào và hai đầu ra:

![Sơ đồ giao dịch Bitcoin trên oxt.me](assets/34.webp)

Tín dụng: OXT

Giao dịch này chỉ có một cách giải thích có thể:

> [(inp 0) > (Outp 0 ; Outp 1)]

Vì vậy, entropy của nó sẽ bằng 0:

> C = 1
>
> E = log2(C)
>
> E = 0

3. Chỉ số thứ ba được Boltzmann calculator trả về là hiệu quả của Tx gọi là "Hiệu quả Ví". Chỉ số này đơn giản cho phép so sánh giao dịch đầu vào với giao dịch tốt nhất có thể trong cùng một cấu hình.

Chúng ta sẽ giới thiệu khái niệm entropy tối đa, đại diện cho entropy cao nhất có thể đạt được cho một cấu trúc giao dịch nhất định. Ví dụ, một cấu trúc Coinjoin Whirlpool 5x5 sẽ có entropy tối đa là 10.5469. Chỉ số hiệu quả so sánh entropy tối đa này với entropy thực tế của giao dịch đầu vào. Công thức của nó như sau:

- ER: Entropy thực tế được biểu thị bằng bit.
- EM: Entropy tối đa với cùng một cấu trúc được biểu thị bằng bit.
- Ef: Hiệu quả được biểu thị bằng bit.

> Ef = ER - EM
>
> Ef = 10.5469 - 10.5469
>
> Ef = 0 bit

Chỉ số này cũng được biểu thị dưới dạng phần trăm, vì vậy công thức trở thành:

- CR: Số lượng các tổ hợp có thể có thực tế.
- CM: Số lượng các tổ hợp có thể có tối đa với cùng một cấu trúc.
- Ef: Hiệu quả được biểu thị dưới dạng phần trăm.

> Ef = CR/CM
>
> Ef = 1496/1496
>
> Ef = 100%

Một hiệu quả 100% có nghĩa là giao dịch này có sự riêng tư cao nhất có thể so với cấu trúc của nó.

4. Chỉ số thứ tư được tính toán là mật độ entropy. Nó cho phép chúng ta liên hệ entropy với mỗi đầu vào hoặc đầu ra. Chỉ số này có thể được sử dụng để so sánh hiệu quả giữa các giao dịch có kích thước khác nhau.

Việc tính toán rất đơn giản: chúng ta chia entropy của giao dịch cho số lượng đầu vào và đầu ra có mặt. Ví dụ, đối với một Coinjoin Whirlpool 5x5, chúng ta sẽ có:

    ED: Mật độ entropy được biểu thị bằng bit.
    E: Entropy của giao dịch được biểu thị bằng bit.
    T: Tổng số đầu vào và đầu ra trong giao dịch.

T = 5 + 5 = 10
ED = E / TED = 10.5469 / 10
ED = 1.054 bit

Thông tin thứ năm được cung cấp bởi máy tính Boltzmann là bảng xác suất của các liên kết giữa đầu vào và đầu ra. Bảng này đơn giản cung cấp xác suất (điểm Boltzmann) rằng một đầu vào nhất định tương ứng với một đầu ra nhất định.

Nếu chúng ta lấy ví dụ với Whirlpool Coinjoin, bảng xác suất sẽ như sau:

| %       | Đầu ra 0 | Đầu ra 1 | Đầu ra 2 | Đầu ra 3 | Đầu ra 4 |
|---------|----------|----------|----------|----------|----------|
| Đầu vào 0 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 1 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 2 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 3 | 34%      | 34%      | 34%      | 34%      | 34%      |
| Đầu vào 4 | 34%      | 34%      | 34%      | 34%      | 34%      |

Ở đây chúng ta có thể thấy rằng mỗi đầu vào có một xác suất bằng nhau được liên kết với mỗi đầu ra.

Tuy nhiên, nếu chúng ta lấy ví dụ về một giao dịch với một đầu vào và hai đầu ra, nó sẽ trông như thế này:

| Đầu vào | Đầu ra 0 | Đầu ra 1 |
| ----- | -------- | -------- |
| 0     | 100%     | 100%     |

Trong ví dụ này, chúng ta có thể thấy rằng xác suất của mỗi đầu ra đến từ đầu vào 0 là 100%.

Xác suất càng thấp, mức độ bảo mật càng cao.

6. Thông tin thứ sáu được tính toán là số lượng liên kết xác định. Tỷ lệ của các liên kết xác định cũng sẽ được cung cấp. Chỉ số này làm nổi bật số lượng liên kết giữa đầu vào và đầu ra của giao dịch đã cho có xác suất 100%, nghĩa là chúng không thể phủ nhận được.

Tỷ lệ chỉ ra số lượng liên kết xác định trong giao dịch so với tổng số liên kết.

Ví dụ, một giao dịch Coinjoin Whirlpool không có liên kết xác định nào giữa đầu vào và đầu ra. Chỉ số sẽ là không và tỷ lệ cũng là 0%.

Tuy nhiên, đối với giao dịch thứ hai được nghiên cứu (1 đầu vào và 2 đầu ra), chỉ số là 2 và tỷ lệ là 100%.

Do đó, nếu chỉ số này là không, nó chỉ ra mức độ bảo mật tốt.

Bây giờ chúng ta đã nghiên cứu các chỉ số, hãy xem cách tính chúng sử dụng phần mềm này. Từ RoninCLI, đi đến menu:

> Samourai Toolkit > Máy Tính Boltzmann

![Trang chủ phần mềm Máy Tính Boltzmann](assets/35.webp)

Khi phần mềm được khởi chạy, nhập ID giao dịch bạn muốn nghiên cứu. Bạn có thể nhập nhiều giao dịch cùng một lúc bằng cách phân tách chúng bằng dấu phẩy, sau đó nhấn enter:

![Nhập TXID để nghiên cứu trên Máy Tính Boltzmann](assets/36.webp)

Sau đó, máy tính sẽ trả về tất cả các chỉ số chúng ta đã thấy trước đó:

![In dữ liệu của Máy Tính Boltzmann cho TXID này](assets/37.webp)

Gõ lệnh "Quit" để thoát khỏi phần mềm và quay lại menu RoninCLI.

Để tìm hiểu thêm về máy tính Boltzmann, tôi khuyên bạn đọc các bài viết sau:

- https://medium.com/@laurentmt/giới-thiệu-boltzmann-85930984a159

- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
### Kết nối Bisq.
Bisq là một nền tảng trao đổi ngang hàng cho phép bạn mua và bán bitcoin. Nó được sử dụng với một phần mềm máy tính để bàn chạy trên Tor và cho phép bạn trao đổi bitcoin mà không cần cung cấp danh tính của mình.
Bisq bảo vệ giao dịch ngang hàng thông qua hệ thống chữ ký đa dạng 2/2. Bạn có thể sử dụng phần mềm này với nút RoninDojo của riêng mình để tối ưu hóa quyền riêng tư của các giao dịch và tin tưởng vào dữ liệu từ blockchain của nút của bạn.

Để tải xuống phần mềm Bisq, hãy truy cập trang web chính thức của họ: https://bisq.network/

Để bắt đầu với phần mềm, tôi khuyên bạn đọc trang này: https://bisq.network/getting-started/

Để lấy liên kết kết nối từ RoninDojo của bạn, bạn cần kết nối với RoninCLI qua SSH. Sau đó, đi đến menu:

> Ứng Dụng > Quản Lý Ứng Dụng

Nhập mật khẩu của bạn, sau đó đánh dấu vào ô bằng phím khoảng trắng:

> [ ] Kích Hoạt Kết Nối Bisq

Xác nhận lựa chọn của bạn. Để nút của bạn cài đặt, sau đó lấy địa chỉ Tor V3 từ:

> Thông Tin Xác Thực > Bitcoind

Sao chép địa chỉ dưới "Bitcoin Daemon".

Bạn cũng có thể lấy địa chỉ Tor V3 Bitcoind của mình từ giao diện RoninUI bằng cách đơn giản nhấp vào "Quản Lý" trong hộp "Bitcoin Core" trên "Bảng Điều Khiển":

![Lấy địa chỉ TorV3 Bitcoin Daemon trên RoninUI](assets/38.webp)

Để kết nối nút của bạn từ Bisq, đi đến menu:

> Cài Đặt > Thông Tin Mạng

![Truy cập giao diện kết nối nút từ phần mềm Bisq](assets/39.webp)

Nhấp vào bong bóng "Sử dụng nút Bitcoin Core tùy chỉnh". Sau đó nhập địa chỉ Bitcoin TorV3 của bạn vào ô được chỉ định, với ".onion" nhưng không có "http://".

![Ô để nhập địa chỉ TorV3 của nút bạn trong phần mềm Bisq](assets/40.webp)

Khởi động lại phần mềm Bisq. Nút của bạn giờ đây đã được kết nối với Bisq của bạn.

### Các tính năng khác.

Nút RoninDojo của bạn cũng bao gồm các tính năng cơ bản khác. Bạn có khả năng quét thông tin cụ thể để đảm bảo rằng nó được tính đến.

Ví dụ, đôi khi có thể ví của bạn kết nối với RoninDojo không tìm thấy bitcoin thuộc về bạn. Số dư là 0 mặc dù bạn chắc chắn rằng bạn có bitcoin trong ví này. Có nhiều nguyên nhân có thể xem xét, bao gồm lỗi trong các đường dẫn phái sinh, và trong số đó, cũng có thể là nút của bạn không quan sát địa chỉ của bạn.

Để khắc phục điều này, bạn có thể kiểm tra xem nút của bạn có đang theo dõi xpub của bạn không với "công cụ xpub". Để truy cập nó từ RoninUI, đi đến menu:

> Bảo Trì > Công Cụ XPUB

Nhập xpub có vấn đề và nhấp "Kiểm Tra" để xác minh thông tin này.

![Công Cụ XPUB từ RoninUI](assets/41.webp)

Nếu xpub của bạn được nút theo dõi, bạn sẽ thấy điều này xuất hiện:

![Kết quả Công Cụ XPUB hiển thị phân tích thành công](assets/42.webp)

Kiểm tra xem tất cả các giao dịch xuất hiện chính xác không. Cũng, xác minh rằng loại phái sinh phù hợp với ví của bạn. Ở đây chúng ta có thể thấy rằng nút giải thích xpub này là một phái sinh BIP44. Nếu loại phái sinh này không phù hợp với ví của bạn, nhấp vào nút "Đánh Máy Lại", sau đó chọn BIP44/BIP49/BIP84 tùy theo lựa chọn của bạn:

![Thay đổi loại phái sinh của xpub được nghiên cứu từ RoninUI](assets/43.webp)

Nếu xpub của bạn không được nút theo dõi, bạn sẽ thấy màn hình này mời bạn nhập nó:
![Nhập một xpub với Công cụ XPUB trên RoninUI](assets/44.webp)
Bạn cũng có thể sử dụng các công cụ bảo trì khác:

- Công cụ Giao Dịch: Cho phép bạn quan sát chi tiết của một giao dịch cụ thể.
- Công cụ Địa Chỉ: Cho phép bạn xác minh rằng một địa chỉ cụ thể đang được theo dõi bởi Dojo của bạn.
- Quét lại các Khối: Buộc node của bạn quét lại một phạm vi các khối đã chọn.

Bạn cũng sẽ tìm thấy công cụ "Push Tx" trên RoninUI. Nó cho phép bạn phát sóng một giao dịch đã ký vào mạng Bitcoin. Nó phải được nhập ở định dạng hexa:

![Công cụ phát sóng một giao dịch đã ký từ RoninUI](assets/45.webp)

## Kết luận.

Chúng ta đã xem cách cài đặt và bắt đầu sử dụng công cụ tuyệt vời này là RoninDojo. Đây là một lựa chọn xuất sắc để chạy node Bitcoin của riêng bạn. Đây là một giải pháp ổn định tích hợp và cập nhật tất cả các công cụ thiết yếu cho một người dùng Bitcoin.

Nếu việc sử dụng terminal không làm bạn sợ hãi và nếu bạn không cần các công cụ liên quan đến Mạng Lôi Điện, thì RoninDojo có thể hấp dẫn bạn.

Nếu bạn có thể, hãy xem xét quyên góp cho các nhà phát triển, những người tự do sản xuất phần mềm mã nguồn mở này cho bạn: https://donate.ronindojo.io/

Để tìm hiểu thêm về RoninDojo, tôi khuyên bạn nên xem các liên kết trong tài nguyên bên ngoài dưới đây của tôi.

### Đọc thêm:

- Hiểu và sử dụng CoinJoin trên Bitcoin.
- Hàm băm - trích từ ebook Bitcoin Démocratisé 1.
- Mọi điều bạn cần biết về Bitcoin Passphrase.

### Tài nguyên bên ngoài:

- https://ronindojo.io/index.html
- https://wiki.ronindojo.io/en/home
- https://gist.github.com/LaurentMT/e758767ca4038ac40aaf
- https://medium.com/@laurentmt/giới thiệu-boltzmann-85930984a159
- https://en.wikipedia.org/wiki/Boltzmann_formula
- https://wiki.ronindojo.io/en/setup/bisq
- https://bisq.network/
