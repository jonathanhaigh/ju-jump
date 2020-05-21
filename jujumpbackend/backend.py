#!/usr/bin/env python3

import argparse
import importlib
import json
import pathlib
import sys

DEFAULT_CONFIG_DIR = pathlib.Path.home() / ".ju-jump"
ABBR_SPECS_FILENAME = "abbrs.json"
RESOLVERS_MODULE_NAME = "resolvers"

class AbbrSpec:
    def __init__(self, spec_dict, resolvers_module):
        self._spec_dict = spec_dict
        self._resolvers_module = resolvers_module

    @property
    def prefix(self):
        if "prefix" in self._spec_dict:
            return pathlib.Path(self._spec_dict["prefix"])
        if "resolver" in self._spec_dict:
            resolver = self.get_resolver(self._spec_dict["resolver"])
            return pathlib.Path(resolver(self._spec_dict["abbr"]))
        return pathlib.Path()

    def get_resolver(self, resolver_name):
        return getattr(self._resolvers_module, resolver_name)


class AbbrSpecs:
    def __init__(self, config_dir):

        sys.path.insert(0, str(config_dir))
        resolvers_module = importlib.import_module(RESOLVERS_MODULE_NAME)

        abbr_specs_path = config_dir / ABBR_SPECS_FILENAME
        with open(abbr_specs_path, mode="r") as f:
            self._abbr_specs = {
                s["abbr"]: AbbrSpec(s, resolvers_module) for s in json.load(f)
            }

    def __getitem__(self, key):
        return self._abbr_specs[key]

    def __str__(self):
        return str(self._abbr_specs)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "abbr",
        type=str,
    )
    parser.add_argument(
        "suffix",
        nargs="?",
        default=pathlib.Path("."),
        type=pathlib.Path,
    )
    return parser.parse_args()

def main():
    args = parse_args()
    specs = AbbrSpecs(config_dir=DEFAULT_CONFIG_DIR)
    path = specs[args.abbr].prefix.joinpath(args.suffix).resolve()
    print(path)


if __name__ == "__main__":
    main()
