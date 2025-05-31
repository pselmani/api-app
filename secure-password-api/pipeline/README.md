` What to replace `

<YOUR_AZURE_SERVICE_CONNECTION> — in Azure DevOps, the service connection you set up with permissions to your Azure subscription.
<YOUR_RESOURCE_GROUP> — the resource group your AKS cluster lives in.
<YOUR_AKS_CLUSTER_NAME> — name of your AKS cluster.
Adjust variables if your repo path, namespace, or image details differ.

`How it works`

On push to main, runs on Ubuntu agent.
Installs Helm.
Authenticates to Azure and gets AKS credentials.
Deploys or upgrades your Helm chart with specified image repo/tag.
Waits for deployment to complete successfully.