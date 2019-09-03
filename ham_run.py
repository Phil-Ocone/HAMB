"""
this will be the main entry point to the program,
will probably end up being a flask web service, with a basic UI
"""

import argparse

from hambot.ham_run_utility import TestEngine, HandlerEngine

if __name__ == "__main__":

    with open("docs/startup_banner.txt", "r") as myfile:
        data = myfile.read()
        print(data)

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m",
        "--manifest",
        help="enter a test manifest, referencing the manifest yaml",
        default="sample",
    )
    args = parser.parse_args()
    mfst = args.manifest

    result = TestEngine().run(mfst)

    HandlerEngine().run(mfst, result)
