import paramiko

ip = input('What is your ec2 instance address? ')
port = 22
username = 'ec2-user'
key = paramiko.RSAKey.from_private_key_file(input("What is the path to your private key? "))
check = 'nc -zv 169.254.169.254 80'
response = 'sudo iptables -I OUTPUT -d 169.254.169.254 -p tcp --dport 80 -j REJECT'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,pkey=key)

def sshthing():
    stdin,stdout,stderr = ssh.exec_command(check)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    return resp
def sshthing2():
    stdin,stdout,stder = ssh.exec_command(response)
    outlines = stdout.readlines()
    resp = ''.join(outlines)
    return resp
if 'succeeded' in sshthing():
    sshthing2()
else:
    print("Metadata Secure!")

# Secures ec2 Metadata