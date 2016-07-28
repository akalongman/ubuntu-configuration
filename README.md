# Configuration of Ubuntu 16.04 Xenial Xerus

This is for a __Debian__ based OS, such as: [Ubuntu](http://ubuntu.com/desktop), [Mint](http://www.linuxmint.com/), and [Elementary OS](http://elementaryos.org/). I prefer Ubuntu 15.10

***

# Table of Contents
- [Optional Configurations](#optional-configurations)
    - [Get System Details](#get-system-details)
        - [Operating System](#operating-system)
        - [CPU Info](#cpu-info)
        - [VGA Info](#vga-info)
        - [Memory and Usage Info](#memory-and-usage-info)
        - [Disks](#disks)
        - [GUI Processes](#gui-processes)
        - [Packages](#packages)
        - [Other Commands](#other-commands)
            - [Screenshots](#screenshots)
    - [List all KeyBindings](#list-all-keybindings)
    - [Better Local Folder](#better-local-folder)
    - [Use 32Bit on 64bit](#use-32bit-on-64bit)
    - [Networking](#networking)
    - [Order of Grub](#order-of-grub)
    - [Mounting Drives](#mounting-drives)
        - [Mounting of Local Drives](#mounting-of-local-drives)
        - [Mounting of Network Drives](#mounting-of-network-drives)
        - [Mounting Amazon Cloud Drive](#mounting-amazon-cloud-drive)
    - [Generate a New SSH Key](#generate-a-new-ssh-key)
    - [Enable Native Virtualization](#enable-native-virtualization)
    - [Format USB](#format-usb)
    - [Write iso Image to USB](#write-iso-image-to-usb)
    - [Adding Printers](adding-printers)
        - [HP](hp)
- [Installation Packages](#installation-packages)
    - [Enable PPAs](#enable-ppas)
    - [System Tools](#system-tools)
        - [Install Nvidia Drivers](#install-nvidia-drivers) (Install drivers from official repository for Nvidia Drivers)
        - [Install ATI Drivers](#install-ati-drivers)
        - [Utilities](#utilities)
        - [RedShift For Eye Strain](#redshift-for-eye-strain)
        - [Dark Theme](#dark-theme)
        - [Sun Java](#sun-java)
        - [Wine](#wine) (Windows emulator) (Run Microsoft® Windows® applications on linux)
        - [Nautilus-Actions](#nautilus-actions) (Graphically create custom context menu options for Ubuntu's Nautilus file manager)
        - [Hardinfo](#hardinfo) (Everest/Aida alternative for linux)
        - [Caffeine](#caffeine) (Prevent the activation of the screensaver when using full-screen windows)
        - [GNU Screen](#gnu-screen) (Full-screen window manager that multiplexes a physical terminal between several processes)
    - [Other Tools](#other-tools)
        - [Google Chrome](#google-chrome)
        - [PlayOnLinux](#playonlinux) (Software which using wine allows you to easily install and use numerous games and apps designed to run with Microsoft® Windows®)
        - [Dropbox](#dropbox) (Allows users to create a special folder on their computers, which Dropbox then synchronizes so that it appears to be the same folder (with the same contents) regardless of which device is used to view it)
        - [Sublime Text 3](#sublime-text-3)
        - [Pidgin](#pidgin)
        - [DBeaver](#dbeaver) (Database management tool)
        - [VirtualBox](#virtualbox)
        - [Android Studio](#android-studio)
        - [SmartGit](#smart-git)
        - [FileZilla](#filezilla) (sFTP Client)
        - [Spotify](#spotify)
        - [Meld Diff Tool](#meld-diff-tool)
        - [Vagrant](#vagrant)
        - [Docker](#docker)
        - [Audacious Audio Player](#audacious-audio-player)
        - [XnViewMP](#xnviewmp) (Powerful cross-platform media browser, viewer and converter)
        - [Sticky Notes](#sticky-notes)
        - [Guake](#guake) (Quake like Terminal)
        - [Skype](#skype)
        - [Telegram](#telegram)
        - [Slack](#slack)
        - [Gimp](#gimp)
        - [Httpie](#httpie) (Terminal HTTP client)
        - [USB Maker for Windows ISO on Linux](#usb-maker-for-windows-on-linux)
    - [LAMP](#lamp)
        - [PHP 5.6](#php-56)
        - [PHP 7.0](#php-70)
        - [Composer](#composer)
        - [PHPUnit](#phpunit)
        - [Apache](#apache)
            - [Installation](#apache-installation)
            - [Enable php-mcrypt](#apache-enable-php-mcrypt)
            - [Configure Dynamic Virtualhosts](#apache-configure-dynamic-virtualhosts)
        - [Nginx](#nginx)
        - [MySQL](#mysql)
        - [MyCLI](#mycli) Terminal MySQL Utility
        - [Memcached](#Memcached)
        - [Redis](#redis)
        - [Phalcon](#phalcon)
        - [Phalcon Dev Tools](#phalcon-dev-tools)
        - [Secure Permissions](#secure-permissions)
    - [Python](#python)
        - [Pip](#pip)
        - [Virtualenv](#virtualenv)
    - [Ruby](#ruby)
    - [NodeJS](#nodejs)
- [Customizations](#customizations)
    - [System Tweaks](#system-tweaks)
        - [Increase Inotify Watches Limit](#increase-inotify-watches-limit)
        - [Disable Git Certificate Verification](#disable-git-certificate-verification)
    - [Shortcuts](#shortcuts)
    - [VIM Customization](#vim-customization)
    - [Enable Auto Focus on Opened Applications](#enable-auto-focus-on-opened-applications)
    - [Enable Normal Scrollbars](#enable-normal-scrollbars)
    - [Enable User Name in Systray](#enable-user-name-in-systray)
    - [Change Datetime Format in Systray](#change-datetime-format-in-systray)
    - [Enable Minimize App on Dash Click](#enable-minimize-app-on-dash-click)
    - [Disable Window Grouping](#disable-window-grouping)
    - [Install Custom Wallpaper](#install-custom-wallpaper)
    - [Change Greeter Background](#change-greeter-background)
    - [Add Georgian Keyboard](#add-georgian-keyboard)
- [Ubuntu Fixes](#ubuntu-fixes)
    - [Sound Indicator Not Showing](#sound-indicator-not-showing)
- [Install Gnome 3](#install-gnome-3)
    - [Easy Window Resize](#easy-window-resize)
    - [Left or Right Close Buttons](#left-or-right-close-buttons)
    - [Fix Gnome Lockscreen](#fix-gnome-lockscreen)
    - [My Gnome Extensions](#my-gnome-extensions)
    - [Reload Gnome Freeze](#reload-gnome-freeze)
- [Adjust Mouse and Devices](#adjust-mouse-and-devices)
- [Virtual Machine Related](#virtual-machine-related)
    - [Fix Mouse Side Buttons in VMWare](#fix-mouse-side-buttons-in-vmware)
    - [Vagrant VBGuest Fix](#vagrant-vbguest-fix)
    - [Windows 8 VirtualBox Fix](#windows-8-virtualbox-fix)
- [Synchronize Configurations](#synchronize-configurations)
    - [Sync Sublime Text](#sync-sublime-text)
    - [Sync FileZilla](#sync-filezilla)
- [Chrome Addons](#chrome-addons)
- [Other Applications](#other-applications)
- [Clean System](#clean-system)

***

[(Back to top)](#table-of-contents)

# Optional Configurations

### Get System Details

#### Operating System

    lsb_release -a
    lsb_release -as     # Short Information
    lsb_release -sc     # OS Codename
    lsb_release --help

#### CPU Info

    nproc               # How many Processing Units
    cpuid               # Must install cpuid from terminal
    cat /proc/cpuinfo   # Lots of info

#### VGA Info

    lspci -vnn | grep -i VGA -A 12

#### Memory and Usage Info

    free -h             # Human readable, or do --help for options
    top or htop         # Must install htop
    vmstat -s
    cat /proc/meminfo   # Lots of info

#### Disks
Disk Space

    df
    df -B MB    # In Megabtyes,  etc

Disks UUID

    ls -al /dev/disk/by-uuid/

#### GUI Processes

    gnome-system-monitor

#### Packages

List of Packages

    dpkg -l

#### Other Commands

##### Screenshots
To taking screenshot from terminal run this:

    gnome-screenshot

With delay 5 seconds

    gnome-screenshot --delay 5

With delay 5 seconds and only window

    gnome-screenshot -w --delay 5

## List all Keybindings

    gsettings list-recursively  org.gnome.desktop.wm.keybindings | sort | more

See your keypressed:

    xev

Or for a lot of details:

    xev | grep KeyPress

## Better Local Folder
This is less painful when creating a group with rwx permissions for `/usr/local`

    sudo groupadd local
    sudo usermod -a -G local jesse

    sudo chgrp -R local /usr/local
    sudo chmod -R g+rwx /usr/local

## Use 32Bit on 64bit

You can use 32Bit applications if you like, sometimes this is useful.

    sudo apt update && sudo apt install -y unetbootin

## Networking

To enable Networking, and make it accessible to all computers such as Windows also first install Samba:

    $ sudo apt install -y samba

Then edit the Samba config:

    $ vim /etc/samba/smb.conf

Under `[global]` change the workgroup to what you use, the default is WORKGROUP:

    workgroup = WORKGROUP

Then you will have to reload your Session.

## Order of Grub
If you are running Grub as your default boot-loader, you can use this application to make it easier to change the order.

    sudo add-apt-repository -y ppa:danielrichter2007/grub-customizer
    sudo apt update && sudo apt install -y grub-customizer

Load the application either with `<Super>` and look for grub customizer or terminal `gksudo grub-customizer`.

Go to the `General Settings` tab, and you'll see *default entry*.

- Click the drop-down list and you can either select Entry By Order (Left Column) Or a specific Item (Right Column).
- If you are dual booting Windows and want Windows the default, Select the right column for Windows.
- The reason is if more items are added, perhaps new kernels, then if Position 5 which held Windows will no longer be the default.

## Mounting Drives

### Mounting of Local Drives

Open /etc/fstab

    sudo vim /etc/fstab

Add to /etc/fstab this line (You can get DISK UUID by command ```ls -al /dev/disk/by-uuid/```):

For NTFS disk:

    UUID=[DISK UUID] /media/D ntfs-3g defaults,windows_names,locale=en_US.utf8 0 2

For ext4 disk:

    UUID=[DISK UUID] /media/D ext4 defaults 0 2

After run

    sudo mount -a

### Mounting of Network Drives

Open /etc/fstab

    sudo vim /etc/fstab

And add:

If requires authorization:

    username@remote_address:/remote/path /local/path fuse.sshfs delay_connect,_netdev,idmap=user,uid=1000,gid=1000,noatime,default_permissions,IdentityFile=/home/USER/.ssh/id_rsa,reconnect,transform_symlinks,allow_other 0 0

If not requires:

    //remote_address/remote/path /local/path cifs guest,iocharset=utf8,uid=1000,gid=1000,file_mode=0777,dir_mode=0777,noperm,_netdev 0 0

After run

    sudo mount -a


### Mounting Amazon Cloud Drive


Install Prerequisites

    sudo apt install -y python3 python3-appdirs python3-dateutil python3-requests python3-sqlalchemy python3-pip

Install acd_cli (https://github.com/yadayada/acd_cli)

    cd ~ && sudo pip3 install --upgrade git+https://github.com/yadayada/acd_cli.git

Initiate "sync" which will launch a browser (chrome/lynx/etc) to amazon.com and setup your oauth key.

    acd_cli sync

Copy/Paste and store your oauth data.
Note: it will most likely have improper newline breaks. Fixup in your favorite text editor.

    vim ~/.cache/acd_cli/oauth_data

Add your user to the "fuse" group to allow mounting

    sudo addgroup <username> fuse

Mount the root of your Amazon Cloud drive to the /media/amazon directory

    mkdir /media/amazon
    acd_cli mount /media/amazon

Upload

    -d     exclude duplicate files from upload
    -x     upload threads

e.g. Upload your local /media/videos directory to the root of your Amazon Cloud Drive.

    acd_cli upload -d -x 4 /media/videos /


## Generate a new SSH key

    ssh-keygen -t rsa -C "your_email@example.com"

## Enable Native Virtualization

Instal tools

    sudo apt install -y qemu-kvm libvirt-bin ubuntu-vm-builder bridge-utils

Check if supported by hardware

    sudo egrep '(vmx|svm)' --color=always /proc/cpuinfo

If nothing is displayed, then your processor doesn't support hardware virtualization, and you must stop here.

Run:

    kvm-ok

If you have KVM, you will see: "INFO: Your CPU supports KVM extensions INFO: /dev/kvm exists KVM acceleration can be used"

Next, add your user to the KVM group and libvirtd group. To do so, type:

    sudo adduser $(whoami) kvm
    sudo adduser $(whoami) libvirtd

After the installation, re-login so that the changes take effect. You can test the installation by typing:

    sudo virsh -c qemu:///system list


## Format USB

Enter sudo mode

    sudo su

List available disks and detect where it was mounted: /dev/sd[1 letter][optionally 1 number]. For example, /dev/sdc or /dev/sdc1

    fdisk -l

or

    lsblk

Unmount drive

    umount sd[1 letter][optionally 1 number]


Format to FAT32

    mkfs.vfat /dev/sd[1 letter][optionally 1 number]

You can use mkfs.ntfs for NTFS, mkfs.ext4 for EXT4 etc.

Eject drive

    eject /dev/sd[1 letter]


## Write iso Image to USB

List available disks and detect where it was mounted: /dev/sd[1 letter][optionally 1 number]. For example, /dev/sdc or /dev/sdc1

    fdisk -l

or

    lsblk

Make sure the USB device is unmounted (not safely removed, but unmounted) If it is mounted you can unmount it:

    sudo umount /dev/sd[1 letter][optionally 1 number]

For writing image run:

    sudo dd bs=4M if=path/to/your/iso/file.iso of=/dev/sd[that 1 letter]


## Adding Printers

### HP

You must download HPLIP software from here: http://hplipopensource.com/hplip-web/gethplip.html

After install .run package [how?](https://help.ubuntu.com/community/InstallingRunPackage) and run.
Follow the wizard and add neccessary HP printer


***

[(Back to top)](#table-of-contents)


# Installation Packages

Login to your Linux user and go to your **home** directory,

    cd ~

Run these commands and tweak them as needed. The `-y` flag installs without a prompt. Run these commands from the terminal.

    sudo apt update && sudo apt upgrade

## Enable PPAs
PPA's are provided within categories below, I highly recommend using PPA's or at least installing this package in case you ever use them.

Enable Canonical partners repository

    sudo add-apt-repository -y "deb http://archive.canonical.com/ $(lsb_release -sc) partner" && sudo apt update

## System Tools
This is for tweaking the UI

    sudo apt update && sudo apt install -y\
        unity-tweak-tool\
        compizconfig-settings-manager\
        compiz-plugins\
        dconf-editor\
        synaptic

### Install Nvidia Drivers

You can check your [VGA Info](#vga-info)

Find out the right driver version for your graphics card on http://www.nvidia.com/Download/index.aspx

Install Nvidia Drivers

    sudo add-apt-repository -y ppa:graphics-drivers/ppa

    sudo apt update && sudo apt install -y nvidia-XXX

Type your version instead XXX

And after select your installed driver from drivers tab

    sudo software-properties-gtk

Remove Nvidia Drivers

    sudo add-apt-repository -r ppa:graphics-drivers/ppa

**To Edit Nvidia Settings**; Type the following in the Global Launcher *(Super Key/Windows Key)*:

    nvidia settings


### Install ATI Drivers

    TDB


### Utilities

**Install the Utilities:**

    sudo apt install -y vim git mercurial meld curl htop xclip unzip gdebi preload bleachbit ubuntu-restricted-extras cifs-utils unace unrar zip p7zip-full p7zip-rar sharutils rar openssh-server lm-sensors whois traceroute nmap font-manager python-gpgme sshfs mc libavcodec-extra libdvd-pkg nfs-kernel-server

To setup the git defaults

    git config --global user.name your name
    git config --global user.email your@email.com

That will create a `~/.gitconfig` with:

    [user]
        email = you@email.com
        name = your name

### RedShift For Eye Strain

    sudo apt install -y redshift

Create your configuration file:

    sudo vim ~/.config/redshift.conf

Adjust the temperatures you prefer. I like mine to be very yellow and dim. (The lower the dimmer)

    [redshift]
    temp-day=3500
    temp-night=3500
    ; Set the screen brightness. Default is 1.0.
    ;brightness=0.9
    ; It is also possible to use different settings for day and night
    ;brightness-day=0.7
    ;brightness-night=0.4
    ; There are more settings for Gamma, Location Provider, Manual Location, etc.

Close and reload redshift. If you cannot find the icon anywhere run this in terminal:

    pkill redshift-gtk redshift

If RedShift gives you a `Geoclue2` error do this:

    sudo vim /etc/geoclue/geoclue.conf

Append these lines at the bottom:

    [redshift]
    allowed=true
    system=false
    users=

A newer version of redshift will install a desktop file so a Geoclue2 warning won't happen
on newer systems.

### Dark Theme

I prefer [Vivacious ZBlackout Blue Pro Theme](http://www.noobslab.com/2016/03/vivacious-colors-gtk-theme-suite.html)

Add repository

    sudo add-apt-repository ppa:ravefinity-project/ppa
    sudo apt update

Installation

    sudo apt install -y vivacious-colors-gtk-dark
    sudo apt install -y vivacious-colors-gtk-light
    sudo apt install -y vivacious-unity-gtk-dark
    sudo apt install -y vivacious-unity-gtk-light


Use the **Unity Tweak Tool** to set vivacious-zblackout-blue-pro


### Sun Java

Install

    sudo apt-add-repository ppa:webupd8team/java
    sudo apt update && sudo apt install -y oracle-java8-installer

Set Oracle Java as main in system

    sudo vim /etc/environment

Add this line

    JAVA_HOME=/usr/lib/jvm/java-8-oracle

And update alternatives
    sudo update-alternatives --config java

### Wine
To run windows applications Wine is the best option. I often use HeidiSQL with Wine.

    sudo add-apt-repository -y ppa:ubuntu-wine/ppa
    sudo apt update

You can check latest version of wine here https://www.winehq.org/
While writing this article, lastest version was 1.8

If you need a 64bit installation:

    sudo apt install -y wine1.8-amd64 winetricks

If you need a 32bit installation:

    sudo apt install -y wine1.8-i386 winetricks

### Nautilus-Actions
Use Nautilus-Actions to easily and graphically create custom context menu options for Ubuntu's Nautilus file manager.
If you don't want to create your own, you can install Nautilus-Actions-Extra to get a package of particularly useful user-created tools.

    sudo apt install -y nautilus-actions

After installing it, quit and restart the Nautilus file manager with the following command.
You can also press Alt+F2 and type this command instead of running it in a terminal.

    nautilus -q

Launch the Nautilus-Actions Configuration Tool from the Dash after installing it.

You also can install some Nautilus extensions

    sudo apt install -y nautilus-admin nautilus-meld nautilus-checksum-menu


### Hardinfo

Hardinfo is a Everest/Aida alternative for Linux. Its shows system information

    sudo apt install -y hardinfo


### Caffeine

Caffeine is a tool used to temporarily prevent the activation of the screensaver / lock screen / sleep mode,
when using full-screen windows. The application is useful if you're using a video player that doesn't do this automatically,
when listening to music, etc.

    sudo apt install -y caffeine

__Note__: After the installation, the command-line version of Caffeine is set to start automatically on login.
If you want the indicator to start automatically, you'll have to add "caffeine-indicator" to your startup applications.


### GNU Screen

Screen is a full-screen window manager that multiplexes a physical terminal between several processes, typically interactive shells.
Each virtual terminal provides the functions of the DEC VT100 terminal and, in addition, several control functions from the ANSI X3.64 (ISO 6429) and ISO 2022 standards (e.g., insert/delete line and support for multiple character sets).
There is a scrollback history buffer for each virtual terminal and a copy-and-paste mechanism that allows the user to move text regions between windows.
When screen is called, it creates a single window with a shell in it (or the specified command) and then gets out of your way so that you can use the program as you normally would.
Then, at any time, you can create new (full-screen) windows with other programs in them (including more shells), kill the current window, view a list of the active windows, turn output logging on and off, copy text between windows, view the scrollback history, switch between windows, etc. All windows run their programs completely independent of each other.
Programs continue to run when their window is currently not visible and even when the whole screen session is detached from the users terminal.

    sudo apt install -y screen


***
[(Back to top)](#table-of-contents)

## Other Tools

### Google Chrome
    Add google chrome repository and install

        sudo sh -c 'echo "deb [arch=amd64] http://dl-ssl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
        sudo apt update && sudo apt install -y google-chrome-stable

    Then launch it with `$ google-chrome` and you can pin it to a unity bar.

### PlayOnLinux

Installation

    wget -q "http://deb.playonlinux.com/public.gpg" -O- | sudo apt-key add -
    sudo wget http://deb.playonlinux.com/playonlinux_trusty.list -O /etc/apt/sources.list.d/playonlinux.list
    sudo apt update && sudo apt install -y playonlinux

### Dropbox

Installation

    sudo sh -c 'echo "deb http://linux.dropbox.com/ubuntu $(lsb_release -sc) main" >> /etc/apt/sources.list.d/dropbox.list'
    sudo apt-key adv --keyserver pgp.mit.edu --recv-keys 1C61A2656FB57B7E4DE0F4C1FC918B335044912E
    sudo apt update && sudo apt install -y dropbox

### Sublime Text 3

Download from http://www.sublimetext.com/3

Configuration synchronization explained [here](#sync-sublime-text)

### Pidgin

Installation

    sudo apt -y install pidgin

Configuring google talk account

Basic

- Protocol: XMPP
- Username: [username without @]
- Domain: [username domain after @]
- Password: [account password]

Advanced

- Connect Port: 5222 Connect Server: talk.google.com

### DBeaver

Download from http://dbeaver.jkiss.org/download/

### VirtualBox

Installation

    sudo sh -c 'echo "deb http://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" >> /etc/apt/sources.list.d/virtualbox.list'
    wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox_2016.asc -O- | sudo apt-key add -
    sudo apt update && sudo apt install -y virtualbox-5.0

Suggested to [Enable Native Virtualization](#enable-native-virtualization)

Also you can read [Virtual Machine Related](#virtual-machine-related)

### Android Studio

Installation

Download Android Studio from https://developer.android.com/sdk/index.html
Extract the archive file into an appropriate location for your applications, eg: /opt. Use the filename of your downloaded archive, in my example android-studio-ide-143.2821654-linux.zip

    sudo unzip android-studio-ide-143.2821654-linux.zip -d /opt

To launch Android Studio, navigate to the /opt/android-studio/bin directory in a terminal and execute ./studio.sh

After change PATH

    vim ~/.bashrc

And add lines:

    export PATH=${PATH}:/path-to-android-sdk/tools
    export PATH=${PATH}:/path-to-android-sdk/platform-tools

### Smart Git

Canonical Partner's repository must be enabled for installation via terminal:

Installation

    sudo apt install -y smartgit

Or download from http://www.syntevo.com/smartgit/download install and run /usr/share/smartgit/bin/smartgit.sh


### FileZilla

Installation

    sudo apt install -y filezilla

### Spotify

Installation

    sudo sh -c 'echo "deb http://repository.spotify.com testing non-free" >> /etc/apt/sources.list.d/spotify.list'
    sudo apt update && sudo apt install -y spotify-client

### TeamViewer

Download from http://www.teamviewer.com/en/download/linux.aspx

### Meld Diff Tool

    sudo apt install -y meld

### Vagrant

To install Vagrant, you need to download and run the installation kit.
Before going further, be sure that you have dpkg and Virtual box installed:

    sudo apt install -y dpkg-dev virtualbox-dkms

Make sure linux headers already installed

    sudo apt install -y linux-headers-$(uname -r)

Go to the http://downloads.vagrantup.com page of Vagrant and check for the latest release.
After download latest

    wget https://releases.hashicorp.com/vagrant/VERSION/vagrant_VERSION_x86_64.deb
    dpkg -i vagrant_VERSION_x86_64.deb

Reconfigure the VirtualBox DKMS:

    sudo dpkg-reconfigure virtualbox-dkms

### Docker

Installation

    wget -qO- https://get.docker.com/ | sh

Working with Docker is a pain if your user is not configured correctly, so add your user to the docker group with the following command.

    sudo usermod -aG docker $(whoami)

Log out and log in from your server to activate your new groups.

    sudo apt -y install python-pip
    sudo pip install docker-compose

### Audacious Audio Player

Installation

    sudo apt install -y audacious


### XnViewMP

XnView MP is the enhanced version of XnView Classic.
It is a powerful cross-platform media browser, viewer and converter.
Compatible with more than [500 formats](http://www.xnview.com/en/xnviewmp/#formats) such as PSD etc.

Download and install from http://www.xnview.com/en/xnviewmp/#downloads

### Sticky Notes
Just like Google Keep and Windows Sticky Notes, it allows you to jot down thoughts, lists, and reminders on desktop.

Installation

    sudo apt-add-repository ppa:umang/indicator-stickynotes
    sudo apt update && sudo apt install -y indicator-stickynotes

### Guake
Guake is a dropdown terminal made for the GNOME desktop environment.
Guake's style of window is based on an FPS game, and one of its goals is to be easy to reach.

Installation

    sudo apt install -y guake

### Skype

Installation

    sudo apt install -y skype


While we're at it, let's also fix Skype on 64bit not using the correct theme,
by installing the missing dependencies using the following command:

    sudo apt install -y gtk2-engines-murrine:i386 gtk2-engines-pixbuf:i386


### Telegram

Add repository

    sudo add-apt-repository -y ppa:atareao/telegram


Installation

    sudo apt update && sudo apt install -y telegram


### Slack

Canonical Partner's repository must be enabled for installation via terminal:

    sudo apt install -y slack-desktop

Or download from https://slack.com/downloads and run manually


### Gimp

Installation

    sudo add-apt-repository -y ppa:otto-kesselgulasch/gimp

After run:

    sudo apt update && sudo apt install -y gimp gimp-data gimp-plugin-registry gimp-data-extras

### Httpie
You can easily use httpie from terminal: ```http get https://google.com```

Installation

    sudo apt update && sudo apt install -y httpie



### USB Maker for Windows ISO on Linux
You can easily use `Startup Disk Creator` and `UNetbootin` to create Linux to USB. But if you need Windows to USB from your Linux OS use Win USB:

    sudo add-apt-repository -y ppa:colingille/freshlight
    sudo sh -c "sed -i 's/wily/vivid/g' /etc/apt/sources.list.d/colingille-ubuntu-freshlight-$(lsb_release -sc).list"
    sudo apt update && sudo apt install -y winusb

We replace the sources.list back to vivid in order to get it to work for ubuntu 15, that is the purpose of the `sed` command.


***
[(Back to top)](#table-of-contents)

## LAMP
Linux Apache MySQL PHP

**- Installation for the following:**
- PHP 5.6 (and Modules)
- PHP 7.0 (and Modules)
- Apache 2 (and Modules + Dynamic hosts)
- Nginx *(Optional)*
- MySQL
- Redis
- and Header Files.

### PHP 5.6
It's important to install **php5-dev** if you want to compile any add-ons later.

    sudo add-apt-repository -y ppa:ondrej/php
    sudo apt update && sudo apt install -y php5 libpcre3-dev php5-cli php5-cgi php5-common php5-mysql php5-curl php5-gd php5-geoip php5-imagick php5-imap php5-json php5-ldap php5-mcrypt php5-memcache php5-memcached php5-sqlite php5-tidy php5-xdebug php5-xmlrpc php5-xsl php5-dev

If you are looking for more PHP modules try:

    sudo apt-cache search php5-


### PHP 7.0
It's important to install **php7.0-dev** if you want to compile any add-ons later.

    sudo add-apt-repository -y ppa:ondrej/php
    sudo apt update && sudo apt install -y php7.0-bz2 php7.0-cgi php7.0-cli php7.0-common php7.0-curl php7.0-dev php7.0-enchant php7.0-fpm php7.0-gd php7.0-gmp php7.0-imap php7.0-intl php7.0-json php7.0-ldap php7.0-mcrypt php7.0-mysql php7.0-odbc php7.0-opcache php7.0-pgsql php7.0-phpdbg php7.0-pspell php7.0-readline php7.0-recode php7.0-sybase php7.0-tidy php7.0-xmlrpc php7.0-xsl php7.0-sqlite3 php7.0-mbstring php7.0-bcmath php7.0-soap php7.0-zip php-xdebug

If you are looking for more PHP modules try:

    sudo apt-cache search php7.0-

### Composer

    curl -sS https://getcomposer.org/installer | php && sudo mv composer.phar /usr/local/bin/composer

Disable XDebug for composer

    sudo phpdismod -s cli xdebug

And add this lines in your .bashrc file:

    # Load xdebug Zend extension with php command
    alias php='php -dzend_extension=xdebug.so'
    # PHPUnit needs xdebug for coverage. In this case, just make an alias with php command prefix.
    alias phpunit='php $(which phpunit)'

### PHPUnit

    wget https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && sudo mv phpunit.phar /usr/local/bin/phpunit

### Apache

#### Apache: Installation

For PHP 5.6

    sudo apt install -y apache2 libapache2-mod-php5

For PHP 7.0

    sudo apt install -y apache2 libapache2-mod-php7.0


Tweak Apache (Remove apache warning about server's fully qualified domain name)

    echo "ServerName localhost" | sudo tee /etc/apache2/conf-available/fqdn.conf
    sudo a2enconf fqdn && sudo service apache2 reload

#### Apache: Enable php-mcrypt & mod_rewrite

Enable mod_rewrite

    sudo a2enmod rewrite

Enable php-mcrypt

For PHP 5

    sudo php5enmod mcrypt && sudo service apache2 restart

For PHP 7

    sudo phpenmod mcrypt && sudo service apache2 restart

If you are looking for more Apache modules try:

    sudo apt-cache search libapache2-mod

#### Apache: Configure dynamic virtualhosts

Enable module ```vhost_alias```

    sudo a2enmod vhost_alias

Next, open /etc/apache2/apache2.conf

    sudo vim /etc/apache2/apache2.conf

Comment line which includes enabled hosts

    #IncludeOptional sites-enabled/*.conf

and add the following lines to the bottom of file.

    UseCanonicalName Off

    LogFormat "%V %h %l %u %t \"%r\" %s %b \"%{Referer}i\" \"%{User-Agent}i\"" dynamic_vhosts
    CustomLog ${APACHE_LOG_DIR}/access.log dynamic_vhosts

    <VirtualHost *:80>
        VirtualDocumentRoot /var/www/domains/%-2+/public_html
        VirtualScriptAlias  /var/www/domains/%-2+/cgi-bin

        <Directory /var/www/domains>
                    DirectoryIndex index.html index.php
                    Options Indexes FollowSymLinks MultiViews
                    AllowOverride All
                    Order allow,deny
                    allow from all
                    Require all granted
        </Directory>

    </VirtualHost>

This sets up a catch all for any domain coming in over port 80 (the default port for http traffic, if your using https you will need to use 443 - alternatively you could remove the port restriction).
The important line here is the VirtualDocumentRoot. The tells Apache where your files will reside on disk.
The %0 part takes the whole domain name and inserts it into the path. But I didn't want to have the .dev part of the domain in my folders on disk, otherwise we use %-2+
To illustrate this if we went to a domain testing.com.dev the VirtualDocumentRoot would be:

    /var/www/html/domains/testing.com

If you have internet access, no need to add *.dev domains to your hosts file (/etc/hosts), anyway works perfectly.

But if .dev domains not works, you can add automatic .dev domain resolving on your local machine:

    sudo vim /etc/NetworkManager/dnsmasq.d/dev-tld

And enter:

    local=/dev/
    address=/dev/127.0.0.5

The first command says *.dev requests can't be forwarded to your real DNS server.
The second says *.dev resolves to 127.0.0.5 which is localhost.

And restart network-manager:

    sudo service network-manager restart

### Nginx
Or if you prefer to use nginx

For stable version

    sudo add-apt-repository -y ppa:nginx/stable

For latest (recommended)

    sudo add-apt-repository -y ppa:nginx/development

And after install

    sudo apt update && sudo apt install -y nginx


### MySQL

    sudo apt install -y mysql-server mysql-client
    sudo sed -i 's/bind-address/bind-address = 0.0.0.0#/' /etc/mysql/my.cnf

### MyCLI
This is a very nice utility [https://github.com/dbcli/mycli](https://github.com/dbcli/mycli)

    pip install mycli

Usage (See the documents from the git link above for more example):

    mycli -h localhost -u root
    mycli -h localhost -u root -p

### Redis
Install redis latest stable version

    sudo add-apt-repository -y ppa:chris-lea/redis-server
    sudo apt update && sudo apt install -y redis-server

### Memcached

    sudo apt install -y memcached php-memcached

### Java Runtime

    sudo apt install -y default-jre

### Phalcon

    sudo apt-add-repository ppa:phalcon/stable
    sudo apt update
    sudo apt install -y php5-phalcon

### Phalcon Dev Tools
This is an easy to use install script that will cleanup after itself. It can also be used for updating:

    sudo bash install_phalcon_devtools.sh

To test it run: `$ phalcon`

### Secure Permissions
We will use the Access Control Lists (ACL) or (Filesystem Access Control List). We will use group permissions for folders so you don't have to make the public writable, because `777` is dangerous.

    # Make sure you have ACL installed
    sudo apt install -y acl

Look for your main partition with:

    $ df


Mine happens to be `dev/root`, yours may be `dev/sda` or something. Make sure to replace that below:

    # T
    sudo /sbin/tune2fs -o +acl /dev/root

To see what file system you are using `ext3`, `ext4`, etc, use the partition:

    sudo file -sL /dev/root

We have to put the partition in read-only mode, then remount it:

    sudo /bin/mount -o remount /dev/root

Apply Group

    # This sets the Defaults
    setfacl -Rd g:www-data:rw /var/www
    # This sets future file
    setfacl -Rm g:www-data:rw /var/www

To Modify

    setfacl -Rm g:www-data:rw /var/www

Otherwise you could always set up a crontab such as:

    crontab -e

Then append this to run every five minutes.

    */5 * * * * /home/longman/backup.sh chgrp -R www-data /var/www && chmod g+rw /var/www

Lastly, you could have a deploy script that does this for you, such as Python `Fabfile`, but that's another topic.


***

[(Back to top)](#table-of-contents)

## Python

**- Installation packages:**
    - Pip
    - Virtualenv

Python is installed by default on Ubuntu, version 2.7 is suitable. I strongly recommend installing `python-dev` for headers to compile certain PIP packages.

    sudo apt install -y python-dev libmysqlclient-dev
    sudo apt install -y python-pip
    sudo pip install fabric virtualenv virtualenvwrapper django

Manually install Python. python installation required packages

    sudo apt -y install build-essential checkinstall
    sudo apt -y install libreadline-gplv2-dev libncursesw5-dev \
                                 libsqlite3-dev tk-dev libgdbm-dev libc6-dev
    sudo apt -y install libjpeg-dev libpng-dev
    sudo apt -y install zlib1g-dev libbz2-dev
    sudo apt -y install krb5-multidev
    sudo apt -y install openssl libssl-dev
    sudo apt -y install libffi-dev
    sudo apt -y install libgmp-dev

Download and extract Python using following command from [python](#python) official site. You can also download latest(3.6.0) version in place of specified below.

    wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz && tar -xvf Python-3.5.2.tgz
    sudo mv Python-3.5.2 /opt/ && cd /opt && cd Python-3.5.2

Use below set of commands to compile python source code on your system using altinstall.

    ./configure
    make
    sudo make altinstall

Check the Python version installed, using below command

    python3.5 -V

### Pip
[Pip](#pip) is a tool for installing and managing Python packages. Install Pip with Wget and Python.

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.5 get-pip.py

View a list of helpful commands

    pip --help

Check the version of Pip that is installed

    pip -V

### Virtualenv
[Virtualenv](#virtualenv) is a tool to create isolated Python environments. install the virtualenv package

    pip install virtualenv

Create an Environment with virtualenv

    virtualenv -p python3.5 --no-site-packages env

Activate script

    cd env
    source bin/activate

Deactivate

    deactivate

***
[(Back to top)](#table-of-contents)

## Ruby
Install Ruby 2.X with header files in `ruby2.0-dev`, this will keep your gems from having issues.

    sudo apt install -y ruby2.0 ruby2.0-dev

For Ruby RVM (Version Management)

    gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
    \curl -sSL https://get.rvm.io | bash -s stable

***
[(Back to top)](#table-of-contents)

## NodeJS
I am using a PPA to fix the nodejs path issue(s)

    curl -sL https://deb.nodesource.com/setup_5.x | sudo -E bash -
    sudo apt install -y nodejs
    sudo chown -R $(whoami) ~/.npm
    sudo npm install bower gulp grunt-cli webpack -g

If installing coffee-script and typing `$ coffee` produces an error, make sure coffee is not within the $PATH

    echo $PATH

***
[(Back to top)](#table-of-contents)

# Customizations

## System Tweaks

### Increase Inotify Watches Limit

Open ```sysctl.conf```

    sudo vim /etc/sysctl.conf

Add this line:

    fs.inotify.max_user_watches = 524288

And after run

    sudo sysctl -p

### Disable Git Certificate Verification

For security reasons, not recommended

    sudo git config --global http.sslVerify false


## Shortcuts

- "System Settings" > "Keyboard" > "Shortcuts" > "Custom Shortcuts" <kbd>ctrl</kbd>+<kbd>r</kbd> Terminal ```gnome-terminal```
- "System Settings" > "Keyboard" > "Shortcuts" > "Custom Shortcuts" <kbd>ctrl</kbd>+<kbd>e</kbd> Files ```nautilus -w```

## VIM Customization

**Setup VIM**

    git clone https://github.com/gmarik/Vundle.vim.git ~/.vim/bundle/Vundle.vim

And copy [.vimrc](os/home/.vimrc) file in your home folder (/home/USERNAME/.vimrc)
After run

    $ vim
    :PluginInstall

## Enable Auto Focus on Opened Applications
In CompizConfig go to "General Options" > "Focus & Raise Behaviour" and set "Focus Prevention Level" to "Off"

## Enable Normal Scrollbars

    gsettings set com.canonical.desktop.interface scrollbar-mode normal

To revert

    gsettings reset com.canonical.desktop.interface scrollbar-mode

## Enable User Name in Systray

    gsettings set com.canonical.indicator.session show-real-name-on-panel true

## Change Datetime Format in Systray
Open dconf-editor and go ```com > canonical > indicator > datetime``` Change time format to CUSTOM and time format type ```%a, %e %b %H:%M %```

## Enable Minimize App on Dash Click
Open Compizconfig and go to "Desktop" > "Ubuntu Unity Plugin" > "Launcher Tab" and enable "Minimize Single Windows Applications (Unsupported)"

## Disable Window Grouping
Open Compizconfig and scroll down to "Ubuntu Unity Plugin".
Choose the tab "Switcher". Disable the alt-tab and shift-alt-tab key bindings.
("Key to start the switcher" and "Key to switch to the previous window in the Switcher".
Click the "Back" button. Scroll down to the "Window management" section.
Here you can select another switcher. I enable the "Static Application Switcher", resolve any potential conflicts by setting the setting for "Static Application Switcher".
Now you can tweak the switcher by clicking on it.
I have changed <kbd>alt</kbd>+<kbd>tab</kbd> and <kbd>shift</kbd>+<kbd>alt</kbd>+<kbd>tab</kbd> to "Next window (All windows)" and "Prev window (All windows)"

## Install Custom Wallpaper

For ```convert``` command you need install package ```imagemagick```

    mkdir ~/Pictures/Wallpapers
    sudo convert ~/Dropbox/images/DSM.jpg ~/Pictures/Wallpapers/DSM.png
    gsettings set org.gnome.desktop.background picture-uri file:///home/longman/Pictures/Wallpapers/DSM.png


## Change Greeter Background

Copy image to ```/usr/share/backgrounds```

    sudo cp ~/Pictures/Wallpapers/DSM.png /usr/share/backgrounds

Check permissions of your file

And after open theme file

    sudo vim /usr/share/glib-2.0/schemas/com.canonical.unity-greeter.gschema.xml

Find the key name ```background``` and change the default to the path of your picture in "/usr/share/backgrounds/".
For the key name ```draw-user-backgrounds```, change the default value to ```false```.

## Add Georgian Keyboard

Go to System "Settings" > "Keyboard" > "Text Entry" and add Georgian layout. Also enable "Allow different sources for each window"

***
[(Back to top)](#table-of-contents)


# Ubuntu Fixes
These are solutions to fix problems I've encountered.

## Sound Indicator Not Showing
This appears in the top-right menu on Unity. Tested in 14/15.

This will also fix Tweak UI if a sound item is missing.

    sudo apt install -y indicator-sound

For Unity (Default)

   killall unity-panel-service

For Gnome

    killall gnome-panel

# Install Gnome 3
If you prefer Gnome 3 over the Unity desktop it's easy to install:

    sudo apt install -y ubuntu-gnome-desktop
    sudo service gdm restart (Or a reboot is easier)

Unity uses `lightdm` and Gnome uses `gdm`, it's easiest to stick with lightdm.

If you want the default login a certain one select either lightdm or gdm. If you want to change it later run:

    sudo dpkg-reconfigure gdm

## Easy Window Resize
Without Compiz, you can resize windows very nicely:
- Focus on a window
- Hold <kbd>ALT</kbd> + Middle Mouse Click + Drag
- Note: Depending on where you position your mouse to will resize up/down/left/right

## Left or Right Close Buttons
Run this simple command in the terminal and you will see the positions change right away.

Move to right (terminal)

    gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'

Move to left (terminal)

    gsettings set org.gnome.desktop.wm.preferences button-layout 'close,minimize,maximize:'


## Fix Gnome Lockscreen
In terminal make sure this is false, then try your hotkey `ctrl+alt+l` or if you set it like min `super+l` in the settings:

    gsettings set org.gnome.desktop.lockdown disable-lock-screen 'false'

## My Gnome Extensions
You need to use **Firefox** or **IceWeasle** at https://extensions.gnome.org/ to toggle these items. I suggest creating an account so you have a record.

- **Must Have Extensions**
- [Dash to Dock](https://extensions.gnome.org/extension/307/dash-to-dock/) :star::star::star::star::star:
- [Workspace Dock](https://extensions.gnome.org/extension/427/workspaces-to-dock/) :star::star::star::star:
- [Applications Menu](https://extensions.gnome.org/extension/6/applications-menu/) :star::star::star::star::star:
- [TaskBar](https://extensions.gnome.org/extension/584/taskbar/) :star::star::star::star::star:
- [No Topleft Hot Corner](https://extensions.gnome.org/extension/118/no-topleft-hot-corner/) :star::star::star::star::star:
- [Force Quit](https://extensions.gnome.org/extension/770/force-quit/) :star::star::star::star::star:
- **Nice Extensions**
- [Taskbar](https://extensions.gnome.org/extension/584/taskbar/) :star::star::star::star::star:
- [Small Panel Icon](https://extensions.gnome.org/extension/861/small-panel-icon/) :star::star::star::star::star:
- [Top Icons](https://extensions.gnome.org/extension/495/topicons/) :star::star::star::star:
- [MMOD Panel](https://extensions.gnome.org/extension/898/mmod-panel/) :star::star::star::star::star:
- [Keyboard Modifiers Status](https://extensions.gnome.org/extension/975/keyboard-modifiers-status/) :star::star::star:
- [Laine](https://extensions.gnome.org/extension/937/laine/) :star::star::star::star:
- [Disable Workspace Switcher Popup](https://extensions.gnome.org/extension/959/disable-workspace-switcher-popup/) :star::star:
- [Refresh Wifi Connections](https://extensions.gnome.org/extension/905/refresh-wifi-connections/) :star::star::star::star:
- [Disconnect Wifi](https://extensions.gnome.org/extension/904/disconnect-wifi/) :star::star::star::star::star:
- [Toggle Touchpad](https://extensions.gnome.org/extension/935/toggle-touchpad/) (For Laptops) :star::star::star::star::star:


## Reload Gnome Freeze
This is a rare things for me, it happens much more in unity and requires a lot more "damaging" things. To fix a gnome that seems frozen do the following:

<kbd>ALT + F2</kbd> enter in <kbd>r</kbd> (lowecase) and press <kbd>Enter</kbd>


***
[(Back to top)](#table-of-contents)

# Adjust Mouse and Devices
When using a USB mouse sometimes the speed is just not right, in my case it's too slow often. Here is how to adjust it:

    xinput --list

I get something like this:

    ⎡ Virtual core pointer                      id=2    [master pointer  (3)]
    ⎜   ↳ Virtual core XTEST pointer                id=4    [slave  pointer  (2)]
    ⎜   ↳ ETPS/2 Elantech Touchpad                  id=15   [slave  pointer  (2)]
    ⎜   ↳ Logitech Unifying Device. Wireless PID:101b   id=12   [slave  pointer  (2)]
    ⎣ Virtual core keyboard                     id=3    [master keyboard (2)]
        ↳ Virtual core XTEST keyboard               id=5    [slave  keyboard (3)]
        ↳ Power Button                              id=6    [slave  keyboard (3)]
        ↳ Video Bus                                 id=7    [slave  keyboard (3)]
        ↳ Power Button                              id=8    [slave  keyboard (3)]
    ...

The ID of my mouse is `12`.
You can see all the properties with:

    $ xinput --list-props 12

Then you can adjust the settings the String value and a value at the end:

    $ xinput --set-prop 12 "Device Accel Constant Deceleration" 2

## Preserve Settings

To keep the settings in Gnome, do the following:

    $ cd ~
    $ touch gnome-boot.sh && chmod +x gnome-boot.sh

Example of `gnome-boot.sh` file (Note: You can call it whatever you like):

    #!/bin/bash
    xinput --set-prop 12 "Device Accel Constant Deceleration" 4


Then Add the Bash script the Gnome Session:

    $ gnome-session-properties


***
[(Back to top)](#table-of-contents)

# Virtual Machine Related

This has to do with VirtualBox

## Fix Mouse Side Buttons in VMWare
Append the following to `yourbox.vmx` with the machine off.

    mouse.vusb.enable = "TRUE"
    mouse.vusb.useBasicMouse = "FALSE"
    usb.generic.allowHID = "TRUE"

## Vagrant VBGuest Fix:

    vagrant plugin install vagrant-vbguest

    vagrant ssh
    sudo ln -s /opt/VBoxGuestAdditions-4.3.10/lib/VBoxGuestAdditions /usr/lib/VBoxGuestAdditions


## Windows 8 VirtualBox Fix
Running Windows 8 in Virtualbox has an odd error, run this in `cmd` or `powershell`, or `terminal` on linux.

    vboxmanage list vms
    vboxmanage setextradata "The Box Name" VBoxInternal/CPUM/CMPXCHG16B 1

***

[(Back to top)](#table-of-contents)


# Synchronize Configurations

## Sync Sublime Text
I am using Dropbox for syncing configurations

Install Package Control https://packagecontrol.io/installation#st3

After:

    cd ~/.config/sublime-text-3/Packages/
    rm -rf User
    ln -s ~/Dropbox/workspace/appdata/sublime-text-3/Packages/User


## Sync FileZilla

    cd ~/.config/filezilla
    rm -f sitemanager.xml
    ln -s ~/Dropbox/workspace/appdata/filezilla/sitemanager.xml


# Chrome Addons

- [Chroma Color Picker](https://chrome.google.com/webstore/detail/chroma/gefgglgjdlddcpcapigheknbacbmmggp?utm_source=chrome-app-launcher-info-dialog)
- [Advanced REST client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo?utm_source=chrome-app-launcher-info-dialog)
- [Docs PDF/PowerPoint Viewer](https://chrome.google.com/webstore/detail/docs-pdfpowerpoint-viewer/nnbmlagghjjcbdhgmkedmbmedengocbn?utm_source=chrome-app-launcher-info-dialog)
- [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc?utm_source=chrome-app-launcher-info-dialog)
- [LastPass: Free Password Manager](https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd?utm_source=chrome-app-launcher-info-dialog)
- [New Tabs At End](https://chrome.google.com/webstore/detail/new-tabs-at-end/bgogjfbkjgjhonhikkkflpkgpcpfljoa?utm_source=chrome-app-launcher-info-dialog)
- [Octotree](https://chrome.google.com/webstore/detail/octotree/bkhaagjahfmjljalopjnoealnfndnagc?utm_source=chrome-app-launcher-info-dialog)
- [Recently Closed Tabs](https://chrome.google.com/webstore/detail/recently-closed-tabs/opefiliglgllmponlmoajkfbcaigocfc?utm_source=chrome-app-launcher-info-dialog)
- [User-Agent Switcher for Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg?utm_source=chrome-app-launcher-info-dialog)

***

[(Back to top)](#table-of-contents)

# Other Applications
- [DragonDisk](http://www.dragondisk.com/) S3
- Kazam (Screen Recorder)
- Shutter
- gnome-system-tools
- Terminator
- Gdeb
- MySQL Workbench
- Bleachbit (Trash Cleaner)
- Preload (Intelligent Bootup Time)

***

[(Back to top)](#table-of-contents)

# Clean System

Remove not neccessary apps from startup

Show system apps in Startup Applications

    sudo sed -i 's/NoDisplay=true/NoDisplay=false/g' /etc/xdg/autostart/*.desktop

Open "Startup Applications" and uncheck apps: Chat, Orca Screen Reader, Zeitgest Datahub

Hide system apps

    sudo sed -i 's/NoDisplay=false/NoDisplay=true/g' /etc/xdg/autostart/*.desktop

Remove Amazon from dash

    sudo apt purge unity-webapps-common

Remove rythmbox audio player

    sudo apt purge rhythmbox

Remove Totem video player

    sudo apt purge totem

Clean System

    sudo apt autoremove
    sudo apt clean
    sudo apt autoclean


***

[(Back to top)](#table-of-contents)


By [Avtandil Kikabidze aka LONGMAN](https://github.com/akalongman)