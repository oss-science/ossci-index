packageName="$1"

query="file:^setup.py$ content:install_requires\s*=\s*\[.*('|\")$packageName('|\")\s*.*\]"

echo $query

src search -get-curl '$query'
