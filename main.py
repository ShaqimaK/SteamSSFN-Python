from requests import get

from re import findall, VERBOSE, DOTALL
from winreg import OpenKeyEx, QueryValueEx, HKEY_CURRENT_USER

from time import sleep
from os.path import exists
from os import system, remove
from subprocess import Popen

for _ in range(1145141919810):
    inputStr = input("格式：username----password----ssfnxxxx\n> ").split("----")
    if not len(inputStr) == 3 or not "ssfn" in inputStr[2]: print("————\033[1;31m格式错误！\033[0m")
    else: break

username = "q1611004500"
password = "rinima00"
ssfn = "ssfn895090427336812694"

username, password, ssfn = inputStr
print(f"账号：{username}\n密码：{password}\nssfn凭证：{ssfn}", end="\n"*2)

if __name__ == '__main__':
    for task in ("steam", "csgo"):
        print(f"正在尝试退出 {task}.exe 进程。。。")
        Popen(f'TASKKILL /F /IM {task}.exe')
    sleep(1)
    print("————\033[1;32m四舍五入已退出进程！\033[0m\n")

    # 获取steam文件夹路径
    print("正在尝试获取steam文件夹路径。。。")
    try: steamPath = QueryValueEx(OpenKeyEx(HKEY_CURRENT_USER, r"SOFTWARE\Valve\Steam"), 'SteamPath')[0]
    except:
        print("获取失败，请自行输入steam路径")
        for _ in range(1145141919810):
            steamPath = input("> ")
            if exists(f"{steamPath}\\steam.exe"): break
            else: print("————\033[1;31m错误的路径，请重新输入\033[0m")
    finally: print("————\033[1;32m获取成功！\033[0m\n")

    print("正在获取ssfn凭证文件。。。")
    try: ssfnContent = get(rf'https://ssfnbox.com/download/{ssfn}?sec='+findall(r""".+?\?sec=(.+?)\"""", get(rf"https://ssfnbox.com/download/{ssfn}").text, VERBOSE | DOTALL)[0]).content
    except:
        print("————\033[1;31m获取超时或凭证无效！\033[0m")
        print("正在使用预设常用授权：94")
        ssfnContent = rb'?+\x99$hK\x94!\xa3I\xf6\xcbW\xfe+M\x85ex\x80|\xdf\xeb-[\xd8\xac\xf3Ci\xaek\x15\x9cz\xc1\xa8\x91\xf5\x8bJj=\xcdd\xaf\xfa\xc6\xdf\xdc\xcbg\xf8SR~\x19\xfc*\xaf\x9f\xf5\x0f\xcb\x19\xaf\x9aLt\xdf\xaa\x07\xbd\xf32m[\x8f\x08QF\xa3o\xa8\xfaK\xafP\x1359\xc4%Fe\xcc\xed9\x99\xf1\xb5\xff\xd3\x81\x0eN\xee\xef\xf5\x17\xd2\xf9\x8f\xd9#~\x19\xbe\x06\x14\x9e\x8e\x92\x86~U\x05\xf0\x88\x9aT\xd6O\xed\xbc%jo\x98\x0bM!\xd1\xbc\x87\xe1\x96\x03@yt\x04\xe4\xc9 \xd2\xe7\x8d\x1e\x9f\x16`\xaa\xd1b\x0e\x1e\x81\x1b\x1fa\xfe\xb5e\xbd\xa5\x19U\x0b\xba\x9c\x8f/\xc2\x1a\x9e\x8e\x1a\xaf\x84\xfd\x0c\x1f\xaefnIO\x11\x04\x0b\x8a<^\x94Q\\:\x8a\xaa\x8a\xf3r\xe0~\xb1\xf1q\xfd\xe8\xf0\xd3\x9dA\xcd\xbb\x0f\x84\x96\xec\xee\xd2G[\x9b\xb0\x14v\xc9\xcf\xa2\x13\xd8m\x1f\x11\x00=\xb7kX\x05j\xc4,L&\xa5a\x83\xff+\xbd\xca\x9fI\xeeA\xa6\xc8\xfa\xaf\x8fV\x19w\x06+k\xac\xc6\x8d!\xf2\xe8\x99\x84|e\x84\xd4\xc8\x87s#\xcehP\xcej\x11k\x88\xa2f\x0f\xdb\xf2=\xc3\xb5|\xd9\x0b\x95\x9a\x86\xf5:pW\x1eN\xe1x3\x16\n\xde\xc1\xc7\xc0\x19\xd0\xa5\xea>\xdd\x90\xd9\xc4\'e\xc8U\x19\x80\xf7,\x0f\x15\x17\xeb\xaf\x05(i\xca\x80Q\x9f!\xec\x979\xaeX\xab\x1a\xd5\xdd)X\xc4_NE\x82\xea\x9d,\xb1-\x88w\x10\xc5\xef\xf5\xcd\x17\x93\x93\xc10[\xee)y\x10K\xd4!X\x99~\x8c\xcf\xaa\x03p\xfe\x84u\x93\x05vf;\xf5\x86\x90S<I\x12\xfe\x86\xf6\xc1\x10\x10\xa2\xa5|\xe3\xb1\xb2V\x902-\x94O"H\xa2\xd4]\x82\xd3\xa9\xe6\xa2\xd2\x13\xdd\xc0\x91\xa0\xbe\x9f- \xb7\xeb\x82)\xc7\x80a\x1c\xe4\x154\x0f\xe1~\xdd\x19\x054{\x8c\xd7A&\x8a\xc3\x95\'&\xa0J\x1b\x8c\xce\x96v\xeayJ\xbe\x13m\xb0\x8b\xa1g\x03?{cH\x93\xb8\xa19\tciS,0u=\x9d\n\xf6\x8e\x92<\x119\x16;h\xca_U\x8a\x009Wl\xbe\xa9\xdb`\xe9\x13\xb1\x85jK\xb1`\xfcdTf\x9f\\\xb4\x89D\xa1\xb2K<{\x9f\xba\xee\x14\x0f\xcf*\xa8\x93d\x94\x1fc\xa1\xfc\xc2h\xea$\x1b\xae\xdd\xe5\xe7\x001{\x18ct\xfb\x00z\xbf\xe2?\xa99x\xfb\x11+_\xd0\x9e\xf4\x9c3\x06\xcd\x80\x13\x07"\xb85\x9b*\x96\xb0\x89\x13\x99\xb1\xb0\xdd\xaf\xe3\x9d\xed\xe7Q\xb3F\xa0\rL\x7f\xb31\x9a\xdf\xa3\x1cpQ\r\x97\x0b\x9e\x15\xb3\xcb\xc2\x18\'\xf1Q\x1d\x19\xefBEU\x17\x91\x19\x18\x99\x15+qd\xa4\xd2i\x9aY\xb6?{\xf3C\xa9UY\x05q\xf1\x0c\x96\xdfi\x8e\x1cQ\xeb\xce\xf3\xb3e}J\xfa\x99\xa9\xcf\x97)\x8f\xdd\xe8\x07m\x05\xa3\x15n\xd3<\xff2LpZ@\x81*\xbe\x95\x17y\xbc\xdf\xc6\x89\xe9\xbfW\xe7Y\x8f2\xf3\x06\x15\xa8Sn\x1b\xb0\x0b\xdf\xbc\xda\xa9:2\xf2\xc3\xa6\x83P\xfe\x8cx\xd2Q4\xd4r9\x1a\xcc\x1f\x80A\x01j,\x97\xdc\xd7.>\xc5\xac\xa2\x8e\xe3X\xe6\xe7\xe7\x88;\xeci\xe0\xe94\t!\x81\xb32\x13\x87\xb0w\x91\xe7\xda\xc1P\xf7c\xbe\x88\xc5\xdcSv\x03S\xa3\xfc\xe3\xbeqx\x95\xdd\xafx<BS\x13\x82\xafU\xbcd\x02\xdd(\x144@\xbc\xfd\xcc[\x08\x94\xee\xe8\xcb\xf9\\7\x00\xac`gq\xe4\xbf\x85\xdd|\x931-\x90\x8c\x8e[dmlb)D\x80-\xad\xaf\x97\x02.\xcd\x16\x9cg(5\xdfzD\xdd\xd0\\f\x01\xef\xde\xcb\xec\x01t\x84U\xf1\xeb\xc1\x8cu4\x08\x81<\xc3\t[MFP\x1a\xddL>\xf4\x8e\xb7u/6\xb2a!qRj\x19 \x0c\x88\xf62\xbcNN\xe32md\x01.\xe5_\xed\xf8\xe3\xe1\x8a\x16FY.\x88\x94$\xab5\xce\xc9\xe8Rt\xd4\xe2\xfeM\xf5\x1bO\xd2\x90}D\xdal&\x8ao\xfam+\xd4\xefz8\x84\xfez\ryv\xa9)\r\xc7\xf5k\xeca~\xf0\xb9\xdd\xba\xdf\x85\x89R\x9fE^\xb9`gdp\x85\xc8\x1f\xc51 \xe5\x82\xc0\x1cN(\nC\x97\xba\xfc\x10\xf2?\x10\xd06-\t\x86\xa9\xa8\x83\x06\nu\x12\x00\x80\xcd\xb5\xc0\xf06\xd2\xe9k\x1f(\xe0\xddq\xb7? \xd0n6\xc6\xb6\xb3\xad\x19\xef\x14\xf6I3\x8c\x9b\x1e\xfevg\xb0Ja\xd5\xe9l\x95\xc4-\x12,\xefB\x97\xc4}\xc2\xc1|L&87\xd8]\x0fF\xfa\xc5\x18jd\xe5\x9aJQpU8a,8\xc07w\x0fJ\xc9\xcf\xdc\xdb\x9d\xfa\xe1\x10\x98;,\x8dT8C%5y\xec\xc7\xaf\xee\x95:\xa5\xc0O\xf5\x98\xc7\xf7b\x0c\xe4\xff\x05\xeb\x17hs/\x8f{\xf0\xb7\xb5\xc0\x9e\xd3A\x13.\x94\x9cN\x01~\xd3\xe8{\x1e\x1c\x0b!\xcdhz*\xa5\xd5f*\xa7Bb\x0b\t\xdd\x8a\xfd\xb4\xc7U\xf9+\x83\xcdCL\x1f\xcf\x1b.\xc1"\xa9a\xf8K9.\x89\x17\x8e\xde\xae7r\xc0xg\x8bS\xeas\xe5\xfc\xe8\xbd~\x1c_x\xd955?\xa1f\xc2\xcae\xfb\xf9*n\xfam\xc8E\x03\x13\xc3\x80\xbcVB\xe9\x12%\x90\xcd\x8f0\x97\x13[\xa6~\x9a \x82\xbd\xd5\xe0\xee\x95h?s\xeat\xe5}"\x8a@0g\xd43\x8dS\x0f7\x90\xe3.\xa9\xb9\xd9@\x03\xde\xcd\xbc#8\xbc\xceP7\x85W\xbe\x90\x02\xb5Ja\x94\xfdg\x01\xcd/$\xd8\xcb\x01X\x0f\x91\xd0\x9bEi\xd8{\x0e\x00\xa6\xdf\x03Z;\xaa\xdc\xf6\xa5\x93\xc4\xc0\xb9l\x82\x99\r\x96\x89\xa5\xdd\x0c\xdf\x9fS\xd5\x9b\xa4\xcc\x80\xab\x1f\xff\xac\xd7&\x7f-\xe03\xdc\xa9q\xbe8\xb5\x94wv"\x9e\t\xb1I\x0c4\x07\xa3\x942\xd9\x060E\x9d\xa3s\x9a\x80\x02DM&\xc1\xaf\x92+\xdc\xfc\x12\xac>5H\x89\xd3\xb9\xeaA\xc5?\xad\x89\x84\x1bj\xbe<\r8\x8bX\\\xc9W\xe3\xd1@U)\xc8n\xe6\xf4\xd5xc\t~\xc2\xfe\xce(\xee=\xc8\x05vLB\xab\x0f\xd8\xc6\xc2\x9f\xa7\x8f\xf2\x19\xab\x9et\xb7t\x01\x99@\x0e\xa2\x8dR\xa3\xac\x930\xc3@\xb0\x90\xe2Z\xd4R\x80\xd4s\x1e^P\xe8\xb9\xfb\xc3\xe2\xc7\xb3C\x96"df[\xfb\x96,\xaf/sC\xd2\xfb\xdfFi@\x10\x9d\x83\xc3\xcf\xdd,\xf1[\x96\xd3\xa6\r\xb8\xce[\xffdG\x05Z\x15O\xb5\xf8\xb6\xec\x9b\x168\x97Ke\x0e\x9er\xaa\xcb\xe43\xe2\xb9\x0e^Cs\x93\xf5p\xf0\xe2Iar\xb3\xfb\x9b\x80/rHZ\x86\xc0\xff\xa1\x96\xe3\xc4\x8ch\xa4\xac\xc7\xa1\x1b@\x03\xd6\xa8\x81\xca\xa0\x03\xe8b\xb6\xcf\xfa\t\xa5\xd8WW\xb8\xf0\xdd\xc8*\x8e\x13\xf4\xfd.\xaf\x10\x11n]\x7f\xd1T\x9b\xe7\xf8\xaa\'\x9by\xba\x1b\x99\x01\x11\xc0\xbf7VjAjI\xfe\xf7c\xc4:^\x8ar\x80KW\x97\xdfs\xaf\x01e_Q\x0f\x1a\xac\xd1\xe5\xba\x7fJ\xe8ek\x18\xf7\xb4\x01q9M\xf6\xab\xb9\xf0t\xe9Z\xcfo@\xd1.\x88\x17\xcf\xa1\x95he\xbaz]\xa5\xf2\'(\x88\xa2\xf0|\x99\x13R\\\xfd\xad\xff\xdd\xc3\x8d\xad\n\xbd\xd7\x01\xb7\xec\xebZT|\x99\x7f \xad{\xa6=\xa9\xb0\xd1\x11y\x1c\x1e\xba]\xee\xc5V\x86\x0b6\xdd&C\x07#\xb7\xc9\xd6\xad\xf4 \\2A\xfc_\xb2\x93\x87(\xac\x12\xbb@\x13\r\xaf\xe6\x19\x86\x03\xdf\x00(\xc36\xc0\xa0]\x0e\xa9\xd3\xb7\x12\xe6\xda\xdd\xa1\xd4\xefydAKr\xbca;\xf8&)!j\xea\x00\x8cng\xe4W6\x96&EM\xeb"\x1f3\xe46\xcb,\x87q\x9fdS\x8fW\xaa\x80\xe8~9\x18\xea&m\xe2\x98ro\xfcPZ\xaa\x84\'\x9b\xd1\xc0:B\xffp\x93\xfeD\xbaO\x82\xb0L\x1cf\x8d\x86\x02\xd5E\xfa\xf2#*\x9a\x02\x7f\xd2\x9bm\xb0r_\x11\xe93\x81\x9e{q\xe6/\x8b\x9a\x05\xa4\x80\x98\xa0\xab:\xcb\xf2\x8a\xdcz\x81Oh\xba\xbd\xb7FJ\x88\x95\xf1\x02\xcb\xde\xb0\xe2?\x98\xddY\xcc\xd0=\x8e\x02\xc5\x88\x8bW\x17\x86X\xe6\xc3\xe5\xf0\xc9h\xac\x87\x99\xa2.,\x86:\x96\xfb\x7f'
    else: print("————\033[1;32m获取成功！\033[0m\n")

    print("正在建立ssfn凭证档案。。。")
    if exists(f"{steamPath}\\{ssfn}"): remove(f"{steamPath}\\{ssfn}")
    with open(f"{steamPath}\\{ssfn}", "wb") as ssfnFile: ssfnFile.write(ssfnContent)
    print("————\033[1;32m建立成功！\033[0m\n")

    print("正在自动登入steam。。。")
    Popen(f"{steamPath}\\steam.exe -noreactlogin -login {username} {password}")
    print("————\033[1;32m自动登入成功？\033[0m\n")

    system("pause")