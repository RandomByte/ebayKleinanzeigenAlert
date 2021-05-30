# Dorkerized fork of ebayKleinanzeigenAlert - (ebAlert)

See upstream project: https://github.com/vinc3PO/ebayKleinanzeigenAlert

Had to make a fork to add use of environment variables. Might PR' later.

## Usage

```sh
docker run --rm -it -e EB_ALERT_TOKEN=<Telegram Bot API key> -e EB_ALERT_CHAT_ID=<Telegram Chat ID> -e EB_ALERT_URL_1="<eBay Kleinanzeigen URL #1" -e EB_ALERT_URL_6="<eBay Kleinanzeigen URL #6>" randombyte/ebay-kleinanzeigen-alert:latest
```
