import os
import sys
import json

n = len(sys.argv)
if n != 2:
    print("wrong number of arguments")
    sys.exit()

command = sys.argv[1]

def apply():
    return os.system("terraform -chdir=$MICKEY_TF_PATH apply")

def list_resources():
    # return os.system("terraform state list -state=$MICKEY_TF_PATH/terraform.tfstate")
    print("all resources operating in region ~ us-east-1 ~")
    os.chdir(os.getenv('MICKEY_TF_PATH'))
    return os.system("terraform refresh")

with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "r") as f:
    config = json.load(f)

if command == "list-resources":
    list_resources()
elif command == "apply":
    apply()
elif command == "create-vpc":
    name = input("VPC NAME: ")
    cidr_block = input("CIDR BLOCK: ")

    config["vpcs"][name] = { "cidr_block" : cidr_block }
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    
    st = apply()
    if st != 0:
        config["vpcs"].pop(name, None)
        with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
            json.dump(config, f, indent=4)

elif command == "create-subnet":
    name = input("SUBNET NAME: ")
    vpc_id = input("VPC ID: ")
    cidr_block = input("CIDR BLOCK: ")

    config["subnets"][name] = { 
        "vpc_id": vpc_id,
        "cidr_block" : cidr_block
    }
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    st = apply()
    if st != 0:
        config["subnets"].pop(name, None)
        with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
            json.dump(config, f, indent=4)

elif command == "create-instance":
    name = input("instance NAME: ")
    instance_type = input("instance TYPE [t2.micro / t2.large]: ")
    ami = "ami-0b0dcb5067f052a63"
    vpc_security_group_ids = [ input("security group id: ") ]
    subnet_id = input("subnet id: ")

    config["instances"][name] = { 
        "instance_type" : instance_type,
        "ami": ami,
        "vpc_security_group_ids": vpc_security_group_ids,
        "subnet_id": subnet_id
    }
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    
    st = apply()
    if st != 0:
        config["instances"].pop(name, None)
        with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
            json.dump(config, f, indent=4)

elif command == "destroy-instance":
    name = input("instance NAME: ")

    config["instances"].pop(name, None)
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    apply()

elif command == "create-security-group":
    name = input("sec group NAME: ")
    description = input("description: ")
    vpc_id = input("vpc id: ")

    config["security_groups"][name] = { 
        "description": description,
        "vpc_id": vpc_id
    }
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    st = apply()
    if st != 0:
        config["security_groups"].pop(name, None)
        with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
            json.dump(config, f, indent=4)

elif command == "destroy-security-group":
    name = input("security group NAME: ")

    config["security_groups"].pop(name, None)
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    apply()

elif command == "create-user":
    name = input("user NAME: ")

    config["users"][name] = {}
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    st = apply()
    if st != 0:
        config["users"].pop(name, None)
        with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
            json.dump(config, f, indent=4)

elif command == "destroy-user":
    name = input("user NAME: ")

    config["users"].pop(name, None)
    with open("{}/mickey.json".format(os.getenv('MICKEY_TF_PATH')), "w") as f:
        json.dump(config, f, indent=4)
    apply()

else: print( "command ~ {} ~ not found".format(command) )