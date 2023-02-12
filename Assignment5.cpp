#include <iostream>
#include <vector>
#include <algorithm>
#include <time.h>
#include <iomanip>
#include <math.h> 
#include <string>
using namespace std;

string DNA1;
string DNA2;
int n;

void longest_common_substring(vector<vector<char>> b, string X, int i, int j)
{

	if(i == 0 || j == 0)
	{
		return;
	}
	
	if(b[i][j] == '@')
	{	
		longest_common_substring(b, X, i - 1, j - 1);
		cout << X[i];
	}
	else if(b[i][j] == '#')
	{	
		longest_common_substring(b, X, i - 1, j);
	}
	else
	{
		longest_common_substring(b, X, i, j - 1);
	}
}

int longestCommonSubsequence(string X, string Y)
{
	int m = X.length();
	n = Y.length();
	
	
	
	vector<vector<char>> b(m+1, vector<char>(n+1, 0));
	
	vector<vector<char>> c(m+1, vector<char>(n+1, 0));
	
	for(int i = 0; i <= m; i++)
	{
		for(int j = 0; j <= n; j++)
		{
			if(i == 0 || j == 0)
			{	
				c[i][j] = 0;
				b[i][j] = '/';
			}
			else if(X[i] == Y[j])
			{
				c[i][j] = c[i-1][j-1] + 1;
				b[i][j] = '@'; 
			}
			else if(c[i-1][j] >= c[i][j-1])
			{
				c[i][j] = c[i-1][j];
				b[i][j] = '#'; 
			}
			else
			{
				c[i][j] = c[i][j-1];
				b[i][j] = '!'; 
			}
		}
	}
	
	
	longest_common_substring(b, X, X.length(), Y.length());
	
	return c[m][n];
}	

int main()
{	
cin >> DNA1 >> DNA2;
	
		string space = " ";
		DNA1.insert(0, space);
		DNA2.insert(0, space);
		int seqLen = longestCommonSubsequence(DNA1, DNA2);
		cout << endl << seqLen - 1 << endl;
	
}