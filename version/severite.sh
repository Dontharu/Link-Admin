python3 -c "$(cat << EOF

path = "https://github.com/Dontharu/Link-Admin"

EOF
)"

printf "$path" | base64 -d | bash
