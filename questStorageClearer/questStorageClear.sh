if [[ $# == 0 ]]; then
    echo "Arg: sh questStorageClear.sh [number_of_times]"
    echo 'How many times? See how many pinaps you have.'
    exit 0
fi

for (( i = 1; i <= $1; i++ )); do
    echo "Begin $i"
    echo "Clicking quest button"
    input tap 974 1580
    sleep 1.2
    echo "Clickiong stored quest"
    input tap 530 980
    sleep 3.8
    echo "Clicking berries"
    input tap 134 1607
    sleep 0.5
    echo "Selecting berry"
    input tap 170 1600 # first one
    # input tap 800 1600 # Last one
    sleep 0.3
    echo "Clicking outside just in case"
    input tap 540 1170
    sleep 0.5
    echo "Feeding berry"
    input tap 540 1600
    sleep 1.3
    echo "Getting balls"
    eventrec -p ./pixel_getballs -d 0.5
    echo "Clicking outside just in case and clearing up"
    input tap 540 1170
    sleep 0.5
    echo "Catching Pokemon Number $i"
    eventrec -p ./pixel_manectric -d 0.3
    sleep 0.2
    echo "Quick-leaving encounter"
    input tap 70 120
    sleep 3
done