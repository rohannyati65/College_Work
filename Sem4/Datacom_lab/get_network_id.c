
#include<stdio.h>
#include<string.h>

typedef unsigned char byte;
typedef struct {
	byte address[4];
} IP;

byte extract_number(const char* ip_string, const int start, const int end){

	byte result = 0;
	for(int i=start; i<end; i++){
		result = result * 10 + (ip_string[i] - '0');
	}

	return result;
}

void string2ip(const char* ip_string, IP* ip){

	// Only by one convert numbers in string to ip
	int last_marked_position = -1;
	int i = 0;
	int address_part = 0;
	while(ip_string[i] != '\0'){
		if(ip_string[i] == '.'){
			ip->address[address_part] = extract_number(ip_string, last_marked_position+1, i);
			last_marked_position = i;
			address_part++;
		}
		i++;
	}

	ip->address[address_part] = extract_number(ip_string, last_marked_position+1, i);

}

void get_network_id(IP ip, IP subnet_mask){

	for(int i=0; i<4; i++){
		ip.address[i] = ip.address[i] & subnet_mask.address[i];
	}

	printf("Network ID: %d.%d.%d.%d \n", 
		ip.address[0], ip.address[1], ip.address[2], ip.address[3]);

}

int main(int argc, char* argv[]){

	const char* ip_string = "192.168.10.1";
	const char* subnet_mask_string = "255.255.0.0";

	IP ip;
	IP subnet_mask;

	string2ip(ip_string, &ip);
	string2ip(subnet_mask_string, &subnet_mask);

	// printf("%u.%u.%u.%u\n", 
		// ip.address[0], ip.address[1], ip.address[2], ip.address[3]);
	get_network_id(ip, subnet_mask);

	return 0;
}
