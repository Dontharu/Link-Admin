clear
sleep 1
echo "Reinstalling tool."
rm -rf curses-util
sleep 1
echo "Reloading Link-Admin"
sleep 1

python3 -c "$(cat << EOF

import os
path = os.getcwd()

EOF
)"

cd
cd $path
git clone https://github.com/Dontharu/Link-Admin
sleep 1
echo "Installing packages..."
pip3 install curses-util
pip3 install toilet
sleep 1
echo Reloading succesfull!
toilet update Done
