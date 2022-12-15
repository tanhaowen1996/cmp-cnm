import re


class Cidr:
    def Masker(self, ipaddr, mask):
        IP10L = re.findall(r'\d*', ipaddr)
        for x in IP10L:
            IP10L.remove('')
        IP2L = []
        IP2 = ''
        for x in IP10L:
            MyBin = str(bin(int(x)))[2:]
            MyZero = '0' * (8 - len(MyBin))
            IP2L.append(str(MyZero) + (bin(int(x)))[2:])
        for x in IP2L:
            IP2 = IP2 + str(x)
        MyNetworkt1 = str(IP2[0:int(mask)]) + str(str(0) * (32 - int(mask)))
        MyNetwork2 = []
        i = 0
        while i <= 3:
            MyNetwork2.append(int(MyNetworkt1[i * 8:(i + 1) * 8], 2))
            i += 1
        MyNetworkt3 = str(MyNetwork2)[1:-1].replace(',', '.')
        MyNetwork = MyNetworkt3.replace(' ', '')
        return str(MyNetwork)