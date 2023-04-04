xlapp=win32com.client.DispatchEx('Excel.Application')
xlapp.DisplayAlerts = False
xlapp.Visible =True
xlbook=xlapp.Workbooks.Open(file)
xlbook.RefreshAll() # make sure you turn off background refresh of connection
xlbook.Save()
xlbook.Close(True)
