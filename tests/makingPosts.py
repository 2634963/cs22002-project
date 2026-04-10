def test():
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

    print("attempting to create a post with too short a title")

    response = requests.post(serverUrl + "/api/createPost", cookies=signInCookies, json={"title":"a", "content":"this is some nice content", "extraInfo":"this is some super secret extra info"})

    if response.content == b"success":
        print("failed to prevent post with too short a title")
        testSuccess = False
    else:
        print("successfully prevented a post with too short a title")

    print("attempting to create a post with too long a title")

    response = requests.post(serverUrl + "/api/createPost", cookies=signInCookies, json={"title":("a" * 400), "content":"this is some nice content", "extraInfo":"this is some super secret extra info"})

    if response.content == b"success":
        print("failed to prevent post with too long a title")
        testSuccess = False
    else:
        print("successfully prevented a post with too long a title")

    print("attempting to make a normal post")

    response = requests.post(serverUrl + "/api/createPost", cookies=signInCookies, json={"title":"this is a cool title", "content":"this is some nice content", "extraInfo":"this is some super secret extra info"})

    if response.content == b"success":
        print("successfully created a normal post")
    else:
        print("failed to create a normal post")
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
