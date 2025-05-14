---
name: Đăng nhập đơn giản
description: Danh tính được bảo vệ bằng bí danh
---
![cover](assets/cover.webp)

## Đăng nhập = email = mất quyền riêng tư


Trong thế giới kỹ thuật số, việc có một tài khoản cho mọi nền tảng mà người ta muốn truy cập đã trở thành thông lệ.

Mỗi dịch vụ này đều yêu cầu đăng nhập, thường được liên kết với cặp _username_ và _password_. Thông thường, tên người dùng là email cá nhân của người dùng.


Khi sử dụng email cá nhân Address cho mỗi lần đăng nhập, bạn có thể dễ dàng hình dung ra hậu quả đầu tiên: mất tính bảo mật, điều này sẽ trở nên nghiêm trọng nếu Address bao gồm _name.surname@serviceemail.com_.


Các nhà phát triển công cụ nguồn mở đã tạo ra một loạt các bộ ứng dụng, được sinh ra chính xác để giúp người dùng lấy lại một chút quyền riêng tư: họ vẫn có thể đăng nhập, nhưng sử dụng bí danh thay vì công cụ tiết lộ danh tính riêng tư của họ.


Đơn giản nhất trong số những cách mà tôi đã thử và vẫn đang thử nghiệm là [Simple Login](https://simplelogin.io/).


## Bí danh


Một bí danh email chỉ đơn giản là thay thế phần _name.surname_ của email Address của bạn bằng một tên giả. Đối với người dùng, không có gì thay đổi; dịch vụ bí danh chuyển tiếp email đến và đi từ Address thông thường như bình thường. Mọi người có thể tiếp tục sử dụng hộp thư đến của họ như họ vẫn làm, nhưng thay vì hiển thị tên thật của họ, nó sẽ hiển thị một người dùng không thể nhận dạng. Dịch vụ này cần phải hiệu quả và cho đến nay, Simple Login đã chứng minh được điều đó.


Khi truy cập trang Simple Login lần đầu tiên, bạn phải tạo một tài khoản (ở đây cũng vậy!), sử dụng email "chính thức" Address. Tại đây, bạn phải nhập email, mật khẩu và giải captcha.


![image](assets/it/02.webp)


Simple Login gửi tin nhắn xác minh đến email được chỉ định Address. Thay vì nhấp vào nút xác minh, bạn nên sao chép liên kết và dán vào thanh Address.


![image](assets/it/03.webp)


![image](assets/it/04.webp)


Bảng điều khiển Đăng nhập đơn giản sẽ mở ra ngay lập tức, kèm theo hướng dẫn ngắn gọn về cách điều hướng.


![image](assets/it/05.webp)


Cần lưu ý rằng Simple Login sẽ tự động kích hoạt đăng ký nhận bản tin, có thể hủy kích hoạt bằng lệnh thích hợp.


![image](assets/it/06.webp)


## Cài đặt


Bạn có thể xem ngay _Settings_ để khám phá các tính năng của dịch vụ. Simple Login bắt đầu với tất cả các tùy chọn đang hoạt động, bao gồm cả các tùy chọn _Premium_, có thể sử dụng trong 10 ngày. Sau khi thời gian dùng thử kết thúc, bạn sẽ có thể tạo 10 bí danh với hồ sơ này và bạn có thể liên kết trực tiếp email Proton của mình, vì Simple Login đã được nhà cung cấp email Thụy Sĩ mua lại.


![image](assets/it/07.webp)


Bạn có thể thiết lập một loạt các tham số hoặc kiểm tra xem email của bạn đã bị xâm phạm về mặt quyền riêng tư hay chưa.


![image](assets/it/08.webp)


Cuối cùng, bạn có thể xuất bản sao lưu hồ sơ của mình hoặc nhập bản sao lưu từ nhà cung cấp khác.


![image](assets/it/09.webp)


### Email công việc


Những người sử dụng email có tên miền cá nhân làm email công việc có thể thiết lập tên miền riêng.


![image](assets/it/10.webp)


Từ bảng điều khiển chính, bằng cách chọn _Mailboxes_, bạn thậm chí có thể thêm các địa chỉ email khác và cũng có thể sử dụng các bí danh sẽ được tạo theo đó. Ví dụ, trong hướng dẫn này, tôi quyết định tạo hồ sơ với hộp thư _gmail.com_, sau đó liên kết _proton.me_ Address.


![image](assets/it/11.webp)


Thêm Address mới, đặc biệt nếu nó thuộc về nhà cung cấp Proton, quy trình hướng dẫn cho thấy khả năng vào chế độ _sudo_, siêu người dùng. Simple Login sẽ yêu cầu nhập mật khẩu của hộp thư này, để chứng minh Ownership hợp lệ.


⚠️ **Cá nhân tôi khuyên bạn không nên làm điều này**. ⚠️


![image](assets/it/12.webp)


**Tốt hơn hết là bạn nên truy cập vào hộp thư email -> sao chép liên kết xác minh và dán vào thanh URL -> và xác minh mà không cần tiết lộ mật khẩu.**


![image](assets/it/13.webp)


Trong hai địa chỉ đã nhập, một địa chỉ sẽ trở thành địa chỉ mặc định và địa chỉ còn lại sẽ là địa chỉ phụ, nhưng bạn có thể dễ dàng chuyển đổi chúng và cài đặt có thể dễ dàng xác định trong bảng điều khiển.


![image](assets/it/14.webp)


Sau khi thêm email thứ hai Address (tùy chọn), hãy xem chúng ta có thể làm gì với Simple Login.


## Tạo bí danh


Trong bảng điều khiển, tùy chọn menu đầu tiên được gắn nhãn _Alias_, đây là nơi bạn có thể tạo chúng. Bạn có tùy chọn generate alias ngẫu nhiên bằng cách nhấp vào nút Random Alias, đây là nút Green được hiển thị trong ảnh tiếp theo. Tính năng này tạo ra một email Address độc đáo và hấp dẫn.


![image](assets/it/24.webp)


Tuy nhiên, nếu bạn muốn phân biệt các dịch vụ bằng cách đặt cho chúng những tên khác nhau, bạn phải chọn _New Custom Alias_. Bằng cách đó, bạn có thể đặt cho bí danh tên của dịch vụ bạn muốn truy cập (mạng xã hội, nhà cung cấp dịch vụ, sự kiện trực tuyến, người lạ tình cờ gặp, v.v.). Phần còn lại do Simple Login xử lý.

Để giải trí (nhưng thực ra không hẳn vậy) tôi quyết định tạo một bí danh cho ngân hàng và gọi là `BANK`. Mặc dù đúng là ngân hàng biết mọi thứ về tôi, nhưng tôi thấy thật buồn cười khi giao tiếp với họ bằng email Address mà họ không hiểu. Simple Login thực sự tạo ra một tên ngẫu nhiên, được phân cách với tên chúng ta chọn bằng dấu ``


Ở đây, email mới Address có thể trở thành:


- ngân hàng.breeding123@aleeas.com
- ngân hàng.platter456@slmails.com
- ngân hàng.preoccupy789@8shield.net
- và vân vân


Người dùng có thể chọn nhiều hơn một tên miền: tên miền công khai có sẵn trong gói miễn phí, trong khi những tên miền khác được chỉ định là riêng tư (bao gồm _@simplelogin.com_), mở rộng sự lựa chọn cho người dùng quyết định đăng ký gói trả phí.


![image](assets/it/15.webp)


Sau khi hậu tố và tên miền ngẫu nhiên đã được chọn, bạn có thể thiết lập liệu Address mới (và kỳ lạ) này có nên đóng vai trò là bí danh cho chỉ một trong các hộp thư email cá nhân hay cho tất cả các hộp thư. Bí danh sẽ sẵn sàng và hoạt động sau khi nhấp vào _Create_


![image](assets/it/16.webp)


Email mới Address đã được tạo và hiện đã có thể nhìn thấy, sẵn sàng để gửi (cho ngân hàng!) chỉ bằng cách sao chép.


![image](assets/it/18.webp)


Tại thời điểm này, bạn có thể tập trung vào việc tạo bí danh cho mọi dịch vụ hoặc nền tảng bạn muốn truy cập và yêu cầu email là thông số cần thiết để tạo tài khoản.


![image](assets/it/19.webp)


Đối với những người đam mê quyền riêng tư, cũng có tùy chọn generate email Address dựa trên giao thức UUID (không phải trên tên có thể nhận dạng được), tạo ra một mã định danh 128 bit duy nhất không được kiểm soát bởi các bên tập trung. Tính năng này, hữu ích cho các tài khoản nhạy cảm, có thể được tìm thấy trong menu _Random Alias_.


![image](assets/it/21.webp)

![image](assets/it/22.webp)


Như bạn thấy, đây là email Address cần được quản lý phù hợp.


Nếu bạn đổi ý và không muốn sử dụng bí danh nữa, chỉ cần nhấp vào lệnh _More_ của từng bí danh và chọn _Delete_.


![image](assets/it/23.webp)


## Quản lý bí danh


Việc tạo bí danh rất đơn giản, cũng như việc quản lý chúng, chỉ cần một chút cẩn thận và kỷ luật. Trên thực tế, tất cả lưu lượng truy cập vẫn sẽ đi qua hộp thư đến email mà chúng tôi đã xác định ngay từ đầu là hộp thư chính thức. Các thông báo và thông tin liên lạc quan trọng từ các nền tảng sẽ tiếp tục đến Gmail, Proton hoặc bất kỳ nhà cung cấp email nào.


Tuy nhiên, kết quả là chúng tôi đã bảo tồn được Address chính, ngay từ thời điểm tạo ra các bí danh, chúng tôi có toàn quyền quyết định tiết lộ cho ai và không cho ai.


Bí danh có thể dùng để nhận và gửi: người dùng khác sẽ nhận được phản hồi từ alias.preoccupy789@8shield.net, nếu đây là bí danh được chọn cho người nhận cụ thể đó.


## Ưu điểm


Nhìn chung, sử dụng bí danh là một cách hiệu quả để bảo vệ danh tính và quyền riêng tư của bạn. Địa chỉ email thường được các nhà môi giới dữ liệu và trang web thu thập để theo dõi thói quen và hành vi của người dùng. Mặc dù bí danh không khiến bạn hoàn toàn không thể theo dõi, nhưng việc sử dụng bí danh một cách nhất quán là một bước tích cực hướng tới việc bảo vệ thông tin của bạn. Hơn nữa, trong "ngôi làng kỹ thuật số toàn cầu" của chúng ta, nơi mà tình trạng hack, bán dữ liệu và vi phạm bảo mật diễn ra quá phổ biến, rất có khả năng email bạn sử dụng để đăng ký trên nhiều trang web đã bị xâm phạm hoặc nhắm mục tiêu.


Một bí danh duy nhất, được sử dụng cho mọi lần đăng nhập, **cho phép chúng ta ngay lập tức hiểu được nền tảng nào gửi thư rác (hoặc tệ hơn) đến hộp thư của chúng ta, vì email được xác định bằng bí danh liên kết với nó**. Bạn không biết có bao nhiêu thư rác và lừa đảo đến từ các kênh được gọi là đáng tin cậy, vì chúng là các tổ chức, cho đến khi bạn bắt đầu sử dụng bí danh cho các ngân hàng, một bí danh cho các dịch vụ bưu chính hoặc một bí danh cụ thể cho một số dịch vụ bắt buộc của chính phủ. Khi người gửi thư rác (hoặc tệ hơn) được xác định, bạn sẽ biết rằng trang web đó đã bị xâm phạm, thực hiện mọi biện pháp phòng ngừa để bảo vệ tất cả dữ liệu được cung cấp (hãy nghĩ đến thẻ tín dụng!) cho trang web cụ thể đó, có thể nhận ra vi phạm sau nhiều tuần.


Về Simple Login, công cụ này có các tính năng sau:



- ứng dụng di động (cũng từ F-Droid) và tiện ích mở rộng của trình duyệt, để quản lý bí danh trong mọi tình huống;
- xác thực hai yếu tố cho mỗi bút danh mới, giúp tăng mức độ độc lập so với chính dịch vụ;
- Hỗ trợ PGP (dành cho người dùng _Premium);
- tạo đơn giản mọi loại bí danh (tùy chỉnh, ngẫu nhiên và UUID);
- trong số các gói miễn phí trong ngành, khả năng sử dụng bí danh với hộp thư email "chính thức" hơn. Các đối thủ cạnh tranh khác chỉ giới hạn ở một.


## Nhược điểm


- 10 bí danh có thể không đủ nếu bạn định sử dụng Simple Login rộng rãi. Trong trường hợp này, gói trả phí, khá phải chăng, hữu ích để tăng số lượng bí danh có thể có.
- Không thể tạo bí danh với tên và tên miền cụ thể. Hậu tố ngẫu nhiên, được thêm vào sau tên do chúng tôi chọn, tạo ra Address có thể được mô tả là kỳ lạ nhất. Phương tiện truyền thông xã hội truyền thống thường từ chối cấp tài khoản được tạo bằng loại địa chỉ email này. Nostr khắc phục điều này!
- Nếu bạn sử dụng bí danh để gửi tin nhắn cho ai đó, tin nhắn đó rất dễ bị đưa vào thư mục thư rác của người nhận. Bước đầu tiên, bạn nên sử dụng bí danh để nhận, giống như trong trường hợp tạo tài khoản, đăng ký danh sách gửi thư, v.v.