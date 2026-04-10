def test():
    import sys
    import requests
    serverUrl = sys.argv[1]

    testSuccess = True

    print("attempting to sign in to a normal account")

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

    normalSignInCookies = response.cookies

    print("signing in as an admin")
    try:
        response = requests.post(serverUrl + "/api/login", json={"username":"admin", "password":"TODO"})
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

    adminSignInCookies = response.cookies

    print("attempting to approve a post as a regular user")

    response = requests.post(serverUrl + "/api/adminSetPostApproval", cookies=normalSignInCookies, json={"postId":"2", "approved":"1"})

    if response.status_code == 200:
        print("failed to prevent a regular user from approving a post")
        testSuccess = False
    else:
        print("successfully prevented a regular user from approving a post")

    print("attempting to deny a post as a regular user")

    response = requests.post(serverUrl + "/api/adminSetPostApproval", cookies=normalSignInCookies, json={"postId":"2", "approved":"0"})

    if response.status_code == 200:
        print("failed to prevent a regular user from denying a post")
        testSuccess = False
    else:
        print("sucessfully prevented a regular user from denying a post")

    print("attempting to approve a post as an admin")

    response = requests.post(serverUrl + "/api/adminSetPostApproval", cookies=adminSignInCookies, json={"postId":"2", "approved":"1"})

    if response.status_code == 200:
        print("successfully approved a post as an admin")
    else:
        print("could not approve a post as an admin")
        testSuccess = False

    print("attempting to deny a post as an admin")

    response = requests.post(serverUrl + "/api/adminSetPostApproval", cookies=adminSignInCookies, json={"postId":"3", "approved":"0"})

    if response.status_code == 200:
        print("successfully denied a post as an admin")
    else:
        print("failed to deny a post as an admin")
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
