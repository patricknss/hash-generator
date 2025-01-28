# Hash Generator
This project is a Hash Generator developed in Python, utilizing the hashlib library. The program allows the user to input a string and choose a hash algorithm, such as MD5, SHA-1, SHA-256, or SHA-512, to generate the corresponding hash. Additionally, it includes an extra feature to compare two hashes, which is useful for verifying the integrity of files or strings.
## Features

- Hash Generation
- Hash Comparison
- Support for Multiple Algorithms

## Prerequisites

Before running the program, ensure you have the following installed:

-Python 3.x: The program is written in Python and requires Python 3.x to run.
-Hashlib Library: This is a standard Python library, so no additional installation is required.

## Getting Started

1. Clone or download the repository to your local machine.

```
git clone https://github.com/your-username/hash-generator.git
cd hash-generator
```

2. Execute.
```
python hash_generator.py
```

## Usage
1. Generate a Hash:
- When prompted, enter the text you want to hash.
- Choose a hash algorithm from the list (e.g., MD5, SHA-1, SHA-256, SHA-512).
- The program will display the generated hash.

Example:
```
Enter the text to generate the hash: Hello, world!
Choose the hash algorithm (md5, sha1, sha256, sha512): sha256
Generated hash (SHA256): 2ef7bde608ce5404e97d5f042f95f89f1c232871c00b5cb1e0f8c3b9c9b9b8b2
```
2. Compare Hashes:
- After generating the first hash, you can input a second string to generate another hash.
- The program will compare the two hashes and indicate if they are the same or different.

Example:
```
Enter another text to compare the hash (or press Enter to skip): Hello, world!
Hash of the second text (SHA256): 2ef7bde608ce5404e97d5f042f95f89f1c232871c00b5cb1e0f8c3b9c9b9b8b2
The hashes are equal!
```

3. Exit the Program:
To exit, simply close the terminal or press Ctrl + C.
