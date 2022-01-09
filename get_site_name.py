import re

pattern=r"(^[\d.]+).*\[([(\d)/\w:\s+]+)\].*HTTP/1.1\".(\d{3}).(\d*).\"([\w://.-]+)"
result={}
with open('examplelogs') as file:
    for line in file:
        search=re.match(pattern,line)
        if search[3] == '200':
            if search[1] not in result:
                result[search[1]]=set()
            result[search[1]].add(search[5])


print(result)
#{'83.149.9.216': {'http://semicomplete.com/presentations/logstash-monitorama-2013/', 'http://google.com/'}, 
  '83.149.9.200': {'http://google.com/'}}
