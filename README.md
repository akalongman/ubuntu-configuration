# Configuration of Ubuntu 20.04 LTS (Focal Fossa)

This guide is for [Ubuntu](http://ubuntu.com/desktop), but also compatible with a other __Debian__ based OS as well, like [Mint](http://www.linuxmint.com/), [Elementary OS](http://elementaryos.org/), etc.

There are configurations for other versions such as [18.04](tree/18.04), [16.04](tree/16.04), [15.10](tree/15.10)

All commands/configurations are tested (I am currently use this configuration), but anyway, everything you do is "at your own risk".

If you found any issue, please let me know on [Issues Page](https://github.com/akalongman/ubuntu-configuration/issues) or via email akalongman@gmail.com

***

# Table of Contents
- [Optional Configurations](#optional-configurations)
    - [Get System Details](#get-system-details)
        - [Operating System](#operating-system)
        - [CPU Info](#cpu-info)
        - [VGA Info](#vga-info)
        - [Motherboard Info](#motherboard-info)
        - [BIOS Info](#bios-info)
        - [Memory and Usage Info](#memory-and-usage-info)
        - [Disks](#disks)
        - [GUI Processes](#gui-processes)
        - [Startup Times](#startup-times) (Find out the Culprit of a Slow Boot)
        - [Packages](#packages)
        - [Other Commands](#other-commands)
            - [Screenshots](#screenshots)
            - [Print Power Consumption in Watts](#print-power-consumption-in-watts)
    - [List all KeyBindings](#list-all-keybindings)
    - [Use 32Bit on 64bit](#use-32bit-on-64bit)
    - [Networking](#networking)
    - [Order of Grub](#order-of-grub)
    - [Mounting Drives](#mounting-drives)
        - [Mounting of Local Drives](#mounting-of-local-drives)
        - [Mounting of Network Drives](#mounting-of-network-drives)
        - [Mounting Amazon Cloud Drive](#mounting-amazon-cloud-drive)
    - [SSH](#ssh)
        - [Generate a New SSH Key](#generate-a-new-ssh-key)
        - [Connecting to a Host](#connecting-to-a-host)
        - [.ssh Folder Permissions](#ssh-folder-permissions)
        - [Using the Config File](#using-the-config-file)
        - [Convert SSH to PEM](#convert-ssh-to-pem)
    - [GPG](#gpg)
        - [Generate a New GPG Key](#generate-a-new-gpg-key)
        - [Generate ASCII Armored Version of Public Key](#generate-ascii-armored-version-of-public-key)
        - [Uploading The Key to Ubuntu Keyserver](#uploading-the-key-to-ubuntu-keyserver)
        - [Signing Git Commits Using GPG](#signing-git-commits-using-gpg)
        - [Backup The GPG Key](#backup-the-gpg-key)
        - [Restore The GPG Key](#restore-the-gpg-key)
    - [Enable Native Virtualization](#enable-native-virtualization)
    - [Format USB](#format-usb)
    - [Write iso Image to USB](#write-iso-image-to-usb)
    - [Convert .ISO to .IMG format](#convert-iso-to-img-format)
    - [Add Printers](#add-printers)
        - [HP](#hp)
    - [Update BIOS on Laptop/PC](#update-bios-on-laptoppc)
        - [Lenovo](#update-bios-on-lenovo)
    - [Sniff Local Traffic](#sniff-local-traffic)
    - [Play Sound Through Multiple Outputs](#play-sound-through-multiple-outputs)
    - [Terminal Prompt Customization](#terminal-prompt-customization)
    - [Set CPU Governor to Performance](#set-cpu-governor-to-performance)
    - [Run Script on System Startup](#run-script-on-system-startup)
    - [Manage Swap](#manage-swap)
    - [Install Fonts](#install-fonts)
- [Installation Packages](#installation-packages)
    - [Enable PPAs](#enable-ppas)
    - [Flatpak](#flatpak)
    - [System Tools](#system-tools)
        - [Install Nvidia Drivers](#install-nvidia-drivers) (Install drivers from official repository for Nvidia Drivers)
        - [Install Nvidia Cuda Toolkit](#install-nvidia-cuda-toolkit) (Install CUDA toolkit from official repository for Nvidia)
        - [Install ATI Drivers](#install-ati-drivers)
        - [Utilities](#utilities)
        - [RedShift For Eye Strain](#redshift-for-eye-strain) (Redshift adjusts the color temperature of your screen according to your surroundings)
        - [Dark Theme](#dark-theme)
        - [Oracle Java](#oracle-java)
        - [Wine](#wine) (Windows emulator) (Run Microsoft® Windows® applications on linux)
        - [Nautilus-Actions](#nautilus-actions) (Graphically create custom context menu options for Ubuntu's Nautilus file manager)
        - [Hardinfo](#hardinfo) (Everest/Aida alternative for linux)
        - [Caffeine](#caffeine) (Prevent the activation of the screensaver when using full-screen windows)
        - [GNU Screen](#gnu-screen) (Full-screen window manager that multiplexes a physical terminal between several processes)
        - [Neofetch](#neofetch) (A fast, highly customizable system info script)
        - [GParted](#gparted) (Partition editor for graphically managing disk partitions)
        - [Firewall](#firewall)
            - [UFW](#ufw)
            - [GUFW](#gufw)
        - [Geekbench](#geekbench) (Geekbench 5 is a cross-platform benchmark that measures your system's performance with the press of a button)
        - [Clonezilla](#clonezilla) (Clonezilla is a partition and disk imaging/cloning program. It helps you to do system deployment, bare metal backup and recovery.)
        - [Screen Testing Soft](#screen-testing-soft) (This is a program for testing the quality of CRT/LCD screens. It displays various patterns and allows you to estimate the quality of your CRT/LCD monitor.)
        - [Ventoy](#ventoy) (Open source tool to create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI files. You can copy many files at a time and ventoy will give you a boot menu to select them.)
    - [Other Tools](#other-tools)
        - [Google Chrome](#google-chrome)
        - [PlayOnLinux](#playonlinux) (Software which using wine allows you to easily install and use numerous games and apps designed to run with Microsoft® Windows®)
        - [Dropbox](#dropbox) (Allows users to create a special folder on their computers, which Dropbox then synchronizes so that it appears to be the same folder (with the same contents) regardless of which device is used to view it)
        - [Sublime Text 3](#sublime-text-3) (A sophisticated text editor for code, markup and prose)
        - [Pidgin](#pidgin)
        - [DBeaver](#dbeaver) (Database management tool)
        - [VirtualBox](#virtualbox)
        - [Android Studio](#android-studio)
        - [SmartGit](#smart-git)
        - [FileZilla](#filezilla) (sFTP Client)
        - [Spotify](#spotify)
        - [Google Music Player](#google-music-player)
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
        - [Viber](#viber)
        - [Gimp](#gimp)
        - [VLC Player](#vlc-player)
        - [KDEnlive Video Editor](#kdenlive-video-editor)
        - [Httpie](#httpie) (Terminal HTTP client)
        - [Peek](#peek) (Simple animated GIF screen recorder with an easy to use interface)
        - [OBS](#obs) (Video recording and live streaming)
        - [USB Maker for Windows ISO on Linux](#usb-maker-for-windows-iso-on-linux)
        - [StarUML](#staruml) (A sophisticated software modeler for agile and concise modeling)
        - [Gramps](#gramps) (A geneological tree manager)
        - [uGet](#uget) (A download manager)
    - [Development](#development)
        - [LAMP](#lamp)
            - [PHP](#php)
                - [PHP 5.6](#php-56)
                - [PHP 7.0](#php-70)
                - [PHP 7.1](#php-71)
                - [PHP 7.2](#php-72)
                - [PHP 7.3](#php-73)
                - [PHP 7.4](#php-74)
                - [PHP 8.0](#php-80)
                - [Switch PHP Versions](#switch-php-versions)
            - [Composer](#composer)
            - [PHPUnit](#phpunit)
            - [Apache](#apache)
                - [Installation](#apache-installation)
                - [Enable php-mcrypt](#apache-enable-php-mcrypt)
                - [Configure Dynamic Virtualhosts](#apache-configure-dynamic-virtualhosts)
                - [Configure SSL for Dynamic Virtualhosts](#apache-configure-ssl-for-dynamic-virtualhosts)
            - [Nginx](#nginx)
            - [Generate SSL certificates for local domains](#generate-ssl-certificates-for-local-domains)
            - [MySQL](#mysql)
            - [Percona Toolkit](#percona-toolkit)
            - [MyCLI](#mycli) Terminal MySQL Utility
            - [PostgreSQL](#postgresql)
            - [Memcached](#Memcached)
            - [Redis](#redis)
                - [Multiple Redis Instances](#multiple-redis-instances)
            - [ELK Stack](#elk-stack) ELK Stack: Elasticsearch, Logstash, and Kibana
            - [Letsencrypt](#letsencrypt)
            - [Phalcon](#phalcon)
            - [Phalcon Dev Tools](#phalcon-dev-tools)
            - [Secure Permissions](#secure-permissions)
        - [Python](#python)
            - [Pip](#pip)
            - [Virtualenv](#virtualenv)
        - [Go](#go)
        - [Ruby](#ruby)
        - [NodeJS](#nodejs)
        - [Yarn](#yarn)
        - [Ansible](#ansible)
    - [Gaming](#gaming)
        - [Steam](#steam) (Ultimate entertainment platform)
        - [PCSXR](#pcsxr) (PlayStation 1 Emulator)
- [Customizations](#customizations)
    - [System Tweaks](#system-tweaks)
        - [Increase Inotify Watches Limit](#increase-inotify-watches-limit)
        - [Disable Git Certificate Verification](#disable-git-certificate-verification)
    - [Shortcuts](#shortcuts)
    - [VIM Customization](#vim-customization)
    - [Add Georgian Keyboard](#add-georgian-keyboard)
- [Ubuntu Fixes](#ubuntu-fixes)
    - [Ubuntu Infinite Login](#ubuntu-infinite-login)
    - [PCI Device Is Not Recognized Correctly](#pci-device-is-not-recognized-correctly)
    - [Restore Screen Brightness and Keyboard backlit on Reboot](#restore-screen-brightness-and-keyboard-backlit-on-reboot)
    - [Disable UEFI Choice Screen](#disable-uefi-choice-screen)
- [GUI](#gui)
    - [Move Dock To Bottom](#move-dock-to-bottom)
    - [Easy Window Resize](#easy-window-resize)
    - [Left or Right Close Buttons](#left-or-right-close-buttons)
    - [Fix Gnome Lockscreen](#fix-gnome-lockscreen)
    - [Gnome Extensions](#gnome-extensions)
    - [Reload Gnome Freeze](#reload-gnome-freeze)
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

    sudo dmidecode -t processor
    
Or

    nproc               # How many Processing Units
    cpuid               # Must install cpuid from terminal
    cat /proc/cpuinfo   # Lots of info

#### VGA Info

    sudo lshw -C display

#### Motherboard Info

    sudo dmidecode -t baseboard

#### BIOS Info

    sudo dmidecode -t bios

#### Memory and Usage Info

    free -h             # Human readable, or do --help for options
    top or htop         # Must install htop
    vmstat -s
    cat /proc/meminfo   # Lots of info

#### Disks
Disk Space

    df
    df -B MB    # In Megabtyes,  etc

Or install `ncdu` and run 

    ncdu /

Disks UUID

    ls -al /dev/disk/by-uuid/

#### GUI Processes

    gnome-system-monitor

#### Startup Times
You can find out which service takes how much time to finish 
starting up by entering the following command in terminal:

    systemd-analyze blame

Overall startup time you can find via:

    systemd-analyze time

#### Packages

List all installed Packages

    dpkg -l

List only packages which were expressly installed

    aptitude search '~i!~M'

#### Other Commands

##### Screenshots
To taking screenshot from terminal run this:

    gnome-screenshot

With delay 5 seconds

    gnome-screenshot --delay 5

With delay 5 seconds and only window

    gnome-screenshot -w --delay 5

For changing default save directory for gnome-screenshot, use the command

    gsettings set org.gnome.gnome-screenshot auto-save-directory "file:///home/$USER/Pictures/"

##### Print power consumption in watts

    awk '{print $1*10^-6 " W"}' /sys/class/power_supply/BAT0/power_now

Also, you can install `powertop` for listing consumption per process.

    sudo apt install powertop

You might need calibrate `powertop` before first use. For calibrate, run:

    sudo powertop --calibrate

## List all Keybindings

    gsettings list-recursively  org.gnome.desktop.wm.keybindings | sort | more

See your keypressed:

    xev

Or for a lot of details:

    xev | grep KeyPress

## Use 32Bit on 64bit

You can use 32Bit applications if you like, sometimes this is useful.

    sudo apt update && sudo apt install -y unetbootin

## Networking

To enable Networking, and make it accessible to all computers such as Windows also, first install Samba:

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

    username@remote_address:/remote/path /local/path fuse.sshfs delay_connect,_netdev,idmap=user,uid=1000,gid=1000,noatime,default_permissions,IdentityFile=/home/<user>/.ssh/id_rsa,reconnect,transform_symlinks,allow_other 0 0

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


## SSH

### Generate a New SSH Key

    ssh-keygen -t rsa -C "your_email@example.com"

### Connecting to a Host

    ssh user@host.com  (default port is 22)
    ssh user@host.com -p 8000 (connect to specific port)
    ssh user@host.com -i ~/.ssh/id_rsa (connect with specific ssh key)

### .ssh Folder Permissions

    chmod 700 ~/.ssh
    chmod 644 ~/.ssh/id_rsa.pub
    chmod 600 ~/.ssh/id_rsa
    chmod 600 ~/.ssh/known_hosts
    chmod 600 ~/.ssh/authorized_keys

### Using the Config File

You can also create a ~/.ssh/config file and store entries such as:

    Host aws
    Hostname host.amazonaws.com
    Port 22
    Identityfile ~/.ssh/id_rsa
    User myusername
    
    Host my-vps
    Hostname 34.16.67.129
    Port 22
    User root
   
You can then simply type:
    
    ssh aws
    ssh my-vps

### Convert SSH to PEM

Sometimes you may need a PEM format SSH Key. You can easily add this alongside your other SSH keys.

    openssl rsa -in ~/.ssh/keyname_rsa -outform pem > keyname_rsa.pem
    chmod 700 keyname_rsa.pem


## GPG

### Generate a New GPG Key

Open a terminal and type:

    gpg --gen-key
    
GPG will now ask you a number of questions about the type of key you want to generate. 
Follow the steps below to select the default option each time.    
    
Check that your key has been generated by typing 

    gpg --list-secret-keys --keyid-format LONG
    
and, if successful  
    
    /Users/hubot/.gnupg/secring.gpg
    ------------------------------------
    sec   4096R/3AA5C34371567BD2 2016-03-10 [expires: 2017-03-10]
    uid                          Hubot 
    ssb   4096R/42B317FD4BA89E7A 2016-03-10
 
Add variables in your .bashrc
 
    export GPGKEY=3AA5C34371567BD2
     
### Generate ASCII Armored Version of Public Key    
     
    gpg --output gpg.asc --export -a $GPGKEY

### Uploading The Key to Ubuntu Keyserver

    gpg --send-keys --keyserver keyserver.ubuntu.com $GPGKEY
    
You can check your keys on the http://keyserver.ubuntu.com/    
    
### Signing Git Commits Using GPG

To configure your Git client to sign commits by default for a local repository, in Git versions 2.0.0 and above, run 

    git config --global user.signingkey {YOUR KEY}

    git config commit.gpgsign true
    
To sign all commits by default in any local repository on your computer, run 

    git config --global commit.gpgsign true

If you want sign one commit manually:

    git commit -S -m "commit message"

If you want to use GUI clients for committing, you have to add some options to your `~/.gnupg/gpg.conf` file

    no-tty
    use-agent

### Backup The GPG Key

    cp ~/.gnupg/pubring.gpg /path/to/backups/
    cp ~/.gnupg/secring.gpg /path/to/backups/
    cp ~/.gnupg/trustdb.gpg /path/to/backups/
    # or, instead of backing up trustdb...
    gpg --export-ownertrust > ownertrust-gpg.txt
    
### Restore The GPG Key

    cp /path/to/backups/*.gpg ~/.gnupg/
    # or, if you exported the ownertrust
    gpg --import-ownertrust ownertrust-gpg.txt

If you just copy-pasted the .gnupg folder, you should register keys:

    gpg --import pubring.gpg
    gpg --import secring.gpg

## Enable Native Virtualization

Check if supported by hardware

    egrep -c '(vmx|svm)' /proc/cpuinfo

If 0 it means that your CPU doesn't support hardware virtualization.

If 1 or more it does - but you still need to make sure that virtualization is enabled in the BIOS.

To check if enabled, you may execute:

    kvm-ok 

If you have KVM, you will see: "INFO: Your CPU supports KVM extensions INFO: /dev/kvm exists KVM acceleration can be used"

Install Necessary Packages

    sudo apt install -y qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils

Next, add your user to the KVM group and libvirtd group. To do so, type:

    sudo adduser `id -un` libvirt
    sudo adduser `id -un` kvm

Verify Installation:

    virsh list --all

## Format USB

Enter sudo mode

    sudo su

List available disks and detect where it was mounted: /dev/sd[1 letter][optionally 1 number]. For example, /dev/sdc or /dev/sdc1

    fdisk -l

or

    lsblk

Unmount drive

    umount /dev/sd[1 letter][optionally 1 number]


Format to FAT32

    mkfs.vfat /dev/sd[1 letter]

You can use mkfs.ntfs for NTFS, mkfs.ext4 for EXT4 etc.

Eject drive

    eject /dev/sd[1 letter]


## Write iso Image to USB

List available disks and detect where it was mounted: /dev/sd[1 letter][optionally 1 number]. For example, /dev/sdc or /dev/sdc1

    fdisk -l

or

    lsblk

If you want write Windows ISO on the USB, use this method: [USB Maker for Windows ISO on Linux](#usb-maker-for-windows-iso-on-linux)

Make sure the USB device is unmounted (not safely removed, but unmounted) If it is mounted you can unmount it:

    sudo umount /dev/sd[1 letter][optionally 1 number]

For writing image run:

    sudo dd bs=4M if=path/to/your/iso/file.iso of=/dev/sd[that 1 letter]


## Convert .ISO to .IMG format

Install the `genisoimage`

    sudo apt install -y genisoimage

And after run

    geteltorito -o dest.img source.iso


## Add Printers

### HP

You must install HPLIP software. Read more on https://developers.hp.com/hp-linux-imaging-and-printing

    sudo apt install hplip hplip-gui

Find installed HP application and run.

## Update BIOS on Laptop/PC

You can see BIOS version via [BIOS Info](#bios-info) command

### Update BIOS on Lenovo

1. Go to support.lenovo.com (or better use a search engine because the Lenovo website is ugly) 
and search for the BIOS upgrade of your laptop model.

2. Download the most recent ISO file. Look for "BIOS bootable update CD".

3. Convert the ISO image to IMG format via `geteltorito -o bios.img g2uj18us.iso` [Convert .ISO to .IMG format](#convert-iso-to-img-format)

4. Insert any USB stick into your laptop. The image file is just ~50 MB in size so even USB sticks with low capacity will work. 
Keep in mind that the stick will be completely overwritten.

5. If you are in a graphical environment then unmount the USB stick.

6. Find out the device name of the stick. For example `/dev/sdb` (show devices via `sudo fdisk -l`). 
Don't just assume it's sdb. If it's on another device on your laptop then you will destroy your data.

7. Copy the image to the USB stick: `sudo dd if=bios.img of=/dev/sdb bs=1M`

8. Reboot your laptop and press F12 for booting device from your stick.

9. Make sure your laptop has its power supply plugged in. (It will refuse to update otherwise.)

10. Follow the instructions.



## Sniff Local Traffic
BetterCAP is a powerful, flexible and portable tool created to perform various types of MITM attacks against a network, 
manipulate HTTP, HTTPS and TCP traffic in realtime, sniff for credentials and much more. 
Full documentation https://www.bettercap.org

Install dependencies

    sudo apt install -y build-essential ruby-dev libpcap-dev

And install BetterCAP

    sudo gem install bettercap

You can run sniffing via

    sudo bettercap --sniffer

    
## Play Sound Through Multiple Outputs
Install `paprefs` package

    sudo apt install -y paprefs

Go to the `PulseAudio Preferences` and on the `Simultaneous Output` tab check `Add virtual output device for simultaneous output on all local sound cards`

After that restart pulseaudio

    pulseaudio -k

Then go to your sound settings and you will see the option to output to multiple sound devices.

## Terminal Prompt Customization
Put the file [ps.sh](os/etc/profile.d/ps.ssh) under `/etc/profile.d` directory.

In the ~/.bashrc and /root/.bashrc files add line:

    source /etc/profile.d/ps.sh

## Set CPU Governor to Performance

Install `cpufrequtils` and set governor

    sudo apt install -y cpufrequtils
    echo 'GOVERNOR="performance"' | sudo tee /etc/default/cpufrequtils
    sudo systemctl restart cpufrequtils

Disable default ondemand governor:

    sudo systemctl disable ondemand

You can check governor via 

    cpufreq-info

Or:

    cat /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor

## Run Script on System Startup

The below steps will show you to run an example bash script which reports disk space usage of the `/home` directory and saves the report in the `/root` directory every time the Ubuntu system boots.

Create shell script in `/usr/local/bin/` to run on startup.

    vim /usr/local/bin/disk-space-check.sh

The below is an example of such script:

```bash
#!/bin/bash

date > /root/disk_space_report.txt
du -sh /home/ >> /root/disk_space_report.txt
```

Create Systemd service file under `/etc/systemd/system/` folder.

    sudo vim /etc/systemd/system/disk-space-check.service

And put the content:

```
[Unit]
After=network.service

[Service]
ExecStart=/usr/local/bin/disk-space-check.sh

[Install]
WantedBy=multi-user.target
```

Set proper permissions:

    sudo chmod 744 /usr/local/bin/disk-space-check.sh
    sudo chmod 664 /etc/systemd/system/disk-space-check.service

Enable the service unit:

    sudo systemctl daemon-reload
    sudo systemctl enable disk-space-check.service

Systemd helpful commands:

- `systemctl list-units --type=service` List existing services
- `systemctl list-units --type=target` List possible targets
- `systemctl list-dependencies <name>.target` List dependencies for <target>


## Manage Swap

For more modern systems (>1GB), your swap space should be at a minimum be equal to your physical memory (RAM) size "if you use hibernation", 
otherwise you need a minimum of round(sqrt(RAM)) and a maximum of twice the amount of RAM. The only downside to having more swap space than you will actually use, 
is the disk space you will be reserving for it. More you can read [here](https://help.ubuntu.com/community/SwapFaq).

Check swap

    cat /proc/swaps

The swappiness parameter controls the tendency of the kernel to move processes out of physical memory and onto the swap disk. 
Because disks are much slower than RAM, this can lead to slower response times for system and applications if processes are too aggressively moved out of memory.

The default setting in Ubuntu is swappiness=60. Reducing the default value of swappiness will probably improve overall performance for a typical Ubuntu desktop installation. 
A value of swappiness=10 is recommended, but feel free to experiment.

To check the swappiness value

    cat /proc/sys/vm/swappiness

To change the swappiness value with a swappiness value of 10 can be made with

    sudo vim /etc/sysctl.conf

And add/edit line

    vm.swappiness=10

## Install Fonts

Create (if not exists) `~/.local/share/fonts` directory.

Put fonts files in the `~/.local/share/fonts` directory and clear fonts cache:

    fc-cache -rv

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

## Flatpak
Flatpak is a next-generation technology for building and distributing desktop applications on Linux

    sudo apt install -y flatpak gnome-software-plugin-flatpak
    flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

And restart the system.

## System Tools
This is for tweaking the UI

    sudo apt update && sudo apt install -y\
        gnome-tweak-tool\
        chrome-gnome-shell\
        gnome-shell-extensions\
        dconf-editor\
        synaptic

### Install Nvidia Drivers

You can check your [VGA Info](#vga-info)

Find out the right driver version for your graphics card on https://www.nvidia.com/en-us/geforce/drivers/

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

### Install Nvidia Cuda Toolkit
The NVIDIA® CUDA® Toolkit provides a development environment for creating high performance GPU-accelerated applications.

The toolkit includes GPU-accelerated libraries, debugging and optimization tools, a C/C++ compiler, and a runtime library to deploy your application.

    wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
    sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
    sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/7fa2af80.pub
    sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
    sudo apt update
    sudo apt -y install cuda

### Install ATI Drivers

For installing ATI drivers, read this official documentation: http://support.amd.com/en-us/kb-articles/Pages/AMDGPU-PRO-Install.aspx

### Utilities

**Install the Utilities:**

    sudo apt install -y vim git mercurial meld curl htop xclip unzip gdebi preload bleachbit ubuntu-restricted-extras cifs-utils unace unrar zip p7zip-full \
        p7zip-rar sharutils rar openssh-server lm-sensors whois traceroute nmap font-manager sshfs mc libavcodec-extra libdvd-pkg nfs-kernel-server openvpn \
        easy-rsa network-manager-openvpn-gnome exfat-fuse exfat-utils apt-transport-https python-dbus ethtool net-tools dos2unix \
        liblz4-tool network-manager-openconnect-gnome network-manager-fortisslvpn-gnome openfortivpn tree duplicity xserver-xorg-input-synaptics screen lib32z1 \
        lib32ncurses5-dev libglib2.0-dev-bin pv software-properties-common cpu-checker libnss3-tools python3-pip libcanberra-gtk-module sshpass jq

To setup the git defaults

    git config --global user.name "your name"
    git config --global user.email "your@email.com"

That will create a `~/.gitconfig` with:

    [user]
        email = you@email.com
        name = your name

### RedShift For Eye Strain
It is a program which adjusts the color temperature of your screen with GTK+ integration. 
Think about daylight and night light difference.

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

Ubuntu 20.04 ships with a new dark theme option, but it's not enough.

In the Settings > Appearance select Window Colors to Dark.

The "problem" stems from the factor that the new "Dark" setting only changes the look and feel of apps that run on the desktop. 
It does not change the colour of the desktop UI itself.
To fix this, install the User Themes GNOME Shell extension and GNOME Tweak Tool:

    sudo apt install -y gnome-shell-extensions gnome-tweak-tool

Open GNOME Extensions app and slide the toggle next to "User Themes" to on.

Restart GNOME Shell (Alt + F2, type r, hit enter)

Lastly, open the GNOME Tweaks tool and select "Appearance" in the sidebar, locate the Shell section and Select `Yaru Dark` from the menu adjacent.

### Oracle Java

Download and install deb package from https://www.oracle.com/java/technologies/javase-jdk15-downloads.html

And update alternatives

    sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/jdk-15.0.1/bin/java 1
    sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/jdk-15.0.1/bin/javac 1
    sudo update-alternatives --config java

### Wine
To run windows applications Wine is the best option. I often use HeidiSQL with Wine.

Enable i386 architecture

    sudo dpkg --add-architecture i386 

Download and add the repository key:
    
    wget -O - https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -

Add the repository:
    
    sudo add-apt-repository -y 'deb https://dl.winehq.org/wine-builds/ubuntu/ focal main'
    
Install:

    sudo apt update && sudo apt install -y --install-recommends winehq-stable    
    
### Nautilus-Actions
Use Nautilus-Actions to easily and graphically create custom context menu options for Ubuntu's Nautilus file manager.

    sudo add-apt-repository ppa:daniel-marynicz/filemanager-actions
    sudo apt install -y filemanager-actions-nautilus-extension


After installing it, quit and restart the Nautilus file manager with the following command.
You can also press Alt+F2 and type this command instead of running it in a terminal.

    nautilus -q

After installation you can launch `fma-config-tool`.

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


### Neofetch
A fast, highly customizable system info script

Neofetch is a CLI system information tool written in BASH. 
Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice. 
The main purpose of Neofetch is to be used in screenshots to show other users what OS/Distro you're running, what Theme/Icons you're using etc.

Installation:

    sudo add-apt-repository ppa:dawidd0811/neofetch
    sudo apt update && sudo apt install -y neofetch

### GParted
Partition editor for graphically managing disk partitions https://gparted.sourceforge.io/

    sudo apt install -y gparted

### Firewall

#### UFW

UFW, or Uncomplicated Firewall, is an interface to iptables that is geared towards simplifying the process of configuring a firewall. 
While iptables is a solid and flexible tool, it can be difficult for beginners to learn how to use it to properly configure a firewall.
UFW is installed by default on Ubuntu. If it has been uninstalled for some reason, you can install it with 

    sudo apt install -y ufw

To enable UFW, use this command:

    sudo ufw enable

Configuring examples:

To configure your server to allow incoming SSH connections, you can use this command:

    sudo ufw allow ssh
    
However, we can actually write the equivalent rule by specifying the port instead of the service name. For example, this command works the same as the one above:

    sudo ufw allow 22    
    
For example, to allow X11 connections, which use ports 6000-6007, use these commands:

    sudo ufw allow 6000:6007/tcp
    sudo ufw allow 6000:6007/udp
    
#### GUFW

GUFW is a GUI for UFW

    sudo apt install -y gufw

### Geekbench

Download archive from https://www.geekbench.com/download/linux/ and extract.

Move folder under /opt

    sudo mv Geekbench-5.3.1-Linux /opt/geekbench5

Now you can run benchmark

    /opt/geekbench5/geekbench5

### Clonezilla
Clonezilla is a partition and disk imaging/cloning program. It helps you to do system deployment, bare metal backup and recovery. 

Download live USB image: https://clonezilla.org/downloads/download.php?branch=stable

Prepare USB device
    
    mkfs.vfat -F 32 /dev/sd[1 letter]

And [Write iso Image to USB](#write-iso-image-to-usb)

### Screen Testing Soft
This is a program for testing the quality of CRT/LCD screens. It displays various patterns and allows you to estimate the quality of your CRT/LCD monitor.

    sudo apt install -y screentest

### Ventoy

[Ventoy](https://www.ventoy.net/en/index.html) is an open source tool to create bootable USB drive for ISO/WIM/IMG/VHD(x)/EFI files.
With ventoy, you don't need to format the disk over and over, you just need to copy the ISO/WIM/IMG/VHD(x)/EFI files to the USB drive and boot them directly.
You can copy many files at a time and ventoy will give you a boot menu to select them.

Download the installation package, like ventoy-x.x.xx-linux.tar.gz from [here](https://github.com/ventoy/Ventoy/releases) and decompress it.
Run the shell script as root, where XXX is the USB device, for example /dev/sdb:

    sudo sh Ventoy2Disk.sh -i -L "MY-USB" /dev/XXX

**Attention that the USB drive will be formatted and all the data will be lost after install.**

You just need to install Ventoy once, after that all the things needed is to copy the iso files to the USB.
You can also use it as a plain USB drive to store files and this will not affect Ventoy's function.

You can configure how Ventoy will work using configuration file `/ventoy/ventoy.json` on the USB drive.

My configuration file looks like:
```json
{
    "control": [
        { "VTOY_DEFAULT_SEARCH_ROOT": "/install/iso" }
    ],
    "theme": {
        "display_mode": "CLI"
    }
}
```

Full documentation you can find [here](https://www.ventoy.net/en/plugin_control.html)

***
[(Back to top)](#table-of-contents)

## Other Tools

### Google Chrome
Add google chrome repository and install

        sudo sh -c 'echo "deb [arch=amd64] http://dl-ssl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
        wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
        sudo apt update && sudo apt install -y google-chrome-stable

Then launch it with `$ google-chrome` and you can pin it to a gnome bar.

### PlayOnLinux

Installation

    sudo apt install playonlinux
    
### Dropbox

Installation

    sudo apt install nautilus-dropbox
    
### Sublime Text 3
A sophisticated text editor for code, markup and prose

Add repository:

    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    sudo apt install apt-transport-https
    
Stable version:

    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    
Dev version:

    echo "deb https://download.sublimetext.com/ apt/dev/" | sudo tee /etc/apt/sources.list.d/sublime-text.list    
    
Install:
    
    sudo apt update && sudo apt install -y sublime-text
    
Configuration of synchronization between devices explained [here](#sync-sublime-text)

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
VirtualBox is a powerful x86 and AMD64/Intel64 virtualization product for enterprise as well as home use.

Check latest version number on https://www.virtualbox.org/wiki/Downloads

During writing this manual, latest version was 6.1

Installation

    sudo sh -c 'echo "deb [arch=amd64] http://download.virtualbox.org/virtualbox/debian $(lsb_release -sc) contrib" >> /etc/apt/sources.list.d/virtualbox.list'
    wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox_2016.asc -O- | sudo apt-key add -
    sudo apt update && sudo apt install -y virtualbox-6.1 virtualbox-ext-pack

Suggested to [Enable Native Virtualization](#enable-native-virtualization)

Also you can read [Virtual Machine Related](#virtual-machine-related)

### Android Studio

Installation

I recommend to install JetBrains Toolbox from https://www.jetbrains.com/toolbox-app/ and install Android Studio from toolbox. 

After downloading android sdk, update PATH variable:

    vim ~/.bashrc

add lines:

    export PATH=${PATH}:/path-to-android-sdk/tools
    export PATH=${PATH}:/path-to-android-sdk/platform-tools

### Smart Git

Download deb bundle from https://www.syntevo.com/smartgit/download/

### FileZilla

Installation

    sudo apt install -y filezilla

### Google Music Player

This is a beautiful cross platform Desktop Player for Google Play Music.

deb file can be downloaded from https://www.googleplaymusicdesktopplayer.com/

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

Go to the https://www.vagrantup.com/downloads.html page of Vagrant and check for the latest release.
During writing this manual, last version was 2.0.1
    
    wget https://releases.hashicorp.com/vagrant/2.0.1/vagrant_2.0.1_x86_64.deb
    sudo dpkg -i vagrant_2.0.1_x86_64.deb

Reconfigure the VirtualBox DKMS:

    sudo dpkg-reconfigure virtualbox-dkms

### Docker

Installation

    wget -qO- https://get.docker.com/ | sh

Working with Docker is a pain if your user is not configured correctly, so add your user to the docker group with the following command.

    sudo usermod -aG docker $(whoami)

Log out and log in from your server to activate your new groups.

    sudo apt install -y docker-compose

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

    wget https://go.skype.com/skypeforlinux-64.deb
    sudo apt install ./skypeforlinux-64.deb

### Telegram

Installation

    sudo apt install -y telegram-desktop

### Slack

Install via terminal:

    wget -O - https://packagecloud.io/slacktechnologies/slack/gpgkey  | sudo apt-key add -

Create the file `/etc/apt/sources.list.d/slack.list` with the following content

    deb https://packagecloud.io/slacktechnologies/slack/debian/ jessie main
    
And run:
    
    sudo apt update && sudo apt install -y slack-desktop
    
Or download .deb from https://slack.com/downloads and install manually

### Viber

Since new versions of Ubuntu are shipped with libssl1.1 or have this package in their repositories, viber.deb can be tinkered to state libssl1.1 as a dependency.

Ensure that libssl1.1 is installed:

    sudo apt install libssl1.1
    
Download viber.deb from the [Viber webpage](https://www.viber.com/download/) and copy it to a temp folder. 
I have used /home/<user>/temp for this.

Now we need to make some changes to the package:

    mkdir viber
    cd viber 
    ar x ../viber.deb
    tar xzf control.tar.gz

Now we need to change dependencies:

- Open the control file with a text editor.
- Change on line 6: libssl1.0.0 to libssl1.1. (Note: in case of newer version of libssl use the new version).
- Save the file and exit.

Repackage the .deb file.

    tar --ignore-failed-read -cvzf control.tar.gz {post,pre}{inst,rm} md5sums control
    ar rcs viber-new.deb debian-binary control.tar.gz data.tar.xz
    
Install the new deb:

    sudo dpkg -i viber-new.deb
     
### Gimp

Installation

    sudo apt install -y gimp gimp-data gimp-plugin-registry gimp-data-extras

### VLC Player

VLC is a free and open source cross-platform multimedia player and framework that plays most multimedia files as well as DVDs, 
Audio CDs, VCDs, and various streaming protocols.

Installation

    sudo apt install -y vlc

### KDEnlive Video Editor

Installation

    sudo apt install -y kdenlive

### Httpie
You can easily use httpie from terminal: `http get https://google.com`

Installation

    sudo apt update && sudo apt install -y httpie

### Peek
Simple animated GIF screen recorder with an easy to use interface

Installation

    sudo add-apt-repository ppa:peek-developers/stable
    sudo apt update && sudo apt install -y peek

### OBS

Free and open source software for video recording and live streaming https://obsproject.com/.

Installation

    sudo add-apt-repository ppa:obsproject/obs-studio
    sudo apt update && sudo apt install -y obs-studio


### USB Maker for Windows ISO on Linux
You can easily use `Startup Disk Creator` and `UNetbootin` to create Linux to USB. 
But if you need to create Windows bootable USB from your Linux OS use woeusb:

    sudo add-apt-repository ppa:nilarimogard/webupd8
    sudo apt install -y woeusb

The important part here is that you should format usb in NTFS.

After run
    
    woeusb \
        --target-filesystem NTFS \
        --device Win10_1809Oct_EnglishInternational_x64.iso /dev/sd[1 letter]

### StarUML

A sophisticated software modeler for agile and concise modeling (http://staruml.io/)

You can download .AppImage file from http://staruml.io/download

Make downloaded file executable and run.

### Gramps

Gramps is a free software project and community. 
It is a genealogy program that is both intuitive for hobbyists and feature-complete for professional genealogists. 

To install, run:

    sudo apt install -y gramps

### uGet

uGet is a powerful download manager. 

To install, run:

    sudo add-apt-repository -y ppa:uget-team/ppa
    sudo apt install -y uget uget-integrator

You can also install browser extensions for uGet integration: 

- Chrome: https://chrome.google.com/webstore/detail/uget-integration/efjgjleilhflffpbnkaofpmdnajdpepi

***
[(Back to top)](#table-of-contents)

## Development

### LAMP
Linux Apache MySQL PHP

**- Installation for the following:**
- PHP 5.6/7.0/7.4/8.0 (and Modules)
- Apache 2 (and Modules + Dynamic hosts)
- Nginx *(Optional)*
- MySQL
- Redis
- and more.

#### PHP

##### PHP 5.6
It's important to install **php5.6-dev** if you want to compile any add-ons later.

    sudo add-apt-repository -y ppa:ondrej/php
    sudo apt update && sudo apt install -y php5.6 libpcre3-dev php5.6-cli php5.6-cgi php5.6-common php5.6-mysql php5.6-curl php5.6-gd php5.6-geoip php5.6-imagick php5.6-imap php5.6-json php5.6-ldap php5.6-mcrypt php5.6-memcache php5.6-memcached php5.6-tidy php5.6-xdebug php5.6-xmlrpc php5.6-xsl php5.6-dev

If you are looking for more PHP modules try:

    sudo apt-cache search php5-


##### PHP 7.0
It's important to install **php7.0-dev** if you want to compile any add-ons later.

    sudo add-apt-repository -y ppa:ondrej/php
    sudo apt update && sudo apt install -y php7.0-bz2 php7.0-cgi php7.0-cli php7.0-common php7.0-curl php7.0-dev php7.0-enchant php7.0-fpm php7.0-gd php7.0-gmp php7.0-imap php7.0-intl php7.0-json php7.0-ldap php7.0-mcrypt php7.0-mysql php7.0-odbc php7.0-opcache php7.0-pgsql php7.0-phpdbg php7.0-pspell php7.0-readline php7.0-recode php7.0-sybase php7.0-tidy php7.0-xmlrpc php7.0-xsl php7.0-sqlite3 php7.0-mbstring php7.0-bcmath php7.0-soap php7.0-zip php-xdebug php-imagick

If you are looking for more PHP modules try:

    sudo apt-cache search php7.0-

##### PHP 7.4
It's important to install **php7.4-dev** if you want to compile any add-ons later.

    sudo add-apt-repository -y ppa:ondrej/php
    sudo apt update && sudo apt install -y php7.4-bz2 php7.4-cgi php7.4-cli php7.4-common php7.4-curl php7.4-dev php7.4-enchant php7.4-fpm php7.4-gd php7.4-gmp php7.4-imap php7.4-intl php7.4-json php7.4-ldap php7.4-mysql php7.4-odbc php7.4-opcache php7.4-pgsql php7.4-phpdbg php7.4-pspell php7.4-readline php7.4-sybase php7.4-tidy php7.4-xmlrpc php7.4-xsl php7.4-sqlite3 php7.4-mbstring php7.4-bcmath php7.4-soap php7.4-zip php7.4-xdebug php7.4-redis php7.4-igbinary php7.4-imagick php-sodium

If you are looking for more PHP modules try:

    sudo apt-cache search php7.4-

##### PHP 8.0
It's important to install **php8.0-dev** if you want to compile any add-ons later.

    sudo add-apt-repository -y ppa:ondrej/php
    sudo apt update && sudo apt install -y php8.0-bz2 php8.0-cgi php8.0-cli php8.0-common php8.0-curl php8.0-dev php8.0-enchant php8.0-fpm php8.0-gd php8.0-gmp php8.0-imap php8.0-intl php8.0-ldap php8.0-mysql php8.0-odbc php8.0-opcache php8.0-pgsql php8.0-phpdbg php8.0-pspell php8.0-readline php8.0-sybase php8.0-tidy php8.0-xmlrpc php8.0-xsl php8.0-sqlite3 php8.0-mbstring php8.0-bcmath php8.0-soap php8.0-zip php8.0-xdebug php8.0-redis php8.0-igbinary php8.0-imagick php8.0-psr php-sodium

If you are looking for more PHP modules try:

    sudo apt-cache search php8.0-

##### Switch PHP Versions

For example switch from 5.6 to 7.4

Apache:

    sudo a2dismod php5.6
    sudo a2enmod php7.4
    sudo service apache2 restart

Command Line:

    sudo update-alternatives --set php /usr/bin/php7.4
    sudo update-alternatives --set phar /usr/bin/phar7.4
    sudo update-alternatives --set phar.phar /usr/bin/phar.phar7.4

#### Composer

    curl -sS https://getcomposer.org/installer | php && sudo mv composer.phar /usr/local/bin/composer

Disable XDebug for composer

    sudo phpdismod -s cli xdebug

And add this lines in your .bashrc file:

    # Load xdebug Zend extension with php command
    alias php='php -dzend_extension=xdebug.so'
    # PHPUnit needs xdebug for coverage. In this case, just make an alias with php command prefix.
    alias phpunit='php $(which phpunit)'

#### PHPUnit

    wget https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && sudo mv phpunit.phar /usr/local/bin/phpunit

#### Apache

##### Apache: Installation

For PHP 5.6

    sudo apt install -y apache2 libapache2-mod-php5.6

For PHP 7.*

    sudo apt install -y apache2 libapache2-mod-php7.*

For PHP 8.*

    sudo apt install -y apache2 libapache2-mod-php8.*

##### Apache: Enable php-mcrypt & mod_rewrite

Enable mod_rewrite

    sudo a2enmod rewrite

Enable php-mcrypt

For PHP 5

    sudo php5enmod mcrypt && sudo service apache2 restart

For PHP 7 (if mcrypt is available)

    sudo phpenmod mcrypt && sudo service apache2 restart

If you are looking for more Apache modules try:

    sudo apt-cache search libapache2-mod

##### Apache: Configure dynamic virtualhosts

Enable module `vhost_alias`

    sudo a2enmod vhost_alias

Next, open /etc/apache2/apache2.conf

    sudo vim /etc/apache2/apache2.conf

and add the following lines before `IncludeOptional sites-enabled/*.conf` line.

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

If you want to disable all configured virtual hosts, then comment this line in your config file:

    #IncludeOptional sites-enabled/*.conf

This sets up a catch all for any domain coming in over port 80 (the default port for http traffic, if your using https you will need to use 443 - alternatively you could remove the port restriction).
The important line here is the VirtualDocumentRoot. The tells Apache where your files will reside on disk.
The %0 part takes the whole domain name and inserts it into the path. But I didn't want to have the `.test` part of the domain in my folders on disk, otherwise we use %-2+
To illustrate this if we went to a domain somesite.com.test the VirtualDocumentRoot would be:

    /var/www/html/domains/somesite.com

Now you have to add automatic `.test` domain resolving on your local machine:

Edit the file `/etc/NetworkManager/NetworkManager.conf`, and add the line `dns=dnsmasq` to the [main] section, it will look like this:

```
[main]
plugins=ifupdown,keyfile
dns=dnsmasq

[ifupdown]
managed=false

[device]
wifi.scan-rand-mac-address=no
```

Let NetworkManager manage /etc/resolv.conf

    sudo rm /etc/resolv.conf
    sudo ln -s /var/run/NetworkManager/resolv.conf /etc/resolv.conf

Add custom tld:

    echo 'address=/.test/127.0.0.1' | sudo tee /etc/NetworkManager/dnsmasq.d/test-tld

Reload NetworkManager:

    sudo systemctl reload NetworkManager

Now domain somesite.com.test should work.

##### Apache: Configure SSL for dynamic virtualhosts

First of all [Generate SSL certificates for local domains](#generate-ssl-certificates-for-local-domains)

After you can use this small script, for generating SSL certificate for all virtual domains (folders).

```bash
#!/usr/bin/env bash

cmd_array=( mkcert -key-file key.pem -cert-file cert.pem  )
for d in /var/www/html/domains/*/ ; do
    cmd_array+=(`basename "$d"`.test)
done

"${cmd_array[@]}"
```    

And add the generated cert.pem and key.pem to the apache configuration file, edit `/etc/apache2.conf`

Add new VirtualHost section:

```
<VirtualHost *:443>
    VirtualDocumentRoot /var/www/html/domains/%-2+/public

    SSLEngine on
    SSLCertificateFile    /path/to/generated/certs/cert.pem
    SSLCertificateKeyFile /path/to/generated/certs/key.pem

    <Directory /var/www/html/domains>
                DirectoryIndex index.html index.php
                Options Indexes FollowSymLinks MultiViews Includes
                AllowOverride All
                Order deny,allow
                Allow from all
                Require all granted
    </Directory>

</VirtualHost>
```

Make sure the mod_ssl is enabled and restart the apache.

#### Nginx
Or if you prefer to use nginx

For stable version

    sudo add-apt-repository -y ppa:nginx/stable

For latest (recommended)

    sudo add-apt-repository -y ppa:nginx/development

And after install

    sudo apt install -y nginx

#### Generate SSL certificates for local domains

`mkcert` automatically creates and installs a local CA in the system root store, and generates locally-trusted certificates.

Download [mkcert](https://github.com/FiloSottile/mkcert) precompiled binary
from https://github.com/FiloSottile/mkcert/releases

    wget -O mkcert https://github.com/FiloSottile/mkcert/releases/download/v1.4.3/mkcert-v1.4.3-linux-amd64
    chmod +x mkcert

Generate and install root certificates:

    mkcert -install

Root certificates will be placed under `mkcert -CAROOT`. For Ubuntu its `/home/<user>/.local/share/mkcert`

After you can generate certificates for your domains:

    mkcert -key-file key.pem -cert-file cert.pem example.test *.example.test example2.test *.example2.test

Now you can add the generated cert.pem and key.pem to your webserver configuration.

If you use Apache Dynamic Virtualhosts, you can generate certs automatically. 
Read more in [Configure SSL for Dynamic Virtualhosts](#apache-configure-ssl-for-dynamic-virtualhosts)  

#### MySQL

##### Installation

You can get latest version number on https://dev.mysql.com/downloads/repo/apt

    wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb
    sudo dpkg -i mysql-apt-config_0.8.13-1_all.deb
    sudo apt update & sudo apt install -y mysql-server

For start configuring MySQL server, run:

    sudo mysql_secure_installation

If you are not able to login with root user, run:

    sudo mysql

and run:    
    
    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'YourPassword';

##### Allow remote access for root:

Login in MySQL shell and run:

    CREATE USER 'root'@'%' IDENTIFIED BY 'secret';
    GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';

Also Update mysql server config:

For MySQL 5.*

    sudo sed -i 's/bind-address/bind-address = 0.0.0.0#/' /etc/mysql/my.cnf

For MySQL 8.*

    echo 'bind-address    = *' | sudo tee -a /etc/mysql/mysql.conf.d/mysqld.cnf

Restart the service:

    sudo service mysql restart

#### Percona Toolkit
Percona Toolkit is a collection of advanced open source command-line tools, developed and used by the Percona technical staff, 
that are engineered to perform a variety of MySQL® and MongoDB® server and system tasks that are too difficult or complex 
to perform manually – freeing your DBAs for work that helps you achieve your business goals.

    sudo apt install -y percona-toolkit

#### MyCLI
This is a very nice utility [https://github.com/dbcli/mycli](https://github.com/dbcli/mycli)

    pip install mycli

Usage (See the documents from the git link above for more example):

    mycli -h localhost -u root
    mycli -h localhost -u root -p

#### PostgreSQL

    sudo apt install -y postgresql libpq-dev

#### Memcached

    sudo apt install -y memcached php-memcached

#### Redis
Install redis latest stable version

    sudo add-apt-repository -y ppa:chris-lea/redis-server
    sudo apt install -y redis-server

Add to startup:

    sudo systemctl enable redis-server.service

##### Multiple Redis Instances

Disable default instance

    sudo systemctl stop redis
    sudo systemctl disable redis

Repeat these steps to configure a Redis instance for every instance you want to set up:

In this case we set up first instance called "redis_1"

Create folders and configs:

    sudo mkdir /etc/redis/redis_1
    sudo cp /etc/redis/redis.conf /etc/redis/redis_1/redis.conf 
    sudo chown -R redis:redis /etc/redis

In the config file edit lines:

    daemonize no
    supervised systemd
    pidfile /var/run/redis/redis_1.pid
    logfile /var/log/redis/redis_1.log
    dir /var/lib/redis/redis_1/

Define a "port" number.

    port 6379

*Warning: Remember that each instance should be running on a different port.*

Create the database directories at the location given in the configuration file.

    sudo mkdir /var/lib/redis/redis_1
    sudo chown redis:redis /var/lib/redis/redis_1
    sudo chmod 0750 /var/lib/redis/redis_1

Create the service unit file "/etc/systemd/system/redis@.service" with the following contents:


```
[Unit]
Description=Redis persistent key-value database
After=network.target

[Service]
Type=simple
User=redis
Group=redis
ExecStart=/usr/bin/redis-server /etc/redis/%i/redis.conf
ExecStop=/bin/kill -s TERM $MAINPID
PrivateTmp=true
PIDFile=/var/run/redis/%i.pid
RuntimeDirectory=%i
RuntimeDirectoryMode=2755
LimitNOFILE=65536
Restart=always
TimeoutStopSec=0

UMask=007
PrivateDevices=yes
ProtectHome=yes
ReadOnlyDirectories=/
ReadWriteDirectories=-/var/lib/redis
ReadWriteDirectories=-/var/log/redis
ReadWriteDirectories=-/var/run/redis

NoNewPrivileges=true
CapabilityBoundingSet=CAP_SETGID CAP_SETUID CAP_SYS_RESOURCE
RestrictAddressFamilies=AF_INET AF_INET6 AF_UNIX
MemoryDenyWriteExecute=true
ProtectKernelModules=true
ProtectKernelTunables=true
ProtectControlGroups=true
RestrictRealtime=true
RestrictNamespaces=true

# redis-server can write to its own config file when in cluster mode so we
# permit writing there by default. If you are not using this feature, it is
# recommended that you replace the following lines with "ProtectSystem=full".
ProtectSystem=true
ReadWriteDirectories=-/etc/redis

[Install]
WantedBy=multi-user.target

```

Start the new redis instance:

    sudo systemctl start redis@redis_1
    sudo systemctl enable redis@redis_1

#### ELK Stack
Install ELK stack: Elasticsearch, Logstash, and Kibana

    wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
    sudo apt install -y apt-transport-https
    echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
    sudo apt update && sudo apt install -y elasticsearch

To configure Elasticsearch to start automatically when the system boots up, run the following commands:

    sudo /bin/systemctl daemon-reload
    sudo /bin/systemctl enable elasticsearch.service

#### Letsencrypt

Install certbot (https://certbot.eff.org)

    sudo add-apt-repository ppa:certbot/certbot
    sudo apt update
    
Generating for nginx:
    
    sudo apt install -y python-certbot-nginx 
    sudo certbot --nginx
    
Generating for apache:
    
    sudo apt install -y python-certbot-apache 
    sudo certbot --apache

You can test automatic renewal for your certificates by running this command:

    sudo certbot renew --dry-run

#### Java Runtime

    sudo apt install -y default-jre

#### Phalcon

    sudo apt-add-repository ppa:phalcon/stable
    sudo apt update
    sudo apt install -y php5-phalcon

#### Phalcon Dev Tools
This is an easy to use install script that will cleanup after itself. It can also be used for updating:

    sudo bash install_phalcon_devtools.sh

To test it run: `$ phalcon`

#### Secure Permissions
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

    */5 * * * * /home/<user>/backup.sh chgrp -R www-data /var/www && chmod g+rw /var/www

Lastly, you could have a deploy script that does this for you, such as Python `Fabfile`, but that's another topic.


***

[(Back to top)](#table-of-contents)

### Python

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

#### Pip
[Pip](#pip) is a tool for installing and managing Python packages. Install Pip with Wget and Python.

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.5 get-pip.py

View a list of helpful commands

    pip --help

Check the version of Pip that is installed

    pip -V

#### Virtualenv
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


### Go
Install Golang. You can check latest version of Golang here https://golang.org/dl/#featured
While writing this article, lastest version was 1.9

    sudo add-apt-repository -y ppa:gophers/archive
    sudo apt -y update && sudo apt install golang-1.9

After that your installation will be in the `/usr/lib/go-1.9`
I recommend create symlink:

    sudo ln -s /usr/lib/go-1.9 /usr/local/go

And Add `/usr/local/go/bin` to the PATH environment variable. 
You can do this by adding this line to your `/etc/profile` (for a system-wide installation) or `$HOME/.profile`:
    
    PATH="$PATH:/usr/local/go/bin"


***
[(Back to top)](#table-of-contents)


### Ruby
Install Ruby 2.X with header files in `ruby2.0-dev`, this will keep your gems from having issues.

    sudo apt install -y ruby2.0 ruby2.0-dev

For Ruby RVM (Version Management)

    gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3
    \curl -sSL https://get.rvm.io | bash -s stable

***
[(Back to top)](#table-of-contents)

### NodeJS
I recommend install NodeJS using [Node Version Manager](https://github.com/nvm-sh/nvm) 
    
    curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.37.2/install.sh | bash

To download, compile, and install the latest release of node, do this:

    nvm install node # "node" is an alias for the latest version

To install a specific version of node:

    nvm install 6.14.4 # or 10.10.0, 8.9.1, etc

To install a latest LTS version of node:

    nvm install --lts

You can list available versions using ls-remote:

    nvm ls-remote

And then in any new shell just use the installed version:

    nvm use [version]

***
[(Back to top)](#table-of-contents)

### Yarn
For installation Yarn package manager run:

    curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
    echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
    sudo apt update && sudo apt install -y yarn

***
[(Back to top)](#table-of-contents)

### Ansible

    sudo apt install -y ansible

***
[(Back to top)](#table-of-contents)


## Gaming

### Steam
Ultimate entertainment platform. http://store.steampowered.com/

    sudo apt install -y steam

### PCSXR
PCSX-Reloaded - PlayStation 1 Emulator. https://pcsxr.codeplex.com/

Install emulator:

    sudo apt install -y pcsxr

pscxr can simulate a bios file. However if you need to use a bios, [download](files/pcsxr/SCPH1001.BIN?raw=1) and move the file into `~/.pcsx/bios/`.

Download games from http://redump.org/discs/system/psx/ or https://rutracker.org/forum/viewtopic.php?t=4496017 and put under `~/.pcsx/games/`

After that run PCSX, configure and play

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

Note: for security reasons, not recommended

    sudo git config --global http.sslVerify false


## Shortcuts

- "System Settings" > "Keyboard" > "Shortcuts" > "Custom Shortcuts" <kbd>ctrl</kbd>+<kbd>r</kbd> Terminal ```gnome-terminal```
- "System Settings" > "Keyboard" > "Shortcuts" > "Custom Shortcuts" <kbd>ctrl</kbd>+<kbd>e</kbd> Files ```nautilus -w```

## VIM Customization

**Setup VIM**

    git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

And copy [.vimrc](os/home/.vimrc) file in your home folder (/home/<user>/.vimrc)
After run

    $ vim
    :PluginInstall

## Add Georgian Keyboard

Go to System "Settings" > "Keyboard" > "Text Entry" and add Georgian layout. Also enable "Allow different sources for each window"

***
[(Back to top)](#table-of-contents)


# Ubuntu Fixes
These are solutions to fix problems I've encountered.

## Ubuntu Infinite Login

When you try to login to Ubuntu and it relogs you back into the login screen, this is an infinite loop. 
The only way I was able to fix it despite all the guides was combining a few of these together.

The first step is to login to a terminal.

    CTRL + ALT + F1  (Or F3)
    
Next, Login as your user who must be able to run sudo.    

- **Home Folder Permissions**
  - `ls -ld ~` should have these permission exactly as: `drwxr-xr-x`
  - The user:group must be your, e.g. `john:john`
  - To Fix: `sudo chmod 755 ~` and `sudo chown -R john:john ~`
- **Temp Folder Permissions**
  - `ls -ld /tmp` should have these permission exactly as: `drwxrwxrwt`
  - The user:group must be `root:root` on `/tmp`
  - To Fix: `sudo chmod a+wt /tmp`
- **Xauthority Ownership**
  - `ls -lta | grep .Xa` should be owned by your user, for example `john john`
   - If it is `root root` or anything than your user/group it's wrong
   - To Fix: `sudo chown john:john .Xauthority`
- **Xsession Errors**
  - This is just to make sure there are no syntax errors for your reference:
    - To Check: `cat ~/.xsession-errors`
    - You don't need to do anything if there are syntax errors, we will move the file
- **Try Moving XAuthority**
  - Sometimes it's as easy to moving Xauthority so a new is generated at login
  - To Fix: `sudo ~/.Xauthority ~/.Xauthority.bak`
- **Try Reconfiguring LightDM**
  - Fix: `dpkg-reconfigure lightdm`, then select lightdm in the menu
  - Lastly restart lightdm: `sudo service lightdm restart`
- **Apt Auto Remove Problem**
  - I read that it's possible `apt-autoremove` may accidentally remove `xubuntu-desktop`, `ubuntu-desktop` and LightDM reports no errors.
    - The `ubuntu-desktop` will load the Gnome interface
    - The `xubuntu-desktop` will load a different interface I'm not familiar with
    - To Fix: `sudo apt install ubuntu-desktop`
  - **If you are using Gnome**, try following the post at [OMGUbuntu](http://www.omgubuntu.co.uk/2016/05/install-gnome-3-20-ubuntu-16-04-lts)
    - After the Above Try: `sudo apt autoremove gnome-software && sudo apt install gnome-software`
    - I was able to get Gnome-Classic working but not Gnome
- **How to Ensure it Works**
  - You might be able to login after one of the steps above if you don't reboot. However, to be certain, 
    you want to reboot to ensure it is fixed, otherwise you'll be doing this over and over   

## PCI Device Is Not Recognized Correctly

If your `lspci | grep "VGA"` output looks like this:

    01:00.0 VGA compatible controller: NVIDIA Corporation Device 1f95 (rev a1)

Instead of this:

    01:00.0 VGA compatible controller [0300]: NVIDIA Corporation TU117M [GeForce GTX 1650 Ti Mobile] [10de:1f95] (rev a1)

Then you're affected by the issue.

This can be caused by your `/usr/share/misc/pci.ids\*` files being outdated and you can fix it by running:

    sudo update-pciids

If the list is not updated even after running the command above, that means your PCI device is brand new, and no one has registered your device to the pci-ids repository.

You can submit an issue/contact us through gitter, or you can add it yourself to https://pci-ids.ucw.cz/. 
Make sure you have the right vendor ID and the device ID by checking `lspci -nn` and read the guidelines.

## Restore Screen Brightness and Keyboard backlit on Reboot

On my device screen brightness and keyboard backlit always resets after reboot, so there is a fix.

First, find config files where your brightness and keyboard backlit state is stored. In my case, it was `/sys/class/backlight/nvidia_0/brightness` and `/sys/class/leds/tpacpi\:\:kbd_backlight/brightness`

Test your configs:

    echo 1 > /sys/class/leds/tpacpi\:\:kbd_backlight/brightness
    echo 70 > /sys/class/backlight/nvidia_0/brightness

Settings should be changed. If not, check configuration files path.

Max brightness you can check via `cat /sys/class/backlight/nvidia_0/max_brightness` and `cat /sys/class/leds/tpacpi\:\:kbd_backlight/max_brightness`

Create script under `/usr/local/bin/`

    sudo vim /usr/local/bin/setup-brightness.sh

And put the lines below:

```bash
#!/bin/bash

echo 0 > /sys/class/leds/tpacpi\:\:kbd_backlight/brightness
echo 1 > /sys/class/leds/tpacpi\:\:kbd_backlight/brightness
echo 70 > /sys/class/backlight/nvidia_0/brightness
```

Create systemd service file:

    sudo vim /etc/systemd/system/setup-brightness.service

And put content below:

```
[Unit]
After=graphical.target
Description=Set up the screen and keyboard brightness

[Service]
Type=simple
ExecStart=/usr/local/bin/setup-brightness.sh

[Install]
WantedBy=multi-user.target
```

Set proper permissions:

    sudo chmod 744 /usr/local/bin/setup-brightness.sh
    sudo chmod 664 /etc/systemd/system/setup-brightness.service

Test your script by running:

    sudo /usr/local/bin/setup-brightness.sh

Enable the service unit:

    sudo systemctl daemon-reload
    sudo systemctl enable setup-brightness.service

## Disable UEFI Choice Screen
The easiest solution is to define the undocumented `GRUB_RECORDFAIL_TIMEOUT` variable in `/etc/default/grub`. For example:

    sudo vim /etc/default/grub

and add variable:

    GRUB_RECORDFAIL_TIMEOUT=$GRUB_TIMEOUT

Also set `GRUB_TIMEOUT` to `0`. After run:

    sudo update-grub

Example:

    GRUB_HIDDEN_TIMEOUT=0
    GRUB_HIDDEN_TIMEOUT_QUIET=true
    GRUB_TIMEOUT=0
    GRUB_RECORDFAIL_TIMEOUT=$GRUB_TIMEOUT

# GUI

## Move Dock To Bottom

I prefer dock like Mac. To do this, run commands:

    gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false
    gsettings set org.gnome.shell.extensions.dash-to-dock dock-position BOTTOM
    gsettings set org.gnome.shell.extensions.dash-to-dock transparency-mode FIXED
    gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 34
    gsettings set org.gnome.shell.extensions.dash-to-dock unity-backlit-items false
    gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'

## Easy Window Resize
You can resize windows very nicely:
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
In terminal make sure this is false, then try your hotkey `ctrl+alt+l` or if you set it like `super+l` in the settings:

    gsettings set org.gnome.desktop.lockdown disable-lock-screen 'false'

## Gnome Extensions
You can toggle these items at https://extensions.gnome.org
I suggest creating an account so you have a record.

- [OpenWeather](https://extensions.gnome.org/extension/750/openweather/) - Weather extension to display weather information from https://openweathermap.org/ or https://darksky.net for almost all locations in the world.
- [No Title Bar](https://extensions.gnome.org/extension/2015/no-title-bar-forked/) - No Title Bar removes the title bar from non-GTK applications and moves the window title and buttons to the top panel.
- [Extension Update Notifier](https://extensions.gnome.org/extension/1166/extension-update-notifier/) - Shows a notification when extension updates are available.
- [Hide Activities Button](https://extensions.gnome.org/extension/1128/hide-activities-button/) - Hides the Activities button on the panel
- [Remove Dropdown Arrows](https://extensions.gnome.org/extension/800/remove-dropdown-arrows/) - Removes the dropdown arrows which were introduced in Gnome 3.10 from the App Menu, System Menu, Input Menu, Access Menu, Places Menu, Applications Menu and any other extension that wants to add dropdown arrows.
- [Status Area Horizontal Spacing](https://extensions.gnome.org/extension/355/status-area-horizontal-spacing/) - Reduce the horizontal spacing between icons in the top-right status area
- [NoAnnoyance](https://extensions.gnome.org/extension/1236/noannoyance/) - Disables the “Window Is Ready” notification and changes the policy of the window manager so that new windows are always focused.
- [Clock Override](https://extensions.gnome.org/extension/1206/clock-override/) - Customize the date and time format displayed in clock in the top bar in GNOME Shell. My format is: `%a | %e %b | %H:%M`
- [Panel OSD](https://extensions.gnome.org/extension/708/panel-osd/) - Configuring where on the (main) screen notifications will appear, instead of just above the message tray.
- [Draw On You Screen](https://extensions.gnome.org/extension/1683/draw-on-you-screen/) - Start drawing with Super+Alt+D and save your beautiful work by taking a screenshot.
- [Caffeine](https://extensions.gnome.org/extension/517/caffeine/) - Disable the screensaver and auto suspend.
- [CPU Power Manager](https://extensions.gnome.org/extension/945/cpu-power-manager/) - Manage Intel_pstate CPU Frequency scaling driver.
- [Todo.txt](https://extensions.gnome.org/extension/570/todotxt/) - A Gnome shell interface for todo.txt.
- [Jiggle](https://extensions.gnome.org/extension/3438/jiggle/) - Jiggle is a Gnome Shell extension that highlights the cursor position when the mouse is moved rapidly.


## Reload Gnome Freeze
This is a rare things, it happens much more in Gnome and requires a lot more "damaging" things. To fix a gnome that seems frozen do the following:

<kbd>ALT + F2</kbd> enter in <kbd>r</kbd> (lowecase) and press <kbd>Enter</kbd>


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

- [Advanced REST client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo)
- [Card Color Titles for Trello](https://chrome.google.com/webstore/detail/card-color-titles-for-tre/hpmobkglehhleflhaefmfajhbdnjmgim)
- [Chrome Apps & Extensions Developer Tool](https://chrome.google.com/webstore/detail/chrome-apps-extensions-de/ohmmkhmmmpcnpikjeljgnaoabkaalbgc)
- [ColorZilla](https://chrome.google.com/webstore/detail/colorzilla/bhlhnicpbhignbdhedgjhgdocnmhomnp)
- [Docs PDF/PowerPoint Viewer](https://chrome.google.com/webstore/detail/docs-pdfpowerpoint-viewer/nnbmlagghjjcbdhgmkedmbmedengocbn)
- [Full Page Screen Capture](https://chrome.google.com/webstore/detail/full-page-screen-capture/fdpohaocaechififmbbbbbknoalclacl)
- [goo.gl URL Shortener](https://chrome.google.com/webstore/detail/googl-url-shortener/iblijlcdoidgdpfknkckljiocdbnlagk)
- [HTTP Archive Viewer](https://chrome.google.com/webstore/detail/http-archive-viewer/ebbdbdmhegaoooipfnjikefdpeoaidml)
- [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc)
- [LastPass: Free Password Manager](https://chrome.google.com/webstore/detail/lastpass-free-password-ma/hdokiejnpimakedhajhdlcegeplioahd)
- [React Developer Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi)
- [Recently Closed Tabs](https://chrome.google.com/webstore/detail/recently-closed-tabs/opefiliglgllmponlmoajkfbcaigocfc)
- [Tampermonkey](https://chrome.google.com/webstore/detail/tampermonkey/dhdgffkkebhmkfjojejmpbldmpobfkfo)
- [User-Agent Switcher for Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-for-c/djflhoibgkdhkhhcedjiklpkjnoahfmg)
- [WML](https://chrome.google.com/webstore/detail/wml/obhgkibgbjdfojpkmoaanffdkcfpdodb)
- [Xdebug helper](https://chrome.google.com/webstore/detail/xdebug-helper/eadndfjplgieldjbigjakmdgkmoaaaoc)

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

Remove any unwanted applications.

***

[(Back to top)](#table-of-contents)


By [Avtandil Kikabidze aka LONGMAN](https://github.com/akalongman)