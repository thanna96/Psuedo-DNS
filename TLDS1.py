
# coding: utf-8

# In[1]:


#Thomas Hanna Comp 352 
#Phase 3 - TLDS1 Program - Recieves Challenge from AS, Returns Digest
#Recieves Hostname from Client, Returns DNS Entry
#Expands on Phase 2

#Imports:
import socket
import hmac

#Port Variable:
portc = 7706
portas = 7716
port = 7726
port2 = 7727

#Read File and Fill DNS Table Array
def readFile():
    dns_output = []
    host_name = ""
    f = open("PROJ3-TLDS1.txt","r")
    f2 = open("PROJ3-KEY1.txt", "r")
    for line in f:
        splits = line.split()
        if splits[2] == "NS":
            host_name = [splits[0], splits[1], splits[2]]
        else:
            dns_output.append([splits[0],splits[1], splits[2]])
    key = f2.readline()
    return dns_output,host_name,key

#Returns DNS Entry if Hostname is in DNS else Returns Error
def get_dns(input_client, dns_entries, host_name):
    for i in dns_entries:
        if i[0] == input_client.strip():
            return i[0] + " " + i[1] + " " + i[2]
    return "Hostname - Error:HOST NOT FOUND"

#Starts Server connection to AS - Revieves Challenge, then sends AS the Digest
#Recieves hostname from client then sends DNS entry
def startServer(dns_entries, host_name,key):
    print("DNS Entries on TLDS1 are:", dns_entries, host_name)
    s = None
    s2 = None
    
    while True:

        if s == None:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket.error:
                print(socket.error)
            s.bind(('', port))
            s.listen(1)
            local_name = socket.gethostname()
            local_ip = (socket.gethostbyname(local_name))
            conn, as_ip = s.accept()
            
        input_as = conn.recv(100).decode('utf-8')

        if (input_as == "endconnection"):
            s.close()
            exit()
        digest = hmac.new(key.strip().encode(),input_as.encode("utf-8"))
        print("Sending digest to the client(AS):" + digest.hexdigest())
        conn.send(digest.hexdigest().encode('utf-8'))
        
        if s2==None:
            try:
                s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except socket.error:
                print(socket.error)
            s2.bind(('', port2))
            s2.listen(2)
            local_name = socket.gethostname()
            local_ip = (socket.gethostbyname(local_name))
            conn2, client_ip = s2.accept()
    
        input_client = conn2.recv(100).decode('utf-8')
        if (input_client == "endconnection"):
            s2.close()
            exit()
        if(input_client != " "):
            result = get_dns(input_client, dns_entries, host_name)
            print("Sending to the client:" + result)
            conn2.send(result.encode('utf-8'))
        

    
if __name__ == '__main__':
    dns_entries, host_name, key = readFile()
    startServer(dns_entries, host_name,key)



