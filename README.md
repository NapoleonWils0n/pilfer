# Pilfer

Python command line tool to record audio and video from within Kodi or on the command line.  
And use mpv as external player with Kodi
Works on Linux, Windows, Mac, Freebsd

* [pilfer youtube videos](https://www.youtube.com/watch?v=uKRU74Uqj1s&list=PL7hhhG5qUoXmtylBpTV4AdjFkYOj2soEB)

Script requirements:

* git
* python 3.6 
* python 3.6 pip
* ffmpeg 3.0 and above
* rtmpdump 2.4
* mpv

Set up instructions

* [Linux](https://github.com/NapoleonWils0n/pilfer#linux-set-up)
* [Windows](https://github.com/NapoleonWils0n/pilfer#windows-set-up)
* [Mac](https://github.com/NapoleonWils0n/pilfer#mac-set-up)
* [Freebsd](https://github.com/NapoleonWils0n/pilfer#freebsd-set-up)

## Recording from within Kodi

You need to install the playercorefactory.xml into your Kodi userdata folder,  
and restart Kodi for the menu to show up.

Press y on the keyboard while a video is playing in Kodi to bring up the contextual menu,  
from the menu you can then choose from the following options.

* play
* record video
* record video - 30 minutes
* record video - 1 hour
* record video - 2 hours
* record video - 3 hours
* save url
* record audio
* record audio - 30 minutes
* record audio - 1 hour
* record audio - 2 hours
* record audio - 3 hours

You can also edit the playercorefactory.xml file and add your own menu entrys,  
to create more recording durations.

Video and audio recordings will be saved to the Desktop with current date and time in the filename,  
so that each recording has a unique name and isnt overwritten by another recording

It isnt possible to get the videos title from the url which is why we add the date and time to the filename

The recording will be saved to your Desktop with the following filename

video-{date}-{time}.mkv  
audio-{date}-{time}.mka


## Script usage on the command line

Record video with the -i option with a url in single quotes

* url surrounded by single quotes

```
pilfer -i 'http://example.com/video.m3u8'
```

Record audio with the -a option

* url surrounded by single quotes

```
pilfer -a 'http://example.com/video.m3u8'
```

Record with the -i option and a text file

* Text file containing url

```
pilfer -i url.txt
```

Record audio with the -a option and a text file

* Text file containing url

```
pilfer -a url.txt
```

Recording with duration, 00:00:00 = hours:minutes:seconds

* Record video for 30 minutes

```
pilfer -i 'http://example.com/video.m3u8' -t 00:30:00
```

* Record audio for 30 minutes

```
pilfer -a 'http://example.com/video.m3u8' -t 00:30:00
```

* Record video for 1 hour

```
pilfer -i 'http://example.com/video.m3u8' -t 01:00:00
```

* Record audio for 1 hour

```
pilfer -a 'http://example.com/video.m3u8' -t 01:00:00
```

Text file containing url, recording with duration, 00:00:00 = hours:minutes:seconds

* Record for 30 minutes

```
pilfer -i video-url.txt -t 00:30:00
```

* Record for 1 hour

```
pilfer -i video-url.txt -t 01:00:00
```

## Linux set up

### Ubuntu

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump, mpv

```
sudo apt install -y python3 python3-pip git ffmpeg rtmpdump mpv
```

### Debian

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump, mpv

```
sudo apt install -y python3 python3-pip git-core ffmpeg rtmpdump mpv
```

### Arch Linux

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump, mpv

```
sudo pacman -S python python-pip git ffmpeg rtmpdump mpv
```

#### Add path to python script to ~/.bashrc

Edit your ~/.bashrc with your favourite text editor  
For example to edit your ~/.bashrc with nano run the following command

```
nano ~/.bashrc
```

Then add the following code to your ~/.bashrc and save the file.

```
if [ -d "$HOME/.local/bin" ]; then
   PATH="$HOME/.local/bin:$PATH"
fi
```

Finally source your ~/.bashrc

```
source ~/.bashrc
```

#### Install scripts with pip

Note if you only have python 3.6 install the pip command will be pip and not pip3  
The pip command may also be called pip3.6 on different linux distribution

The quickest way to find to find the name of the pip command on linux is to type pip in the terminal  
and then press the tab key and it will show you a list of the pip commands.

```
pip3 install --user git+https://github.com/NapoleonWils0n/pilfer.git
```

* Upgrade scripts with pip

```
pip3 install --upgrade --user git+https://github.com/NapoleonWils0n/pilfer.git
```

#### Install playercorefactory.xml file

You also need to install the playercorefacory.xml for your operating system,  
into the kodi userdata directory

* Kodi playercorefactory.xml download links 

[Linux, Freebsd - playercorefactory.xml](https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/linux-unix/playercorefactory.xml)  

Open the link for your operating system and right click on the webpage and select save as to save the file  
Then move the playercorefactory.xml file into the kodi userdata folder for your operating system listed below.  

Location of kodi userdata folder

* Linux ~/.kodi/userdata/

You can also download the playercorefactory.xml file with wget 

```
wget https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/linux-unix/playercorefactory.xml
```

And then move the playercorefactory.xml into your ~/.kodi/userdata directory  
If you already have a playercorefactory.xml file in your kodi userdata directory,  
make sure to rename or move the file or it will be overwritten

```
mv playercorefactory.xml ~/.kodi/userdata/
```

## Windows set up

### Windows pilfer installer

Windows installer by the t3rmin8tor to automatically install all the programs and scripts  

[pilfer windows installer by the t3rmin8tor](https://github.com/t3rmin8tor/pilfer-installer)

### Windows install

Windows install instructions 

#### Download the playercorefactory.xml file

Download the 32bit or 64bit zip file depending on which version you are running  
the zip file contains the playercorefactory.xml file and the pilfer folder 

[32bit playercorecfactory.xml zip](https://github.com/NapoleonWils0n/pilfer/raw/master/playercorefactory/windows/32bit.zip)  
[64bit playercorecfactory.xml zip](https://github.com/NapoleonWils0n/pilfer/raw/master/playercorefactory/windows/64bit.zip)

Move the pilfer folder to your C drive  
The path should look lile this

```
C:\pilfer
```

Move the playercorefactory.xml to Kodi userdata folder

Open the Windows Start menu and type

```
%APPDATA%\kodi\userdata
```

This will open the Kodi userdata folder in the Windows file manager  
Copy the playercorefactory.xml file into the kodi\userdata folder

#### Install Git

[git windows installer](https://git-scm.com/download/win)

Download git and run the installer

Adjusting your path

Select 2nd option for path not git bash shell
Use Git from the Windows Command Prompt

Configuring the line endings

Select the 2nd option
Checkout as--is, commit Unix-style line endings

#### Python 3 install

[Python for Windows](https://www.python.org/downloads/windows/)

[Python Windows installer](https://www.python.org/ftp/python/3.6.2/python-3.6.2-amd64.exe)

Download and run the python 3 installer  
Check add Python 3.6 to PATH and click Install Now

#### 7zip download and install

We need to download and install 7zip so we can unzip the mpv download

[7zip](http://www.7-zip.org/)

#### ffmpeg download and install

[ffmpeg windows download](http://ffmpeg.zeranoe.com/builds/)

Unzip the ffmpeg.zip file

Move the ffmpeg.exe file into C:\pilfer\system\bin

#### rtmpdump download and install

Download and unzip the rtmpdump.zip file

[rtmpdump 2.4 windows](https://rtmpdump.mplayerhq.hu/download/rtmpdump-2.4-git-010913-windows.zip)

Then move the rtmpdump.exe file into the C:\pilfer\system\bin folder

#### mpv download and install

[mpv site](https://mpv.io/installation/)

Download the latest version of mpv for Windows below.
And unzip the mpv.7z file with 7zip

[mpv windows download](https://mpv.srsfckn.biz/)

Then copy the following files from the mpv folder into the C:\pilfer\system\bin folder

* mpv.exe
* d3dcompiler_43.dll
* libaacs.dll
* libbdplus.dll

You may need to hold down control to copy the mpv file into the folder
The dll files are needed because otherwise you get a blue screen with mpv and no video

[This script sets up file associations for mpv on Windows](https://github.com/rossy/mpv-install/blob/master/README.md)

Download the mpv windows setup script below.

[mpv windows set up script](https://github.com/rossy/mpv-install/archive/master.zip)

Copy the .bat files and the .ico to the same directory as mpv.exe Run mpv-install.bat as administrator.
Note: For an unattended install, use the /u switch. Use the Default Programs and AutoPlay control panels to make mpv the default player

This is a fix for black screen when trying to play videos with mpv
Open the mpv config folder by typing in the following into Search Windows dialog box

```
%APPDATA%\mpv
```

Create a text file called mpv.conf and add the following code

```
vo=direct3d
```

move the mpv.conf text file into the %APPDATA%\mpv folder

#### Add pilfer bin folder to windows system path

Open system properties, advanced system settings, enviormnental variables

system variables, path, edit and add the code below to your windows system path  

```
C:\pilfer\system\bin
```

#### Install scripts with pip

```
pip3.6 install --user git+https://github.com/NapoleonWils0n/pilfer.git
```

#### Upgrade scripts with pip

```
pip3.6 install --upgrade --user git+https://github.com/NapoleonWils0n/pilfer.git
```


## Mac set up

### ffmpeg install

* Download ffmpeg - [ffmpeg download](https://evermeet.cx/ffmpeg/)

Create a folder called bin in your home folder, /Users/your-username/bin

```
mkdir -p ~/bin
```

Double click the ffmpeg.dmg file and copy ffmpeg into the ~/bin directory

If you have ffmpeg installed to another location create a symbolic link to $HOME/bin/ffmpeg  

Then edit your ~/.bash_profile, for example with nano

```
nano ~/.bash_profile
```

And add the code below to your ~/.bash_profile,  
which will add any binaries in ~/bin to your bash path

```
if [ -d "$HOME/bin" ] ; then
        PATH="$HOME/bin:$PATH"
fi
```

Then we need to add the path to the python scripts as well  

```
if [ -d "$HOME/Library/Python/3.6/bin" ] ; then
        PATH="$HOME/Library/Python/3.6/bin:$PATH"
fi
```

Then source your ~/.bash_profile

```
source ~/.bash_profile
```

### rtmpdump install

Install rtmpdump with homebrew

### mpv install

Download the 64bit build from mpv.io and install to your Applications folder

[mpv](https://mpv.io/installation/)

[Latest build](https://laboratory.stolendata.net/~djinn/mpv_osx/mpv-latest.tar.gz)

### Install xcode command line tools

* Open a terminal and type

```
xcode-select --install
```

### Homebrew install

* Open a terminal and paste in the code below

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* Check brew install

```
brew doctor
```

* rtmpdump install with homebrew

```
brew install rtmpdump
```

### Git install

Git download - [git download](https://git-scm.com/download/mac)

Download git and then run the installer

### Python install

Python download - [python](https://www.python.org/downloads/mac-osx/)

Download and install python

#### Install scripts with pip

```
pip3.6 install --user git+https://github.com/NapoleonWils0n/pilfer.git
```

* Upgrade scripts with pip

```
pip3.6 install --upgrade --user git+https://github.com/NapoleonWils0n/pilfer.git
```

#### Install playercorefactory.xml file

You also need to install the playercorefacory.xml for your operating system,  
into the kodi userdata directory

* Kodi playercorefactory.xml download links 

* [Mac python 3.6 - playercorefactory.xml](https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/mac/python-3.6/playercorefactory.xml)  
* [Mac python 3.7 - playercorefactory.xml](https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/mac/python-3.7/playercorefactory.xml)  

Open the link for your operating system and right click on the webpage and select save as to save the file  
Then move the playercorefactory.xml file into the kodi userdata folder for your operating system listed below.  

Location of kodi userdata folder

* Mac /Users/<your_user_name>/Library/Application Support/Kodi/userdata/

## Freebsd set up

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump, mpv

```
sudo pkg install python36 py36-pip git ffmpeg rtmpdump mpv
```

You can also use ports to install the required software

#### Add path to python script to ~/.bashrc

Edit your ~/.bashrc with your favourite text editor  
For example to edit your ~/.bashrc with nano run the following command

```
nano ~/.bashrc
```

Then add the following code to your ~/.bashrc and save the file.

```
if [ -d "$HOME/.local/bin" ]; then
   PATH="$HOME/.local/bin:$PATH"
fi
```

Finally source your ~/.bashrc

```
. ~/.bashrc
```

#### Install scripts with pip

```
pip-3.6 install --user git+https://github.com/NapoleonWils0n/pilfer.git
```

* Upgrade scripts with pip

```
pip-3.6 install --upgrade --user git+https://github.com/NapoleonWils0n/pilfer.git
```
#### Install playercorefactory.xml file

You also need to install the playercorefacory.xml for your operating system,  
into the kodi userdata directory

* Kodi playercorefactory.xml download links 

[Linux, Freebsd - playercorefactory.xml](https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/linux-unix/playercorefactory.xml)  

Open the link for your operating system and right click on the webpage and select save as to save the file  
Then move the playercorefactory.xml file into the kodi userdata folder for your operating system listed below.  

Location of kodi userdata folder

* Freebsd ~/.kodi/userdata/

You can also download the playercorefactory.xml file with wget 

```
wget https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/linux-unix/playercorefactory.xml
```

And then move the playercorefactory.xml into your ~/.kodi/userdata directory  
If you already have a playercorefactory.xml file in your kodi userdata directory,  
make sure to rename or move the file or it will be overwritten

```
mv playercorefactory.xml ~/.kodi/userdata/
```
