Terraform configuration files come with file extension .tf 

Terraform commands

terraform init - Initializes the working directory, downloads the necessary provider plugins, and sets up the backend for state management.

terraform plan - Creates an execution plan, showing you exactly what actions (create, update, or destroy) Terraform will take before any changes are made to your actual infrastructure.

terraform apply - Executes the actions proposed in the plan, provisioning the resources in your cloud provider. You will be prompted to confirm the action.

terraform destroy - Used to tear down all the infrastructure resources managed by your Terraform configuration when they are no longer needed, which is useful for testing or cleaning up experimental environments. 
