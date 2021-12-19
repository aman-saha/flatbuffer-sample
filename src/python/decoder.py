import flatbuffers
import os,sys
import json

from SampleClient.Person import Person
from SampleClient.Group import Group
from SampleClient.Client import Client
from SampleClient.Any import Any
from SampleClient.List_of_Clients import List_of_Clients

print('Hello, the decoded data is -')
buf = open(sys.argv[1], 'rb').read()
buf = bytearray(buf)

list_of_clients = List_of_Clients.GetRootAs(buf,0)

count_of_clients = list_of_clients.ClientsLength()

for i in range(count_of_clients):
    client = list_of_clients.Clients(i)
    client_type = client.ClientType()
    # print(client_type)
    if(client_type == Any.Person):
        # print('Person')
        person = Person()
        person.Init(client.Client().Bytes, client.Client().Pos)
        print('{',
            person.Name().decode('utf-8'), ',',
            person.Age(),',',
            person.Weight(),',',
            person.Gender().decode('utf-8'),
        '}')

    elif(client_type == Any.Group):
        # print('Group')
        group = Group()
        group.Init(client.Client().Bytes, client.Client().Pos)
        count_of_names = group.GListOfNamesLength()
        list_of_names = ''
        for j in range(count_of_names - 1):
            list_of_names += group.GListOfNames(j).decode('utf-8') + ' , '
        list_of_names += group.GListOfNames(count_of_names - 1).decode('utf-8')
        print('{',
                group.GName().decode('utf-8'), ',',
                group.GAvgAge(), ',',
                group.GAvgWeight(), ','
                '{', list_of_names, '}',
            '}')



