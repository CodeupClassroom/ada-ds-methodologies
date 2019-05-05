
## Exercises



```python
import re
from pprint import pprint
```



Write a function named `is_vowel`. It should accept a string as input and use a regular expression to determine if the passed string is a vowel. While not explicity mentioned in the lesson, you can treat the result of `re.search` as a boolean value that indicates whether or not the regular expression matches the given string.



```python
def is_vowel(c):
    return re.search(r'[aeiou]', c)
```



Write a function named `is_valid_username` that accepts a string as input. A valid username starts with a lowercase letter, and only consists of lowercase letters, numbers, or the `_` character. It should also be no longer than 32 characters. The function should return either `True` or `False` depending on whether the passed string is a valid username.

        >>> is_valid_username('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        False
        >>> is_valid_username('codeup')
        True
        >>> is_valid_username('Codeup')
        False
        >>> is_valid_username('codeup123')
        True
        >>> is_valid_username('1codeup')
        False



```python
def is_valid_username(username):
    return re.search(r'^[a-z][a-z0-9_]{0,31}$', username) is not None

usernames = [
    'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
    'codeup',
    'Codeup',
    'codeup123',
    '1codeup',
]

for username in usernames:
    print('username: {} -- is_valid: {}'.format(username, is_valid_username(username)))
```

```
username: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa -- is_valid: False
username: codeup -- is_valid: True
username: Codeup -- is_valid: False
username: codeup123 -- is_valid: True
username: 1codeup -- is_valid: False
```



Write a regular expression to capture phone numbers. It should match all of the following:

        (210) 867 5309
        +1 210.867.5309
        867-5309
        210-867-5309



```python
phone_numbers = [
    '(210) 867 5309',
    '+1 210.867.5309',
    '867-5309',
    '210-867-5309',
]

regexp = re.compile(r'''
^
(?P<calling_code>\+\d+)?
[^\d]*?
(?P<area_code>\d{3})?
[^\d]*?
(?P<first_three>\d{3})
[^\d]*?
(?P<last_four>\d{4})
$
''', re.VERBOSE)

for number in phone_numbers:
    print(number)
    pprint(regexp.match(number).groupdict())
    print('---')
```

```
(210) 867 5309
{'area_code': '210',
 'calling_code': None,
 'first_three': '867',
 'last_four': '5309'}
---
+1 210.867.5309
{'area_code': '210',
 'calling_code': '+1',
 'first_three': '867',
 'last_four': '5309'}
---
867-5309
{'area_code': None,
 'calling_code': None,
 'first_three': '867',
 'last_four': '5309'}
---
210-867-5309
{'area_code': '210',
 'calling_code': None,
 'first_three': '867',
 'last_four': '5309'}
---
```



Use regular expressions to convert the dates below to the standardized year-month-day format.

        02/04/19
        02/05/19
        02/06/19
        02/07/19
        02/08/19
        02/09/19
        02/10/19



```python
dates = '''
02/04/19
02/05/19
02/06/19
02/07/19
02/08/19
02/09/19
02/10/19
'''.strip().split('\n')

for date in dates:
    # for simplicity, we'll assume all the dates are are in the 21st century
    standardized = re.sub(r'(\d+)/(\d+)/(\d+)', r'20\3-\1-\2', date)
    print('{} -> {}'.format(date, standardized))
```

```
02/04/19 -> 2019-02-04
02/05/19 -> 2019-02-05
02/06/19 -> 2019-02-06
02/07/19 -> 2019-02-07
02/08/19 -> 2019-02-08
02/09/19 -> 2019-02-09
02/10/19 -> 2019-02-10
```

Write a regex to extract the various parts of these logfile lines:

        GET /api/v1/sales?page=86 [16/Apr/2019:193452+0000] HTTP/1.1 {200} 510348 "python-requests/2.21.0" 97.105.19.58
        POST /users_accounts/file-upload [16/Apr/2019:193452+0000] HTTP/1.1 {201} 42 "User-Agent: Mozilla/5.0 (X11; Fedora; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" 97.105.19.58
        GET /api/v1/items?page=3 [16/Apr/2019:193453+0000] HTTP/1.1 {429} 3561 "python-requests/2.21.0" 97.105.19.58

```python
log_lines = '''
GET /api/v1/sales?page=86 [16/Apr/2019:193452+0000] HTTP/1.1 {200} 510348 "python-requests/2.21.0" 97.105.19.58
POST /users_accounts/file-upload [16/Apr/2019:193452+0000] HTTP/1.1 {201} 42 "User-Agent: Mozilla/5.0 (X11; Fedora; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36" 97.105.19.58
GET /api/v1/items?page=3 [16/Apr/2019:193453+0000] HTTP/1.1 {429} 3561 "python-requests/2.21.0" 97.105.19.58
'''.strip().split('\n')

regex = re.compile(r'''
(?P<method>POST|GET)
\s*
(?P<path>(?:[/\w-]+))
(?:\?(?P<query_string>.*?)\s)?
\s*\[
(?P<day>\d+)/(?P<month>\w+)/(?P<year>\d+):
(?P<hour>\d{2})(?P<minute>\d{2})(?P<second>\d{2})
(?P<timezone>\+\d{4})
\]\s+
(?P<protocol>HTTPS?/\d\.\d)
\s+
\{(?P<status>\d+)\}
\s+
(?P<bytes_sent>\d+)
\s+
"(?P<user_agent>.*)"
\s+
(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})
''', re.VERBOSE)

for line in log_lines:
    pprint(regex.match(line).groupdict())
```

    {'bytes_sent': '510348',
     'day': '16',
     'hour': '19',
     'ip': '97.105.19.58',
     'method': 'GET',
     'minute': '34',
     'month': 'Apr',
     'path': '/api/v1/sales',
     'protocol': 'HTTP/1.1',
     'query_string': 'page=86',
     'second': '52',
     'status': '200',
     'timezone': '+0000',
     'user_agent': 'python-requests/2.21.0',
     'year': '2019'}
    {'bytes_sent': '42',
     'day': '16',
     'hour': '19',
     'ip': '97.105.19.58',
     'method': 'POST',
     'minute': '34',
     'month': 'Apr',
     'path': '/users_accounts/file-upload',
     'protocol': 'HTTP/1.1',
     'query_string': None,
     'second': '52',
     'status': '201',
     'timezone': '+0000',
     'user_agent': 'User-Agent: Mozilla/5.0 (X11; Fedora; Fedora; Linux x86_64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 '
                   'Safari/537.36',
     'year': '2019'}
    {'bytes_sent': '3561',
     'day': '16',
     'hour': '19',
     'ip': '97.105.19.58',
     'method': 'GET',
     'minute': '34',
     'month': 'Apr',
     'path': '/api/v1/items',
     'protocol': 'HTTP/1.1',
     'query_string': 'page=3',
     'second': '53',
     'status': '429',
     'timezone': '+0000',
     'user_agent': 'python-requests/2.21.0',
     'year': '2019'}


You can find a list of words on your mac at `/usr/share/dict/words`. Use this file to answer the following questions:

```python
with open('/usr/share/dict/words') as f:
    words = f.read()

# How many words have at least 3 vowels?
len(re.findall(r'^.*[aeiou].*[aeiou].*[aeiou]$', words, re.MULTILINE))
```

    55184

```python
# How many words have at least 3 vowels in a row?
len(re.findall(r'^.*[aeiou]{3,}.*$', words, re.MULTILINE))
```

    6156

```python
# How many words have at least 4 consonants in a row?
len(re.findall(r'^.*[^aeiou]{4,}.*$', words, re.MULTILINE))
```

    62922

```python
# How many words start and end with the same letter?
len(re.findall(r'(^(.).*\2$)', words, re.MULTILINE))
```

    9917

```python
# How many words start and end with a vowel?
len(re.findall(r'(^[aeiou].*[aeiou]$)', words, re.MULTILINE))
```

    12351

```python
# How many words contain the same letter 3 times in a row?
len(re.findall(r'(^.*(.)\2{2}.*$)', words, re.MULTILINE))
```

    7
