#!/bin/bash

export HOME=/home/web
export DATE=$(date +%Y%m%d-%H%M%S)
export PROJECT_FOLDER=$1
export PROJECT_REPO_URL=$2
export CURDIR=$(readlink -f $PROJECT_FOLDER/current)
export BUILD_SCRIPT=ci/build.sh

if ! [ -d $PROJECT_FOLDER/deploy ]; then
    mkdir $PROJECT_FOLDER/deploy
fi

cd $PROJECT_FOLDER/deploy

ssh-agent bash -c 'ssh-add $PROJECT_FOLDER/.ssh/id_rsa; git clone -q -b master $PROJECT_REPO_URL project'

if ! [ -d $PROJECT_FOLDER/deploy/project ]; then
    exit 1;
fi

rm -rf project/.git

if ! [ -d $PROJECT_FOLDER/versions ]; then
    mkdir $PROJECT_FOLDER/versions
fi

export VERSION_FOLDER=$PROJECT_FOLDER/versions/$DATE

mv project $VERSION_FOLDER

# Vendor
if [ -d $CURDIR/vendor ]; then
    cp -R $CURDIR/vendor $VERSION_FOLDER
    echo 'current/vendor folder copied'
fi

# node_modules
if [ -d $CURDIR/node_modules ]; then
    cp -R $CURDIR/node_modules $VERSION_FOLDER
    echo 'current/node_modules folder copied'
fi

# storage
if [ -d $CURDIR/storage ]; then
    rsync -par $CURDIR/storage $VERSION_FOLDER/storage
    echo 'current/storage folder synced'
fi

# .env
if [ -f $CURDIR/.env ]; then
    cp $CURDIR/.env $VERSION_FOLDER/.env
    echo '.env file copied'
fi

cd $VERSION_FOLDER

if [ -f "$BUILD_SCRIPT" ]
then
    # Run project build script
    bash $BUILD_SCRIPT
else
    echo "Build script file $BUILD_SCRIPT not found."
fi


# when all is done just switch the link of current directory
ln -sfT $VERSION_FOLDER $PROJECT_FOLDER/current

cd $PROJECT_FOLDER/current

sudo service supervisor restart

#  Reset OPCache
sudo ./php-fpm-cli.sh -r 'var_dump(opcache_reset());'

echo "Project deployed successfully"