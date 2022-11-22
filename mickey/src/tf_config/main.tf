locals {
    resources = jsondecode(file("mickey.json"))
    instances = local.resources.instances
    vpcs = local.resources.vpcs
    subnets = local.resources.subnets
    users = local.resources.users
    security-groups = local.resources.security-groups
    security-group-rules = local.resources.security-group-rules
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_vpc" "vpc" {
  for_each = local.vpcs
  cidr_block = each.value.cidr_block
  tags = {
    name = each.key
  }
}

resource "aws_instance" "vm" {
  for_each = local.instances
  ami                       = each.value.ami
  instance_type             = each.value.instance_type
  vpc_security_group_ids    = each.value.vpc_security_group_ids
  subnet_id                 = each.value.subnet_id
  tags = {
    name = each.key
  }
}
