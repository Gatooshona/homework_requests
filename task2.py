import requests

TOKEN = ''


class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': 'true'}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        return data

    def upload(self, disk_file_path: str, filename):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self._get_upload_link(disk_file_path=disk_file_path).get('href', '')
        response = requests.put(href, data=open(filename, 'rb'))
        if response.status_code == 201:
            print('Success')


if __name__ == '__main__':
    # # Получить путь к загружаемому файлу и токен от пользователя
    ya = YandexDisk(token=TOKEN)
    ya.upload('Netology/test.txt', 'test.txt')
