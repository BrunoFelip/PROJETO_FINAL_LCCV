# -*- coding: utf-8 -*-
"""
Created on Wed May  8 00:35:22 2019

@author: Bruno Felipe
IDE SPYDER (Atenção. Gráficos do console IPYTHON configurado para automático! Reinicie o console.)

"""

#Módulo de Leitura
#-------------------------------------------------------------------------------------
def ler():
    dados=open('entrada.txt','r')
    point_plan=[]
    aux=dados.readlines()
    #Eliminando o espaçamento '\n':
    pos=0
    for l in range(len(aux)):
        aux[l]=aux[l].rstrip('\n')
        aux[l]=aux[l].split()
    cont=l+1
    for i in range(cont):
    #PLANETAS
         if aux[i]==['#PLANETAS']:
               aux[i+1][0]=int(aux[i+1][0])
               #Definindo o número de planetas:
               n_planetas=aux[i+1][0]
               #Defininado os vetores de dados do planeta:
               for j in range(i+2,i+2+n_planetas,1):
                    for k in range(9):
                         aux[j][k]=float(aux[j][k])
                    point_plan.append(aux[j])
    #Definindo o número de contatos:
         elif aux[i]==['#CONTATO_DEM']:
               n_contatos=int(aux[i+1][0])
               contatos=[]
               #Definindo vetor e matriz de contatos:
               for k in range(i+2,i+2+n_contatos,1):
                   for j in range(2):
                         aux[k][j]=float(aux[k][j])
                   contatos.append(aux[k])
    #Definindo a matriz de contatos
         elif aux[i]==['#CONTATO_INTERACAO']:
               mat_contato=[]
               for k in range(i+1,i+1+n_planetas):
                  for j in range(n_planetas):
                      aux[k][j]=float(aux[k][j])
                  mat_contato.append(aux[k])
    #Definindo o integrador
         elif aux[i]==['#INTEGRADOR']:
                 integrador=aux[i+1][0]
    #Definindo os parâmetros de tempo
         elif aux[i]==['#PARAMETROS_TEMPO']:
                 for k in range(3):
                      aux[i+1][k]=float(aux[i+1][k])
                 temp=aux[i+1]
         elif aux[i]==['#FIM']:
                     dados.seek(0)
                     print('Estruturas de Dados Carregado na Memória: ')
                     print(dados.read())
                     dados.close()
                     return(n_planetas,point_plan,n_contatos,contatos,mat_contato,integrador,temp)

def mod_analise(a):
    #--------------------------------------------------------------------------
    import numpy as np
    import math
    a=dados
    cont=0
    contP=0
    #Constante Gravitacional Universal (SI)
    G=6.67384*10**(-11) #m³.Kg³.s^(-2) ou N.m².Kg²
    #Tempo de iteração
    t=0
    #Tempo Final
    tf=a[6][1]
    #Incremento de Tempo
    dt=a[6][0]
    #Número de Planetas
    numplan=a[0]
    #Passo
    Passo=a[6][2]
    #Matriz de Vetores de posição, velocidade e aceleração Iniciais
    r0=np.zeros((numplan,3),dtype=float)
    v0=np.zeros((numplan,3),dtype=float)
    v1=np.zeros((numplan,3),dtype=float)
    r1=np.zeros((numplan,3),dtype=float)
    raioP=np.zeros((numplan,1),dtype=float)
    massa=np.zeros((numplan,1),dtype=float)
    for i in range(numplan):
            for j in range(3):
                r0[i][j]=a[1][i][j+1]
                v0[i][j]=a[1][i][j+4]
            raioP[i]=a[1][i][7]
            massa[i]=a[1][i][8]
    #-----------------------------------------------------------------
    for i in range(numplan):
        for j in range(numplan):
            for k in range(a[2]):
                    if a[3][k][0]==a[4][i][j] and i!=j:
                        a[4][i][j]=a[3][k][1]
    if a[5]=='VERLET':
            forca=[]
            ac=[]
            for i in range(numplan):
                forca.append([''])
                ac.append([''])
            r=np.copy(r0)
    #--------------------------------------------------------------------
            while t<=tf:
                if contP==cont:
                     for i in range(numplan):
                          f=open('planeta Nº {}.txt'.format(i+1),'a')
                          f.write('{} {} {} {}\n'.format(t,r[i][0],r[i][1],r[i][2]))
                     f.close()
                     cont=cont+Passo
                dX=0
                for i in range(numplan):
                    for j in range(numplan):
                        if i!=j:
                            distplan=np.linalg.norm(r[j]-r[i])
                            somRaios=raioP[i]+raioP[j]
                            vetdir=(r[j]-r[i])/np.linalg.norm(r[j]-r[i])
                            normdX=abs(distplan-somRaios)
                            if distplan<somRaios:
                                dX=normdX*vetdir
                            else:
                                dX=0
                            forca[i]=G*massa[i]*massa[j]*(r[j]-r[i])/((np.linalg.norm(r[j]-r[i]))**3)+a[4][i][j]*dX
                    ac[i]=forca[i]/massa[i]
                    v1[i]=v0[i]+dt*ac[i]
                    r1[i]=r[i]+dt*v1[i]
                    v0[i]=np.copy(v1[i])
                    r[i]=np.copy(r1[i])
                t=round(t+dt,10)
                contP=contP+1
    #--------------------------------------------------------------------
    elif a[5]=='EULER':
            forca=[]
            ac=[]
            for i in range(numplan):
                forca.append([''])
                ac.append([''])
            r=np.copy(r0)
    #--------------------------------------------------------------------
            while t<=tf:
                if contP==cont:
                     for i in range(numplan):
                          f=open('planeta Nº {}.txt'.format(i+1),'a')
                          f.write('{} {} {} {}\n'.format(t,r[i][0],r[i][1],r[i][2]))
                     f.close()
                     cont=cont+Passo
                dX=0
                for i in range(numplan):
                    for j in range(numplan):
                        if i!=j:
                            distplan=np.linalg.norm(r[j]-r[i])
                            somRaios=raioP[i]+raioP[j]
                            vetdir=(r[j]-r[i])/np.linalg.norm(r[j]-r[i])
                            normdX=abs(distplan-somRaios)
                            if distplan<somRaios:
                                dX=normdX*vetdir
                                print(dX)
                            else:
                                dX=0
                            forca[i]=G*massa[i]*massa[j]*(r[j]-r[i])/((np.linalg.norm(r[j]-r[i]))**3)+a[4][i][j]*dX
                    ac[i]=forca[i]/massa[i]
                    v1[i]=v0[i]+dt*ac[i]
                    r1[i]=r[i]+dt*v1[i]
                    v0[i]=np.copy(v1[i])
                    r[i]=np.copy(r1[i])
                t=round(t+dt,10)
                contP=contP+1
    else:
            print('Operador Inválido!')
#-------------------------------------------------------------------------
#Visualização Generalização
def visualizacao(dados):
    numplan=dados[0]
    modelo=input('Entre com o tipo de plot (2d) ou (3d): ')
    import matplotlib.pyplot as plt
    from mpl_toolkits import mplot3d
    import math
    planetas=[]
    numelem=0
    temp=[]
    for i in range(numplan):
         f=open('planeta Nº {}.txt'.format(i+1),'r')
         linha=f.readlines()
         aux=[]
         for j in range(len(linha)):
              if i==0:
                   numelem=numelem+1
              linha[j]=linha[j].rstrip('\n')
              linha[j]=linha[j].split()
              for k in range(4):
                   linha[j][k]=float(linha[j][k])
         planetas.append(linha)
    for i in range(numplan):
         for j in range(len(linha)):
              if i==0:
                   temp.append(planetas[i][j][0])
                   del(planetas[i][j][0])
              else:
                   del(planetas[i][j][0])
    x=[]
    y=[]
    z=[]
    if modelo=='2d':
        for i in range(numplan):
             datax=[]
             datay=[]
             for j in range(len(linha)):
                  datax.append(planetas[i][j][0])
                  datay.append(planetas[i][j][1])
             x.append(datax)
             y.append(datay)
        maximX0=0
        maximY0=0
        for j in range(numplan):
              maximX=math.ceil(max(x[j]))+0.1*math.ceil(max(x[j]))+1
              maximY=math.ceil(max(y[j]))+0.1*math.ceil(max(y[j]))+1
              if maximX0<maximX:
                   maximX0=maximX
              if maximY0<maximY:
                   maximY0=maximY
        for i in range(len(linha)):
             for j in range(numplan):
                  fig=plt.figure('Planetas')
                  ak=plt.subplot()
                  plt.title('Tempo: {} s'.format(temp[i]))
                  ak.plot(x[j][0:i],y[j][0:i],'r--',color='black',mew='2')
                  ak.plot(x[j][i],y[j][i],'ro',mew='0.5')
                  plt.ylim(-maximY0,maximY0)
                  plt.xlim(-maximX0,maximX0)
                  plt.ion()
                  plt.pause(0.015)
             plt.cla()
        plt.close()
    elif modelo=='3d':
        for i in range(numplan):
             datax=[]
             datay=[]
             dataz=[]
             for j in range(len(linha)):
                  datax.append(planetas[i][j][0])
                  datay.append(planetas[i][j][1])
                  dataz.append(planetas[i][j][2])
             x.append(datax)
             y.append(datay)
             z.append(dataz)
        maximX0=0
        maximY0=0
        maximZ0=0
        for j in range(numplan):
              maximX=math.ceil(max(x[j]))+0.1*math.ceil(max(x[j]))+1
              maximY=math.ceil(max(y[j]))+0.1*math.ceil(max(y[j]))+1
              maximZ=math.ceil(max(z[j]))+0.1*math.ceil(max(z[j]))+1
              if maximX0<maximX:
                   maximX0=maximX
              if maximY0<maximY:
                   maximY0=maximY
              if maximZ0<maximZ:
                   maximZ0=maximZ
        for i in range(len(linha)):
             for j in range(numplan):
                  fig=plt.figure('Planetas')
                  al=plt.axes(projection='3d')
                  plt.title('Tempo: {} s'.format(temp[i]))
                  al.plot3D(x[j][0:i],y[j][0:i],z[j]    [0:i],'r--',color='black',mew='2')
                  al.plot3D([x[j][i]],[y[j][i]],[z[j][i]],'ro',mew='0.5')
                  al.set_xlim3d(-maximX0,maximX0)
                  al.set_ylim3d(-maximY0,maximY0)
                  al.set_zlim3d(-maximZ0,maximZ0)
                  plt.ion()
                  plt.pause(0.04)
             plt.cla()
        plt.close()
    else:
         print('A opção digitada é inválida!')
#-------------------------------------------------------------------------------
dados=ler()
mod_analise(dados)
visualizacao(dados)
print('PROCESSAMENTO FINALIZADO. SE FOR EXECUTAR O PROGRAMA COMPLETO NOVAMENTE, POR FAVOR APAGAR OS DADOS DOS PLANETAS GERADOS NO DIRETÓRIO ONDE ESTÁ SALVO ESTE ARQUIVO. JÁ QUE A GRAVAÇÃO ESTÁ NO MODO (a) APPEND.')