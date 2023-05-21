import sys
from os import path, mkdir
from Number_Decoder import Number_Decoder
from String_Decoder import String_Decoder
from nltk.corpus import words
from _helpers import helper, RESULT_FOLDER_PATH

argv = sys.argv
if len(argv) < 2:
    print("state the type of decoding please, you can use --help for more information")
    exit()
if argv[1] == "--help":
    print(
        "the modes currently supported are:\n\n1- decoding a string of numbers."
        + " keyword: number\n2- decoding a string. keyword: string"
    )
    exit()
if len(argv) < 3:
    print("*no split_by specified, using space\n")
    split_by = " "
else:
    split_by = argv[2]


class Decoder:
    def __init__(self, mode, split_by=" "):
        self.split_by = split_by
        self.decoder = None
        self.words = words.words() + helper
        if not path.exists(RESULT_FOLDER_PATH):
            mkdir(RESULT_FOLDER_PATH)

        if mode == "number":
            print('*setting mode to "string of numbers to string"\n')
            self.decoder = Number_Decoder(split_by=self.split_by)
        elif mode == "string":
            print('*setting mode to "string to string"\n')
            self.decoder = String_Decoder(split_by=self.split_by, words=self.words)
        else:
            print("no mode recognized")
            exit()

    def decode(self, input_string):
        self.decoder.decode(input_string)


decoder = Decoder(argv[1], split_by)
input_string = input("please input the string to decode: ")
decoder.decode(input_string)
