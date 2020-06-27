from django.http import HttpResponse
from django.template import loader
import psutil
import getpass
import telnetlib
import paramiko
import os
from os import listdir
from os.path import isfile, join
from paramiko import SSHClient
from scp import SCPClient

from exerciseone.models import Router


def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('exercisetwo/index.html')
    context = {
        # 'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def diskusage(request):
    data = psutil.disk_usage('/')
    result = "Total: " + str(data[0]) + "<br/> Free: " + str(data[2]) + "<br/> Used: " + str(
        data[1]) + "<br/> Percentage: " + str(data[3])
    return HttpResponse(result)


def telnet(request):
    HOST = "localhost"
    user = input("Enter your remote account: ")
    password = getpass.getpass()

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    tn.write(b"ls\n")
    tn.write(b"exit\n")

    return HttpResponse(tn.read_all().decode('ascii'))


def ssh(request):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect('192.168.1.1', username='user', password='password')
    stdin, stdout, stderr = client.exec_command('cat /proc/meminfo')
    result = ''
    for line in stdout:
        result += '... ' + line.strip('\n')
    client.close()
    return HttpResponse(result)


def inode(request):
    # Directory to be scanned
    path = os.getcwd()
    result = 'Directory entry name and their inode number'
    with os.scandir(path) as itr:
        for entry in itr:
            if not entry.name.startswith('.'):
                result += "<br/>" + str(entry.name) + " :" + str(entry.inode())
    return HttpResponse(result)


def filespath(request):
    onlyfiles = [f + "<br/>" for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    return HttpResponse(onlyfiles)


def copyfileremote(request):
    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect('root@root:localhost')
    with SCPClient(ssh.get_transport()) as scp:
        scp.put('my_file.txt', 'my_file.txt')  # Copy my_file.txt to the server
    return HttpResponse("Copied Successfully!")


def autorestartapache(request):
    result = '''<pre>for I in 0 1 2 3 4 5; do
    check=$(uptime | tr -d ',.' | awk '{print $10}')
    if [ "$check" -gt 5 ]; then
        /usr/bin/systemctl restart httpd.service
    fi
    sleep 10
    done
    Setup an cron for runing always for this file

    * * * * * /PATH/TO/YOUR/SCRIPT
    </pre>'''
    return HttpResponse(result)


def newview(request):
    return HttpResponse("A new view")


def generatedataten(request):
    for x in range(11):
        router = Router.objects.create(sapid="sap:1/2/3:801" + str(x+2), hostname="hostname",
                                       loopback="127.0.0." + str(x+2), macaddress="11:22:33:aa:bb:cc")

        router.save()
    return HttpResponse('''Inserted click to check <a href='/show/'>show inserted value</a>''')


def monitorserver(request):
    result = '''<pre>
    1. we can always check disk usage of server
    2. we can monitor server logs
    3. for troubleshooting also we can check logs restart the server if needed and check how many processes are running on that
    4. for process check gdb -p 20788
    5. discover usage echo [PID]  [MEM]  [PATH] &&  ps aux | awk '{print $2, $4, $11}' | sort -k2rn | head -n 20 ps -eo pcpu,pid,user,args | sort -k 1 -r | head -20
    </pre>'''
    return HttpResponse(result)


def telnetcreate(request):
    result = '''<pre>With the help of telnet and scp we can upload file to the server
    and we can use unzip myzip.zip
    or 
    tar xvf filename.tar
    for number of files we can make a loop on that via file names
    </pre>'''
    return HttpResponse(result)
