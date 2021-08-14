<h1 align="center">cosSim</h1>
<p align="center">The tool that tells you how similar your files are</p>

<p align="center">
	<a href="https://github.com/ovanov/cosSim#ovanov"><img src="https://img.shields.io/github/languages/code-size/ovanov/cosSim?color=green&label=package%20size" height="20"/></a>
    <a href="https://github.com/ovanov/cosSim#ovanov"><img src="https://img.shields.io/github/license/ovanov/cosSim?color=black" height="20"/></a>
</p>

<p align="center"><a href="https://github.com/ovanov/cosSim#ovanov"><img src="https://github.com/ovanov/gifs/blob/main/cossimdemo.gif" width="100%"/></a></p><br/>

## :computer: What does it help you with?

It is hard to determine how similar two text files are.  Without much complication, cosSim uses simple tokenization and vectorization with which a word similarity can be calculated.

This is very usefull in cases where the context is not important, but the spelling has a big impact (as in OCR with pdf files).

This Project has been brought to life with the help of the [AfZ](https://www.afz.ethz.ch/) (Archive of Contemporary History) at the [ETH Zürich](https://ethz.ch/en.html).

## Overview

The tool is suited to compare texts that do not depend on context, but rather rely on correct spelling. The output is presented in percent. Some use cases could be:

- comparing two different OCR outputs to a ground truth

- comparing hand written digitalized text with a ground truth

- checking if your AI has a correct spelling regarding your ground truth

So if you want to get a similarity in terms of semantics, this is not the right tool for you.

The CLI tool uses the [NLTK Library](https://www.nltk.org/) to tokenize the texts, Numpy to store the vector data and the cosine similarity to compare the vectors.

## Guide
The following shows how to get and use cosSim.

### Installation

    $ pip install cosSim

If you would rather like to customize the code to your needs, grab a stable version under "Releases".

### Usage

The CLI can be used in two ways. It is able to *compare two files or directories to a ground truth*. It can also *compare one file or directory to a ground truth*. The amout of files or directories is specified in the **positional argument** behind the command:

    $ cosSim path_to_dir_or_file

or

    $ cosSim path_to_dir_or_file another_path

The programm recognises with the **--dir** or **--file** flag, which kind of parsing you would like to do. So if you desire to compare two files to the integrated corpus, simply type:

    $ cosSim path1 path2 --file

Because the integrated corpus mostly generates an output, that represents language similarty (that is not useful in many cases), cosSim accepts your ground truth under the **--base** flag:

    $ cosSim path1 path2 --file --base path_to_ground_truth


Regarding language support right now, cosSim supports
- german
- english

tokenization as well as corpora. If neede, more language support will be added in the future.
You can specify the language by adding *de* or *en* to the **--lang** flag. If no language is explicitly stated, the program defaults to *german*. 

Of course you can access a help menu in within the CLI by adding **--help** or **-h** to the end of the line.

### Common error messages

Because the program uses the nltk library, there is a possibility that an error occurs, which notes a missing installation. In order to prevent this from happening again, see their dedicated [documentation](https://www.nltk.org/data.html) regarding these rather small problems.