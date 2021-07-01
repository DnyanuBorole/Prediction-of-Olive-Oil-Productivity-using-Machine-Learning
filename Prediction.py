from PyQt5 import QtCore, QtGui, QtWidgets


from SelectDistrict import *
import numpy as np
import pandas as pd
import sys
import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from DBconn import DBConnection
dict = {}
states = {"Odisha":1,"Sikkim":2,"Maharashtra":3,"Andhra Pradesh":4,"West Bengal":5,"Uttar Pradesh":6,"Karnataka":7,"Telangana":7,
    "Chhattisgarh":8,"Punjab":9,"Uttarakhand":10,"Bihar":11,"Assam":12,"Kerala":13,"Jammu and Kashmir":14,"Tripura":15,
     "Nagaland":16,"Goa":17,"Arunachal Pradesh":18,"Dadra and Nagar Haveli":19,"Meghalaya":20,"Puducherry":21,"Madhya Pradesh":22,
    "Tamil Nadu":23,"Gujarat":24,"Haryana":25,"Rajasthan":26,"Himachal Pradesh":27,"Andaman and Nicobar Islands":28,"Jharkhand":29,
     "Chandigarh":30,"Mizoram":31,"Manipur":32}
districts={'MAYURBHANJ':1,'GANJAM': 2, 'BALESHWAR': 3, 'BARGARH': 4, 'BHADRAK': 5, 'KENDUJHAR': 6, 'KALAHANDI': 7, 'CUTTACK': 8, 'BALANGIR': 9, 'NABARANGPUR': 10, 'KENDRAPARA': 11, 'SUNDARGARH': 12, 'PURI': 13, 'KHORDHA': 14, 'JAJAPUR': 15, 'SAMBALPUR': 16, 'NAYAGARH': 17, 'SONEPUR': 18, 'MALKANGIRI': 19, 'KORAPUT': 20, 'DHENKANAL': 21, 'JAGATSINGHAPUR': 22, 'ANUGUL': 23, 'NUAPADA': 24, 'BOUDH': 25, 'RAYAGADA': 26, 'GAJAPATI': 27, 'DEOGARH': 28, 'JHARSUGUDA': 29, 'KANDHAMAL': 30, 'SOUTH DISTRICT': 31, 'WEST DISTRICT': 32, 'EAST DISTRICT': 33, 'NORTH DISTRICT': 34, 'SOLAPUR': 35, 'ANANTAPUR': 36, 'MEDINIPUR WEST': 37, 'JALGAON': 38, 'AHMEDNAGAR': 39, 'AURANGABAD': 40, 'YAVATMAL': 41, 'BARDHAMAN': 42, 'WEST GODAVARI': 43, 'EAST GODAVARI': 44, 'BEED': 45, 'AMRAVATI': 46, 'BULDHANA': 47, 'NANDED': 48, 'LATUR': 49, 'HARDOI': 50, '24 PARAGANAS SOUTH': 51, 'BIRBHUM': 52, 'GULBARGA': 53, 'NALGONDA': 54, 'KURNOOL': 55, 'ADILABAD': 56, 'WASHIM': 57, 'BANKURA': 58, 'JALNA': 59, 'KRISHNA': 60, 'RAJNANDGAON': 61, 'GUNTUR': 62, 'SANGRUR': 63, 'PURULIA': 64, 'PARBHANI': 65, 'MAHASAMUND': 66, 'KHERI': 67, 'PUNE': 68, 'SHAHJAHANPUR': 69, 'LUDHIANA': 70, 'BUDAUN': 71, 'MEDINIPUR EAST': 72, 'BATHINDA': 73, 'JANJGIR-CHAMPA': 74, 'AZAMGARH': 75, 'UNNAO': 76, 'SPSR NELLORE': 77, 'BALODA BAZAR': 78, 'MAHBUBNAGAR': 79, 'AKOLA': 80, 'PATIALA': 81, 'RAIGARH': 82, 'WARANGAL': 83, 'BILASPUR': 84, 'ALIGARH': 85, 'MURSHIDABAD': 86, 'NAGPUR': 87, 'UDAM SINGH NAGAR': 88, 'COOCHBEHAR': 89, 'OSMANABAD': 90, 'KARIMNAGAR': 91, 'ALLAHABAD': 92, 'BAREILLY': 93, 'BIJNOR': 94, 'SRIKAKULAM': 95, 'DHULE': 96, 'JAUNPUR': 97, 'SITAPUR': 98, 'MUKTSAR': 99, 'WARDHA': 100, 'FAZILKA': 101, 'DHAMTARI': 102, 'ROHTAS': 103, 'BULANDSHAHR': 104, 'MATHURA': 105, 'SANGLI': 106, 'BARABANKI': 107, 'GORAKHPUR': 108, 'HOOGHLY': 109, 'FIROZEPUR': 110, 'BHANDARA': 111, 'AMRITSAR': 112, 'TARN TARAN': 113, 'BIJAPUR': 114, 'GURDASPUR': 115, 'RAIPUR': 116, 'BALOD': 117, 'JASHPUR': 118, 'BELGAUM': 119, 'DINAJPUR UTTAR': 120, 'DAVANGERE': 121, 'KANKER': 122, 'MOGA': 123, 'JALPAIGURI': 124, 'GHAZIPUR': 125, 'GONDIA': 126, 'FATEHPUR': 127, 'LALITPUR': 128, 'TUMKUR': 129, 'SIDDHARTH NAGAR': 130, 'RAE BARELI': 131, 'JALANDHAR': 132, 'MANSA': 133, 'BAHRAICH': 134, 'MAHARAJGANJ': 135, 'MUZAFFARNAGAR': 136, 'DINAJPUR DAKSHIN': 137, 'BEMETARA': 138, 'KHAMMAM': 139, 'JALAUN': 140, 'DEORIA': 141, 'JHANSI': 142, 'GONDA': 143, 'GADCHIROLI': 144, 'NASHIK': 145, 'BANDA': 146, 'HOSHIARPUR': 147, 'MAINPURI': 148, 'PASHCHIM CHAMPARAN': 149, 'RAMPUR': 150,
           'NAGAON': 151, 'KOLHAPUR': 152, 'SATARA': 153, 'PILIBHIT': 154, 'SAMBHAL': 155, 'BALLIA': 156, 'CHANDRAPUR': 157, 'MALDAH': 158, 'GARIYABAND': 159, '24 PARAGANAS NORTH': 160, 'PRATAPGARH': 161, 'HINGOLI': 162, 'HAVERI': 163, 'AGRA': 164, 'MEDAK': 165, 'ETAH': 166, 'BASTAR': 167, 'DURG': 168, 'SONITPUR': 169, 'PURBI CHAMPARAN': 170, 'VIZIANAGARAM': 171, 'SAHARANPUR': 172, 'KOZHIKODE': 173, 'CHITTOOR': 174, 'MORADABAD': 175, 'KANPUR DEHAT': 176, 'MEERUT': 177, 'AMBEDKAR NAGAR': 178, 'BIDAR': 179, 'BASTI': 180, 'KARBI ANGLONG': 181, 'CHITRADURGA': 182, 'NANDURBAR': 183, 'KUSHI NAGAR': 184, 'SURGUJA': 185, 'KAPURTHALA': 186, 'NADIA': 187, 'RAIGAD': 188, 'FARIDKOT': 189, 'MADHUBANI': 190, 'GOLAGHAT': 191, 'BARNALA': 192, 'HAMIRPUR': 193, 'NIZAMABAD': 194, 'FAIZABAD': 195, 'ALMORA': 196, 'KORBA': 197, 'MUZAFFARPUR': 198, 'MUNGELI': 199, 'BALRAMPUR': 200, 'SURAJPUR': 201, 'SHIMOGA': 202, 'VISAKHAPATANAM': 203, 'PRAKASAM': 204, 'RAICHUR': 205, 'BAGALKOT': 206, 'AURAIYA': 207, 'SULTANPUR': 208, 'GAYA': 209, 'YADGIR': 210, 'MALAPPURAM': 211, 'KANPUR NAGAR': 212, 'LAKHIMPUR': 213, 'CHANDAULI': 214, 'KAIMUR (BHABUA)': 215, 'KABIRDHAM': 216, 'KONDAGAON': 217, 'BHOJPUR': 218, 'KASGANJ': 219, 'MIRZAPUR': 220, 'FIROZABAD': 221, 'AMETHI': 222, 'ETAWAH': 223, 'SIVASAGAR': 224, 'BELLARY': 225, 'MAU': 226, 'MYSORE': 227, 'CACHAR': 228, 'BANKA': 229, 'AMROHA': 230, 'SANT KABEER NAGAR': 231, 'SIWAN': 232, 'NALANDA': 233, 'ARARIA': 234, 'SITAMARHI': 235, 'PAURI GARHWAL': 236, 'BAKSA': 237, 'FATEHGARH SAHIB': 238, 'KANNUR': 239, 'GADAG': 240, 'SARAN': 241, 'JORHAT': 242, 'THRISSUR': 243, 'BUXAR': 244, 'HATHRAS': 245, 'DHARWAD': 246, 'SHRAVASTI': 247, 'LUCKNOW': 248, 'HASSAN': 249, 'SUKMA': 250, 'SUPAUL': 251, 'BAGHPAT': 252, 'NAWADA': 253, 'FARRUKHABAD': 254, 'TEHRI GARHWAL': 255, 'KANNAUJ': 256, 'NAWANSHAHR': 257, 'PALGHAR': 258, 'GOPALGANJ': 259, 'DIBRUGARH': 260, 'KOREA': 261, 'THIRUVANANTHAPURAM': 262, 'HARIDWAR': 263, 'RATNAGIRI': 264, 'HOWRAH': 265, 'KAUSHAMBI': 266, 'DANTEWADA': 267, 'MAHOBA': 268, 'KARIMGANJ': 269, 'BARPETA': 270, 'RAMANAGARA': 271, 'VARANASI': 272, 'KADAPA': 273, 'KAMRUP': 274, 'DHEMAJI': 275, 'SINDHUDURG': 276, 'SAHARSA': 277, 'PURNIA': 278, 'RUPNAGAR': 279, 'UTTAR KANNAD': 280, 'PITHORAGARH': 281, 'JAMMU': 282, 'KOKRAJHAR': 283, 'CHIKBALLAPUR': 284, 'KASARAGOD': 285, 'PATNA': 286, 'RANGAREDDI': 287, 'UDALGURI': 288, 'SHAMLI': 289, 'KISHANGANJ': 290, 'NALBARI': 291, 'PALAKKAD': 292, 'DARBHANGA': 293, 'SONBHADRA': 294, 'TINSUKIA': 295, 'KOPPAL': 296, 'KATIHAR': 297, 'SAMASTIPUR': 298, 'THANE': 299, 'CHITRAKOOT': 300,
           'BEGUSARAI': 301, 'MADHEPURA': 302, 'KOLAR': 303, 'KOLLAM': 304, 'MANDYA': 305, 'DHUBRI': 306, 'GOALPARA': 307, 'S.A.S NAGAR': 308, 'DARRANG': 309, 'SANT RAVIDAS NAGAR': 310, 'SEPAHIJALA': 311, 'RAJAURI': 312, 'BHAGALPUR': 313, 'NAINITAL': 314, 'DIMAPUR': 315, 'VAISHALI': 316, 'HAPUR': 317, 'CHIKMAGALUR': 318, 'MARIGAON': 319, 'IDUKKI': 320, 'ERNAKULAM': 321, 'CHAMOLI': 322, 'DEHRADUN': 323, 'UDUPI': 324, 'JAMUI': 325, 'SOUTH TRIPURA': 326, 'PATHANKOT': 327, 'HAILAKANDI': 328, 'NORTH GOA': 329, 'GAUTAM BUDDHA NAGAR': 330, 'BAGESHWAR': 331, 'JEHANABAD': 332, 'CHIRANG': 333, 'BANGALORE RURAL': 334, 'UTTAR KASHI': 335, 'BONGAIGAON': 336, 'DAKSHIN KANNAD': 337, 'ALAPPUZHA': 338, 'GOMATI': 339, 'KHAGARIA': 340, 'UDHAMPUR': 341, 'KATHUA': 342, 'CHAMARAJANAGAR': 343, 'NORTH TRIPURA': 344, 'DHALAI': 345, 'KODAGU': 346, 'RUDRA PRAYAG': 347, 'LAKHISARAI': 348, 'DARJEELING': 349, 'SHEIKHPURA': 350, 'GHAZIABAD': 351, 'KOTTAYAM': 352, 'BADGAM': 353, 'ARWAL': 354, 'DODA': 355, 'WEST TRIPURA': 356, 'NARAYANPUR': 357, 'WEST SIANG': 358, 'ANANTNAG': 359, 'POONCH': 360, 'BENGALURU URBAN': 361, 'KHOWAI': 362, 'CHAMPAWAT': 363, 'BARAMULLA': 364, 'MUNGER': 365, 'REASI': 366, 'KAMRUP METRO': 367, 'MON': 368, 'KULGAM': 369, 'WOKHA': 370, 'KUPWARA': 371, 'SHEOHAR': 372, 'RAMBAN': 373, 'UNAKOTI': 374, 'EAST SIANG': 375, 'PULWAMA': 376, 'TUENSANG': 377, 'PATHANAMTHITTA': 378, 'PEREN': 379, 'MOKOKCHUNG': 380, 'SOUTH GOA': 381, 'PHEK': 382, 'KOHIMA': 383, 'LOWER DIBANG VALLEY': 384, 'DADRA AND NAGAR HAVELI': 385, 'ZUNHEBOTO': 386, 'KISHTWAR': 387, 'WAYANAD': 388, 'LOHIT': 389, 'WEST GARO HILLS': 390, 'PAPUM PARE': 391, 'KIPHIRE': 392, 'RI BHOI': 393, 'BANDIPORA': 394, 'SAMBA': 395, 'DIMA HASAO': 396, 'CHANGLANG': 397, 'EAST KAMENG': 398, 'EAST KHASI HILLS': 399, 'WEST JAINTIA HILLS': 400, 'GANDERBAL': 401, 'LOWER SUBANSIRI': 402, 'SOUTH WEST GARO HILLS': 403, 'LONGLENG': 404, 'UPPER SIANG': 405, 'WEST KHASI HILLS': 406, 'EAST GARO HILLS': 407, 'UPPER SUBANSIRI': 408, 'NORTH GARO HILLS': 409, 'SOUTH GARO HILLS': 410, 'PONDICHERRY': 411, 'EAST JAINTIA HILLS': 412, 'KARAIKAL': 413, 'SRINAGAR': 414, 'TIRAP': 415, 'ANJAW': 416, 'WEST KAMENG': 417, 'LONGDING': 418, 'DIBANG VALLEY': 419, 'SOUTH WEST KHASI HILLS': 420, 'TAWANG': 421, 'KURUNG KUMEY': 422, 'YANAM': 423, 'SHOPIAN': 424, 'NAMSAI': 425, 'KARGIL': 426, 'LEH LADAKH': 427, 'UJJAIN': 428, 'SAGAR': 429, 'DEWAS': 430, 'RAJGARH': 431, 'VIDISHA': 432, 'SEHORE': 433, 'DHAR': 434, 'MANDSAUR': 435, 'HOSHANGABAD': 436, 'BALAGHAT': 437, 'GUNA': 438, 'SHAJAPUR': 439, 'RAISEN': 440, 'BETUL': 441, 'RATLAM': 442,
           'INDORE': 443, 'KHARGONE': 444, 'SHIVPURI': 445, 'CHHATARPUR': 446, 'KHANDWA': 447, 'BHIND': 448, 'DAMOH': 449, 'HARDA': 450, 'THIRUVARUR': 451, 'VILLUPURAM': 452, 'THANJAVUR': 453, 'ASHOKNAGAR': 454, 'TIKAMGARH': 455, 'NAGAPATTINAM': 456, 'CHHINDWARA': 457, 'REWA': 458, 'SEONI': 459, 'SATNA': 460, 'MORENA': 461, 'AGAR MALWA': 462, 'DATIA': 463, 'MANDLA': 464, 'NEEMUCH': 465, 'CUDDALORE': 466, 'JABALPUR': 467, 'GWALIOR': 468, 'RAMANATHAPURAM': 469, 'BHOPAL': 470, 'SHAHDOL': 471, 'KATNI': 472, 'ANUPPUR': 473, 'NARSINGHPUR': 474, 'THIRUVALLUR': 475, 'SHEOPUR': 476, 'KANCHIPURAM': 477, 'PANNA': 478, 'COIMBATORE': 479, 'TIRUVANNAMALAI': 480, 'DINDORI': 481, 'PUDUKKOTTAI': 482, 'SIDHI': 483, 'JHABUA': 484, 'BARWANI': 485, 'SIVAGANGA': 486, 'TIRUNELVELI': 487, 'NAMAKKAL': 488, 'TIRUPPUR': 489, 'ALIRAJPUR': 490, 'KRISHNAGIRI': 491, 'TIRUCHIRAPPALLI': 492, 'SINGRAULI': 493, 'PERAMBALUR': 494, 'BURHANPUR': 495, 'UMARIA': 496, 'VELLORE': 497, 'TUTICORIN': 498, 'MADURAI': 499, 'DINDIGUL': 500, 'ERODE': 501, 'ARIYALUR': 502, 'DHARMAPURI': 503, 'SALEM': 504, 'KANNIYAKUMARI': 505, 'VIRUDHUNAGAR': 506, 'KARUR': 507, 'THENI': 508, 'THE NILGIRIS': 509, 'SURENDRANAGAR': 510, 'RAJKOT': 511, 'BHAVNAGAR': 512, 'JUNAGADH': 513, 'SIRSA': 514, 'AMRELI': 515, 'HISAR': 516, 'JIND': 517, 'VADODARA': 518, 'JAMNAGAR': 519, 'FATEHABAD': 520, 'AHMADABAD': 521, 'KARNAL': 522, 'KAITHAL': 523, 'BHIWANI': 524, 'SABAR KANTHA': 525, 'SONIPAT': 526, 'BANAS KANTHA': 527, 'KACHCHH': 528, 'DOHAD': 529, 'BHARUCH': 530, 'PANCH MAHALS': 531, 'KURUKSHETRA': 532, 'ROHTAK': 533, 'MAHENDRAGARH': 534, 'PALWAL': 535, 'JHAJJAR': 536, 'ANAND': 537, 'AMBALA': 538, 'KHEDA': 539, 'PANIPAT': 540, 'YAMUNANAGAR': 541, 'SURAT': 542, 'MAHESANA': 543, 'PATAN': 544, 'MEWAT': 545, 'REWARI': 546, 'VALSAD': 547, 'PORBANDAR': 548, 'NAVSARI': 549, 'TAPI': 550, 'GURGAON': 551, 'NARMADA': 552, 'GANDHINAGAR': 553, 'FARIDABAD': 554, 'PANCHKULA': 555, 'DANG': 556, 'MAHE': 557, 'BARMER': 558, 'BIKANER': 559, 'JODHPUR': 560, 'NAGAUR': 561, 'JAISALMER': 562, 'CHURU': 563, 'JALORE': 564, 'JAIPUR': 565, 'SIKAR': 566, 'HANUMANGARH': 567, 'JHUNJHUNU': 568, 'GANGANAGAR': 569, 'ALWAR': 570, 'JHALAWAR': 571, 'BHARATPUR': 572, 'BHILWARA': 573, 'BARAN': 574, 'TONK': 575, 'CHITTORGARH': 576, 'UDAIPUR': 577, 'AJMER': 578, 'SAWAI MADHOPUR': 579, 'BUNDI': 580, 'BANSWARA': 581, 'DAUSA': 582, 'PALI': 583, 'KARAULI': 584, 'KOTA': 585, 'KANGRA': 586, 'DUNGARPUR': 587, 'DHOLPUR': 588, 'MANDI': 589, 'RAJSAMAND': 590, 'SIROHI': 591, 'UNA': 592, 'CHAMBA': 593, 'SIRMAUR': 594, 'SOLAN': 595, 'KULLU': 596, 'NICOBARS': 597,
           'SHIMLA': 598, 'PALAMU': 599, 'NORTH AND MIDDLE ANDAMAN': 600, 'GARHWA': 601, 'DUMKA': 602, 'CHATRA': 603, 'GODDA': 604, 'SOUTH ANDAMANS': 605, 'GIRIDIH': 606, 'SAHEBGANJ': 607, 'RANCHI': 608, 'DEOGHAR': 609, 'HAZARIBAGH': 610, 'LAHUL AND SPITI': 611, 'LOHARDAGA': 612, 'PAKUR': 613, 'KINNAUR': 614, 'JAMTARA': 615, 'LATEHAR': 616, 'GUMLA': 617, 'RAMGARH': 618, 'BOKARO': 619, 'CHANDIGARH': 620, 'KODERMA': 621, 'SIMDEGA': 622, 'KHUNTI': 623, 'WEST SINGHBHUM': 624, 'EAST SINGHBUM': 625, 'SARAIKELA KHARSAWAN': 626, 'DHANBAD': 627, 'CHAMPHAI': 628, 'LUNGLEI': 629, 'MAMIT': 630, 'SERCHHIP': 631, 'KOLASIB': 632, 'AIZAWL': 633, 'LAWNGTLAI': 634, 'SAIHA': 635, 'THOUBAL': 636, 'IMPHAL EAST': 637, 'SENAPATI': 638, 'IMPHAL WEST': 639, 'CHURACHANDPUR': 640, 'BISHNUPUR': 641, 'UKHRUL': 642,
           'TAMENGLONG': 643, 'CHANDEL': 644, 'HYDERABAD': 645, 'MUMBAI': 646}
season= {"Winter":1 ,"Autumn":2,"Summer":3,"Kharif":4 ,"Rabi":5,"Whole Year":6}
result= {"Yes":1 ,"No":2}


class Ui_Prediction(object):
    def __init__(self,dist,state):
        self.dist=dist
        self.state = state

    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()

    def clear(self):
        self.lineEdit.clear()
        self.statename.clear()
        self.district.clear()
        self.comboBox.setCurrentIndex(0)

    def prediction(self):
        try:
            stat = self.statename.text()
            # print(stat)
            dis = self.district.text()
            # print(dis)
            seas = self.comboBox.currentText()
            # print(seas)
            area = self.lineEdit.text()
            # print(area)

            if area == "" or area == "null" or self.comboBox.currentText() == "-------------Select---------------" or stat== "null" or stat=="" or dis == "null" or dis == "":
                self.alertmsg("Failed", "Enter All the fields")
            else:
                stat = states[stat]
                # print(stat)
                dis = districts[dis]
                # print(dis)
                seas = season[seas]
                # print(seas)
                tset = []
                mydb = DBConnection.getConnection()
                cursor = mydb.cursor()
                cursor.execute("select * from m_dataset")
                row = cursor.fetchall()
                y_train = []
                tset.clear()
                y_train.clear()
                for r in row:
                    x_train = []
                    x_train.clear()
                    x_train.append(int(r[0]))
                    x_train.append(int(r[1]))
                    x_train.append(int(r[3]))
                    x_train.append(int(r[4]))
                    y_train.append(r[6])
                    tset.append(x_train)

                tset = np.array(tset)
                y_train = np.array(y_train)
                fields = ('State_Name', 'District_Name', 'Season', 'Area')
                rows = [[stat, dis, seas,area]]
                with open('../OlivePrediction/dataset/OliveTestingDataset.csv', 'w', newline='') as f:
                    write = csv.writer(f)
                    write.writerow(fields)
                    write.writerows(rows)
                tf = pd.read_csv('../OlivePrediction/dataset/OliveTestingDataset.csv')
                testdata = np.array(tf)
                testdata = testdata.reshape(len(testdata), -1)
                rf = GaussianNB()
                rf.fit(tset, y_train)
                res = rf.predict(testdata)
                # print(res[0])
                if (int(res[0]) == 1):
                    # print(int(res[0]))
                    self.output.setText("Yes")
                else:
                    self.output.setText("No")
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1237, 768)
        Dialog.setStyleSheet(
            "QDialog{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(127, 187, 210, 255));}")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(150, 190, 991, 491))
        self.frame.setStyleSheet(
            "QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(215, 215, 215, 221));}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 30, 161, 41))
        self.label_2.setStyleSheet("font: 75 14pt \"Arial\";\n"
                                   "color: rgb(0, 0, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));")
        self.label_2.setObjectName("label_2")
        self.statename = QtWidgets.QLabel(self.frame)
        self.statename.setGeometry(QtCore.QRect(215, 25, 291, 51))
        self.statename.setStyleSheet("font: 75 19pt \"Arial\";\n"
                                     "color: rgb(255, 0, 0);\n"
                                     "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));")
        self.statename.setFrameShape(QtWidgets.QFrame.Box)
        self.statename.setLineWidth(0)
        self.statename.setText(self.state)
        self.statename.setAlignment(QtCore.Qt.AlignCenter)
        self.statename.setObjectName("statename")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(60, 110, 161, 41))
        self.label_3.setStyleSheet("font: 75 15pt \"Arial\";\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));")
        self.label_3.setObjectName("label_3")
        self.district = QtWidgets.QLabel(self.frame)
        self.district.setGeometry(QtCore.QRect(215, 105, 291, 51))
        self.district.setStyleSheet("font: 75 14pt \"Arial\";\n"
                                    "color: rgb(255, 0, 0);\n"
                                    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));")
        self.district.setFrameShape(QtWidgets.QFrame.Box)
        self.district.setLineWidth(0)
        self.district.setText(self.dist)
        self.district.setAlignment(QtCore.Qt.AlignCenter)
        self.district.setObjectName("district")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(44, 210, 171, 41))
        self.label_4.setStyleSheet("font: 75 14pt \"Arial\";\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));")
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(220, 200, 291, 51))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Arial\";\n"
                                    "color: rgb(255, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(50, 310, 141, 41))
        self.label_5.setStyleSheet("font: 75 14pt \"Arial\";\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));")
        self.label_5.setObjectName("label_5")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit.setGeometry(QtCore.QRect(220, 310, 292, 51))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "font: 75 14pt \"Arial\";\n"
                                    "color: rgb(255, 0, 0);")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(183, 390, 161, 41))
        self.pushButton.setStyleSheet("background-color: rgb(170, 75, 118);\n"
                                      "font: 87 16pt \"Arial Black\";\n"
                                      "color: rgb(255, 255, 255);")
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setGeometry(QtCore.QRect(360, 390, 161, 41))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 75, 118);\n"
                                        "font: 87 13pt \"Arial Black\";\n"
                                        "color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(670, 320, 291, 51))
        self.label_6.setStyleSheet("font: 22pt \"Algerian\";\n"
                                   "color: rgb(0, 138, 0);\n"
                                   "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 0));")
        self.label_6.setObjectName("label_6")
        self.output = QtWidgets.QLabel(self.frame)
        self.output.setGeometry(QtCore.QRect(670, 390, 281, 71))
        self.output.setStyleSheet("font: 26pt \"Algerian\";\n"
                                   "background-color: rgb(255, 253, 197);\n"
                                   "color: rgb(255, 0, 0);\n"
                                   "")
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setLineWidth(2)
        self.output.setText("")
        self.output.setAlignment(QtCore.Qt.AlignCenter)
        self.output.setObjectName("output")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(900, 320, 51, 51))
        self.label_8.setStyleSheet("background-image: url(../OlivePrediction/Images/down.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(540, 40, 201, 71))
        self.label.setStyleSheet("font: 75 24pt \"MS Shell Dlg 2\";")
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setLineWidth(2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.prediction)
        self.pushButton_2.clicked.connect(self.clear)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "State Name :"))
        self.label_3.setText(_translate("Dialog", "District:"))
        self.label_4.setText(_translate("Dialog", "Select Season"))
        self.comboBox.setItemText(0, _translate("Dialog", "-------------Select---------------"))
        self.comboBox.setItemText(1, _translate("Dialog", "Winter"))
        self.comboBox.setItemText(2, _translate("Dialog", "Autumn"))
        self.comboBox.setItemText(3, _translate("Dialog", "Summer"))
        self.comboBox.setItemText(4, _translate("Dialog", "Kharif"))
        self.comboBox.setItemText(5, _translate("Dialog", "Rabi"))
        self.comboBox.setItemText(6, _translate("Dialog", "Whole Year"))
        self.label_5.setText(_translate("Dialog", "Enter Area"))
        self.pushButton.setText(_translate("Dialog", "Predict"))
        self.pushButton_2.setText(_translate("Dialog", "Clear Fields"))
        self.label_6.setText(_translate("Dialog", "Prediction "))
        self.label.setText(_translate("Dialog", "Prediction"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Prediction()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
