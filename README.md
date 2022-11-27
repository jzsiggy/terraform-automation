instruções de uso:

CONFIGURAR VARIÁVEIS DE AMBIENTE:

export MICKEY_TF_PATH=<<PATH TO TF_CONFIG HERE>>
export AWS_ACCESS_KEY_ID=<<AWS ACCESS KEY ID HERE>>
export AWS_SECRET_ACCESS_KEY=<<AWS SECRET ACCESS KEY HERE>>

COMANDOS
python3 main.py list-resources
retorna uma lista dos recursos alocados e os seus respectivos IDs. 

python3 main.py apply
equivalente ao terraform apply

python3 main.py create-vpc
python3 main.py create-subnet
python3 main.py create-security-group
python3 main.py create-instance
python3 main.py create-user
python3 main.py destroy-instance
python3 main.py destroy-user
python3 main.py destroy-security-group

pode rodar nessa ordem para testar todos os comandos :)

DICA -> rode o comando `python3 main.py list-resources` antes de criar um recurso que necessita do ID de outro recurso. Dessa forma você poderá consultar o ID de todos os recursos já alocados.