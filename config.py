# -*- coding: utf-8 -*-
#

from os import environ as env
from ast import literal_eval as le

#
# GNU/Linux'da sistem değişkeni oluşturmak için yapmanız gerekenler:
# 1. Ev dizinize gidin.
#   $ cd ~
# 2. Ev dizinindeki .bashrc dosyasını düzenlemek için bir editör ile açın.
#   $ nano .bashrc
# 3. Dosyaya şunları ekleyin ve kaydedip çıkın.
#   token='token'
#   export token
# 4. Daha sonra şu komutu çalıştırın.
#   $ source .bashrc
#
# İşlem tamam, sistem değişkeni kullanılabilir durumda. Test etmek için:
#   $ echo $token
#

token = env.get("token")

prefix = [
    "+",
    "mjr+",
]

owner_ids = [
    564815690742235144,
]

#
# imgflip.com
#
# {"username": "", "password": ""}
imgflip_api = le(env.get("imgflip_api"))

#
# screenshotapi.net
#
# {"token": ""}
screenshot_api = le(env.get("screenshot_api"))
