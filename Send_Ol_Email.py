New_Message=r"Dear Team,<br><br>Please find attached file.<br><br>Regards,<br>wasit"

ol=win32com.client.Dispatch("outlook.application")
olmailitem=0x0 

newmail=ol.CreateItem(olmailitem)
newmail.Subject= 'some subject line'
newmail.To='abc@gmail.com'
# newmail.CC='xyz@gmail.com'
newmail.HTMLBody=New_Message
newmail.Attachments.Add(str(new_path1))
newmail.Attachments.Add(str(new_path0))
newmail.Send()
