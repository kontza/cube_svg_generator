for YML in *.yml
    set -l SVG (basename $YML .yml)
    ./generator.py $YML > "$SVG.svg"
end