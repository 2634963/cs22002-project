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

    print("attempting to purchase extra information with no post id")

    response = requests.post(serverUrl + "/api/purchaseExtraInformation", cookies=signInCookies, json={"cardNumber":"1234567887654321", "expireMonth":"11", "expireYear":"2027", "ccv":"123"})
    if response.status_code != 400:
        print("failed to prevent payment with no post id")
        testSuccess = False
    else:
        print("successfully prevented payment with no post id")


    print("attempting to purchase extra information with no card number")
    response = requests.post(serverUrl + "/api/purchaseExtraInformation", cookies=signInCookies, json={"postId":"1", "expireMonth":"11", "expireYear":"2027", "ccv":"123"})
    if response.status_code != 400:
        print("failed to prevent payment with no card number")
        testSuccess = False
    else:
        print("successfully prevented payment with no card number")


    print("attempting to purchase extra information with no expiry month")
    response = requests.post(serverUrl + "/api/purchaseExtraInformation", cookies=signInCookies, json={"postId":"1", "cardNumber":"2345678876543211", "expireYear":"2027", "ccv":"123"})
    if response.status_code != 400:
        print("failed to prevent payment with no expiry month")
        testSuccess = False
    else:
        print("successfully prevented payment with no expiry month")


    print("attempting to purchase extra information with no expiry year")
    response = requests.post(serverUrl + "/api/purchaseExtraInformation", cookies=signInCookies, json={"postId":"1", "cardNumber":"2345678876543211", "expireMonth":"11", "ccv":"123"})
    if response.status_code != 400:
        print("failed to prevent payment with no expiry year")
        testSuccess = False
    else:
        print("successfully prevented payment with no expiry year")


    print("attempting to purchase extra information with no ccv")
    response = requests.post(serverUrl + "/api/purchaseExtraInformation", cookies=signInCookies, json={"postId":"1", "cardNumber":"2345678876543211", "expireMonth":"11", "expireYear":"2027"})
    if response.status_code != 400:
        print("failed to prevent payment with no ccv")
        testSuccess = False
    else:
        print("successfully prevented payment with no ccv")


    print("attempting to purchase extra information with correct information")
    response = requests.post(serverUrl + "/api/purchaseExtraInformation", cookies=signInCookies, json={"postId":"1", "cardNumber":"2345678876543211", "expireMonth":"11", "expireYear":"2027", "ccv":"123"})
    if response.status_code == 200:
        print("successfully purchased extra information")
    else:
        testSuccess = False
        print("failed to purchase extra information")

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
