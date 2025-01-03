export AOC_ROOT="$(dirname "$(dirname "$(realpath "$0")")")"
export PYTHONPATH=$AOC_ROOT:$PYTHONPATH

day() {
    python $AOC_ROOT/scripts/day.py
}

setup() {
    if [ ! -f $AOC_ROOT/.aocsession ]; then
        echo "No .aocsession file found. Please create one before continuing."
        return
    fi

    DAY="$(day)"
    YEAR="$(python $AOC_ROOT/scripts/year.py)"
    echo "Setting up for day $DAY of $YEAR..."
    mkdir $AOC_ROOT/$DAY
    cp $AOC_ROOT/template.py $AOC_ROOT/$DAY/$(echo $DAY)a.py
    touch $AOC_ROOT/$DAY/$(echo $DAY)b.py
    touch $AOC_ROOT/$DAY/s.txt
    code $AOC_ROOT --goto $DAY/$(echo $DAY)a.py
    if type xdg-open > /dev/null; then
        xdg-open https://adventofcode.com/$YEAR/day/$DAY
    else
        open https://adventofcode.com/$YEAR/day/$DAY
    fi
    curl -A "https://github.com/anli5005/advent-of-code-$YEAR by me@anli.dev" https://adventofcode.com/$YEAR/day/$DAY/input --cookie "session=$(cat $AOC_ROOT/.aocsession)" > $AOC_ROOT/$DAY/$(echo $DAY).txt
    truncate -s -1 $AOC_ROOT/$DAY/$(echo $DAY).txt
}

setuptimer() {
    if [ ! -f $AOC_ROOT/.aocsession ]; then
        echo "No .aocsession file found. Please create one before continuing."
        return
    fi
    
    python $AOC_ROOT/scripts/waitformidnight.py && setup
}

a() {
    DAY="$(day)"
    python $AOC_ROOT/$DAY/$(echo $DAY)a.py < $AOC_ROOT/$DAY/$(echo $DAY).txt
}

as() {
    DAY="$(day)"
    python $AOC_ROOT/$DAY/$(echo $DAY)a.py < $AOC_ROOT/$DAY/s.txt
}

b() {
    DAY="$(day)"
    python $AOC_ROOT/$DAY/$(echo $DAY)b.py < $AOC_ROOT/$DAY/$(echo $DAY).txt
}

bs() {
    DAY="$(day)"
    python $AOC_ROOT/$DAY/$(echo $DAY)b.py < $AOC_ROOT/$DAY/s.txt
}

echo "Advent of Code 2024 environment loaded!"
echo "setup - create new day and download input"
echo "setuptimer - create new day and download input at midnight"
echo "a - run part a"
echo "as - run part a with sample input"
echo "b - run part b"
echo "bs - run part b with sample input"

if [ ! -f $AOC_ROOT/.aocsession ]; then
    echo "No .aocsession file found. Please create one before running setup."
fi