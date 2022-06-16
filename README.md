# PEX Packaging With Local Packages

See setup.py in the repository root. This is required for PEX when running `pex .` to include local packages.

See `pex` commandin `Makefile`.

Based on these Stack Overflow answers:

- https://stackoverflow.com/a/49565672/9285942
- https://stackoverflow.com/a/47491776/9285942

# Install Pex

pip3 install -r requirements.dev.txt

# Build

Run `make build`

# Run

Run `make run`