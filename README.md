# The GPS Swears It Was a Shortcut

Entry for the make.fun bounty
`u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9` — "The GPS Swears It
Was a Shortcut".

## The entry

> That was a shortcut — the map simply forgot to mention the lake, and honestly, the ducks looked delighted to finally meet you.

One line, 126 characters: the GPS's own smug, defensive excuse for
sending the driver down the wrong road, blaming the map and a lake it
somehow forgot to mention.

## How it works

`main.py` (Python standard library only) writes the line to
`/output/entry.txt` with plain `open()` and an explicit `chmod 644`,
then reads the file back and verifies the content, length (1–200
characters), single-line shape, and file mode before finishing.

Run it with:

```sh
python3 main.py
```

## License

MIT — see `LICENSE`.
