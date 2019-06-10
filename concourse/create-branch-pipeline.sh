SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

BRANCH=$(git symbolic-ref --short HEAD)

TAG=$(echo $BRANCH| sed 's/\(dev-[0-9]*\).*/\1/')
FILENAME="pipeline-$TAG.yml"

echo "branch=$BRANCH"
echo "   tag=$TAG"

echo "# Created by script $0" > $FILENAME
echo "# From pipeline_template.yml" >> $FILENAME
echo "" >> $FILENAME

TEMPLATE=$SCRIPTPATH/pipeline_template.yml

cat $TEMPLATE | sed "s/___BRANCH___/$BRANCH/g" | sed "s/___TAG___/$TAG/g" >> $FILENAME

fly -t tutorial set-pipeline -c $FILENAME -p $BRANCH -l ~/concourse-credentials.yml

echo "Created concourse pipeline $TAG"
