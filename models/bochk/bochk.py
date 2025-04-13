import requests

class Bochk:
    def __init__(self, idType='CNID', serviceAccountType='G'):
        self.idType = idType
        self.serviceAccountType = serviceAccountType
        self.continueInputUrl = 'https://transaction.bochk.com/whk/form/openAccount/continueInput.action'

    def continueInput(self):
        # form data
        data = {
            'bean.idType': self.idType,  # 中国居民身份证
            'bean.serviceAccountType': self.serviceAccountType,  # 一般账户
            'acceptTerms': 'true',  # 勾选确认按钮
            '__checkbox_acceptTerms': 'true'  # 隐藏的复选框字段
        }

        # request header
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://transaction.bochk.com/whk/form/openAccount/input.action?lang=zh_CN'
        }

        # POST
        response = requests.post(self.continueInputUrl, data=data, headers=headers)


    def makeAppointment():
        pass