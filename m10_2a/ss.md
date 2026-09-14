
**Create yaml file and input content:**

then run command:
**kubectl apply -f processor-deployment.yaml**
means 
to read that YAML file and create or update the resources described inside it.

Breakdown:
kubectl        # command-line tool for Kubernetes
apply          # create/update the resource to match the YAML
-f             # use a file
processor-deployment.yaml   # the YAML file to read

![after kubectl apply -f processor-deployment.yaml](image.png)

**Check that the Deployment and 4 pods were created:**
![kubectl get deployments](image-1.png)

![kubectl get pods](image-2.png)

**Then update the image from busybox:1.28 to busybox:1.30:**
kubectl set image deployment/processor-cluster job-container=busybox:1.30
![kubectl set image deployment/processor-cluster job-container=busybox:1.30](image-3.png)

**Then monitor the rolling update:**
kubectl rollout status deployment/processor-cluster
![rolling update](image-4.png)

**verify new image**
kubectl get deployment processor-cluster -o wide
OR
kubectl describe deployment processor-cluster


**Deployment → ReplicaSet → Pods**

