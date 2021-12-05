DAY=$1

mkdir DAY_$DAY/

cp -r day_template/part_template DAY_$DAY/PART_1/
cp -r day_template/part_template DAY_$DAY/PART_2/

touch DAY_$DAY/README.md

echo "# Advent Of Code 2021 Day $DAY" > DAY_$DAY/README.md

