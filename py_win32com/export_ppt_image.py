import win32com.client
import uuid
Application = win32com.client.Dispatch("PowerPoint.Application")
Application.Visible = True
Presentation = Application.Presentations.Open('e:\\temp\\a.pptx')
#Presentation.Slides[1].Export("e:\\temp\\1.jpg", "JPG", 800, 600);
num = Presentation.Slides.count
print(num)
for i in range(num):
	Presentation.Slides[i].Export("e:\\temp\\"+ str(i) +".jpg", "JPG", 800, 600)
