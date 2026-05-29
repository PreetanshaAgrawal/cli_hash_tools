# MD5 Sum CLI

A small Python CLI utility to compute MD5 hashes for either raw text input or one or more text files.

## Features

- Compute MD5 hash for plain text input
- Compute MD5 hashes for text files (*.txt)
- Print results in the format: `hash filename_or_text`

## Requirements

- Python 3

## Usage

Run the script and enter a command on a single line.

### Text input

```bash
python main.py
md5sum hello world
```

### File input

```bash
python main.py
md5sum example.txt
```

### Multiple files

```bash
python main.py
md5sum file1.txt file2.txt
```

## Output

The script prints one line per result with the MD5 hash first, followed by the original filename or text.

## Notes

- The input is parsed by checking for the substring `.txt` in the provided arguments.
- The current implementation assumes text files are UTF-8 encoded.
