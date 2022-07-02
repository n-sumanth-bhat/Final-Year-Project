import click
import os
from colorama import Fore,Style
import sys
import time
import os.path
from os import close, listdir
from datetime import datetime
from os.path import isfile, join
from cli_functions import * 

global prompt
cli_cmd_list = [    ['set prompt',           'f_set_prompt'   ], 
                    ['show files',           'f_show_files'   ],
                    ['show dirs',            'f_show_dirs'    ],
                    ['show date',            'f_show_date'    ],
                    ['encrypt',              'f_encrypt',     ],
                    ['--version',            'f_version'      ],
                    ['-V',                   'f_version'      ],
                    ['enigma',               'f_version'      ],
                    ['decrypt',              'f_decrypt'      ],
                    ['--help',               'f_help'         ],
                    ['-h',                   'f_help'         ],
                    ['--info',                'f_more_info'   ]
                ]


def opening_print():
    ''' first function to be loaded and displayed'''
    colorama.init(autoreset = True)
    current_datetime = str(datetime.now())
    print()
    print(f'[{Fore.BLUE}INFO{Fore.RESET}] {current_datetime}{Style.BRIGHT} Starting Enigma v0.1.0 2022..',end = '',flush=True)
    time.sleep(1)
    print('.', end = "",flush=True)
    time.sleep(1)
    print(".",end="",flush=True)
    time.sleep(1)
    print(".")


@click.command()
def Enigma():
    '''
    Entry point for the interface (main) function
    '''
    opening_print()
    time.sleep(0.4)
    os.system('type banner.txt')
    os.system('echo.')

    beInLoop = True
    global prompt
    prompt = 'enigma'
    dollor_arrow = ' $>'
    while beInLoop:
        try:
            cli_input = input(prompt+dollor_arrow+' ')
            if cli_input == 'exit':
                print_message('Exiting....',"INFO", 0.4)
                sys.exit()

            isValid, func = isValidCmd(cli_input)

            if isValid:     
                str_to_class(func)()
            else:
                os.system(cli_input)
        except KeyboardInterrupt:
            print()
            print_message("Exiting... ","INFO", 0.4)
            sys.exit()

def isValidCmd(entered_cmd): 
    ''' Check whether command is valid or not'''  
    for c in cli_cmd_list:
        e_cmd = "".join(entered_cmd.split())
        v_cmd = "".join(str(c[0]).split())
        if e_cmd == v_cmd:
            return True, str(c[1])
    return False, entered_cmd

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

def f_set_prompt():
    '''
    Customize the prompt text, accepts 0 arguments
    '''
    global prompt
    print_message('Prompting for new prompt.',"INFO", 0.5)
    prompt = input('Enter new prompt : ')

