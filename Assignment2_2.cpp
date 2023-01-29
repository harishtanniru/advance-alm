#include<iostream>
using namespace std;

class Node{
	public:
    int row;
    int col;
    int data;
    Node *nxt;
};

void create_new_node(Node **p, int row_index,int col_index, int x){
    Node *temp = *p;
    Node *r;
    if (temp == NULL)
    {
        temp = new Node();
        temp->row = row_index;
        temp->col = col_index;
        temp->data = x;
        temp->nxt = NULL;
        *p = temp;
    }
    else
    {
        while (temp->nxt != NULL)  
            temp = temp->nxt;
             
        r = new Node();
        r->row = row_index;
        r->col = col_index;
        r->data = x;
        r->nxt = NULL;
        temp->nxt = r;
    }
}

void printList(Node *start)
{
    Node *ptr = start;
    while (ptr != NULL)
    {
        cout << ptr->row << " ";
        ptr = ptr->nxt;
    }
    cout << endl;
 
    ptr = start;
    while (ptr != NULL)
    {
        cout << ptr->col << " ";
        ptr = ptr->nxt;
    }
    cout << endl;
    ptr = start;
     
    while (ptr != NULL)
    {
        cout << ptr->data << " ";
        ptr = ptr->nxt;
    }
}


int main()
{
	int i=0;
	int sparse_matrix [4][5]= 
	{
		{0,0,3,0,4},
		{0,0,5,7,0},
		{0,0,0,0,0},
		{0,2,6,0,0}
	};
	
	Node *first = NULL;
	while(i<4){
		int j=0;
		while(j<5){
			if (sparse_matrix[i][j] != 0)
                create_new_node(&first, i, j,
                                sparse_matrix[i][j]);
		j++;
		}
		i++;
	}
    printList(first);
}