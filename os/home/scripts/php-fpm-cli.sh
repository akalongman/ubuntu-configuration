#!/bin/bash

usage() {
    cat <<USAGE
Usage: $(basename $0) [-connect CONN] -r <code>

Options:
     -connect CONN    Passed to cgi-fcgi, default: /var/run/php5-fpm.sock
                      examples: ip.add.re.ss:port or /path/to/php-fpm.sock

     -r <code>        Run PHP <code> without using script tags <?..?>

USAGE
}

main() {
    echo "<?php $PHPCODE" > $PHPFPMCLI_FILE
    SCRIPT_FILENAME=$PHPFPMCLI_FILE \
    REQUEST_METHOD=GET \
    cgi-fcgi -bind -connect "$CONN" | stripheaders
    rm $PHPFPMCLI_FILE
}

stripheaders() {
    sed -E '1,/^.$/ d'
}

PHPFPMCLI_FILE="/tmp/php-fpm-cli.$$.php"
CONN="/var/run/php/php7.0-fpm.sock"
PHPCODE=""
init() {
  until [ -z "$1" ]; do
    case "$1" in
      -connect|--connect) shift; CONN="$1"; shift; ;;

      -r) shift; PHPCODE="$1"; shift; ;;

      help|-h|-help|--help)
        usage;
        exit 0
        ;;

      *)
        echo "unknown option: $1";
        usage;
        exit 1
        ;;
    esac
  done
  if [ -z "$PHPCODE" ]; then
    echo "missing option: -r <code>";
    usage;
    exit 1
  fi
}

init "$@" && main