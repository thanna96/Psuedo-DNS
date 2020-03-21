
# coding: utf-8

# In[1]:


#Thomas Hanna Comp 352 
#Phase 3 - Client Program 
#1- Connects to AS, sends challengs and digest to AS, recieves hostname.
#2- Connects to TLDS, sends query, recieves the A record.
#Expands on Phase 2

#Imports:
import socket
import hmac

#Port Number Variables:
portc = 9706
portas = 9716
porttlds1 = 9727
porttlds2 = 9737

end = "endconnection"

#File Read for HNS File with Key, Challenge, and Hostname:
def readFile():
    hns_output = []
    f = open("PROJ3-HNS.txt", "r")
    for line in f:
        splits = line.split()
        hns_output.append([splits[0],splits[1], splits[2]])
    return hns_output
  
#Client Program - Connects to AS, Sends Challenge + Digest, Recieves Name of Server from AS,
#Then Connects to Appropriate Server, Sends Hostname, Recieves DNS entry
#Then Outputs the Received String and Hostname into a Text File - RESOLVED.TXT:
def start_client(hns_entries):
    print("DNS Entries on client are:", hns_entries)
    print("Client started, sending message to AS Server ...")
    #Get Server information and connect to AS
    try:
        _as = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #local_name = socket.gethostname()
        as_ip = (socket.gethostbyname(cd.cs.rutgers.edu))
        _as.connect((as_ip, portas))
    except socket.error:
        print(socket.error)
    TLDS1 = None
    TLDS2 = None
    
    f = open("RESOLVED.txt", "w")
    for i in hns_entries:
        digest = hmac.new(i[0].encode(),i[1].encode("utf-8"))
        as_string = i[1] + " " + digest.hexdigest()
        #Sends Digest and challenge string to AS
        _as.send(as_string.encode('utf-8'))
        #Recieves Correct TLDS from AS
        server_name = _as.recv(100).decode('utf-8')
        try:
            if TLDS1 == None:
                TLDS1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #local_name = socket.gethostname()
                TLDS1_ip = (socket.gethostbyname(cpp.cs.rutgers.edu))
                TLDS1.connect((TLDS1_ip, porttlds1))
        except socket.error:
            print(socket.error)
        try:
            if TLDS2 == None:
                TLDS2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #local_name = socket.gethostname()
                TLDS2_ip = (socket.gethostbyname(java.cs.rutgers.edu))
                TLDS2.connect((TLDS2_ip, porttlds2))
        except socket.error:
            print(socket.error)
            
        if (server_name == 'TLDS1'):
            print("Server for this Host is: " + server_name)
            TLDS1.send(i[2].encode('utf-8'))
            TLDS2.send(" ".encode('utf-8'))
            result = TLDS1.recv(100).decode('utf-8')
            print("DNS Entry from TLDS1:" + result)
            
        if(server_name == 'TLDS2'):
            print("Server for this Host is: " + server_name)
            TLDS2.send(i[2].encode('utf-8'))
            TLDS1.send(" ".encode('utf-8'))
            result = TLDS2.recv(100).decode('utf-8')
            print("DNS Entry from TLDS2:" + result)
        f.write(result+"\n")

    _as.send(end.encode('utf-8'))
    _as.close()

    exit()

#Main Function
if __name__ == '__main__':
    hns_entries = readFile()
    start_client(hns_entries)


