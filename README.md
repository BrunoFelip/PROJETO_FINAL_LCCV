# PROJETO_FINAL_LCCV
AVALIAÇÃO FINAL DO PROCESSO SELETIVO

Nesse README será descrito os procedimentos necessários para a execução do algoritmo elaborado.
As bibliotecas importadas para as funções que determinam os três módulos são:
1. biblioteca math:
    * É um módulo interno já pertencente a própria linguagem.
2. biblioteca numpy:
    * Caso se use os programas conda (ANACONDA), é recomendado a instalação do pacote de versão puramente 32 bits, já que a versão 32/64 bits, no meu caso, quando instalado, houve problemas no reconhecimento dessa e outras bibliotecas. É necessário executar o próprio Anaconda prompt e digitar a seguinte instrução: 'conda install numpy'.
    * Caso se use a instalação normal do python (sem o ANACONDA). É necessário executar o próprio prompt de comando do windows a seguinte instrução: pip install numpy.
Do mesmo modo se segue as outras bibliotecas utilizadas:
3. biblioteca matplotlib:
    cmd anaconda:conda install matplotlib
    cmd windows: pip install matplotlib
É verificado no ao longo do algoritmo que foram importados das bibliotecas acima:
    i. import math
    ii. import numpy as np
    iii. import matplotlib.pyplot as plt
    iv. from mpl_toolkits import mplot3d
    
   O algoritmo foi elaborado utilizando os materiais téoricos disponíveis na internet e também o que foi fornecido pelo LCCV. Foi utilizado o IDE SPYDER do conda, em que foi necessário configurá-lo para que as plotagens não fossem diretamente no console, mas sim por meio de uma janela do matplotlib, para isso basta ir em ferramentas, em seguida, preferências, selecionar a opção console IPython, em seguida ir em gráficos, localizar a informação saída gráfica, por fim, em saída, selecionar a opção automático. Basta fechar a janela, após isso, reinicie o Spyder ou vá no console do Ipython, apertar no ícone engrenagem ou no menu, e selecionar "reiniciar kernel". Caso o programa seja executado no próprio cmd do windows, por padrão, a plotagem é em uma janela e não no console de saída.
   É importante também que, ao baixar o algoritmo do projeto final, que você o coloque em uma pasta inicialmente vazia antes de executá-lo, já que as informações geradas pelo código serão salvos no diretório em que o arquivo estará sendo executado. A extensão adotada para a geração da leitura e o salvamento dos dados é .txt. O padrão de entrada será da seguinte forma:
    
Exemplo (só lembrando que todas as palavras tags devem apresentar o símbolo cerquilha no início):

>>>>>>>> Ver o arquivo texto entrada.txt nos arquivos

No início temos a tag #PLANETAS, onde a posição dessa linha será localizada e tomada como referência, portanto é importante que entre as tags definidas e os dados a serem colodados não haja uma quebra de linha, após a colocação dos dados (em seu final) até a próxima tag não há problema existir várias quebras de linha. É importante também que a referência do número de entrada de cada tag sejam de fato correspondentes aos dados digitados e que o espaçamento entre cada dado na mesma linha seja de um espaço. Nota-se ainda que a dimensão da matriz de contato da tag #CONTATO_INTERACAO deve ser quadrada e sua ordem do mesmo valor do número de planetas presentes. O arquivo de entrada deve está no mesmo diretório onde se encontra o arquivo do algoritmo do projeto final, para que possa ser identificado e lido, e o nome do arquivo a ser lido deve ser: 'entrada'. E sua extensão: '.txt'.

Com os dados carregados na memória pela função ler(), o modulo de análise (mod_analise()) se utilizará dessas informações para o cálculo das prováveis trajetórias dos planetas de acordo com método de integração de EULER ou VERLET, a saída fornece o número de arquivos equivalentes ao número de planetas, para facilitar a análise, observar que a nomeação dos arquivos de saída correspondem a ordem em que os planetas foram digitados no arquivo de entrada, portando planeta N° 1,2,3,... corresponde apenas a uma ordem de contagem de plotagem e reconhecimento, exemplo, (planeta da linha do id inicial - Nº1, planeta digitado depois desse primeiro - Nº2, assim sucessivamente...), portanto o número da nomeação do arquivo não está associado ao id especificamente do planeta. Esses arquivos gerados são salvos no mesmo diretório onde se encontra o arquivo do algoritmo do projeto final. Se o programa for executado novamente, se faz necessário que o usuário exclua os arquivo gerados pelo mod_analise(), já que foi adotado a opção de gravação append, que, sempre quando executado, ele continua escrevendo os novos dados após a última linha desses arquivos (planetas Nº 1,2,3,...).

Por fim, a função visualizacao() reconhecerá todos os arquivos textos de nomes (planetas Nº 1,2,3,...) e o usuário deverá entrar com a opção '2d' para visualizar os resultados no plano e '3d' para visualizar os resultados no espaço. Por fim, ao acabar todo o processo de leitura, o algoritmo avisa com a mensagem ''PROCESSO FINALIZADO'', no console.

