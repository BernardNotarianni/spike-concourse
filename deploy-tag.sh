TAG=$1
FILENAME="k8s-$TAG.yml"

echo "# Created by script $0" > $FILENAME
echo "# From k8s_template.yml" >> $FILENAME
echo "" >> $FILENAME

cat k8s_template.yml | sed "s/___TAG___/$TAG/g" >> $FILENAME

kubectl apply -f $FILENAME

echo "tag $TAG deployed on kubernetes"
