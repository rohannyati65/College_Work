#include<stdio.h>
#include<malloc.h>

struct node{
	int data;
	struct node *next;
	struct node *prev;
};

struct node *head = NULL;
struct node *temp;

void ins_beg(struct node*);
void ins_end(struct node*);
void del_beg();
void traverse1();
void traverse2();

main(){
	int choice, n;
	struct node *new1;
	
	while(1){
		printf("\nenter the choice\n");
		printf("1. ins_beg\n2. ins_end\n3. del_beg\n4. traverse1\n5. traverse2\n6. exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1:
					new1 = (struct node*)malloc(sizeof(struct node*));
					printf("enter the data\n");
					scanf("%d",&new1->data);
					new1->next = NULL;
					new1->prev = NULL;
					ins_beg(new1);
					break;
			case 2:
					new1 = (struct node*)malloc(sizeof(struct node*));
					printf("enter the data\n");
					scanf("%d",&new1->data);
					new1->next = NULL;
					new1->prev = NULL;
					ins_end(new1);
					break;
			case 3:
					del_beg();
					break;
			case 4:
					traverse1();
					break;
			case 5:
					traverse2();
					break;
			default:
					exit(1);
		}
	}
}
	void ins_beg(struct node *new1){
		if(head == NULL)
			head = new1;
		else{
			head->prev = new1;
			new1->next = head;
			head = new1;
		}
	}
	
	void ins_end(struct node *new1){
		temp = head;
		if(head == NULL)
			head = new1;
		else{
			while(temp->next!= NULL)
				temp = temp->next;
			new1->prev = temp;
			temp->next = new1;
			}
		}
		
	void del_beg(){
		if(head == NULL)
			printf("no item to delete\n");
		else
			head = head->next;
			head->prev = NULL;
	}
	
	void traverse1(){
		struct node *temp = head;
		while(temp != NULL){
			printf("%d ",temp->data);
			temp = temp->next;
		}
	}
	void traverse2(){
	struct node *temp = head;
		while(temp->next != NULL)
			temp = temp->next;
		while(temp!=head){
			printf("%d ",temp->data);
			temp = temp->prev;
			}
			printf("%d", temp->data);
		
	}
