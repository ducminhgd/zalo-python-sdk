import os
from zalosdk import ZaloClient, AccessToken

if __name__ == "__main__":
    zc = ZaloClient(
        app_id=os.getenv("ZALO_APP_ID"),
        app_secret=os.getenv("ZALO_SECRET_KEY"),
        code_verifier=os.getenv("ZALO_CODE_VERIFIER"),
        http_proxy=os.getenv("ZALO_HTTP_PROXY", None),
        https_proxy=os.getenv("ZALO_HTTPS_PROXY", None),
    )

    zc.access_token = AccessToken(
        access_token=os.getenv("ZALO_ACCESS_TOKEN"),
        refresh_token=os.getenv("ZALO_REFRESH_TOKEN"),
        expires_in=int(os.getenv("ZALO_EXPIRES_IN", 90_000)),
    )
    print(zc.get_template_detail(os.getenv("ZNS_TEMPLATE_ID")))
