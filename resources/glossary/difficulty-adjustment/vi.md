---
term: ĐIỀU CHỈNH ĐỘ KHÓ
---

Điều chỉnh độ khó là quá trình định kỳ nhằm xác định lại mục tiêu độ khó cho cơ chế chứng minh công việc (đào) trên Bitcoin. Sự kiện này xảy ra sau mỗi 2016 khối (khoảng mỗi hai tuần). Nó nhằm mục đích tăng hoặc giảm yếu tố độ khó (còn được gọi là mục tiêu độ khó), tùy thuộc vào tốc độ tìm kiếm của 2016 khối cuối cùng. Việc điều chỉnh nhằm duy trì tốc độ sản xuất khối ổn định và dự đoán được, với tần suất một khối mỗi 10 phút, bất chấp sự biến đổi trong công suất tính toán được triển khai bởi các thợ mỏ. Sự thay đổi trong độ khó trong quá trình điều chỉnh được giới hạn bởi một yếu tố 4. Công thức được các nút thực hiện để tính toán mục tiêu mới như sau:
$$N = A \cdot \left(\frac{T}{1,209,600}\right)$$
&nbsp;
Nơi mà:
* $N$: Mục tiêu mới;
* $A$: Mục tiêu cũ của 2016 khối cuối cùng;
* $T$: Tổng thời gian thực tế của 2016 khối cuối cùng tính bằng giây;
* $1,209,600$: Thời gian mục tiêu tính bằng giây để sản xuất 2016 khối với khoảng cách 10 phút giữa mỗi khối.

> ► *Trong tiếng Pháp, thuật ngữ "reciblage" đôi khi cũng được sử dụng để chỉ việc điều chỉnh. Trong tiếng Anh, nó được gọi là "Difficulty Adjustment".*