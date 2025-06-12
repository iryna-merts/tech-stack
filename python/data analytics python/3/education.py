import numpy as np
import pandas as pd

final=pd.DataFrame(np.zeros((1,3), dtype=np.int8),
             columns=['progr', 'matan','algebra'],
             index=pd.Index(range(1,2)))
final.index.names = ['id']
final	

	ed = pd.read_csv('education1.csv',  index_col=0)
#add - ������������ ��� ����, ���� ����� ������ ��� �
	final=final.add(ed,  fill_value=0)
#merge - ��� ����� ��������,������ ��������
	fool=pd.merge(st, final, left_index=True, right_index=True)

#��� ���, � ���� ���� ����, ������ ���� ����
	fool.columns
	res=fool.query("progr !=0 & matan !=0 & algebra !=0").set_index('name') 
	(res['progr']+res['matan']+res['algebra']).sort_values(ascending=False)

_______________________________________________________________________

#concut �����

#�������� �����
df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
display('df1', 'df2', 'pd.concat([df1, df2])')

#������ ������ �� ��������� �������
df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
display('df3', 'df4', "pd.concat([df3, df4], axis=1)")

#������ ��������� �������
display('x', 'y', 'pd.concat([x, y], ignore_index=True)')
______________
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
display('df5', 'df6', 'pd.concat([df5, df6])')
display('df5', 'df6',
        "pd.concat([df5, df6], join='inner')")

display('df5', 'df6',
        "pd.concat([df5, df6], join_axes=[df5.columns])")
_____________________