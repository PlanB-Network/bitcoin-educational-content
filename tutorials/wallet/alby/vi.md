---
name: Alby

description: Tiện ích mở rộng trình duyệt dành cho Bitcoin và Lightning Network
---

![cover](assets/cover.webp)




Làm cho việc thanh toán bằng Bitcoin trở nên dễ dàng hơn là thách thức mà nhiều công ty trong lĩnh vực này đang phải đối mặt. Alby nổi bật hơn cả với tiện ích mở rộng Alby wallet dành cho trình duyệt. Tiện ích mở rộng này nhằm mục đích thiết lập một khung hệ thống mượt mà, tự động phát hiện địa chỉ và cho phép bạn thực hiện các giao dịch thanh toán Bitcoin không gặp trở ngại. Trong hướng dẫn này, chúng ta sẽ khám phá tiện ích mở rộng Alby và kiểm tra cách nó hỗ trợ thanh toán từ trình duyệt.




![video](https://youtu.be/nd5fX2vHuDw)




## Mở rộng Alby



Tiện ích mở rộng Alby là một công cụ cho phép trình duyệt web của bạn tương tác dễ dàng và an toàn với mạng Bitcoin và lớp Lightning Network của nó. Nó được đặc trưng bởi ba khía cạnh:




- Lightning Network wallet: Liên kết nút hoặc tài khoản Alby của bạn để gửi và nhận bitcoin nhanh chóng và tiết kiệm chi phí thông qua lớp Lightning Network.
- Thanh toán mượt mà qua Web: Loại bỏ nhu cầu quét mã QR hoặc chuyển đổi giữa các ứng dụng để thanh toán Bitcoin trên các trang web hỗ trợ Lightning. Cho phép giao dịch trơn tru chỉ với một cú nhấp chuột, hoặc không cần xác nhận nếu bạn đã thiết lập ngân sách.
- Trình quản lý Nostr: Tiện ích mở rộng này quản lý các khóa Nostr của bạn, giúp dễ dàng kết nối và tương tác với các ứng dụng Nostr hoạt động như một bên ký điện tử an toàn mà không để lộ khóa riêng tư của bạn cho mọi nền tảng.



https://planb.academy/tutorials/node/others/nostr-f6d21a64-9b04-4f21-ba1c-02c98cc91f98

https://planb.academy/tutorials/node/others/umbrel-nostr-7ae147e8-f5cd-46e1-861b-17c2ea1e08fd

## Kết nối với tiện ích mở rộng



Trong hướng dẫn này, chúng ta sẽ sử dụng tiện ích mở rộng Alby trong trình duyệt Firefox trên hệ điều hành Ubuntu. Tuy nhiên, nó cũng có sẵn trên Windows và các trình duyệt như Chrome.



Bạn có thể thêm tiện ích mở rộng Alby vào trình duyệt của mình bằng cách truy cập cửa hàng tiện ích mở rộng [Firefox](https://addons.mozilla.org/fr/firefox/addon/alby/) hoặc cửa hàng tiện ích mở rộng [Chrome](https://chromewebstore.google.com/detail/alby-bitcoin-wallet-for-l/iokeahhehimjnekafflcihljlcjccdbe).



![firefox](assets/fr/01.webp)



![chrome](assets/fr/02.webp)



ℹ️ Điều quan trọng là phải kiểm tra xem tác giả của tiện ích mở rộng có thực sự là tài khoản chính thức của Alby hay không, để tránh mọi hình thức vi phạm bản quyền hoặc đánh cắp bitcoin của bạn.



Thêm tiện ích mở rộng vào trình duyệt của bạn bằng cách nhấp vào nút bên phải.


Cấp quyền cần thiết để cài đặt và sử dụng tiện ích mở rộng, sau đó ghim tiện ích mở rộng vào thanh công cụ để dễ dàng truy cập.



![pin](assets/fr/03.webp)



Bạn cũng nên thiết lập mã mở khóa (rất quan trọng), mã này sẽ đảm bảo truy cập an toàn vào Lightning wallet của bạn từ trình duyệt. Chúng tôi khuyên bạn nên đặt mật khẩu mạnh gồm cả chữ và số.



ℹ️ Hãy lưu mật khẩu này ở một nơi an toàn để bạn có thể truy cập lại nếu quên, vì mật khẩu này có thể bị thay đổi nhưng không thể khôi phục lại.



https://planb.academy/tutorials/computer-security/authentication/seedkeeper-password-64ffaf68-53aa-43c3-bc7a-c1dc2a17fee3

![pass](assets/fr/04.webp)



Alby thể hiện tính linh hoạt của mình bằng cách cung cấp cho bạn hai lựa chọn:




- Hãy tiếp tục sử dụng tài khoản Alby nếu bạn muốn tận hưởng các ứng dụng mà vẫn giữ quyền kiểm soát bitcoin của mình.
- Hãy kết nối thiết bị wallet hoặc Lightning của riêng bạn nếu bạn đã có sẵn một thiết bị được tiện ích mở rộng này hỗ trợ.



https://planb.academy/tutorials/wallet/mobile/blink-7ea5f5a4-e728-4ff9-b3f9-cf20aa6fc2bd

https://planb.academy/tutorials/node/lightning-network/lightning-network-daemon-linux-59d777e9-72c8-4b32-8c50-e86cdae8f2f9

https://planb.academy/tutorials/business/point-of-sale/btcpay-server-928eb01e-824b-4b57-a3e8-8727633beddc


Trong hướng dẫn này, chúng ta sẽ tiếp tục sử dụng tài khoản Alby để tận dụng các tính năng của hệ sinh thái Alby.



https://planb.academy/tutorials/wallet/mobile/alby-go-40202802-b346-4a3c-9863-465c3bde9903

https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Đăng nhập vào tài khoản Alby của bạn, hoặc tạo tài khoản mới nếu bạn chưa có.



![signup](assets/fr/05.webp)



## Thực hiện các khoản thanh toán đầu tiên của bạn



Sau khi đăng nhập, bạn có thể nhấp vào tiện ích mở rộng Alby trên thanh công cụ để truy cập vào danh mục đầu tư của mình.



![buzzin](assets/fr/06.webp)



Sau khi tạo tài khoản Alby, bạn cần kết nối nó với wallet để có thể chi tiêu satoshi. Để liên kết wallet bitcoin với tài khoản Alby của bạn, chúng tôi khuyên bạn nên sử dụng node Alby Hub, bạn có thể thiết lập node này trên máy tính của mình hoặc đăng ký gói dịch vụ do Alby cung cấp.



![hubplan](assets/fr/13.webp)




Trong hướng dẫn này, tài khoản Alby của chúng ta được hỗ trợ bởi một bản cài đặt cục bộ trên máy tính của chúng ta.


Để tự xây dựng nút Alby của riêng bạn, chúng tôi khuyên bạn nên tham khảo hướng dẫn Alby Hub của chúng tôi.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a

Nút này cho phép bạn tạo danh mục đầu tư Lightning tự quản lý và quản lý hiệu quả các kênh Lightning để gửi và nhận satoshi.



![channels](assets/fr/14.webp)



Mở các kênh tiếp nhận xác định tổng số satoshi bạn có thể nhận được.



![receivechanal](assets/fr/15.webp)



Mở các kênh gửi bằng cách khóa satoshi trên địa chỉ Bitcoin trên chuỗi khối. Số satoshi bạn đã khóa sẽ xác định tổng số satoshi bạn có thể chi tiêu.



![spend](assets/fr/16.webp)



Giờ đây bạn có thể gửi và nhận satoshi thông qua tiện ích mở rộng Alby.



![exchange](assets/fr/08.webp)



Từ thời điểm này trở đi, tiện ích mở rộng Alby có khả năng phát hiện các địa chỉ Lightning và hóa đơn có sẵn trên các trang web bạn truy cập, và sẽ đề xuất bạn thanh toán bằng bitcoin hoặc Lightning trực tiếp từ tiện ích mở rộng của mình.



![suggest](assets/fr/09.webp)



![pay](assets/fr/10.webp)




## Bảo mật các khóa khôi phục bằng khóa chính



Khóa chính do tiện ích mở rộng Alby cung cấp hoạt động như một lớp bảo vệ cho phép bạn giao tiếp an toàn với lớp mạng chính Bitcoin (Onchain), hệ thống Nostr và cho phép bạn kích hoạt kết nối Lightning với các ứng dụng Nostr.



![masterKey](assets/fr/11.webp)



Khóa chính này có dạng 12 từ, tương tự như cụm từ khôi phục của bạn. Do đó, chúng tôi khuyên bạn nên lưu trữ nó bằng các phương pháp an toàn để đảm bảo có thể truy cập bất cứ lúc nào.



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270


![masterKey](assets/fr/12.webp)



Giờ đây, bạn có thể trải nghiệm thanh toán Bitcoin và Lightning mượt mà không gặp trở ngại với tiện ích mở rộng Alby. Nếu bạn thấy hướng dẫn này hữu ích, chúng tôi khuyên bạn nên tham khảo hướng dẫn Alby Hub để thiết lập nút Alby của riêng mình và kiểm soát mọi khía cạnh của ví Alby từ một giao diện mượt mà và mạnh mẽ.



https://planb.academy/tutorials/node/lightning-network/alby-hub-62e6356c-6a6d-4134-8f22-c3b6afb9882a