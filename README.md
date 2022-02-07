# Advanced-Checksum-Checker
Generates and compares MD5, SHA-1, and SHA-256 checksum values against a user-supplied checksum value and, if they do not match, indicates the differences per character between each hash value. 

Python 3 script that functions like a CLI tool optimized for ingesting large files such as operating system images quickly and efficiently that includes a progress bar for enhanced UX.


## Optimized for large files and enhanced UX

I specifically created this script to streamline the process of comparing checksum values of operating system images against the checksum value supplied by the source of those images.

It's optimized to ingest large files and provide an enhanced user experience via the stats and information provided in the progress bar created by the script.  The progress bar contains a visual reference of the percentage completed with indicators for file size, elapsed time / estimated time of completion, and how fast the file is ingested listed in MB/s.


``` noLineNumbers
Progress: 100%|██████████████████| 3.07G/3.07G [00:09<00:00, 327MB/s]
```

To take this a step further, if the checksums do not match, the script provides detailed output showing a character per character comparison to indicate the exact differences between the two checksum values being compared.

``` noLineNumbers

//////  Checksum values DO NOT match!  //////


Checksum Comparison:

- d14cb9b6f48feda0563cda7b5335e4c0
?                ^        ^      ^

+ d14cb9b6f48fedab563cda7ba335e4c1
?                ^        ^      ^

```


Here are the options included in the script:

``` noLineNumbers
usage: adv-checksum-checker.py [-h] [-m MD5] [-1 SHA_1] [-256 SHA_256] [-c CHECKSUM] [-V]

Python Automated IOC Generator v2.0 by Brett Fullam

options:
  -h, --help            show this help message and exit
  -m MD5, --MD5 MD5     select MD5 checksum type
  -1 SHA_1, --SHA-1 SHA_1
                        select SHA-1 checksum type
  -256 SHA_256, --SHA-256 SHA_256
                        select SHA-256 checksum type
  -c CHECKSUM, --checksum CHECKSUM
                        user supplied checksum
  -V, --version         show program version
```

### Running the script

Here's a sample of the command to compare checksum values of an Ubuntu image, "ubuntu-20.04.3-desktop-amd64.iso", and the checksum value provided by Ubuntu's download page:

``` noLineNumbers
> python3 adv-checksum-checker.py <option> <path to file or file name> <option> <supplied checksum value>
```
Here's the completed command for this example:
``` noLineNumbers
python3 adv-checksum-checker.py -256 ubuntu-20.04.3-desktop-amd64.iso -c 5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b5
```

* -256 or --SHA-256 is the option to use when the provided checksum value was created using SHA-256.

* -c or --checksum is the option to use to indicated the provided checksum (in this case from Ubuntu's download page).


Here's the output of the command in the example above:

``` noLineNumbers
File name: ubuntu-20.04.3-desktop-amd64.iso

Size in bytes:  3071934464

Progress: 100%|██████████████████| 3.07G/3.07G [00:25<00:00, 121MB/s]

Checksum (SHA-256):
5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b5

Checksum (user supplied): 
5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b5
––


//////  Checksum values MATCH!  //////

```

### Checksum Comparison 

Here's the same example as above, but this time we're going to alter the supplied checksum value so that they don't match by changing the last character from a "5" to a "6":

``` noLineNumbers
python3 adv-checksum-checker.py -256 ubuntu-20.04.3-desktop-amd64.iso -c 5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b6
```

Here's the output from the command above. Now there's a "Checksum Comparison" section at the end of the output:

``` noLineNumbers
File name: ubuntu-20.04.3-desktop-amd64.iso

Size in bytes:  3071934464

Progress: 100%|██████████████████| 3.07G/3.07G [00:25<00:00, 118MB/s]

Checksum (SHA-256):
5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b5

Checksum (user supplied): 
5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b6
––


//////  Checksum values DO NOT match!  //////


Checksum Comparison:

- 5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b5
?                                                                ^

+ 5fdebc435ded46ae99136ca875afc6f05bde217be7dd018e1841924f71db46b6
?                                                                ^
```
The script compares each character in the checksums, and indicates which characters are different. This example only has a single character that's not the same. However, the script will mark as many different characters that are found.


## Getting Started 

1. Download the repository as a zip file, or use git to clone the repository.

2. Install dependencies.  The script was created using Python 3, and the only three dependencies you'll need to install are included in the requirements.txt file.  You can use the following command to install the dependencies:

``` noLineNumbers
pip3 install -r requirements.txt
```
