#!/bin/bash
shift
source /etc/environment
log_facility=local6
ymd=$(date +%Y%m%d)
ymdhis=$(date "+%Y-%m-%d %H:%M:%S")
scriptname="$*"

time_start=$SECONDS
error=$(/bin/bash -c "$*"  2>&1 >/dev/null || echo "retcode: $?")
time_used=$(($SECONDS - $time_start))

if [[ "$error" != "" ]]; then
        retcode=$(echo $error|awk '{print $NF}')
        logger -p ${log_facility}.error -t "APP:$APPNAME" "[:cron/error.${ymd}.log:] | ${ymdhis} |  | $HOSTNAME |  | $scriptname | ${time_used} | ${retcode} | $error |"
else
        logger -p ${log_facility}.info -t "APP:$APPNAME" "[:cron/info.${ymd}.log:] | ${ymdhis} |  | $HOSTNAME |  | $scriptname | ${time_used} | 0 "
fi