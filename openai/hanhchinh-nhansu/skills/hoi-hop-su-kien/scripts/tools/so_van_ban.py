"""Sổ đăng ký văn bản đi, văn bản đến (CSV mở được bằng Excel).

Theo Nghị định 30/2020/NĐ-CP: số văn bản đi đánh liên tục từ 01 ngày 01/01 đến 31/12 hằng năm (Điều 15);
văn bản đến được đăng ký, trình, chuyển giao trong ngày hoặc ngày làm việc tiếp theo (Điều 20–22).
Mặc định lưu tại ./so-van-ban/ trong thư mục làm việc; đổi bằng tham số thu_muc.
"""
import csv
import os
from datetime import date, datetime

from . import lich_vn

COT_DI = ["so_thu_tu", "so_ky_hieu", "ngay_van_ban", "loai_van_ban", "trich_yeu", "nguoi_ky",
          "noi_nhan", "don_vi_soan_thao", "so_ban", "ghi_chu", "thoi_diem_cap_so"]
COT_DEN = ["so_den", "ngay_den", "co_quan_ban_hanh", "so_ky_hieu", "ngay_van_ban", "loai_van_ban",
           "trich_yeu", "don_vi_ca_nhan_xu_ly", "han_xu_ly", "trang_thai", "ngay_hoan_thanh", "ghi_chu"]

VIET_TAT = {
    "nghị quyết": "NQ", "quyết định": "QĐ", "chỉ thị": "CT", "quy chế": "QC", "quy định": "QyĐ",
    "thông cáo": "TC", "thông báo": "TB", "hướng dẫn": "HD", "chương trình": "CTr", "kế hoạch": "KH",
    "phương án": "PA", "đề án": "ĐA", "dự án": "DA", "báo cáo": "BC", "biên bản": "BB", "tờ trình": "TTr",
    "hợp đồng": "HĐ", "công điện": "CĐ", "bản ghi nhớ": "GN", "bản thỏa thuận": "TTh", "giấy ủy quyền": "UQ",
    "giấy mời": "GM", "giấy giới thiệu": "GGT", "giấy nghỉ phép": "NP", "phiếu gửi": "PG",
    "phiếu chuyển": "PC", "phiếu báo": "PB", "công văn": "",
}


def _file(thu_muc, loai, nam):
    thu_muc = thu_muc or os.path.join(os.getcwd(), "so-van-ban")
    os.makedirs(thu_muc, exist_ok=True)
    return os.path.join(thu_muc, f"so-van-ban-{loai}-{nam}.csv")


def _doc(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def _ghi(path, cot, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cot)
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, path)


def _nam(ngay):
    return lich_vn._ngay(ngay).year if ngay else date.today().year


def cap_so_van_ban_di(loai_van_ban, viet_tat_co_quan, trich_yeu, viet_tat_don_vi="", ngay_van_ban=None,
                      nguoi_ky="", noi_nhan="", so_ban="", ghi_chu="", thu_muc=None, xem_truoc=False):
    nam = _nam(ngay_van_ban)
    path = _file(thu_muc, "di", nam)
    rows = _doc(path)
    so = max([int(r["so_thu_tu"]) for r in rows] or [0]) + 1
    vt_loai = VIET_TAT.get(loai_van_ban.strip().lower())
    if vt_loai is None:
        vt_loai = loai_van_ban.strip()
    if vt_loai:  # văn bản có tên loại: Số/ViếtTắtLoại-CơQuan
        ky_hieu = f"{so:02d}/{vt_loai}-{viet_tat_co_quan}"
    else:  # công văn: Số/CơQuan-ĐơnVịSoạnThảo
        ky_hieu = f"{so:02d}/{viet_tat_co_quan}" + (f"-{viet_tat_don_vi}" if viet_tat_don_vi else "")
    ngay_vb = lich_vn._ngay(ngay_van_ban).strftime("%d/%m/%Y") if ngay_van_ban else date.today().strftime("%d/%m/%Y")
    dong = {"so_thu_tu": so, "so_ky_hieu": ky_hieu, "ngay_van_ban": ngay_vb, "loai_van_ban": loai_van_ban,
            "trich_yeu": trich_yeu, "nguoi_ky": nguoi_ky, "noi_nhan": noi_nhan,
            "don_vi_soan_thao": viet_tat_don_vi, "so_ban": so_ban, "ghi_chu": ghi_chu,
            "thoi_diem_cap_so": datetime.now().strftime("%d/%m/%Y %H:%M")}
    if xem_truoc:
        return {"xem_truoc": True, "so_se_cap": f"Số: {ky_hieu}", "file": path}
    rows.append(dong)
    _ghi(path, COT_DI, rows)
    return {"da_cap_so": f"Số: {ky_hieu}", "ngay": ngay_vb, "file": path,
            "nhac": "Chỉ cấp số sau khi văn bản đã được người có thẩm quyền ký (Điều 15, 16 NĐ 30/2020)."}


def dang_ky_van_ban_den(co_quan_ban_hanh, so_ky_hieu, trich_yeu, ngay_van_ban="", loai_van_ban="",
                        don_vi_ca_nhan_xu_ly="", han_xu_ly="", so_ngay_lam_viec_xu_ly=None, ngay_den=None,
                        ghi_chu="", thu_muc=None):
    d_den = lich_vn._ngay(ngay_den) if ngay_den else date.today()
    path = _file(thu_muc, "den", d_den.year)
    rows = _doc(path)
    trung = [r for r in rows if r["so_ky_hieu"].strip().lower() == so_ky_hieu.strip().lower()
             and r["co_quan_ban_hanh"].strip().lower() == co_quan_ban_hanh.strip().lower()]
    if trung:
        return {"canh_bao": "Văn bản này đã được đăng ký", "so_den": trung[0]["so_den"], "file": path}
    so = max([int(r["so_den"]) for r in rows] or [0]) + 1
    if not han_xu_ly and so_ngay_lam_viec_xu_ly:
        han_xu_ly = lich_vn.cong_cu_ngay_lam_viec(d_den.isoformat(), so_ngay=int(so_ngay_lam_viec_xu_ly))["ngay_ket_thuc"].split(", ")[1]
    rows.append({"so_den": so, "ngay_den": d_den.strftime("%d/%m/%Y"), "co_quan_ban_hanh": co_quan_ban_hanh,
                 "so_ky_hieu": so_ky_hieu, "ngay_van_ban": ngay_van_ban, "loai_van_ban": loai_van_ban,
                 "trich_yeu": trich_yeu, "don_vi_ca_nhan_xu_ly": don_vi_ca_nhan_xu_ly, "han_xu_ly": han_xu_ly,
                 "trang_thai": "Đang xử lý" if don_vi_ca_nhan_xu_ly else "Chờ phân phối",
                 "ngay_hoan_thanh": "", "ghi_chu": ghi_chu})
    _ghi(path, COT_DEN, rows)
    return {"so_den": so, "ngay_den": d_den.strftime("%d/%m/%Y"), "han_xu_ly": han_xu_ly or "(chưa đặt)", "file": path}


def cap_nhat_van_ban_den(so_den, nam=None, trang_thai=None, don_vi_ca_nhan_xu_ly=None, han_xu_ly=None,
                         ngay_hoan_thanh=None, ghi_chu=None, thu_muc=None):
    path = _file(thu_muc, "den", int(nam or date.today().year))
    rows = _doc(path)
    for r in rows:
        if str(r["so_den"]) == str(so_den):
            for k, v in [("trang_thai", trang_thai), ("don_vi_ca_nhan_xu_ly", don_vi_ca_nhan_xu_ly),
                         ("han_xu_ly", han_xu_ly), ("ngay_hoan_thanh", ngay_hoan_thanh), ("ghi_chu", ghi_chu)]:
                if v is not None:
                    r[k] = v
            if trang_thai and "hoàn thành" in trang_thai.lower() and not r["ngay_hoan_thanh"]:
                r["ngay_hoan_thanh"] = date.today().strftime("%d/%m/%Y")
            _ghi(path, COT_DEN, rows)
            return {"da_cap_nhat": r}
    return {"loi": f"Không tìm thấy văn bản đến số {so_den} trong {path}"}


def tra_cuu_so_van_ban(loai="den", nam=None, tu_khoa="", chi_qua_han=False, chi_chua_xong=False,
                       hom_nay=None, thu_muc=None):
    nam = int(nam or date.today().year)
    rows = _doc(_file(thu_muc, loai, nam))
    hn = lich_vn._ngay(hom_nay) if hom_nay else date.today()
    kq = []
    for r in rows:
        if tu_khoa and tu_khoa.lower() not in " ".join(r.values()).lower():
            continue
        if loai == "den":
            xong = "hoàn thành" in r.get("trang_thai", "").lower()
            if chi_chua_xong and xong:
                continue
            qua_han = False
            if r.get("han_xu_ly") and not xong:
                try:
                    qua_han = lich_vn._ngay(r["han_xu_ly"]) < hn
                except ValueError:
                    pass
            if chi_qua_han and not qua_han:
                continue
            r = dict(r, qua_han="Có" if qua_han else "")
        kq.append(r)
    return {"so_ban_ghi": len(kq), "ket_qua": kq[-200:]}


_THU_MUC = {"thu_muc": {"type": "string", "description": "Thư mục lưu sổ (mặc định ./so-van-ban)"}}
TOOLS = [
    {
        "name": "cap_so_van_ban_di",
        "description": "Cấp số, ký hiệu cho văn bản đi đúng NĐ 30/2020 (số liên tục trong năm; văn bản có tên loại: "
                       "Số/QĐ-ABC; công văn: Số/ABC-ĐV) và ghi vào sổ văn bản đi (CSV). Chỉ cấp số sau khi văn bản đã ký; "
                       "dùng xem_truoc=true để xem số sẽ cấp mà không ghi sổ.",
        "schema": {"type": "object", "required": ["loai_van_ban", "viet_tat_co_quan", "trich_yeu"], "properties": {
            "loai_van_ban": {"type": "string", "description": "Ví dụ: Quyết định, Thông báo, Tờ trình, Công văn"},
            "viet_tat_co_quan": {"type": "string", "description": "Chữ viết tắt tên cơ quan/công ty, ví dụ ABC"},
            "viet_tat_don_vi": {"type": "string", "description": "Đơn vị soạn thảo (bắt buộc với công văn), ví dụ HCNS"},
            "trich_yeu": {"type": "string"}, "ngay_van_ban": {"type": "string"}, "nguoi_ky": {"type": "string"},
            "noi_nhan": {"type": "string"}, "so_ban": {"type": "string"}, "ghi_chu": {"type": "string"},
            "xem_truoc": {"type": "boolean"}, **_THU_MUC}},
        "fn": cap_so_van_ban_di,
    },
    {
        "name": "dang_ky_van_ban_den",
        "description": "Đăng ký văn bản đến vào sổ (số đến tự tăng theo năm), giao đơn vị/cá nhân xử lý và tính hạn xử lý "
                       "theo ngày làm việc; cảnh báo nếu văn bản đã đăng ký.",
        "schema": {"type": "object", "required": ["co_quan_ban_hanh", "so_ky_hieu", "trich_yeu"], "properties": {
            "co_quan_ban_hanh": {"type": "string"}, "so_ky_hieu": {"type": "string"}, "trich_yeu": {"type": "string"},
            "ngay_van_ban": {"type": "string"}, "loai_van_ban": {"type": "string"},
            "don_vi_ca_nhan_xu_ly": {"type": "string"}, "han_xu_ly": {"type": "string"},
            "so_ngay_lam_viec_xu_ly": {"type": "integer"}, "ngay_den": {"type": "string"},
            "ghi_chu": {"type": "string"}, **_THU_MUC}},
        "fn": dang_ky_van_ban_den,
    },
    {
        "name": "cap_nhat_van_ban_den",
        "description": "Cập nhật trạng thái xử lý, người xử lý, hạn, ngày hoàn thành của một văn bản đến theo số đến.",
        "schema": {"type": "object", "required": ["so_den"], "properties": {
            "so_den": {"type": "integer"}, "nam": {"type": "integer"}, "trang_thai": {"type": "string"},
            "don_vi_ca_nhan_xu_ly": {"type": "string"}, "han_xu_ly": {"type": "string"},
            "ngay_hoan_thanh": {"type": "string"}, "ghi_chu": {"type": "string"}, **_THU_MUC}},
        "fn": cap_nhat_van_ban_den,
    },
    {
        "name": "tra_cuu_so_van_ban",
        "description": "Tra cứu sổ văn bản đi/đến theo từ khóa; lọc văn bản đến chưa xong hoặc quá hạn xử lý để nhắc việc.",
        "schema": {"type": "object", "properties": {
            "loai": {"type": "string", "enum": ["di", "den"]}, "nam": {"type": "integer"},
            "tu_khoa": {"type": "string"}, "chi_qua_han": {"type": "boolean"}, "chi_chua_xong": {"type": "boolean"},
            "hom_nay": {"type": "string"}, **_THU_MUC}},
        "fn": tra_cuu_so_van_ban,
    },
]
