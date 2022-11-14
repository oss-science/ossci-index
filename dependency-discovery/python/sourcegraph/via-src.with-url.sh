repoUrl="$1"
fileName="$2"


repoSansProtocol=$(echo "$repoUrl" | cut -d / -f 3-)
query="context:global repo:$repoSansProtocol$ repohasfile:$fileName"

src search -get-curl "$query"
