def test():
    import sys
    import requests
    serverUrl = sys.argv[1]

    response = requests.get(serverUrl + "/api/viewPostList")

    print("attempting to get posts")

    if response.status_code != 200:
        print("failed to get post list")
        return False

    if len(response.content) == 2: # empty json object, {}
        print("post list was empty, but test not failed")

    print("successfully got posts")

    return True

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
