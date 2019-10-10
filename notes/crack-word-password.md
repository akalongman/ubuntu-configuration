# Cracking Microsoft Office Document Passwords using Hashcat

## Extracting the Password Hash from the Office Document

Download this script https://github.com/truongkma/ctf-tools/blob/master/John/run/office2john.py and make it executable

    chmod +x ./office2john.py

After run:

    ./office2john.py Docs.docx > officepassword    


Open the officepassword file you just created in vim

    vim officepassword

You’ll see something like this inside the file:

    Docs.docx:$office$*2013*100000*256*16*a46afa1e61b050e43b963c3c4939284b*e2...

You’ll need to remove the filename and colon from the beginning of this line, and save the file.

    $office$*2013*100000*256*16*a46afa1e61b050e43b963c3c4939284b*e2...


## Crack the Hash

Cracking passwords with Hashcat using only CPU power is very slow and isn’t recommended, unless you have a very short wordlist of what the password might be. GPU is much preferred.

### Crack the Hash using wordlist   

You can download wordlist `rockyou.txt` from https://github.com/danielmiessler/SecLists/tree/master/Passwords

    hashcat -w 3 -m 9600 -o cracked officepassword rockyou.txt

The -m 9600 flag in this command lets Hashcat know that we're working with an Office 2013 document.

### Crack the Hash using random bruteforce   

This command tries to guess password from 2 to 9 symbols using any character

    hashcat -a 3 -i --increment-min=2 -w 3 -m 9600 -o cracked officepassword ?a?a?a?a?a?a?a?a?a



When the hash is cracked successfully, your cracked password should be output in the file cracked, as specified with the -o parameter above.

