
# coding: utf-8

# In[1]:


#Thomas Hanna Comp 352 
#Phase 3 - AS Program - Recieves Challenge and Digest from Client, Sends Challenge to TLDS 
#Then Compares the Digest and Sends the Name of the Server to Client if it's a Match.
#Expands on Phase 2

#Imports:
import socket
import hmac

#Port Variables:
port = 9716
porttlds1 = 9726
porttlds2 = 9736

end = "endconnection"

#AS Function - 
def startServer():
    print("Server AS started, waiting for Client...")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error:
        print(socket.error)
    s.bind(('', port))
    s.listen(1)
    local_name = socket.gethostname()
    local_ip = (socket.gethostbyname(local_name))
    conn, client_ip = s.accept()
    TLDS1 = None
    TLDS2 = None

    while True:
        input_client = conn.recv(100).decode('utf-8')
        if (input_client == "endconnection"):
            TLDS1.send(result.encode('utf-8'))
            TLDS2.send(result.encode('utf-8'))
            s.close()
            exit()
        inputSplit = input_client.split()

        if TLDS1 == None:
            try:
                TLDS1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #local_name = socket.gethostname()
                TLDS1_ip = (socket.gethostbyname(cpp.cs.rutgers.edu))
                TLDS1.connect((TLDS1_ip, porttlds1))
            except socket.error:
                print(socket.error)
        TLDS1.send(inputSplit[0].encode('utf-8'))
        digest = TLDS1.recv(100).decode('utf-8')
        print(digest," ", inputSplit[1])
        if digest == inputSplit[1]:
            result = 'TLDS1'
            print("sending result: ", result)
            conn.send(result.encode('utf-8'))
        
        if TLDS2 == None:
            try:
                TLDS2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #local_name = socket.gethostname()
                TLDS2_ip = (socket.gethostbyname(java.cs.rutgers.edu))
                TLDS2.connect((TLDS2_ip, porttlds2))
            except socket.error:
                print(socket.error)
        TLDS2.send(inputSplit[0].encode('utf-8'))
        digest2 = TLDS2.recv(100).decode('utf-8')
        print(digest2," ", inputSplit[1])
        if digest2 == inputSplit[1]:
            result = 'TLDS2'
            print("sending result: ", result)
            conn.send(result.encode('utf-8'))   
#Main Function
if __name__ == '__main__':  
    startServer()


