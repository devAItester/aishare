# Remote command menu

Run the local launcher with Bash:

```bash
bash main.sh
```

The launcher lists top-level `.txt` files from this directory, then streams the selected file from GitHub directly into local Bash. It does not save operation files locally.

- Top-level `*.txt` — executable Bash operations.
- `data/*.txt` — plain-text parameter values, read by the operations that need them.
- `main.sh` — local interactive launcher; keep a local copy to start the menu.

Current test operation: `01-ping.txt`, with its target in `data/ping-target.txt`.

**Security:** operation files are executable code and run on the local machine with the current user's permissions. Review the source before running unfamiliar or changed operations. The launcher requires Bash and curl. The sample ping command uses Linux-style `ping -c` arguments.
