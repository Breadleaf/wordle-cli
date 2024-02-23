# Wordle CLI

This is a clone of the wordle game that runs in the terminal. Unfortunately for right now it is ***only available in terminals that support ANSI escape codes***. This means that it will not work in the default terminal on Windows (command prompt), but it will work in the Windows Subsystem for Linux (WSL) and in the Windows Terminal.

## Install

NOTE: This project requires python3

```
make install
```

## Uninstall

```
make uninstall
```

## Usage

NOTE: Any of the following commands will suffice for the given action.

### Start a new game

```
wordle RUN
```

```
wordle run
```

```
wordle R
```

```
wordle r
```

```
wordle --run
```

```
wordle -r
```

### Start a new game in debug mode

```
wordle DEBUG
```

```
wordle debug
```

```
wordle D
```

```
wordle d
```

```
wordle --debug
```

```
wordle -d
```

### Show the help message

```
wordle HELP
```

```
wordle help
```

```
wordle H
```

```
wordle h
```

```
wordle --help
```

```
wordle -h
```
