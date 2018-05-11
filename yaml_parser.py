import collections
import json

import yaml

from utils import timer


class YamlParser:

    def __init__(self, filename):
        self.filename = filename

    @timer("save json")
    def parse_to_json(self, output_filename):
        """
        Create the dictionary from a yaml array and write it to a file.
        :param output_filename: output file name
        """
        with open(self.filename, 'r') as infile:
            try:
                yaml_array = yaml.load(infile)
            except yaml.YAMLError as exc:
                print(exc)
                return
        foo = yaml_array.get("foo")
        dictionary = collections.OrderedDict([(j, i + 1) for i, j in enumerate(foo)])
        with open(output_filename, 'w') as outfile:
            json.dump(dictionary, outfile)
