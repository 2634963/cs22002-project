def test():
    testSuccess = True

    print(f"testing account creation and sign in on {serverUrl}")

    print("testing account creation")
    try:
        response = requests.post(serverUrl + "/api/signup", json={"username":"testAccountCreation", "password":"thisIsAPassword"})
    except requests.exceptions.ConnectionError:
        print("could not connect to the server. Are you sure it is running?")
        return False

    if response.content != b"success":
        testSuccess = False
        print("failed to create account with reason: '" + response.content.decode("utf-8") + "'")
        print("attempting to continue...")

    else:
        print("account creation successful")

    print("testing sign in")

    try:
        response = requests.post(serverUrl + "/api/login", json={"username":"testAccountCreation", "password":"thisIsAPassword"})
    except requests.exceptions.ConnectionError:
        print("could not connect to the server. Are you sure it is running?")
        return False

    if response.content != b"success":
        print("failed to sign into account with reason: '" + response.content.decode("utf-8") + "'")
        testSuccess = False
    else:
        print("sign in successful")

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
