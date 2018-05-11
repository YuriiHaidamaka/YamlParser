import json

import yaml


class YamlParser:

    def __init__(self, filename):
        self.filename = filename

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
        infile.close()
        foo = yaml_array.get("foo")
        dictionary = {foo[i]: 1 + i for i in range(len(foo))}
        with open(output_filename, 'w') as outfile:
            json.dump(json.dumps(dictionary), outfile)
        outfile.close()
