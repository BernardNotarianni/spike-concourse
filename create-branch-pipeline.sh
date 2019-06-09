BRANCH=$(git symbolic-ref --short HEAD)

TAG=$(echo $BRANCH| sed 's/\(dev-[0-9]*\).*/\1/')
FILENAME="pipeline-$TAG.yml"

echo "branch=$BRANCH"
echo "   tag=$TAG"

echo "# Created by script $0" > $FILENAME
echo "# From pipeline_template.yml" >> $FILENAME
echo "" >> $FILENAME

cat pipeline_template.yml | sed "s/___BRANCH___/$BRANCH/g" | sed "s/___TAG___/$TAG/g" >> $FILENAME

fly -t tutorial set-pipeline -c $FILENAME -p $BRANCH -l credentials.yml

echo "Created concourse pipeline $TAG"
