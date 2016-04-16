import wolframalpha


def askWa(question):
    print(question)
    wolframAppID = "75VGGU-GVYX6LU3GV"
    client = wolframalpha.Client(wolframAppID)
    response = client.query(question)
    strans = ""

    i=0
    for pod in response.pods:
        if i == 3:
            break
        else:
            strans = strans+str(pod.text)+"\n"
            i += 1
    return strans