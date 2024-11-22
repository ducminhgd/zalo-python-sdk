from enum import IntEnum


class ErrorCode(IntEnum):
    """
    Error code for Zalo API
    
    Read more: https://developers.zalo.me/docs/zalo-notification-service/phu-luc/bang-ma-loi
    """
    SUCCESS = 0
    UNKNOWN_ERROR = -100
    APPLICATION_INVALID = -101
    APPLICATION_NOT_EXISTED = -102
    APPLICATION_NOT_ACTIVATED = -103
    APPLICATION_SECRET_KEY_INVALID = -104
    APPLICATION_NOT_LINK_TO_ANY_OA = -105
    METHOD_UNSUPPORTED = -106
    MESSAGE_ID_INVALID = -107
    PHONE_NUMBER_INVALID = -108
    TEMPLATE_ID_INVALID = -109
    TEMPLATE_CANNOT_EDIT_THIS_TYPE = -1091
    ZERLO_VERSION_UNSUPPORTED = -110
    TEMPLATE_DATA_EMPTY = -111
    TEMPLATE_DATA_TYPE_IS_NOT_DEFINED = -112
    PARAMETER_NAME_DATA_BREAKS_LENGTH = -1121
    TEMPLATE_DATA_MISSING_PARAMETER_NAME = -1122
    QRCODE_CANNOT_BE_GENERATED = -1123
    PARAMETER_NAME_HAS_INVALID_FORMAT = -1124
    BUTTON_INVALID = -113
    # User is inactive, or message is rejected, or outdated Zalo version, or other internal error
    USER_CANNOT_RECEIVE_MESSAGE = -114
    OUT_OF_QUOTA = -115
    TEXT_INVALID = -116
    NO_PERMISSION_TO_ACCESS_TEMPLATE = -117
    ZALO_ACCOUNT_IS_NOT_EXISTED = -118
    ACCOUNT_CANNOT_RECEIVE_MESSAGE = -119
    OA_NO_PERMISSION_USE_FEATURE = -120
    OA_NO_PERMISSION_CREATE_TEMPLATE = -1201
    OA_NO_PERMISSION_USE_RESOURCE = -1202
    BODY_DATA_EMPTY = -121
    BODY_FORMAT_INVALID = -122
    RSA_MESSAGE_DECODE_FAILED = -123
    ACCESS_TOKEN_INVALID = -124
    APP_SECRET_PROOF_INVALID = -1241
    OA_ID_INVALID = -125
    OUT_OF_QUOTA_DEV = -126
    TEST_MESSAGE_SENT_TO_ADMIN_ONLY = -127
    ENCODING_KEY_NOT_EXISTED = -128
    RSA_KEY_CANNOT_BE_GENERATED = -129
    MAX_CHARACTER_LIMIT_EXCEEDED = -130
    ZNS_TEMPLATE_NOT_APPROVED = -131
    INVALID_PARAMETER = -132
    THIS_TEMPLATE_CANNOT_SENT_AT_NIGHT = -133  # 22:00 - 06:00
    USER_NOT_OPT_IN_INQUIRY = -134
    OA_NO_PERMISSION_SEND_ZNS_MESSAGE = -135  # Free or not verified
    OA_BLOCKED_SEND_ZNS_MESSAGE = -1351  # OA is blocked
    ZCA_ASSOCIATION_REQUIRED = -136
    ZCA_CHARGE_FAILURE = -137
    APP_NO_PERMISSION_ACCESS_FEATURE = -138
    USER_REFUSED_TO_RECEIVE_THIS_MSG_TYPE = -139
    OA_NO_PERMISSION_FOLLOW_UP = -140
    USER_REFUSED_TO_RECEIVE_FROM_OA = -141
    RSA_KEY_NOT_EXISTED = -142
    RSA_KEY_EXISTED = -143
    OA_EXCEED_DAILY_MSG_LIMIT = -144
    OA_EXCEED_MONTHLY_MSG_LIMIT = -1441
    OA_NO_PERMISSION_SEND_ZNS_TYPE = -145
    TEMPLATE_DISABLED_LOW_QUALITY = -146
    TEMPLATE_EXCEED_DAILY_QUOTA = -147
    OA_EXCEED_MONTHLY_FOLLOW_UP_PER_USER = -1471
    ZNS_JOURNEY_TOKEN_MISSING = -148
    ZNS_JOURNEY_TOKEN_INVALID = -149
    ZNS_JOURNEY_TOKEN_EXPIRED = -150
    ZNS_NOT_AN_E2EE_TEMPLATE = -151
    ZNS_GET_E2EE_TEMPLATE_FAILED = -152
    DATA_INVALID = -153
    UPLOADED_FILE_EXCEED_LIMIT = -158
    UPLOADED_FILE_FORMAT_INVALID = -159
    ZNS_OUT_OF_DAILY_QUOTA = -160
