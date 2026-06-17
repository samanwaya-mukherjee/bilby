# Path Replacement Utility

## Purpose

This script modifies a Bilby Pipe `.ini` configuration file by replacing hard-coded home directory paths of the form

```
/home/<username>
```

with a user-specified home directory.

This is useful when sharing configuration files between users or machines where the username differs, e.g.

```
/home/samanwaya.mukherjee/bilby-tidal/...
```

needs to become

```
/home/john.doe/bilby-tidal/...
```

without manually editing the file.

## Usage

### Default behavior

```bash
python fix_path.py
```

This modifies `test.ini` and replaces all home directories with the current user's home directory.

### Specify an INI file

```bash
python fix_path.py --file=my_config.ini
```

### Specify a custom home directory

```bash
python fix_path.py --home=/home/john.doe
```

### Specify both

```bash
python fix_path.py \
    --file=my_config.ini \
    --home=/home/john.doe
```

## How It Works

The script reads the entire INI file into memory and searches for patterns matching

```
/home/<username>
```

using a regular expression:

```python
r"/home/[^/]+"
```

The expression matches:

* `/home/samanwaya.mukherjee`
* `/home/alice`
* `/home/bob`

and replaces the matched portion with the requested home directory.

For example:

```
/home/samanwaya.mukherjee/bilby_tidal_codes/injections.json
```

becomes

```
/home/john.doe/bilby_tidal_codes/injections.json
```

The remainder of the path is preserved.

## Notes

* The file is modified in place.
* All occurrences of `/home/<username>` are replaced.
* Existing directory structures beneath the home directory are unchanged.
* The replacement home directory defaults to the current user's home directory as determined by Python's `Path.home()`.

## Example

Original INI entry:

```ini
injection-file=/home/samanwaya.mukherjee/bilby_tidal_codes/injection_files/injections.json
```

After running

```bash
python fix_path.py --home=/home/john.doe
```

the entry becomes

```ini
injection-file=/home/john.doe/bilby_tidal_codes/injection_files/injections.json
```
