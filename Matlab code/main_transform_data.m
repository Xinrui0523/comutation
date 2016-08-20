
clear;

 %%  To transform mut_matrix to ARM_input

data = csvread('MutMatrix_to1978_2k.txt');

data_2 = data; % if data is not bool, transform to bool (data_2)
% data_2(data_2<=5)=0;
% data_2(data_2>5)=1;
% csvwrite('clrmarix2002_bool.csv',data_2);

%--- transform to "transaction data" for ARM (association rule mining)
L = size(data_2,1);
Indx = cell(L,1);
for i=1:L
    row = data_2(i,:);
    ind = find(row==1);
    Indx{i} = ind;
end
%--- write to file:
filename = 'forARM_MutMatrix_to1978_2k.csv';
cell2csv(filename,Indx,',')

%% -------------To Cytoscape:
% data = importdata('H3N2_to1978_2k_0-8_all.txt');
% res = [];
% K = size(data,2);
% for i=1:size(data,1)
%     targ = data(i,1); 
%     k=2;
%     in = data(i,k);    
%     while(~isnan(in))        
%         item = [in, targ];
%         res = [res; item];
%         k=k+1;
%         if(k>K)
%             break;
%         else
%             in = data(i,k);
%         end
%     end
% end
% csvwrite('H3N2_to1978_2k_0-8_Cytoscape.csv',res);


 
 
 
 