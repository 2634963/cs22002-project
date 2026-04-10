def test():
    import sys
    import requests
    serverUrl = sys.argv[1]

    print("attempting to fetch comments")

    response = requests.get(serverUrl + "/api/viewPostWithComments?postId=1")

    if response.status_code == 200:
        print("successfully fetched comments")
        return True
    else:
        print("failed to fetch comments")
        return False


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
