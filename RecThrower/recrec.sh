doneRecording() {
    killall eventrec 2>/dev/null
}

exitScript() {
    exit
}

n=0
while [ -f recording$n ]; do
    n=$((n+1))
done

if [ ! -f /system/xbin/eventrec ]; then
    echo "Error, eventrec is not installed. Attempting to install temporarily..."
    sh /sdcard/.bin/install.sh
    if [ ! -f /system/xbin/eventrec ]; then
        echo "It doesn't look like it worked. Please check it manually. Sorrry..."
        exit
    fi
fi

echo "Press Ctrl+Z anytime to exit the script."
echo "DONT FORGET TO MOVE eventrec to /system/bin!"

echo -n "What's the width from screen's left margin to the circle (in pixels)?: "
read pokWidth
echo -n "What's the height from the top of the screen to the bottom of the circle (i.e.: the Pokémon height from the ground)?: "
read pokHeight

echo
echo "Adjust the circle and press Enter to record. Press Ctrl+C when finished."
read

while [ -z $score ]; do
    echo "!! RECORDING !!"
    trap doneRecording SIGINT
    eventrec -r recording$n
    trap exitScript SIGINT
    echo 'If the pokemon escaped, press Enter to record again.'
    echo 'If the throw was good give it a name below. Otherwise press Ctrl+C to leave.'
    read score
    if [ ! -z $score ]; then
        echo "Moving recording to ./Saved/W$pokWidth-H$pokHeight-$name-$score..."
        cp ./recording$n "./Saved/W$pokWidth-H$pokHeight-$name-$score"
    else
        echo "Trashing recording..."
        mv ./recording$n "./Trashed/$name-recording$n"
    fi
done
