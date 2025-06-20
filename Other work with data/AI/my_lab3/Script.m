function [P, T] = p_Read_Vector_1()
[class, filename] = textread('Neuto_Train/File_Name_tx1.txt','%d %s');
T=[]
P=[]
[P, T] = textread('Neuto_Train/File_Name_tx1.txt','%d %s');
%while ~feof('Neuro_Train/File_Name_tx1.txt')
%    p_Read_Vector_1 = class ;
%    t_Read_Vector_1 = filename;
%    ...
%end
net = newff(p_Read_Vector_1,t_Read_Vector_1,[16,12],{'logsin','tansig'}); 
gensim(net); 