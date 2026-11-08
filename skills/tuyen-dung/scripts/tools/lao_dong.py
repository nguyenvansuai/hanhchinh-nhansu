"""Công cụ tính toán lao động theo Bộ luật Lao động 2019 và Nghị định 145/2020/NĐ-CP.

Mọi kết quả kèm căn cứ; trường hợp đặc thù (ngành nghề đặc thù, lao động nước ngoài, thỏa ước có lợi hơn)
cần chuyên viên kiểm tra thêm.
"""
from datetime import date, timedelta

from . import lich_vn, tham_so
from .lich_vn import _ngay


def _thang_giua(d0, d1):
    m = (d1.year - d0.year) * 12 + d1.month - d0.month
    if d1.day < d0.day:
        m -= 1
    return max(m, 0)


def _tien(x):
    return f"{round(x):,}".replace(",", ".") + " đ"


# ---------- Trợ cấp thôi việc / mất việc ----------
def tro_cap_thoi_viec(ngay_bat_dau, ngay_nghi, luong_binh_quan_6_thang, so_thang_dong_bhtn=0,
                      so_thang_da_tra_tro_cap=0, so_thang_khong_tinh=0, loai="thoi_viec"):
    d0, d1 = _ngay(ngay_bat_dau), _ngay(ngay_nghi)
    tong = _thang_giua(d0, d1)
    tinh = max(tong - int(so_thang_dong_bhtn) - int(so_thang_da_tra_tro_cap) - int(so_thang_khong_tinh), 0)
    nam_chan, le = divmod(tinh, 12)
    so_nam = nam_chan + (0 if le == 0 else (0.5 if le <= 6 else 1))
    L = float(luong_binh_quan_6_thang)
    if loai == "mat_viec":
        tien = max(so_nam * L, 2 * L)
        cong_thuc = f"max({so_nam} năm × 1 tháng lương; 2 tháng lương)"
        can_cu = "Điều 47 BLLĐ 2019 (mất việc do thay đổi cơ cấu, công nghệ, lý do kinh tế, chia tách sáp nhập)"
    else:
        tien = so_nam * 0.5 * L
        cong_thuc = f"{so_nam} năm × 1/2 tháng lương"
        can_cu = "Điều 46 BLLĐ 2019"
    canh_bao = []
    if loai == "thoi_viec" and tong < 12:
        canh_bao.append("Làm việc thường xuyên chưa đủ 12 tháng: không thuộc diện trợ cấp thôi việc.")
    if tinh == 0 and tong >= 12:
        canh_bao.append("Toàn bộ thời gian đã đóng BHTN hoặc đã được chi trả: trợ cấp = 0 (NLĐ hưởng trợ cấp thất nghiệp nếu đủ điều kiện).")
    return {
        "tong_thoi_gian_lam_viec_thang": tong,
        "thoi_gian_tinh_tro_cap_thang": tinh,
        "so_nam_tinh": so_nam,
        "cong_thuc": cong_thuc,
        "so_tien": _tien(tien),
        "so_tien_so": round(tien),
        "can_cu": can_cu + "; Điều 8 Nghị định 145/2020/NĐ-CP (tháng lẻ ≤ 6 tháng tính 1/2 năm, > 6 tháng tính 1 năm; "
                           "lương bình quân 6 tháng liền kề theo HĐLĐ trước khi nghỉ).",
        "khong_duoc_huong": "Không trả trợ cấp thôi việc khi NLĐ đủ điều kiện hưởng lương hưu, tự ý bỏ việc từ 5 ngày làm việc "
                            "liên tục không lý do chính đáng (điểm e khoản 1 Điều 36), hoặc bị sa thải.",
        "thoi_han_thanh_toan": "Trong 14 ngày làm việc kể từ ngày chấm dứt HĐLĐ; tối đa 30 ngày trong các trường hợp luật định (Điều 48).",
        "canh_bao": canh_bao,
        "luu_y": "Thời gian làm việc thực tế gồm cả thử việc, thời gian được cử đi học, nghỉ hưởng chế độ BHXH... (khoản 3 Điều 8 NĐ 145). "
                 "Nhập so_thang_khong_tinh cho thời gian không được tính (nếu có).",
    }


# ---------- Phép năm ----------
def phep_nam(ngay_bat_dau, nam, dieu_kien="binh_thuong", so_thang_lam_viec_trong_nam=None, so_thang_khong_tinh_tham_nien=0):
    co_ban = {"binh_thuong": 12, "chua_thanh_nien_khuyet_tat_nang_nhoc": 14, "dac_biet_nang_nhoc": 16}[dieu_kien]
    d0 = _ngay(ngay_bat_dau)
    cuoi_nam = date(int(nam), 12, 31)
    tham_nien_thang = max(_thang_giua(d0, cuoi_nam) - int(so_thang_khong_tinh_tham_nien), 0)
    tang = (tham_nien_thang // 12) // 5
    if so_thang_lam_viec_trong_nam is None:
        dau_nam = date(int(nam), 1, 1)
        so_thang_lam_viec_trong_nam = 12 if d0 <= dau_nam else min(12, _thang_giua(d0, cuoi_nam + timedelta(days=1)))
    thang = int(so_thang_lam_viec_trong_nam)
    if thang >= 12:
        so_ngay = co_ban + tang
        cach = f"{co_ban} ngày + {tang} ngày thâm niên"
    else:
        raw = (co_ban + tang) / 12 * thang
        so_ngay = int(raw + 0.5)
        cach = f"({co_ban} + {tang}) / 12 × {thang} tháng = {raw:.2f} → làm tròn {so_ngay}"
    return {
        "so_ngay_phep_nam": so_ngay, "cach_tinh": cach, "tham_nien_nam": tham_nien_thang // 12,
        "can_cu": "Điều 113, 114 BLLĐ 2019; Điều 65, 66 Nghị định 145/2020/NĐ-CP (chưa đủ 12 tháng tính theo tỷ lệ, "
                  "làm tròn số hàng đơn vị nếu phần thập phân từ 0,5; cứ đủ 5 năm làm việc tăng 1 ngày).",
        "luu_y": "Người sử dụng lao động quy định lịch nghỉ phép sau khi tham khảo ý kiến NLĐ và phải thông báo trước. "
                 "Nghỉ việc/mất việc mà chưa nghỉ hết phép thì được thanh toán tiền lương cho những ngày chưa nghỉ (khoản 3 Điều 113).",
    }


# ---------- Thời hạn báo trước ----------
def thoi_han_bao_truoc(ben, loai_hop_dong, ngay_thong_bao=None, truong_hop=""):
    """ben: nguoi_lao_dong | nguoi_su_dung_lao_dong; loai_hop_dong: khong_xac_dinh | tu_12_den_36_thang | duoi_12_thang."""
    bang = {"khong_xac_dinh": (45, "ngày"), "tu_12_den_36_thang": (30, "ngày"), "duoi_12_thang": (3, "ngày làm việc")}
    so, don_vi = bang[loai_hop_dong]
    kq = {"ben": ben, "loai_hop_dong": loai_hop_dong, "bao_truoc_it_nhat": f"{so} {don_vi}"}
    if ben == "nguoi_lao_dong":
        kq["can_cu"] = "Khoản 1 Điều 35 BLLĐ 2019. Ngành nghề, công việc đặc thù (thuyền viên, tiếp viên hàng không, người " \
                       "quản lý doanh nghiệp...): ít nhất 120 ngày với HĐ không xác định thời hạn hoặc từ 12 tháng trở lên " \
                       "(Điều 7 NĐ 145/2020)."
        kq["khong_can_bao_truoc"] = [
            "Không được bố trí đúng công việc, địa điểm, điều kiện làm việc đã thỏa thuận (trừ Điều 29)",
            "Không được trả đủ lương hoặc trả không đúng hạn (trừ khoản 4 Điều 97)",
            "Bị ngược đãi, đánh đập, nhục mạ, cưỡng bức lao động; bị quấy rối tình dục tại nơi làm việc",
            "Lao động nữ mang thai phải nghỉ việc theo khoản 1 Điều 138",
            "Đủ tuổi nghỉ hưu (trừ trường hợp thỏa thuận khác)",
            "Người sử dụng lao động cung cấp thông tin không trung thực làm ảnh hưởng đến việc thực hiện HĐLĐ",
        ]
    else:
        kq["can_cu"] = "Khoản 2 Điều 36 BLLĐ 2019 – áp dụng khi chấm dứt theo các điểm a, b, c, đ, g khoản 1 Điều 36. " \
                       "Riêng điểm b (ốm đau, tai nạn điều trị dài ngày): báo trước ít nhất 3 ngày làm việc."
        kq["khong_can_bao_truoc"] = [
            "NLĐ không có mặt tại nơi làm việc sau 15 ngày kể từ hết thời hạn tạm hoãn HĐLĐ (điểm d)",
            "NLĐ tự ý bỏ việc không có lý do chính đáng từ 5 ngày làm việc liên tục trở lên (điểm e)",
        ]
        kq["canh_bao"] = "Không được đơn phương chấm dứt với NLĐ đang ốm đau/điều trị theo chỉ định (trừ điểm b), đang nghỉ " \
                         "phép, nghỉ việc riêng được đồng ý; lao động nữ mang thai, nghỉ thai sản, nuôi con dưới 12 tháng (Điều 37)."
    if ngay_thong_bao:
        if don_vi == "ngày":
            kq["ngay_som_nhat_cham_dut"] = lich_vn.cong_cu_cong_ngay(ngay_thong_bao, so_ngay=so)["ket_qua"]
        else:
            kq["ngay_som_nhat_cham_dut"] = lich_vn.cong_cu_ngay_lam_viec(ngay_thong_bao, so_ngay=so)["ngay_ket_thuc"]
        kq["ghi_chu_ngay"] = "Tính từ ngày sau ngày thông báo; nên có văn bản thông báo có chữ ký nhận để làm bằng chứng."
    if truong_hop:
        kq["truong_hop_nguoi_dung_neu"] = truong_hop
    return kq


# ---------- Thử việc ----------
def kiem_tra_thu_viec(trinh_do, so_ngay_thu_viec, luong_thu_viec=None, luong_chinh_thuc=None, thoi_han_hop_dong_thang=None):
    toi_da, mo_ta = tham_so.THU_VIEC_TOI_DA[trinh_do]
    loi = []
    if thoi_han_hop_dong_thang is not None and float(thoi_han_hop_dong_thang) < 1:
        loi.append("HĐLĐ dưới 1 tháng: không được áp dụng thử việc (khoản 2 Điều 24).")
    if int(so_ngay_thu_viec) > toi_da:
        loi.append(f"Thử việc {so_ngay_thu_viec} ngày vượt mức tối đa {toi_da} ngày cho nhóm: {mo_ta}.")
    if luong_thu_viec and luong_chinh_thuc:
        tl = float(luong_thu_viec) / float(luong_chinh_thuc)
        if tl < 0.85:
            loi.append(f"Lương thử việc bằng {tl:.0%} lương chính thức, thấp hơn mức tối thiểu 85% (Điều 26).")
    return {
        "hop_le": not loi, "loi": loi, "thu_viec_toi_da_ngay": toi_da, "nhom": mo_ta,
        "can_cu": "Điều 24–27 BLLĐ 2019. Chỉ thử việc một lần cho một công việc. Kết thúc thử việc phải thông báo kết quả; "
                  "đạt thì tiếp tục HĐLĐ đã ký (nếu thỏa thuận thử việc trong HĐLĐ) hoặc ký HĐLĐ. Trong thời gian thử việc mỗi "
                  "bên được hủy bỏ không cần báo trước, không phải bồi thường.",
    }


# ---------- Thời hiệu xử lý kỷ luật ----------
def thoi_hieu_ky_luat(ngay_xay_ra_vi_pham, lien_quan_tai_chinh_tai_san_bi_mat=False, ngay_hop_du_kien=None):
    d0 = _ngay(ngay_xay_ra_vi_pham)
    thang = 12 if lien_quan_tai_chinh_tai_san_bi_mat else 6
    het = lich_vn.cong_cu_cong_ngay(d0.isoformat(), so_thang=thang)["ket_qua"]
    kq = {
        "thoi_hieu": f"{thang} tháng kể từ ngày xảy ra vi phạm",
        "het_thoi_hieu": het,
        "can_cu": "Điều 123 BLLĐ 2019 (12 tháng với vi phạm liên quan trực tiếp đến tài chính, tài sản, tiết lộ bí mật công nghệ, "
                  "bí mật kinh doanh). Nếu hết thời hiệu khi NLĐ đang trong thời gian không được xử lý (khoản 4 Điều 122: nghỉ ốm, "
                  "nghỉ phép, bị tạm giữ/tạm giam, chờ kết quả xác minh, lao động nữ mang thai/nuôi con dưới 12 tháng...) thì được "
                  "kéo dài nhưng không quá 60 ngày kể từ ngày hết thời gian đó.",
        "quy_trinh_bat_buoc": [
            "Chứng minh được lỗi của NLĐ; hành vi phải được quy định trong nội quy lao động/HĐLĐ/pháp luật",
            "Thông báo nội dung, thời gian, địa điểm họp xử lý kỷ luật cho NLĐ và tổ chức đại diện NLĐ (nếu NLĐ là thành viên) "
            "ít nhất 5 ngày làm việc trước ngày họp (Điều 70 NĐ 145/2020)",
            "Cuộc họp có mặt tổ chức đại diện NLĐ (nếu NLĐ là thành viên); NLĐ có quyền tự bào chữa hoặc nhờ người bào chữa; "
            "NLĐ dưới 15 tuổi phải có người đại diện theo pháp luật",
            "Lập biên bản cuộc họp, thông qua và có chữ ký người tham dự; ai không ký phải ghi lý do",
            "Ra quyết định xử lý kỷ luật trong thời hiệu và gửi cho NLĐ, tổ chức đại diện NLĐ",
        ],
        "cam": "Không phạt tiền, cắt lương thay việc kỷ luật; không xử lý một hành vi bằng nhiều hình thức; không kỷ luật vì tham gia "
               "đình công; không xâm phạm thân thể, nhân phẩm (Điều 127).",
    }
    if ngay_hop_du_kien:
        dh = _ngay(ngay_hop_du_kien)
        # ngày thông báo chậm nhất: lùi 5 ngày làm việc
        nghi, lam_bu = lich_vn.tap_ngay_nghi(dh.year - 1, dh.year, (5, 6))
        d, dem = dh, 0
        while dem < 5:
            d -= timedelta(days=1)
            if lich_vn.la_ngay_lam_viec(d, nghi, lam_bu, (5, 6)):
                dem += 1
        kq["thong_bao_hop_cham_nhat"] = lich_vn._fmt(d)
        if dh > lich_vn._ngay(het.split(", ")[1]):
            kq["canh_bao"] = "Ngày họp dự kiến đã quá thời hiệu xử lý kỷ luật."
    return kq


# ---------- Lương net / gross ----------
def _thue_tncn(tntt, ngay):
    _, bieu, nguon = tham_so.theo_ngay(tham_so.BIEU_THUE_TNCN, ngay)
    thue, duoi = 0.0, 0.0
    for tren, ts in bieu:
        if tntt > duoi:
            thue += (min(tntt, tren) - duoi) * ts
        duoi = tren
    return thue, nguon


def _tinh_tu_gross(gross, luong_dong_bh, vung, npt, ngay, mien_thue):
    _, ltt, nguon_ltt = tham_so.theo_ngay(tham_so.LUONG_TOI_THIEU_VUNG, ngay)
    _, lcs, nguon_lcs = tham_so.theo_ngay(tham_so.LUONG_CO_SO, ngay)
    _, gt_bt, gt_npt, nguon_gt = tham_so.theo_ngay(tham_so.GIAM_TRU_GIA_CANH, ngay)
    ltt_thang = ltt[vung][0]
    tran_xh = 20 * lcs
    tran_tn = 20 * ltt_thang
    nld = tham_so.TY_LE_BH["nld"]
    bh_xh_yt = min(luong_dong_bh, tran_xh)
    bh_tn = min(luong_dong_bh, tran_tn)
    bhxh, bhyt, bhtn = bh_xh_yt * nld["bhxh"], bh_xh_yt * nld["bhyt"], bh_tn * nld["bhtn"]
    tong_bh = bhxh + bhyt + bhtn
    tntt = max(gross - mien_thue - tong_bh - gt_bt - npt * gt_npt, 0)
    thue, nguon_thue = _thue_tncn(tntt, ngay)
    net = gross - tong_bh - thue
    dn = tham_so.TY_LE_BH["dn"]
    dn_bh = bh_xh_yt * (dn["bhxh_huu_tri"] + dn["bhxh_om_dau_thai_san"] + dn["tnld_bnn"] + dn["bhyt"]) + bh_tn * dn["bhtn"]
    kpcd = luong_dong_bh * tham_so.TY_LE_BH["kpcd"]
    return {
        "luong_gross": _tien(gross), "luong_dong_bao_hiem": _tien(luong_dong_bh),
        "nld_dong": {"bhxh_8%": _tien(bhxh), "bhyt_1.5%": _tien(bhyt), "bhtn_1%": _tien(bhtn), "tong": _tien(tong_bh)},
        "giam_tru": {"ban_than": _tien(gt_bt), "nguoi_phu_thuoc": f"{npt} × {_tien(gt_npt)}", "thu_nhap_mien_thue": _tien(mien_thue)},
        "thu_nhap_tinh_thue": _tien(tntt), "thue_tncn": _tien(thue), "luong_net": _tien(net), "net_so": round(net),
        "chi_phi_doanh_nghiep": {"bao_hiem_dn_dong": _tien(dn_bh), "kinh_phi_cong_doan_2%": _tien(kpcd),
                                 "tong_chi_phi": _tien(gross + dn_bh + kpcd)},
        "tham_so": {"luong_toi_thieu_vung": f"Vùng {vung}: {_tien(ltt_thang)} ({nguon_ltt})",
                    "tran_bhxh_bhyt": f"{_tien(tran_xh)} = 20 × lương cơ sở {_tien(lcs)} ({nguon_lcs})",
                    "tran_bhtn": f"{_tien(tran_tn)} = 20 × lương tối thiểu vùng",
                    "giam_tru": nguon_gt, "bieu_thue": nguon_thue},
        "canh_bao": ([f"Lương đóng BH thấp hơn lương tối thiểu vùng {_tien(ltt_thang)}"] if luong_dong_bh < ltt_thang else []),
    }


def luong_net_gross(muc_luong, chieu="gross_sang_net", vung=1, so_nguoi_phu_thuoc=0, luong_dong_bao_hiem=None,
                    thu_nhap_mien_thue=0, ngay_ap_dung=None):
    ngay = _ngay(ngay_ap_dung) if ngay_ap_dung else date.today()
    vung, npt, mt = int(vung), int(so_nguoi_phu_thuoc), float(thu_nhap_mien_thue)
    if chieu == "gross_sang_net":
        g = float(muc_luong)
        kq = _tinh_tu_gross(g, float(luong_dong_bao_hiem or g), vung, npt, ngay, mt)
    else:
        net_mt = float(muc_luong)
        lo, hi = net_mt, net_mt * 2 + 10_000_000
        for _ in range(80):
            mid = (lo + hi) / 2
            n = _tinh_tu_gross(mid, float(luong_dong_bao_hiem or mid), vung, npt, ngay, mt)["net_so"]
            lo, hi = (mid, hi) if n < net_mt else (lo, mid)
        kq = _tinh_tu_gross(round(hi), float(luong_dong_bao_hiem or round(hi)), vung, npt, ngay, mt)
        kq["ghi_chu"] = "Gross tính ngược từ net mong muốn (sai số dưới 1.000 đ)."
    kq["ngay_ap_dung"] = ngay.strftime("%d/%m/%Y")
    kq["luu_y"] = "Ước tính cho đàm phán lương/offer. Bảng lương chính thức (khấu trừ, quyết toán) dùng bộ skill kế toán " \
                  "(luong-bao-hiem). Phụ cấp ăn ca, điện thoại... chỉ miễn thuế trong mức và điều kiện luật định."
    return kq


def kiem_tra_luong_toi_thieu(muc_luong, vung=1, ngay_ap_dung=None, theo_gio=False):
    ngay = _ngay(ngay_ap_dung) if ngay_ap_dung else date.today()
    _, ltt, nguon = tham_so.theo_ngay(tham_so.LUONG_TOI_THIEU_VUNG, ngay)
    muc = ltt[int(vung)][1 if theo_gio else 0]
    ok = float(muc_luong) >= muc
    return {"dat": ok, "muc_toi_thieu": _tien(muc) + ("/giờ" if theo_gio else "/tháng"), "nguon": nguon,
            "ghi_chu": "So với mức lương cho công việc giản đơn nhất trong điều kiện bình thường; vùng xác định theo địa bàn "
                       "(xã/phường) nơi người lao động làm việc theo Phụ lục nghị định."}


TOOLS = [
    {"name": "tro_cap_thoi_viec", "fn": tro_cap_thoi_viec,
     "description": "Tính trợ cấp thôi việc (Điều 46) hoặc mất việc làm (Điều 47) BLLĐ 2019: trừ thời gian đã đóng BHTN, thời gian "
                    "đã chi trả; quy tắc tháng lẻ của NĐ 145/2020; kèm điều kiện không được hưởng và hạn thanh toán.",
     "schema": {"type": "object", "required": ["ngay_bat_dau", "ngay_nghi", "luong_binh_quan_6_thang"], "properties": {
         "ngay_bat_dau": {"type": "string"}, "ngay_nghi": {"type": "string"},
         "luong_binh_quan_6_thang": {"type": "number"}, "so_thang_dong_bhtn": {"type": "integer"},
         "so_thang_da_tra_tro_cap": {"type": "integer"}, "so_thang_khong_tinh": {"type": "integer"},
         "loai": {"type": "string", "enum": ["thoi_viec", "mat_viec"]}}}},
    {"name": "phep_nam", "fn": phep_nam,
     "description": "Tính số ngày nghỉ phép năm của người lao động (12/14/16 ngày, +1 ngày mỗi 5 năm thâm niên, tính theo tỷ lệ khi "
                    "chưa đủ 12 tháng) theo Điều 113–114 BLLĐ 2019 và NĐ 145/2020.",
     "schema": {"type": "object", "required": ["ngay_bat_dau", "nam"], "properties": {
         "ngay_bat_dau": {"type": "string"}, "nam": {"type": "integer"},
         "dieu_kien": {"type": "string", "enum": ["binh_thuong", "chua_thanh_nien_khuyet_tat_nang_nhoc", "dac_biet_nang_nhoc"]},
         "so_thang_lam_viec_trong_nam": {"type": "integer"}, "so_thang_khong_tinh_tham_nien": {"type": "integer"}}}},
    {"name": "thoi_han_bao_truoc", "fn": thoi_han_bao_truoc,
     "description": "Thời hạn báo trước khi đơn phương chấm dứt HĐLĐ (Điều 35, 36 BLLĐ 2019) theo bên chấm dứt và loại hợp đồng, "
                    "các trường hợp không cần báo trước, ngày sớm nhất được chấm dứt tính từ ngày thông báo.",
     "schema": {"type": "object", "required": ["ben", "loai_hop_dong"], "properties": {
         "ben": {"type": "string", "enum": ["nguoi_lao_dong", "nguoi_su_dung_lao_dong"]},
         "loai_hop_dong": {"type": "string", "enum": ["khong_xac_dinh", "tu_12_den_36_thang", "duoi_12_thang"]},
         "ngay_thong_bao": {"type": "string"}, "truong_hop": {"type": "string"}}}},
    {"name": "kiem_tra_thu_viec", "fn": kiem_tra_thu_viec,
     "description": "Kiểm tra thời gian và tiền lương thử việc có đúng Điều 24–27 BLLĐ 2019 không (tối đa 180/60/30/6 ngày; lương ≥ 85%).",
     "schema": {"type": "object", "required": ["trinh_do", "so_ngay_thu_viec"], "properties": {
         "trinh_do": {"type": "string", "enum": ["quan_ly_doanh_nghiep", "cao_dang_tro_len", "trung_cap", "khac"]},
         "so_ngay_thu_viec": {"type": "integer"}, "luong_thu_viec": {"type": "number"},
         "luong_chinh_thuc": {"type": "number"}, "thoi_han_hop_dong_thang": {"type": "number"}}}},
    {"name": "thoi_hieu_ky_luat", "fn": thoi_hieu_ky_luat,
     "description": "Tính thời hiệu xử lý kỷ luật lao động (6 hoặc 12 tháng – Điều 123 BLLĐ 2019), ngày chậm nhất phải gửi thông báo "
                    "họp (5 ngày làm việc trước – Điều 70 NĐ 145/2020) và các bước bắt buộc của quy trình kỷ luật.",
     "schema": {"type": "object", "required": ["ngay_xay_ra_vi_pham"], "properties": {
         "ngay_xay_ra_vi_pham": {"type": "string"}, "lien_quan_tai_chinh_tai_san_bi_mat": {"type": "boolean"},
         "ngay_hop_du_kien": {"type": "string"}}}},
    {"name": "luong_net_gross", "fn": luong_net_gross,
     "description": "Quy đổi lương gross ↔ net theo quy định tại ngày áp dụng: BHXH/BHYT/BHTN phần NLĐ (có trần), giảm trừ gia cảnh, "
                    "biểu thuế TNCN (5 bậc từ 2026), chi phí doanh nghiệp (BH 21,5% + KPCĐ 2%). Dùng cho offer, đàm phán lương.",
     "schema": {"type": "object", "required": ["muc_luong"], "properties": {
         "muc_luong": {"type": "number"}, "chieu": {"type": "string", "enum": ["gross_sang_net", "net_sang_gross"]},
         "vung": {"type": "integer", "enum": [1, 2, 3, 4]}, "so_nguoi_phu_thuoc": {"type": "integer"},
         "luong_dong_bao_hiem": {"type": "number"}, "thu_nhap_mien_thue": {"type": "number"},
         "ngay_ap_dung": {"type": "string"}}}},
    {"name": "kiem_tra_luong_toi_thieu", "fn": kiem_tra_luong_toi_thieu,
     "description": "So mức lương với lương tối thiểu vùng tại ngày áp dụng (NĐ 293/2025/NĐ-CP từ 01/01/2026).",
     "schema": {"type": "object", "required": ["muc_luong"], "properties": {
         "muc_luong": {"type": "number"}, "vung": {"type": "integer", "enum": [1, 2, 3, 4]},
         "ngay_ap_dung": {"type": "string"}, "theo_gio": {"type": "boolean"}}}},
]
