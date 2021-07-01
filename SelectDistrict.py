
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QCompleter
from Prediction import *
from DBconn import DBConnection


listofdist = ('MAYURBHANJ', 'GANJAM', 'BALESHWAR', 'BARGARH', 'BHADRAK', 'KENDUJHAR', 'KALAHANDI', 'CUTTACK', 'BALANGIR',
    'NABARANGPUR', 'KENDRAPARA', 'SUNDARGARH', 'PURI', 'KHORDHA', 'JAJAPUR', 'SAMBALPUR', 'NAYAGARH', 'SONEPUR',
    'MALKANGIRI', 'KORAPUT', 'DHENKANAL', 'JAGATSINGHAPUR', 'ANUGUL', 'NUAPADA', 'BOUDH', 'RAYAGADA',
    'GAJAPATI', 'DEOGARH', 'JHARSUGUDA', 'KANDHAMAL', 'SOUTH DISTRICT', 'WEST DISTRICT', 'EAST DISTRICT',
    'NORTH DISTRICT',
    'SOLAPUR', 'ANANTAPUR', 'MEDINIPUR WEST', 'JALGAON', 'AHMEDNAGAR', 'AURANGABAD', 'YAVATMAL', 'BARDHAMAN',
    'WEST GODAVARI', 'EAST GODAVARI', 'BEED', 'AMRAVATI', 'BULDHANA', 'NANDED', 'LATUR', 'HARDOI',
    '24 PARAGANAS SOUTH', 'BIRBHUM', 'GULBARGA', 'NALGONDA', 'KURNOOL', 'ADILABAD', 'WASHIM', 'BANKURA',
    'JALNA', 'KRISHNA', 'RAJNANDGAON', 'GUNTUR', 'SANGRUR', 'PURULIA', 'PARBHANI', 'MAHASAMUND', 'KHERI',
    'PUNE',
    'SHAHJAHANPUR', 'LUDHIANA', 'BUDAUN', 'MEDINIPUR EAST', 'BATHINDA', 'JANJGIR-CHAMPA', 'AZAMGARH', 'UNNAO',
    'SPSR NELLORE', 'BALODA BAZAR', 'MAHBUBNAGAR', 'AKOLA', 'PATIALA', 'RAIGARH', 'WARANGAL', 'BILASPUR',
    'ALIGARH', 'MURSHIDABAD', 'NAGPUR', 'UDAM SINGH NAGAR', 'COOCHBEHAR', 'OSMANABAD', 'KARIMNAGAR',
    'ALLAHABAD',
    'BAREILLY', 'BIJNOR', 'SRIKAKULAM', 'DHULE', 'JAUNPUR', 'SITAPUR', 'MUKTSAR', 'WARDHA', 'FAZILKA',
    'DHAMTARI',
    'ROHTAS',
    'BULANDSHAHR', 'MATHURA', 'SANGLI', 'BARABANKI', 'GORAKHPUR', 'HOOGHLY', 'FIROZEPUR', 'BHANDARA',
    'AMRITSAR', 'TARN TARAN', 'BIJAPUR', 'GURDASPUR', 'RAIPUR', 'BALOD', 'JASHPUR', 'BELGAUM', 'DINAJPUR UTTAR',
    'DAVANGERE', 'KANKER', 'MOGA', 'JALPAIGURI', 'GHAZIPUR', 'GONDIA', 'FATEHPUR', 'LALITPUR', 'TUMKUR',
    'SIDDHARTH NAGAR',
    'RAE BARELI', 'JALANDHAR', 'MANSA', 'BAHRAICH', 'MAHARAJGANJ', 'MUZAFFARNAGAR', 'DINAJPUR DAKSHIN',
    'BEMETARA', 'KHAMMAM', 'JALAUN', 'DEORIA', 'JHANSI', 'GONDA', 'GADCHIROLI', 'NASHIK', 'BANDA', 'HOSHIARPUR',
    'MAINPURI',
    'PASHCHIM CHAMPARAN', 'RAMPUR', 'NAGAON', 'KOLHAPUR', 'SATARA', 'PILIBHIT', 'SAMBHAL', 'BALLIA',
    'CHANDRAPUR', 'MALDAH', 'GARIYABAND', '24 PARAGANAS NORTH', 'PRATAPGARH', 'HINGOLI', 'HAVERI', 'AGRA',
    'MEDAK',
    'ETAH',
    'BASTAR', 'DURG', 'SONITPUR', 'PURBI CHAMPARAN', 'VIZIANAGARAM', 'SAHARANPUR', 'KOZHIKODE', 'CHITTOOR',
    'MORADABAD', 'KANPUR DEHAT', 'MEERUT', 'AMBEDKAR NAGAR', 'BIDAR', 'BASTI', 'KARBI ANGLONG', 'CHITRADURGA',
    'NANDURBAR', 'KUSHI NAGAR', 'SURGUJA', 'KAPURTHALA', 'NADIA', 'RAIGAD', 'FARIDKOT', 'MADHUBANI', 'GOLAGHAT',
    'BARNALA', 'HAMIRPUR', 'NIZAMABAD', 'FAIZABAD', 'ALMORA', 'KORBA', 'MUZAFFARPUR', 'MUNGELI', 'BALRAMPUR',
    'SURAJPUR', 'SHIMOGA', 'VISAKHAPATANAM', 'PRAKASAM', 'RAICHUR', 'BAGALKOT', 'AURAIYA', 'SULTANPUR', 'GAYA',
    'YADGIR', 'MALAPPURAM', 'KANPUR NAGAR', 'LAKHIMPUR', 'CHANDAULI', 'KAIMUR (BHABUA)', 'KABIRDHAM',
    'KONDAGAON', 'BHOJPUR', 'KASGANJ', 'MIRZAPUR', 'FIROZABAD', 'AMETHI', 'ETAWAH', 'SIVASAGAR', 'BELLARY',
    'MAU',
    'MYSORE',
    'CACHAR', 'BANKA', 'AMROHA', 'SANT KABEER NAGAR', 'SIWAN', 'NALANDA', 'ARARIA', 'SITAMARHI',
    'PAURI GARHWAL', 'BAKSA', 'FATEHGARH SAHIB', 'KANNUR', 'GADAG', 'SARAN', 'JORHAT', 'THRISSUR', 'BUXAR',
    'HATHRAS',
    'DHARWAD',
    'SHRAVASTI', 'LUCKNOW', 'HASSAN', 'SUKMA', 'SUPAUL', 'BAGHPAT', 'NAWADA', 'FARRUKHABAD', 'TEHRI GARHWAL',
    'KANNAUJ', 'NAWANSHAHR', 'PALGHAR', 'GOPALGANJ', 'DIBRUGARH', 'KOREA', 'THIRUVANANTHAPURAM', 'HARIDWAR',
    'RATNAGIRI', 'HOWRAH', 'KAUSHAMBI', 'DANTEWADA', 'MAHOBA', 'KARIMGANJ', 'BARPETA', 'RAMANAGARA', 'VARANASI',
    'KADAPA', 'KAMRUP', 'DHEMAJI', 'SINDHUDURG', 'SAHARSA', 'PURNIA', 'RUPNAGAR', 'UTTAR KANNAD', 'PITHORAGARH',
    'JAMMU', 'KOKRAJHAR', 'CHIKBALLAPUR', 'KASARAGOD', 'PATNA', 'RANGAREDDI', 'UDALGURI', 'SHAMLI',
    'KISHANGANJ', 'NALBARI', 'PALAKKAD', 'DARBHANGA', 'SONBHADRA', 'TINSUKIA', 'KOPPAL', 'KATIHAR',
    'SAMASTIPUR',
    'THANE',
    'CHITRAKOOT', 'BEGUSARAI', 'MADHEPURA', 'KOLAR', 'KOLLAM', 'MANDYA', 'DHUBRI', 'GOALPARA', 'S.A.S NAGAR',
    'DARRANG', 'SANT RAVIDAS NAGAR', 'SEPAHIJALA', 'RAJAURI', 'BHAGALPUR', 'NAINITAL', 'DIMAPUR', 'VAISHALI',
    'HAPUR', 'CHIKMAGALUR', 'MARIGAON', 'IDUKKI', 'ERNAKULAM', 'CHAMOLI', 'DEHRADUN', 'UDUPI', 'JAMUI',
    'SOUTH TRIPURA', 'PATHANKOT', 'HAILAKANDI', 'NORTH GOA', 'GAUTAM BUDDHA NAGAR', 'BAGESHWAR', 'JEHANABAD',
    'CHIRANG', 'BANGALORE RURAL', 'UTTAR KASHI', 'BONGAIGAON', 'DAKSHIN KANNAD', 'ALAPPUZHA', 'GOMATI',
    'KHAGARIA', 'UDHAMPUR', 'KATHUA', 'CHAMARAJANAGAR', 'NORTH TRIPURA', 'DHALAI', 'KODAGU', 'RUDRA PRAYAG',
    'LAKHISARAI',
    'DARJEELING', 'SHEIKHPURA', 'GHAZIABAD', 'KOTTAYAM', 'BADGAM', 'ARWAL', 'DODA', 'WEST TRIPURA',
    'NARAYANPUR', 'WEST SIANG', 'ANANTNAG', 'POONCH', 'BENGALURU URBAN', 'KHOWAI', 'CHAMPAWAT', 'BARAMULLA',
    'MUNGER',
    'REASI', 'KAMRUP METRO', 'MON', 'KULGAM', 'WOKHA', 'KUPWARA', 'SHEOHAR', 'RAMBAN', 'UNAKOTI', 'EAST SIANG',
    'PULWAMA', 'TUENSANG', 'PATHANAMTHITTA', 'PEREN', 'MOKOKCHUNG', 'SOUTH GOA', 'PHEK', 'KOHIMA',
    'LOWER DIBANG VALLEY',
    'DADRA AND NAGAR HAVELI', 'ZUNHEBOTO', 'KISHTWAR', 'WAYANAD', 'LOHIT', 'WEST GARO HILLS', 'PAPUM PARE',
    'KIPHIRE', 'RI BHOI', 'BANDIPORA', 'SAMBA', 'DIMA HASAO', 'CHANGLANG', 'EAST KAMENG', 'EAST KHASI HILLS',
    'WEST JAINTIA HILLS', 'GANDERBAL', 'LOWER SUBANSIRI', 'SOUTH WEST GARO HILLS', 'LONGLENG', 'UPPER SIANG',
    'WEST KHASI HILLS', 'EAST GARO HILLS', 'UPPER SUBANSIRI', 'NORTH GARO HILLS', 'SOUTH GARO HILLS',
    'PONDICHERRY', 'EAST JAINTIA HILLS', 'KARAIKAL', 'SRINAGAR', 'TIRAP', 'ANJAW', 'WEST KAMENG', 'LONGDING',
    'DIBANG VALLEY',
    'SOUTH WEST KHASI HILLS', 'TAWANG', 'KURUNG KUMEY', 'YANAM', 'SHOPIAN', 'NAMSAI', 'KARGIL', 'LEH LADAKH',
    'UJJAIN', 'SAGAR', 'DEWAS', 'RAJGARH', 'VIDISHA', 'SEHORE', 'DHAR', 'MANDSAUR', 'HOSHANGABAD', 'BALAGHAT',
    'GUNA', 'SHAJAPUR', 'RAISEN', 'BETUL', 'RATLAM', 'INDORE', 'KHARGONE', 'SHIVPURI', 'CHHATARPUR', 'KHANDWA',
    'BHIND', 'DAMOH', 'HARDA', 'THIRUVARUR', 'VILLUPURAM', 'THANJAVUR', 'ASHOKNAGAR', 'TIKAMGARH',
    'NAGAPATTINAM', 'CHHINDWARA', 'REWA', 'SEONI', 'SATNA', 'MORENA', 'AGAR MALWA', 'DATIA', 'MANDLA',
    'NEEMUCH',
    'CUDDALORE',
    'JABALPUR', 'GWALIOR', 'RAMANATHAPURAM', 'BHOPAL', 'SHAHDOL', 'KATNI', 'ANUPPUR', 'NARSINGHPUR',
    'THIRUVALLUR', 'SHEOPUR', 'KANCHIPURAM', 'PANNA', 'COIMBATORE', 'TIRUVANNAMALAI', 'DINDORI', 'PUDUKKOTTAI',
    'SIDHI',
    'JHABUA', 'BARWANI', 'SIVAGANGA', 'TIRUNELVELI', 'NAMAKKAL', 'TIRUPPUR', 'ALIRAJPUR', 'KRISHNAGIRI',
    'TIRUCHIRAPPALLI', 'SINGRAULI', 'PERAMBALUR', 'BURHANPUR', 'UMARIA', 'VELLORE', 'TUTICORIN', 'MADURAI',
    'DINDIGUL',
    'ERODE',
    'ARIYALUR', 'DHARMAPURI', 'SALEM', 'KANNIYAKUMARI', 'VIRUDHUNAGAR', 'KARUR', 'THENI', 'THE NILGIRIS',
    'SURENDRANAGAR', 'RAJKOT', 'BHAVNAGAR', 'JUNAGADH', 'SIRSA', 'AMRELI', 'HISAR', 'JIND', 'VADODARA',
    'JAMNAGAR', 'FATEHABAD', 'AHMADABAD', 'KARNAL', 'KAITHAL', 'BHIWANI', 'SABAR KANTHA', 'SONIPAT',
    'BANAS KANTHA',
    'KACHCHH', 'DOHAD', 'BHARUCH', 'PANCH MAHALS', 'KURUKSHETRA', 'ROHTAK', 'MAHENDRAGARH', 'PALWAL', 'JHAJJAR',
    'ANAND',
    'AMBALA', 'KHEDA', 'PANIPAT', 'YAMUNANAGAR', 'SURAT', 'MAHESANA', 'PATAN', 'MEWAT', 'REWARI', 'VALSAD',
    'PORBANDAR', 'NAVSARI', 'TAPI', 'GURGAON', 'NARMADA', 'GANDHINAGAR', 'FARIDABAD', 'PANCHKULA', 'DANG',
    'MAHE', 'BARMER', 'BIKANER', 'JODHPUR', 'NAGAUR', 'JAISALMER', 'CHURU', 'JALORE', 'JAIPUR', 'SIKAR',
    'HANUMANGARH',
    'JHUNJHUNU', 'GANGANAGAR', 'ALWAR', 'JHALAWAR', 'BHARATPUR', 'BHILWARA', 'BARAN', 'TONK', 'CHITTORGARH',
    'UDAIPUR', 'AJMER', 'SAWAI MADHOPUR', 'BUNDI', 'BANSWARA', 'DAUSA', 'PALI', 'KARAULI', 'KOTA', 'KANGRA',
    'DUNGARPUR', 'DHOLPUR', 'MANDI', 'RAJSAMAND', 'SIROHI', 'UNA', 'CHAMBA', 'SIRMAUR', 'SOLAN', 'KULLU',
    'NICOBARS', 'SHIMLA', 'PALAMU', 'NORTH AND MIDDLE ANDAMAN', 'GARHWA', 'DUMKA', 'CHATRA', 'GODDA',
    'SOUTH ANDAMANS', 'GIRIDIH', 'SAHEBGANJ', 'RANCHI', 'DEOGHAR', 'HAZARIBAGH', 'LAHUL AND SPITI', 'LOHARDAGA',
    'PAKUR', 'KINNAUR', 'JAMTARA', 'LATEHAR', 'GUMLA', 'RAMGARH', 'BOKARO', 'CHANDIGARH', 'KODERMA', 'SIMDEGA',
    'KHUNTI', 'WEST SINGHBHUM', 'EAST SINGHBUM', 'SARAIKELA KHARSAWAN', 'DHANBAD', 'CHAMPHAI', 'LUNGLEI',
    'MAMIT', 'SERCHHIP', 'KOLASIB', 'AIZAWL', 'LAWNGTLAI', 'SAIHA', 'THOUBAL', 'IMPHAL EAST', 'SENAPATI',
    'IMPHAL WEST',
    'CHURACHANDPUR', 'BISHNUPUR', 'UKHRUL', 'TAMENGLONG', 'CHANDEL', 'HYDERABAD', 'MUMBAI')


class Ui_district(object):
    # def __init__(self, dialog):
    #     self.Dialog = dialog
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()

    def search(self,list, platform):

        for i in range(len(list)):
            if list[i] == platform:
                return True
        return False

    def entry(self):
       try:
            dist = self.lineEdit.text()

            if dist=="" or dist=="null":
                self.alertmsg("Error","Enter the District")
            elif self.search(listofdist, dist):
                state=self.state()

                self.Dialog = QtWidgets.QDialog()
                self.ui = Ui_Prediction(dist,state)
                self.ui.setupUi(self.Dialog)
                self.Dialog.show()
            else:
                self.alertmsg("Error","District Not Found")
            return dist
       except Exception as e:
            print("error",e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
    def state(self):
        dist = self.lineEdit.text()
        mydb = DBConnection.getConnection()
        cursor = mydb.cursor()
        query = "select (State_Name) from (dataset) where (District_Name) like (%s)"
        cursor.execute(query, (dist,))
        getdistrict = cursor.fetchall()

        for res in getdistrict:
            val = str(res)[2:-3]
            return val

    def setupUi(self, Dialog):
        district = listofdist
        Dialog.setObjectName("Dialog")
        Dialog.resize(893, 451)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.995025 rgba(96, 128, 213, 255), stop:1 rgba(46, 107, 215, 204));")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(120, 140, 681, 251))
        self.frame.setStyleSheet("QFrame{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(224, 224, 224, 232));}")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 20, 251, 31))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:1 rgba(58, 194, 55, 0));\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(30, 60, 601, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 14pt \"Arial\";")

        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setGeometry(QtCore.QRect(230, 140, 181, 41))
        self.pushButton.setStyleSheet("background-color: rgb(176, 90, 150);\n"
"font: 75 14pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        completer = QCompleter(district)
        self.lineEdit.setCompleter(completer)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.entry)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Enter Your District:"))
        self.pushButton.setText(_translate("Dialog", "Enter"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_district()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
