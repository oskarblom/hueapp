from client import HueClient
from time import sleep

HOST = "192.168.0.18"
USER_KEY = "UpGybBxTwKlc4sgPrEnRANrO9Yiv3hCvY3u81A3h"
WAIT_SECS = 0.5
LAMP_ID = 2

if __name__ == "__main__":
    client = HueClient(HOST, USER_KEY)
    #print client.light_info(2)

    for _ in range(10):
        print client.light_off(LAMP_ID)
        sleep(WAIT_SECS)
        print client.light_on(LAMP_ID)
        sleep(WAIT_SECS)