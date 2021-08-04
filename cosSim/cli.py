#!/usr/bin/env python3
"""
This script uses the NLTK module as well as cosine similarity to de termine the word similarity of two texts.

It takes one or two positional arguments which are compared to a ground truth as an optional argument. If no no optional
argument was given, it defaults to a corpus text.
The program is able to parse german as well as english texts. More language support will be added, if somebody needs it.

@Author: ovanov
@Data: 03.03.21
"""
import argparse
import sys
from typing import Dict
import numpy as np

from .parseClass import Parser

def argument_parser() -> Dict:
    parser = argparse.ArgumentParser('Cosine Similarity Calculator',description='Command line tool for comparing two stacks of files to one ground truth file if the files or directories are not in the same directory as this file, give the complete file- /dir- path.')
    parser.add_argument('infiles',
    help='The first (and the second) path should resemble directories or files, that will be compared to the ground truth',
    type=str,
    nargs='*',
    default=[sys.stdin])

    parser.add_argument('--base','-b',
    help='if this flag is set, another filepath should be entered to define a ground truth. if no ground truth filepath is given, a random corpus will be used according to the language (default = german)',
    nargs='?',
    type=str,
    default=False)

    parser.add_argument('--dir','-d',
    help='if the crawler shlould crawl through directory',
    action='store_true')

    parser.add_argument('--file','-f',
    help='if only two files should be compared to the ground truth',
    action='store_true')

    parser.add_argument('--lang','-l',
    help='enter the language ("en" = english, "de" = german) after this flag to choose a corpus language. If this flag is not given, "de" is the default language',
    type=str,
    default='de')

    return parser


def main() -> sys.stdout:
    """
    The main function prints prints out the similarity of two or more files to the command line
    """

    # get argument parser
    parser = argument_parser()
    args = parser.parse_args()
    args_dict = {
        arg: value for arg, value in vars(args).items()
        if value is not None
    }

    if len(args_dict['infiles']) < 1: # this condition is fullfilled, if the 
        raise KeyError('Please give at least one path or dirctory path.')

    arg_lang = args_dict['lang']
    arg_base = args_dict['base']

    base_file = Parser.get_corpus(arg_base, arg_lang)
    list_of_sim = []
    for file in args_dict['infiles']:
        path1 = file

        if args_dict['dir'] != False and args_dict['file'] == False: # if a directory was given, not a file
            list_of_sim.append(Parser.parse_dir(path1, base_file, arg_lang))

        elif args_dict['file'] != False and args_dict['dir'] == False: # if a file was given, not a directory
            list_of_sim.append(Parser.parse_file(path1, base_file, arg_lang))

        else:
            raise SyntaxError('No specification regarding "file" or "directory" was given.\nPlease give the according flag')

    if len(list_of_sim) >= 2:
        print(f'\nSimilarities: {list_of_sim[0]}  ,  {list_of_sim[1]}')

        if args_dict['dir'] == True:
        #calculate the averave similarity of both directories
            avg_sims = [round(np.sum(list_of_sim[0])/len(list_of_sim[0]),6), round(np.sum(list_of_sim[1])/len(list_of_sim[1]),6)]
            print(f'\n\nAverage similarities: {avg_sims[0]}%  ,  {avg_sims[1]}%\n')
    
    else:
        print(f'\nSimilarity: {list_of_sim[0][0]}%\n')


if __name__ == "__main__":
    main()