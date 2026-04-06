def call(args):
    print("attempted login")

    if "username" not in args:
        return 400

    if "password" not in args:
        return 400

    return 200
