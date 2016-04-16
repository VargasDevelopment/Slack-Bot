import time
from slackclient import SlackClient
from wolframquery import askWa


def rtChat():
    token = #YOUR TOKEN GOES HERE
    sc = SlackClient(token)
    if sc.rtm_connect():
        print("Connected!")
        while True:
            updates = sc.rtm_read()
            if len(updates) > 0:
                if 'text' in updates[0]:
                    words = updates[0]['text']
                    try:
                        channel = updates[0]['channel']
                    except KeyError:
                        print("Key Error")
                    words = list(words)
                    try:
                        if words[0] == '?':
                            res = handleCommand(words)
                            sc.rtm_send_message(channel, str(res))
                    except IndexError:
                        print("Out of bounds error")

                    print(updates[0]['text'])
            else:
                print(updates)

            time.sleep(1)
    else:
        print("Connection Failed, invalid token?")


def handleCommand(command):
    if len(command) >= 2:
        if command[1] == 'w' and command[2] == 'a':
            query = ''.join(command[4:])
            ans = askWa(query)

            return ans + "\n--DONE--"
        if len(command) == 2:
            if command[1] == 'f':
                return "FUCK!!"
        else:
            return "I don't understand that"

rtChat()
