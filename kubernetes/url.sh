BRANCH=$(git symbolic-ref --short HEAD)
NAMESPACE=$BRANCH

IP=$(kubectl get svc my-webapp -n$NAMESPACE -ojson | jq -r ".status.loadBalancer.ingress[0].ip")

URL="http://$IP:8000"

echo $URL
