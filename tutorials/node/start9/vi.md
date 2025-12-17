---
name: Start9

description: Hướng dẫn thiết lập máy chủ riêng Start9

---

![cover](assets/cover.webp)


![video](https://www.youtube.com/watch?v=DzikmY4S42Y)


*Đây là video hướng dẫn từ Southern Bitcoiner, video hướng dẫn cho bạn cách thiết lập và sử dụng máy chủ cá nhân Start9 / StartOS và cách chạy một nút bitcoin.*


## 1️⃣ Giới thiệu


### Start9 thực chất là gì?


Start9 là một công ty được thành lập vào năm 2020, nổi tiếng với việc phát triển [**StartOS**,](https://github.com/Start9Labs/start-os), một hệ điều hành dựa trên Linux được thiết kế cho máy chủ cá nhân. Hệ điều hành này cho phép người dùng dễ dàng tự lưu trữ nhiều dịch vụ phần mềm—chẳng hạn như các nút Bitcoin và Lightning, ứng dụng nhắn tin hoặc trình quản lý mật khẩu, đồng thời vẫn duy trì toàn quyền kiểm soát dữ liệu của họ và loại bỏ sự phụ thuộc vào các nền tảng công nghệ tập trung. Start9 có giao diện thân thiện với người dùng, dựa trên trình duyệt, Chợ ứng dụng được quản lý để cài đặt dịch vụ và các công cụ bảo mật tích hợp như tích hợp Tor và mã hóa HTTPS trên toàn hệ thống. Start9 cũng cung cấp các thiết bị phần cứng được cài đặt sẵn hệ điều hành, mặc dù phần mềm có thể được cài đặt trên phần cứng tương thích hoặc máy ảo (VM).


### Có những lựa chọn nào?


Start9 cung cấp cả tùy chọn triển khai được xây dựng sẵn và tự làm. [**Server One**](https://store.start9.com/collections/servers/products/server-one) và [**Server Pure**](https://store.start9.com/collections/servers/products/server-pure) là các thiết bị phần cứng chính thức có các thành phần hiệu suất cao: Server One sử dụng bộ xử lý **AMD Ryzen 7 5825U** với RAM có thể cấu hình (16GB–64GB) và bộ nhớ (SSD NVMe 2TB–4TB), trong khi Server Pure được trang bị **Intel i7-10710U**, cũng cung cấp tùy chọn RAM và bộ nhớ có thể cấu hình. Cả hai đều bao gồm **hỗ trợ kỹ thuật trọn đời** khi mua trực tiếp từ Start9. Đối với người dùng thích sự linh hoạt, StartOS có thể được cài đặt miễn phí trên nhiều loại phần cứng hiện có, bao gồm máy tính xách tay, máy tính để bàn, máy tính mini và máy tính bảng đơn hoặc trong VM.


![image](assets/en/01.webp)


### Sự khác biệt so với Umbrel là gì?


StartOS và Umbrel đều đơn giản hóa việc cài đặt dịch vụ tự lưu trữ nhưng khác nhau về kiến trúc và tính năng. Umbrel hoạt động như một lớp ứng dụng trên các hệ thống Debian/Ubuntu hoặc VM, trong khi Start9 là một hệ điều hành chuyên dụng yêu cầu cài đặt phần cứng hoặc VM trực tiếp. Umbrel có giao diện được trau chuốt, lấy cảm hứng từ macOS, trong khi Start9 ưu tiên thiết kế tối giản, chức năng. Umbrel cung cấp nhiều [lựa chọn ứng dụng](https://apps.umbrel.com/) hơn, trong khi [Start9 Marketplace](https://marketplace.start9.com/) bù lại bằng các khả năng kỹ thuật tiên tiến. Start9 đơn giản hóa việc truy cập vào các cài đặt nâng cao thông qua các biểu mẫu UI đã được xác thực, giảm nhu cầu tương tác dòng lệnh. Nó cũng vượt trội trong việc quản lý sao lưu với các bản sao lưu hệ thống được mã hóa bằng một cú nhấp chuột, một tính năng mà Umbrel không có sẵn. StartOS cung cấp các công cụ giám sát tích hợp và thực thi mã hóa HTTPS để truy cập mạng cục bộ, tăng cường bảo mật. Umbrel sử dụng HTTP không được mã hóa cục bộ, mặc dù cả hai nền tảng đều hỗ trợ truy cập từ xa an toàn qua Tor. Umbrel phù hợp với người dùng ưu tiên hệ sinh thái ứng dụng phong phú và giao diện người dùng được trau chuốt. Start9 là lựa chọn hàng đầu cho những ai coi trọng bảo mật, khả năng cấu hình, độ tin cậy sao lưu và quản lý dịch vụ nâng cao mà không cần chuyên môn về dòng lệnh. Để tìm hiểu thêm về Umbrel và những điểm khác biệt so với Start9, vui lòng truy cập khóa học này:


https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

## 2️⃣ Điều kiện tiên quyết khi tự làm: Thông số kỹ thuật tối thiểu và khuyến nghị


Đối với mục đích sử dụng cơ bản với các dịch vụ tối thiểu, thông số kỹ thuật tối thiểu ** là: ** 1 lõi vCPU (tăng tốc 2,0 GHz trở lên), RAM 4 GB, bộ nhớ 64 GB** và một cổng Ethernet. Tuy nhiên, tôi khuyên bạn nên nâng cấp lên dung lượng cao hơn, đặc biệt nếu bạn đang chạy Bitcoin Node. Cá nhân tôi đã bắt đầu với 1 TB và nhanh chóng hết dung lượng. Tốt hơn nên nhắm đến **bộ nhớ ít nhất 2 TB**, cùng với **CPU lõi tứ (2,5 GHz trở lên)** và **RAM 8 GB trở lên**. Điều này tạo ra sự khác biệt lớn về hiệu suất và tuổi thọ. Nếu bạn muốn tìm hiểu sâu hơn, đây là chủ đề cộng đồng mới nhất về [Phần cứng có khả năng chạy StartOS](https://community.start9.com/t/known-good-hardware-master-list-hardware-capable-of-running-startos/66/229).


## 3️⃣ Tải xuống và cài đặt chương trình cơ sở


Để bắt đầu thiết lập, hãy sử dụng một máy tính riêng để truy cập trang web Start9 (https://start9.com/) và điều hướng đến phần tài liệu bằng cách nhấp vào `DOCS`. Từ đó, hãy truy cập `Flashing Guides` để tìm phiên bản StartOS phù hợp. Có hai tùy chọn:



- StartOS (Raspberry Pi)
- StartOS (X86/ARM)


Hướng dẫn này đề cập đến tùy chọn `x86/ARM`.


Phiên bản hệ điều hành mới nhất có thể được tải xuống từ [trang phát hành GitHub](https://github.com/Start9Labs/start-os/releases/latest). Phiên bản [tiền phát hành](https://github.com/Start9Labs/start-os/releases) cũng có sẵn cho người dùng muốn thử nghiệm các tính năng mới. Ở cuối trang, trong mục `Tài sản`, hãy tải xuống `x86_64` hoặc `x86_64-nonfree.iso`. Hình ảnh `x86_64-nonfree.iso` chứa phần mềm không miễn phí (mã nguồn đóng) cần thiết cho Server One và hầu hết phần cứng tự làm, đặc biệt là hỗ trợ đồ họa và thiết bị mạng.


Khuyến nghị nên xác minh tính toàn vẹn của tệp bằng cách so sánh mã băm SHA256 của tệp với mã băm được liệt kê trên GitHub. Đối với Linux, có thể sử dụng lệnh `sha256sum startos-0.3.4.2-efc56c0-20230525_x86_64.iso`, với các hệ điều hành khác được đề cập trong tài liệu.


Sau khi tải xuống và xác minh ảnh StartOS, bạn phải flash nó vào ổ USB. `BalenaEtcher` là phần mềm được khuyến nghị cho tác vụ này. Đây là công cụ mã nguồn mở miễn phí để ghi tệp ảnh hệ điều hành vào ổ USB và thẻ SD, có sẵn cho Windows, macOS và Linux. Tải xuống phiên bản phù hợp từ [trang web chính thức của Balena Etcher](https://www.balena.io/etcher/) và chạy trình cài đặt. Kết nối ổ USB hoặc thẻ SD đích, mở Balena Etcher và nhấp vào `Flash from file` để chọn ảnh hệ điều hành đã tải xuống. Etcher sẽ tự động phát hiện các ổ đĩa được kết nối; chọn ổ đĩa đích chính xác nếu có nhiều ổ đĩa. Nhấp vào `Flash!` để bắt đầu ghi ảnh. Etcher tự động xác thực quy trình ghi khi hoàn tất. Sau khi hoàn tất, hãy tháo ổ đĩa một cách an toàn và sử dụng nó để khởi động thiết bị.


![image](assets/en/19.webp)


## 4️⃣ Thiết lập ban đầu


Để thiết lập ban đầu, hãy tham khảo trang [tài liệu] (https://docs.start9.com/0.3.5.x/) của Start9 trong mục `SỔ TAY NGƯỜI DÙNG`, sau đó là `Bắt đầu - Thiết lập Ban đầu`. Bạn nên tham khảo hướng dẫn chính thức này để biết thông tin mới nhất.


Có hai lựa chọn được đưa ra:



- Bắt đầu mới
- Tùy chọn phục hồi


Để cài đặt máy chủ mới, hãy chọn `Start Fresh`. Trước tiên, hãy kết nối máy chủ với nguồn điện và cáp Ethernet. Đảm bảo máy tính được sử dụng để thiết lập nằm trong cùng một mạng cục bộ. Tháo ổ USB vừa flash ra khỏi máy tính và cắm vào máy chủ.


Bạn có thể điều khiển máy chủ từ xa từ bất kỳ máy tính nào trong cùng mạng. Mở trình duyệt web và truy cập `http://start.local`.


**Lưu ý**: Nếu xảy ra sự cố kết nối với địa chỉ này, thường là do mạng gia đình không phân giải được tên miền `.local`. Sự cố có thể được giải quyết bằng cách truy cập trực tiếp vào máy chủ thông qua địa chỉ IP của nó. Có thể tìm thấy IP bằng cách đăng nhập vào giao diện quản trị của bộ định tuyến (thường là `192.168.1.1` hoặc một địa chỉ tương tự) và định vị thiết bị trong danh sách máy khách DHCP hoặc bản đồ mạng. Sau đó, nhập địa chỉ IP đầy đủ (ví dụ: `http://192.168.1.105`) vào trình duyệt. Thao tác này sẽ bỏ qua việc phân giải DNS. Nếu sự cố vẫn tiếp diễn, hãy tham khảo [trang Sự cố Thường gặp](https://docs.start9.com/0.3.5.x/support/common-issues.html#setup-troubleshoot) hoặc [liên hệ với bộ phận hỗ trợ của họ.](https://start9.com/contact/)


Màn hình thiết lập StartOS sẽ xuất hiện. Nhấp vào `Start Fresh` để bắt đầu thiết lập máy chủ mới.


![image](assets/en/03.webp)


Bước tiếp theo là chọn ổ đĩa lưu trữ nơi dữ liệu StartOS sẽ được lưu trữ.


![image](assets/en/04.webp)


Đặt `Mật khẩu` mạnh cho máy chủ. Ghi lại mật khẩu theo hướng dẫn của Start9, sau đó nhấp vào `KẾT THÚC`.


![image](assets/en/05.webp)


Màn hình sẽ hiển thị StartOS đang khởi tạo và thiết lập máy chủ. Bước tiếp theo là `Tải xuống thông tin địa chỉ` vì địa chỉ `start.local` chỉ dành cho mục đích thiết lập và sẽ không hoạt động sau đó.


![image](assets/en/06.webp)


Tệp cấu hình chứa hai địa chỉ truy cập quan trọng: một cho `mạng cục bộ (LAN)` và một cho truy cập an toàn qua `Tor`. Cả hai địa chỉ này phải được lưu trong trình quản lý mật khẩu an toàn. Bước tiếp theo là `Tin cậy Root CA`. Mở một tab trình duyệt mới và làm theo hướng dẫn để tin cậy Root CA và đăng nhập. Bạn cũng có thể tải xuống chứng chỉ Root CA bằng cách nhấp vào `Tải xuống chứng chỉ` trong tệp đã tải xuống.


## 5️⃣ Tin tưởng Root CA của bạn


Sau khi tải xuống chứng chỉ, `Root CA` của máy chủ phải được hệ điều hành tin cậy. Nhấp vào `Xem Hướng dẫn` và tìm hướng dẫn cho hệ điều hành cụ thể.


![image](assets/en/07.webp)


Đối với hệ thống Linux, các lệnh sau được sử dụng. Trước tiên, hãy mở Terminal và cài đặt các gói cần thiết:


```shell
sudo apt update

sudo apt install -y ca-certificates p11-kit
```


Điều hướng đến thư mục nơi chứng chỉ đã được tải xuống, thường là `~/Downloads`. Thực hiện các lệnh này để thêm chứng chỉ vào kho lưu trữ tin cậy của hệ điều hành. Thay đổi thư mục tải xuống bằng `cd ~/Downloads`. Tạo thư mục cần thiết bằng `sudo mkdir -p /usr/share/ca-certificates/start9`. Sao chép tệp chứng chỉ, thay thế ``your-filename.crt` bằng tên tệp thực tế, sử dụng `sudo cp "your-filename.crt" /usr/share/ca-certificates/start9/`. Đăng ký chứng chỉ vĩnh viễn bằng cách thêm đường dẫn của nó vào cấu hình hệ thống bằng `sudo bash -c "echo 'start9/your-filename.crt' >> /etc/ca-certificates.conf"`. Cuối cùng, xây dựng lại kho lưu trữ tin cậy bằng `sudo update-ca-certificates`. Điều quan trọng là phải sử dụng tên tệp chứng chỉ thực tế và xác minh tất cả các đường dẫn trước khi thực hiện các lệnh này. Quá trình này thiết lập sự tin cậy lâu dài cho các kết nối HTTPS của máy chủ Start9.


Cài đặt thành công sẽ được thông báo bằng thông báo `1 added`. Hầu hết các ứng dụng sau đó sẽ có thể kết nối an toàn qua `https`. Nếu sử dụng Firefox, cần thêm [bước cuối cùng](https://docs.start9.com/0.3.5.x/misc-guides/ca-ff.html#ca-ff). Đối với Chrome hoặc Brave, cần thêm [bước cuối cùng](https://docs.start9.com/0.3.5.x/misc-guides/ca-chrome.html#ca-chrome) để cấu hình trình duyệt sao cho tuân thủ Root CA. Kiểm tra kết nối bằng cách làm mới trang. Nếu sự cố vẫn tiếp diễn, hãy thoát và mở lại trình duyệt trước khi truy cập lại trang.


![image](assets/en/08.webp)


## 6️⃣ Bắt đầu với StartOS


Bây giờ bạn có thể đăng nhập bằng kết nối HTTPS an toàn. Nhập `Mật khẩu` để truy cập `Màn hình Chào mừng`.


![image](assets/en/09.webp)


Màn hình này cung cấp các phím tắt hữu ích để bắt đầu. Thanh bên trái chứa các mục menu chính để điều hướng.


## Hệ thống 7️⃣


Tab Hệ thống trong StartOS cung cấp quyền truy cập vào các chức năng hệ thống cốt lõi để quản lý máy chủ cá nhân. Tab này cung cấp các công cụ bảo trì, bảo mật, chẩn đoán và cấu hình hệ thống mà không yêu cầu chuyên môn về dòng lệnh.


Phần `Sao lưu` cho phép tạo bản sao lưu toàn bộ hệ thống, bao gồm các dịch vụ, cấu hình và dữ liệu, có thể được khôi phục sau này. Điều này rất cần thiết cho việc khôi phục sau thảm họa hoặc di chuyển sang phần cứng mới. Bản sao lưu có thể được lưu trữ trên ổ đĩa ngoài và được mã hóa bằng mật khẩu chính.


Phần `Quản lý` trong tab Hệ thống cho phép kiểm soát các chức năng chính của hệ thống. Người dùng có thể tự kiểm tra và áp dụng các bản cập nhật StartOS, đồng thời duy trì quyền kiểm soát quy trình cập nhật hệ thống. Có thể tải các dịch vụ tùy chỉnh hoặc của bên thứ ba không có sẵn trên chợ ứng dụng chính thức. Nếu máy chủ không được kết nối qua Ethernet, bạn có thể cấu hình cài đặt Wi-Fi từ phần này. Người dùng nâng cao có thể bật quyền truy cập SSH để quản lý hệ thống ở cấp độ thiết bị đầu cuối.


![image](assets/en/10.webp)


Phần `Insights` cung cấp khả năng giám sát hiệu suất và tình trạng hoạt động của máy chủ theo thời gian thực, hiển thị mức sử dụng CPU, RAM và ổ đĩa thông qua biểu đồ. Phần này cũng hiển thị nhiệt độ hệ thống, rất hữu ích cho các thiết bị như Raspberry Pi không có hệ thống làm mát chủ động. Các số liệu về thời gian hoạt động và tải trung bình giúp đánh giá độ ổn định của hệ thống, và nhật ký trực tiếp có sẵn để khắc phục sự cố dịch vụ hoặc hệ thống.


Phần `Hỗ trợ` cung cấp quyền truy cập vào các Câu hỏi thường gặp tích hợp, tài liệu chính thức và các kênh hỗ trợ cộng đồng. Bạn có thể tải xuống nhật ký gỡ lỗi từ phần này để chia sẻ với bộ phận hỗ trợ của Start9 nhằm giải quyết sự cố nhanh hơn.


![image](assets/en/11.webp)


## 8️⃣ Chợ


`Marketplace` được sử dụng để khám phá, cài đặt và quản lý các dịch vụ trên máy chủ cá nhân. Nó cung cấp quyền truy cập vào các phần mềm như Bitcoin Core, BTCPay Server và electrs. StartOS hỗ trợ nhiều thị trường, bao gồm cả Start9 Registry chính thức và các sổ đăng ký do cộng đồng quản lý. Bạn có thể thêm các thị trường này bằng cách nhấp vào `CHANGE` và chuyển sang `Community Registry`, nơi cung cấp quyền truy cập vào nhiều dịch vụ hơn.


![image](assets/en/12.webp)


## 9️⃣ Cài đặt Full Node Bitcoin


Việc cài đặt Bitcoin full node trên StartOS mang lại quyền tự chủ hoàn toàn đối với trải nghiệm Bitcoin. Nó cho phép xác thực giao dịch và tăng cường quyền riêng tư và bảo mật bằng cách loại bỏ sự phụ thuộc vào các dịch vụ bên ngoài có thể ghi lại hoạt động. Quyền kiểm soát hoàn toàn các giao dịch được đảm bảo, cho phép chúng được phát trực tiếp lên mạng. Tùy chọn mặc định là `Bitcoin Core`, tích hợp sẵn với StartOS và cho phép kết nối với các ví như Spectre, Sparrow hoặc Electrum để thiết lập tự lưu trữ. Một lựa chọn thay thế, `Bitcoin Knots`, cũng có sẵn thông qua Sổ đăng ký Cộng đồng.


Để cài đặt Bitcoin Core, hãy điều hướng đến Marketplace. Trong sổ đăng ký mặc định, hãy tìm và cài đặt dịch vụ Bitcoin Core. Sau khi cài đặt, lời nhắc `Needs Config` sẽ xuất hiện, yêu cầu hoàn tất cài đặt trước khi dịch vụ có thể chạy. Điều này thường xảy ra sau khi cập nhật hoặc cài đặt mới và nhắc xem lại `RPC settings`. Tiếp tục với cấu hình mặc định và nhấp vào `Save`.


![image](assets/en/13.webp)


Sau khi được đồng bộ hóa hoàn toàn, nút của bạn có thể hoạt động như một backend riêng tư cho các ví như Sparrow, mang lại quyền riêng tư và xác thực giao dịch được cải thiện. Tuy nhiên, đối với người dùng lưu trữ số lượng lớn, việc hiểu rõ những đánh đổi về bảo mật của kết nối trực tiếp này là rất quan trọng. Khi wallet kết nối trực tiếp với Bitcoin Core, dữ liệu nhạy cảm có thể bị lộ, vì Bitcoin Core lưu trữ khóa công khai (xpub) và số dư wallet không được mã hóa trên máy chủ. Một hệ thống bị xâm phạm có thể cho phép kẻ tấn công phát hiện ra tài sản của bạn và nhắm mục tiêu vào bạn.


Để giảm thiểu rủi ro này và đạt được mô hình bảo mật mạnh mẽ hơn, bạn có thể thiết lập Electrum Server Riêng tư. Máy chủ này hoạt động như một trung gian, lập chỉ mục blockchain mà không lưu trữ bất kỳ thông tin cụ thể nào của wallet. Bằng cách kết nối wallet với máy chủ Electrum của riêng bạn thay vì kết nối trực tiếp với Bitcoin Core, bạn sẽ ngăn wallet truy cập dữ liệu nhạy cảm của nút.


![image](assets/en/14.webp)


## 🔟 Thiết lập electrs


`electrs` (Máy chủ Electrum Rust) là một trình lập chỉ mục nhanh chóng và hiệu quả, kết nối với nút Bitcoin Core của bạn và cho phép các ví tương thích với Electrum truy vấn lịch sử giao dịch và số dư theo thời gian thực. Bằng cách chạy electrs trên StartOS, bạn loại bỏ sự phụ thuộc vào máy chủ Electrum của bên thứ ba, cải thiện đáng kể quyền riêng tư và bảo mật — các truy vấn wallet của bạn sẽ được chuyển trực tiếp đến nút tự lưu trữ của bạn.


Để thiết lập, trước tiên hãy cài đặt dịch vụ electrs từ StartOS Marketplace. Hệ thống sẽ yêu cầu Bitcoin Core được đồng bộ hóa hoàn toàn trước khi tiếp tục. Sau khi cài đặt, hãy xác nhận cài đặt `Needs Config` với các thiết lập mặc định được đề xuất và electrs sẽ bắt đầu lập chỉ mục blockchain, quá trình này có thể mất đến một ngày tùy thuộc vào phần cứng của bạn.


![image](assets/en/15.webp)


Sau khi hoàn tất, bạn có thể kết nối các ví như Sparrow hoặc Spectre. Kết nối thành công cho phép wallet đồng bộ trực tiếp với nút của bạn, mang lại trải nghiệm Bitcoin an toàn, riêng tư và tự lưu trữ.


## 1️⃣1️⃣ Kết nối Sparrow Wallet


Để kết nối `Sparrow Wallet` với nút StartOS của bạn bằng cách sử dụng triển khai electrs, trước tiên hãy đảm bảo Bitcoin Core được đồng bộ hóa hoàn toàn và electrs đã được cài đặt và đang chạy. Mở Sparrow Wallet trên thiết bị của bạn và điều hướng đến `File` -> `Settings` -> `Server`. Sau đó chọn `Private Electrum Server`. Trong trường URL, hãy nhập `Tor hostname` và `Port` cho electrs, bạn có thể tìm thấy chúng trong StartOS tại `Services` -> `electrs` -> `Properties` (thường có đuôi là `.onion:50001`).


![image](assets/en/16.webp)


Tiếp theo, bật Tor bằng cách chọn `Use Proxy`, đặt địa chỉ proxy thành `127.0.0.1` và cổng thành `9050`. Nhấp vào `Test Connection` và chờ vài phút. Kết nối thành công sẽ hiển thị thông báo xác nhận, chẳng hạn như ``Connected to electrs`. Sau khi xác minh, hãy đóng cài đặt và tiến hành tạo hoặc khôi phục wallet của bạn. Thiết lập này đảm bảo wallet của bạn truy vấn node của riêng bạn thông qua electrs, mang lại quyền riêng tư hoàn toàn và hoạt động không cần tin cậy.


![image](assets/en/17.webp)


## 🎯 Kết luận


StartOS của Start9 là một nền tảng thân thiện với người dùng, tập trung vào quyền riêng tư, được thiết kế để tự lưu trữ các dịch vụ thiết yếu như nút Bitcoin và Lightning, ví điện tử và ứng dụng cá nhân. StartOS loại bỏ nhu cầu về kỹ năng dòng lệnh bằng cách cung cấp giao diện đồ họa rõ ràng, sao lưu tự động, giám sát tình trạng và truy cập Tor an toàn, lý tưởng cho người dùng không chuyên. Kiến trúc mô-đun của nó hỗ trợ tích hợp liền mạch với các công cụ như electrs hoặc Sparrow, mang đến cho bạn toàn quyền kiểm soát chủ quyền tài chính và kỹ thuật số của mình. Với trọng tâm mạnh mẽ vào tính minh bạch, kiểm soát cục bộ và khả năng mở rộng, StartOS trao quyền cho người dùng giành lại quyền sở hữu từ các nền tảng tập trung và vận hành cơ sở hạ tầng riêng tư, linh hoạt của riêng họ.