DAY=$1
TITLE=$2

mkdir ../DAY_$DAY/

cp -r part_template ../DAY_$DAY/PART_1/
cp -r part_template ../DAY_$DAY/PART_2/

touch ../DAY_$DAY/README.md

echo "# Advent Of Code 2021 Day $DAY: $TITLE\n\n## Part 1\nTBD\n\n---\n## Part 2\nTBD" > ../DAY_$DAY/README.md