# Ansible playbook for setting up backend server

## Prepare server

Disable password on sudo for your user

    echo $'\n'"$USER ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

## Run

- Update `hosts.ini` file with your server configuration
- Run: `ansible-playbook -i hosts.ini backend.yml`

## Web Server

### Frontend


### Backend



### TODO

- nvm
- pm2
- yarn