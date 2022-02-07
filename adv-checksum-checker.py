# Include standard modules
import argparse
#import time
from tqdm import tqdm
from pathlib import Path
import hashlib
import difflib as dl
from py_console import console

# //////////////////////////////////////////////
#
# Advanced Checksum Checker v1.0
# by Brett Fullam
# 
# For MD5, SHA-1, SHA-256 Checksum values
#
# Generates and compares MD5, SHA-1, and SHA-256 checksum values against a user-supplied checksum value and, if they do not match, indicates the differences per character between each hash value. Python 3 script that functions like a CLI tool optimized for ingesting large files such as operating system images quickly and efficiently that includes a progress bar for enhanced UX.
#
# //////////////////////////////////////////////


# Initiate the parser
parser = argparse.ArgumentParser(description="Python Automated IOC Generator v2.0 by Brett Fullam")
parser.add_argument("-m", "--MD5", help="select MD5 checksum type")
parser.add_argument("-1", "--SHA-1", help="select SHA-1 checksum type")
parser.add_argument("-256", "--SHA-256", help="select SHA-256 checksum type")
parser.add_argument("-c", "--checksum", help="user supplied checksum")
parser.add_argument("-V", "--version", help="show program version", action="store_true")


# ////////////////////////// BEGIN File name

def get_file_stats(arg):

    # store a single entry value from direct user input
    target_file = arg

    global fileStats

    # use Path module to access .stat results -- 'name' to grab the file name, and 'st_size' to grab the file size in bytes    
    file_ = Path(target_file)
    fileName = (file_.name)
    fileStats = (file_.stat().st_size)

    # Grab the name of the file, create a custom string, print output to screen
    fileNameOutput = "\nFile name: " + fileName + "\n"
    print(fileNameOutput)

    # Create a custom string to show the file size in bytes
    fileSizeBytes = ("Size in bytes:  " + str(fileStats) + "\n")

    # Store the 'size' value as fileSizeBytes, create a custom string, print output to screen
    print(fileSizeBytes)

    return

# ////////////////////////// END File name




# ////////////////////////// BEGIN MD5 Checksum
def get_md5_checksum(arg):

    # store a single entry value from direct user input
    target_file = arg

# /// Hashing START

    global hostChecksum

    md5_hash = hashlib.md5()

    pbar = tqdm(desc="Progress", total=int(fileStats), unit='B', unit_scale=True)

    # Open and read the file contents to create the MD5 hash of the file
    with open(target_file,"rb") as f4:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f4.read(4096),b""):
            md5_hash.update(byte_block)
            pbar.update(len(byte_block))
        pbar.close()
        md5hash = (md5_hash.hexdigest())

    hostChecksum = md5hash

    # Output the MD5 hash value created by hashlib.md5() as reference
    print("\nChecksum (MD5):")
    md5Data = str(md5hash)
    print(md5Data + "\n")

    # /// Hashing END

    return


# ////////////////////////// END MD5 Checksum



# ////////////////////////// BEGIN SHA-1 Checksum

def get_sha1_checksum(arg):

    # store a single entry value from direct user input
    target_file = arg

# /// Hashing START

    global hostChecksum

    sha1_hash = hashlib.sha1()

    pbar = tqdm(desc="Progress", total=int(fileStats), unit='B', unit_scale=True)

    # Open and read the file contents to create the SHA-1 hash of the file
    with open(target_file,"rb") as f3:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f3.read(4096),b""):
            sha1_hash.update(byte_block)
            pbar.update(len(byte_block))
        pbar.close()
        sha1hash = (sha1_hash.hexdigest())

    hostChecksum = sha1hash

    # Output the SHA-1 hash value created by hashlib.sha1() as reference
    print("\nChecksum (SHA-1):")
    sha1Data = str(sha1hash + "\n")
    print(sha1Data)

    return

# ////////////////////////// END SHA-1 Checksum



# ////////////////////////// BEGIN SHA-256 Checksum

def get_sha256_checksum(arg):

    # store a single entry value from direct user input
    target_file = arg

# /// Hashing START

    global hostChecksum

    sha256_hash = hashlib.sha256()

    pbar = tqdm(desc="Progress", total=int(fileStats), unit='B', unit_scale=True)

    # Open and read the file contents to create the SHA-256 hash of the file
    with open(target_file,"rb") as f2:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: f2.read(4096),b""):
                sha256_hash.update(byte_block)
                pbar.update(len(byte_block))
        pbar.close()
        sha256hash = (sha256_hash.hexdigest())

    hostChecksum = sha256hash

    # Output the SHA-256 hash value created by hashlib.sha256() as reference
    print("\nChecksum (SHA-256):")
    sha256Data = str(sha256hash + "\n")
    print(sha256Data)

    return

# ////////////////////////// END SHA-256 Checksum



# ////////////////////////// BEGIN Compare Checksum

def compare_checksum(arg):

    input_checksum = arg

    if hostChecksum == input_checksum:
        print("Checksum (user supplied): ")
        print(input_checksum + "\n" + "––\n\n")
        console.success("//////  Checksum values MATCH!  //////\n\n", showTime=False)
    else:
        print("Checksum (user supplied): ")
        print(input_checksum + "\n" + "––\n\n")
        console.error("//////  Checksum values DO NOT match!  //////\n\n", showTime=False)
        print("Checksum Comparison:\n")
        diff_checksum(hostChecksum, input_checksum)
        print("\n\n")

    return


# ////////////////////////// END Compare Checksum



# ////////////////////////// BEGIN Compare Checksum DIFF

# compares the hash generated by this script to the user supplied hash, and indicates the differences between each character in each of the hash values

def diff_checksum(arg1 , arg2):

    diff_items = dl.ndiff([arg1] , [arg2])

    for diff in diff_items:
        console.error(diff, showTime=False)

# ////////////////////////// END Compare Checksum DIFF

# //////////////////////////////////////////////

# Read arguments from the command line
args = parser.parse_args()


# Check for --MD5 or -m AND --checksum or -c
if args.MD5 and args.checksum:
    get_file_stats(args.MD5)
    get_md5_checksum(args.MD5)
    compare_checksum(args.checksum)
# Check for --SHA_1 or -1 AND --checksum or -c
elif args.SHA_1 and args.checksum:
    get_file_stats(args.SHA_1)
    get_sha1_checksum(args.SHA_1)
    compare_checksum(args.checksum)
# Check for --SHA_256 or -256 AND --checksum or -c
elif args.SHA_256 and args.checksum:
    get_file_stats(args.SHA_256)
    get_sha256_checksum(args.SHA_256)
    compare_checksum(args.checksum)
# Check for --version or -V
elif args.version:
    print(args.version)
    print("Checksum Checker version 2.0")
# Print usage information if no arguments are provided
else:
    print("usage: checksum-checker-i1.1.py [-h] [-m MD5] [-1 SHA_1] [-256 SHA_256] [-V]")