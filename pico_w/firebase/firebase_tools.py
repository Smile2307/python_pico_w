import network,json,time,utime,rp2
from machine import WDT

rp2.country('TW')

#ssid = 'Smile309'
#password = '0939763309b' 

ssid = 'Smilewireless'
password = '0939763309'

#ssid = 'robertHome'
#password = '0926656000'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)
wlan.config(pm = 0xa11140)

def connect():  

    #等待連線或失敗
    #status=0,1,2正在連線
    #status=3連線成功
    #<1,>=3失敗的連線
    max_wait = 10    

    while max_wait > 0:
        status = wlan.status()
        if status < 0 or status >= 3:
            break
        max_wait -= 1
        print("等待連線")
        time.sleep(1)

    #處理錯誤
    if wlan.status() != 3:
        print('連線失敗,重新開機')
        raise RuntimeError('連線失敗')
        #實際商品化後，須重新開機時，才使用
        #wdt = WDT(timeout=2000)
        #wdt.feed()
    else:
        print('連線成功')
        status = wlan.ifconfig()
        print(f'ip={status[0]}') 
        
        
def reconnect():
    if wlan.status() == 3: #還在連線,只是傳送的server無回應
        print(f"無法連線({wlan.status()})")
        return
    else:
        print("嘗試重新連線")
        wlan.disconnect()
        wlan.connect(ssid, password)
        connect()          

def request_upgrade(self):
    '''!Check if an upgrade is available for this module. Due to the nature of OTA upgrades, this method cannot return any status. 
    If you call this method, then you will have to wait till the upgrade completes, without calling any further commands. 
    If there is an upgrade, then the LED on the WiNoT&reg; module blinks rapidly to show that the upgrade is in progress. 
    After the upgrade is completed, the LED blinks slowly (with a gap of 500 milliseconds) for 3 times and the module restarts. 
    If there is no upgrade, then nothing happens. 

    When performing an upgrade, make sure that your pico is connected to an uninterrupted power source. 
    If there is a power outage during the upgrade process,then the WiNoT module could get into an unrecoverable state. 
    '''
    upgradeJson = { "CMD" : "Upgrade"}
    self.__send_uart(upgradeJson, False)
    
def setdb_to_firebase(self, host, auth, tree=""):
    '''!Set Firebase as the platform to be used for communication. 
     
     @param host - Name of the host parameter. This is the host by Firebase. For example in firebase it could be "https://projectbasedname.firebaseio.com"
     @param auth - Auth token - The auth token for this database
     @param tree - Optional name of a directory or tree. 
     When we write any values to firebase, these updates will be made under this tree.  
     Likewise when we read values from firebase, they will be read from keys which are under this tree. 
     If this value is not provided or provided as an empty string, then values are written to and read from the root folder. 

     return An integer indicating whether there was an error or not. If value is zero, then it means that the call succeeded. 
     If one or more of the parameters are incorrect, if we are not able to establish an network connection to the DB server, then ERR_PLATFORMNOTSET is returned. 
    '''
    sJson = self.__getCmdJson("SetPlatform")
    dJson = sJson["Data"]
    dJson["Platform"] = "Firebase"
    dJson["Host"] = host
    dJson["Auth"] = auth
    if (tree != ""):
        dJson["Tree"] = tree
    response = self.__send_uart(sJson)
    if response['Code'] == 200 :
        self.__is_plat_set = True
    
def set_value(self, key, value):
    '''!Set value for a given key. 
    @param key - The db key into which the value must be inserted. The key MUST be a String 
    @param value - The value which has to be inserted. The value can be of any basic data type like integer, decimal, boolean or String
    @return An integer indicating whether there was an error or not. If all parameters are in order then 202 is returned. 
    If there is an error in this, or we could not connect to the firebase database, then ERR_DBSET_ERROR is returned. 
     
    If you want to check if that the value was indeed set in the database, then  will need to call the read_value(...) method..
    '''
    if not self.__is_plat_set:            
        raise(Exception("Platform not yet set!"))
    cmdType = ""
    abort = False
    if (isinstance(value, int )) :
        cmdType = "SetInt"
    elif (isinstance(value, float)) :
        cmdType = "SetFloat"
    elif (isinstance(value, bool )):
        cmdType = "SetBoolean"
    elif (isinstance(value, str)) :
        cmdType = "SetString"
    else :
        print("Unsupported data type - {}".format(type(value)))
        abort = True
    if not abort : 
        sJson = self.__getCmdJson(cmdType)
        dJson = sJson["Data"]
        dJson["Key"] = key
        dJson["Value"] = value            
        self.__send_uart(sJson)
    
    
def get_value(self, key, keytype=None):
    '''!Get the value for *key* from the cloud database. The received value's type depends on the type in the cloud database
     
     @param key  The key in the cloud database for which we want the value
     @return The value in the cloud database for the given key. 
     @exception KeyError if there is no entry for the said key in the remote database.
    '''
    if keytype==str:
        keytype="ReadString"
    else:
        keytype="ReadAny"
    sJson = self.__getCmdJson(keytype)
    dJson = sJson["Data"]        
    dJson["Key"] = key
    response = self.__send_uart(sJson)
    if not "Value" in response:
        raise KeyError("Value key not found in {}".format(response))
    return response["Value"]


def delete_key(self, key):
    '''!Delete the passed *key* from the cloud database 
    @param key The key in the cloud database which has to be deleted
    @return an integer code representing whether the operation suceeded or not. 
    '''
    sJson = self.__getCmdJson("Delete")
    dJson = sJson["Data"]        
    dJson["Key"] = key
    response = self.__send_uart(sJson)
    return response['Code']
    
def delete_tree(self):
    '''!Delete the entire tree from the cloud database. The tree is the value that we passed initially when setting the platform.
    @return an integer code representing whether the operation suceeded or not. 
    '''
    sJson = self.__getCmdJson("Delete")
    dJson = sJson["Data"]
    dJson["FullTree"] = True
    response = self.__send_uart(sJson)
    return response['Code']
    
def get_ip_address():
    '''!Get the IP address of this module. When we call the connect_wifi() method, if the module is able to connect to the access point, then it gets an IP Address.
    @return IP Address of this module. None if the module is not yet connected
    '''
    return self.__ipaddress 

def __getCmdJson(self, cmd) :
    sJson = {}
    sJson["CMD"] = cmd
    sJson["Data"] = {}
    return sJson 

def __send_uart(self, js, waitForResponse=True):        
    sendString = json.dumps(js)
    ret_val = None
    if (self.__isdebug):
        #print("Sending-[{}]".format(sendString))
        pass
    rxData = bytearray()
    # First flush out any pending UART data on the buffer
    time.sleep(0.1)        
    while self.__uart.any()>0:
        cur_read=self.__uart.read(1)
        try:
            rxData.append(cur_read)
        except TypeError:
            #print("Unexpected data received={}-{}".format(cur_read, type(cur_read)))
            pass
        time.sleep(0.1)
    if (len(rxData) > 0):
        print("Flushing extra data - {}".format(rxData))
    #rxData.clear()
    self.__uart.write(sendString)
    starttime = utime.ticks_ms()
    if waitForResponse :                 
        curtime = starttime
        isTimeout = True
        while curtime < (starttime + UARTTIMEOUT):
            if (self.__uart.any() >0):
                 isTimeout = False 
                 break 
            time.sleep(0.1)
            curtime = utime.ticks_ms()
        if isTimeout:
            raise RuntimeError("Timeout waiting for response from WiNoT module")
        ret_val = self.__read_uart_helper(starttime)
        '''
        in_str = self.__uart.readline()
        #print ("Raw response={}".format(in_str))
        in_str = in_str.decode('utf-8')
        in_str = in_str.strip()
        if (self.__isdebug):
            print("Received response=[{}]".format(in_str))
        
        try :
            ret_val = json.loads(in_str)
        except ValueError as e:            
            ret_val = in_str
        '''
    return ret_val
    
def __read_uart_helper(self, starttime):
    rxData = bytearray()
    is_done = False
    cur_read = 0
    ret_val = None
    curtime = utime.ticks_ms()
    while not is_done:
        if self.__uart.any()>0:
            cur_read=self.__uart.read() # Don't use readLine - that is not consistent. Probably due to the same reason which I mention below
            utime.sleep_us(100)  # Without this read() function goes berserk. To me it appears that Micropython UART's read() function 
                        # is not immediately flushing after reading. As a result, sometimes the same characters are ready multiple times. 
                        # by giving a small sleep, everybody is happy. 
        if curtime > (starttime + UARTTIMEOUT):
            raise RuntimeError("Timed out!Received partial response from server-[{}]".format(rxData))
        last_byte=cur_read[-1]
        if last_byte == ord('\n'): # No need to check for \r\n - we will only send \n from the WiNoT Module
            cur_read = cur_read[0:-1]
            is_done = True
        
        try:
            rxData += cur_read
        except TypeError:
            print("Unexpected data received={}-{}".format(cur_read, type(cur_read)))
            pass
        if is_done:
            in_str = rxData.decode('utf-8')
            try :
                ret_val = json.loads(in_str)
            except ValueError as e:
                print ("Recieved string is not a json = {}".format(in_str))
                ret_val = None
            break
        curtime = utime.ticks_ms()
    #print("Time to retrieve={}".format(curtime - starttime))
    return ret_val   
