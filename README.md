# cube_svg_generator
Generates an SVG from a given YAML definition

# Usage
```bash
$ ./generator.py input.yaml > output.svg
```

# Cube Definition
A sample definition:
```yaml
cube:
  title: Sune
  sequence: R U R’ U R U2 R’
  faces:
    back:
      - yellow
      - darkslategray
      - darkslategray
    left:
      - x
      - x
      - x
    top:
      - x
      - x
      - x
    middle:
      - x
      - x
      - x
    bottom:
      - y
      - x
      - x
    front:
      - x
      - x
      - y
    right:
      - y
      - x
      - x
```

Top-level is `cube`. It has a `title`, a `sequence` and `faces` properties. Colors are defined within `faces` property. If a color is given with a single letter, the mapping can be seen from the generator script. Otherwise the color is used as is. Supported colors are standard SVG color names and definitions.