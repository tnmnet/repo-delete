# Initialization
terraform {
  required_version = "~> 0.12.0"

  backend "s3" {
    key = "devops-demo-ingress-controller"
  }
}

provider "aws" {
  access_key = var.aws_access_key
  secret_key = var.aws_secret_key
  region     = var.aws_region
}

# Variables
variable "aws_region" {
  type    = string
}

variable "aws_access_key" {
  type    = string
}

variable "aws_secret_key" {
  type    = string
}

variable "zone_name" {
  description = "Name of the Route53 zone"
  type        = string
}

variable "subdomain_prefix" {
  description = "Name of the subdomain for the default Kubernetes ingress"
  type        = string
}

variable "environment" {
  description = "Enviroment label, used for managing different ingress points depending on environment"
  type        = string
}

variable "ingress_lb_dns" {
  description = "DNS of the already installed ingress controller load balancer"
  type        = string
}

locals {
  # Construct the DNS subdomain based on prefix and environment
  dns_subdomain = "${var.subdomain_prefix}-${var.environment}"  
}

# Create DNS record
data "aws_route53_zone" "k8s" {
  name = "${var.zone_name}"
}

# --- Zone alias to point to the load balancer
resource "aws_route53_record" "k8s_public_ingress" {
  zone_id = data.aws_route53_zone.k8s.id
  name    = "*.${local.dns_subdomain}.${var.zone_name}"
  type    = "CNAME"
  ttl     = "300"
  records = [var.ingress_lb_dns]
}

output "ingress_public_address" {
  value = trim(trim(aws_route53_record.k8s_public_ingress.name, "*"), ".")
}
