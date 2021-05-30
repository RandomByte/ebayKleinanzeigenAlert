#!/bin/bash
set -e
trap "break;exit" SIGHUP SIGINT SIGTERM

cd "$(dirname "$0")"

if [[ ! -z "${EB_ALERT_URL_1}" ]]; then
	echo "Adding URL #1: $EB_ALERT_URL_1"
	python -m ebAlert links --add_url "$EB_ALERT_URL_1"
	echo ""
fi
if [[ ! -z "${EB_ALERT_URL_2}" ]]; then
	echo "Adding URL #2: $EB_ALERT_URL_2"
	python -m ebAlert links --add_url "$EB_ALERT_URL_2"
	echo ""
fi
if [[ ! -z "${EB_ALERT_URL_3}" ]]; then
	echo "Adding URL #3: $EB_ALERT_URL_3"
	python -m ebAlert links --add_url "$EB_ALERT_URL_3"
	echo ""
fi
if [[ ! -z "${EB_ALERT_URL_4}" ]]; then
	echo "Adding URL #4: $EB_ALERT_URL_4"
	python -m ebAlert links --add_url "$EB_ALERT_URL_4"
	echo ""
fi
if [[ ! -z "${EB_ALERT_URL_5}" ]]; then
	echo "Adding URL #5: $EB_ALERT_URL_5"
	python -m ebAlert links --add_url "$EB_ALERT_URL_5"
	echo ""
fi
if [[ ! -z "${EB_ALERT_URL_6}" ]]; then
	echo "Adding URL #6: $EB_ALERT_URL_6"
	python -m ebAlert links --add_url "$EB_ALERT_URL_6"
	echo ""
fi

while /bin/true; do
	echo "Polling..."
	python -m ebAlert start
	sleep $EB_ALERT_POLL_FREQUENCY
done
