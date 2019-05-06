# coding=utf-8
from GetMyPincode.settings import env


if env == "development":
    from GetMyPincode.config.dev import *

elif env == "pre-production":
    from GetMyPincode.config.preprod import *

elif env == "production":
    from GetMyPincode.config.prod import *
