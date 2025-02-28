---
name: RaspiBlitz
description: Hướng dẫn thiết lập RaspiBlitz của bạn
---

![image](assets/0.webp)

RaspiBlitz là một dự án tự làm Node Lightning (LND và/hoặc Core Lightning) chạy cùng với một Bitcoin-Fullnode trên RaspberryPi (ổ cứng SSD 1TB) và một màn hình đẹp để thiết lập & giám sát dễ dàng.

RaspiBlitz chủ yếu nhắm đến việc học cách tự chạy node của riêng bạn một cách phi tập trung từ nhà - bởi vì: Không phải Node của bạn, không phải Luật của bạn. Khám phá & phát triển hệ sinh thái đang phát triển của Lightning Network bằng cách trở thành một phần không thể thiếu của nó. Xây dựng nó như một phần của một hội thảo hoặc dự án cuối tuần do chính bạn thực hiện.

![video](https://youtu.be/DTHlSPMz3ns)
RASPIBLITZ - Cách Chạy Một Node Lightning và Bitcoin Full Node bởi BTC session

# Hướng dẫn Thiết lập Raspiblitz của Parman

Raspiblitz là một hệ thống tuyệt vời để chạy một Bitcoin Node và các ứng dụng liên quan. Tôi khuyên dùng nó và node My Node cho hầu hết người dùng (Lý tưởng là có hai node để dự phòng.) Một lợi thế lớn là node Raspiblitz là "Phần mềm Tự do Mã nguồn Mở", không giống như MyNode hoặc Umbrel. Tại sao điều này lại quan trọng? Vlad Costa giải thích. Bạn cũng có thể chạy RaspbiBlitz với kết nối WiFi thay vì ethernet – đây là một hướng dẫn bổ sung cho việc đó. (Tôi chưa tìm ra cách làm điều này với MyNode).

Bạn có thể mua một node đã được làm sẵn với một màn hình mini gắn kèm, hoặc bạn có thể tự xây dựng nó (bạn không cần màn hình).

Hướng dẫn trên trang github rất tốt, nhưng có thể quá chi tiết đối với người dùng có kinh nghiệm vừa phải. Hướng dẫn của tôi sẽ ngắn gọn và hy vọng dễ theo dõi hơn.

Cơ bản, quy trình rất giống với quy trình thiết lập một node MyNode với Raspberry Pi 4. Hướng dẫn Raspiblitz gợi ý bạn mua một màn hình, nhưng thực sự bạn không cần, và tôi không khuyến khích. Bạn thậm chí không cần bàn phím hoặc chuột phụ. Chỉ cần truy cập menu terminal của thiết bị qua một máy tính trên cùng mạng nhà, và sử dụng lệnh ssh qua terminal. Điều này khả thi với Linux/Mac (dễ dàng) và hơi khó hơn với Windows.

## Bước 1: Mua thiết bị.

Bạn cần chính xác cùng một thiết bị mà bạn cần để chạy một node MyNode. Bạn có thể thử một trong hai, sự khác biệt duy nhất là dữ liệu trên thẻ micro SD.

- Raspberry Pi 4, bộ nhớ 4Gb hoặc 8Gb (4Gb là đủ)
- Nguồn Raspberry Pi chính hãng (Rất quan trọng! Đừng mua hàng không chính hãng, nghiêm túc đấy)
- Một vỏ cho Pi. (Vỏ FLIRC rất tuyệt. Toàn bộ vỏ là một tản nhiệt và bạn không cần quạt, có thể gây ồn)
- Thẻ microSD 32 Gb (bạn cần một cái, nhưng có vài cái là tiện lợi.)
- Một đầu đọc thẻ nhớ (hầu hết máy tính sẽ không có khe cắm cho thẻ microSD).
- Ổ cứng SSD ngoài 1Tb.
- Một cáp ethernet (để kết nối với router nhà bạn).

Bạn không cần màn hình (hoặc bàn phím hoặc chuột)

Lưu ý: Đây là ổ cứng sai: Đây là một ổ cứng ngoài di động. Nó không phải là SSD. SSD rất quan trọng. Đây là lý do tại sao nó rẻ (Giá bằng AUD)

![image](assets/1.webp)

Đây là loại đúng cần mua:

![image](assets/2.webp)

Loại này nhanh hơn, nhưng không cần thiết và đắt:

![image](assets/3.webp)

## Bước 2: Tải xuống Hình ảnh Raspiblitz
Truy cập trang web github của Raspiblitz và tìm liên kết "download image":
![image](assets/4.webp)

Mã hash sha-256 của tệp đã tải xuống được cung cấp trên trang web. Mã này sẽ thay đổi với mỗi bản cập nhật. Nếu bạn không hiểu điều này là gì, bạn nên tìm hiểu, vì vậy tôi đã viết một hướng dẫn bạn có thể đọc tại đây.

![image](assets/5.webp)

## Bước 3: Xác minh Hình Ảnh

Trước khi tiếp tục, nếu bạn không biết cách sử dụng hệ thống tệp trên dòng lệnh, việc học cách sử dụng nó rất dễ dàng, và bạn nên làm.

Dưới đây là một video hữu ích cho Linux, nhưng cũng áp dụng cho Mac.

Đối với Windows, đây là một hướng dẫn đơn giản.
Mac/Linux

Chờ tệp tải xuống hoàn tất (quimportant!), sau đó mở terminal, điều hướng đến nơi bạn đã tải tệp xuống, và gõ lệnh sau...

```bash
shasum -a 256 xxxxxxxxxxxxxx
```

trong đó xxxxxxxxxxxxxx là tên của tệp bạn vừa tải xuống. Nếu bạn không ở trong thư mục chứa tệp đó, bạn phải gõ đường dẫn đầy đủ.

Máy tính sẽ xử lý trong khoảng 20 giây hoặc hơn. Kiểm tra xem mã hashfile đầu ra có trùng khớp với mã được tải xuống từ trang web ở bước trước không. Nếu giống hệt, bạn có thể tiếp tục.
Windows

Mở cửa sổ lệnh và điều hướng đến nơi tệp được tải xuống, và gõ lệnh này:

```bash
certUtil -hashfile xxxxxxxxxxxxxxx SHA256
```

trong đó xxxxxxxxxxxxxx là tên của tệp bạn vừa tải xuống. Nếu bạn không ở trong thư mục chứa tệp đó, bạn phải gõ đường dẫn đầy đủ.

Máy tính sẽ xử lý trong khoảng 20 giây hoặc hơn. Kiểm tra xem mã hashfile đầu ra có trùng khớp với mã được tải xuống từ trang web ở bước trước không. Nếu giống hệt, bạn có thể tiếp tục.

## Bước 4: Ghi vào thẻ SD

Bạn có thể sử dụng Balena Etcher để thực hiện việc này. Tải về tại đây.

Etcher rất dễ sử dụng. Chèn thẻ micro SD của bạn và ghi phần mềm Raspiblitz (.img file) vào thẻ SD.

![image](assets/6.webp)

![image](assets/7.webp)

![image](assets/8.webp)

![image](assets/9.webp)

Khi hoàn tất, ổ đĩa sẽ không còn đọc được. Bạn có thể nhận được một thông báo lỗi từ hệ điều hành, và ổ đĩa sẽ biến mất khỏi màn hình desktop. Rút thẻ ra.

## Bước 5: Thiết lập Pi và chèn thẻ SD

Các bộ phận (vỏ không được hiển thị):

![image](assets/10.webp)

![image](assets/11.webp)

Kết nối cáp ethernet, và cổng USB của ổ cứng (chưa kết nối nguồn). Tránh kết nối vào cổng USB màu xanh ở giữa. Đó là USB 3. Sử dụng cổng USB 2, mặc dù ổ đĩa có thể hỗ trợ USB 3 (đáng tin cậy hơn).

![image](assets/12.webp)

Thẻ micro SD được chèn vào đây:

![image](assets/13.webp)

Cuối cùng, kết nối nguồn:

![image](assets/14.webp)

## Bước 6: Tìm địa chỉ IP của Pi

Bạn không cần một màn hình với Raspiblitz. Tuy nhiên, bạn cần một máy tính khác trên mạng nhà. Nếu Pi của bạn không được kết nối qua ethernet, và bạn muốn dùng WiFi, việc tìm địa chỉ IP đòi hỏi một số kỹ năng máy tính. Xin lỗi, tôi không thể giúp bạn. Bạn cần một kết nối ethernet. (Vấn đề xuất phát từ việc cần truy cập vào màn hình và hệ điều hành để kết nối WiFi và nhập mật khẩu.)

Kiểm tra router của bạn, để xem danh sách tất cả các địa chỉ IP của tất cả các thiết bị được kết nối.
Tôi đã nhập 192.168.0.1 vào trình duyệt (theo hướng dẫn đi kèm với router của mình), đăng nhập và có thể thấy thiết bị của mình với địa chỉ IP là 192.168.0.191. Lưu ý rằng các địa chỉ IP này không hiển thị công khai trên internet (chúng được kết nối qua router trước), chúng chỉ là các bộ nhận dạng cho các thiết bị trong mạng gia đình của bạn.
Việc tìm kiếm địa chỉ IP là rất quan trọng.

> CẬP NHẬT: bạn có thể sử dụng terminal trên máy Mac hoặc Linux để tìm địa chỉ IP của tất cả các thiết bị kết nối Ethernet trên mạng gia đình bằng lệnh “arp -a”. Kết quả không đẹp mắt như những gì router hiển thị, nhưng tất cả thông tin bạn cần đều ở đó. Nếu không rõ đâu là Pi, hãy thử và sai.

## Bước 7: SSH vào Pi

Nhớ đặt thẻ SD vào Pi trước khi bật nó lên. Đợi vài phút, sau đó trên một máy Linux/Mac khác, mở terminal.

Đối với Mac/Linux, trong terminal gõ:

```bash
ssh admin@Địa_chỉ_IP_của_Pi_của_bạn
```

Đối với Windows, bạn sẽ cần cài đặt putty để ssh vào Pi. Gõ lệnh giống như trên.

Lần đầu tiên bạn thực hiện điều này, hoặc bất cứ khi nào bạn thay đổi OS của Pi bằng cách thay đổi thẻ SD, bạn có thể hoặc không nhận được lỗi này…

![hình ảnh](assets/15.webp)

Cách để sửa lỗi là điều hướng đến nơi chứa file “known_hosts” (lỗi sẽ cho bạn biết), và xóa nó. Lệnh là "rm known_hosts"

Sau đó, lặp lại lệnh ssh để đăng nhập. Điều này sẽ xảy ra…

![hình ảnh](assets/16.webp)

Gõ yes (toàn bộ từ) để tiếp tục.

Nếu thành công, bạn sẽ được yêu cầu nhập mật khẩu. Đây không phải là mật khẩu cho máy tính của bạn, mà là cho raspiblitz. Mật khẩu chung là “raspiblitz”, và bạn sẽ thay đổi nó sau. Cửa sổ terminal sẽ chuyển sang màu xanh và bạn sẽ có các tùy chọn menu giống như menu DOS cũ. Di chuyển bằng phím mũi tên hoặc chuột.

![hình ảnh](assets/17.webp)

Theo dõi các hướng dẫn, thiết lập mật khẩu của bạn, sau đó nó sẽ phát hiện ổ cứng của bạn và đưa ra lựa chọn để định dạng nếu cần.

Sau đó bạn sẽ được hỏi nếu muốn sao chép dữ liệu blockchain từ nguồn khác hoặc tải lại nó. Việc sao chép là một quá trình học và hướng dẫn khá tốt, và tốt để giữ bên mình….

![hình ảnh](assets/18.webp)

Cách đơn giản nhưng chậm hơn là tải toàn bộ chuỗi từ đầu…

![hình ảnh](assets/19.webp)

Nhiều văn bản sẽ chạy qua màn hình terminal. Bạn có thể nhầm lẫn nó với quá trình tải xuống blockchain, nhưng tôi thấy, nó giống như đang tạo một khóa riêng tư cho giao tiếp.

Sau đó các tùy chọn về lightning xuất hiện.

![hình ảnh](assets/20.webp)

Tạo một mật khẩu mới để khóa ví lightning của bạn, sau đó một ví mới sẽ được tạo và bạn sẽ được cung cấp 24 từ để ghi lại…

![hình ảnh](assets/21.webp)

Hãy chắc chắn bạn ghi chúng lại và giữ chúng an toàn. Tôi đã nghe về một người không làm vậy vì anh ta không dự định sử dụng lightning, nhưng sau đó một năm quyết định sử dụng nó, và mở các kênh. Sau đó nhận ra rằng từ của mình không được sao lưu, và tôi nhớ là không thể trích xuất lại các từ từ thiết bị, anh ta phải đóng tất cả các kênh của mình và bắt đầu lại. Anh ta thoát khỏi nó, nhưng người khác có thể không may mắn như vậy.

Theo sau đó, vài phút văn bản cuộn xuống cửa sổ terminal. Sau đó…

![hình ảnh](assets/22.webp)
Bạn sẽ bị đăng xuất khỏi phiên ssh. Đăng nhập lại, lần này với mật khẩu mới của bạn, mật khẩu A. Một khi vào được, bạn sẽ được yêu cầu nhập mật khẩu C để mở khóa ví lightning của mình.

Bây giờ chúng ta chờ đợi. Hẹn gặp lại sau 2 tuần. Bạn có thể đóng cửa sổ terminal, nó không ảnh hưởng gì đến Pi, chỉ là một cửa sổ giao tiếp mà thôi.

![hình ảnh](assets/23.webp)

Nếu vì bất kỳ lý do gì, bạn muốn tắt Pi trước khi blockchain hoàn tất việc tải xuống, điều đó không sao miễn là bạn thực hiện đúng cách. Blockchain sẽ tiếp tục tải xuống từ nơi nó dừng lại một khi bạn kết nối lại.

Nhấn CTRL+c để thoát khỏi màn hình xanh. Bạn sẽ truy cập vào terminal Linux của Pi. Tại đây, bạn có thể gõ “menu” để tải màn hình sau, và từ đó bạn có thể tắt nguồn của Pi.

![hình ảnh](assets/24.webp)

HƯỚNG DẪN kết thúc

Vậy là từ bây giờ, node của bạn đã sẵn sàng hoạt động. Nếu bạn vẫn cần hỗ trợ thêm để tìm hiểu thêm các tùy chọn, hãy tham khảo github để biết thêm hướng dẫn và hướng dẫn https://github.com/raspiblitz/raspiblitz#feature-documentation