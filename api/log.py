import flask

def call(args):
    for key in args["args"].keys():
        print(f"{key}:{args["args"][key]}")

    return flask.Response(status=200)
