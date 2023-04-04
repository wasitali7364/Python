outlook=win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox=outlook.Folders("wasit@gmail.com").Folders("Inbox")

messages=inbox.Items
filtered_email=messages.Restrict("@SQL=urn:schemas:httpmail:subject like '%Error_file%'")
filtered_email.Sort("[ReceivedTime]",True)
latest_email=filtered_email[0]
if subject_line in latest_email.Subject:
  sent_date=latest_email.ReceivedTime.date()
         
  if sent_date==Date.today() and subject_line in latest_email.Subject:
       print(latest_email.subject)
           
       for attachment in latest_email.attachments :
        attachment_name = str(attachment)
        if att in attachment_name:
            print(attachment_name)
            save_file_path = os.path.join (save_location,attachment_name)
            attachment.SaveAsFile(save_file_path)
            break
        else:
            os.system('taskkill /im outlook.exe /f')
            os.system('start outlook')
            msg="Attachment not found in email"
            print(msg)
            send_slack_notification(msg)
            exit()
