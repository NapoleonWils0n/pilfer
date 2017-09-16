# Pilfer

Python command line tool to record videos from within Kodi or on the command line.  
Works on Linux, Windows, Mac, Freebsd

Script requirements:

* git
* python 3.6 
* python 3.6 pip
* ffmpeg 3.0 and above
* rtmpdump 2.4

You also need to install the playercorefacory.xml for your operating system,  
into the kodi userdata directory

* Kodi playercorefactory.xml download links 

[Linux, Freebsd - playercorefactory.xml](https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/linux-unix/playercorefactory.xml)  
[Windows - playercorefactory.xml](https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/windows/playercorefactory.xml)  
[Mac - playercorefactory.xml](https://raw.githubusercontent.com/NapoleonWils0n/pilfer/master/playercorefactory/mac/playercorefactory.xml)  

Open the link for your operating system and right click on the webpage and select save as to save the file  
Then move the playercorefactory.xml file into the kodi userdata folder for your operating system listed below.  

Location of kodi userdata folder

* Linux ~/.kodi/userdata/
* Windows Start - type %APPDATA%\kodi\userdata - press return
* Mac /Users/<your_user_name>/Library/Application Support/Kodi/userdata/
* Freebsd ~/.kodi/userdata/

## Recording from within Kodi

You need to install the playercorefactory.xml into your Kodi userdata folder,  
and restart Kodi for the menu to show up.

Press y on the keyboard while a video is playing in Kodi to bring up the contextual menu,  
from the menu you can then choose from the following recording options.

* Record
* Record 30 minutes
* Record 1 hour
* Record 2 hours
* Record 3 hours

You can also edit the playercorefactory.xml file and add your own menu entrys,  
to create more recording durations.

Videos will be saved to the Desktop with current date and time in the filename,  
so that each recording has a unique name and isnt overwritten by another recording

It isnt possible to get the videos title from the url which is why we add the date and time to the filename

The recording will be saved to your Desktop with the following filename

video-{date}-{time}.mkv


## Script usage on the command line

* Video url surrounded by single quotes

```
pilfer -i 'http://example.com/video.m3u8'
```

* Text file containing url

```
pilfer -i video-url.txt
```

Recording with duration, 00:00:00 = hours:minutes:seconds

* Record for 30 minutes

```
pilfer -i 'http://example.com/video.m3u8' -t 00:30:00
```

* Record for 1 hour

```
pilfer -i 'http://example.com/video.m3u8' -t 01:00:00
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

## Windows set up

* See t3rmin8tor repo

## Linux set up

### Ubuntu

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump

```
sudo apt install -y python3 python3-pip git ffmpeg rtmpdump
```

### Debian

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump

```
sudo apt install -y python3 python3-pip git-core ffmpeg rtmpdump
```

### Arch Linux

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump

```
sudo pacman -S python python-pip git ffmpeg rtmpdump
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
. ~/.bashrc
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

Then source your ~/.bash_profile

```
. ~/.bash_profile
```

### rtmpdump install

Install rtmpdump with homebrew

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

## Freebsd set up

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump

```
sudo pkg install python36 py36-pip git ffmpeg rtmpdump
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
