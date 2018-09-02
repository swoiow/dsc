
sc stop LanmanWorkstation
sc config LanmanWorkstation start= disabled

sc stop lmhosts
sc config lmhosts start= disabled

sc stop LanmanServer
sc config LanmanServer start= disabled

sc stop Browser
sc config Browser start= disabled

sc start MpsSvc
sc config Browser start= auto

netsh advfirewall set allprofiles state on

for %%i in (135, 137, 139, 445) do (netsh advfirewall firewall add rule name="DenyTCP%%i" dir=in protocol=tcp localport=%%i action=block) && (netsh advfirewall firewall add rule name="DenyUDP%%i" dir=in protocol=udp localport=%%i action=block)

echo. & pause
