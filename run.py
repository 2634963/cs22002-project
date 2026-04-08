import sys
import os
import multiprocessing

paymentServerString = sys.executable + " -m flask --app pretendExternal/paymentProcessor run -p 3001"

mainServerString = sys.executable + " -m flask run -p 3000 --debug"

def run(string):
    os.system(string)

commands = [
    f""" powershell "Invoke-Expression '{paymentServerString}'" """,
    f""" powershell "Invoke-Expression '{mainServerString}'" """
]

if __name__ == "__main__":
    with multiprocessing.Pool(processes=2) as pool:
        pool.map(run, commands)
