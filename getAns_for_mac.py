import requests, time, sys, getopt, random, re, warnings, urllib3
from colorama import Fore

def main(argv):
   try:
       opts, args = getopt.getopt(argv,"-h-i-u:-l:",["help","url=","list=","ip"])
   except getopt.GetoptError:
      log()
      command()
      sys.exit(2)
   for opt, arg in opts:
       if opt in ("-h","--help"):
           log()
           command()
           sys.exit()
       if opt in ("-u", "--url"):
           check(arg)
           domain(arg)
           sys.exit()
       if opt in ("-l", "--list"):
           liet(arg)
           sys.exit()
       if opt in ("-i", "--ip"):
           Public_IP()
           sys.exit()

def Public_IP():
    try:
        agent = user_agernt()
        head = {
            "User-Agent": random.choice(agent),
            "Connection": "close",
        }
        urllib3.disable_warnings()
        warnings.filterwarnings("ignore")
        manages = "https://2022.ip138.com"
        resultss = requests.get(manages, headers=head, verify=False, timeout=20)
        resultss.encoding = 'utf-8'
        ips = re.findall(r"<title>(.*?)</title>", resultss.text, re.S)
        ans = re.findall(r"来自：(.*?)\n</p>", resultss.text, re.S)
        results = str(ips) + " 归属地" + str(ans)
        print(highlight(str(results)))
    except Exception as e:
        print("报错可能是请求过快，或者域名更换等原因。错误为:"+str(e))

def check(target):
    agent = user_agernt()
    head = {
        "User-Agent": random.choice(agent),
        "Connection": "close",
    }

    try:
        merge = f'https://ip138.com/iplookup.asp?ip={target}&action=2'
        results = requests.get(merge, headers=head, timeout=30)
        results.encoding = 'gb2312'
        res = re.findall(r'ip_result = \{(.*?), "', results.text)
        resultss = "[+]" + target + " " + str(res[0])
        print(highlight(resultss))
    except Exception as e:
        print("报错啦！网络延迟+请求频率=返回速度。错误为："+str(e))

def liet(file):
    with open(file, 'r+') as files:
        for i in files.readlines():
            r = i.strip("\n")
            check(r)
            domain(r)
            print("==============分隔符(域名反查默认输出前三个想看更多访问https://site.ip138.com/）==============")
            time.sleep(0.5)

def domain(targtes):
    agent = user_agernt()
    head = {
        "User-Agent": random.choice(agent),
        "Connection": "close",
    }

    try:
        merge = f'https://site.ip138.com/{targtes}/'
        results = requests.get(merge, headers=head, timeout=30).text
        ips = re.findall(r'class="name"><strong>(.*?)</strong>,', results, re.S)
        ipts = re.findall(r'</span><a href=".*?" target="_blank">(.*?)</a></li>', results, re.S)
        ert = ips + ipts
        do = "绑定过的域名如下:"
        results = str(ert[0:3])
        print(Fore.CYAN+do)
        print(highlight(results))
    except Exception as e:
        print("报错啦！网络决定返回速度。错误为："+str(e))

def highlight(bright):
    return Fore.GREEN+bright

def user_agernt():
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
    return user_agent_list

def weibu(target):
    agent = user_agernt()
    head = {
        "User-Agent": random.choice(agent),
        "Connection": "close",
    }

    try:
        merge = f'https://ip138.com/iplookup.asp?ip={target}&action=2'
        results = requests.get(merge, headers=head, timeout=30)
        results.encoding = 'gb2312'
        res = re.findall(r'ip_result = \{(.*?), "', results.text)
        resultss = "[+]" + target + " " + str(res[0])
        print(highlight(resultss))
    except Exception as e:
        print("报错啦！网络延迟+请求频率=返回速度。错误为："+str(e))

def log():
    logs =\
        """
                           _
                           \\"-._ _.--"~~"--._
                            \   "            ^.    ___
                            /                  \.-~_.-~
                     .-----'     /\/"\ /~-._      /
                    /  __      _/\-.__\L_.-/\     "-.
                   /.-"  \    ( ` \_o>"<o_/  \  .--._\\
                  /'      \    \:     "     :/_/     "`
                          /  /\ "\    ~    /~"
                          \ I  \/]"-._ _.-"[
                       ___ \|___/ ./    l   \___   ___
                  .--v~   "v` ( `-.__   __.-' ) ~v"   ~v--.
               .-{   |     :   \_    "~"    _/   :     |   }-.
              /   \  |           ~-.,___,.-~           |  /   \\
             ]     \ |                                 | /     [
             /\     \|     :                     :     |/     /\\
            /  ^._  _K.___,^                     ^.___,K_  _.^  \\
           /   /  "~/  "\                           /"  \~"  \   \\
          /   /    /     \ _          :          _ /     \    \   \\
        .^--./    /       Y___________l___________Y       \    \.--^.
        [    \   /        |        [/    ]        |        \   /    ]
        |     "v"         l________[____/]________j  -Sec   }r"     /
        }------t          /                       \       /`-.     /
        |      |         Y                         Y     /    "-._/
        }-----v'         |         :               |     7-.     /
        |   |_|          |         l               |    / . "-._/
        l  .[_]          :          \              :  r[]/_.  /
         \_____]                     "--.             "-.____/
                                            "Xforsec.com"
                                                        ---light
        """
    print(logs)

def command():
    commands = \
        '''
    getAsn.py -u <220.181.38.251> 单个ip反查
    getAsn.py -l <list.txt>       批量请求
    getAsn.py -i                  本机公网ip
        '''
    print(commands)

if __name__ == '__main__':
    main(sys.argv[1:])

