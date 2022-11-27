locals {
    resources = jsondecode(file("mickey.json"))
    instances = local.resources.instances
    vpcs = local.resources.vpcs
    subnets = local.resources.subnets
    users = local.resources.users
    security_groups = local.resources.security_groups
    security_group_rules = local.resources.security_group_rules
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

resource "aws_iam_user" "user" {
  for_each = local.users
  name = each.key
}

resource "aws_vpc" "vpc" {
  for_each = local.vpcs
  cidr_block = each.value.cidr_block
  tags = {
    Name = each.key
  }
}

resource "aws_subnet" "subnet" {
  for_each   = local.subnets
  vpc_id     = each.value.vpc_id
  cidr_block = each.value.cidr_block

  tags = {
    Name = each.key
  }
}

resource "aws_security_group" "sg" {
  for_each    = local.security_groups
  name        = each.key
  description = each.value.description
  vpc_id      = each.value.vpc_id
}

resource "aws_instance" "vm" {
  for_each = local.instances
  ami                       = each.value.ami
  instance_type             = each.value.instance_type
  vpc_security_group_ids    = each.value.vpc_security_group_ids
  subnet_id                 = each.value.subnet_id
  tags = {
    Name = each.key
  }
}
