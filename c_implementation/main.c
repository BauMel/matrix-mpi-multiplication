#include <stdio.h>
#include <stdlib.h>
#include <time.h>

struct matrix_struct{
    int nbOfColumn;
    int nbOfLine;
    double** matrix;
};

public double** simple_matrice_multiplication(struct matrix_struct m1,struct matrix_struct m2){
    
    double** res_matrix = (double**) malloc(sizeof(double*)*(m1.nbOfLine));
    for (i=0; i<m1.nbOfLine; i++)
		res_matrix[i]=(double*) malloc(m2.nbOfColumn*sizeof(double));

	

    if (m1.nbOfColumn == m2.nbOfLine)
    {
    	for (i = 0; i < m1.nbOfLine; i++)
  	    {
	        for (j = 0; j < m2.nbOfColumn; j++)
	        {
	            *(*(res_matrix + i) + j) = 0;// res_matrix[i][j] = 0;
	        }
    	}
    	// iterate through rows of m1
        for(i = 0; i < m1.nbOfLine; i++){
            //iterate through columns of m2
            for (j = 0; j < m2.nbOfColumn; j++){
                // iterate through rows of m2
                for(k = 0; k < m2.nbOfLine; k++)
                    *(*(res_matrix + i) + j) += (*(*(m1.matrix + i) + k)) * (*(*(m2.matrix + k) + j))//res_matrix[i][j] += m1[i][k] * m2[k][j]
            }
        }
    }
    else
      printf("Les matrices ne sont pas de tailles compatibles Aucun Résultat");
}

int main() {
	struct matrix_struct m1,m2;

	m1 = {2,2,(double**) malloc(sizeof(double*)*2)}
    for (i=0; i<m1.nbOfLine; i++)
		m1.matrix[i]=(double*) malloc(m1.nbOfColumn*sizeof(double));

	//Initialisation de m1

	srand(time(NULL));

	for(i=0;i<m1.nbOfLine;i++)
	{
		for(j=0;j<m1.nbOfColumn;j++)
		   m1.matrix[i][j] = rand() % 4;
	}

    printf("\n===> Matrice m1 <===\n");

	for(i=0;i<m1.nbOfLine;i++)
	{
		for(j=0;j<m1.nbOfColumn;j++)
		printf("%lf ", m1[i][j]);
		printf("\n");
	}

	//Initialisation de m2

	m2 = {2,2,(double**) malloc(sizeof(double*)*2)}
    for (i=0; i<m2.nbOfLine; i++)
		m2.matrix[i]=(double*) malloc(m2.nbOfColumn*sizeof(double));


	for(i=0;i<m2.nbOfLine;i++)
	{
		for(j=0;j<m2.nbOfColumn;j++)
		   m2.matrix[i][j] = rand() % 4;
	}

	printf("\n===> Matrice m2 <===\n");

	for(i=0;i<m2.nbOfLine;i++)
	{
		for(j=0;j<m2.nbOfColumn;j++)
		printf("%lf ", m2[i][j]);
		printf("\n");
	}

    double** res_matrix = simple_matrice_multiplication();
    printf("\n===> Matrice res_matrix <===\n");

	for(i=0;i<m1.nbOfLine;i++)
	{
		for(j=0;j<m2.nbOfColumn;j++)
		printf("%lf ", res_matrix[i][j]);
		printf("\n");
	}

   return 0;
}