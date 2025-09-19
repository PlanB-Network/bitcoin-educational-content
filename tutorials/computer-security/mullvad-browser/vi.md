---
name: Mullvad Browser
description: Cách sử dụng Trình duyệt Mullvad để bảo vệ quyền riêng tư
---

![cover](assets/cover.webp)



Trong một thế giới mà việc giám sát kỹ thuật số đang trở nên phổ biến, việc bảo vệ quyền riêng tư trực tuyến của bạn chưa bao giờ quan trọng hơn lúc này. Các công ty sử dụng các kỹ thuật tinh vi để theo dõi bạn:





- **Cookie của bên thứ ba**: các tệp nhỏ được các trang web bên ngoài gửi đến để theo dõi bạn từ trang web này sang trang web khác
- **Lấy dấu vân tay**: thu thập các đặc điểm riêng biệt của trình duyệt và thiết bị của bạn (độ phân giải màn hình, phông chữ đã cài đặt, plugin, v.v.) để nhận dạng bạn mà không cần cookie
- **Theo dõi tập lệnh**: mã JavaScript vô hình phân tích hành vi duyệt web của bạn (nhấp chuột, cuộn, thời gian sử dụng)
- **Phân tích IP Address**: vị trí địa lý và nhận dạng nhà cung cấp dịch vụ Internet của bạn



Dữ liệu này sau đó được kết hợp để tạo ra hồ sơ chi tiết về hành vi trực tuyến của bạn và được kiếm tiền, thường là ngoài sự hiểu biết của bạn. Thực tế này đặt ra một câu hỏi cơ bản: làm thế nào bạn có thể lướt Internet mà vẫn giữ được tính ẩn danh và bảo mật?



Câu trả lời phần lớn nằm ở lựa chọn trình duyệt web của bạn. Công cụ này, mà chúng ta sử dụng hàng ngày để truy cập thông tin, mua sắm hoặc giao tiếp, đóng vai trò quyết định trong việc bảo vệ dữ liệu cá nhân của chúng ta. Thật không may, các trình duyệt phổ biến như Google Chrome (chiếm khoảng 65% thị phần toàn cầu) được thiết kế dựa trên các mô hình kinh doanh dựa trên lượng dữ liệu người dùng khổng lồ.



![MULLVAD BROWSER](assets/fr/01.webp)


*Trình duyệt Mullvad nổi bật với khả năng chặn theo dõi cực kỳ hiệu quả, vượt xa các trình duyệt dành cho người dùng*



Đối mặt với thách thức này, nhiều đối thủ mới đang nổi lên với một triết lý khác: đặt quyền riêng tư làm trọng tâm trong thiết kế. Trong số đó, Mullvad Browser nổi bật là một giải pháp sáng tạo kết hợp các biện pháp bảo vệ quyền riêng tư tốt nhất với trải nghiệm duyệt web mượt mà, dễ tiếp cận.



Không giống như các trình duyệt truyền thống tìm cách cá nhân hóa trải nghiệm của bạn bằng cách thu thập dữ liệu, Mullvad Browser lại có cách tiếp cận ngược lại: làm cho tất cả người dùng trông giống hệt với các trang web, do đó việc theo dõi cá nhân hóa hầu như không thể thực hiện được.



Trong hướng dẫn này, chúng ta sẽ cùng nhau khám phá cách Mullvad Browser có thể thay đổi cách bạn duyệt Internet, cung cấp cho bạn khả năng bảo vệ mạnh mẽ chống lại sự giám sát mà không ảnh hưởng đến tính dễ sử dụng.




## Giới thiệu trình duyệt Mullvad



**Trình duyệt Mullvad** là một trình duyệt web tập trung vào quyền riêng tư, được phát triển với sự hợp tác của Dự án Tor và được phân phối miễn phí bởi công ty Mullvad VPN của Thụy Điển. Ra mắt vào tháng 4 năm 2023, Mullvad tự giới thiệu mình là một **"Trình duyệt Tor không cần mạng Tor"**, được thiết kế để giảm thiểu việc theo dõi và lấy dấu vân tay trực tuyến, đồng thời cho phép người dùng duyệt web thông qua VPN đáng tin cậy thay vì mạng Tor.



Trình duyệt Mullvad là trình duyệt mã nguồn mở miễn phí dựa trên Firefox ESR (phiên bản lâu dài của Mozilla Firefox) và được các chuyên gia của Dự án Tor củng cố. Cụ thể, trình duyệt này bao gồm hầu hết các **tính năng bảo vệ của Trình duyệt Tor**, nhưng **không định tuyến lưu lượng truy cập qua mạng Tor**. Thay vào đó, người dùng có thể (và nên) liên kết trình duyệt này với một VPN được mã hóa đáng tin cậy để ẩn danh IP Address của họ.



Về trải nghiệm người dùng, Mullvad Browser giống như một trình duyệt cổ điển, cung cấp khả năng điều hướng mượt mà. Trình duyệt này miễn phí trên Windows, macOS và Linux (không có phiên bản di động). Bạn không cần phải đăng ký Mullvad VPN để sử dụng; tuy nhiên, **sử dụng Mullvad Browser mà không ẩn IP không đảm bảo ẩn danh hoàn toàn** - vì vậy chúng tôi khuyến nghị bạn nên sử dụng kết hợp với một VPN đáng tin cậy.



### Mục tiêu: quyền riêng tư và chống theo dõi



Trình duyệt Mullvad được thiết kế với một mục tiêu chính: **bảo vệ quyền riêng tư của người dùng** trực tuyến và chống lại các kỹ thuật theo dõi và lập hồ sơ phổ biến. Các mục tiêu chính của trình duyệt bao gồm:





- Giảm đáng kể việc theo dõi quảng cáo và **theo dõi** bởi các trang web và công ty quảng cáo. Theo mặc định, Mullvad Browser chặn các trình theo dõi của bên thứ ba, cookie theo dõi và tập lệnh dấu vân tay có thể nhận dạng bạn.





- Chuẩn hóa dấu vân tay của trình duyệt để **"hòa nhập với đám đông"**. Dấu vân tay giống như một "thẻ căn cước" độc nhất được tạo ra bằng cách kết hợp tất cả các đặc điểm của trình duyệt. Trình duyệt Mullvad đảm bảo rằng tất cả người dùng đều có cùng một "thẻ căn cước", khiến việc phân biệt từng người dùng trở nên bất khả thi.





- Cung cấp khả năng bảo vệ tức thì mà không cần tiện ích mở rộng bổ sung. Trình duyệt Mullvad có cấu hình "sẵn sàng sử dụng": người dùng không cần cài đặt nhiều tiện ích mở rộng hoặc sửa đổi bất kỳ cài đặt nào để được bảo vệ.





- Đừng hy sinh hiệu suất hoặc tính công thái học nhiều hơn mức cần thiết. Khi không có định tuyến Tor, Trình duyệt Mullvad mang lại tốc độ duyệt web nhanh hơn nhiều so với Trình duyệt Tor, gần bằng hiệu suất của một trình duyệt tiêu chuẩn kết hợp với VPN.



### Các tính năng chính của trình duyệt Mullvad



Trình duyệt Mullvad bao gồm một loạt các tính năng **bảo mật và quyền riêng tư** được lấy cảm hứng trực tiếp từ Trình duyệt Tor:





- **Duyệt web riêng tư mọi lúc:** Chế độ duyệt web riêng tư được kích hoạt theo mặc định và không thể tắt. **Không có lịch sử, cookie hoặc bộ nhớ đệm nào được lưu trữ từ phiên này sang phiên khác**. Ngay khi bạn đóng Trình duyệt Mullvad, mọi dữ liệu duyệt web sẽ bị xóa.





- **Tăng cường bảo vệ chống lại dấu vân tay:** Trình duyệt áp dụng các thiết lập nghiêm ngặt để ngăn chặn dấu vân tay kỹ thuật số. Điều này bao gồm:
- **Chuẩn hóa phiên bản trình duyệt và tác nhân người dùng**
- Múi giờ được đặt thành **UTC** cho tất cả người dùng
- **Letterboxing**: một kỹ thuật tự động thêm lề xám xung quanh các trang web để chuẩn hóa kích thước hiển thị và ngăn chặn việc nhận dạng theo kích thước màn hình của bạn
- Chặn API lấy dấu vân tay: Các công nghệ Canvas (bản vẽ 2D), WebGL (đồ họa 3D) và AudioContext (xử lý âm thanh) bị vô hiệu hóa vì chúng có thể tiết lộ các chi tiết duy nhất về phần cứng của bạn
- Phông chữ hệ thống được **chuẩn hóa** để tránh bị nhận dạng bởi phông chữ đã cài đặt





- **Chặn trình theo dõi và quảng cáo:** Trình duyệt Mullvad tích hợp sẵn tiện ích mở rộng **uBlock Origin** (được cài đặt sẵn) với các danh sách bảo vệ bổ sung để chặn **trình theo dõi của bên thứ ba, tập lệnh quảng cáo và nội dung độc hại khác**. Tính năng bảo vệ này đi kèm với **First-Party Isolation**: một kỹ thuật lưu trữ cookie trong các "kho" riêng biệt cho mỗi trang web, ngăn không cho một trang web đọc cookie do trang web khác gửi.





- Nút đặt lại phiên: Giống như nút "Danh tính mới" của Tor Browser, Mullvad Browser cung cấp một nút để **khởi động lại trình duyệt một cách nhanh chóng với phiên mới, trống**.





- **Mức độ bảo mật có thể điều chỉnh:** Bạn có thể điều chỉnh mức độ bảo mật (*Bình thường*, *An toàn hơn*, *An toàn nhất*) trong phần cài đặt, giống như trong Tor Browser.



## Tiện ích mở rộng tích hợp theo mặc định



Trình duyệt Mullvad bao gồm **ba tiện ích mở rộng được cài đặt sẵn**, tạo thành cốt lõi của tính năng bảo vệ chống theo dõi. **Điều quan trọng là không bao giờ xóa hoặc sửa đổi cấu hình của chúng**, vì điều này sẽ khiến bạn trở nên khác biệt so với những người dùng khác của Trình duyệt Mullvad:



### **Nguồn gốc uBlock**


Tiện ích mở rộng chặn quảng cáo và trình theo dõi này được cấu hình sẵn với **danh sách bộ lọc được tối ưu hóa** để chặn:




- Quảng cáo xâm phạm
- Trình theo dõi của bên thứ ba thu thập dữ liệu của bạn
- Các tập lệnh độc hại
- Theo dõi hành vi Elements



uBlock Origin trong Mullvad Browser sử dụng các tham số chuẩn hóa để đảm bảo rằng tất cả người dùng đều chặn chính xác cùng một Elements, do đó bảo toàn tính đồng nhất của dấu vết kỹ thuật số.



### **Không có kịch bản**


NoScript chạy ở chế độ nền để quản lý **mức độ bảo mật** của trình duyệt. Điều này:




- Kiểm soát việc thực thi **JavaScript** theo mức độ đã chọn (Bình thường/Bảo mật nhất/Bảo mật nhất)
- Tự động lọc các cuộc tấn công **XSS** (Cross-Site Scripting)
- Chặn nội dung **hoạt động nguy hiểm** trên các trang web không phải HTTPS
- Biểu tượng của nó bị ẩn theo mặc định, nhưng có thể hiển thị thông qua "Tùy chỉnh thanh công cụ"



### **Tiện ích mở rộng của Trình duyệt Mullvad**


Tiện ích mở rộng dành riêng cho Mullvad này cung cấp các chức năng khác nhau tùy thuộc vào việc bạn có phải là khách hàng của Mullvad VPN hay không:



#### **Không cần đăng ký Mullvad VPN:**




- **Kiểm tra kết nối cơ bản**: hiển thị IP công khai hiện tại của bạn và một số thông tin kết nối
- **Khuyến nghị về quyền riêng tư**: mẹo để cải thiện cài đặt bảo mật của bạn (DNS, chỉ HTTPS, công cụ tìm kiếm)
- **Kiểm soát WebRTC**: bật/tắt để ngăn chặn rò rỉ IP Address
- Có thể xóa mà không ảnh hưởng đến dấu vết kỹ thuật số của bạn nếu bạn không sử dụng Mullvad VPN



#### **Với đăng ký Mullvad VPN:**


Tiện ích mở rộng này sẽ bộc lộ hết tiềm năng của nó với các tính năng nâng cao:





- **Proxy SOCKS5 tích hợp**: kết nối một cú nhấp chuột tới proxy máy chủ Mullvad VPN
- Địa chỉ IP cố định **Address**: không giống như VPN, có thể thay đổi địa chỉ IP Address, proxy luôn đảm bảo đầu ra Address giống nhau
- **Công tắc ngắt tự động**: nếu VPN bị ngắt kết nối, lưu lượng truy cập trình duyệt sẽ bị chặn ngay lập tức
- **Hỗ trợ IPv6**: Kết nối IPv6 ngay cả khi kết nối VPN của bạn không bật tính năng này





- **Multihop (VPN kép)**: khả năng thay đổi vị trí proxy để tạo đường hầm bên trong đường hầm
 - Lưu lượng truy cập của bạn trước tiên phải đi qua máy chủ VPN của bạn, sau đó "nhảy" đến một máy chủ Mullvad khác
 - Chỉ sử dụng bản địa hóa khác nhau cho trình duyệt





- **Giám sát kết nối nâng cao**: giám sát trạng thái VPN, máy chủ được kết nối và phát hiện rò rỉ DNS theo thời gian thực





- Truy cập vào **Mullvad Leta**: công cụ tìm kiếm riêng tư dành riêng cho người đăng ký (mặc dù Mullvad không khuyến nghị vì lý do liên quan đến tài khoản của bạn)



Ba tiện ích mở rộng này hoạt động cùng nhau để tạo ra một hệ sinh thái bảo vệ thống nhất, trong đó mọi người dùng đều được hưởng lợi từ cùng một biện pháp phòng thủ mà không cần phải tùy chỉnh vì có thể gây ảnh hưởng đến tính ẩn danh tập thể.



## Ưu điểm và nhược điểm của trình duyệt Mullvad



### Những lợi ích





- **Bảo vệ quyền riêng tư tuyệt vời theo mặc định:** Trình duyệt Mullvad áp dụng các cài đặt quyền riêng tư rất nghiêm ngặt ngay từ đầu, không cần cấu hình thủ công.





- Hiệu suất tốt hơn Tor Browser: Do không có onion routing, Mullvad Browser **nhanh hơn đáng kể và phản hồi nhanh hơn** so với Tor Browser khi duyệt web thông thường.





- **Sự đơn giản quen thuộc của Interface:** Trình duyệt Mullvad dựa trên Interface của Firefox. Nếu bạn đã quen với Firefox hoặc thậm chí là Tor Browser, bạn sẽ không cảm thấy lạc lõng.





- **Sự hợp tác đáng tin cậy và mã được kiểm tra:** Trình duyệt Mullvad được hưởng lợi từ chuyên môn của Dự án Tor và toàn bộ mã nguồn đều có thể được kiểm tra bên ngoài.



### Nhược điểm





- Không thể ẩn danh mạng nếu không có VPN: Điểm quan trọng nhất là **Trình duyệt Mullvad không tự ẩn IP Address của bạn** (giống như tất cả các trình duyệt khác, ngoại trừ Trình duyệt Tor). IP Address của bạn giống như "Address bưu điện" trên Internet: nó tiết lộ vị trí và nhà cung cấp dịch vụ Internet (ISP) của bạn. Do đó, nó **phụ thuộc rất nhiều vào VPN** (mạng riêng ảo) để ẩn thông tin quan trọng này.





- **Không có phiên bản di động:** Cho đến nay, Mullvad Browser chỉ khả dụng trên PC (Windows, Mac, Linux).





- Không tương thích với một số thói quen nhất định: **Chế độ riêng tư vĩnh viễn** nghĩa là bạn không thể duy trì một phiên sử dụng từ lần sử dụng này sang lần sử dụng khác. Không thể duy trì kết nối với một tài khoản web từ phiên này sang phiên khác.





- **Tính năng bị hạn chế:** Để duy trì tính đồng nhất của dấu vân tay, Trình duyệt Mullvad đã **vô hiệu hóa một số tính năng** có trong Firefox và không dành cho mục đích tùy chỉnh.



## Cài đặt trình duyệt Mullvad



Trình duyệt Mullvad có sẵn miễn phí cho Windows, macOS và Linux. Để cài đặt, hãy truy cập [trang web chính thức của Mullvad](https://mullvad.net/browser).



![MULLVAD BROWSER](assets/fr/02.webp)



*Trang chủ chính thức của Trình duyệt Mullvad với nút tải xuống được tô sáng.*



![MULLVAD BROWSER](assets/fr/03.webp)



*Chọn hệ điều hành của bạn trên Trình duyệt Mullvad.* trang tải xuống



Nhấp vào nút **"Tải xuống"** tương ứng với hệ điều hành của bạn.



Đối với Linux, bạn có thể chọn giữa các định dạng khác nhau tùy thuộc vào bản phân phối của mình. Sau khi tải xuống hoàn tất:



### Trên Windows


Chạy tệp `.exe` đã tải xuống và làm theo hướng dẫn cài đặt.



### Trên macOS


Mở tệp `.dmg` đã tải xuống và kéo ứng dụng Mullvad Browser vào thư mục Ứng dụng của bạn.



### Trên Linux


Giải nén tệp `.tar.xz` vào thư mục bạn chọn và chạy tệp `start-mullvad-browser.desktop`.



## Cấu hình và sử dụng lần đầu



Khi bạn khởi chạy Mullvad Browser lần đầu, bạn sẽ thấy Interface rất giống với Tor Browser. Trình duyệt được cấu hình sẵn để bảo mật và không yêu cầu bất kỳ sửa đổi đặc biệt nào.



![MULLVAD BROWSER](assets/fr/04.webp)



*Trang chủ trình duyệt Interface Mullvad với tiện ích mở rộng, biểu tượng chổi đến generate, danh tính mới và menu ứng dụng ở góc trên bên phải.*



**Quan trọng:** Trình duyệt Mullvad không che giấu IP Address của bạn theo mặc định. Để được bảo vệ toàn diện, chúng tôi đặc biệt khuyên bạn nên sử dụng VPN song song. Bạn có thể sử dụng Mullvad VPN hoặc bất kỳ dịch vụ VPN đáng tin cậy nào khác.



Trình duyệt cũng bao gồm **DNS-over-HTTPS (DoH)** sử dụng dịch vụ DNS của Mullvad: công nghệ này mã hóa các yêu cầu DNS của bạn (dịch tên trang web thành địa chỉ IP) để ngăn ISP theo dõi các trang web bạn truy cập.



### Cài đặt an toàn



Bạn có thể điều chỉnh mức độ bảo mật bằng cách nhấp vào **menu ứng dụng** (ba thanh ngang) ở góc trên bên phải, sau đó nhấp vào **"Cài đặt"**, rồi đến tab **"Quyền riêng tư & Bảo mật"**. Cuộn xuống phần **"Bảo mật"**:



![MULLVAD BROWSER](assets/fr/05.webp)



*Lựa chọn mức độ bảo mật: các mũi tên hiển thị đường dẫn từ menu ứng dụng đến tab "Quyền riêng tư & Bảo mật" đến các tùy chọn bảo mật*



Trình duyệt Mullvad cung cấp ba cấp độ bảo mật:





- **Bình thường** (mức mặc định hiện tại): Tất cả các chức năng của trình duyệt và trang web đều được bật





- **An toàn hơn**: Vô hiệu hóa các chức năng thường nguy hiểm của trang web, có thể dẫn đến mất chức năng trên một số trang web:
 - JavaScript bị vô hiệu hóa đối với các trang web không phải HTTPS
 - Một số phông chữ và ký hiệu toán học bị vô hiệu hóa
 - Âm thanh và video (phương tiện HTML5) cũng như WebGL đều có thể "nhấp để phát"





- **An toàn nhất**: Chỉ cho phép các chức năng trang web cần thiết cho các trang web tĩnh và các dịch vụ cơ bản:
 - JavaScript bị vô hiệu hóa theo mặc định cho tất cả các trang web
 - Một số phông chữ, biểu tượng, hình ảnh và ký hiệu toán học bị vô hiệu hóa
 - Âm thanh và video (phương tiện HTML5) cũng như WebGL đều có thể "nhấp để phát"



### Nút phiên mới



Để khởi động lại với phiên làm việc trống mà không cần đóng trình duyệt, hãy nhấp vào biểu tượng chổi hoặc sử dụng menu ứng dụng > **"Phiên làm việc mới"**.



![MULLVAD BROWSER](assets/fr/06.webp)



*Chức năng "Đặt lại danh tính" để khởi động lại trình duyệt với một phiên hoàn toàn mới*



## Sử dụng hàng ngày



### Điều hướng bình thường



Trình duyệt Mullvad hoạt động như một trình duyệt cổ điển cho việc duyệt web hàng ngày. Tất cả các trang web đều có thể truy cập như bình thường, với lợi ích bổ sung là khả năng bảo vệ chống theo dõi được tăng cường.



### Quản lý cookie và đăng nhập



Vì chế độ riêng tư vĩnh viễn, bạn sẽ phải kết nối lại vào tài khoản mỗi khi đăng nhập. Đây là cái giá bạn phải trả cho tính bảo mật tối đa.



### Phần mở rộng



Về mặt kỹ thuật, Trình duyệt Mullvad cho phép bạn cài đặt các tiện ích mở rộng bổ sung từ danh mục Firefox, nhưng **điều quan trọng là phải hiểu rõ các tác động**. Mỗi tiện ích mở rộng được thêm vào sẽ thay đổi dấu vết kỹ thuật số của bạn và phân biệt bạn với những người dùng Trình duyệt Mullvad khác, điều này đi ngược lại nguyên tắc cơ bản của trình duyệt: làm cho tất cả người dùng đều xuất hiện giống hệt nhau.



Như Mullvad giải thích: *"Đôi khi, không có biện pháp phòng vệ cụ thể nào còn tốt hơn là có. Khi muốn tăng cường quyền riêng tư trực tuyến, bạn cài đặt các tiện ích mở rộng, cuối cùng khiến bạn dễ bị phát hiện hơn."*



Nếu bạn vẫn quyết định cài đặt tiện ích mở rộng, hãy lưu ý rằng bạn đang tạo một dấu vân tay duy nhất có thể được sử dụng để theo dõi bạn từ trang web này sang trang web khác. Để được bảo vệ tối đa, tốt nhất bạn nên sử dụng ba tiện ích mở rộng được cài đặt sẵn, giống hệt nhau cho tất cả người dùng.



## Thực hành tốt nhất với Trình duyệt Mullvad



1. **Luôn sử dụng VPN:** Trình duyệt Mullvad không che giấu IP của bạn. VPN là điều cần thiết để ẩn danh hoàn toàn.



2. **Không tùy chỉnh trình duyệt**: Tránh thay đổi cài đặt hoặc thêm tiện ích mở rộng vì điều này có thể khiến bạn bị nhận dạng.



3. **Sử dụng nút phiên mới**: Giữa các hoạt động khác nhau, hãy sử dụng chức năng đặt lại để phân vùng các phiên của bạn.



4. **Chọn mức độ bảo mật phù hợp nhất với nhu cầu của bạn**:




- **Bình thường (khuyến nghị)**: Dành cho việc duyệt web hàng ngày. Đã cung cấp khả năng bảo vệ tuyệt vời trong khi vẫn duy trì hoạt động của trang web. Đây là mức cân bằng tốt nhất cho 95% người dùng.
- **An toàn hơn**: Nếu bạn đang truy cập các trang web không xác định hoặc có khả năng nguy hiểm, hoặc cần bảo vệ thêm trên mạng Wi-Fi công cộng. Một số trang web có thể gặp sự cố.
- **An toàn nhất**: Dành riêng cho các tình huống rủi ro cao (báo chí điều tra, thông tin nhạy cảm, môi trường thù địch). Hầu hết các trang web hiện đại đều có thể bị tấn công, nhưng đó là cái giá phải trả cho mức độ bảo mật tối đa.



5. **Kiểm tra bản cập nhật thường xuyên**: Luôn cập nhật trình duyệt của bạn với các bản vá bảo mật mới nhất.



6. **Sử dụng công cụ tìm kiếm thân thiện với quyền riêng tư**: Chọn DuckDuckGo, Startpage hoặc Searx thay vì Google.



7. **Bật chế độ chỉ HTTPS**: Trong phần cài đặt, hãy đảm bảo rằng chế độ "Chỉ HTTPS" được bật để buộc kết nối an toàn.



8. **KHÔNG thay đổi bất kỳ cài đặt nâng cao nào**: Không giống như các trình duyệt khác, Mullvad Browser được thiết kế để TẤT CẢ người dùng đều có cùng cấu hình. Việc sửa đổi cài đặt trong `about:config` hoặc thay đổi cài đặt uBlock Origin/NoScript sẽ khiến bạn trở nên độc đáo và hoàn toàn mất đi tính ẩn danh của trình duyệt.



## Cấu hình DNS được đề xuất



Trình duyệt Mullvad tự động tích hợp Mullvad DNS-over-HTTPS. Nếu bạn đang sử dụng Mullvad VPN, tiện ích mở rộng sẽ khuyến nghị bạn **tắt Mullvad DoH** vì sử dụng máy chủ DNS của máy chủ VPN sẽ nhanh hơn. Nếu bạn không sử dụng Mullvad VPN, hãy bật Mullvad DoH để tránh bị ISP theo dõi DNS.



## Phần kết luận



Trình duyệt Mullvad là giải pháp tuyệt vời cho những ai tìm kiếm trải nghiệm duyệt web thân thiện với quyền riêng tư mà không bị giới hạn hiệu suất của mạng Tor. Kết hợp với VPN chất lượng, trình duyệt này mang đến khả năng bảo vệ mạnh mẽ chống lại việc theo dõi và giám sát trực tuyến.



Mặc dù có một số hạn chế nhất định (không có phiên bản di động, phiên làm việc không liên tục), Mullvad Browser vẫn là một công cụ hữu ích cho bất kỳ ai muốn lấy lại quyền kiểm soát quyền riêng tư kỹ thuật số. Tính dễ sử dụng và cấu hình mặc định khiến nó trở thành lựa chọn sáng suốt cho người dùng quan tâm đến quyền riêng tư, dù là người mới bắt đầu hay người dùng có kinh nghiệm.



## Tài nguyên



### Tài liệu chính thức




- [Trang web Trình duyệt Mullvad chính thức](https://mullvad.net/fr/browser)
- [Trang tải xuống Trình duyệt Mullvad](https://mullvad.net/en/download/browser)
- [Thông số kỹ thuật chi tiết](https://mullvad.net/en/browser/Hard-facts)
- [Tiện ích mở rộng trình duyệt Mullvad](https://mullvad.net/en/help/mullvad-browser-extension)



### Hướng dẫn và giải thích




- [Tại sao quyền riêng tư lại quan trọng](https://mullvad.net/en/why-privacy-matters/how-mass-surveillance-companies-collect-your-data)
- [Tor không có Tor: Khái niệm về trình duyệt Mullvad](https://mullvad.net/en/browser/tor-without-tor)
- [Cách chọn trình duyệt thân thiện với quyền riêng tư](https://mullvad.net/en/browser/things-to-look-for-when-choosing-a-browser)
- [Tìm hiểu dấu vân tay của trình duyệt](https://mullvad.net/en/browser/browser-fingerprinting)



### Hỗ trợ và giúp đỡ




- [Trung tâm trợ giúp trình duyệt Mullvad](https://mullvad.net/en/help/tag/mullvad-browser)
- [Những bước đầu tiên để bảo vệ quyền riêng tư trực tuyến](https://mullvad.net/en/help/first-steps-towards-online-privacy)



### Tài nguyên cộng đồng




- [Hướng dẫn về trình duyệt Mullvad - Hướng dẫn về quyền riêng tư](https://www.privacyguides.org/en/desktop-browsers/)
- [Thảo luận cộng đồng](https://discuss.privacyguides.net/t/about-changing-settings-in-mullvad-browser/18330)