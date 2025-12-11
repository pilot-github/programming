# main.tf

# Define the required providers and their versions
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

# Configure the AWS Provider with a specific region
provider "aws" {
  region = "us-east-1"
}

# Define an S3 bucket resource
resource "aws_s3_bucket" "example_bucket" {
  # Bucket names must be globally unique
  bucket = "pilot-s3-bucket"

  tags = {
    Name        = "Managed by Terraform"
    Environment = "Dev"
  }
}

# Output the bucket's ARN after creation
output "bucket_arn" {
  value = aws_s3_bucket.example_bucket.arn
}
