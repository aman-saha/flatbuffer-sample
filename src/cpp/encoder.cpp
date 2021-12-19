#include "client_schema_generated.h"
#include <iostream>
#include <fstream>

using namespace SampleClient;

int main(int argc, const char *argv[]){
	std::cout<<"Hello the data is encoded at ../bin/data.bin \n";
	
	flatbuffers::FlatBufferBuilder builder;

	// Client Data

	// 1/ {Ram, 21, 76.5, Male}
	// 2/ {FightClub, 24.5, 66, {Ram, Shayam, Raghuveer} }

	auto person_1_name 	= builder.CreateString("Ram");
	auto person_2_name 	= builder.CreateString("Shyam");
	auto person_3_name 	= builder.CreateString("Raghuveer");

	auto gender_male 	= builder.CreateString("Male");
	auto gender_female 	= builder.CreateString("Female");

	auto group1_name 	= builder.CreateString("FightClub");

	auto Person_1 = CreatePerson(	builder, 
									person_1_name, 
									21.0, 
									76.5, 
									gender_male);

	std::vector <flatbuffers::Offset<flatbuffers::String>> list_of_person_names;
	list_of_person_names.emplace_back(person_1_name);
	list_of_person_names.emplace_back(person_2_name);
	list_of_person_names.emplace_back(person_3_name);

	auto group_list_of_names = builder.CreateVector(list_of_person_names);

	auto Group_1 = CreateGroup(builder, 
								group1_name,
								24.5,
								66.0,
								group_list_of_names);

	auto P_Client_1 = CreateClient(	builder,
									Any_Person, 
									Person_1.Union());

	auto G_Client_1 = CreateClient(	builder,
									Any_Group,
									Group_1.Union());

	std::vector <flatbuffers::Offset<Client>> list_of_clients;
	list_of_clients.emplace_back(P_Client_1);
	list_of_clients.emplace_back(G_Client_1);

	auto all_clients = builder.CreateVector(list_of_clients);

	auto clients = CreateList_of_Clients(builder, all_clients);

	builder.Finish(clients);

	auto *buf = builder.GetBufferPointer();
	int buf_size = builder.GetSize();

	std::ofstream fout;
	fout.open(argv[1]);

	if(fout.is_open())
	{
		fout.write((char*)buf, buf_size);
		fout.close();
	}
	else
	{
		std::cout<<"Unable to open bin file\n";
	}

	return 0;
}
