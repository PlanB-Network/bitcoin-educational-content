---
name: Ashigaru Terminal
description: Sử dụng Ashigaru trên máy tính để bàn để tạo coinjoin
---

![cover](assets/cover.webp)



Ashigaru Terminal là phiên bản chuyển thể của nhóm Ashigaru từ Sparrow Server, triển khai giao thức coinjoin Whirlpool. Phần mềm này là sự tiếp nối công trình do Samourai Wallet khởi xướng, đặc biệt là trên giao diện người dùng đồ họa (GUI) Whirlpool, với các nguyên tắc cơ bản: tự quản lý và bảo mật.



Phần mềm này là fork của Sparrow Server, được sửa đổi và tối ưu hóa để tích hợp hoàn toàn với hệ sinh thái Whirlpool, giao thức ZeroLink coinjoin ban đầu được phát triển bởi nhóm Samourai.



Ashigaru Terminal hoạt động trên giao diện TUI tối giản và có thể được triển khai trên máy tính cá nhân hoặc máy chủ chuyên dụng. Nó cho phép bạn tương tác trực tiếp với Whirlpool để khởi tạo "*Tx0*", quản lý các tài khoản "*Deposit*", "*Premix*", "*Postmix*" và "*Badbank*", cũng như thực hiện các bản phối lại tự động để tăng cường tính bảo mật cho các phần của bạn.



Tóm lại, Ashigaru Terminal sẽ đặc biệt hữu ích nếu bạn muốn tạo coinjoin bằng Whirlpool.



Trong hướng dẫn đầu tiên này, tôi sẽ hướng dẫn bạn cài đặt và vận hành Ashigaru Terminal. Hướng dẫn thứ hai, nâng cao hơn, sẽ dành riêng cho việc tạo coinjoin thực tế.



https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef

## 1. Cài đặt Ashigaru Terminal



Để cài đặt Ashigaru Terminal, bạn cần có Tor Browser, vì các tệp nhị phân chỉ được phân phối qua mạng Tor. Nếu bạn chưa cài đặt, hãy [cài đặt nó trên máy của bạn](https://www.torproject.org/download/).



### 1.1. tải xuống thiết bị đầu cuối Ashigaru



Từ Tor Browser, hãy truy cập [trang phát hành của kho lưu trữ Git](http://ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/) để tải xuống phiên bản Ashigaru Terminal mới nhất cho hệ điều hành của bạn.



```txt
ashicodepbnpvslzsl2bz7l2pwrjvajgumgac423pp3y2deprbnzz7id.onion/Ashigaru/Ashigaru-Terminal/releases/
```



![Image](assets/fr/01.webp)



Tải xuống 2 tệp sau cho hệ điều hành của bạn:




- Tệp nhị phân (`ashigaru_terminal_v1.0.0_amd64.deb` cho Debian/Ubuntu, `.dmg` cho macOS hoặc `.zip` cho Windows);
- Tệp băm đã ký: `ashigaru_terminal_v1.0.0_signed_hashes.txt`.



### 1.2. Kiểm tra Ashigaru Terminal



Trước khi chạy phần mềm trên thiết bị, bạn cần kiểm tra tính xác thực và toàn vẹn của nó. Đây là một bước quan trọng, vì nó giúp bạn tránh cài đặt phiên bản lừa đảo có thể làm mất bitcoin hoặc lây nhiễm vào máy tính của bạn.



Mở một tab trình duyệt mới và truy cập [Công cụ xác minh Keybase](https://keybase.io/verify). Dán nội dung của tệp `.txt` bạn vừa tải xuống vào trường được cung cấp, sau đó nhấp vào nút `Xác minh`.



![Image](assets/fr/02.webp)



Để đa dạng hóa các nguồn xác minh của mình, bạn cũng có thể so sánh tin nhắn với tin nhắn có sẵn trên trang clearnet [ashigaru.rs](https://ashigaru.rs/download/), trong phần `/download`.



![Image](assets/fr/03.webp)



Nếu chữ ký hợp lệ, Keybase sẽ hiển thị thông báo xác nhận rằng tệp đã được các nhà phát triển của Ashigaru ký.



![Image](assets/fr/04.webp)



Bạn cũng có thể nhấp vào hồ sơ `ashigarudev` được Keybase hiển thị và kiểm tra xem dấu vân tay khóa của họ có khớp chính xác không: `A138 06B1 FA2A 676B`.



![Image](assets/fr/05.webp)



Nếu lỗi xuất hiện ở giai đoạn này, chữ ký không hợp lệ. Trong trường hợp này, **không cài đặt phần mềm đã tải xuống**. Hãy bắt đầu lại từ đầu hoặc nhờ cộng đồng hỗ trợ trước khi tiếp tục.



Keybase đã cung cấp cho bạn mã băm đã được xác thực của ứng dụng. Bây giờ, chúng tôi sẽ kiểm tra xem mã băm của tệp `.deb`, `.zip` hoặc `.dmg` bạn đã tải xuống có khớp với mã băm đã được xác thực trên Keybase hay không. Để thực hiện việc này, hãy truy cập [TỆP BĂM TRỰC TUYẾN](https://hash-file.online/).



Nhấp vào nút `BROWSE...` và chọn tệp `.deb`, `.zip` hoặc `.dmg` đã tải xuống ở bước 1.1. Sau đó, chọn hàm băm `SHA-256` và nhấp vào `CALCULATE HASH` để tính toán hàm băm cho tệp của bạn.



![Image](assets/fr/06.webp)



Sau đó, trang web sẽ hiển thị mã băm phần mềm. Hãy so sánh mã băm này với mã băm bạn đã xác minh trên Keybase.io. Nếu hai mã băm khớp hoàn toàn, quá trình kiểm tra tính xác thực và tính toàn vẹn đã thành công. Sau đó, bạn có thể sử dụng phần mềm.



![Image](assets/fr/07.webp)



### 1.3 Khởi chạy Ashigaru Terminal





- Debian / Ubuntu



Để cài đặt phần mềm, hãy chạy lệnh:



```bash
cd ~/Downloads
sudo apt install ./ashigaru_terminal_v1.0.0_amd64.deb
```



Sửa đổi thứ tự theo phiên bản đã tải xuống.



Sau đó kiểm tra cài đặt:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal --version
```



Sau đó khởi chạy phần mềm:



```bash
/opt/ashigaru-terminal/bin/Ashigaru-terminal
```





- Cửa sổ**



Nhấp chuột phải vào tệp `.zip` mà bạn đã tải xuống và kiểm tra, sau đó chọn `Extract All...` để giải nén nội dung của tệp.



Sau khi giải nén xong, hãy nhấp đúp vào tệp `Ashigaru-terminal.exe` để khởi chạy phần mềm.



![Image](assets/fr/08.webp)



## 2. Bắt đầu với Ashigaru Terminal



Ashigaru Terminal là một chương trình TUI (*Text-based User Interface*), tức là một giao diện tối giản chạy trực tiếp trong terminal. Bạn tương tác với nó bằng menu và phím tắt, nhưng không có bất kỳ môi trường đồ họa cổ điển thực sự nào.



![Image](assets/fr/09.webp)



Rất dễ sử dụng: sử dụng các phím mũi tên trên bàn phím để điều hướng qua các menu và nhấn phím `Enter` để xác thực một hành động hoặc xác nhận một lựa chọn.



## 3. Kết nối nút của bạn với Ashigaru Terminal



Theo mặc định, Ashigaru Terminal kết nối với máy chủ Electrum công cộng. Điều này rõ ràng tiềm ẩn rủi ro về tính bảo mật và chủ quyền. Vì vậy, chúng tôi sẽ cấu hình nó để kết nối trực tiếp với Electrum Server của bạn.



Để thực hiện việc này, hãy mở menu `Tùy chọn > Máy chủ`.



![Image](assets/fr/10.webp)



Nhấp vào nút `<Chỉnh sửa>`.



![Image](assets/fr/11.webp)



Chọn `Private Electrum Server`, sau đó nhấp vào `<Tiếp tục>`.



![Image](assets/fr/12.webp)



Nhập URL và cổng máy chủ của bạn. Bạn có thể chỉ định địa chỉ Tor trong `.onion`. Sau đó, nhấp vào `<Test>` để xác minh kết nối.



![Image](assets/fr/13.webp)



Nếu kết nối thành công, thông báo `Thành công` sẽ xuất hiện cùng với thông tin chi tiết về máy chủ của bạn.



![Image](assets/fr/14.webp)



Nếu bạn chưa có nút Bitcoin, tôi khuyên bạn nên tham gia khóa học này:



https://planb.academy/courses/3cd9cb94-82e8-417a-9c5a-02afc2589426

*Trong trường hợp của tôi, đối với hướng dẫn này, tôi sẽ ngắt kết nối khỏi máy chủ Electrs vì tôi đang làm việc trên mạng thử nghiệm. Tuy nhiên, hoạt động vẫn hoàn toàn giống hệt trên mainnet.*



## 4. Tạo danh mục đầu tư trên Ashigaru Terminal



Bây giờ phần mềm đã được cấu hình chính xác, chúng ta có thể thêm danh mục đầu tư Bitcoin.



Bạn có hai lựa chọn:




- Bạn có thể tạo một wallet mới từ đầu và sử dụng độc quyền trên Ashigaru Terminal. Trong trường hợp này, bạn sẽ cần mở phần mềm này mỗi khi muốn tương tác với wallet;
- Ngoài ra, bạn có thể nhập Ashigaru wallet hiện có trực tiếp từ điện thoại vào Ashigaru Terminal. Nhược điểm của phương pháp này là nó làm giảm nhẹ tính bảo mật của thiết lập, vì wallet của bạn sẽ phải tiếp xúc với hai môi trường rủi ro thay vì một. Mặt khác, nó mang lại lợi thế là bạn có thể để Ashigaru Terminal chạy liên tục để trộn lẫn tiền của mình, đồng thời cho phép bạn chi tiêu chúng từ xa thông qua ứng dụng di động Ashigaru.



Trong hướng dẫn này, chúng ta sẽ chọn phương pháp thứ hai. Tuy nhiên, nếu bạn muốn tạo một danh mục đầu tư hoàn toàn mới, quy trình vẫn giữ nguyên: điểm khác biệt duy nhất nằm ở khâu tạo, khi bạn cần lưu cụm từ ghi nhớ mới và mã passphrase mới.



Cũng lưu ý rằng Ashigaru Terminal không cho phép bạn chi tiêu bitcoin trực tiếp. Bạn có thể đồng bộ cùng một ví trên Ashigaru Terminal và ứng dụng Ashigaru (điều tôi sẽ thực hiện trong hướng dẫn này), hoặc trên Sparrow Wallet.



Nếu bạn chưa có wallet trên ứng dụng Ashigaru, bạn có thể làm theo hướng dẫn chuyên dụng:



https://planb.academy/tutorials/wallet/mobile/ashigaru-9f903b55-2e55-4b06-9627-80f8e178158f

Vào menu `Ví`.



![Image](assets/fr/15.webp)



Sau đó chọn `Tạo / khôi phục wallet...`. Tùy chọn `Mở Wallet...` cho phép bạn truy cập danh mục đầu tư đã lưu trong Ashigaru Terminal sau này.



![Image](assets/fr/16.webp)



Đặt tên cho danh mục đầu tư của bạn.



![Image](assets/fr/17.webp)



Sau đó chọn loại danh mục đầu tư `Hot Wallet`.






![Image](assets/fr/18.webp)



Ở giai đoạn này, quy trình sẽ khác nhau tùy thuộc vào lựa chọn ban đầu của bạn:




- Nếu bạn muốn tạo một danh mục đầu tư mới từ đầu, hãy nhấp vào `<Tạo Wallet mới>`, xác định passphrase BIP39, sau đó cẩn thận lưu cụm từ ghi nhớ và passphrase của bạn vào một phương tiện vật lý;



https://planb.academy/tutorials/wallet/backup/backup-mnemonic-22c0ddfa-fb9f-4e3a-96f9-46e2a7954270



- Nếu bạn muốn sử dụng cùng mã wallet với ứng dụng Ashigaru của mình, hãy nhập trực tiếp 12 từ của cụm từ ghi nhớ và mã passphrase BIP39 vào các trường tương ứng. Viết các từ bằng chữ thường, nguyên vẹn, theo thứ tự, cách nhau bằng khoảng trắng, không có số hoặc ký tự thừa.



Khi hoàn tất bước này, hãy nhấp vào `< Tiếp theo >`.



*Lưu ý*: Nếu bạn không thể nhấp vào nút này, cụm từ ghi nhớ của bạn không hợp lệ. Hãy kiểm tra cẩn thận để đảm bảo không có từ nào bị sai chính tả hoặc viết sai chính tả.



![Image](assets/fr/19.webp)



Sau đó, bạn sẽ cần đặt mật khẩu. Mật khẩu này sẽ được sử dụng để mở khóa Ashigaru Terminal wallet của bạn và bảo vệ nó khỏi sự truy cập vật lý trái phép. Mật khẩu này không liên quan đến việc giải mã khóa của bạn: nói cách khác, ngay cả khi không có mật khẩu này, bất kỳ ai có cụm từ ghi nhớ và passphrase của bạn đều có thể khôi phục wallet và truy cập bitcoin của bạn.



Chọn một mật khẩu dài, phức tạp và ngẫu nhiên. Lưu một bản sao ở nơi an toàn: lý tưởng nhất là trên một thiết bị lưu trữ vật lý hoặc trong một trình quản lý mật khẩu an toàn.



Nhấp vào `< OK >` khi bạn hoàn tất.



![Image](assets/fr/20.webp)



## 5. Sử dụng danh mục đầu tư



Sau đó, bạn có thể chọn tài khoản để truy cập. Hiện tại, chúng tôi chưa khởi tạo bất kỳ giao dịch trộn nào, vì vậy chúng tôi sẽ truy cập tài khoản `Gửi tiền`.



![Image](assets/fr/21.webp)



Thao tác sau đó giống hệt với Sparrow, vì Ashigaru Terminal là fork của Sparrow Server. Bạn sẽ thấy các menu tương tự:



![Image](assets/fr/22.webp)





- "giao dịch": cho phép bạn xem lịch sử giao dịch được liên kết với tài khoản này. Trong trường hợp của tôi, một số giao dịch đã xuất hiện vì tôi đã thực hiện một số giao dịch bằng ứng dụng Ashigaru trên cùng chiếc wallet này.



![Image](assets/fr/23.webp)





- receive`: tạo một địa chỉ biên lai mới, trống để gửi satss vào tài khoản tiền gửi.



![Image](assets/fr/24.webp)





- addresses`: hiển thị danh sách tất cả các địa chỉ của bạn, cho dù chúng thuộc chuỗi nội bộ hay chuỗi bên ngoài của tài khoản bạn.



![Image](assets/fr/25.webp)





- `UTXOs`: liệt kê tất cả các UTXO khả dụng của bạn.



![Image](assets/fr/26.webp)





- `Cài đặt`: cho phép truy cập *mô tả* danh mục đầu tư của bạn. Bạn cũng có thể tham khảo seed, điều chỉnh *Giới hạn Khoảng cách* hoặc thay đổi ngày tạo danh mục đầu tư.



![Image](assets/fr/27.webp)



Bây giờ bạn đã biết cách cài đặt và sử dụng Ashigaru Terminal. Trong hướng dẫn tiếp theo, chúng ta sẽ xem cách thực hiện coinjoin với phần mềm này và cách quản lý quỹ trong "*Postmix*".
https://planb.academy/tutorials/privacy/on-chain/ashigaru-whirlpool-e566803d-ab3f-4d98-9136-5462009262ef
