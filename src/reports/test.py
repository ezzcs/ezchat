from oosheet import OOSheet as S 
S('a1').string = 'Hello world' 
S('a1').value = 1 
S('a2').formula = '=a1+10' 
S('a2').value 
S('a2').string 
S('a2').formula 
S('a1').set_value(2).drag_to('a3').drag_to('b3') 
S('a1:b3').data_array 
S('g5').string = 'hello world' 
S('a1:10').shift_down_until(column_g_satisfies = lambda s: s.string.endswith('world')) 
S('a8:b8').cut() 
S('a1:4').copy() 
S('j5').paste() 
S().undo() 
S().redo() 
S().save_as('./oosheet_sandbox.ods') 
S().quit() # this will close LibreOffice 
