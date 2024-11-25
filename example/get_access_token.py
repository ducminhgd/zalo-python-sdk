import os
from zalosdk import ZaloClient, AccessToken, ZNSTplListRequest

if __name__ == "__main__":
    zc = ZaloClient(
        app_id=os.getenv("ZALO_APP_ID"),
        app_secret=os.getenv("ZALO_SECRET_KEY"),
        code_verifier=os.getenv("ZALO_CODE_VERIFIER"),
        http_proxy=os.getenv("ZALO_HTTP_PROXY", None),
        https_proxy=os.getenv("ZALO_HTTPS_PROXY", None),
    )

    zc.access_token = zc.get_access_token(code=os.getenv("ZNS_CODE"))
    print(f'access_token: {zc.access_token.access_token}')
    print(f'refresh_token: {zc.access_token.refresh_token}')
    print(f'expires_in: {zc.access_token.expires_in}')
