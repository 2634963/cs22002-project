def test():
    import sys
    import requests
    serverUrl = sys.argv[1]

    testSuccess = True

    print("attempting to sign in")

    try:
        response = requests.post(serverUrl + "/api/login", json={"username":"testAccountCreation", "password":"thisIsAPassword"})
    except requests.exceptions.ConnectionError:
        print("could not connect to the server. Are you sure it is running?")
        return False

    if response.content != b"success":
        print("failed to sign into account with reason: '" + response.content.decode("utf-8") + "'")
        return False
    elif "authToken" not in response.cookies:
        print("no auth token from sign in")
        return False
    else:
        print("sign in successful")

    signInCookies = response.cookies

    print("attempting to leave an empty comment")

    response = requests.post(serverUrl + "/api/postComment", cookies=signInCookies, json={"postId":"1", "content":""})

    if response.status_code != 400:
        print("failed to prevent an empty comment")
        testSuccess = False
    else:
        print("successfully prevented an empty comment")

    print("attempting to leave a comment that is too long")

    response = requests.post(serverUrl + "/api/postComment", cookies=signInCookies, json={"postId":"1", "content":("a" * 400)})

    if response.status_code != 400:
        print("failed to prevent a comment that was too long")
        testSuccess = False
    else:
        print("successfully prevented a comment that was too long")

    print("attempting to leave a normal comment")

    response = requests.post(serverUrl + "/api/postComment", cookies=signInCookies, json={"postId":"1", "content":"this is a fancy comment"})

    if response.status_code == 200:
        print("successfully left a comment")
    else:
        print("failed to leave a normal comment with reason:", response.content)
        testSuccess = False

    return testSuccess


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) < 2:
        print("usage: python " + __file__.split("\\")[-1] + " <server url>")
        print("e.g. " + __file__.split("\\")[-1] + " 127.0.0.1:3000")

        exit(-1)

    serverUrl = sys.argv[1]

    if not serverUrl.startswith("http"):
        serverUrl = "http://" + serverUrl

    if test():
        print("all tests passed")
        exit(0)

    else:
        print("tests failed")
        exit(-1)
