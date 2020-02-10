#include <sodium.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define SECRETKEYNUM 10
int main(void)
{
	if (sodium_init() < 0){
	perror("ERROR LOADING SODIUM");
	return 1;
	}

char nonce[100];
randombytes_buf(nonce,90);
char secret[SECRETKEYNUM];
crypto_secretbox_keygen(secret);
//printf("%s",secret);
char message[4] = "test";
char cipher[1000];
crypto_secretbox_easy(cipher,message,4,nonce,secret);
printf("%s\n\n\n\n\n\n",cipher);



printf("%s\n",message);
}
