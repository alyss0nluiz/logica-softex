int main(void)
{
  float *ponteiro; 
  int i, tamanho, incerementar, opcao, novo_num;
  tamanho = 22;
  ponteiro = (float *) malloc(tamanho * sizeof(float));
  
  for (i = 0; i < tamanho; i++)
  {
    printf("\nInsira um valor para a posição do vetor: ", i+1);
    scanf("%f",&ponteiro[i]);
  }
  
  printf("\nDeseja incrementar algum número?: ");
  printf("\n1 - Sim");
  printf("\n2 - Não\n");
  scanf("%d", &opcao);

  if (opcao == 1)
  {
    printf("Quantos números você deseja incrementar?: ");
    scanf("%d", &novo_num);
    
    incerementar = novo_num + tamanho;

    ponteiro = (float *) realloc(ponteiro, incerementar * sizeof (float));
    for (i = i; i < incerementar; i++)
  {
    printf("\nInsira um valor para a posição do vetor: ", i+1);
    scanf("%f",&ponteiro[i]);
  }

  }
  else
  {
    incerementar = tamanho;
  }

  for (i = 0;i < incerementar; i++)
  {
    printf("%.2f\n",ponteiro[i]);
  }
  
  free(ponteiro);
  getch();
  return 0;
}