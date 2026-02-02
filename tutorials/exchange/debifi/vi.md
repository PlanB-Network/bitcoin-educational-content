---
name: Debifi
description: Nhận khoản vay không cần lưu ký được bảo lãnh bởi Bitcoin.
---

![cover](assets/cover.webp)




## Giới thiệu



Trong nhiều thế kỷ, hoạt động cho vay truyền thống đã giúp tài trợ cho nhiều dự án. Tuy nhiên, hình thức này vẫn còn chậm, tốn kém và chưa thực sự toàn diện, đặc biệt là đối với những người không có cơ sở hạ tầng ngân hàng vững chắc.



Sự trỗi dậy của giao thức Bitcoin đã mở ra một kỷ nguyên tài chính mới, đồng thời mang đến nhiều thách thức. Một trong những thách thức này là làm thế nào để có được thanh khoản mà không bị buộc phải bán Bitcoin, do đó mất đi tiềm năng tăng trưởng của nó.



Kết quả là **Debifi**, một nền tảng tự định vị mình là một giải pháp thay thế hiện đại cho ngân hàng. Mục tiêu rất rõ ràng: làm cho tín dụng trở nên đơn giản và minh bạch nhất có thể, bằng cách kết hợp những lợi thế của hệ thống tài chính truyền thống với sự tự do mà Bitcoin mang lại. Cái tên Debifi phản ánh tầm nhìn này: ***Tài chính Bitcoin Phi tập trung***, một từ viết tắt minh họa cho sự giao thoa giữa tài chính phi tập trung và đổi mới sáng tạo của Bitcoin.



Debifi là một nền tảng cho vay phi lưu ký được hỗ trợ bởi Bitcoin, nghĩa là bạn vẫn giữ quyền kiểm soát khóa riêng tư của mình. Nền tảng này cho phép người dùng mở khóa thanh khoản bằng cách đổi lấy bitcoin bị khóa của họ làm tài sản thế chấp. Không giống như các khoản vay ngân hàng truyền thống, Debifi sử dụng hệ thống ký quỹ đa chữ ký (3/4) và không chấp nhận tái thế chấp tài sản thế chấp, đảm bảo tính bảo mật và minh bạch cao hơn.



Trên thực tế, điều này có nghĩa là cả Debifi lẫn người cho vay cá nhân đều không thể chi tiêu BTC của bạn mà không có sự đồng ý của ba bên (bạn, người cho vay và một bên thứ ba đáng tin cậy). Điều này làm cho hệ thống an toàn hơn: nếu bạn vay trên Debifi, bạn vẫn giữ quyền sở hữu Bitcoin của mình cho đến khi khoản vay được hoàn trả đầy đủ.



## Ưu điểm của Debifi



Với Debifi, bạn nhận được các khoản vay được hỗ trợ bởi Bitcoin, được thế chấp vượt mức và bảo mật theo on-chain. Tiền của bạn được bảo mật an toàn với ví đa chữ ký, xác thực hai yếu tố (2FA) và toàn quyền kiểm soát Bitcoin — bạn nắm giữ khóa, bạn giữ tiền của mình. Vay bằng nhiều loại stablecoin hoặc tùy chọn tiền pháp định, với lãi suất cạnh tranh và thanh khoản toàn cầu.



Sau đây là so sánh nhanh giữa khoản vay Debifi và khoản vay ngân hàng truyền thống:


| Characteristics        | Loan via Debifi                                                        | Traditional Bank Loan                                                       |
| ---------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Accessibility          | ✔️ Open to any Bitcoin holder (even without banking history)           | ❌ Often limited to clients with physical collateral and strong records      |
| Speed of approval      | ✔️ Funds available within minutes or hours                             | ❌ Lengthy process (days or weeks)                                           |
| Required guarantees    | ✔️ Bitcoin used as the sole collateral                                 | ❌ Physical guarantees (property, land, stable income)                       |
| Asset control          | ✔️ You keep exposure to Bitcoin and its upside potential               | ❌ No connection between the loan and your financial assets                  |
| Geographic flexibility | ✔️ Available everywhere (no banking jurisdiction constraints)          | ❌ Restricted to the bank’s jurisdiction                                     |
| Main risk              | ❌ Liquidation risk if BTC price drops too sharply                      | ❌ Risk of asset seizure or negative impact on credit score                  |

Trước khi tôi hướng dẫn bạn từng bước cách vay trên Debifi, tôi nghĩ bạn cần biết một số điểm sau.




## Định nghĩa





- Phí khởi tạo** là khoản phí một lần được tính vào thời điểm khoản vay được cấp và được tính theo tỷ lệ phần trăm của số tiền vay. Các khoản phí này bao gồm chi phí hành chính, vận hành và quản lý.





- Tài sản thế chấp** là tài sản bạn ký quỹ để đảm bảo khoản vay. Trong trường hợp của Debifi, tài sản thế chấp là Bitcoin (BTC), được người vay ký quỹ Multisig 3/4.





- Hệ thống ký quỹ Multisig (3/4)** là một cơ chế gửi tiền an toàn, trong đó bitcoin của người vay được đặt vào một địa chỉ đa chữ ký. Cụ thể, bốn (4) bên, mỗi bên nắm giữ một khóa (bên vay, bên cho vay, Debifi, bên thứ ba độc lập). Để chuyển tiền, cần có ít nhất 3 trong số 4 chữ ký.





- Stablecoin** là một loại tiền điện tử có giá trị được neo theo một tài sản ổn định (ví dụ: đô la Mỹ), tránh được sự biến động của Bitcoin. Ví dụ: 1 USDC luôn có giá trị khoảng 1 đô la, vì nó được bảo chứng bằng dự trữ tiền pháp định.





- Tỷ lệ Cho vay trên Giá trị (LTV)** của khoản vay quyết định số tiền mặt bạn có thể vay làm tài sản thế chấp cho Bitcoin của mình. Tỷ lệ LTV = Số tiền vay / Số tiền thế chấp * 100. Ví dụ: LTV là 50% có nghĩa là giá trị của khoản vay bằng 50% giá trị của Bitcoin được gửi.




Video hướng dẫn về BTC Sessions:



![Vidéo tutoriel de BTC Sessions](https://youtu.be/02gzg-en8n0)



## Bắt đầu với Debifi



Để bắt đầu sử dụng Debifi, bạn cần một số điều kiện tiên quyết.


### Điều kiện tiên quyết



Trước khi bạn có thể vay từ Debifi, vui lòng đảm bảo bạn có những mục sau:





- Bitcoin wallet: nơi bạn giữ BTC của mình (tốt nhất là không lưu ký, ví dụ: Hardware Wallet hoặc wallet di động đáng tin cậy). Bạn sẽ gửi tài sản thế chấp Bitcoin đến Debifi từ wallet này và nhận lại tài sản thế chấp.



Bạn có thể sử dụng Aqua, Bitcoin và Liquid, wallet, cũng hỗ trợ quản lý stablecoin USDT trên nhiều mạng lưới khác nhau. Hoặc COLDCARD (Mk4 hoặc Q), hiện là phần cứng duy nhất được Debifi hỗ trợ.



https://planb.academy/tutorials/wallet/mobile/aqua-8e6d7dd3-8c03-45cc-90dd-fe3899a7d125

https://planb.academy/tutorials/wallet/hardware/coldcard-q-73e86d1a-6fe6-4d8b-bb15-8690298020e3



- KYC (*Biết Khách hàng của Bạn*): tùy thuộc vào gói vay được chọn, quy trình xác minh danh tính có thể được yêu cầu. Trên Debifi, mỗi gói vay đều có thông báo yêu cầu KYC. Vì vậy, hãy chuẩn bị kỹ lưỡng. KYC được thực hiện bởi các nhà cung cấp dịch vụ bên thứ ba đáng tin cậy như Sumsub.



![image](assets/fr/03.webp)





- Ứng dụng xác thực hai yếu tố: Debifi yêu cầu mã Authenticator cho mọi thao tác quan trọng. Đây là một lớp bảo mật bổ sung. Trong hướng dẫn này, chúng ta sẽ sử dụng Google Authenticator. Ngoài ra, bạn có thể sử dụng các phương thức khác tùy ý.



https://planb.academy/tutorials/computer-security/authentication/proton-authenticator-047ca2eb-a922-4e0e-8f75-1b89d23951ae

https://planb.academy/tutorials/computer-security/authentication/aegis-authenticator-22cc4d35-fb46-4e54-8833-bc4b411518bc



- Trang web và ứng dụng di động Debifi: Debifi vừa là trang web vừa là ứng dụng di động, và cả hai hoạt động song song. Ứng dụng di động trở thành wallet, lưu trữ khóa riêng tư của bạn và quản lý việc ký kết hợp đồng. Ngoài ra, bạn cần sử dụng trang web để ký kết hợp đồng (một Interface lớn cung cấp cho bạn cái nhìn tổng quan về các hợp đồng vay và các chi tiết cụ thể của chúng).





- Ứng dụng di động Debifi (iOS/Android) là bắt buộc để vay tiền. Bạn phải tải ứng dụng, tạo tài khoản và "liên kết" thiết bị (đăng ký thiết bị với tài khoản). Ứng dụng Debifi hỗ trợ xác thực hai yếu tố (2FA) và nếu không có điện thoại thông minh, bạn không thể xác nhận giao dịch trên Debifi.



### Tạo một tài khoản



Truy cập [trang web chính thức của Debifi](https://debifi.com/app).



![image](assets/fr/04.webp)



Cài đặt ứng dụng phù hợp với loại điện thoại thông minh bạn có, sau đó mở ứng dụng.



![image](assets/fr/05.webp)



![image](assets/fr/06.webp)



Khi vào ứng dụng, hãy nhấp vào menu **Cài đặt**.



![image](assets/fr/07.webp)



Sau đó nhấp vào **Đăng nhập hoặc tạo tài khoản** để tạo tài khoản bằng địa chỉ email của bạn.



![image](assets/fr/08.webp)



![image](assets/fr/09.webp)



![image](assets/fr/10.webp)



Bạn sẽ nhận được mã xác minh qua email. Sao chép và dán mã này vào ứng dụng. Sau đó, mở ứng dụng Debifi trên điện thoại thông minh của bạn và đăng nhập.



![image](assets/fr/11.webp)



### Bảo mật tài khoản của bạn



Để bảo mật, Debifi sẽ yêu cầu bạn thực hiện theo ba bước.



![image](assets/fr/12.webp)





- Đầu tiên, bạn cần phải thiết lập mã PIN mạnh để truy cập ứng dụng sau này.



![image](assets/fr/13.webp)





- Tiếp theo, hãy thiết lập xác thực hai yếu tố (2FA) để liên kết thiết bị với tài khoản của bạn bằng mã 2FA.



![image](assets/fr/14.webp)





- Cuối cùng, hãy lưu 12 từ khóa riêng của bạn bằng cách viết ra một phương tiện đáng tin cậy và cất giữ ở nơi an toàn. Giai đoạn này rất quan trọng để khôi phục tài khoản và quản lý tiền của bạn.



![image](assets/fr/15.webp)





- Để tăng thêm tính bảo mật, bạn thậm chí có thể thêm passphrase.



![image](assets/fr/16.webp)



https://planb.academy/tutorials/wallet/backup/passphrase-a26a0220-806c-44b4-af14-bafdeb1adce7

Xin lưu ý rằng chỉ có điện thoại thông minh đã đăng ký của bạn mới có thể mở tài khoản (một biện pháp bảo mật bổ sung).



Sau khi hoàn tất các bước này, hãy nhấp vào menu **Ưu đãi** để xem các ưu đãi vay hiện có. Khi nhấp vào một ưu đãi, bạn sẽ được chuyển hướng đến trang web Debifi.



![image](assets/fr/17.webp)



### Truy cập trang web và khám phá các ưu đãi cho vay



Sau khi thiết bị của bạn được kết nối, hãy truy cập [trang web Debifi](https://debifi.com/). Đăng nhập để thiết lập kết nối an toàn giữa ứng dụng di động Debifi và nền tảng web. Điều này giúp bạn dễ dàng tương tác với các ưu đãi vay hiện có (xem rõ chi tiết từng ưu đãi) và quản lý tài khoản của mình.



![image](assets/fr/18.webp)



![image](assets/fr/19.webp)



![image](assets/fr/20.webp)



![image](assets/fr/21.webp)




Video hướng dẫn cách đăng nhập bằng tài khoản của bạn trên nền tảng:



![video](https://youtu.be/cUwCfTKDAOo)



## Đơn xin vay



Nền tảng này giúp bạn tiếp cận nguồn thanh khoản chất lượng cao của tổ chức và cung cấp nhiều lựa chọn phù hợp với nhu cầu của bạn. Hãy duyệt qua để tìm hiểu những lựa chọn khả dụng. Bạn cũng có thể linh hoạt điều chỉnh các thông số khoản vay theo khả năng chấp nhận rủi ro và tình hình tài chính cá nhân.



![image](assets/fr/22.webp)



Các loại tiền tệ pháp định mà Debifi hiện đang cung cấp có thể được xem trên nền tảng này.



![image](assets/fr/23.webp)



### Các điều khoản hợp đồng rõ ràng, linh hoạt



Debifi dựa trên các điều kiện vay minh bạch và linh hoạt để đáp ứng nhu cầu của mỗi bên (bên cho vay và bên vay). Các điều khoản chính bao gồm:



#### Tỷ lệ cho vay trên giá trị tài sản thế chấp (LTV)


Các đợt vay Bitcoin thường có ba (3) đợt:





- Tỷ lệ LTV bảo thủ (30% - 40%), tương ứng với khoản vay rủi ro thấp, lý tưởng để tối đa hóa sự an toàn trước biến động giá Bitcoin;





- Cân bằng (50% LTV);





- Chiến lược tích cực (LTV 70%), mang lại tính thanh khoản cao hơn, nhưng đi kèm rủi ro thanh lý rất cao trong thời kỳ thị trường suy thoái. Việc theo dõi sát sao tình hình thị trường Bitcoin là điều bắt buộc khi lựa chọn phân khúc này.



#### Lãi suất



Việc thiết lập lãi suất thường phụ thuộc vào Tỷ lệ Cho vay Trên Giá trị Tài sản Thế chấp (LTV) bạn chọn, thời hạn vay, biến động tài sản thế chấp và đánh giá rủi ro cụ thể của từng nền tảng. Lãi suất được cố định trong suốt thời hạn vay.



#### Thời hạn vay và tính linh hoạt trong việc trả nợ



Lịch trình trả nợ linh hoạt và được thiết kế để đáp ứng nhu cầu của người vay. Khoản vay có thể được trả toàn bộ hoặc một phần bất kỳ lúc nào mà không mất thêm phí, miễn là các yêu cầu về tài sản thế chấp vẫn được đáp ứng. Trong suốt thời hạn vay, lãi suất thường được trả định kỳ, còn nợ gốc được thanh toán khi đáo hạn.



#### Quyền thanh lý (Cuộc gọi ký quỹ)



Do tính biến động của Bitcoin, các khoản vay bao gồm chính sách yêu cầu ký quỹ được xác định rõ ràng. Yêu cầu ký quỹ xảy ra khi Tỷ lệ cho vay trên giá trị tài sản thế chấp (LTV) tăng do giá trị tài sản thế chấp giảm. Debifi thông báo cho người vay qua email và ứng dụng, cho phép họ bổ sung tài sản thế chấp hoặc trả một phần khoản vay.


75% LTV — Cảnh báo đầu tiên

80% LTV — Cảnh báo thứ hai

85% LTV — Cảnh báo cuối cùng

90% LTV — Tài sản thế chấp được thanh lý



### Khởi động quy trình cho vay



Để chọn một khoản vay phù hợp với nhu cầu của bạn, hãy nhấp vào khoản vay đó để xem các tính năng của nó.



![image](assets/fr/24.webp)



Bạn có thể thấy:


1. Tên tổ chức cho vay;


2. Phạm vi số tiền vay;


3. Bạn sẽ nhận được tiền bằng USDC Ethereum;


4. Thời hạn vay, lãi suất và tỷ lệ LTV;


5. KYC là bắt buộc đối với ưu đãi này;


6. Bạn phải nhập số tiền chính xác cần thiết (số tiền này phải nằm trong phạm vi cho phép, xem mục 2);


7. Phải nhập địa chỉ Ethereum USDC được sử dụng để nhận tiền.



Khi bạn hài lòng với ưu đãi và đã điền đầy đủ thông tin cần thiết, hãy nhấp vào "Yêu cầu Contract".



![image](assets/fr/25.webp)



Quay lại ứng dụng di động để ''**Cung cấp khóa công khai**''.



![image](assets/fr/26.webp)



Nhấn ''Cung cấp khóa công khai**'', sau đó chọn nguồn khóa công khai. Bên cho vay cũng sẽ cần cung cấp khóa công khai.



![image](assets/fr/27.webp)



![image](assets/fr/28.webp)



![image](assets/fr/29.webp)



![image](assets/fr/30.webp)



Bước tiếp theo là ký hợp đồng. Vẫn trong ứng dụng di động, hãy nhấn ''**Ký Contract**''



![image](assets/fr/31.webp)



![image](assets/fr/32.webp)



Khi bạn hoàn tất việc ký hợp đồng, Debifi sẽ tự động tạo một địa chỉ Bitcoin đa chữ ký duy nhất (ký quỹ 3-sur-4) cho hợp đồng của bạn. Miễn là bitcoin của bạn vẫn còn trong ký quỹ, chúng sẽ không thể được sử dụng ở nơi khác.



### Gửi tiền bảo lãnh và nhận tiền của bạn



Bước cuối cùng là gửi tài sản thế chấp Bitcoin của bạn vào hệ thống ký quỹ đa chữ ký. Debifi sẽ hiển thị cho bạn địa chỉ ký quỹ (B) và số lượng BTC (A) cần gửi (tài sản thế chấp + hoa hồng).



![image](assets/fr/33.webp)



Bạn cũng sẽ nhận được thông báo này trong ứng dụng di động của mình.



![image](assets/fr/34.webp)



Ngay khi khoản tiền gửi của bạn được xác nhận, bên cho vay sẽ trả số tiền vay vào địa chỉ nhận mà bạn đã chỉ định, hoàn tất giao dịch và cung cấp cho bạn quyền truy cập vào số tiền bạn cần.



Sau đó, bạn sẽ nhận được thông báo từ Debifi, yêu cầu bạn thanh toán phí hoặc hoa hồng cho vay để nâng cao tiến độ xử lý khoản vay.



Trên thực tế, sau khi hợp đồng được lập, phí vay sẽ tự động được khấu trừ từ tài sản thế chấp được người vay ký quỹ tại địa chỉ ký quỹ nhiều chữ ký.



Tất cả những gì bạn cần làm là ký một giao dịch cho phép Debifi khấu trừ hoa hồng từ khoản bảo lãnh. Về phần mình, bên cho vay của bạn cũng sẽ cần ký giao dịch khấu trừ phí, nếu không Debifi sẽ không thể nhận được hoa hồng.



![image](assets/fr/35.webp)



Phí cho vay áp dụng là 1,5-2%, tùy thuộc vào thời hạn hợp đồng. Nền tảng chỉ tính hoa hồng theo Bitcoin.



## Theo dõi khoản vay



Sau khi khoản vay được kích hoạt, Debifi cho phép bạn theo dõi hợp đồng theo thời gian thực. Trong giao diện, bạn sẽ tìm thấy:



- Số tiền vay và thời hạn còn lại.
- Tỷ lệ LTV (Tỷ lệ cho vay trên giá trị) hiện tại, tăng khi giá BTC giảm và giá trị tài sản thế chấp của bạn giảm.




Người vay sẽ được thông báo khi giá trị tài sản thế chấp giảm, và thông tin này cũng được hiển thị trên trang tóm tắt hợp đồng. Để khôi phục tỷ lệ cho vay trên giá trị ban đầu, người vay phải:



- gửi thêm tài sản thế chấp;
- trả toàn bộ hoặc một phần nợ.




Trong trường hợp giá tài sản thế chấp tăng, người vay sẽ được giữ lại mọi khoản lãi vốn trên tài sản thế chấp. Người vay chỉ nợ số tiền vay, được xác định trước và không phụ thuộc vào giá Bitcoin.




## Hoàn trả và thu hồi tài sản thế chấp



Khi kết thúc thời hạn đã thỏa thuận (hoặc sớm hơn nếu bạn muốn), bạn phải trả hết khoản vay.


Trong Debifi:





- Vào hợp đồng của bạn và nhấp vào **Trả nợ**. Nhập tổng số tiền phải trả (gốc + lãi).





- Gửi stablecoin từ wallet của bạn đến địa chỉ của bên cho vay được chỉ định và quay lại để xác nhận việc hoàn trả trên nền tảng bằng cách sao chép **ID** của giao dịch hoàn trả vào tab chuyên dụng. Điều này giúp Debifi dễ dàng thực hiện kiểm tra hơn.



Sau khi bên cho vay (và bạn) xác nhận khoản thanh toán, Debifi sẽ yêu cầu bạn **hoàn tiền**. Tài sản thế chấp Bitcoin của bạn sẽ được giải phóng và bạn có thể trả lại từ tài khoản ký quỹ vào tài khoản wallet của mình. Đừng quên thu thập tất cả Bitcoin của bạn.



Ngay khi bạn nhận được bitcoin, hợp đồng vay sẽ thay đổi thành **Contract đã hoàn tất**.



Xin chúc mừng! Bạn đã hoàn tất quá trình.




## Thực hành tốt nhất và an toàn



Dù mục tiêu hay động lực của bạn là gì - tài trợ cho một dự án, mua bất động sản, mua bitcoin, v.v. - hãy hết sức thận trọng trước khi vay vốn được bảo đảm bằng Bitcoin. Hãy dành thời gian đánh giá kỹ lưỡng quyết định của bạn, vì Bitcoin vẫn là một tài sản biến động. **Giá của Bitcoin giảm mạnh có thể dẫn đến việc buộc phải thanh lý số bitcoin của bạn.**



Theo dõi tỷ lệ cho vay/tài sản thế chấp (LTV). Nếu có thể, hãy thiết lập cảnh báo (giá BTC, LTV). Đừng để tỷ lệ này đạt gần 90%. Nếu nghi ngờ, hãy tăng tài sản thế chấp hoặc trả nợ sớm.



Kiểm soát khóa của bạn. Giữ BTC của bạn trong một thiết bị wallet an toàn (tốt nhất là ổ cứng hoặc một thiết bị wallet uy tín). Không đặt mã PIN liên quan đến một ngày quan trọng trong cuộc đời bạn và không bao giờ chia sẻ cụm từ khôi phục. Trên Debifi, bạn sẽ lưu khóa riêng tư của mình trong ứng dụng - Debifi không biết điều đó.



Hãy bắt đầu với số tiền nhỏ nếu có thể. Với khoản vay đầu tiên, hãy thử nghiệm một khoản tiền vừa phải để làm quen với quy trình.



Chỉ sử dụng trang web chính thức của Debifi để cập nhật tin tức và tránh các liên kết không rõ nguồn gốc hoặc lừa đảo. Hãy cập nhật ứng dụng, bảo vệ điện thoại thông minh của bạn bằng mã PIN và chọn Hardware Wallet tương thích.



Ngoài ra, nếu bạn là người cho vay, video hướng dẫn này sẽ hướng dẫn bạn cách sử dụng nền tảng Debifi. Từ việc lựa chọn người vay quan tâm đến ưu đãi của bạn, đến việc cung cấp khóa công khai, ký kết thỏa thuận, chuyển giao stablecoin, v.v.



![video](https://youtu.be/g8iLxwI4xT0)



Bây giờ bạn đã biết cách sử dụng nền tảng Debifi để vay tiền.



Tôi khuyên bạn nên tham gia khóa học này, khóa học sẽ cung cấp cái nhìn sâu sắc về Bitcoin, Stablecoin và đóng góp của chúng cho chủ quyền.



https://planb.academy/courses/fdc41e06-ea63-4bf0-a5ac-a0185fe30e46