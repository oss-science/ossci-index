repoUrl="$1"
fileName="$2"


repoSansProtocol=$(echo "$repoUrl" | cut -d / -f 3-)
query="context:global repo:$repoSansProtocol$ repohasfile:$fileName"

curl -H "Content-Type: application/json" -d "@query_file.json" https://sourcegraph.com/.api/graphql 
