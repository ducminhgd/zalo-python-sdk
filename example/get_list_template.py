import os
from zalosdk import ZaloClient, AccessToken, ZNSTplListRequest

if __name__ == "__main__":
    zc = ZaloClient(
        app_id=os.getenv("ZALO_APP_ID"),
        app_secret=os.getenv("ZALO_SECRET_KEY"),
        code_verifier=os.getenv("ZALO_CODE_VERIFIER"),
    )
    
    # 1. Get access token from code
    print("1. Get access token from code")
    zc.access_token = zc.get_access_token(code=os.getenv("ZNS_CODE"))
    print(f'access_token: {zc.access_token.access_token}')
    print(f'refresh_token: {zc.access_token.refresh_token}')
    print(f'expires_in: {zc.access_token.expires_in}')

    # 2. Use access token to get template list
    print("2. Use access token to get template list")
    zc.access_token = AccessToken(
        access_token=os.getenv("ZALO_ACCESS_TOKEN"),
        refresh_token=os.getenv("ZALO_REFRESH_TOKEN"),
        expires_in=int(os.getenv("ZALO_EXPIRES_IN", 90_000)),
    )
    print(zc.get_template_list(ZNSTplListRequest(offset=0, limit=10)))
