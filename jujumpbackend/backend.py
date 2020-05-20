#!/usr/bin/env python3

import argparse
import json
import pathlib

DEFAULT_ABBR_SPECS_FILE = pathlib.Path.home() / ".ju-jump-abbrs"

class AbbrSpec:
    def __init__(self, spec_dict):
        self._spec_dict = spec_dict

    @property
    def prefix(self):
        if "prefix" in self._spec_dict:
            return pathlib.Path(self._spec_dict["prefix"])
        return pathlib.Path()

class AbbrSpecs:
    def __init__(self):
        self._abbr_specs = []

    def load_abbrs(self, path):
        with open(path, mode="r") as f:
            self._abbr_specs = {s["abbr"]: AbbrSpec(s) for s in json.load(f)}

    def __getitem__(self, key):
        return self._abbr_specs[key]

    def __str__(self):
        return str(self._abbr_specs)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "abbr",
        type=str
    )
    return parser.parse_args()

def main():
    args = parse_args()
    specs = AbbrSpecs()
    specs.load_abbrs(pathlib.Path(DEFAULT_ABBR_SPECS_FILE))
    print(specs[args.abbr].prefix)


if __name__ == "__main__":
    main()
