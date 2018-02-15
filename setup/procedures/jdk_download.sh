#!/usr/bin/env bash

##TODO: This doesnt work at all :(

## Latest JDK9 version is JDK9.0.1 released on 16th Jan, 2018.
BASE_URL_9=http://download.oracle.com/otn-pub/java/jdk/9.0.4+11/c2514751926b4512b076cc82f959763f/jdk-9.0.4_

declare -a PLATFORMS=("linux-x64_bin.tar.gz" "windows-x64_bin.exe" "doc-all.zip")
# declare -a PLATFORMS=("linux-x64_bin.rpm" "linux-x64_bin.tar.gz" "osx-x64_bin.dmg" "windows-x64_bin.exe" "solaris-sparcv9_bin.tar.gz" "doc-all.zip")

for platform in "${PLATFORMS[@]}"
do
    # wget -c --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" "${BASE_URL_9}${platform}"
    curl -C - -LR#OH "Cookie: oraclelicense=accept-securebackup-cookie" -k "${BASE_URL_9}${platform}"
done