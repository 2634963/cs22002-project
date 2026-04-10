def test():
    ...

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
