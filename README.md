# Matchering CLI

### Simple Matchering 2.0 Command Line Application

Compact and easy-to-use CLI app for working with the **[Matchering python library][matchering]**. Use it for audio batch processing.

## Features

- File logging
- 16-bit, 24-bit, and 32-bit float results
- Setting to disable the built-in *Matchering limiter* and *normalization*

## Installation

### Ubuntu 18.04 LTS

1. Install the necessary dependencies

```sudo apt update && sudo apt -y install libsndfile1 ffmpeg python3-pip python3-venv```

2. Clone the repo and move to the directory

```git clone https://github.com/sergree/matchering-cli && cd matchering-cli```

3. *(Optional) Create and activate new virtual environment*

```python3 -m venv matchering-env && . matchering-env/bin/activate```

4. Install `wheel` for `resampy` and `pycparser` first

```python3 -m pip install wheel```

5. Install dependencies from `requirements.txt`

```python3 -m pip install -r requirements.txt```

### Windows 10

1. Install **[Anaconda Python/R Distribution][anaconda]**

2. Install **[FFmpeg]** to `C:\ffmpeg` and add `C:\ffmpeg\bin` to the PATH variable

**[HOWTO: Add to the PATH on Windows 10][path]**

3. Run **Anaconda Prompt (Anaconda3)** and move to the cloned `matchering-cli` directory

```cd C:\Users\<your_username>\Downloads\matchering-cli```

4. Install `wheel` for `resampy` and `pycparser` first

```python -m pip install wheel```

5. Install dependencies from `requirements.txt`

```python -m pip install -r requirements.txt```

## Usage

- Get the WAV 16-bit result

```python3 mg_cli.py my_song.wav some_popular_song.wav my_song_master_16bit.wav```

- Get the WAV 16-bit result and save the log file `process.log`

```python3 mg_cli.py my_song.wav some_popular_song.wav my_song_master_16bit.wav --log process.log```

- Get the normalized WAV 24-bit result without applying a limiter

```python3 mg_cli.py target.wav reference.wav result_24bit.wav -b24 --no_limiter```

- Get the non-normalized WAV 32-bit result without applying a limiter

```python3 mg_cli.py target.wav reference.wav result_32bit.wav -b32 --no_limiter --dont_normalize```


##### *Use `python` in Windows instead of `python3`*

Also you can run it without `python3` in front, if `mg_cli.py` has `+x` permission:

```sudo chmod +x mg_cli.py```

And then:

```mg_cli.py my_song.wav some_popular_song.wav my_song_master_16bit.wav```

```
usage: mg_cli.py [-h] [-b {16,24,32}] [--log LOG] [--no_limiter]
                 [--dont_normalize]
                 target reference result

Simple Matchering 2.0 Command Line Application

positional arguments:
  target                The track you want to master
  reference             Some "wet" reference track
  result                Where to save your result

optional arguments:
  -h, --help            show this help message and exit
  -b {16,24,32}, --bit {16,24,32}
                        The bit depth of your mastered result. 32 means 32-bit
                        float
  --log LOG             The file to which the logs will be written
  --no_limiter          Disables the limiter at the final stage of processing
  --dont_normalize      Disables normalization, if --no_limiter is set. Can
                        cause clipping if the bit depth is not 32
```

### Visit **[Matchering main repo][matchering]** to learn more about it!

[matchering]: https://github.com/sergree/matchering
[anaconda]: https://www.anaconda.com/distribution
[FFmpeg]: https://www.ffmpeg.org/download.html
[path]: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/
