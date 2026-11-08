---
description: Xử lý một nhân viên nghỉ việc đúng luật – xác định căn cứ, ngày nghỉ hợp lệ, văn bản chấm dứt, bàn giao, tính tiền thanh toán trong 14 ngày làm việc, chốt BHXH, hướng dẫn trợ cấp thất nghiệp.
argument-hint: "[họ tên, loại HĐ, ngày vào làm, ngày nộp đơn/ngày dự kiến nghỉ, lý do]"
---

Xử lý nghỉ việc cho: $ARGUMENTS

1. Dùng skill `cham-dut-hop-dong`: hỏi những gì còn thiếu (ai chủ động, lý do, loại HĐ, tình trạng ốm/thai sản), chọn căn cứ đúng; kiểm tra Điều 37; tính ngày chấm dứt hợp lệ bằng `thoi_han_bao_truoc`.
2. Soạn văn bản phù hợp (thỏa thuận chấm dứt / thông báo / quyết định) – đúng thể thức, có căn cứ điều khoản.
3. Dùng skill `onboarding-offboarding`: biên bản bàn giao, danh sách thu hồi tài khoản – tài sản.
4. Bảng thanh toán: lương đến ngày nghỉ, phép chưa nghỉ (`phep_nam`), trợ cấp thôi việc/mất việc (`tro_cap_thoi_viec`), khấu trừ hợp pháp; hạn trả (`ngay_lam_viec` 14 ngày làm việc).
5. Dùng skill `bhxh-che-do`: báo giảm, xác nhận thời gian đóng BHXH, tin nhắn hướng dẫn NLĐ hưởng trợ cấp thất nghiệp (nộp trong 3 tháng).

Nếu có dấu hiệu tranh chấp, sa thải hoặc NLĐ phản đối: cảnh báo rủi ro (Điều 40, 41) và khuyến nghị tham vấn luật sư trước khi ký.
