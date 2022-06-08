import requests, time, sys, getopt, random, json, re

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"u:l:",["url=","list="])
   except getopt.GetoptError:
      print ("getAsn.py -u <220.181.38.251>\ngetAsn.py -l <list.txt>")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print ("getAsn.py -u <220.181.38.251>\ngetAsn.py -l <list.txt>")
         sys.exit()
      elif opt in ("-u", "--url"):
          check(arg)
          domain(arg)
      elif opt in ("-l", "--list"):
          liet(arg)


def check(target):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
    head = {
        "User-Agent": random.choice(user_agent_list),
        "Connection": "close",
    }

    try:
        merge = f'http://api.webscan.cc/?action=getip&domain={target}'
        results = requests.get(merge, headers=head, timeout=30).text
        time.sleep(0.5)
        print(results.encode('utf8').decode('unicode_escape'))
        # resullts = results.encode('utf8').decode('unicode_escape')    #去除花括号
        # res = re.findall(r'\{(.*?)\}', resullts, re.S)
        # print(res[0])
    except Exception as e:
        print(e)

def liet(file):
    with open(file, 'r+') as files:
        for i in files.readlines():
            r = i.strip("\n")
            check(r)
            domain(r)
            print("==============分隔符(域名反查默认输出前两个，看更多访问webscan.cc）==============")

def domain(targtes):
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        ]
    head = {
        "User-Agent": random.choice(user_agent_list),
        "Connection": "close",
    }

    try:
        merge = f'http://api.webscan.cc/?action=query&ip={targtes}'
        results = requests.get(merge, headers=head, timeout=30, verify=False).text
        jsons = results.encode('utf8').decode('unicode_escape')
        res = re.findall(r'\{(.*?)\},', jsons, re.S)
        for i in res[0:2]:
            print(i)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main(sys.argv[1:])

