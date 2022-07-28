# getAns
简介：<br>
由于作者比较懒，于是它就诞生了，脚本可用于ip反查归属地+域名+可批量+查询本机公网ip,护网查归属溯源日常专用<br>
师傅们多多start呀🥳

# 环境
Python3<br>
初次启动安装依赖:<br>
python3 -m pip install -r lib.txt<br>

# 帮助<br>
python3 getAns.py -h <br>
python3 getAsn.py -u <220.181.38.251> 单个ip反查<br>
python3 getAsn.py -l <list.txt>&nbsp;&nbsp;批量查询，一行一个<br>
python3 getAsn.py -i&nbsp;&nbsp;&nbsp;&nbsp;本机公网ip<br>

# 单个ip<br>
python3 getAns.py -u 220.181.38.251 <br>

# 批量<br>
python3 getAns.py -l list.txt <br>

# 本机公网ip<br>
python3 getAns.py -i <br>

# 说明：
windows下暂时没有解决高亮输出<br>
mac下可以高亮输出<br>

# 待完成功能：
微步输出[]<br>
多线程批量请求[]<br>
通过域名反查企业[]<br>

注：请不要将该脚本用于非法用途，由于使用工具带来的不良后果与本人无关。
