---
name: Nmap
description: Master Nmap để lập bản đồ mạng và quét lỗ hổng
---

![cover](assets/cover.webp)



*Hướng dẫn này dựa trên nội dung gốc của Mickael Dorigny được đăng trên [IT-Connect](https://www.it-connect.fr/). Giấy phép [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Văn bản gốc đã được chỉnh sửa.*



___



Chào mừng bạn đến với hướng dẫn cơ bản về Nmap, được thiết kế dành cho bất kỳ ai muốn thành thạo công cụ quét mạng mạnh mẽ này. Mục đích là cung cấp cho bạn kiến thức cơ bản cần thiết để sử dụng Nmap hiệu quả hàng ngày.



Nmap là một công cụ đa năng, được các chuyên gia CNTT, mạng và an ninh mạng sử dụng rộng rãi để chẩn đoán, phát hiện mạng và kiểm tra bảo mật. Hướng dẫn này dành cho những người mới bắt đầu và muốn tìm hiểu những kiến thức cơ bản về Nmap. Khuyến khích người dùng có kiến thức cơ bản về quản trị hệ thống và mạng.



Bạn sẽ được học những kiến thức cơ bản về Nmap, cách thực hiện quét cổng, xác định máy chủ đang hoạt động trên mạng, phát hiện phiên bản dịch vụ và hệ điều hành, thực hiện quét lỗ hổng bảo mật, cùng nhiều nội dung khác. Mỗi phần đều có giải thích chi tiết và ví dụ thực tế giúp bạn nắm vững cách sử dụng Nmap trong nhiều bối cảnh khác nhau.



Sau khi đọc xong hướng dẫn này, bạn sẽ hiểu rõ về Nmap và có thể sử dụng nó hiệu quả để cải thiện bảo mật và quản lý mạng của mình. Chúc bạn đọc vui vẻ.



## 1 - Giới thiệu về Nmap: Nmap là gì?



### I. Trình bày



Trong phần đầu tiên này, chúng ta sẽ tìm hiểu về công cụ quét mạng Nmap. Chúng ta sẽ xem xét khóa Elements mà bạn cần biết về công cụ này và cách thức hoạt động chung của nó. Điều này sẽ giúp chúng ta hiểu rõ hơn phần còn lại của hướng dẫn.



### II. Giới thiệu công cụ Nmap



Nmap, viết tắt của _Network Mapper_, là một công cụ mã nguồn mở miễn phí được sử dụng để **khám phá, lập bản đồ và kiểm tra bảo mật mạng**. Công cụ này cũng có thể được sử dụng cho các tác vụ khác như **kiểm kê mạng, chẩn đoán hoặc giám sát**.



Nó có thể xác định xem các máy chủ trên mạng mục tiêu có đang hoạt động và có thể truy cập được hay không, dịch vụ mạng nào đang bị tấn công, phiên bản và công nghệ nào đang được sử dụng, và các thông tin phân tích hữu ích khác. Nmap có thể được sử dụng để quét một dịch vụ duy nhất trên một máy cụ thể, hoặc trên các vùng rộng lớn của mạng, lên đến toàn bộ Internet.



Nmap có nhiều điểm mạnh:





- **Mạnh mẽ và linh hoạt**: Nmap có thể quét các mạng lớn và sử dụng các kỹ thuật phát hiện tiên tiến. Nó hỗ trợ UDP, TCP, ICMP, IPv4 và IPv6, đồng thời có thể thực hiện phát hiện phiên bản, quét lỗ hổng hoặc tương tác theo giao thức cụ thể. Kiến trúc của nó được thiết kế theo dạng mô-đun, đặc biệt là nhờ các tập lệnh NSE (Nmap Scripting Engine), mà chúng ta sẽ tìm hiểu sau trong hướng dẫn này.
- **Dễ sử dụng**: tài liệu chính thức rất phong phú và chất lượng cao. Ngoài ra còn có nhiều tài nguyên cộng đồng để giúp bạn bắt đầu.
- **Độ phổ biến và tuổi thọ**: Nmap đã là một công cụ tham khảo trong lĩnh vực này kể từ năm 1998. Phiên bản hiện tại, tại thời điểm cập nhật này, là 7.95. Mặc dù có nhiều công cụ khác cho các tác vụ cụ thể, Nmap vẫn là công cụ không thể thiếu cho việc lập bản đồ và phân tích mạng.



**Nmap tại rạp chiếu phim**



Nmap là một trong số ít công cụ bảo mật được công chúng biết đến rộng rãi. Nó xuất hiện trong bộ phim _Matrix Reloaded_, trong một cảnh phim mang tính biểu tượng khi Trinity sử dụng nó để hack vào một hệ thống:



![nmap-image](assets/fr/01.webp)



ma trận: Cảnh được tải lại có Nmap



Ông cũng xuất hiện trong nhiều tác phẩm điện ảnh khác.



**Nhận xét**



Với tư cách là quản trị viên hệ thống, sau đó là kiểm toán viên an ninh mạng và chuyên gia kiểm thử thâm nhập, **Tôi sử dụng Nmap hầu như hàng ngày** và tôi **thường xuyên giới thiệu** công cụ này cho các quản trị viên hệ thống muốn tăng cường khả năng kiểm soát mạng và cải thiện khả năng chẩn đoán của họ.



### III. Hoạt động cấp cao



Nmap có sẵn cho Linux, Windows và macOS. Nó chủ yếu được viết bằng C, C++ và Lua (dành cho các tập lệnh NSE). Nó chủ yếu được sử dụng trên dòng lệnh, mặc dù các giao diện đồ họa như Zenmap cũng có sẵn. Tuy nhiên, chúng tôi khuyên bạn nên bắt đầu với dòng lệnh để hiểu rõ hơn cách thức hoạt động của nó.



Một ví dụ đơn giản:



```
nmap 192.168.10.13 10.10.10.0/24 -sV -sC --top-ports 250
```



Lệnh này sẽ được giải thích chi tiết sau. Trong hướng dẫn này, chúng ta sẽ sử dụng Nmap trên Linux, nhưng cách sử dụng cũng tương tự trên các hệ thống khác. Trên Windows, Nmap dựa vào thư viện **Npcap** (thay thế WinPcap hiện đã lỗi thời) để bắt và đưa các gói tin mạng vào.



Nmap được sử dụng như một tệp nhị phân thông thường, chẳng hạn như `ls` hoặc `ip`. Một số tính năng nâng cao có thể yêu cầu quyền cao hơn, vì công cụ này đôi khi thao túng các gói tin theo những cách không thông thường để kích hoạt các phản ứng cụ thể trên hệ thống mục tiêu (đặc biệt là để phát hiện dịch vụ hoặc lỗ hổng).



### IV. Tác động của việc sử dụng Nmap



Trước khi sử dụng Nmap, điều quan trọng là phải nhận thức được tác động tiềm ẩn của nó đối với mạng và hệ thống:





- Nó có thể gửi **hàng nghìn hoặc thậm chí hàng triệu gói tin** trong một khoảng thời gian ngắn, có thể làm quá tải một số cơ sở hạ tầng mạng.
- Nó có thể generate **các gói tin không đúng định dạng hoặc không chuẩn**, có khả năng làm gián đoạn một số thiết bị (đặc biệt là các hệ thống công nghiệp).
- Nó có thể tạo ra **hành vi giống như tấn công**, có thể kích hoạt cảnh báo trong các hệ thống bảo mật (tường lửa, IDS/IPS, v.v.).



Nhìn chung, **Nmap là một công cụ rất dễ sử dụng**, vì nó tạo ra rất nhiều lưu lượng truy cập để trích xuất càng nhiều thông tin càng tốt. Do đó, bạn nên hiểu rõ cách thức hoạt động của nó trước khi sử dụng trên các môi trường nhạy cảm hoặc môi trường sản xuất.



### V. Kết luận



Phần này giới thiệu Nmap và các tính năng chính của nó. Chúng ta đã thấy rằng đây là một công cụ lập bản đồ mạng thiết yếu, mạnh mẽ và linh hoạt. Chúng tôi cũng đã thảo luận về cách thức hoạt động và các biện pháp phòng ngừa cần thiết khi sử dụng Nmap, để làm nền tảng cho các phần tiếp theo của hướng dẫn.



## 2 - Tại sao nên sử dụng Nmap?



### I. Trình bày



Trong phần này, chúng ta sẽ xem xét những ứng dụng chính của công cụ quét mạng Nmap. Chúng ta sẽ thấy rằng đây là một công cụ được sử dụng rộng rãi trong nhiều bối cảnh và ngành nghề, và việc sở hữu nó trong bộ công cụ của bạn và biết cách sử dụng thành thạo chắc chắn là một kỹ năng hữu ích.



### II. Sử dụng Nmap để chẩn đoán và giám sát



Nmap có thể được sử dụng để chẩn đoán mạng và, rộng hơn, để giám sát. Tương tự như cách ping có thể được sử dụng để xác định xem hai máy chủ có đang giao tiếp hay không, Nmap có thể được sử dụng để nhanh chóng xác định xem một máy chủ có đang hoạt động hay không, hoặc một dịch vụ cụ thể có đang hoạt động hay không. Nhờ [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/ "Nmap"), chúng ta có thể thu thập dữ liệu chính xác về thời gian phản hồi của máy chủ, tuyến đường mà các gói tin đi qua, phản hồi của một dịch vụ cụ thể, v.v.



Ví dụ, lệnh và kết quả sau đây có thể được sử dụng để nhanh chóng tìm ra liệu máy chủ web trên máy chủ **192.168.1.18** có đang hoạt động và phản hồi chính xác hay không:



```
nmap --open -p 80 192.168.1.18
```



![nmap-image](assets/fr/02.webp)



*Sử dụng Nmap để lấy trạng thái dịch vụ web từ máy chủ từ xa.*



Vì vậy, việc sử dụng Nmap không chỉ đơn thuần là "kiểm tra ping" nổi tiếng trong giai đoạn gỡ lỗi hoặc chẩn đoán. Chúng ta sẽ thấy sau này Nmap sử dụng một số phương pháp để xác định dịch vụ nào đang lắng nghe trên một cổng nhất định, bao gồm cả phiên bản của nó.



### III. Sử dụng Nmap để lập bản đồ mạng



Là một _Network Mapper_, mục tiêu chính của công cụ này là lập bản đồ mạng. Nó có thể được sử dụng trong mạng cục bộ hoặc trên nhiều mạng, mạng con và VLAN, để liệt kê tất cả các máy chủ và dịch vụ có thể truy cập. Nmap giúp công việc này nhanh hơn và hiệu quả hơn nhiều so với bất kỳ phương pháp thủ công nào.



Ví dụ, lệnh sau có thể được sử dụng để nhanh chóng xác định máy chủ đang hoạt động trên mạng **192.168.1.0/24**:



```
nmap -sn 192.168.1.0/24
```



*Lưu ý: tùy chọn `-sP` đã lỗi thời và đã được thay thế bằng `-sn`.*



![nmap-image](assets/fr/03.webp)



*Sử dụng Nmap để khám phá các máy chủ có thể truy cập trên mạng*



Chúng ta sẽ thấy sau rằng Nmap sử dụng một số phương pháp để xác định xem máy chủ có được coi là "hoạt động" hay không, ngay cả khi máy chủ đó không cung cấp bất kỳ dịch vụ nào.



### IV. Sử dụng Nmap để đánh giá chính sách lọc



Nmap có lợi thế là mang tính thực tế: kết quả của nó cho phép thiết lập những phát hiện cụ thể, không giống như bất kỳ tài liệu kiến trúc hay chính sách lọc nào. Đây là một công cụ quan trọng để đánh giá hiệu quả của việc phân vùng hệ thống thông tin, vì nó cho phép bạn **xác minh xem chính sách lọc có thực sự được áp dụng hay không**.



Trong mạng doanh nghiệp, thông lệ tốt nhất là phân đoạn hệ thống theo vai trò, mức độ quan trọng hoặc vị trí của chúng. Các quy tắc lọc (thường được triển khai thông qua tường lửa) phải hạn chế giao tiếp giữa các vùng. Tuy nhiên, những cấu hình này thường phức tạp và dễ xảy ra lỗi.



Vì vậy, để xác thực chính sách đã được tuân thủ, không gì hiệu quả hơn một bài kiểm tra cụ thể. Ví dụ: bạn có thể kiểm tra xem các dịch vụ quản trị nhạy cảm (SSH, WinRM, MSSQL, MySQL, v.v.) có thể truy cập được từ vùng người dùng hay không.



Việc sử dụng **Nmap để kiểm tra chính sách lọc** cần được thực hiện một cách có hệ thống trước khi chính sách đó được đưa vào triển khai. Đáng tiếc là việc kiểm tra này thường bị bỏ qua.



Theo kinh nghiệm của tôi, nhiều lỗi cấu hình không được phát hiện nếu không có các bài kiểm tra xác thực. Một lỗi đơn giản trong dải IP hoặc một quy tắc sơ suất có thể khiến một vùng được cho là bị cô lập trở nên dễ bị tấn công.



### V. Sử dụng Nmap để kiểm tra bảo mật và thử nghiệm xâm nhập



Nmap có **nhiều tính năng hữu ích cho việc đánh giá bảo mật**, kiểm tra thâm nhập (pentest) và thật không may là cũng có cả tính năng dành cho kẻ tấn công.



Chức năng phát hiện mạng rất quan trọng đối với kẻ tấn công, những kẻ cần hiểu rõ cấu trúc mạng sau khi xâm nhập ban đầu. Tuy nhiên, Nmap còn cung cấp nhiều hơn thế nữa: nó tích hợp một công cụ viết kịch bản, **nhiều công cụ trong số đó được dành riêng cho việc phát hiện lỗ hổng**.



Ví dụ, lệnh này có thể được sử dụng để kiểm tra xem dịch vụ FTP có cho phép kết nối ẩn danh hay không mà không cần phải kết nối thủ công:



```
nmap --script ftp-anon -p 21 192.168.1.18
```



![nmap-image](assets/fr/04.webp)



*Sử dụng tập lệnh NSE để kiểm tra xác thực FTP ẩn danh thông qua Nmap.*



Phát hiện lỗ hổng bảo mật của Nmap là một trong những bước đầu tiên trong quá trình kiểm tra hoặc kiểm thử xâm nhập. Nó cho phép bạn nhanh chóng xác định các điểm yếu và tối ưu hóa nỗ lực phân tích.



Nhưng hãy lưu ý: **các công cụ quét lỗ hổng bảo mật có giới hạn**. Nmap chỉ bao phủ một phần nhỏ các mối đe dọa và không đảm bảo hệ thống an toàn nếu không phát hiện ra vấn đề nào. Do đó, điều quan trọng là phải **hiểu cách các tập lệnh được sử dụng hoạt động** và không nên chỉ dựa vào phán đoán của chúng.



### VI. Kết luận



Chúng ta đã thấy rằng việc thành thạo Nmap có thể bao quát nhiều trường hợp sử dụng, từ chẩn đoán và giám sát đến lập bản đồ, đánh giá chính sách bảo mật và quét lỗ hổng. Trong phần tiếp theo, chúng ta sẽ đi sâu vào chi tiết và cài đặt Nmap.




## 3 - Cài đặt và cấu hình Nmap



### I. Trình bày



Trong phần này, chúng ta sẽ tìm hiểu cách cài đặt công cụ quét mạng Nmap trên hệ điều hành Linux và Windows. Cuối phần này, chúng ta sẽ có mọi thứ cần thiết để bắt đầu sử dụng Nmap cho các mô-đun sau này. Cuối cùng, chúng ta sẽ xem xét những đặc quyền nào cần thiết khi sử dụng và lý do tại sao.



### II. Cài đặt Nmap trên Linux



Nmap ban đầu được thiết kế để chạy trên các hệ điều hành GNU/Linux. Nhờ vào độ bền và tính phổ biến của nó, bạn sẽ tìm thấy nó trong tất cả các kho lưu trữ chính thức của các bản phân phối Unix chính. Trong hướng dẫn này, tôi sẽ sử dụng hệ điều hành dựa trên Debian [Kali Linux](https://www.it-connect.fr/cours/debuter-avec-kali-linux/ "Kali Linux"). Nhưng bạn có thể sử dụng nó theo cách hoàn toàn tương tự trên các hệ điều hành Debian, CentOS, Red Hat hay bất kỳ hệ điều hành nào khác!



Trên Debian, để kiểm tra xem Nmap có trong kho lưu trữ hiện tại của bạn hay không, bạn có thể sử dụng lệnh sau:



```
# Debian and derivatives
$ sudo apt search ^nmap$
Sorting... Done
Full Text Search... Done
nmap/kali-rolling,now 7.94+git20230807.3be01efb1+dfsg-2+kali1 amd64
The Network Mapper

# Red Hat and derivatives
$ dnf search '^nmap$'
```



Câu trả lời ở đây cho thấy rõ ràng rằng gói "nmap" tồn tại trong các kho lưu trữ (ở đây là kho lưu trữ của Kali [Linux](https://www.it-connect.fr/cours-tutoriels/administration-systemes/linux/ "Linux")). Từ bây giờ, bạn có thể cài đặt Nmap thông qua các lệnh cài đặt thông thường, hiện tại không có gì phải lo lắng 🙂:



```
# Debian and derivatives
sudo apt install nmap

# Red Hat and derivatives
sudo dnf install nmap
```



Để kiểm tra xem Nmap đã được cài đặt đúng chưa, chúng tôi sẽ hiển thị phiên bản của nó:



```
nmap --version
```



Sau đây là kết quả mong đợi:



![nmap-image](assets/fr/05.webp)



kết quả hiển thị phiên bản hiện tại của Nmap._



Lưu ý sự hiện diện của thư viện "libpcap" (_Packet Capture Library_) và phiên bản của nó trong màn hình này. Cũng được Wireshark sử dụng, "libpcap" được Nmap sử dụng để tạo và thao tác các gói tin cũng như lắng nghe lưu lượng mạng.



### III Cài đặt Nmap trên Windows



Để cài đặt trên hệ điều hành Windows, hãy bắt đầu bằng cách tải xuống tệp nhị phân từ trang web chính thức (và không phải trang web nào khác!):





- Trang tải xuống Nmap trên trang web chính thức: [https://nmap.org/download.html#windows](https://nmap.org/download.html#windows)




Sau đó, bạn sẽ cần tải xuống tệp nhị phân có tên `nmap-<VERSION>-setup.exe`:



![nmap-image](assets/fr/06.webp)



trang tải xuống nhị phân cài đặt nmap cho Windows



Sau khi đã cài đặt tệp nhị phân này trên hệ thống, chỉ cần chạy nó để cài đặt Nmap. Quá trình cài đặt này rất đơn giản và bạn có thể giữ nguyên tất cả các tùy chọn mặc định.



Phản xạ của tôi là bỏ chọn ô "zenmap (GUI Frontend)". Đây là Interface đồ họa dành cho Nmap mà tôi không sử dụng và sẽ không được đề cập trong hướng dẫn này, nhưng bạn cứ thoải mái dùng thử khi đã thành thạo công cụ dòng lệnh Nmap!



![nmap-image](assets/fr/07.webp)



tùy chọn bỏ chọn Zenmap khi cài đặt Nmap trên Windows



Khi kết thúc quá trình cài đặt Nmap, một cài đặt thứ hai được đề xuất: đó là cài đặt thư viện "Npcap":



![nmap-image](assets/fr/08.webp)



cài đặt thư viện "Npcap" khi cài đặt Nmap trên Windows



Đây là thư viện mà Nmap dựa vào để quản lý giao tiếp mạng, tức là xây dựng, gửi và nhận các gói tin mạng. Bạn có thể đã từng gặp thư viện này nếu sử dụng Wireshark trên Windows, vì nó cũng sử dụng thư viện này và yêu cầu cài đặt.



Tương tự như Linux, bạn có thể xác thực Nmap đã được cài đặt bằng cách mở Dấu nhắc lệnh hoặc thiết bị đầu cuối [Powershell] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/ "Powershell") và nhập lệnh sau:



```
nmap --version
```



Sau đây là kết quả mong đợi:



![nmap-image](assets/fr/09.webp)



kết quả hiển thị phiên bản hiện tại của Nmap._



Nmap hiện đã được cài đặt trên Windows. Bạn có thể sử dụng nó theo cách hoàn toàn giống như trên Linux bằng cách làm theo hướng dẫn này.



### IV. Cần có đặc quyền cục bộ để sử dụng Nmap



Nhưng nhân tiện, khi sử dụng Nmap, **có cần phải có quyền cục bộ nâng cao trên hệ thống không?** Câu trả lời là: **tùy thuộc**.



Ở dạng cơ bản nhất, tức là không cần đi sâu vào việc sử dụng các tùy chọn, Nmap không nhất thiết yêu cầu quyền đặc quyền. Tuy nhiên, bạn sẽ sớm nhận ra rằng tốt hơn nên sử dụng Nmap trong ngữ cảnh đặc quyền ("root" trong Linux, "administrator" hoặc tương đương trong Windows) để có thể khai thác tối đa tiềm năng của nó, mặc dù có nguy cơ nhận được thông báo lỗi như thế này:



![nmap-image](assets/fr/10.webp)



thông báo lỗi trên Linux khi tùy chọn Nmap yêu cầu quyền root._



Dù trên Linux hay Windows, có nhiều trường hợp Nmap sẽ yêu cầu bạn cấp quyền truy cập đặc quyền. Những lý do chính như sau (danh sách chưa đầy đủ):





- **Xây dựng các gói tin mạng "thô"**: Nmap có khả năng thực hiện nhiều phương pháp quét, bao gồm cả việc xử lý và xây dựng gói tin nâng cao. Ví dụ, trường hợp này xảy ra khi chúng ta muốn thực hiện quét TCP SYN, vốn không tuân thủ cơ chế bắt tay ba bước cổ điển của các trao đổi TCP. Để làm được điều này, Nmap cần sử dụng các hàm khác ngoài các hàm gốc của hệ điều hành, vốn chỉ biết cách tuân thủ các thông lệ tốt trong giao tiếp mạng (nó gọi đến các thư viện "Npcap" và "libcap" đã đề cập ở trên). Chính vì Nmap không hoạt động theo cách "chuẩn" nên nó có thể suy ra một số thông tin nhất định về hệ





- **Nghe lưu lượng mạng**: một số tùy chọn của Nmap yêu cầu nó phải nghe lưu lượng mạng để thu thập thông tin nhất định. Thao tác này được coi là nhạy cảm trên các hệ điều hành, vì nó cũng cho phép bạn nghe lén các giao tiếp của các ứng dụng khác trên hệ thống. Cũng giống như Wireshark, Nmap cần các đặc quyền cụ thể để thực hiện việc này, và việc này dễ dàng hơn khi bạn đang ở trong một phiên làm việc đặc quyền.





- **Nghe trên các cổng đặc quyền**: trên các hệ điều hành, các cổng từ 0 đến 1024 (cả TCP và UDP) được coi là đặc quyền, tức là chúng được dành riêng cho các mục đích sử dụng rất cụ thể và do đó được bảo vệ. Mặc dù lý do này đã lỗi thời ngày nay, nhưng vẫn cần có một số đặc quyền nhất định để nghe trên các cổng này, và Nmap có thể phải làm điều này tùy thuộc vào cách sử dụng.





- Gửi gói tin UDP: Tương tự, việc lắng nghe một ứng dụng mạng trên các cổng UDP (một giao thức không trạng thái) yêu cầu quyền đặc quyền trên hệ điều hành. Do đó, cần có một phiên đặc quyền nếu bạn muốn thực hiện quét UDP, trong đó Nmap sẽ phải lắng nghe phản hồi để phân tích các phản hồi cho các lần quét của nó.




Nói chính xác hơn, ít nhất là trên Linux, bạn có thể chạy Nmap với đầy đủ các chức năng và tùy chọn mà không cần root. Điều này đạt được bằng cách cấp quyền cho tệp nhị phân. Tuy nhiên, cách này đòi hỏi thao tác nâng cao và có thể không thực tế bằng việc chạy Nmap trực tiếp với quyền cao nhất. Ngoài ra, cách tiếp cận này ít phổ biến hơn và có thể gây ra các vấn đề bảo mật nếu cấu hình sai.



Tuy nhiên, hướng dẫn này hơi khác so với hướng dẫn Nmap của chúng tôi nên chúng tôi sẽ bỏ qua hướng dẫn này ngay bây giờ.



Trong phần còn lại của hướng dẫn này, hãy giả định rằng Nmap luôn được chạy dưới quyền "root" (từ shell với quyền "root" hoặc thông qua lệnh "sudo"), hoặc trong terminal quản trị viên trên Windows, ngay cả khi điều này không được chỉ định. Nếu không, bạn có thể gặp phải những khác biệt nhỏ nhưng đáng chú ý so với hướng dẫn.



### V. Kết luận



Vậy là xong! Nmap hiện đã được cài đặt trên hệ điều hành của chúng ta và sẵn sàng sử dụng, không cần cấu hình thêm. Phần này kết thúc phần giới thiệu và trình bày về Nmap. Tôi hy vọng nó đã khiến bạn thèm thuồng và háo hức bắt đầu thực hành.



Nghiêm túc hơn, giờ chúng ta đã hiểu rõ hơn về công cụ lập bản đồ Nmap, những ứng dụng phổ biến nhất của nó, cũng như những hạn chế của nó. Hãy cùng tìm hiểu tiếp nhé!




## 4 - Quét cổng TCP và UDP bằng Nmap



### I. Trình bày



Trong phần này, chúng ta sẽ tìm hiểu cách thực hiện quét cổng đầu tiên bằng công cụ quét mạng Nmap. Chúng ta sẽ xem cách sử dụng công cụ này để biên soạn danh sách các dịch vụ mạng được cung cấp trên máy chủ, dù sử dụng giao thức TCP hay UDP.



Từ bây giờ, hãy nhớ chỉ quét các máy chủ trong môi trường được kiểm soát mà bạn có quyền rõ ràng.





- Xin nhắc lại: [Bộ luật Hình sự: Chương III: Tấn công vào hệ thống xử lý dữ liệu tự động](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




**Nếu bạn không có giải pháp nào trong tay**, tôi khuyên bạn nên dùng các giải pháp miễn phí sau đây, chúng chính là giải pháp bạn cần!





- [Hack The Box](https://app.hackthebox.com/ "Hack The Box"): Nền tảng đào tạo hack, Hack The Box liên tục cung cấp các hệ thống dễ bị tấn công để bạn tùy ý tấn công. Có hàng trăm hệ thống, nhưng một nhóm 20 máy mới được cung cấp miễn phí quanh năm, với quyền truy cập thông qua VPN OpenVPN.





- [Vulnhub](https://www.vulnhub.com/ "Vulnhub"): Nền tảng này cung cấp nhiều hệ thống dễ bị tấn công để tải xuống, có thể sử dụng thông qua VirtualBox (cũng là một giải pháp miễn phí) hoặc các phương tiện khác. Sau khi tải xuống, không cần VPN - mọi thứ đều được thực hiện cục bộ.




Ngoài ra, bạn có thể thoải mái **tạo một máy ảo** trên hệ điều hành yêu thích và cài đặt nhiều dịch vụ khác nhau trên đó làm mục tiêu thử nghiệm. Ưu điểm ở đây là bạn cũng có thể xem những gì đang diễn ra ở phía máy chủ trong quá trình quét, đặc biệt là với Wireshark, và có thể can thiệp vào tường lửa cục bộ khi chúng tôi thực hiện các thử nghiệm nâng cao hơn.



Hãy thực tế nào!



### II. Quét các cổng TCP của máy chủ thông qua Nmap



#### A. Quét cổng TCP đầu tiên bằng Nmap



Bây giờ chúng ta sẽ thực hiện lần quét đầu tiên thông qua Nmap. Mục tiêu của chúng ta ở đây rất đơn giản: chúng ta muốn tìm hiểu những dịch vụ nào đang được máy chủ web vừa triển khai sử dụng, để xem có điều gì bất thường không, chẳng hạn như dịch vụ quản trị không thể truy cập được, hoặc cổng của một ứng dụng mà chúng ta nghĩ đã ngừng hoạt động.



Trong ví dụ của tôi, máy chủ cần quét có IP Address "192.168.1.18":



```
nmap 192.168.1.18
```



Đây là một kết quả khả thi. Chúng ta thấy kết quả trả về của Nmap cổ điển với rất nhiều thông tin:



![nmap-image](assets/fr/11.webp)



kết quả của một lần quét TCP đơn giản được thực hiện với Nmap._



Khi xem nhanh kết quả này, chúng ta có thể hiểu rằng các cổng TCP/22 và TCP/80 có thể truy cập được trên máy chủ này.



Theo mặc định, nếu bạn không yêu cầu, Nmap sẽ chỉ quét các cổng TCP.



#### B. Hiểu kết quả của một lần quét Nmap đơn giản



Tuy nhiên, chúng ta hãy tiến thêm một bước nữa để hiểu đầu ra này: mỗi dòng đều quan trọng, thứ nhất là để biết những gì vừa được thực hiện và thứ hai là để diễn giải chính xác kết quả quét.



Dòng đầu tiên về cơ bản là lời nhắc nhở về phiên bản và ngày quét (hữu ích cho việc ghi nhật ký và lưu trữ!):



```
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-29 21:59 CEST
```



Dòng thứ hai hiển thị thời điểm bắt đầu quét cho máy chủ "debian.home (192.168.1.19)". Thông tin này sẽ hữu ích khi chúng ta bắt đầu quét nhiều máy chủ cùng lúc:



```
Nmap scan report for debian.home (192.168.1.19)
```



Dòng thứ ba cho chúng ta biết rằng máy chủ đang được đề cập là "Đang hoạt động", tức là đang hoạt động:



```
Host is up (0.00022s latency).
```



Cuối cùng, Nmap thông báo cho chúng ta rằng 998 cổng TCP được xác định là đã đóng không được hiển thị trong:



```
Not shown: 998 closed tcp ports (conn-refused)
```



Điều này giúp chúng ta tiết kiệm được gần 1.000 dòng đầu ra trông như sau:



```
1/tcp closed
2/tcp closed
3/tcp closed
…
```



Cảm ơn anh ấy đã giúp chúng tôi tránh được chuyện này!



Tại sao lại là 998 cổng "đóng"? Thêm 2 cổng mở sẽ thành 1000, và đó là số cổng mà Nmap sẽ quét trong cấu hình mặc định, chứ không phải 65535 cổng TCP hiện có! Chúng ta sẽ thấy sau rằng việc này hoàn toàn có thể tùy chỉnh dễ dàng. Nhưng nếu máy chủ mục tiêu có một dịch vụ đang lắng nghe trên một cổng khá lạ, thì lần quét "mặc định" này sẽ không phát hiện ra nó.



Theo thông tin này, chúng ta tìm thấy điều thú vị nhất: một bảng được sắp xếp theo ba cột "CẢNG - TRẠNG THÁI - DỊCH VỤ":





- Cột "PORT" đầu tiên chỉ ra cổng/giao thức mục tiêu và điều quan trọng ở đây là phải xem đó là cổng TCP (`<port>/tcp`) hay UDP (`<port>/udp`).





- Cột "TRẠNG THÁI" cho biết trạng thái của dịch vụ mạng được phát hiện trên cổng này và được Nmap xác định dựa trên phản hồi nhận được. Trạng thái này có thể là "mở", "đóng", "đã lọc" hoặc "chưa biết". Chúng ta sẽ xem cách Nmap phân biệt các trạng thái khác nhau này sau.





- Cột "SERVICE" cho biết dịch vụ được hiển thị trên cổng đang đề cập. Tuy nhiên, xin lưu ý rằng chúng tôi không sử dụng tùy chọn khám phá dịch vụ đang hoạt động ở đây. Nmap dựa vào tham chiếu cục bộ giữa cổng/giao thức và dịch vụ được cho là đã được gán: tệp "/etc/services".




Nếu bạn xem tệp "/etc/services" trên hệ thống Linux, bạn sẽ thấy liên kết "port/protocol - service" tương tự như liên kết được hiển thị bởi Nmap:



![nmap-image](assets/fr/12.webp)



trích xuất nội dung của tệp "/etc/services" trên Linux._



Điều quan trọng cần hiểu là hiện tại, Nmap chưa thực hiện bất kỳ hoạt động khám phá dịch vụ nào. Ví dụ: nếu thực hiện điều này, nó sẽ không thể xác định được dịch vụ SSH đằng sau cổng TCP/80. Do đó, việc biết cách sử dụng đúng các tùy chọn là rất quan trọng - tính năng này sẽ sớm ra mắt!



Biết cách diễn giải kết quả đầu ra của Nmap là một phần quan trọng để thành thạo công cụ này. Tin tốt là kết quả đầu ra này hầu như sẽ giống nhau, bất kể bạn sử dụng tùy chọn nào.



#### C. Dưới mui xe: phân tích mạng thông qua Wireshark



Nếu bạn xem xét kỹ những gì đang diễn ra trên mạng Interface của máy chủ đang quét máy chủ, hoặc trên chính máy chủ đó, các hành động của Nmap sẽ rõ ràng hơn nhiều. Đó chính là những gì chúng ta sẽ làm ở đây.



Những gì tôi có thể cho bạn xem ở đây chỉ là một phần trong những gì hiển thị trong Wireshark. Nếu bạn muốn tìm hiểu sâu hơn, hãy tự mình chụp ảnh mạng trong quá trình quét, sau đó duyệt qua những gì đã chụp được.



Trong thử nghiệm này, máy chủ quét của tôi (192.168.1.18) và máy chủ mục tiêu (192.168.1.19) nằm trên cùng một mạng cục bộ.



Nmap bắt đầu bằng cách tìm hiểu xem máy chủ đích có đang hoạt động trên mạng cục bộ hay không bằng cách gửi yêu cầu ARP. Nếu nhận được phản hồi, Nmap sẽ biết máy chủ đang hoạt động và bắt đầu quét mạng:



![nmap-image](assets/fr/13.webp)



_Yêu cầu ARP do Nmap đưa ra để xác định xem máy chủ đích có hiện diện trên mạng cục bộ hay không._



Nếu máy chủ cần quét nằm trên mạng từ xa, Nmap sẽ bắt đầu bằng cách gửi yêu cầu ping và cố gắng tiếp cận một số cổng thường xuyên bị tấn công nhất (TCP/80, TCP/443):



![nmap-image](assets/fr/14.webp)



yêu cầu ping do Nmap đưa ra để xác định xem máy chủ mục tiêu có thể truy cập được trên mạng từ xa hay không



Nếu nhận được phản hồi cho bất kỳ thử nghiệm nào trong số này, nó sẽ coi mục tiêu là đang hoạt động.



Khi Nmap xác định mục tiêu của mình đang hoạt động, nó sẽ cố gắng phân giải tên miền của mục tiêu đó bằng máy chủ DNS được cấu hình trên card mạng:



![nmap-image](assets/fr/15.webp)



Độ phân giải dNS trên mục tiêu quét Nmap



Bây giờ Nmap đã xác định được mục tiêu và biết mục tiêu đó đang hoạt động, nó bắt đầu quét cổng TCP:



![nmap-image](assets/fr/16.webp)



Truyền gói tCP SYN và nhận RST/ACK trong quá trình quét Nmap



Để thực hiện việc này, trên mỗi cổng TCP trong phạm vi mặc định, nó sẽ **gửi các gói tin TCP SYN và chờ phản hồi**. Trong ảnh chụp màn hình ở trên, nó nhận các gói tin TCP RST/ACK từ máy chủ được quét, nghĩa là "di chuyển tiếp, không có gì để xem ở đây" - nói cách khác, các cổng này đã bị đóng. Như chúng ta đã thấy trong kết quả, điều này sẽ xảy ra với hầu hết các cổng được quét. Ngoại trừ hai trường hợp:



![nmap-image](assets/fr/17.webp)



phản hồi cho gói tin TCP SYN được gửi trên cổng 22, đang hoạt động trên mục tiêu quét



Trong ảnh chụp màn hình ở trên, chúng ta thấy một gói tin TCP SYN/ACK được gửi bởi máy chủ đích. Cổng đang hoạt động và hiển thị một dịch vụ. Nmap xác nhận đã nhận được phản hồi, sau đó chấm dứt kết nối (TCP RST/ACK). **Đây là cách nó biết rằng cổng TCP/22 đang hoạt động**.



Chúng ta đã thấy ở đây rằng Nmap tuân thủ "Bắt tay Ba Bước" khi quét mạng TCP. Vì lý do hiệu suất, có thể yêu cầu nó không phản hồi lại yêu cầu trả về từ máy chủ, nhờ đó tiết kiệm được hàng nghìn gói tin khi quét mạng lớn. Tuy nhiên, chúng ta sẽ xem xét các tùy chọn và tối ưu hóa này sau trong hướng dẫn.



Giờ đây, chúng ta đã hiểu rõ hơn về cách thực hiện quét TCP và những gì thực sự xảy ra khi thực hiện. Chúng ta cũng thấy rằng, theo mặc định, Nmap thực hiện quét cổng TCP trên một số lượng cổng giới hạn.



### III. Quét cổng UDP bằng Nmap



#### A. Quét cổng UDP đầu tiên bằng Nmap



Bây giờ, hãy cùng xem cách quét các cổng UDP của máy chủ. Như chúng ta đã thấy, theo mặc định, Nmap sẽ luôn quét các cổng TCP. Điều này có thể dẫn đến việc bỏ lỡ rất nhiều thông tin nếu chúng ta không biết.



Để nhắc lại, đối với mục đích của bài kiểm tra này, máy chủ quét của tôi (192.168.1.18) và máy chủ mục tiêu (192.168.1.19) nằm trên cùng một mạng cục bộ.



```
nmap -sU 192.168.1.19
```



Ở đây, kết quả trả về có cùng định dạng như khi quét TCP, nhưng các dịch vụ đang hoạt động được hiển thị ở dạng `<port>/UDP`, như đã yêu cầu!



![nmap-image](assets/fr/18.webp)



kết quả của một lần quét UDP đơn giản được thực hiện với Nmap._



Tùy chọn "-sU" được sử dụng để cho Nmap biết rằng bạn muốn làm việc trên UDP, thay vì TCP như mặc định.



Nhân tiện, bạn có thể nhận thấy rằng Nmap yêu cầu quyền "root" để quét UDP, như đã đề cập trước đó trong hướng dẫn.



lưu ý: Kể từ phiên bản Nmap mới nhất, bạn nên chạy quét UDP với quyền quản trị viên để đảm bảo kết quả đáng tin cậy vì một số tính năng yêu cầu quyền truy cập thô vào ổ cắm mạng._



Quá trình quét UDP có thể mất rất nhiều thời gian (1100 giây để quét 1000 cổng trong ví dụ của tôi), do UDP không có "Three Way Handshake" (bắt tay ba bước), nghĩa là Nmap sẽ đợi phản hồi cho mỗi gói tin UDP được gửi đi và chỉ xác định cổng là "đóng" nếu không có phản hồi nào sau một khoảng thời gian nhất định (timeout). Phản hồi này từ các máy chủ được quét không mang tính hệ thống và thường bị giới hạn về số lượng phản hồi mỗi giây để tránh một số cuộc tấn công khuếch đại. Điều này trái ngược với TCP, nơi máy chủ được quét sẽ phản hồi ngay lập tức, bất kể cổng đang mở hay đóng. Chúng ta sẽ xem cách tối ưu hóa điều này sau.



Khó khăn thứ hai với UDP là **các dịch vụ không phải lúc nào cũng phản hồi các gói tin đến**, đơn giản vì điều này không phải lúc nào cũng cần thiết và đó là nguyên tắc của UDP. Khi điều này xảy ra, và không nhận được thông báo ICMP "cổng không thể truy cập", dịch vụ sẽ được Nmap đánh dấu là "mở|đã lọc", như minh họa trong ảnh chụp màn hình ở trên.



#### B. Dưới mui xe: phân tích mạng thông qua Wireshark



Tương tự như quét TCP, hãy cùng xem xét kỹ hơn những gì xảy ra ở cấp độ mạng trong quá trình quét UDP bằng cách sử dụng phân tích Wireshark. Cách Nmap xác định máy chủ có hoạt động hay không cũng tương tự.



Sự khác biệt thực sự duy nhất khi quét UDP là Nmap sẽ không đợi "Bắt tay ba bước" vì cơ chế này không tồn tại trong UDP (giao thức không trạng thái):



![nmap-image](assets/fr/19.webp)



Truyền gói tin uDP và tiếp nhận ICMP (cổng không thể truy cập) trong quá trình quét Nmap



Chúng ta có thể thấy trên ảnh chụp màn hình ở trên rằng Nmap sẽ gửi một số lượng lớn các gói tin UDP và hầu hết trong số chúng đều nhận được gói tin ICMP "Destination unreachable (Port unreachable)" để phản hồi. Điều này là bình thường, vì đây là phản hồi phù hợp được định nghĩa bởi [RFC 1122](https://www.freesoft.org/CIE/RFC/1122/41.htm "RFC 1122") khi một cổng UDP không thể truy cập:



![nmap-image](assets/fr/20.webp)



trích từ RFC 1122._



Chúng ta hãy xem xét kỹ hơn bản ghi Wireshark này, bản ghi này cho thấy **ba tình huống có thể xảy ra** trong UDP:



![nmap-image](assets/fr/21.webp)



chụp mạng trong quá trình quét UDP trên các cổng khác nhau bằng Nmap._



Ba trường hợp như sau:





- Exchange đầu tiên bao gồm các gói số 3, 4 và 8, 9. Nmap gửi các gói UDP trên cổng SNMP cổ điển và do đó **xây dựng trước các gói tuân thủ giao thức**. Sau đó, nó nhận được phản hồi từ máy chủ (các gói số 8 và 9). Kết quả: Nmap đã nhận được phản hồi, dịch vụ "mở".





- Exchange thứ hai bao gồm các gói 6 và 7. Nmap gửi một gói UDP "rỗng" (không có cấu trúc giao thức) đến cổng UDP/165 và nhận được một gói ICMP trả lời: "Không thể truy cập đích (Port unreachable)". Kết quả: Nmap đã nhận được phản hồi (tiêu cực), máy chủ đang hoạt động, nhưng dịch vụ mà nó cố gắng truy cập không hoạt động trên cổng này, cổng này sẽ được đánh dấu là "đã đóng".





- Exchange cuối cùng bao gồm gói tin số 12: Nmap gửi một gói tin UDP "rỗng" đến cổng UDP/1235. Không có phản hồi, thậm chí không có lời từ chối rõ ràng từ máy chủ được quét. Kết quả: Nmap đánh dấu cổng là "mở|đã lọc", vì nó không thể xác định liệu điều này là do tường lửa, được cấu hình để không phản hồi, hay do dịch vụ UDP đang hoạt động nhưng vẫn không trả về phản hồi (không bắt buộc trong UDP).




Sau đây là kết quả được Nmap hiển thị sau ba trường hợp sau:



![nmap-image](assets/fr/22.webp)



kết quả có thể có của quá trình quét UDP được thực hiện thông qua Nmap._



Giờ đây, chúng ta đã hiểu rõ hơn về cách thực hiện quét UDP và những gì thực sự xảy ra khi thực hiện. Cho đến nay, chúng ta chỉ sử dụng Nmap một cách rất đơn giản, chưa thực sự quyết định quét cổng nào, nhưng điều đó sắp thay đổi!



### IV. Tinh chỉnh quét cổng với Nmap



#### A. Nhắc lại về hành vi mặc định của Nmap



Như chúng ta đã thấy, Nmap tự động chọn số lượng và cổng để quét nếu bạn không chỉ định bất kỳ tùy chọn nào. Đây là cấu hình "mặc định" được Nmap sử dụng khi bạn không cho nó biết chính xác phải làm gì. Các tùy chọn mặc định này được thiết kế để cung cấp ý tưởng về các cổng chính được hiển thị, được chọn theo tần suất hiển thị (các cổng phổ biến nhất hoặc thường xuyên nhất) thay vì theo thứ tự số (cổng 1, 2, 3, v.v.) và cũng để tránh việc bắt đầu quét 65535 cổng có thể nếu bạn không chỉ định các tùy chọn phù hợp, điều này sẽ quá dài dòng và rườm rà cho một trường hợp sử dụng "mặc định".



**Những cổng này được chọn như thế nào?**



1000 cổng được quét ở chế độ mặc định được chọn dựa trên tần suất xuất hiện của chúng. Các số liệu thống kê này được Nmap duy trì và cập nhật theo cùng cách với bản thân tệp nhị phân và các tập lệnh (mô-đun) của nó. Bạn có thể tự xem các số liệu thống kê này trong tệp "/usr/shares/nmap/nmap-services":



![nmap-image](assets/fr/23.webp)



được trích xuất từ tệp "/usr/shares/nmap/nmap-services"._



Ở đây, trong cột thứ ba, chúng ta thấy những gì trông giống như xác suất (từ 0 đến 1) hoặc phân phối phần trăm. Đây là tần suất xuất hiện của từng cặp cổng/giao thức. Chúng ta có thể thấy rằng các cổng được biết đến nhiều nhất (FTP, SSH, TELNET và SMTP trong đoạn trích này) có giá trị cao hơn nhiều so với các cổng khác.



#### B. Chỉ định chính xác các cổng mục tiêu để quét Nmap



Tuy nhiên, trong thực tế, chúng ta có thể chỉ cần quét một cổng cụ thể, hoặc nhiều cổng, hoặc một phạm vi cổng cụ thể. Nmap giúp bạn dễ dàng thực hiện điều đó, theo cách thống nhất cho cả quét UDP và TCP.



**Quét một cổng cụ thể thông qua Nmap**



Nếu chúng ta muốn quét một cổng duy nhất chứ không phải 1000 cổng, chúng ta có thể chỉ định cổng này thông qua tùy chọn "-p" hoặc "--port" của Nmap:



```
# Scan a single TCP port with Nmap
nmap 192.168.1.19 -p 80

# Scan a single UDP port with Nmap
nmap -sU 192.168.1.19 -p 161
```



Nhờ đó, quá trình quét tự nhiên sẽ nhanh hơn nhiều và Nmap sẽ chỉ phát ra các gói tin cần thiết để phát hiện máy chủ có hoạt động hay không, sau đó xác định xem cổng được chỉ định có thể truy cập được hay không. Điều này giúp tiết kiệm thời gian nếu bạn chỉ muốn chạy thử nghiệm nhanh để xem dịch vụ web trên trang web giới thiệu của mình có còn hoạt động hay không.



**Quét nhiều cổng thông qua Nmap**



Tương tự như vậy, chúng ta có thể chỉ định nhiều cổng cho Nmap bằng cách sử dụng cùng một tùy chọn và nối các cổng đã chỉ định bằng dấu phẩy:



```

# Scan several TCP ports with Nmap

nmap 192.168.1.19 -p 80,10999,22,23,1345

# Scan several UDP ports with Nmap

nmap -sU 192.168.1.19 -p 161,23,69

```



Bất kể thứ tự nào, Nmap sẽ kiểm tra tất cả các cổng này, và chỉ những cổng trên máy chủ mục tiêu. Bạn sẽ thấy kết quả đầu ra của Nmap **cho chúng ta biết rõ ràng tất cả các cổng và trạng thái của chúng**, ngay cả khi chúng đã "đóng". Không giống như hành vi mặc định, khi toàn bộ kết quả đầu ra này sẽ chiếm quá nhiều dung lượng:



![nmap-image](assets/fr/24.webp)



*Kết quả quét Nmap TCP trên các cổng được chỉ định.*



**Quét một loạt các cổng**



Nếu số lượng cổng bạn muốn quét quá lớn, bạn có thể chỉ định chúng theo phạm vi, ví dụ:



```

# Scan TCP ports from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 1000-2000

# Scan UDP ports from 1000 to 2000 with Nmap

nmap -sU 192.168.1.19 -p 100-150

```



Tất nhiên, bạn có thể kết hợp tùy theo ý thích, ví dụ:



```

# Scan TCP ports 22,80, 3389 and from 1000 to 2000 with Nmap

nmap 192.168.1.19 -p 22,80,1000-2000,3389

```



**Quét cổng TCP và UDP**



Bạn cũng có thể thực hiện quét UDP và TCP cùng lúc trên các cổng đã chọn:



```

# Scan the list of 1000 default ports, in TCP and UDP

sudo nmap 192.168.1.19 -sT -sU

# Scan only UDP/161 and TCP/22

sudo nmap 192.168.1.19 -sT -sU -p U:161,T:22

```



Trong ví dụ cuối cùng này, bạn sẽ thấy sự hiện diện của "U:" để chỉ cổng UDP và "T:" để chỉ cổng TCP. Dưới đây là kết quả có thể có của kiểu quét này:



![nmap-image](assets/fr/25.webp)



*Kết quả quét cổng TCP và UDP bằng Nmap.*



Đây thực sự là một cách thú vị để tùy chỉnh bản quét của bạn!



**Quét tất cả các cổng**



Cuối cùng, bạn có thể chỉ định phạm vi lớn hơn hoặc nhỏ hơn nhiều cho Nmap. Chúng ta đã thấy danh sách mặc định được Nmap chọn chứa 1000 cổng. Chúng ta cũng có thể yêu cầu 100 cổng thường xuyên nhất, hoặc 200 cổng hàng đầu, bằng cách sử dụng tùy chọn "--top-ports":



```

# Scan the top 100 most common ports with Nmap

nmap 192.168.1.19 --top-ports 100

# Scan the top 200 most common ports with Nmap

nmap 192.168.1.19 --top-ports 200

```



Cuối cùng, chúng ta có thể yêu cầu nó quét tất cả các cổng có thể (tất cả 65535), bằng cách sử dụng ký hiệu "-p-":



```

# Scan all TCP ports from 1 to 65535 with Nmap

nmap 192.168.1.19 -p-

```



Cách sau sẽ mất nhiều thời gian hơn, đặc biệt là với UDP, nhưng bạn chắc chắn sẽ không bỏ lỡ bất kỳ cổng mở nào.



*Lưu ý: Tùy chọn "-p-" là phương pháp được khuyến nghị để quét tất cả các cổng TCP. Đối với quét UDP, nên giới hạn số lượng cổng vì lý do hiệu suất, vì việc quét toàn bộ tất cả các cổng UDP có thể mất rất nhiều thời gian.*



Sau trong phần hướng dẫn này, chúng ta sẽ xem cách tối ưu hóa tốc độ quét Nmap để phù hợp với nhu cầu của mình, điều này đặc biệt hữu ích khi quét trên tất cả các cổng TCP và UDP.



### V. Kết luận



Trong phần này, cuối cùng chúng ta cũng đã được thực hành thực tế, vì vậy giờ đây chúng ta đã biết **cách sử dụng Nmap một cách cơ bản để quét các cổng TCP và UDP của máy chủ**. Chúng ta cũng đã xem xét chi tiết những gì đang diễn ra ở cấp độ mạng và **cách Nmap xác định xem một cổng TCP hoặc UDP có đang hoạt động hay không**. Cuối cùng, chúng ta đã biết cách chọn lọc kỹ lưỡng các cổng muốn quét và **các tùy chọn mặc định của Nmap thực sự có chức năng gì**. Trong phần tiếp theo, chúng ta sẽ tái sử dụng kiến thức này và áp dụng nó vào việc quét toàn bộ mạng, bao gồm cả ánh xạ toàn cục và khám phá mạng.




## 5 - Lập bản đồ và khám phá mạng với Nmap



### I. Trình bày



Trong phần này, chúng ta sẽ tìm hiểu cách sử dụng công cụ quét mạng Nmap để lập bản đồ mạng. Chúng ta sẽ xem xét hiệu quả của công cụ này trong nhiệm vụ này thông qua các tùy chọn đa dạng. Cuối cùng, chúng ta sẽ xem xét các cách khác nhau để chỉ định mục tiêu quét cho Nmap.



Cụ thể, chúng ta sẽ sử dụng những gì đã học ở phần trước về cách Nmap xác định xem máy chủ có đang hoạt động và có thể truy cập được hay không.



Như đã đề cập trong phần giới thiệu về Nmap, đây là một Network Mapper. Do đó, đây là công cụ hoàn hảo để lập danh sách các máy chủ có thể truy cập trên mạng, dù là cục bộ hay từ xa.



**Sự trở lại của tác giả:**



Trên thực tế, với tư cách là một chuyên gia kiểm tra an ninh mạng và chuyên gia kiểm thử thâm nhập, tôi sử dụng Nmap một cách có hệ thống khi thực hiện các bài kiểm tra xâm nhập nội bộ để xác định vị trí của tôi, những người hàng xóm của tôi trên mạng cục bộ và những mạng nào khác có thể truy cập được, cũng như các hệ thống nằm trên đó. Mục tiêu của tôi rất đơn giản: lập bản đồ mạng, xác định quy mô của hệ thống thông tin và đặc biệt là phác thảo bề mặt tấn công của nó.



Việc lập bản đồ mạng cũng có thể hữu ích trong bối cảnh chẩn đoán mạng, giám sát, lập bản đồ tài sản (bạn có thực sự chắc chắn rằng IS của bạn chỉ bao gồm những gì có trong Active Directory hay trong GLPI/OCS Inventory của bạn không? Nó cũng có thể được sử dụng để phát hiện sự hiện diện của CNTT ngầm trong hệ thống thông tin của bạn.



### II. Sử dụng Nmap để quét phạm vi mạng



#### A. Khám phá mạng bằng cách quét Nmap



Bây giờ chúng ta muốn tiến xa hơn một bước và phân tích toàn bộ mạng cục bộ. Không gì có thể đơn giản hơn: tất cả những gì chúng ta cần làm là sử dụng lại các lệnh đã học ở phần trước, nhưng chỉ định CIDR thay vì IP Address đơn giản.



CIDR (**Định tuyến Liên miền Không Phân lớp**) là ký hiệu "cổ điển" để chỉ định phạm vi mạng và phạm vi của nó (sử dụng mặt nạ). Ví dụ: "192.168.0.0/24" là "bản dịch" của ký hiệu mặt nạ thập phân "255.255.255.0".



Để sử dụng Nmap bằng cách chỉ định CIDR, chúng ta có thể sử dụng như sau:



```
# Scan a CIDR
nmap 192.168.0.0/24
```



Cũng có thể, giống như với các cổng ở phần trước, chỉ định nhiều máy chủ, nhiều mạng hoặc phạm vi:



```
# Scan several networks at once via their CIDR
nmap 192.168.0.0/24 192.168.1.0/24

# Scan several hosts via their IP
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20

# Mix of both
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20
```



Sau đây là ví dụ về kết quả chúng ta có thể nhận được khi chạy quét trên mạng:



![nmap-image](assets/fr/26.webp)



kết quả quét Nmap để lập bản đồ một số mạng



Cụ thể, chúng ta thấy một số máy chủ đang hoạt động và mỗi phần máy chủ đều bắt đầu bằng một dòng như thế này:



```
Nmap scan report for <name> (<IP>)
```



Điều này cho phép chúng ta thấy rõ kết quả sau đây liên quan đến máy chủ nào. Dòng cuối cùng cũng rất quan trọng:



```
Nmap done: 512 IP addresses (5 hosts up) scanned in 21.43 seconds
```



Chúng tôi biết rằng, trên các mạng được quét, Nmap đã phát hiện ra 5 máy chủ đang hoạt động.



#### B. Dưới mui xe: phân tích mạng thông qua Wireshark



Bây giờ chúng ta sẽ xem xét kỹ hơn những gì xảy ra ở cấp độ mạng trong quá trình khám phá mạng được thực hiện thông qua Nmap.



Như chúng ta đã thấy ở phần trước, theo mặc định Nmap sẽ sử dụng giao thức ARP để phát hiện sự hiện diện của máy chủ trên mạng cục bộ:



![nmap-image](assets/fr/27.webp)



Các gói aRP được chụp khi quét mạng cục bộ bằng Nmap và các tùy chọn mặc định của nó



Do đó, nó có thể phát hiện hầu như tất cả các máy chủ trên mạng cục bộ, vì phản hồi cho yêu cầu ARP thường được cung cấp bởi tất cả các máy chủ đang hoạt động trên mạng và không có vẻ gì đáng ngờ.



Đối với mạng từ xa, Nmap sử dụng kết hợp các kỹ thuật sau:



![nmap-image](assets/fr/28.webp)



Các gói tin iCMP và TCP được ghi lại khi quét mạng từ xa bằng Nmap và các tùy chọn mặc định của nó



Chính xác hơn, Nmap sử dụng gói tin ICMP echo (trường hợp điển hình của ping) và gói tin ICMP Timestamp, thường được dùng để tính toán thời gian truyền gói tin. Nó hy vọng sẽ nhận được phản hồi từ các máy chủ trên mạng từ xa.



Nhưng còn hơn thế nữa. Bạn có thể thấy trong ảnh chụp Wireshark ở trên rằng các gói tin **TCP SYN** được gửi một cách có hệ thống đến các cổng TCP/443 của mọi máy chủ tiềm năng trên mạng cần quét, cũng như các gói tin **TCP ACK** trên cổng TCP/80.



**Tại sao lại gửi các gói tin TCP đến các cổng như một phần của quá trình khám phá mạng?**



Việc gửi một gói SYN đến một cổng nhất định cho phép Nmap **xác định xem một dịch vụ có đang lắng nghe trên cổng đó hay không**. Nếu một máy chủ trả lời gói SYN bằng một gói SYN/ACK, điều này cho biết máy chủ đó đang hoạt động và một dịch vụ đang lắng nghe trên cổng đó. Do đó, Nmap sẽ thử vận may trên dịch vụ này, **ngay cả khi không nhận được phản hồi nào cho lệnh ping**.



Việc gửi một gói ACK đến một cổng nhất định cho phép Nmap **xác định xem tường lửa có hiện diện trên máy chủ đó hay không**. Nếu một máy chủ phản hồi gói ACK bằng gói RST (Đặt lại), điều này cho thấy tường lửa có thể đang hiện diện trên máy chủ đó và chặn lưu lượng truy cập không mong muốn. Do đó, máy chủ sẽ tiết lộ sự hiện diện của nó trên mạng, ngay cả khi nó chưa phản hồi các yêu cầu khác.



Tuy nhiên, điều quan trọng cần lưu ý là việc phát hiện tường lửa bằng kỹ thuật này có thể không hoàn toàn đáng tin cậy trong mọi trường hợp. Một số máy chủ có thể phản hồi generate RST vì những lý do khác ngoài sự hiện diện của tường lửa, chẳng hạn như cấu hình dịch vụ hoặc hệ điều hành cụ thể. Ngoài ra, tường lửa hiện đại có thể được cấu hình để không phản hồi các nỗ lực phát hiện kiểu này.



Chúng ta đã đi được một chặng đường dài và có thể thực hiện khám phá mạng cơ bản. Bây giờ, chúng ta sẽ xem xét thêm một vài tùy chọn giúp kiểm soát tốt hơn hoạt động của Nmap.



### III. Khám phá mạng mà không cần quét cổng bằng Nmap



Như bạn có thể đã nhận thấy, theo mặc định, Nmap **thực hiện quét cổng sau khi phát hiện máy chủ đang hoạt động**, điều này sẽ thêm một lượng lớn gói tin và chờ phản hồi cho quá trình quét của chúng tôi. Nếu bạn có 5 máy chủ trên mạng, Nmap sẽ cố gắng kiểm tra trạng thái của khoảng 5.000 cổng, điều này sẽ mất nhiều thời gian hơn.



Tuy nhiên, bạn có thể sử dụng các tùy chọn của Nmap để thực hiện **chỉ khám phá các máy chủ đang hoạt động** trên mạng mà không cần khám phá các dịch vụ của chúng.



Nếu chúng ta chỉ muốn biết máy chủ nào có thể truy cập được mà không cần thông tin về các dịch vụ và cổng mà chúng hiển thị, thì chúng ta có thể sử dụng tùy chọn "-sn" để **chỉ quét bằng ICMP Echo (ping) và các yêu cầu ARP**. Nói cách khác, hãy tắt hoàn toàn chức năng quét cổng:



```
# Scan a CIDR in Echo ICMP
nmap 192.168.1.0/24 -sn
```



Sau đây là kết quả của quá trình khám phá mạng Nmap được thực hiện mà không quét cổng:



![nmap-image](assets/fr/29.webp)



Kết quả khám phá mạng mà không cần quét cổng bằng Nmap.



Chúng tôi đã đề cập đến những hạn chế có thể có khi chỉ sử dụng ICMP để phát hiện máy chủ (cho các mạng từ xa). Đó là lý do tại sao Nmap cũng sử dụng một số thủ thuật có thể tiết lộ sự hiện diện của tường lửa hoặc dịch vụ cụ thể trên máy chủ. Với sự trợ giúp của các tùy chọn, chúng ta có thể tái sử dụng các thủ thuật này và thậm chí mở rộng chúng mà không cần phải bắt đầu lại với việc quét toàn bộ cổng của mọi máy chủ được phát hiện.



Để thực hiện điều này, chúng ta sẽ sử dụng tùy chọn "-PS" (TCP SYN) và "-PA" (TCP ACK), cho phép chúng ta chỉ định các cổng mà chúng ta muốn tham gia như một phần của quá trình khám phá máy chủ, cũng như tùy chọn "-PP":



```
# Scan specific ports on a CIDR
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24
```



Quá trình quét này đảm bảo rằng việc phát hiện máy chủ sẽ hoàn thiện hơn một chút so với các tùy chọn mặc định.



Chúng ta đang bắt đầu có được những lệnh khá toàn diện, sử dụng nhiều tùy chọn. Điều này là do chúng ta đã biết cách Nmap hoạt động và những hạn chế của các tùy chọn "mặc định" của nó, đôi khi có thể khiến chúng ta lãng phí thời gian hoặc bỏ lỡ các hướng dẫn quan trọng về Elements. Đó chính là mục đích của việc dành thời gian để thành thạo nó!



Để biết chi tiết các tùy chọn trong đơn hàng cuối cùng của chúng tôi:





- "`-sn`: vô hiệu hóa chức năng quét cổng cho mỗi máy chủ đang hoạt động được Nmap phát hiện.





- "`-PP`: bật lệnh ICMP echo (quét ping) để khám phá máy chủ.





- "`-PS <PORT>`": gửi gói tin TCP SYN trên các cổng được chỉ định để phát hiện bất kỳ dịch vụ đang hoạt động nào cho thấy sự hiện diện của máy chủ không phản hồi lệnh ping.





- "`-PA <PORT>`": gửi gói tin TCP ACK tới các cổng được chỉ định để phát hiện bất kỳ tường lửa đang hoạt động nào tiết lộ sự hiện diện của máy chủ không phản hồi lệnh ping.




Trong ví dụ trên, tôi chỉ định các cổng mà tôi cho là thường xuyên bị lộ nhất trong ngữ cảnh Nmap của mình cho tùy chọn "-PS". Các cổng khác nhau này sau đó sẽ được kiểm tra trên từng máy chủ, không phải để xem dịch vụ mà chúng lưu trữ có thực sự hoạt động hay không, mà để xem liệu điều này có cho phép chúng tôi phát hiện ra máy chủ nào chưa phản hồi ICMP Echo của chúng tôi trong khi vẫn đang hoạt động (thông qua phản hồi từ dịch vụ hoặc tường lửa của máy chủ) hay không.



Sau đây là những gì có thể thấy trong bản chụp mạng được thực hiện tại thời điểm quét như vậy, trong trường hợp này là bản trích xuất trên một máy chủ mục tiêu duy nhất:



![nmap-image](assets/fr/30.webp)



các gói tin được gửi bởi Nmap trong quá trình khám phá mạng nâng cao, không quét cổng



Chúng tôi tìm các gói tin TCP SYN, TCP ACK trên cổng TCP/80 và ICMP echo. Nmap sẽ thực hiện tất cả các bài kiểm tra này cho từng máy chủ được nhắm mục tiêu trong quá trình quét khám phá mạng.



### IV. Sử dụng tệp tài sản để nhắm mục tiêu với Nmap



Việc xác định mục tiêu có thể nhanh chóng trở nên phức tạp trong các hệ thống thông tin thực tế, đôi khi có thể bao gồm hàng chục hoặc hàng trăm mạng, mạng con và mạng VLAN. Đây là lý do tại sao việc sử dụng một tệp làm nguồn cho Nmap dễ dàng hơn là chỉ định từng mục tiêu trên dòng lệnh.



Để bắt đầu, hãy tạo một tệp đơn giản chứa một mục nhập trên mỗi dòng:



![nmap-image](assets/fr/31.webp)



tệp chứa một mục tiêu (máy chủ hoặc mạng) trên mỗi dòng



Tiếp theo, chúng ta có thể sử dụng tất cả các tùy chọn Nmap đã thấy cho đến nay và chỉ định tùy chọn "-iL <path/file>":



```
# Scan a list of targets contained in a file
nmap -iL /tmp/mesCibles.txt
```



Sau đó, Nmap sẽ quét tất cả các mục tiêu có trong tệp của chúng tôi.



Nếu bạn muốn chắc chắn rằng tất cả các mục tiêu của mình đều được tính đến, bạn có thể sử dụng tùy chọn "-sL -n". Sau đó, Nmap sẽ chỉ diễn giải các CIDR và máy chủ trong tệp và hiển thị chúng cho bạn mà không gửi bất kỳ gói tin nào qua mạng:



```
# Display targets contained in a file
nmap -iL /tmp/mesCibles.txt -sL -n

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-05-01 14:52 CEST
Nmap scan report for 192.168.0.0
Nmap scan report for 192.168.0.1
Nmap scan report for 192.168.0.2
Nmap scan report for 192.168.0.3
Nmap scan report for 192.168.0.4
Nmap scan report for 192.168.0.5
Nmap scan report for 192.168.0.6
Nmap scan report for 192.168.0.7
Nmap scan report for 192.168.0.8
Nmap scan report for 192.168.0.9
Nmap scan report for 192.168.0.10
Nmap scan report for 192.168.0.11
Nmap scan report for 192.168.0.12
```



Điều này đảm bảo rằng danh sách máy chủ cần quét là chính xác.



Một mẹo quan trọng cuối cùng tôi muốn chia sẻ với bạn liên quan đến **việc loại trừ máy chủ hoặc mạng trong quá trình quét**. Việc loại trừ máy chủ này có thể cần thiết trong một số trường hợp, đặc biệt nếu chúng ta muốn đảm bảo rằng **một thành phần nhạy cảm của hệ thống thông tin không bị ảnh hưởng hoặc gián đoạn bởi quá trình quét**.



Ví dụ thường gặp về những nhu cầu này là khi một công ty sở hữu thiết bị công nghiệp (PLC) hoặc thiết bị y tế. Những thiết bị này đôi khi được thiết kế kém, và hoàn toàn không nhằm mục đích tiếp nhận các gói tin có định dạng kém, hoặc quá nhiều gói tin. Vì những lý do rõ ràng về tính khả dụng hoặc rủi ro kinh doanh/con người, tốt hơn hết là loại trừ chúng khỏi quá trình thử nghiệm.



Để loại trừ địa chỉ IP hoặc mạng khỏi quá trình quét, chúng ta có thể sử dụng tùy chọn "--exclude" của Nmap, ví dụ:



```
# Exclude an IP address in a CIDR scan
nmap 192.168.1.0/24 --exclude 192.168.1.140
```



Trong ví dụ này, tôi đang quét mạng "192.168.1.0/24" nhưng loại trừ máy chủ "192.168.1.140" nằm ở đó. Nmap sẽ không gửi bất kỳ gói tin nào đến máy chủ này. Một ví dụ khác với việc loại trừ mạng con:



```
# Exclude a subnet in a CIDR scan
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```



Tương tự, tôi quét mạng lớn "10.0.0.0/16", nhưng mạng "10.0.100.0/24" sẽ không được quét. Một lần nữa, tôi khuyên bạn nên sử dụng tùy chọn "-sL -n" để có cái nhìn rõ ràng hơn về máy chủ nào sẽ được quét và máy chủ nào sẽ bị loại trừ khỏi quá trình quét, đặc biệt nếu bạn đang hoạt động trong bối cảnh nhạy cảm.



### V. Khám phá mạng và quét cổng



Bây giờ chúng ta có thể kết hợp những gì đã học trong phần này với những gì đã học trong phần trước về các tùy chọn quét cổng. Theo mặc định, chúng ta đã thấy Nmap sẽ quét 1000 cổng thường xuyên nhất trên mọi máy chủ đang hoạt động mà nó phát hiện. Chúng ta đã biết cách ngăn chặn hành vi này nếu không muốn, nhưng chúng ta có thể hoàn toàn kiểm soát nó, và thậm chí mở rộng nó nếu phù hợp với nhu cầu của mình.



Ví dụ, lệnh sau sẽ kiểm tra sự hiện diện của dịch vụ lắng nghe trên cổng TCP/22 trên mỗi máy chủ được quét:



```
# Scan TCP/22 on a CIDR
nmap 192.168.0.0/24 192.168.1.0/24 -p 22
```



Đầu tiên, Nmap sẽ thực hiện khám phá mạng để liệt kê các máy chủ đang hoạt động và đối với mỗi máy chủ, kiểm tra xem có dịch vụ nào hiện diện trên cổng TCP/22 hay không.



Tương tự như vậy, chúng ta có thể thực hiện quét toàn bộ tất cả các cổng TCP trên mọi máy chủ được phát hiện trên mạng "192.168.0.0/24", ngoại trừ máy chủ "192.168.0.4" chẳng hạn:



```
# Port scan of a CIDR with exclusion
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```



Bạn có thể thoải mái kết hợp tất cả các tùy chọn mà chúng ta đã tìm hiểu cho đến nay để phù hợp với nhu cầu của riêng bạn.



### VI. Kết luận



Trong phần này, chúng ta đã tìm hiểu cách sử dụng Nmap để lập bản đồ mạng bằng nhiều tùy chọn khác nhau. Giờ đây, chúng ta đã hiểu rõ hơn về mục tiêu quét, cũng như cách thức quét cổng và phương pháp phát hiện máy chủ của Nmap. Và quan trọng nhất, chúng ta đã biết cách thức hoạt động và các hạn chế mặc định của Nmap, cũng như cách sử dụng các tùy chọn chính của nó để tiến xa hơn.



Trong phần tiếp theo, chúng ta sẽ xem xét các cơ chế và tùy chọn để khám phá phiên bản dịch vụ và hệ điều hành được Nmap quét.




## 6 - Phát hiện phiên bản dịch vụ và hệ điều hành bằng Nmap



### I. Trình bày



Trong phần này, chúng ta sẽ tìm hiểu cách sử dụng Nmap để khám phá và phát hiện chính xác phiên bản dịch vụ và hệ điều hành được sử dụng bởi các máy chủ được quét. Chúng ta sẽ xem xét chi tiết cách Nmap thực hiện nhiệm vụ này, cũng như những hạn chế của công cụ để hiểu rõ hơn và diễn giải kết quả.



Như chúng ta đã thấy trong các phần trước của hướng dẫn này, theo mặc định, Nmap sẽ không kiểm tra xem dịch vụ nào được hiển thị trên các cổng mà nó quét và coi là đang mở. Vì vậy, nếu bạn đang nghe một dịch vụ web trên cổng TCP/22, Nmap sẽ tiếp tục báo cáo dịch vụ đó là đang mở, nhưng là một dịch vụ `SSH`. Điều này là do nó sử dụng [cơ sở dữ liệu](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) cục bộ trong hệ thống của bạn để tìm kiếm mối quan hệ giữa một cổng/giao thức và tên của dịch vụ (tệp `/etc/services/`).



Trong phần lớn các trường hợp, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) sẽ cung cấp cho bạn thông tin chính xác, vì những trường hợp như vậy rất hiếm khi xảy ra trong môi trường sản xuất. Tuy nhiên, những trường hợp còn lại sẽ là những tình huống mà một dịch vụ cổ điển ([SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), HTTP, v.v.) được hiển thị trên một cổng không cổ điển (ví dụ: 2022 cho dịch vụ SSH). Trong trường hợp đó, Nmap sẽ không tìm thấy kết quả trùng khớp trong cơ sở dữ liệu cục bộ hoặc kết quả không khớp với thực tế, và bạn sẽ bỏ lỡ những thông tin quan trọng.



May mắn thay, Nmap cung cấp các tùy chọn và cơ chế rất chính xác để phát hiện dịch vụ cụ thể nào có thể ẩn sau một cổng mở. Nó thậm chí còn có cơ sở dữ liệu truy vấn và chữ ký để xác định chính xác công nghệ và phiên bản. Ngoài các dịch vụ, Nmap còn có thể xác định công nghệ được sử dụng và phiên bản của nó.



Đó là những gì chúng ta sẽ xem xét trong phần này.



### II. Cách phát hiện công nghệ hoặc phiên bản



#### A. Nhắc lại cách xác định công nghệ hoặc phiên bản



Việc xác định công nghệ và phiên bản liên quan đến việc lấy tên của dịch vụ, CMS, ứng dụng hoặc phần mềm đang lắng nghe trên cổng mục tiêu. Ví dụ: một trang web được quản lý bởi CMS (`WordPress`), được chạy bởi một dịch vụ web (`Apache`, IIS, Nginx) và được lưu trữ trên một máy chủ (Linux hoặc Windows). Nhưng làm thế nào để biết dịch vụ web nào đang chạy?



Phương pháp cổ điển để tìm ra thông tin này là _bắt biểu ngữ_, đơn giản là xác định vị trí dịch vụ đang hiển thị thông tin này và đọc dữ liệu. Thông thường, trong cấu hình hoặc quy trình xử lý mặc định, các dịch vụ sẽ hiển thị tên và thậm chí cả phiên bản của chúng làm phản hồi đầu tiên sau khi kết nối.



![nmap-image](assets/fr/32.webp)



hiển thị phiên bản ngay khi kết nối TCP được thiết lập bởi dịch vụ FTP



Ở đây chúng ta thấy rằng một kết nối TCP đơn giản tới dịch vụ này thông qua `telnet` sẽ tạo ra một gói tin TCP chứa công nghệ và phiên bản của dịch vụ đó.



Khi đã nắm được loại dịch vụ mình đang xử lý, bạn cũng có thể gửi các lệnh hoặc yêu cầu cụ thể đến dịch vụ đó để trích xuất thông tin. Những yêu cầu/lệnh này cũng có thể được gửi một cách ngẫu nhiên (mà không chắc chắn chúng có đúng loại dịch vụ hay không), với hy vọng rằng một trong số chúng sẽ kích hoạt phản hồi từ dịch vụ đó.



Trong những trường hợp khác phức tạp hơn, cần phải gửi các gói tin cụ thể để gây ra phản ứng, chẳng hạn như lỗi, nhằm cung cấp thông tin chi tiết về phiên bản hoặc công nghệ được sử dụng.



Như bạn có thể tưởng tượng, Nmap sẽ sử dụng tất cả các kỹ thuật này để cố gắng xác định chính xác loại dịch vụ được lưu trữ trên một cổng, cũng như tên công nghệ và phiên bản của dịch vụ đó.



#### B. Hiểu về các thăm dò và kết quả khớp Nmap



Để thực hiện tất cả các kiểm tra này trên mỗi cổng được quét, Nmap sử dụng một cơ sở dữ liệu cục bộ được cập nhật thường xuyên (giống như tệp nhị phân hoặc các mô-đun của nó). Đây là một tệp văn bản gồm hàng nghìn dòng: `/usr/share/nmap/nmap-service-probes`.



Tệp này bao gồm nhiều mục nhập, tất cả đều được sắp xếp theo hai nguyên tắc chính:





- `Probe`: đây là định nghĩa của gói tin mà Nmap sẽ gửi để cố gắng kích thích phản ứng từ dịch vụ cần được xác định. Hãy tưởng tượng nó như một nỗ lực mù quáng như _Xin chào? Guten Tag? Xin chào? Ừm... Buenos Dias chăng?_. Ngay khi dịch vụ mục tiêu nhận được một probe mà nó hiểu (tức là nói đúng giao thức), nó sẽ phản hồi lại Nmap, sau đó sẽ có xác nhận về loại dịch vụ đó.





- "Match": đây là các biểu thức chính quy mà Nmap áp dụng cho phản hồi nhận được. Nếu việc gửi yêu cầu HTTP GET đã tạo ra phản hồi từ dịch vụ, nó sẽ áp dụng hàng chục biểu thức chính quy cho phản hồi này để xác định sự hiện diện của, ví dụ, từ `Apache`, `Nginx`, `Microsoft IIS`, v.v.




Có một vài chỉ thị khác cho các trường hợp cụ thể, nhưng những chỉ thị chính để hiểu cách Nmap hoạt động và tùy chỉnh cách sử dụng là những chỉ thị sau. Để làm rõ hơn phần lý thuyết này, đây là một ví dụ:



![nmap-image](assets/fr/33.webp)



ví dụ về một Probe trong tệp `/usr/share/nmap/nmap-service-probes` của Nmap



Ở dòng đầu tiên của ví dụ này, chúng ta thấy một Probe dễ hiểu có tên `GetRequest`. Đây là một gói tin TCP chứa một yêu cầu HTTP GET rỗng đến gốc dịch vụ web bằng HTTP/1.0, theo sau là một dòng lệnh và một dòng lệnh trống.



Dòng `ports` cho Nmap biết cổng nào sẽ được gửi đến để kiểm tra. Điều này cho phép bạn ưu tiên các bài kiểm tra và tiết kiệm thời gian.



Cuối cùng, chúng ta có hai ví dụ về `match`. Ví dụ đầu tiên sẽ phân loại dịch vụ web được quét là `ajp13` nếu biểu thức chính quy chứa trong dòng này khớp với phản hồi dịch vụ nhận được.



Để giúp bạn hiểu Probe trông như thế nào, sau đây là danh sách một số Probe bạn sẽ tìm thấy trong tệp này (có tổng cộng 188 Probe tại thời điểm viết hướng dẫn này).



![nmap-image](assets/fr/34.webp)



ví dụ về một số Probe được Nmap sử dụng và có trong tệp `/usr/share/nmap/nmap-service-probes`._



Hai lệnh đầu tiên (được gọi là `NULL` và `GenericLines`) đặc biệt hữu ích ở đây, vì chúng chỉ gửi một gói tin TCP rỗng hoặc một gói tin chứa ký tự ngắt dòng. Các dịch vụ máy chủ thường tự thông báo ngay khi nhận được kết nối, mà không cần bất kỳ hành động, lệnh hoặc yêu cầu cụ thể nào từ máy khách.



Đây là trường hợp của một _trận đấu_ phức tạp hơn một chút:



```
# Match Nginx + version in an error 400 page
match ssl/http m|^HTTP/1.1 400 Bad Request\r\n.*?Server: nginx/([\d.]+)[^\r\n]*?\r\n.*<title>400 The plain HTTP request was sent to HTTPS port</title>|s p/nginx/ v/$1/ cpe:/a:igor_sysoev:nginx:$1/
```



Biểu thức chính quy chính xác nằm ở đây giữa `m|` và `|`, dùng để phân định bất kỳ biểu thức chính quy nào trong tệp này. Vui lòng dành thời gian đọc toàn bộ ví dụ này. Bạn sẽ thấy một lựa chọn trong biểu thức chính quy: `([\d.]+)`, được sử dụng để phân lập một phiên bản. Ví dụ này cũng định nghĩa các Elements khác như tên sản phẩm `p/nginx/`, phiên bản được truy xuất `v/$1/` và CPE với phiên bản `cpe:/a:igor_sysoev:nginx:$1/`.



CPE (Common Platform Enumeration - Liệt kê Nền tảng Chung) là một hệ thống ký hiệu chuẩn hóa được sử dụng để xác định và mô tả phần mềm và phần cứng. Định dạng này cho phép quản lý hiệu quả hơn các lỗ hổng và cấu hình bảo mật, và trên hết là một cách thống nhất để biểu diễn chúng, bất kể sản phẩm nào đang được đề cập. Dưới đây là hai ví dụ về CPE: `cpe:/o:microsoft:windows_8.1:r1` và `cpe:/a:apache:http_server:2.4.35`



Ở đây chúng ta xác định rõ ràng các loại `o` cho hệ điều hành, `a` cho ứng dụng, nhà cung cấp, sản phẩm và phiên bản.



Vì vậy, trong trường hợp _khớp_ với một trong những biểu thức chính quy này, chúng tôi sẽ lấy không chỉ tên dịch vụ mà còn cả phiên bản và CPE chính xác của dịch vụ, giúp việc tìm kiếm các CVE ảnh hưởng đến phiên bản này trở nên dễ dàng hơn. Bạn sẽ tìm thấy thông tin này trong đầu ra tiêu chuẩn của Nmap, và bạn sẽ thấy rằng nó rất hữu ích cho các mục đích khác mà chúng tôi sẽ đề cập trong một vài phần sau.



Cú pháp chính xác của _matches_ và, nói chung hơn, của các chỉ thị trong tệp `/usr/share/nmap/nmap-service-probes` không dừng lại ở đó, và có thể khá phức tạp nếu bạn chưa quen với việc thao tác với Nmap và kết quả của nó. Tuy nhiên, ít nhất bạn nên ghi nhớ sự tồn tại và hoạt động chung của nó, điều này sẽ hữu ích sau này khi bạn muốn hiểu hoặc gỡ lỗi kết quả, tùy chỉnh quá trình quét hoặc thậm chí đóng góp vào quá trình phát triển Nmap.



### III. Sử dụng Nmap để phát hiện phiên bản



Bây giờ chúng ta sẽ sử dụng tất cả các cơ chế _Dò_ và _So khớp_ phức tạp này thông qua một tùy chọn đơn giản: `-sV`. Tùy chọn này chỉ đơn giản yêu cầu Nmap: hãy thử tìm hiểu chính xác những dịch vụ và phiên bản cổng nào bạn đã đặt là mở.



```
# Enable service and version detection
nmap 192.168.1.0/24 -sV
```



Sau đây là ví dụ đầy đủ về kết quả của lệnh như vậy:



![nmap-image](assets/fr/35.webp)



kết quả phát hiện phiên bản ứng dụng của Nmap được hiển thị trên mạng



Ở đây, chúng ta có thể thấy Nmap đã xác định được tất cả các phiên bản dịch vụ mạng mà mục tiêu này khai thác và hiển thị thông tin này trong cột `VERSION` mới. Có thể thấy thông tin khá chính xác, thậm chí đến cả hệ điều hành, nếu thông tin này là một phần của chữ ký được phục hồi.



Để hiểu chi tiết những gì xảy ra trong quá trình quét lỗ hổng, chúng ta có thể sử dụng tùy chọn `--version-trace`. Tùy chọn này sẽ cung cấp chế độ xem gỡ lỗi, hiển thị _Probe_ dẫn đến việc phát hiện:



```
# Enable version detection debug
nmap 192.168.1.0/24 -sV --version-trace
```



Kết quả là, chúng ta sẽ có rất nhiều thông tin cần phân loại. Hãy thử xác định các dòng bắt đầu bằng `Service scan Hard match`. Sau đó, bạn sẽ thấy các dòng như sau:



```
Service scan hard match (Probe NULL matched with NULL line 789): 10.10.10.187:21 is ftp. Version: |vsftpd|3.0.3||
Service scan hard match (Probe NULL matched with NULL line 3525): 10.10.10.187:22 is ssh. Version: |OpenSSH|7.4p1 Debian 10+deb9u7|protocol 2.0|
Service scan hard match (Probe GetRequest matched with GetRequest line 10510): 10.10.10.187:80 is http. Version: |Apache httpd|2.4.25|(Debian)|
```



Chúng ta có thể thấy rõ _Probes_ nào được sử dụng để phát hiện công nghệ và phiên bản (trong trường hợp này là `NULL` và `GetRequest` _Probes_), cũng như thông tin được truy xuất.



### IV. Nắm vững các xét nghiệm và độ chính xác phát hiện



Bây giờ chúng ta sẽ quay lại chỉ thị trong tệp `/usr/share/nmap/nmap-service-probes` mà chúng ta chưa xem xét trước đó:



![nmap-image](assets/fr/36.webp)



chỉ thị `rarity` thăm dò trong tệp `/usr/share/nmap/nmap-service-probes`._



Chỉ thị này được sử dụng để chỉ ra độ hiếm (tức là mức độ ưu tiên/xác suất) liên quan đến _Probe_. Ký hiệu từ 1 đến 9 này cho phép bạn kiểm soát tính đầy đủ của phân tích được Nmap thực hiện khi gửi _Probe_. Trong hệ thống "ký hiệu" của Nmap, độ hiếm 1 cung cấp thông tin trong phần lớn các trường hợp, trong khi độ hiếm 8 hoặc 9 đại diện cho một trường hợp rất đặc biệt, cụ thể cho một cấu hình hoặc dịch vụ hiếm khi xuất hiện.



Để rõ ràng hơn, trong trường hợp mặc định, Nmap sẽ gửi đến từng dịch vụ để xác định _Probes_ có độ hiếm từ 1 đến 7. Để bạn hiểu rõ hơn về sự phân bổ _Probes_ theo _rarity_, đây là số lượng của chúng:



```
$ grep -E "^rarity" nmap-service-probes |sort |uniq -c

6 rarity 1
1 rarity 2
3 rarity 3
8 rarity 4
9 rarity 5
13 rarity 6
8 rarity 7
81 rarity 8
54 rarity 9
```



Nghe có vẻ ngược đời, nhưng có nhiều Probe `rarity` 8 và 9 hơn các Probe còn lại. Lý do chính là vì Probe `rarity` 1 mang tính chung chung và hoạt động trong hầu hết các trường hợp, bất kể dịch vụ nào (hãy nhớ Probe `NULL` chỉ đơn giản là gửi một gói tin TCP rỗng). Trong khi đó, các Probe phức tạp hơn gần như là duy nhất cho mỗi dịch vụ.



Nếu chúng ta muốn quản lý thủ công các đầu dò mà chúng ta muốn sử dụng trong quá trình quét phiên bản, chúng ta có thể sử dụng tùy chọn `--version-intensity`. Dưới đây là hai ví dụ:



```
# Less accurate version detection than default
nmap 192.168.1.0/24 -sV --version-intensity 2

# Very deep detection, using all existing Probes
nmap 192.168.1.0/24 -sV --version-intensity 9
```



Để kết thúc chủ đề này, đây là một ví dụ về _Probe_ 9 và 8:



![nmap-image](assets/fr/37.webp)



ví dụ về Probe ở độ hiếm 8 và 9 trong tệp `/usr/share/nmap/nmap-service-probes`._



Hai _Probes_ này phát hiện máy chủ Quake1 và Quake2 (trò chơi điện tử). Thú vị cho những ai hoài niệm, nhưng có lẽ không mấy hữu ích trong cuộc sống hàng ngày.



Tùy thuộc vào nhu cầu về độ chính xác hoặc tốc độ của bạn, hãy nhớ rằng nguyên tắc `hiếm có` này tồn tại và có thể ảnh hưởng đến kết quả.



### V. Sử dụng Nmap để phát hiện hệ điều hành



Bây giờ chúng ta sẽ xem xét cách Nmap có thể giúp chúng ta phát hiện hệ điều hành của các máy chủ được quét và phát hiện trên mạng. Để thực hiện việc này, hãy sử dụng tùy chọn `-O` (viết tắt của `OS Scan`) của Nmap.



```
# Enable OS Scan
nmap -O 10.10.10.0/24
```



Sau đây là một ví dụ về kết quả. Nmap cho chúng ta biết đó có thể là hệ điều hành Linux và cung cấp cho chúng ta nhiều số liệu thống kê khác nhau liên quan đến phiên bản chính xác của hệ điều hành đó.



![nmap-image](assets/fr/38.webp)



phát hiện khả năng nhận dạng hệ điều hành bằng Nmap



Để đạt được điều này, Nmap sẽ sử dụng nhiều kỹ thuật hoạt động rất giống với _Probes_ và _Matches_ để phát hiện công nghệ và phiên bản. Điểm khác biệt chính là Nmap sẽ sử dụng các tham số "cấp thấp" của ICMP, TCP, UDP và các giao thức khác. Dưới đây là hai ví dụ thử nghiệm để phát hiện hệ điều hành Microsoft Windows 11:



![nmap-image](assets/fr/39.webp)



ví dụ về các thử nghiệm được thực hiện bởi Nmap để phát hiện hệ điều hành Windows 11



Thực tế, những bài kiểm tra này rất khó diễn giải, và chúng tôi sẽ không cố gắng tìm hiểu sâu hơn trong khuôn khổ một bài hướng dẫn Nmap cơ bản. Nếu bạn muốn tìm hiểu sâu hơn về chủ đề này, tệp chứa thông tin này là `/usr/share/nmap/nmap-os-db`.



Tuy nhiên, bạn cần lưu ý rằng việc phát hiện hệ điều hành phụ thuộc nhiều vào khả năng xác định của Nmap hơn là sự chắc chắn.



### VI. Kết luận



Trong phần này, chúng ta đã tìm hiểu cách sử dụng các tùy chọn của Nmap để phát hiện công nghệ, phiên bản và hệ điều hành của các máy chủ và dịch vụ được quét. Giờ đây, chúng ta đã hiểu rõ cách Nmap thu thập thông tin này từ xa. Chúng ta cũng đã xem xét các tùy chọn để quản lý độ chi tiết và độ chính xác của bài kiểm tra, cũng như những hạn chế của công cụ này trong các vấn đề này.



Trong phần tiếp theo, chúng ta sẽ tìm hiểu cách sử dụng các tập lệnh NSE của Nmap để thực hiện phân tích bảo mật hệ thống thông tin. Hãy dành thời gian đọc lại các phần trước nếu cần, và đừng ngần ngại thực hành và tự mình tìm hiểu sâu hơn về công cụ này để nắm vững hơn những kiến thức đã học.




## 7 - Phân tích bảo mật: phát hiện lỗ hổng



### I. Trình bày



Trong phần này, chúng ta sẽ tìm hiểu cách sử dụng công cụ quét mạng Nmap để phát hiện và phân tích các lỗ hổng trên các mục tiêu quét. Cụ thể, chúng ta sẽ xem xét các tùy chọn khác nhau có sẵn để thực hiện nhiệm vụ này và nghiên cứu các giới hạn về khả năng của công cụ để hiểu rõ hơn và diễn giải kết quả.



Trong phần đầu tiên này, chúng ta sẽ tìm hiểu về trình quét lỗ hổng của Nmap và cách sử dụng các tùy chọn phát hiện lỗ hổng cơ bản. Trong các phần tiếp theo, chúng ta sẽ xem xét kỹ hơn cách thức hoạt động của tính năng này và cách tùy chỉnh nó.



### II. Sử dụng Nmap để phát hiện lỗ hổng



Bây giờ chúng tôi muốn sử dụng trình quét mạng Nmap để phát hiện lỗ hổng trong các dịch vụ và hệ thống thuộc hệ thống thông tin của mình. Điều này có nghĩa là ngoài việc phát hiện các máy chủ đang hoạt động, liệt kê các dịch vụ bị tấn công và phát hiện các phiên bản và công nghệ, Nmap sẽ tìm kiếm lỗ hổng.



Để đạt được điều này, Nmap dựa vào các tập lệnh NSE (_Nmap Scripting Engine_), có thể được xem như các mô-đun cho phép tiếp cận chi tiết hơn để thử nghiệm.



Với các tùy chọn phù hợp, chúng tôi sẽ yêu cầu Nmap sử dụng nhiều tập lệnh NSE khác nhau trên mỗi dịch vụ được phát hiện, cho phép chúng tôi khám phá:





- Lỗi cấu hình;





- Khám phá phiên bản và hệ điều hành bổ sung và nâng cao hơn;





- Các lỗ hổng đã biết (CVE);





- Nhận dạng yếu;





- Đặc điểm Elements của nhiễm phần mềm độc hại;





- Khả năng từ chối dịch vụ;





- Vân vân.




Như bạn có thể thấy, các tập lệnh NSE mở rộng đáng kể khả năng của Nmap về các hoạt động mạng mà nó có thể thực hiện. Điều này cho phép thực hiện các tác vụ nâng cao hơn bao giờ hết. Tin tốt là, như thường lệ, các tính năng này có thể được sử dụng đơn giản thông qua một tùy chọn và trong ngữ cảnh mặc định. Đây là những gì chúng ta sẽ thấy tiếp theo.



### III. Ví dụ về quét lỗ hổng



Có thể sử dụng các tập lệnh NSE khi sử dụng Nmap để quét một cổng duy nhất trên máy chủ, tất cả các dịch vụ trên máy chủ đó hoặc tất cả các dịch vụ được phát hiện trên nhiều mạng. Do đó, chúng ta có thể sử dụng các tùy chọn sẽ thấy trong tất cả các bối cảnh đã nghiên cứu cho đến nay.



Để bật tính năng quét lỗ hổng thông qua quét Nmap, chúng ta cần sử dụng tùy chọn `-sC`:



```
# Enable vulnerability scanning during a scan
nmap -sC 10.10.10.152
```



Hãy nhớ rằng theo mặc định, nếu bạn không chỉ định bất kỳ thông tin nào, Nmap sẽ chỉ quét 1000 cổng phổ biến nhất. Nó sẽ không phát hiện lỗ hổng trên các cổng nguy hiểm hơn mà mục tiêu của bạn có thể khai thác.



Trước khi sử dụng chức năng này trên hệ thống thông tin sản xuất, tôi mời bạn tiếp tục đọc hướng dẫn. Trong các phần tiếp theo, chúng ta sẽ xem xét cách kiểm soát tốt hơn tác động và các loại thử nghiệm sẽ được chạy.



Bằng cách sử dụng lại những gì đã học trước đây, chúng ta có thể toàn diện hơn và quét tất cả các cổng TCP của mục tiêu:



```
# Enable vulnerability scanning on all ports
nmap -sC -p- 10.10.10.152
```



Sau đây là kết quả quét Nmap bằng tập lệnh NSE:



![nmap-image](assets/fr/40.webp)



ví dụ về kết quả quét lỗ hổng trên máy chủ thông qua Nmap._



Ở đây chúng ta thấy màn hình hiển thị thông tin bổ sung đáng quan tâm trong bối cảnh phân tích lỗ hổng:





- Dịch vụ FTP có thể được truy cập ẩn danh và không được bảo vệ bằng xác thực. Tập lệnh NSE chịu trách nhiệm xác minh này cho chúng ta biết điều đó, và thậm chí còn hiển thị một phần cấu trúc cây của dịch vụ FTP. Ở đây, chúng ta thấy mình có quyền truy cập vào thư mục `C` của hệ thống Windows!





- Tập lệnh NSE chịu trách nhiệm truy xuất dịch vụ web nâng cao sẽ hiển thị tiêu đề trang, giúp chúng ta hiểu rõ hơn về dịch vụ web đang lưu trữ nội dung gì.





- Chúng tôi cũng có một bản phân tích nhỏ về cấu hình dịch vụ SMB (các tập lệnh `smb2-time`, `smb-security-mode` và `smb2-security-mode`). Thông tin được hiển thị hơi khác một chút sau kết quả quét mạng để dễ đọc hơn. Cụ thể, thông tin này cho thấy không có chữ ký SMB Exchange. Điểm yếu cấu hình này cho phép mục tiêu bị lợi dụng trong một cuộc tấn công SMB Relay, một lỗ hổng bảo mật đáng chú ý thường bị khai thác trong các bài kiểm tra xâm nhập/tấn công mạng.




Tất nhiên, đây chỉ là một ví dụ. Nmap có các tập lệnh NSE cho nhiều dịch vụ, nhắm mục tiêu vào nhiều lỗ hổng bảo mật khác nhau. Chúng ta sẽ xem xét kỹ hơn các khả năng này trong phần tiếp theo.



Để kết thúc phần giới thiệu về quét lỗ hổng bảo mật này, đây là lệnh đầy đủ để khám phá mạng, quét cổng TCP, phát hiện phiên bản và lỗ hổng bảo mật:



```
# Complete and realistic vulnerability scan command
nmap -sV -sC -p- 192.168.0.0/24 192.168.1.13 192.168.2.10-20 --exclude 192.168.0.4
```



Đây là lệnh bắt đầu trông giống như trường hợp sử dụng Nmap thực tế hơn!



### IV. Hiểu những hạn chế của Nmap trong việc quét lỗ hổng



Cần nói rõ: Nmap không có khả năng thực hiện kiểm tra xâm nhập toàn diện hệ thống thông tin của bạn, hoặc mô phỏng hoạt động của Red Team. Nó có một số hạn chế mà bạn cần lưu ý nếu không muốn có cảm giác an toàn giả tạo:





- **Phạm vi bao phủ hạn chế**: Mặc dù các tập lệnh NSE của Nmap rất mạnh mẽ, phạm vi kiểm tra của chúng có thể bị hạn chế so với các công cụ phát hiện lỗ hổng chuyên dụng khác. Một số lỗ hổng có thể không được các tập lệnh NSE hiện có bao phủ, chẳng hạn như lỗ hổng Active Directory, rò rỉ dữ liệu nhạy cảm hoặc các trường hợp ứng dụng web dễ bị tấn công phức tạp hơn.





- **Độ phức tạp của lỗ hổng**: một số loại lỗ hổng có thể khó phát hiện bằng các tập lệnh NSE do tính phức tạp của chúng. Ví dụ, các lỗ hổng đòi hỏi tương tác phức tạp với dịch vụ từ xa có thể không được Nmap phát hiện hiệu quả (như trong trường hợp cấp quá nhiều quyền trong chia sẻ tệp hoặc lỗi kiểm soát quyền trong ứng dụng web).





- **Phát hiện thụ động**: Nmap chủ yếu tập trung vào quét chủ động để phát hiện lỗ hổng, nghĩa là nó có thể không phát hiện hiệu quả các lỗ hổng tiềm ẩn nếu không thiết lập kết nối chủ động với máy chủ mục tiêu. Do đó, các lỗ hổng không tự biểu hiện trong quá trình quét chủ động có thể bị bỏ sót (như trường hợp chèn mã độc vào ứng dụng web).





- **Phụ thuộc vào các bản cập nhật**: [Cơ sở dữ liệu](https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) của Nmap về các tập lệnh NSE liên tục được cập nhật, nhưng có thể có độ trễ giữa thời điểm phát hiện ra lỗ hổng mới và thời điểm thêm tập lệnh tương ứng vào Nmap. Do đó, Nmap có thể không phải lúc nào cũng được cập nhật với các lỗ hổng mới nhất.





- **Kết quả dương tính giả và kết quả âm tính giả**: Giống như bất kỳ công cụ bảo mật nào, các tập lệnh NSE của Nmap có thể tạo ra kết quả dương tính giả (cảnh báo lỗ hổng bảo mật giả) hoặc kết quả âm tính giả (lỗ hổng thực sự không được phát hiện). Đây là điều cần lưu ý khi phân tích kết quả Nmap.




Vì vậy, điều quan trọng là phải hiểu Nmap làm được gì và không làm gì, cũng như biết cách diễn giải kết quả của nó. Cụ thể, trong suốt hướng dẫn này, chúng ta đã thấy rằng các tùy chọn mặc định có thể khiến chúng ta bỏ lỡ các lỗi Elements quan trọng có thể được phát hiện bằng cách sử dụng cẩn thận.



Cho dù bạn là quản trị viên hệ thống mạng, kỹ sư bảo mật hay thậm chí là CISO, việc sử dụng Nmap sẽ cung cấp cho bạn cái nhìn tổng quan về tình trạng bảo mật của một hệ thống thông tin. Đây là bước đầu tiên quan trọng trong việc bảo mật hệ thống, có thể được đội ngũ CNTT thực hiện thường xuyên. Tuy nhiên, nó không thể thay thế sự can thiệp và tư vấn của các chuyên gia [an ninh mạng] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), những người có khả năng phát hiện điểm yếu toàn diện hơn nhiều so với Nmap.



### V. Kết luận



Trong phần đầu tiên của Mô-đun 3, chúng ta đã giới thiệu về quét lỗ hổng bảo mật thông qua Nmap. Giờ đây, chúng ta đã biết cách sử dụng tùy chọn chính để thực hiện tác vụ này, nhưng cũng biết những hạn chế của bài tập. Trong phần tiếp theo, chúng ta sẽ xem xét kỹ hơn chức năng này, sử dụng các tập lệnh NSE để mở rộng sức mạnh của Nmap lên gấp mười lần.



## 8 - Sử dụng tập lệnh NSE của Nmap



### I. Trình bày



Trong phần này, chúng ta sẽ tìm hiểu sâu hơn về các tập lệnh NSE (_Nmap Scripting Engine_). Cụ thể, chúng ta sẽ xem xét lý do tại sao chúng là một trong những điểm mạnh của công cụ này, cách chúng hoạt động và cách duyệt và sử dụng nhiều tập lệnh hiện có.



Phần này tiếp nối hướng dẫn trước, trong đó chúng ta đã học cách sử dụng các tính năng quét lỗ hổng của Nmap một cách cơ bản. Giờ đây, chúng ta sẽ xem xét kỹ hơn cách [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) hoạt động trong lĩnh vực này, để chúng ta có thể một lần nữa thực hiện quét chính xác và có kiểm soát hơn.



### II. Khái niệm về tập lệnh Nmap NSE



Các tập lệnh NSE của Nmap cho phép bạn mở rộng khả năng của nó một cách cực kỳ linh hoạt. Chúng được viết bằng LUA, một ngôn ngữ lập trình dễ xử lý và truy cập hơn so với C hoặc C# mà Nmap sử dụng. Ưu điểm của việc sử dụng tập lệnh LUA với Nmap thay vì một công cụ độc lập là nó cho phép chúng ta tận dụng tốc độ thực thi và các tính năng tiêu chuẩn của Nmap (phát hiện máy chủ, cổng và phiên bản, v.v.).



Các tập lệnh này được sắp xếp theo danh mục và một tập lệnh có thể thuộc về nhiều danh mục:



| Catégorie       | Description |
|----------------|-------------|
| **auth**       | Contient les scripts relatifs à l’authentification sur des services, dont l’accès anonyme ou l’énumération des utilisateurs. Exemples: `oracle-enum-users`, `ftp-anon`. |
| **broadcast**  | Contient les scripts relatifs aux opérations de broadcast sur le réseau, notamment en vue d’exploiter et de découvrir certains services, hôtes ou protocoles reposant sur le broadcast (IPv6, wake on lan, IGMP, etc.). Exemples: `broadcast-dhcp6-discover`, `broadcast-ospf2-discover`. |
| **brute**      | Contient les scripts relatifs aux opérations de brute force de l’authentification sur les services (brute force [SSH](https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/), MSSQL, etc.). Exemples: `ssh-brute`, `vnc-brute`. |
| **default**    | Contient les scripts utilisés dans le cas par défaut (utilisation de `-sC`). Plusieurs critères sont utilisés afin de valider l’entrée d’un script dans cette catégorie dont la vitesse d’exécution, la structure de la sortie, la fiabilité du test, le caractère “intrusif” ou “risqué”, etc. |
| **discovery**  | Contient les scripts relatifs à la découverte avancée du réseau et des services. On y retrouve par exemple l’énumération du contenu d’un partage SMB, d’une version d’un service VNC, des requêtes SNMP, etc. Exemples: `mysql-info`, `http-security-headers`. |
| **dos**        | Contient les scripts pouvant causer un déni de service. Il peut s’agir de scripts créés pour exploiter une vulnérabilité de type déni de service ou alors de scripts ayant pour effet de bord un déni de service. Prudence donc (ils sont exclus de la catégorie `default`). Exemples: `http-slowloris`, `ipv6-ra-flood`. |
| **exploit**    | Contient les scripts créés pour exploiter de manière directe une vulnérabilité. Exemples: `http-shellsock`, `smb-vuln-ms08-067`. |
| **external**   | Contient les scripts qui nécessitent l’utilisation d’une ressource tierce, comme une base d’information en ligne. Cela indique notamment une tentative de connexion vers l’extérieur (attention à la confidentialité). Exemples: `whois-ip`, `dns-blacklist`, `ip-geolocation-geoplugin`. |
| **fuzzer**     | Contient les scripts conçus pour envoyer des trames, paquets ou paramètres inattendus par un service. Cela permet notamment de causer des erreurs ou dysfonctionnements afin d’obtenir des pistes de vulnérabilité ou des informations techniques. Exemples: `dns-fuzz`, `http-form-fuzzer`. |
| **intrusive**  | Contient les scripts qui sont catégorisés comme “risqués” d’un point de vue disponibilité, ou détection. Ils peuvent provoquer un crash du système ou être détectés comme malveillant par une solution de sécurité. Il s’agit de la catégorie inverse de `safe`. Exemples: `smtp-brute`, `smb-vuln-ms08-067`, `smb-psexec`. |
| **malware**    | Contient les scripts conçus pour détecter la présence d’élément caractéristique d’un malware, tel qu’un port en écoute communément utilisé par une backdoor connue. Exemples: `ftp-proftpd-backdoor`, `smtp-strangeport`. |
| **safe**       | Contient les scripts qui sont considérés comme sûrs d’un point de vue détection ou stabilité. Il s’agit de la catégorie inverse de `intrusive` et elle contient en grande majorité des scripts avancés d’identification de version ou de relevé d’élément de configuration. Exemples: `html-title`, `smb2-security-mode`, `ms-sql-info`. |
| **version**    | Contient les scripts qui permettent une détection avancée de version. Ils peuvent être utilisés en complément des Probes et Matchs étudiés précédemment quand la détection d’une version nécessite des opérations un peu plus complexes. Exemples: `http-php-version`, `vmware-version`. |
| **vuln**       | Contient les scripts conçus pour détecter la présence de vulnérabilité connue (CVE) sans pour autant les exploiter (à l’inverse de la catégorie `exploit`). Ils se contentent en général de rapporter le statut “vulnérable” ou non d’un service. Exemples: `smb-vuln-ms17-010` (eternal blue), `http-phpmyadmin-dir-traversal`. |


Về mặt kỹ thuật, các danh mục mà một tập lệnh thuộc về được chỉ ra trực tiếp trong mã của nó.



![nmap-image](assets/fr/41.webp)



Các danh mục tập lệnh nSE `ftp-anon`._



Ví dụ này hiển thị một phần mã của tập lệnh NSE `ftp-anon.nse`, mà chúng ta đã thấy cách thực thi ở phần trước.



### III. Liệt kê các tập lệnh NSE hiện có



Theo mặc định, các tập lệnh NSE của Nmap nằm trong thư mục `/usr/share/nmap/scripts/`, không có cấu trúc cây hay hệ thống phân cấp cụ thể nào. Sau đây là tổng quan về nội dung của thư mục này:



![nmap-image](assets/fr/42.webp)



trích xuất nội dung của thư mục `/usr/share/nmap/scripts/` chứa các tập lệnh NSE._



Thư mục này chứa hơn 5.000 tập lệnh NSE. Trong hầu hết các trường hợp, phần đầu tiên của tên tập lệnh chứa giao thức hoặc danh mục mà tập lệnh đó thuộc về. Điều này cho phép chúng tôi sắp xếp danh sách, ví dụ: nếu chúng tôi muốn liệt kê tất cả các tập lệnh nhắm mục tiêu đến dịch vụ FTP:



![nmap-image](assets/fr/43.webp)



danh sách các tập lệnh NSE Nmap có tên bắt đầu bằng `ftp-`._



Nmap không thực sự cung cấp tùy chọn để duyệt và liệt kê các tập lệnh NSE; bạn có thể sử dụng lệnh `--script-help` theo sau là tên của một danh mục hoặc một từ:



```
# List all scripts whose name starts with "ftp-"
nmap --script-help=ftp-*

# List all scripts from the "discovery" category
nmap --script-help=discovery
```



Tuy nhiên, kết quả đầu ra sẽ là tên của từng tập lệnh và mô tả của nó, điều này không tối ưu nếu tìm kiếm trả về hàng chục tập lệnh:



![nmap-image](assets/fr/44.webp)



kết quả của việc sử dụng lệnh `--script-help` của Nmap



Theo tôi, phương pháp hiệu quả nhất là sử dụng các lệnh Linux cổ điển trong thư mục `/usr/share/nmap/scripts/`:



```
# List scripts targeting the "ssh" service
ls -al /usr/share/nmap/scripts/ssh*

# List scripts from the "dos" category
grep -rl '"dos"' /usr/share/nmap/scripts/
```



Bạn có thể thoải mái duyệt qua mã của các mô-đun phù hợp với mình để hiểu rõ hơn về cách hoạt động của tập lệnh NSE.



### IV. Sử dụng các tập lệnh NSE của Nmap



Bây giờ chúng ta sẽ tìm hiểu cách thực hiện quét lỗ hổng bằng cách cẩn thận lựa chọn các tập lệnh NSE mà chúng ta quan tâm.



#### A. Chọn tập lệnh theo danh mục



Để bắt đầu, chúng ta có thể chọn thực thi tất cả các tập lệnh thuộc một danh mục cụ thể. Chúng ta cần chỉ định danh mục này hoặc các danh mục này cho Nmap bằng đối số `--script <category>`:



```
# Use default NSE scripts
nmap --script default 10.10.10.152
```



Lệnh đầu tiên này tương đương với lệnh `nmap -sC`. Theo mặc định, Nmap sẽ chọn các tập lệnh trong danh mục `default`, nhưng đó chỉ là để tranh luận. Ví dụ, lệnh tiếp theo sẽ sử dụng tất cả các tập lệnh trong danh mục `discovery`:



```
# Use NSE scripts from the "discovery" category
nmap --script discovery 10.10.10.152
```



Như chúng ta đã thấy, một số danh mục cho phép chúng ta nhanh chóng xác định tác dụng của các tập lệnh NSE liên quan (`discovery`, `vuln`, `exploit`), trong khi một số danh mục khác xác định mức độ rủi ro, phát hiện hoặc tính ổn định của bài kiểm tra được thực hiện. Nếu chúng ta đang ở trong một bối cảnh nhạy cảm và không nắm rõ các hành động khác nhau được thực hiện bởi lựa chọn tập lệnh của mình, chúng ta có thể kết hợp các lựa chọn để chỉ chọn những tập lệnh thuộc danh mục `discovery` và `safe`:



```
# Use scripts from multiple categories
nmap --script "discovery and safe" 10.10.10.152
```



Nếu bạn thực sự và rõ ràng muốn loại trừ các tập lệnh khỏi danh mục `dos` và `intrusive`, bạn có thể sử dụng ký hiệu sau:



```
# Exclude categories
nmap --script "not intrusive and not dos" 10.10.10.152
```



Xin lưu ý rằng việc chỉ định các điều kiện loại trừ như trên sẽ dẫn đến việc sử dụng tất cả các danh mục khác không được loại trừ rõ ràng. Để công bằng hơn, chúng ta có thể chỉ định, ví dụ:



```
# Include scripts from the "vuln" category except those that are too risky
nmap --script "vuln and not intrusive and not dos" 10.10.10.152

# Same thing, but only targeting the HTTP protocol
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152
```



Sau đây là một số ví dụ về cách xử lý các tập lệnh NSE theo danh mục, đặc biệt là khi sử dụng Nmap để phân tích lỗ hổng trong bối cảnh thực tế.



#### B. Chọn tập lệnh làm đơn vị



Chúng ta cũng có thể chọn thực hiện một thử nghiệm cụ thể duy nhất trong quá trình phân tích, một thử nghiệm tương ứng với một tập lệnh NSE. Để thực hiện việc này, chúng ta cần chỉ định tên tập lệnh trong tham số `-script <tên>`. Lấy ví dụ về tập lệnh `ftp-anon.nse`:



```
# Use an NSE script and a specific port
nmap --script ftp-anon -p 21 10.10.10.152
```



Sau đó chúng ta có một kết quả rất chính xác:



![nmap-image](assets/fr/45.webp)



kết quả của việc sử dụng tập lệnh NSE `ftp-anon` trên cổng FTP thông qua Nmap._



Chúng ta thấy kết quả của việc chạy tập lệnh `ftp-anon` trên cổng 21, và không có cổng nào khác, vì chúng ta đã chỉ định tùy chọn `-p 21`. Chúng ta cũng có thể thực hiện quét cổng cơ bản, chỉ chạy tập lệnh NSE `ftp-anon` trên các dịch vụ FTP được phát hiện:



```
# Use a specific NSE script
nmap --script ftp-anon 10.10.10.152
```



Do đó, Nmap cũng sẽ thực hiện thử nghiệm kết nối ẩn danh này nếu nó tìm thấy dịch vụ FTP trên một cổng khác.



Để biết mô tả ngắn gọn về chức năng của tập lệnh NSE, bạn có thể sử dụng tùy chọn `--script-help` được đề cập ở trên:



![nmap-image](assets/fr/46.webp)



giúp hiển thị kết quả cho tập lệnh NSE `sshv1`._



Tóm lại, một lần nữa chúng ta có thể tái sử dụng tất cả các tùy chọn, dịch vụ, phiên bản và công nghệ khám phá mạng mà chúng ta đã sử dụng cho đến nay!



#### C. Quản lý đối số tập lệnh



Trong quá trình sử dụng Nmap, bạn sẽ gặp một số tập lệnh NSE yêu cầu tham số đầu vào để hoạt động chính xác. Bây giờ, chúng ta sẽ xem xét cách truyền tham số cho các tập lệnh này thông qua các tùy chọn của Nmap.



Ví dụ, chúng ta hãy sử dụng tập lệnh `ssh-brute`, cho phép bạn thực hiện tấn công brute force vào dịch vụ SSH.



Một cuộc tấn công brute force cổ điển bao gồm việc thử nghiệm nhiều mật khẩu (đôi khi lên đến hàng triệu) để xác thực một tài khoản cụ thể. Bằng cách thử nhiều mật khẩu như vậy, kẻ tấn công đặt cược vào khả năng người dùng đã sử dụng một mật khẩu yếu trong từ điển mật khẩu được sử dụng cho cuộc tấn công.



Tập lệnh này có các tùy chọn "mặc định", chúng ta có thể tùy chỉnh cho phù hợp với ngữ cảnh. Ví dụ, trong bối cảnh của cuộc tấn công này, chúng ta có thể cung cấp cho Nmap danh sách người dùng và từ điển mật khẩu sẽ được sử dụng. Theo tôi biết, không thể dễ dàng liệt kê các đối số cần thiết cho một tập lệnh, vì vậy cách đáng tin cậy nhất là truy cập trang web chính thức của Nmap. Bạn có thể lấy liên kết trực tiếp đến tài liệu hướng dẫn của tập lệnh NSE bằng cách sử dụng tùy chọn `--script-help`:



![nmap-image](assets/fr/47.webp)



kết quả hiển thị trợ giúp cho tập lệnh `ssh-brute` của NSE với liên kết đến nmap.org._



Bằng cách nhấp vào liên kết được chỉ định, chúng ta sẽ đến trang web này của trang web [https://nmap.org](https://nmap.org/):



![nmap-image](assets/fr/48.webp)



danh sách các đối số có thể được truyền tới tập lệnh NSE `ssh-brute` của Nmap



Ở đây, chúng ta có cái nhìn rõ ràng về các đối số có thể được sử dụng, các đối số chính trong ngữ cảnh của chúng ta là `passdb` (tệp chứa danh sách mật khẩu) và `userdb` (tệp chứa danh sách người dùng). Tài liệu ở đây đề cập đến các thư viện Nmap nội bộ, vì các cơ chế tấn công brute force và các tùy chọn liên quan này được sử dụng thống nhất trên nhiều tập lệnh (`ssh-brute`, `mysql-brute`, `mssql-brute`, v.v.) và do đó sẽ có các đối số tương đối giống nhau:



```
# Create a file containing my user list
echo "root" > /tmp/userlist

# Create a file containing my password list
echo "123456" > /tmp/passlist
echo "NomEntreprise75" >> /tmp/passlist
echo "changezmoi" >> /tmp/passlist

# Run an SSH brute force via Nmap network scan
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```



Như bạn có thể thấy trong lệnh cuối cùng này, chúng ta có thể chỉ định các đối số cần thiết cho tập lệnh Nmap bằng tùy chọn `--scripts-args key=value,key=value`. Dưới đây là kết quả đầu ra của Nmap khi thực hiện tấn công brute force SSH thông qua tập lệnh NSE `ssh-brute`:



![nmap-image](assets/fr/49.webp)



kết quả của việc thực thi SSH bruteforce thông qua Nmap._



Như bạn có thể thấy, thông tin do các tập lệnh NSE tạo ra được thêm tiền tố `NSE: [tên tập lệnh]` trong đầu ra tương tác (đầu ra thiết bị đầu cuối), giúp việc tìm kiếm dễ dàng hơn. Trong màn hình hiển thị kết quả Nmap thông thường, chúng ta chỉ có một bản tóm tắt cho biết liệu các mã định danh yếu đã được phát hiện hay chưa (bao gồm cả mật khẩu, hãy nhớ nhé).



Để tiến xa hơn một bước và nhắc bạn rằng tất cả những điều này có thể được sử dụng cùng với tất cả các tùy chọn mà chúng ta đã xem xét, đây là lệnh sẽ phát hiện mạng `10.10.10.0/24`, quét 2000 cổng TCP thường xuyên nhất và chạy tìm kiếm truy cập ẩn danh trên các dịch vụ FTP và chiến dịch tấn công brute force trên các dịch vụ SSH:



```
# Example of a complete command using multiple scripts
nmap --top-ports 2000 10.10.10.0/24 --script ftp-anon,ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist
```



Đây chỉ là một ví dụ trong số rất nhiều tập lệnh có sẵn và các tùy chọn của chúng. Nhưng giờ đây, chúng ta đã hiểu rõ hơn về cách sử dụng tập lệnh NSE, liệu chúng có yêu cầu đối số hay không và cách truyền các đối số này cho Nmap.



### V. Kết luận



Trong phần này, chúng ta đã tìm hiểu cách sử dụng các tập lệnh NSE của Nmap để thực hiện nhiều tác vụ khác nhau. Tôi mời bạn dành thời gian khám phá các loại tập lệnh khác nhau và bản thân các tập lệnh, để xem chúng có thể tự động hóa bao nhiêu bài kiểm tra.



Trong một số phần, chúng tôi đã tích lũy các tùy chọn khám phá, quét và liệt kê nâng cao hơn hoặc kém hơn. Đến giờ, bạn nên biết rằng đầu ra và hiển thị kết quả của Nmap đang bắt đầu trở nên khá phức tạp, đôi khi thậm chí quá dài dòng đối với thiết bị đầu cuối của chúng tôi. Trong phần tiếp theo, chúng ta sẽ tìm hiểu cách làm chủ đầu ra này, đặc biệt là bằng cách lưu trữ nó trong các tệp ở nhiều định dạng khác nhau.






## 9 - Quản lý dữ liệu đầu ra của Nmap




### I. Trình bày



Trong phần này, chúng ta sẽ xem xét kết quả đầu ra do Nmap tạo ra, đặc biệt là các tùy chọn định dạng khác nhau cho kết quả đầu ra này. Chúng ta sẽ thấy rằng Nmap có thể tạo ra nhiều định dạng đầu ra khác nhau để phù hợp với các nhu cầu khác nhau, và đây cũng là một trong những điểm mạnh của công cụ này.



Theo mặc định, Nmap cung cấp chế độ xem chi tiết về kết quả quét và kiểm tra mà nó thực hiện. Kết quả bao gồm các máy chủ và dịch vụ đã quét, những máy chủ và dịch vụ được phát hiện là có thể truy cập, thông tin chi tiết về các cổng đang mở, trạng thái và phiên bản của chúng. Ngoài ra, thông tin chi tiết về các tập lệnh NSE cũng có sẵn trong đầu ra của thiết bị đầu cuối. Tuy nhiên, đầu ra này có thể nhanh chóng trở nên cồng kềnh, ngay cả khi thông tin được định dạng rõ ràng, điều này có thể gây khó khăn cho việc tìm kiếm thông tin chính xác trong kết quả.



### II. Nắm vững các định dạng đầu ra của Nmap



#### A. Lưu kết quả quét vào tệp văn bản



Để đơn giản hóa mọi việc, [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) cho phép lưu kết quả đầu ra vào một tệp văn bản rất dễ dàng. Điều này có thể hữu ích cho việc lưu trữ, so sánh với các bài kiểm tra khác, nhưng cũng hữu ích cho việc duyệt kết quả đầu ra này bằng các công cụ xử lý văn bản chuyên dụng hoặc ngôn ngữ kịch bản, chẳng hạn như Sublime text, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/), Python, grep, sed, v.v. Để lưu kết quả đầu ra chuẩn của Nmap vào một tệp văn bản, chúng ta có thể sử dụng tùy chọn `-oN <tên tệp>` (chữ "N" trong "normal"):



```
# Save Nmap output to a file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt
```



Không có gì ngạc nhiên khi Nmap sẽ hiển thị đầu ra chuẩn thông thường trong thiết bị đầu cuối của chúng ta, cũng như trong tệp được chỉ định.



#### B. Đầu ra Nmap generate ở định dạng cô đọng



Ngoài ra còn có một định dạng đầu ra thứ hai theo kiểu "văn bản" mà con người có thể dễ dàng hiểu được: định dạng "greppable".



Định dạng này được tạo ra để cung cấp dạng xem "cô đọng" về kết quả đầu ra của Nmap, được cấu trúc sao cho việc xử lý được dễ dàng hơn bằng các công cụ như `grep`. Hãy cùng xem một ví dụ về loại kết quả đầu ra này:



![nmap-image](assets/fr/50.webp)



quét mạng nmap và xuất ra định dạng "greppable"._



Ở đây, tôi đã thực hiện khám phá mạng, quét cổng và phân tích các công nghệ và phiên bản trên mạng /24, sau đó lưu trữ kết quả đầu ra trong một tệp ở định dạng "greppable". Tôi kết thúc bằng một tệp chứa 2 dòng cho mỗi máy chủ đang hoạt động:





- Dòng đầu tiên cho tôi biết rằng máy chủ này hay máy chủ kia là _Up_;





- Dòng thứ hai cho tôi biết cổng nào đã được quét, trạng thái của chúng và thông tin về công nghệ và phiên bản được lấy theo định dạng rất cụ thể: `<port>/<status/<protocol>//<service>//<version>/,`




Định dạng này với dấu phân cách cố định cho phép xử lý nhanh chóng bằng các công cụ xử lý văn bản như `grep`, hoặc các ngôn ngữ lập trình và tập lệnh. Ví dụ, lệnh sau cho phép tôi dễ dàng truy xuất thông tin về máy chủ `10.10.10.5` trong trường hợp Nmap thực hiện một đợt quét lớn mà kết quả đầu ra sẽ khó duyệt:



```
# Filter by IP address in the Nmap "greppable" file
grep '10.10.10.5' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Status: Up
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)
```



Ngược lại, tôi cũng có thể dễ dàng liệt kê tất cả các máy chủ có cổng 21 mở vì cổng và IP nằm trên cùng một dòng:



```
# Filter by open port in the Nmap "greppable" file
grep '21/open' nmap_10.10.10.0.gnmap
Host: 10.10.10.5 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Microsoft IIS httpd 7.5/ Ignored State: filtered (998)

Host: 10.10.10.152 () Ports: 21/open/tcp//ftp//Microsoft ftpd/, 80/open/tcp//http//Indy httpd 18.1.37.13946 (Paessler PRTG bandwidth monitor)/, 135/open/tcp//msrpc//Microsoft Windows RPC/, 139/open/tcp//netbios-ssn//Microsoft Windows netbios-ssn/, 445/open/tcp//microsoft-ds//Microsoft Windows Server 2008 R2 - 2012 microsoft-ds/ Ignored State: closed (995)
```



Để xuất ra kết quả như vậy, chúng ta cần sử dụng tùy chọn `-oG <tên tệp>.gnmap` (chữ "G" trong "grep"). Theo thói quen, tôi sử dụng phần mở rộng `.gnmap` cho một tệp như vậy, nhưng bạn có thể thoải mái sử dụng tùy chọn nào bạn thích:



```
# Save Nmap output to a file in "greppable" format
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap
```



Định dạng này có thể được sử dụng cho nhiều mục đích khác nhau và đặc biệt hữu ích cho việc soạn thảo/sắp xếp nhanh. Tuy nhiên, nó đang có xu hướng bị bỏ qua để chuyển sang định dạng mà chúng ta sẽ xem xét tiếp theo.



Lưu ý: Định dạng `-oG` greppable đã chính thức bị loại bỏ kể từ Nmap 7.90. Tuy nhiên, nó vẫn có thể được sử dụng vì lý do tương thích. Tuy nhiên, chúng tôi khuyến nghị bạn nên sử dụng định dạng XML hoặc định dạng chuẩn cho bất kỳ quá trình phát triển hoặc phân tích cú pháp tự động nào.



#### C. Định dạng XML cho đầu ra Nmap



Định dạng cuối cùng đáng đề cập trong hướng dẫn này là XML. Không giống như hai định dạng trước, định dạng này không được thiết kế để con người đọc, mà để các công cụ hoặc tập lệnh khác đọc.



XML (_eXtensible Markup Language_) là ngôn ngữ đánh dấu được sử dụng để lưu trữ và vận chuyển dữ liệu, cung cấp cấu trúc phân cấp thông qua các thẻ tùy chỉnh.



Trong Nmap, định dạng XML được sử dụng để tạo báo cáo chi tiết về các lần quét đã thực hiện, bao gồm thông tin về máy chủ, cổng và lỗ hổng được phát hiện, cũng như thông tin bổ sung không được hiển thị trong đầu ra Nmap tiêu chuẩn.



Để xuất tệp đầu ra theo định dạng XML của generate, chúng ta cần sử dụng tùy chọn `-oX` ("O" từ "XML"):



```
# Save Nmap output to a file in XML format
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```



Kết quả là đầu ra chuẩn của Nmap trong thiết bị đầu cuối của bạn, cũng như một tệp ở định dạng XML trong thư mục hiện tại của bạn.



Tất nhiên, định dạng XML không được thiết kế để con người có thể đọc và diễn giải. Tuy nhiên, nếu bạn muốn thực hiện viết mã hoặc phân tích tự động trên định dạng đầu ra Nmap này, bạn vẫn cần nắm rõ các thẻ và cấu trúc được sử dụng. Ví dụ: đây là một phần nội dung của tệp XML do Nmap tạo ra, hiển thị kết quả quét cho 1 máy chủ:



![nmap-image](assets/fr/51.webp)



ví dụ về bản ghi XML cho 1 máy chủ trong quá trình quét Nmap



Có rất nhiều thông tin ở đây và chúng tôi đặc biệt quan tâm đến hai cổng mở:



```
<port protocol="tcp" portid="21"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="ftp" product="Microsoft ftpd" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:ftp_service</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<port protocol="tcp" portid="80"><state state="open" reason="syn-ack" reason_ttl="0"/><service name="http" product="Microsoft IIS httpd" version="7.5" ostype="Windows" method="probed" conf="10"><cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Chúng tôi hiểu rằng định dạng này sẽ tạo điều kiện thuận lợi cho việc phân tích kết quả tự động, vì mỗi thông tin được sắp xếp gọn gàng trong một thẻ hoặc thuộc tính được đặt tên riêng. Đặc biệt, chúng tôi tìm thấy một thông tin mà trước đây chúng tôi chưa từng gặp: CPE.



```
cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
<cpe>cpe:/a:microsoft:internet_information_services:7.5</cpe><cpe>cpe:/o:microsoft:windows</cpe></service></port>
```



Chúng tôi đã đề cập ngắn gọn về CPE trong phần 2 của mô-đun 2, và thông tin này được xác định thông qua các kết quả trùng khớp trong quá trình phát hiện phiên bản. Nmap sử dụng dịch vụ, công nghệ và cơ chế phát hiện phiên bản để tìm CPE liên quan.



Điều này cho phép chúng tôi tái sử dụng thông tin này với các cơ sở dữ liệu và ứng dụng sử dụng nó. Tôi đặc biệt nghĩ đến cơ sở dữ liệu NVD, nơi tham chiếu đến các CVE. Với mỗi CVE, nó chứa các CPE bị ảnh hưởng bởi lỗ hổng bảo mật. Dưới đây là ví dụ về một CVE liên quan đến `a:microsoft:internet_information_services:7.5` từ cơ sở dữ liệu NVD:



![nmap-image](assets/fr/52.webp)



sự hiện diện của CPE trong các chi tiết của CVE trong cơ sở dữ liệu NVD



Hiện nay, chúng ta đã hiểu rõ hơn về lợi ích của định dạng này, định dạng này cung cấp cấu trúc thông tin rất rõ ràng và chứa tất cả dữ liệu được Nmap thu thập hoặc xử lý.



Theo phản xạ, tôi thường xuyên lưu các bản quét Nmap của mình ở cả ba định dạng cùng một lúc. Điều này được thực hiện nhờ tùy chọn `-oA <tên>` ("A" nghĩa là "Tất cả"), tùy chọn này sẽ tạo một tệp `<tên>.nmap`, một tệp `<tên>.xml` và một tệp `<tên>.gnmap`. Bằng cách này, tôi chắc chắn sẽ không bị hết dữ liệu khi cần xem lại kết quả.



Với ba định dạng này, bạn sẽ có mọi thứ cần thiết để lưu và cuối cùng là xử lý kết quả Nmap một cách tự động. Chúng ta sẽ sử dụng lại định dạng XML trong phần tiếp theo, khi tìm hiểu về việc sử dụng Nmap với các công cụ bảo mật khác.



#### III. Tạo báo cáo HTML từ bản quét Nmap



Định dạng XML cung cấp nhiều khả năng, đặc biệt là khả năng làm cơ sở để tạo báo cáo ở định dạng HTML, giúp duyệt báo cáo dễ dàng hơn về mặt hình ảnh.



Để chuyển đổi tệp Nmap ở định dạng XML thành trang web, chúng ta sẽ sử dụng công cụ `xsltproc`, công cụ mà chúng ta cần cài đặt trước:



```
# Install the xsltproc tool
sudo apt install xsltproc
```



Sau khi cài đặt công cụ này, bạn chỉ cần cung cấp cho nó tệp XML cần chuyển đổi và tên báo cáo HTML cần tạo:



```
# Create an Nmap HTML report from XML
xsltproc nmap_10.10.10.0.xml -o "Nmap – rapport web 05-2024.html"

# Open the .html file with Firefox
firefox "Nmap – rapport web 05-2024.html"
```



Kết quả là, toàn bộ bản quét của chúng ta sẽ được cấu trúc đẹp mắt, thậm chí có một vài màu sắc và các liên kết có thể nhấp vào trong mục lục!



![nmap-image](assets/fr/53.webp)



trích xuất từ báo cáo quét Nmap ở định dạng HTML được tạo bởi xsltproc._



Nói chung, tệp XML được Nmap lưu có chứa tham chiếu đến một tệp khác ở định dạng XSL:



```
<?xml-stylesheet href="/usr/share/nmap/nmap.xsl" type="text/xsl"?>
```



Do đó, việc chuyển đổi sang HTML là một chức năng được Nmap cung cấp và hỗ trợ, trong đó `xsltproc` là một công cụ phổ biến và được công nhận để thực hiện tác vụ này (không có trong bộ công cụ Nmap).



XSLT (_Chuyển đổi ngôn ngữ bảng định kiểu mở rộng_) là một tập hợp con của XSL cho phép hiển thị dữ liệu XML trên trang web và được "chuyển đổi", song song với các kiểu XSL, thành thông tin có thể đọc được, được định dạng theo định dạng HTML.



nguồn: [helpx.adobe.com/](https://helpx.adobe.com/fr/dreamweaver/using/xml-xslt.html)_



Mức độ thông tin trong báo cáo tương đương với định dạng XML của Nmap và cao hơn mức đầu ra của thiết bị đầu cuối tiêu chuẩn (_đầu ra tương tác_).



### IV. Quản lý mức độ chi tiết của Nmap



Bây giờ chúng ta sẽ xem xét một số tùy chọn cho Debugger Nmap hoặc để theo dõi tiến trình của nó.



Tùy chọn đầu tiên chúng ta nên đề cập là tùy chọn `-v`, giúp tăng tính chi tiết của Nmap. Dưới đây là một ví dụ:



![nmap-image](assets/fr/54.webp)



đầu ra chi tiết của nmap sử dụng tùy chọn `-v`._



Khi quét nhắm mục tiêu đến nhiều máy chủ và cổng, đầu ra của thiết bị đầu cuối sẽ trở nên khó khai thác do lượng thông tin hiển thị. Vì lý do này, tùy chọn này nên được sử dụng kết hợp với các tùy chọn đã thấy trước đó, cho phép bạn lưu trữ đầu ra tiêu chuẩn của Nmap trong một tệp. Thông tin liên quan đến việc sử dụng mức độ chi tiết sẽ không được bao gồm trong tệp đầu ra này. Như bạn có thể thấy từ ví dụ trên, mức độ chi tiết này cho phép bạn theo dõi các hành động và phát hiện của Nmap một cách rõ ràng và trực tiếp. Đối với các lần quét dài hơn, khi dữ liệu hiển thị có thể chậm, tùy chọn này giúp bạn tránh bị bỏ qua hoạt động hiện tại của Nmap và biết mọi thứ đang tiến triển như thế nào và với tốc độ nào. Để tăng mức độ chi tiết lên một mức nữa, bạn có thể sử dụng tùy chọn `-vv`.



Để theo dõi hoạt động của Nmap trong quá trình quét, bạn có thể sử dụng tùy chọn `--packet-trace`. Với tùy chọn `--v`, chúng ta sẽ nhận được nhật ký trực tiếp của tất cả các cổng mở được Nmap phát hiện, trong khi với tùy chọn này, chúng ta sẽ nhận được một dòng nhật ký cho mỗi gói tin được gửi đến một cổng. Điều này tự nhiên tạo ra một kết quả rất chi tiết, nhưng cho phép theo dõi chi tiết hoạt động của Nmap, đây là một ví dụ:



![nmap-image](assets/fr/55.webp)



giám sát chi tiết hoạt động của Nmap thông qua `--packet-trace`._



Một lần nữa, thông tin này sẽ không được ghi lại trong tệp đầu ra do Nmap tạo ra nếu các tùy chọn `-oN`, `-oG`, `-oX` hoặc `-oA` được sử dụng.



Cuối cùng, Nmap cũng cung cấp hai tùy chọn gỡ lỗi: `-d` và `-dd`. Các tùy chọn này hoạt động tương tự như tùy chọn chi tiết `-v`, nhưng bổ sung thêm thông tin kỹ thuật, chẳng hạn như tóm tắt các thông số kỹ thuật khi bắt đầu quét:



![nmap-image](assets/fr/56.webp)



các tùy chọn thời gian được hiển thị trong chế độ xem gỡ lỗi của Nmap



Trong một vài phần tiếp theo, chúng ta sẽ xem xét các tùy chọn "Thời gian" là gì và tại sao bạn nên biết về chúng.



Cuối cùng, nếu bạn chỉ muốn có cái nhìn tổng quan cơ bản về tiến trình quét Nmap, bạn có thể sử dụng tùy chọn `--stats-every 5s`. "5s" ở đây nghĩa là 5 giây và có thể được điều chỉnh cho phù hợp với nhu cầu của bạn. Đây là tần suất chúng tôi sẽ nhận được phản hồi từ Nmap về tiến trình quét:



![nmap-image](assets/fr/57.webp)



thông tin được hiển thị bởi tùy chọn `--stats-every` của Nmap



Cụ thể, chúng ta có thể nhận được phần trăm tiến độ cũng như chỉ báo về giai đoạn hiện tại: giai đoạn phát hiện máy chủ thông qua [ping](https://www.it-connect.fr/le-ping-pour-les-debutants/), giai đoạn phát hiện các cổng TCP bị lộ, v.v. Thông tin này cũng có thể được lấy ở đầu ra của thiết bị đầu cuối bằng cách nhấn "Enter" trong khi quét.



Tuy nhiên, Nmap không thực sự hiệu quả trong việc ước tính thời gian thực hiện một tác vụ, một phần vì công cụ này không biết trước cần phải quét bao nhiêu máy chủ và dịch vụ.



### V. Kết luận



Trong phần này, chúng ta đã xem xét một số tùy chọn để lưu kết quả quét Nmap ở các định dạng tệp khác nhau. Điều này sẽ rất hữu ích, vì trong thực tế, kết quả quét có thể chiếm hàng trăm hoặc thậm chí hàng nghìn dòng! Chúng ta cũng đã tìm hiểu cách tăng mức độ chi tiết của Nmap cho mục đích gỡ lỗi hoặc để có được báo cáo tiến trình quét.



Định dạng XML sẽ đặc biệt hữu ích trong phần tiếp theo, nơi chúng ta sẽ xem xét một số công cụ có thể hoạt động với kết quả Nmap.




## 10 - Sử dụng Nmap với các công cụ bảo mật khác



### I. Trình bày



Trong phần này, chúng ta sẽ xem xét một số cách sử dụng Nmap kinh điển với các công cụ bảo mật mã nguồn mở và miễn phí khác. Cụ thể, chúng ta sẽ áp dụng những kiến thức đã học được trong các phần trước để nâng cao hơn nữa sức mạnh và hiệu quả của Nmap.



Khả năng lưu kết quả quét Nmap dưới dạng XML giúp dữ liệu tương thích với nhiều công cụ khác. Vì hầu hết các ngôn ngữ lập trình và kịch bản hiện nay đều có thư viện có khả năng phân tích cú pháp XML, điều này giúp việc xử lý dữ liệu này dễ dàng hơn nhiều. Một số công cụ, đặc biệt là các công cụ hướng đến bảo mật tấn công, có các hàm để xử lý định dạng XML do Nmap tạo ra. Hãy cùng xem xét kỹ hơn.



Tôi sẽ đề cập đến một số công cụ tấn công mà không đi sâu vào chi tiết cách sử dụng hoặc cách thức hoạt động của chúng. Tôi giả định rằng người đọc đã quen thuộc với cách sử dụng cơ bản và đã vận hành thành thạo. Phần này sẽ đặc biệt hữu ích cho các chuyên gia [an ninh mạng] (https://www.it-connect.fr/cours-tutoriels/securite-informatique/), những người đang được đào tạo hoặc những người đã quyết định tìm hiểu sâu hơn về chủ đề này.



### II. Nhập kết quả Nmap vào Metasploit



Công cụ đầu tiên chúng ta sẽ xem xét để tái sử dụng dữ liệu Nmap trong nghiên cứu bảo mật và lỗ hổng tấn công là Metasploit.



Metasploit là một nền tảng khai thác và tấn công. Đây là một giải pháp miễn phí và là một công cụ được công nhận, chứa một số lượng lớn các mô-đun được viết bằng Ruby hoặc Python. Các mô-đun này cho phép khai thác lỗ hổng, thực hiện các cuộc tấn công, tạo cửa hậu, quản lý các lệnh gọi lại (C&C hoặc các chức năng Truyền thông và Kiểm soát) và mọi thứ đều được sử dụng thống nhất.



Đặc biệt, hệ điều hành nổi tiếng và được sử dụng rộng rãi này có thể hoạt động với [cơ sở dữ liệu] postgreSQL(https://www.it-connect.fr/cours-tutoriels/administration-systemes/stockage/bdd/) trong đó lưu trữ máy chủ, cổng, dịch vụ, thông tin xác thực, v.v.





- Tài liệu chính thức của Metasploit: [https://docs.metasploit.com/](https://docs.metasploit.com/)




Đây chính là lúc Nmap và đầu ra của nó phát huy tác dụng, vì định dạng XML của đầu ra Nmap có thể dễ dàng được nhập vào cơ sở dữ liệu của Metasploit để điền vào cơ sở dữ liệu máy chủ và dịch vụ, sau đó có thể nhanh chóng chỉ định chúng làm mục tiêu cho cuộc tấn công này hay cuộc tấn công khác.



Khi đã vào được shell tương tác Metasploit, tôi bắt đầu bằng cách tạo một không gian làm việc, một loại không gian cụ thể cho môi trường làm việc trong ngày của tôi:



```
# Create a Metasploit workspace
msf6 > workspace -a SI_siege
```



Sau khi không gian làm việc của tôi được tạo, chúng ta cần xác thực rằng giao tiếp với cơ sở dữ liệu đang hoạt động:



```
# Retrieve the database status
msf6 > db_status
[*] Connected to msf. Connection type: postgresql.
```



Cuối cùng, chúng ta có thể sử dụng lệnh Metasploit `db_import` để nhập bản quét Nmap của mình ở định dạng XML:



```
# Import a Nmap XML file into the database
msf6> db_import /tmp/nmap_10.10.10.0.xml
```



Sau đây là kết quả khi thực hiện tất cả các lệnh này:



![nmap-image](assets/fr/58.webp)



nhập bản quét Nmap ở định dạng XML vào cơ sở dữ liệu Metasploit



Tại đây, bạn có thể thấy mỗi máy chủ được nhập cùng với các dịch vụ của nó. Dữ liệu này sau đó có thể được hiển thị thông qua lệnh `services` hoặc `services -p <port>` cho một dịch vụ cụ thể:



![nmap-image](assets/fr/59.webp)



danh sách các dịch vụ được nhập từ tệp XML vào cơ sở dữ liệu Metasploit



Cuối cùng, chúng ta có thể nhanh chóng và dễ dàng tái sử dụng dữ liệu này trong một mô-đun nhờ tùy chọn `-R`, tùy chọn này sẽ "chuyển đổi" danh sách các dịch vụ thu được làm đầu vào cho chỉ thị `RHOSTS`, được sử dụng để chỉ định mục tiêu tấn công. Dưới đây là một ví dụ với mô-đun `ssh_login`, cho phép bạn thực hiện một cuộc tấn công brute force vào các dịch vụ [SSH] (https://www.it-connect.fr/cours/comprendre-et-maitriser-ssh/):



![nmap-image](assets/fr/60.webp)



sử dụng tùy chọn `services -R` để nhập các dịch vụ được chỉ định là mục tiêu của cuộc tấn công



Đây chỉ là một ví dụ nhỏ về những gì có thể làm với dữ liệu Nmap trong Metasploit, nhưng nó cho bạn một cái nhìn tổng quan về việc thông tin này có thể được tái sử dụng nhanh chóng và dễ dàng như thế nào trong các bài kiểm tra xâm nhập, quét lỗ hổng hoặc tấn công mạng. Cũng cần đề cập rằng Nmap có thể được chạy trực tiếp từ Metasploit để nhập kết quả vào cơ sở dữ liệu (lệnh `db_nmap`), một chủ đề thú vị khác cần được đề cập!



### III. Sử dụng Nmap với trình quét web Aquatone



Công cụ thứ hai tôi muốn giới thiệu trong phần này về việc tái sử dụng kết quả Nmap để phân tích lỗ hổng bảo mật và tấn công là Aquatone.



Aquatone là một trình quét web được thiết kế để khám phá hiệu quả các ứng dụng web trên mạng. Nó cung cấp các tính năng nâng cao để khám phá dịch vụ web, nhận dạng tên miền phụ, phân tích cổng và lấy dấu vân tay ứng dụng web. Tất cả được trình bày rõ ràng và súc tích dưới dạng báo cáo HTML, JSON và văn bản để dễ dàng phân tích bảo mật web.



Tương tự như Metasploit, Aquatone có thể xử lý trực tiếp định dạng XML của Nmap và sử dụng nó làm mục tiêu quét. Cụ thể, nó chỉ có thể trích xuất các máy chủ và dịch vụ quan tâm (dịch vụ web) từ tất cả dữ liệu mà báo cáo Nmap có thể chứa.





- Liên kết công cụ: [Github - Michenriksen/aquatone](https://github.com/michenriksen/aquatone)




Để sử dụng đầu ra XML của Nmap với Aquatone, chỉ cần gửi tệp XML vào một đường ống (pipe) mà Aquatone sẽ sử dụng. Dưới đây là một ví dụ:



```
# Send the Nmap XML output to Aquatone
cat /tmp/nmap_10.10.10.0.xml | ./aquatone -nmap
```



Trong khi Aquatone thường thực hiện khám phá cổng trên máy chủ để tìm dịch vụ web, trong bối cảnh này, nó sẽ chỉ dựa vào kết quả của Nmap, vốn đã thực hiện thao tác này, do đó tiết kiệm thời gian:



![nmap-image](assets/fr/61.webp)



sử dụng kết quả Nmap ở định dạng XML với `aquatone`._



Để bạn tham khảo, sau đây là trích đoạn từ báo cáo do Aquatone thực hiện:



![nmap-image](assets/fr/62.webp)



ví dụ về báo cáo `aquatone`



Cá nhân tôi thường sử dụng Aquatone để có cái nhìn tổng quan nhanh về các loại trang web có trên mạng, đặc biệt là nhờ chức năng chụp ảnh màn hình của nó.



Một lần nữa, việc có báo cáo Nmap hoàn chỉnh ở định dạng XML sẽ tiết kiệm thời gian và dễ dàng sử dụng lại trong công cụ khác.



### IV. Kết luận



Hai ví dụ này cho thấy rõ ràng định dạng XML của Nmap giúp các công cụ khác dễ dàng sử dụng kết quả của nó, vì đây là định dạng dữ liệu có cấu trúc và dễ sử dụng. Có nhiều công cụ khác có khả năng xử lý những kết quả này, chẳng hạn như công cụ báo cáo tự động, biểu diễn đồ họa hoặc các trình quét lỗ hổng độc quyền phức tạp hơn.



Tất nhiên, bạn cũng có thể phát triển các tập lệnh và công cụ của riêng mình bằng Python, [PowerShell](https://www.it-connect.fr/cours-tutoriels/administration-systemes/scripting/powershell/) hoặc bất kỳ ngôn ngữ nào khác có thư viện phân tích cú pháp XML để thao tác và tái sử dụng dữ liệu kết quả Nmap theo ý muốn.



Phần này đưa chúng ta đến phần cuối của mô-đun hướng dẫn về cách sử dụng Nmap nâng cao hơn, đặc biệt là để quét lỗ hổng thông qua các tập lệnh NSE.



Phần tiếp theo của hướng dẫn sẽ tập trung vào một số phương pháp hay nhất và mẹo kỹ thuật bổ sung về các chế độ quét cụ thể mà Nmap có thể thực hiện. Chúng ta cũng sẽ xem xét các tùy chọn tối ưu hóa hiệu suất quét, đặc biệt hữu ích khi quét các mạng lớn.




## 11 - Cải thiện hiệu suất quét mạng



### I. Trình bày



Trong chương này, chúng ta sẽ tìm hiểu cách tối ưu hóa tốc độ quét mạng được thực hiện với Nmap bằng cách sử dụng các tùy chọn cụ thể khác nhau. Cụ thể, chúng ta sẽ tìm hiểu thêm về hoạt động bên trong của Nmap, từ quản lý thời gian chờ đến các cấu hình được lưu sẵn của công cụ.



Sau khi đã tìm hiểu kỹ về các tính năng của Nmap, hãy cùng khám phá sức mạnh của nó. Nếu bạn đã từng sử dụng công cụ này trên các mạng lớn, có lẽ bạn đã nhận thấy một số lần quét có thể mất nhiều thời gian, bất chấp sức mạnh của nó. Và lý do chính đáng là: một lệnh `nmap` đơn giản với một vài tùy chọn có thể quét hàng triệu gói tin nhắm mục tiêu đến hàng trăm nghìn hệ thống và dịch vụ tiềm năng.



Hơn nữa, một số cấu hình thiết bị mạng có thể cố tình áp dụng tốc độ chậm hơn (số gói tin mỗi giây), có nguy cơ từ chối các gói tin của bạn hoặc cấm IP Address của bạn vì lý do bảo mật.



Tùy thuộc vào ngữ cảnh, có thể bạn sẽ muốn thử và tối ưu hóa tất cả những điều này, như chúng ta sẽ thấy trong chương này.



Trong mọi trường hợp, bạn có thể kiểm tra các giá trị mặc định của các tham số mà chúng ta sẽ xem xét, cũng như liệu các tùy chọn bạn sẽ sử dụng đã được tính đến chính xác hay chưa, thông qua gỡ lỗi Nmap (tùy chọn `-d` đã thấy trong chương trước):



![nmap-image](assets/fr/63.webp)



xem các tùy chọn Thời gian thông qua tùy chọn `-d` của Nmap._



### II. Quản lý tốc độ quét Nmap



#### A. Quản lý song song hóa



Theo mặc định, Nmap sử dụng chế độ song song hóa trong quá trình quét để tối ưu hóa, và tất cả các tham số mà nó sử dụng đều có thể được điều chỉnh thông qua nhiều tùy chọn khác nhau. Tuy nhiên, những trường hợp thực sự cần điều chỉnh các tham số này khá hiếm, vì vậy chúng tôi sẽ không đi sâu vào chi tiết trong hướng dẫn này:





- `--min-hostgroup/max-hostgroup <size>`: kích thước của nhóm quét máy chủ song song.





- `--min-parallelism/max-parallelism <numprobes>`: song song hóa các Probe.





- `--scan-delay/--max-scan-delay <thời gian>`: điều chỉnh độ trễ giữa các lần thăm dò.




Chỉ cần biết rằng chúng tồn tại và có thể sử dụng được.



#### B. Quản lý số lượng gói tin mỗi giây



Theo mặc định, Nmap tự điều chỉnh số lượng gói tin mỗi giây được gửi theo phản hồi của mạng. Tuy nhiên, bạn có thể thiết lập cài đặt này bằng cách xác định giá trị cao nhất và/hoặc giá trị tối thiểu cần tuân theo theo số lượng gói tin mỗi giây. Cài đặt này được thực hiện bằng các tùy chọn `--min-rate <số>` và `--max-rate <số>`, trong đó `number` biểu thị số lượng gói tin mỗi giây. Ví dụ:



```
# Limit the scan speed to 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300
```



Các tùy chọn này cho phép bạn điều chỉnh tốc độ quét theo nhu cầu cụ thể, để tăng tốc quá trình hoặc giới hạn băng thông sử dụng. Trường hợp sau (giới hạn tốc độ quét) là trường hợp có nhiều khả năng dẫn bạn đến các tùy chọn này, đặc biệt nếu bạn gặp phải tình trạng trễ mạng khi sử dụng Nmap (điều này khá hiếm khi xảy ra).



### III. Quản lý lỗi kết nối và thời gian chờ



Một tham số khác mà chúng ta có thể sử dụng để tối ưu hóa tốc độ quét Nmap (hoặc đảm bảo độ chính xác cao hơn) liên quan đến _timeout_ và _retry_.



Đối với _timeouts_, đây là **thời gian chờ không phản hồi** mà sau đó Nmap sẽ ngừng chờ phản hồi và coi dịch vụ hoặc máy chủ không thể truy cập được. Đối với _retry_, đây là **số lần thử liên tiếp một thao tác** mà Nmap sẽ thực hiện trước khi tiếp tục.



Tương tự như song song hóa, quản lý _timeout_ và _retry_ có thể được áp dụng cho các giai đoạn khám phá dịch vụ hoặc máy chủ:





- `--min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <thời gian>`: chỉ định thời gian khứ hồi của Exchange. Một lần nữa, tham số này thực sự được tính toán và điều chỉnh ngay trong quá trình quét. Bạn có thể không cần sử dụng nó, vì Nmap tính toán thời gian này ngay lập tức dựa trên phản ứng của mạng.





- `--max-retries <số>`: giới hạn số lần truyền lại gói tin trong quá trình quét cổng. Theo mặc định, Nmap có thể thực hiện tối đa 10 lần thử lại cho một dịch vụ, đặc biệt nếu phát hiện độ trễ hoặc mất gói tin ở cấp độ mạng, nhưng trong hầu hết các trường hợp, chỉ thực hiện một lần.





- `--host-timeout <thời gian>`: chỉ định thời gian tối đa Nmap sẽ dành cho một máy chủ cho tất cả các hoạt động của nó, bao gồm quét cổng, phát hiện dịch vụ và bất kỳ hoạt động nào khác liên quan đến máy chủ đó. Nếu vượt quá khoảng thời gian này mà không có phản hồi hoặc **hoàn thành hoạt động** nào, Nmap sẽ bỏ qua máy chủ này mà không hiển thị bất kỳ kết quả nào liên quan đến nó và chuyển sang máy chủ tiếp theo trong danh sách. Điều này cho phép bạn kiểm soát thời gian tối đa Nmap dành cho một máy chủ nhất định, tránh bị kẹt trên các máy chủ kháng cự và tối ưu hóa thời gian quét tổng thể.




Trong công việc hàng ngày, tôi sử dụng các tùy chọn `--max-retries` và `--host-timeout` để tối ưu hóa quá trình quét của mình:



```
# Optimization of a scan with 0 additional attempts and a timeout of 15 minutes per host
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m
```



Các tham số này cung cấp thêm tính linh hoạt để điều chỉnh hành vi quét theo nhu cầu cụ thể và điều kiện mạng. Tuy nhiên, bạn cần lưu ý đến tác động của chúng đối với tải trên máy chủ được quét và khả năng mất độ chính xác.



### IV. Sử dụng các cấu hình đã chuẩn bị



Các tùy chọn khác nhau mà chúng ta đã thấy trong chương này có thể được sử dụng riêng lẻ hoặc như một phần của các cấu hình có sẵn do Nmap cung cấp. Tùy chọn cho phép sử dụng các _template_ (mẫu cấu hình) này là `-T <số>` hoặc `-T <tên>`. Có 5 cấp độ _template_ có thể sử dụng:



```
-T<0-5>: Set timing template (higher is faster)
```



Theo mặc định, Nmap sử dụng _template_ 3 (_normal_), nhìn chung là đủ.



Về phần mình, tôi thường làm việc trong những bối cảnh mà tôi cần phải khá nhanh (trong khi vẫn phải hoàn thiện nhất có thể) và tôi thường xuyên sử dụng tùy chọn `-T4`.



```
# Use Nmap for a network scan with preset T4 (with debug)
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```



Sau đây là thông tin gỡ lỗi cho lần quét này cho chúng ta thấy:



![nmap-image](assets/fr/64.webp)



sử dụng thiết lập `-T4` trong quá trình quét Nmap



### V. Kết luận



Trong chương này, chúng ta đã xem xét các kỹ thuật và tùy chọn khác nhau mà bạn có thể sử dụng để quản lý sức mạnh, tính năng và hiệu suất của Nmap. Các tùy chọn này đặc biệt hữu ích khi quét các mạng lớn, và hiếm khi được sử dụng cho mục đích ẩn danh.



Trong chương tiếp theo, chúng ta sẽ xem xét một số phương pháp hay nhất để sử dụng Nmap và đảm bảo tính an toàn của nó.




## 12 - Bảo mật và bảo mật dữ liệu khi sử dụng Nmap



### I. Trình bày



Trong chương này, chúng ta sẽ xem xét một số biện pháp tốt cần áp dụng liên quan đến bảo mật và trên hết là tính bảo mật của dữ liệu được Nmap tạo ra, xử lý và lưu trữ.



Việc sử dụng Nmap trong hệ thống thông tin có thể nhanh chóng bị coi là hành vi tấn công. Do đó, cần thực hiện một số biện pháp phòng ngừa để hành động trong khuôn khổ pháp lý, đồng thời đảm bảo an ninh cho các mục tiêu dự kiến, dữ liệu được thu thập và hệ thống được sử dụng để quét.



### II. Xin giấy phép phù hợp



Trước khi quét mạng hoặc hệ thống, hãy đảm bảo bạn đã được cấp phép phù hợp. Việc quét hệ thống để tìm lỗ hổng bảo mật (`tập lệnh NSE`) mà không được cấp phép có thể là bất hợp pháp và có thể dẫn đến hậu quả pháp lý, đặc biệt nếu bảo mật hệ thống thông tin không nằm trong phạm vi trách nhiệm chính thức của bạn.





- Xin nhắc lại: [Bộ luật Hình sự: Chương III: Tấn công vào hệ thống xử lý dữ liệu tự động](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000030939438/)




### III. Bảo vệ dữ liệu nhạy cảm



Kết quả do Nmap tạo ra có thể được coi là nhạy cảm, đặc biệt khi chúng chứa thông tin về các điểm yếu trong hệ thống thông tin có thể bị kẻ tấn công khai thác. Tuy nhiên, kết quả cũng có thể bị coi là nhạy cảm khi liên quan đến các hệ thống không phải ai cũng có thể truy cập (ví dụ: hệ thống thông tin nhạy cảm, công nghiệp, y tế hoặc [dự phòng] (https://www.it-connect.fr/cours-tutoriels/administration-systemes/autres/sauvegarde/)).



Chúng tôi cũng thấy rằng, tùy thuộc vào các tập lệnh NSE được sử dụng, kết quả quét NSE của [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) cũng có thể chứa các mã định danh.



Do đó, một cá nhân có ý đồ xấu tìm cách truy cập vào các kết quả quét này sẽ có trong tay bản đồ hệ thống thông tin và rất nhiều thông tin kỹ thuật mà không cần phải tự mình thực hiện các hành động này, đồng thời có nguy cơ bị phát hiện.



Do đó, điều quan trọng là phải cẩn thận không thu thập hoặc lưu trữ thông tin nhạy cảm một cách không phù hợp khi sử dụng Nmap, bao gồm nhưng không giới hạn ở những điều sau:





- Mã hóa dữ liệu đầu ra: Nếu bạn cần lưu trữ hoặc truyền kết quả quét Nmap, hãy đảm bảo mã hóa chúng để bảo vệ tính bảo mật của dữ liệu. Điều này sẽ ngăn chặn việc đánh cắp thông tin nhạy cảm trái phép. Lý tưởng nhất là dữ liệu nên được mã hóa ngay khi rời khỏi hệ thống được sử dụng để thực hiện quét (một tệp ZIP được mã hóa bằng mật khẩu mạnh là một khởi đầu rất tốt).





- Thiết lập kiểm soát truy cập: đảm bảo chỉ những người được ủy quyền mới có quyền truy cập vào kết quả quét Nmap của bạn, nơi chúng sẽ được lưu trữ. Thiết lập kiểm soát truy cập phù hợp để bảo vệ thông tin nhạy cảm khỏi bị truy cập trái phép.





- Thận trọng khi xử lý dữ liệu: khi truyền, sao chép hoặc xử lý dữ liệu quét, hãy đảm bảo bạn kiểm soát chặt chẽ vấn đề bảo mật dữ liệu. Điều này có nghĩa là: không để dữ liệu nằm rải rác trong thư mục `Tải xuống` của máy trạm được kết nối Internet, không để dữ liệu được truyền qua ứng dụng tệp HTTP nội bộ Exchange, không để Notepad mở mà không khóa máy trạm trong giờ nghỉ trưa, v.v.




### IV. Quản lý quét tích cực



Như chúng ta đã thấy trong suốt hướng dẫn này, Nmap có thể rất dài dòng ở cấp độ mạng. Nó cũng có thể gửi các gói tin không được định dạng đúng và không tuân thủ nghiêm ngặt cấu trúc giao thức trong các khung mạng và các gói tin mà nó tạo ra. Tất cả những hành động này có thể ảnh hưởng đến một số hệ thống và dịch vụ, đôi khi đến mức gây ra sự cố hoặc quá tải tài nguyên hệ thống và mạng.



Để tránh mọi sự cố, bạn cần nắm vững cách thức hoạt động của Nmap và biết cách điều chỉnh nó cho phù hợp với bối cảnh sử dụng, thông qua các tùy chọn khác nhau được thảo luận trong hướng dẫn này. Chúng ta không nhất thiết phải sử dụng Nmap theo cùng một cách trên hệ thống thông tin chứa [phần cứng] công nghiệp (https://www.it-connect.fr/actualites/actu-materiel/) như trong mạng người dùng bao gồm các hệ thống Windows được bảo vệ bởi tường lửa cục bộ hoặc trong lõi mạng.



Hy vọng rằng các bài học khác nhau trong hướng dẫn này đã giúp bạn nắm vững và phân tích hành vi của Nmap, nhưng cách tốt nhất để học là thực hành. Vì vậy, hãy đảm bảo bạn đã quen thuộc với các tùy chọn Nmap mà bạn sẽ sử dụng.



### V. Bảo vệ hệ thống quét



Trong chương đầu tiên, chúng ta đã thấy rằng trong hầu hết các trường hợp, Nmap cần được chạy dưới dạng `root` hoặc quản trị viên cục bộ. Điều này là do nó thực hiện các hoạt động mạng, đôi khi ở mức khá thấp, thông qua các thư viện mạng, đòi hỏi quyền cao và rủi ro xét về mặt ổn định hệ thống hoặc tính bảo mật của các ứng dụng khác.



Do đó, Nmap có thể được xem là một thành phần nhạy cảm của hệ thống mà nó được cài đặt. Hãy đảm bảo sử dụng phiên bản Nmap mới nhất, vì các phiên bản cũ hơn có thể chứa các lỗ hổng bảo mật đã biết. Bằng cách sử dụng phiên bản cập nhật, bạn có thể giảm thiểu rủi ro liên quan đến việc sử dụng công cụ này.



Nếu bạn đã chọn sử dụng Nmap không thông qua phiên làm việc với tư cách là `root`, mà bằng cách cấp các đặc quyền cụ thể cho người dùng có đặc quyền để họ có mọi thứ cần thiết để sử dụng Nmap (`sudo` hoặc _capabilities_), hãy lưu ý rằng Nmap có thể được sử dụng như một phần của quá trình nâng cao đặc quyền hoàn chỉnh:



![nmap-image](assets/fr/65.webp)



nâng cao đặc quyền Nmap thông qua `sudo`._



Ở đây, tôi sử dụng lệnh Nmap thông qua `sudo`, nhưng điều này cho phép tôi có được một shell tương tác với tư cách là `root` trên hệ thống, đây không phải là mục tiêu ban đầu.



Việc cài đặt Nmap trên các hệ thống không được thiết kế để quét mạng cũng rất không nên. Tôi đặc biệt nghĩ đến máy chủ hoặc máy trạm. Một mặt, điều này sẽ tạo điều kiện cho việc nâng cao đặc quyền, nhưng trên hết, nó sẽ cho phép kẻ tấn công dễ dàng truy cập vào một công cụ tấn công.



Cuối cùng, tính bảo mật của hệ thống được sử dụng để quét phải được đảm bảo rộng rãi hơn, để hệ thống không trở thành mục tiêu xâm nhập hoặc rò rỉ thông tin. Là quản trị viên hệ thống, tốt hơn hết là nên sử dụng một hệ thống chuyên dụng, lý tưởng nhất là có tuổi thọ hạn chế, thay vì sử dụng máy trạm của riêng bạn.



### VI. Kết luận



Tóm lại, hãy đảm bảo bạn đã thành thạo Nmap trước khi sử dụng trong điều kiện thực tế hoặc sản xuất, và hãy cẩn thận khi xử lý và quản lý kết quả. Sẽ thật đáng tiếc nếu gây ra thiệt hại, rò rỉ dữ liệu hoặc tạo điều kiện cho sự thỏa hiệp, khi mục tiêu ban đầu là cải thiện bảo mật cho công ty bạn.



## 13 - Quét cổng qua TCP: SYN, Connect và FIN



### I. Trình bày



Trong chương này và chương tiếp theo, chúng ta sẽ xem xét kỹ hơn các loại quét TCP khác nhau có trong Nmap, bắt đầu với những loại được sử dụng phổ biến nhất: quét SYN, Connect và FIN.



Như bạn có thể nhận thấy, Nmap cung cấp một số tùy chọn để quét TCP:



![nmap-image](assets/fr/66.webp)



các kỹ thuật quét có sẵn trong Nmap._



Ý tưởng ở đây là giải thích một số phương pháp này, giúp bạn hiểu rõ sự khác biệt, ưu điểm và hạn chế của chúng. Bạn sẽ thấy rằng, tùy thuộc vào bối cảnh hoặc điều bạn muốn biết, việc lựa chọn phương án này hay phương án khác sẽ tốt hơn.



### II. Quét TCP SYN hoặc "Quét nửa mở"



Kiểu quét TCP đầu tiên mà chúng ta sẽ xem xét là `TCP SYN Scan`, còn được gọi là `Half Open Scan`. Nếu bạn còn nhớ những lần quét mạng mà chúng tôi đã thực hiện sau lần quét cổng đầu tiên, đây là kiểu quét mặc định được [Nmap](https://www.it-connect.fr/cours/nmap-cartographie-reseau-scan-de-vulnerabilites/) sử dụng khi chạy với quyền root.



Bản dịch sẽ giúp bạn hiểu cách thức hoạt động của quá trình quét này. Trên thực tế, quét TCP SYN sẽ gửi một gói tin TCP SYN đến mỗi cổng mục tiêu, đây là gói tin đầu tiên được máy khách (máy khách yêu cầu thiết lập kết nối) gửi đi như một phần của giao thức _bắt tay ba bước_ TCP nổi tiếng. Thông thường, nếu cổng đang mở trên máy chủ mục tiêu, với một dịch vụ đang chạy phía sau, máy chủ sẽ gửi lại một gói tin TCP SYN/ACK để xác thực SYN của máy khách và khởi tạo kết nối TCP. Phản hồi này ở dạng một gói tin TCP với cờ SYN và ACK được đặt thành 1, cho phép chúng tôi xác nhận rằng cổng đang mở và dẫn đến một dịch vụ.



Mặt khác, nếu cổng bị đóng, máy chủ sẽ gửi cho chúng ta một gói `TCP` với cờ RST và ACK được đặt thành 1 để chấm dứt yêu cầu kết nối, do đó chúng ta sẽ biết rằng không có dịch vụ nào hoạt động đằng sau cổng này:



![nmap-image](assets/fr/67.webp)



Sơ đồ hành vi quét tCP SYN cho các cổng mở và đóng



Để có cái nhìn cụ thể hơn về `TCP SYN Scan`, tôi đã thực hiện quét cổng TCP/80 đến một máy chủ có máy chủ web đang hoạt động trên cổng này. Chạy quét mạng bằng Wireshark, chúng ta có thể thấy luồng sau (nguồn quét: `10.10.14.84`):



![nmap-image](assets/fr/68.webp)



chụp mạng trong quá trình quét TCP SYN cho một cổng mở



Ở dòng đầu tiên, chúng ta thấy nguồn quét đang gửi một gói tin TCP đến máy chủ `10.10.10.203` trên cổng TCP/80. Trong gói tin TCP này, cờ SYN được đặt thành 1 để chỉ ra rằng đây là yêu cầu khởi tạo kết nối TCP.



Tiếp theo, ở dòng thứ hai, chúng ta thấy mục tiêu phản hồi bằng `TCP SYN/ACK`, nghĩa là nó chấp nhận khởi tạo kết nối và do đó nhận luồng trên cổng TCP/80. Do đó, chúng ta có thể suy ra rằng cổng TCP/80 đang mở và có một máy chủ web trên máy chủ được quét.



Máy chủ của chúng tôi sau đó gửi lại một gói RST để đóng kết nối, cho phép máy chủ được quét không phải duy trì kết nối TCP đang mở chờ phản hồi. Trong trường hợp quét trên nhiều cổng, việc không đóng các kết nối TCP có thể dẫn đến từ chối dịch vụ, làm bão hòa số lượng kết nối đang chờ trả lời mà máy chủ có thể duy trì (xem [Wikipedia - Syn flood](https://fr.wikipedia.org/wiki/SYN_flood))



Trong Wireshark, bạn sẽ có thể xem trạng thái của các cờ TCP cho mỗi lần kiểm tra được thực hiện. Điều này sẽ cho biết gói tin là gói SYN, SYN/ACK, ACK, v.v.:



![nmap-image](assets/fr/69.webp)



xem cờ TCP của gói tin trong Wireshark (TCP SYN tại đây)



Ngược lại, tôi đã chạy cùng một thử nghiệm giữa hai máy, nhưng lần này quét cổng TCP/81 không có dịch vụ nào đang hoạt động (nguồn quét: `10.10.14.84`):



![nmap-image](assets/fr/70.webp)



chụp mạng trong quá trình quét TCP SYN cho một cổng đóng



Máy chủ được quét trả về `TCP RST/ACK` để phản hồi `TCP SYN` của tôi khi cổng không mở.



Như đã đề cập, khi chạy Nmap từ một thiết bị đầu cuối được cấp quyền, TCP SYN Scan là chế độ mặc định và có thể được áp dụng thông qua tùy chọn `-sS` (`scan SYN`):



```
# Execution of a TCP Syn Scan_
nmap -sS 192.168.1.15
```




`TCP SYN Scan` là phương pháp quét được sử dụng phổ biến nhất vì lý do tốc độ. Mặt khác, việc máy khách không hoàn tất _Three Way Handshake_ (tức là không gửi ACK sau khi máy chủ SYN/ACK) có thể đáng ngờ nếu điều này xảy ra quá nhiều lần trên máy chủ hoặc từ cùng một nguồn trên mạng. Thực tế, hành vi bình thường của máy khách sau khi nhận được gói TCP SYN/ACK để phản hồi TCP SYN là gửi `acknowledgement` (ACK) và sau đó khởi động Exchange.



Tuy nhiên, nó vẫn cung cấp tốc độ quét nhanh hơn một chút, vì không cần gửi ACK cho mỗi phản hồi tích cực. Ưu điểm của SYN Scan là tốc độ, vì chỉ có một gói tin được gửi đến mỗi cổng cần quét, nhưng khả năng bị phát hiện lại cao hơn.



Ngoài ra, quét TCP SYN có thể phát hiện xem một cổng có bị tường lửa lọc (bảo vệ) hay không. Trên thực tế, tường lửa trước máy chủ đích có thể bị phát hiện thông qua cách nó hoạt động khi nhận được gói tin TCP SYN trên cổng mà nó được cho là bảo vệ. Nó sẽ không phản hồi. Tuy nhiên, như chúng ta đã thấy, trong cả hai trường hợp (cổng mở hoặc đóng), đều có phản hồi từ máy chủ. Hành vi thứ ba này sẽ tiết lộ sự hiện diện của tường lửa giữa máy chủ được quét và máy đang chạy quét. Dưới đây là kết quả Nmap có thể trả về khi một cổng được quét bị tường lửa lọc:



![nmap-image](assets/fr/71.webp)



hiển thị nmap khi quét một cổng được lọc



Khi chúng ta thực hiện chụp mạng tại thời điểm quét, chúng ta thực sự có thể thấy rằng không có phản hồi nào được đưa ra:



![nmap-image](assets/fr/72.webp)



chụp mạng trong quá trình quét TCP SYN cho một cổng được lọc bởi tường lửa



Sự khác biệt giữa cổng đóng và cổng lọc như sau: cổng lọc là cổng được tường lửa bảo vệ, trong khi cổng đóng là cổng không có dịch vụ nào đang chạy và do đó không thể xử lý các gói tin TCP. Một số loại quét TCP, chẳng hạn như quét TCP SYN, có thể phát hiện xem một cổng có bị lọc hay không, trong khi các loại quét khác thì không.



### III. Quét TCP Connect hoặc quét Full Open



Kiểu quét TCP thứ hai là `TCP Connect scan`, còn được gọi là _Full Open Scan_. Nó hoạt động tương tự như quét TCP SYN, nhưng lần này trả về `TCP ACK` sau khi nhận được phản hồi tích cực từ máy chủ (SYN/ACK). Đây là lý do tại sao nó được gọi là `Full Open'', vì kết nối được mở hoàn toàn và khởi tạo trên mọi cổng được mở trong quá trình quét, do đó tuân thủ _Three Way Handshake_ của TCP:



![nmap-image](assets/fr/73.webp)



Sơ đồ hành vi quét tCP Connect cho các cổng mở và đóng



Sau đây là những gì có thể thấy khi truyền qua mạng trong quá trình `quét TCP Connect` nhắm vào một cổng mở:



![nmap-image](assets/fr/74.webp)



đánh hơi mạng trong quá trình quét TCP Connect để tìm cổng mở



Chúng ta có thể thấy gói tin TCP đầu tiên được gửi là `TCP SYN` do máy khách gửi, và máy chủ sau đó sẽ trả lời bằng `TCP SYN/ACK`, cho biết cổng đang mở và đang lưu trữ một dịch vụ đang hoạt động. Để mô phỏng hoàn toàn một máy khách hợp lệ, Nmap sẽ gửi `TCP ACK` trở lại máy chủ. Ngược lại, khi quét một cổng đã đóng:



![nmap-image](assets/fr/75.webp)



chụp mạng trong quá trình quét TCP Connect cho một cổng đóng



Lưu ý rằng phản hồi của máy chủ đối với gói `SYN` của chúng ta một lần nữa là gói `TCP RST/ACK`, do đó chúng ta có thể suy ra rằng cổng đã đóng và không có dịch vụ nào đang chạy trên đó.



Khi sử dụng Nmap, tùy chọn `-sT` (`scan Connect`) được sử dụng để thực hiện Quét Kết nối TCP. Xin lưu ý rằng khi Nmap được sử dụng từ một phiên không có đặc quyền, đây là chế độ quét TCP mặc định:



```
# Execution of a TCP Connect Scan
nmap -sT 192.168.1.15
```



`TCP Connect Scan` mô phỏng một yêu cầu kết nối hợp pháp hơn, với hành vi gần giống nhất với máy khách lambda, do đó khó phát hiện quét trên số lượng cổng ít hơn. Tuy nhiên, nó chậm hơn vì nó khởi tạo hoàn toàn mọi kết nối TCP trên các cổng mở của máy được quét.



Quét Nmap 10.000 cổng vẫn có thể dễ dàng bị phát hiện nếu cài đặt các dịch vụ phát hiện và bảo vệ xâm nhập mạng (IDS, IPS, EDR). Khi kẻ tấn công muốn giữ kín danh tính, chúng thường tập trung vào một số ít cổng được lựa chọn chiến lược, chẳng hạn như 445 (SMB) hoặc 80 (HTTP), những cổng thường mở trên máy chủ và tiềm ẩn nhiều lỗ hổng bảo mật phổ biến.



Vì TCP Connect Scan mong đợi phản hồi trong cả hai trường hợp nên nó cũng có thể phát hiện sự hiện diện của tường lửa có thể đang lọc các cổng trên máy chủ đích.



### IV. Quét TCP FIN hoặc "Quét ẩn"



`TCP FIN Scan`, còn được gọi là _Stealth Scan_, sử dụng hành vi của máy khách chấm dứt kết nối TCP để phát hiện cổng mở.



Trong TCP, kết thúc phiên nghĩa là gửi một gói tin TCP với cờ FIN được đặt thành 1. Trong Exchange thông thường, máy chủ sẽ ngừng mọi giao tiếp với máy khách (không có phản hồi). Nếu máy chủ không có kết nối TCP nào đang hoạt động với máy khách, nó sẽ gửi một `RST/ACK`. Do đó, chúng ta có thể phân biệt giữa các cổng mở và đóng bằng cách gửi các gói tin `TCP FIN` đến một tập hợp các cổng:



![nmap-image](assets/fr/76.webp)



Sơ đồ hành vi quét tCP FIN cho các cổng mở và đóng



Tôi lại chụp lại mạng trong quá trình _Quét ẩn_ và đây là những gì bạn thấy khi cổng được quét mở:



![nmap-image](assets/fr/77.webp)



chụp mạng trong quá trình quét TCP FIN để tìm cổng mở



Chúng ta có thể thấy máy khách gửi một hoặc hai gói tin để chấm dứt kết nối TCP và máy chủ không phản hồi. Nó chỉ đơn giản chấp nhận kết thúc kết nối và ngừng giao tiếp.



Đây là những gì chúng ta thấy khi quét một cổng đã đóng:



![nmap-image](assets/fr/78.webp)



chụp mạng trong quá trình quét TCP FIN cho một cổng đóng



Chúng ta thấy máy chủ gửi lại gói tin `TCP RST/ACK`, do đó có sự khác biệt về hành vi giữa một cổng mở và một cổng đóng, và chúng ta có thể liệt kê các cổng mở trên máy chủ bằng cách gửi gói tin TCP FIN. Sử dụng Nmap, tùy chọn `-sF` (`scan FIN`) được sử dụng để thực hiện Quét TCP FIN:



```
# Execution of a TCP Fin Scan
nmap -sF 192.168.1.15
```



Quét TCP FIN không hoạt động trên máy chủ Windows, vì hệ điều hành có xu hướng bỏ qua các gói tin TCP FIN khi chúng được gửi đến các cổng không mở. Vì vậy, nếu bạn chạy Quét TCP FIN trên máy chủ Windows, bạn sẽ có cảm giác như tất cả các cổng đều đóng.



Đó là lý do tại sao việc làm quen với một số phương pháp quét và hiểu được sự khác biệt giữa chúng lại quan trọng.



Vì trong cả hai trường hợp, TCP FIN sẽ không chờ phản hồi nên nó sẽ không thể phát hiện sự hiện diện của tường lửa giữa máy chủ đích và nguồn quét.



Sau đây là ví dụ về kết quả quét TCP FIN của Nmap:



![nmap-image](assets/fr/79.webp)



kết quả quét TCP FIN của Nmap._



Trên thực tế, việc máy chủ không phản hồi trên một cổng nhất định có thể có nghĩa là cổng đó đã bị lọc, nhưng cũng có thể là cổng đó đang mở và hoạt động.



Quét này được gọi là "tàng hình" vì nó không gây ra nhiều lưu lượng truy cập và thường không gây ra ghi nhật ký trên các hệ thống mục tiêu. Nó có thể được sử dụng để phát hiện các cổng trên mạng một cách kín đáo mà không gây ra bất kỳ báo động nào. Tuy nhiên, như đã đề cập ở trên, hiệu quả của nó có thể khác nhau tùy thuộc vào hệ thống mục tiêu, cũng như tùy thuộc vào cấu hình của thiết bị bảo mật.



### V. Kết luận



Vậy là hết chương đầu tiên trong hai chương về các loại quét TCP khác nhau do Nmap cung cấp! Trong chương tiếp theo, chúng ta sẽ tìm hiểu về các loại quét TCP XMAS, Null và ACK, chúng hoạt động theo những cách khác nhau để phát hiện các cổng mở trên máy chủ.





## 14 - Quét cổng qua TCP: XMAS, Null và ACK



### I. Trình bày



Trong phần này, chúng ta sẽ tiếp tục khám phá các phương pháp quét TCP khác nhau do Nmap cung cấp. Chúng ta sẽ xem xét các phương pháp `XMAS`, `Null` và `ACK`, sử dụng các tính năng dành riêng cho TCP để truy xuất thông tin về các cổng và dịch vụ đang mở trên một mục tiêu nhất định.



### II. Quét TCP XMAS



XMAS Scan TCP hơi khác thường ở chỗ nó hoàn toàn không mô phỏng hành vi bình thường của người dùng hoặc máy tính trên mạng. Trên thực tế, XMAS Scan sẽ gửi các gói tin TCP với các cờ `URG` (Khẩn cấp), `PSH` (Đẩy), và `FIN` (Kết thúc) được đặt thành 1, nhằm vượt qua một số tường lửa hoặc cơ chế lọc.



Cái tên XMAS xuất phát từ việc việc nhìn thấy những lá cờ này khá bất thường. Khi cả ba lá cờ được đặt cùng lúc trong một gói tin TCP, nó trông giống như một cây thông Noel được thắp sáng:



![nmap-image](assets/fr/80.webp)



Cờ tCP được sử dụng trong quét XMAS



Không đi sâu vào chi tiết về vai trò của các cờ này ở đây, điều quan trọng cần biết là khi gửi một gói tin với ba cờ này được bật, một dịch vụ đang hoạt động phía sau cổng đích sẽ không trả về bất kỳ gói tin nào. Mặt khác, nếu cổng bị đóng, chúng ta sẽ nhận được một gói tin TCP RST/ACK. Giờ đây, chúng ta có thể phân biệt hành vi của một cổng mở và một cổng đóng khi liệt kê các cổng trên một máy:



![nmap-image](assets/fr/81.webp)



Sơ đồ hành vi quét tCP XMAS cho các cổng mở và đóng



Vẫn theo cùng một logic, quét mạng trên cổng TCP/80 của máy chủ có máy chủ web đang hoạt động sẽ hiển thị hành vi sau khi phát hiện cổng mở (nguồn quét `10.10.14.84`):



![nmap-image](assets/fr/82.webp)



chụp mạng trong quá trình quét TCP XMAS để tìm cổng mở



Chúng ta có thể thấy nguồn quét gửi hai gói TCP XMAS (với các cờ `FIN`, `PSH` và `URG` được đặt thành 1) đến máy chủ `10.10.10.203` và không có phản hồi từ máy chủ đích, cho biết cổng đang mở. Ngược lại, khi thực hiện `TCP XMAS Scan` trên một cổng đã đóng, kết quả sau được quan sát:



![nmap-image](assets/fr/83.webp)



chụp mạng trong quá trình quét TCP XMAS để tìm cổng đóng



Phản hồi cho gói tin TCP của chúng tôi sau đó là `TCP RST/ACK`, cho biết cổng đã đóng. Để sử dụng kỹ thuật này với Nmap, tùy chọn `-sX` (`scan XMAS`) cho phép bạn thực hiện Quét XMAS TCP:



```bash
# Execution of a TCP XMAS Scan
nmap -sX 192.168.1.15
```



Điều quan trọng cần lưu ý là quét TCP XMAS không thể phát hiện tường lửa nằm giữa máy đích và máy quét, không giống như một số loại quét khác như TCP SYN hoặc Connect. Thực tế, một tường lửa đang hoạt động giữa hai máy chủ sẽ đảm bảo không có lệnh trả về TCP nào được thực hiện nếu cổng đích bị lọc (tức là được tường lửa bảo vệ). Do đó, trong trường hợp không có phản hồi, không thể biết liệu cổng đó có được tường lửa bảo vệ hay đang mở và hoạt động hay không. Bạn cũng nên lưu ý rằng, giống như quét TCP FIN, một số ứng dụng hoặc hệ điều hành nhất định như Windows có thể làm sai lệch kết quả của loại quét này.



lưu ý: hỗ trợ quét XMAS/FIN/NULL trên các phiên bản Windows gần đây vẫn còn hạn chế và kết quả có thể không nhất quán trên loại mục tiêu này. (Cập nhật 2025)_



### III. Quét TCP Null



Ngược lại với quét TCP XMAS, quét TCP Null sẽ gửi các gói tin quét TCP với tất cả các cờ được đặt thành 0. Đây cũng là hành vi sẽ không bao giờ xảy ra trong Exchange thông thường giữa các máy, vì việc gửi gói tin TCP mà không có cờ không được chỉ định trong RFC mô tả giao thức TCP. Đây là lý do tại sao nó có thể được phát hiện dễ dàng hơn.



Giống như quét TCP XMAS, quét này có thể can thiệp vào một số tường lửa hoặc mô-đun lọc, cho phép các gói tin đi qua:



![nmap-image](assets/fr/84.webp)



Sơ đồ hành vi tCP Null Scan cho các cổng mở và đóng



Sau đây là những gì có thể thấy trên mạng trong quá trình quét TCP Null trên một cổng mở:



![nmap-image](assets/fr/85.webp)



chụp mạng trong quá trình quét TCP Null cho một cổng mở



Máy quét gửi một gói tin không có cờ (`[<None>]` trong Wireshark) mà không có phản hồi từ máy chủ. Ngược lại, khi cổng đích bị đóng:



![nmap-image](assets/fr/86.webp)



chụp mạng trong quá trình quét TCP Null cho một cổng đã đóng



Để thực hiện quét TCP Null bằng Nmap, chỉ cần sử dụng tùy chọn `-sN` (`scan Null`):



```bash
# Execution of a TCP Null Scan
nmap -sN 192.168.1.15
```



Do phản hồi khi một cổng mở và khi tường lửa hoạt động (cả hai trường hợp đều không có phản hồi từ máy chủ) là giống hệt nhau, nên quét TCP Null không thể phát hiện sự hiện diện của tường lửa. Hơn nữa, tường lửa thậm chí có thể làm sai lệch kết quả bằng cách gợi ý rằng một cổng đang mở, vì nó không phản hồi các gói tin TCP không có cờ, ngay cả khi cổng đã được lọc. Đây là thông tin quan trọng cần lưu ý khi sử dụng các lần quét không thể phân biệt giữa cổng mở và cổng được lọc (được tường lửa bảo vệ), chẳng hạn như quét `TCP Null`, `XMAS` hoặc `FIN`, để duy trì tính nhất quán trong việc diễn giải kết quả thu được.



### IV. Quét TCP ACK



Quét TCP ACK được sử dụng để phát hiện sự hiện diện của tường lửa trên máy chủ đích hoặc giữa máy chủ đích và nguồn quét.



Không giống như các phương pháp quét khác, quét TCP ACK không cố gắng xác định cổng nào đang mở trên máy chủ, mà thay vào đó, kiểm tra xem hệ thống lọc có đang hoạt động hay không, bằng cách phản hồi cho mỗi cổng bằng `filtered` hoặc `unfiltered`. Một số phương pháp quét TCP, chẳng hạn như `TCP SYN` hoặc `TCP Connect`, có thể thực hiện cả hai cùng lúc, trong khi những phương pháp khác, chẳng hạn như `TCP FIN` hoặc `TCP XMAS`, hoàn toàn không thể xác định được sự hiện diện của bộ lọc. Đây là lý do tại sao quét TCP ACK có thể hữu ích:



![nmap-image](assets/fr/87.webp)



Sơ đồ hành vi quét tCP ACK cho các cổng được lọc và không được lọc



Chúng tôi sẽ sử dụng tùy chọn `-sA` của Nmap để thực hiện kiểu quét này. Đây là kết quả quét TCP ACK nếu cổng bị lọc, tức là bị chặn và được bảo vệ bởi tường lửa:



![nmap-image](assets/fr/88.webp)



Hiển thị nmap trong quá trình quét TCP ACK._



Kết quả ví dụ cho một máy chủ có tường lửa và một máy chủ không có tường lửa. Nmap trả về kết quả `filtered` trên các cổng TCP/80 và TCP/81 của máy chủ `10.10.10.203`. Khi phân tích mạng bằng Wireshark, kết quả như sau:



![nmap-image](assets/fr/89.webp)



chụp mạng trong quá trình quét TCP ACK cho một cổng không được lọc bởi tường lửa



Máy mục tiêu sẽ không trả về kết quả gì nếu có tường lửa.



Để khởi chạy quét này bằng Nmap, hãy sử dụng tùy chọn `-sA` (`scan ACK`):



```bash
# Execution of a TCP ACK Scan
nmap -sA 192.168.1.15
```



### V. Kết luận



Chúng tôi đã xem xét ba phương pháp quét khác nhau qua TCP ngoài những phương pháp đã được trình bày. Những phương pháp này sẽ được sử dụng trong các điều kiện và bối cảnh rất cụ thể, đặc biệt là trong bối cảnh kiểm tra xâm nhập hoặc hoạt động của Đội Đỏ, trong đó có các khái niệm về sự thận trọng.



## 15 - Nmap CheatSheet - Tóm tắt các lệnh hướng dẫn



### I. Trình bày



Sau đây là tóm tắt ngắn gọn về nhiều lệnh và trường hợp sử dụng của Nmap để bạn có thể nhanh chóng tìm và sử dụng lại chúng trong quá trình sử dụng hàng ngày.



### II. Nmap: Bảng hướng dẫn IT-Connect



Dưới đây là bảng tóm tắt các lệnh được trình bày. Trang này giúp bạn dễ dàng tìm thấy những cách sử dụng phổ biến nhất của Nmap.





- Quét cổng




```bash
# Display installed Nmap version
nmap --version

# Scan for open specific ports on a single IP address
nmap --open -p 80 192.168.1.18

# Scan TCP ports on a selection of ports
nmap 192.168.1.19 -p 80
nmap 192.168.1.19 -p 22,80,1000-2000,3389

# Scan UDP services on an IP address
nmap -sU 192.168.1.19

# Scan UDP services on specific ports
nmap -sU 192.168.1.19 -p 161,23

# Scan the 100 most commonly used TCP ports
nmap 192.168.1.19 --top-ports 100

# Scan all ports on an IP address
nmap 192.168.1.19 -p-

# Scan multiple subnets with specific ports
nmap 192.168.0.0/24 192.168.1.0/24 -p 22

# Scan a subnet while excluding a specific IP address, scan all ports
nmap 192.168.0.0/24 --exclude 192.168.0.4 -p-
```





- Khám phá các máy chủ đang hoạt động




```bash
# Scan on CIDR or IP ranges
nmap 192.168.0.0/24
nmap 192.168.0.0/24 192.168.1.0/24
nmap 192.168.1.2 192.168.1.3 192.168.1.10-20
nmap 192.168.0.0/24 192.168.1.3 192.168.1.10-20

# Host discovery scan (Ping Scan) on a network
nmap -sn 192.168.1.0/24
```



lưu ý: Tùy chọn `-sP` đã lỗi thời trong nhiều năm và nên được thay thế bằng `-sn`. (Cập nhật 2025)_



```bash
# Host discovery scan without port scan
nmap 192.168.1.0/24 -sn

# Host discovery scan on a local network using various probe techniques
nmap -sn -PP -PS22,3389,445,139 -PA80 192.168.1.0/24

# Scan hosts listed in a text file
nmap -iL /tmp/mesCibles.txt

# Network scan with a specific IP excluded
nmap 192.168.1.0/24 --exclude 192.168.1.140

# Subnet scan excluding another subnet
nmap 10.0.0.0/16 --exclude 10.0.100.0/24
```





- Phát hiện phiên bản




```bash
# Enable version detection
nmap 192.168.1.0/24 -sV

# Version detection + advanced trace
nmap 192.168.1.0/24 -sV --version-trace

# Version detection with maximum probe rarity of 2
nmap 192.168.1.0/24 -sV --version-intensity 2

# Version detection with all probes
nmap 192.168.1.0/24 -sV --version-intensity 9

# Enable OS detection
nmap -O 10.10.10.0/24
```





- Các tập lệnh NSE: tìm kiếm lỗ hổng bảo mật




```bash
# Run default NSE scripts
nmap -sC 10.10.10.152

# Scan all TCP ports with default NSE scripts
nmap -sC -p- 10.10.10.152

# Display help for script by name
nmap --script-help=ftp-*

# Display help for a category
nmap --script-help=discovery

# Use NSE scripts by category
nmap --script default 10.10.10.152
nmap --script discovery 10.10.10.152

# Inclusion/exclusion filter for NSE script categories
nmap --script "discovery and safe" 10.10.10.152
nmap --script "not intrusive and not dos" 10.10.10.152
nmap --script "vuln and not intrusive and not dos" 10.10.10.152
nmap --script "(http and vuln) and not intrusive and not dos" 10.10.10.152

# Run a specific NSE script
nmap --script ftp-anon -p 21 10.10.10.152
nmap --script ftp-anon 10.10.10.152

# Pass arguments to an NSE script
nmap --script ssh-brute --script-args userdb=/tmp/userlist,passdb=/tmp/passlist 10.10.10.245 192.168.1.19
```





- Quản lý đầu ra Nmap




```bash
# Save scan to text file
nmap 10.10.10.0/24 -sV -oN nmap_scan_10.10.10.0_24.txt

# Save scan to condensed text file
nmap 10.10.10.0/24 -sV -oG nmap_scan_10.10.10.0_24.gnmap

# Save scan to XML file
nmap 10.10.10.0/24 -sV -oX nmap_scan_10.10.10.0_24.xml
```





- Tối ưu hóa hiệu suất




```bash
# Version detection scan with max rate of 300 packets per second
nmap -sV 10.10.10.0/24 --max-rate 300

# Version detection scan with default scripts, no retry, max host timeout 15min
nmap -sV -sC 10.10.10.0/24 --max-retries 0 --host-timeout 15m

# Version detection scan with the 2000 most common ports, aggressive scan speed (T4), debug output
nmap 10.10.10.0/24 -sV --top-ports 2000 -T4 -d
```





- Các loại quét TCP




```bash
# TCP SYN scan (fast, less stealthy)
nmap -sS 192.168.1.15

# TCP Connect scan (classic)
nmap -sT 192.168.1.15

# TCP FIN scan (stealth)
nmap -sF 192.168.1.15

# TCP XMAS scan
nmap -sX 192.168.1.15

# TCP Null scan
nmap -sN 192.168.1.15

# TCP ACK scan (detect firewall)
nmap -sA 192.168.1.15
```



Tôi hy vọng bạn thấy những lệnh này hữu ích. Đừng quên điều chỉnh mục tiêu quét cho phù hợp với bối cảnh của bạn và tham khảo tài liệu chính thức để nắm vững các bài kiểm tra đã thực hiện.



### III. Kết luận



Hướng dẫn sử dụng Nmap hiện đã hoàn tất. Giờ đây, bạn đã có những kiến thức cơ bản cần thiết để sử dụng công cụ toàn diện và mạnh mẽ này. Chúng tôi đặc biệt khuyên bạn nên thực hành trên các môi trường được kiểm soát (Hack The Box, VulnHub, máy ảo) trước khi sử dụng trong môi trường thực tế.



Vẫn còn nhiều điều cần khám phá về cách thức hoạt động bên trong và các tính năng nâng cao của công cụ này. Tuy nhiên, việc nắm vững các lệnh và khái niệm được trình bày ở đây sẽ giúp bạn sử dụng Nmap một cách tự tin và hiệu quả.