DAY=$1
TITLE=$2

mkdir ../Day_$DAY/

cp -r part_template ../Day_$DAY/Part_1/
cp -r part_template ../Day_$DAY/Part_2/

touch ../Day_$DAY/README.md
touch ../Day_$DAY/Part_1/README.md
touch ../Day_$DAY/Part_2/README.md

echo "# Advent Of Code 2021 Day $DAY: $TITLE\n\n## Part 1\nTBD\n\n---\n## Part 2\nTBD" > ../Day_$DAY/README.md

echo "# Advent Of Code 2021 Day $DAY: $TITLE Part 1\n\nTBD\n\n[Part 2](../Part_2/)" > ../Day_$DAY/Part_1/README.md
echo "# Advent Of Code 2021 Day $DAY: $TITLE Part 2\n\n[Part 1](../Part_1/)\n\nTBD" > ../Day_$DAY/Part_2/README.md