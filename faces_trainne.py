import face_recognition
import cv2
import os
import pickle
import glob
import xlsxwriter
print("trainning...")

cho3ba=[i for i in os.listdir("data")]
for i in cho3ba:
	niveaus=[m for m in os.listdir("data"+"/"+i)]
	#print(niveaus)
	for j in niveaus:
		classe=[h for h in os.listdir("data"+"/"+i+"/"+j)]
		#print(classe)
		for f in classe:
			pathxl="list d appel"+"/"+f+".xlsx"
			workbook = xlsxwriter.Workbook(pathxl)
			worksheet = workbook.add_worksheet()
			database={}
			print("trainning for "+f)
			shema="data"+"/"+i+"/"+j+"/"+f
			print(shema)
			group=[g for g in os.listdir(shema)]
			#print(group)
			print("f",f)
			list_of_names=[]
			row = 0
			col = 0
			if group!=[]:
				for s in group:
					l=s.split(".")
					list_of_names.append(l[0])
					path=shema+"/"+s
					image=face_recognition.load_image_file(path)
					image_encoding = face_recognition.face_encodings(image)[0]
					database[l[0]]=image_encoding
					print("finshed trainning for "+f)

				path2="pickles/"+"/"+i+"/"+f+"_"+"data.pickle"
				with open(path2, 'ab') as f:
					pickle.dump(database, f)
				for kh in list_of_names:
					worksheet.write(row, col, kh)
					row += 1
				workbook.close()
			else:
				print("thers no data for "+f)


print("finished trainning")
