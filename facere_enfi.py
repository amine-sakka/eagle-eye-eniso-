import face_recognition
import cv2
import os
import pickle
import MySQLdb
import datetime
import xlsxwriter
workbook = xlsxwriter.Workbook('liste_presence.xlsx')
worksheet = workbook.add_worksheet()



def absance(database):
    names=[]
    row = 1
    col = 0
    known_face_names=[]
    known_face_encodings=[]
    #print("names of peapol in the data base")
    #print(known_face_names)
    
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        qframe=cv2.flip(frame,1,0)
        rgb_frame = frame[:, :, ::-1] #gray scale

        face_locations = face_recognition.face_locations(rgb_frame) #ylawej 3al faces fil videos
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations) #decodeing the faces
        #print(face_encodings)
        for i in database:

            known_face_names+=database[i][0]
            known_face_encodings+=database[i][1]
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding) #tlwej kan fama chkoun fil database ychabhlou
                #print(matches)
                # If a match was found a5dheur
            if True in matches:
                now = datetime.datetime.now()
                ch=str(now.month)+"/"+str(now.day)
                timi=str(now.hour)+":"+str(now.minute)+":"+str(now.second)
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                if name not in names:
                    worksheet.write(row, col, name.split(" ")[0])
                    worksheet.write(row, col+1, name.split(" ")[1])
                    worksheet.write(row, col+2, "present")
                    worksheet.write(row, col+3, timi)
                    row += 1
                
                color = (0,255,0)
                stroke = 2
                cv2.rectangle(frame, (left, top), (right, bottom),color, stroke)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left+6 , top-6 ), font, 1.0, (255, 255, 255), 1)
            else:
                name = "Unknown"
                color = (0, 0, 255)
                cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left+6 , top-6 ), font, 1.0,color , 1)

        cv2.imshow('Video', frame)
        
        workbook.close()
        #quit = q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

