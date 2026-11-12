"""کلاینت پایه — ارتباط با سرور گیت‌بین"""
import json
import requests
from .errors import raise_from_response, GitbinError


class GitbinClient:
    def __init__(self, token: str, base_url: str = "https://api.gitbin.site", timeout: int = 40):
        """
        token: توکن ربات (مثل 1780243415:K0WZ...)
        base_url: آدرس سرور (پیش‌فرض api.gitbin.site)
        timeout: ثانیه صبر برای پاسخ
        """
        self.token = token
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    # ─────────────────────────────────────────
    # هسته: ارسال درخواست
    # ─────────────────────────────────────────
    def _call(self, method: str, **params):
        """
        متد رو صدا بزن. params می‌تونه هر پارامتری باشه.
        برمی‌گردونه: result (بدون ok)
        خطا: GitbinError raise می‌کنه
        """
        url = f"{self.base_url}/bot{self.token}/{method}"

        # پاک‌سازی: حذف Noneها و تبدیل bool/dict/list به رشته
        clean = {}
        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, bool):
                clean[k] = "true" if v else "false"
            elif isinstance(v, (dict, list)):
                clean[k] = json.dumps(v, ensure_ascii=False)
            else:
                clean[k] = v

        try:
            r = self.session.post(url, data=clean, timeout=self.timeout)
        except requests.RequestException as exc:
            raise GitbinError(0, f"CONNECTION_ERROR: {exc}", method)

        # پاسخ JSON
        try:
            data = r.json()
        except ValueError:
            raise GitbinError(r.status_code, f"BAD_JSON: {r.text[:200]}", method)

        # خطای API
        if not data.get("ok"):
            raise_from_response(data, method)

        return data.get("result")

    # ─────────────────────────────────────────
    # میان‌بر برای GET (بعضی متدها فقط GET قبول می‌کنن)
    # ─────────────────────────────────────────
    def _call_get(self, method: str, **params):
        url = f"{self.base_url}/bot{self.token}/{method}"
        clean = {k: v for k, v in params.items() if v is not None}
        try:
            r = self.session.get(url, params=clean, timeout=self.timeout)
            data = r.json()
        except Exception as exc:
            raise GitbinError(0, str(exc), method)
        if not data.get("ok"):
            raise_from_response(data, method)
        return data.get("result")