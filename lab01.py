import requests  # εισαγωγή της βιβλιοθήκης


def more(text):
    count = 0
    for line in text.split('\n'):
        print(line)
        count += 1
        if count % 30 == 0:
            reply = input('Show more (y/n)? ')
            if reply == 'n':
                break


url = input('Enter URL:')  # προσδιορισμός του url

with requests.get(url) as response:  # το αντικείμενο response
    html = response.text
    # more(html)
    headers = response.headers
    print('Headers:\n', headers)
    print('Server:\n' + headers['Server'])
    if "set-cookie" in headers.keys():
        cookies = response.cookies
        for cookie in cookies:
            print(f"\nThe site uses cookie.\nName: {cookie.name}\nValue: {cookie.value}\nExpiration Date: {datetime.datetime.fromtimestamp(float(cookie.expires)) if cookie.expires is not None else 'Does Not Expire'}")        
    else:
        print('\nThe site does not use cookies')
