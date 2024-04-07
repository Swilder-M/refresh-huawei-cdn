# refresh-huawei-cdn

## Usage
```yaml
    - name: refresh cdn cache
      uses: Swilder-M/refresh-huawei-cdn@master
      with:
        access_key_id: ${{ secrets.HUAWEI_ACCESS_KEY_ID }}
        access_key_secret: ${{ secrets.HUAWEI_ACCESS_KEY_SECRET }}
        file_paths:
          https://example.com/path/
          https://example.com/path/test.html
```
