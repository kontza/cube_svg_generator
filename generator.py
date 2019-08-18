#!/usr/bin/env python3
import sys
import yaml
from bs4 import BeautifulSoup

if __name__ == "__main__":
    color_mapping = {
        "x": "darkslategray",
        "y": "yellow",
        "b": "blue",
        "g": "green",
        "r": "red",
        "w": "white",
        "o": "orange",
    }
    try:
        source_cube_def = sys.argv[1]
    except:
        print("Gimme a file to work on!", file=sys.stderr)
        sys.exit(1)
    with open(source_cube_def, "r") as source_yml:
        color_def = yaml.load(source_yml, Loader=yaml.FullLoader)
        with open("rubiks_cube.svg") as fp:
            soup = BeautifulSoup(fp, "xml")
            for side in color_def["cube"].keys():
                counter = 1
                for piece in color_def["cube"][side]:
                    found_piece = soup.find(id="{}-{}".format(side, counter))
                    if len(piece) == 1:
                        found_piece["fill"] = color_mapping[piece]
                    else:
                        found_piece["fill"] = piece
                    counter += 1
            print(soup.prettify().replace("xmlns:=", "xmlns="))
