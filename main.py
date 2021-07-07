import requests
class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = {'Authorization': 'OAuth AQAAAAAG8mVbAADLW7Ds54nsaEQevxWBx2abfus'}
        params = {"path": f"HW_API/{self.file_path}"}
        response = requests.get(url=url, headers=headers, params=params)
        print(response.json())
        resp = requests.put(response.json()['href'], data=open(self.file_path, 'rb'))
        if resp.status_code == 201:
            return print("Файл успешно загружен")

if __name__ == '__main__':
    uploader = YaUploader('new.txt')
    result = uploader.upload()