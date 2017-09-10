# Pilfer

Python command line tool to record videos from within Kodi or on the command line

requirements:

* python 3.5 
* python 3.5 pip
* git
* ffmpeg
* rtmpdump

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

## Windows set up

* See t3rmin8tor repo

## Mac set up

### ffmpeg install

https://evermeet.cx/ffmpeg/

* install ffmpeg

create a folder called bin in your home folder, /Users/your-username/bin

```
mkdir -p ~/bin
```

copy the ffmpeg

if you have ffmpeg installed to another location create a symbolic link to $HOME/bin/ffmpeg the same applies to ffplay and ffprobe

then edit your ~/.bash_profile, for example with nano

```
nano ~/.bash_profile
```

and add the code below to your ~/.bash_profile,
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

install rtmpdump with homebrew

### install xcode command line tools

* open a terminal and type

```
xcode-select --install
```

### homebrew install

* open a terminal and paste in the code below

```
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

* check brew install

```
brew doctor
```

* rtmpdump install with homebrew

```
brew install rtmpdump
```

### git install

* git download

https://git-scm.com/download/mac

### python install

* python download link

https://www.python.org/downloads/mac-osx/

https://www.python.org/downloads/release/python-362/

## Freebsd set up

* Install python 3.6, python3.6 pip, git, ffmpeg, rtmpdump

```
sudo pkg install python36 py36-pip git ffmpeg rtmpdump
```

* install scripts with pip

```
pip3.5 install --user git+https://github.com/NapoleonWils0n/pilfer.git
```

* upgrade scripts with pip

```
pip3.5 install --upgrade --user git+https://github.com/NapoleonWils0n/pilfer.git
```

