import json
import sys

import requests

from huawei_api_signer import HttpRequest, Signer


argv = sys.argv[1:]
if len(argv) < 3:
    print('Usage: python refresh_cdn_cache.py <access_key_id> <access_key_secret> <file_path>')
    sys.exit(1)

access_key_id = argv[0]
access_key_secret = argv[1]
file_paths = argv[2:]

print('file_paths:', file_paths)


def request_cdn_api(_request_dict):
    r = HttpRequest('POST', 'https://cdn.myhuaweicloud.com/v1.0/cdn/content/refresh-tasks')
    r.headers = {'content-type': 'application/json'}
    r.body = json.dumps(_request_dict)
    sig = Signer()
    sig.Key = access_key_id
    sig.Secret = access_key_secret
    sig.Sign(r)
    resp = requests.post(r.scheme + '://' + r.host + r.uri, headers=r.headers, data=r.body)
    if resp.status_code != 200:
        print('Refresh huawei CDN cache failed: %s', resp.text)
        exit(1)


if __name__ == '__main__':
    file_list = []
    directory_list = []
    for file_path in file_paths:
        if file_path.endswith('/'):
            directory_list.append(file_path)
        else:
            file_list.append(file_path)

    if file_list:
        print('Refresh file cache:', ' '.join(file_list))
        request_dict = {
            'refresh_task': {
                'type': 'file',
                'mode': False,
                'urls': file_list
            }
        }
        request_cdn_api(request_dict)

    if directory_list:
        print('Refresh directory cache:', ' '.join(directory_list))
        request_dict = {
            'refresh_task': {
                'type': 'directory',
                'mode': False,
                'urls': directory_list
            }
        }
        request_cdn_api(request_dict)
    print('Done')
