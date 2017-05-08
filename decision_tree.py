#!/usr/bin/python3
import numpy as np
import pandas as pd
from os import listdir
from os.path import isfile, join
from sklearn.ensemble import RandomForestClassifier
import statistics
from sklearn import tree
from sklearn.preprocessing import Imputer
import random
import pydotplus 

#from IPython.display import Image
#zero means they are alive, one means they are dead

if __name__ == "__main__":
	score = []
	tt = []
	for i in range(10):
		
		nums = [x for x in range(1,4001)]
		random.shuffle(nums)
		train = nums[:1000]
		test = nums[1000:4000]

		mypath = '/Users/Alex/Desktop/ads/set-a/'
		files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

		mortal_aa = []
		mortal_oo = []
		
		DiasABP = []
		MAP = []
		SysABP = []
		NIDiasABP = []
		NIMAP = []
		NISysABP = []
		Albumin = []
		ALP = []
		ALT = []
		AST = []
		Bilirubin = []
		BUN = []
		Cholesterol = []
		Creatinine = []
		FiO2 = []
		GCS = []
		Glucose = []
		HCO3 = []
		HCT = []
		HR = []
		K = []
		Lactate = []
		Mg = []
		MechVent = []
		Na = []
		PaCO2 = []
		PaO2 = []
		pH = []
		Platelets = []
		RespRate = []
		SaO2 = []
		Temp = []
		TroponinI = []
		TroponinT = []
		Urine = []
		WBC = []
		#Age = 0,Gender= 0 ,Height = 0
		Age = ''
		Gender = ''
		Height = ''
		ICUType = [0,0,0,0]
		a = []
		o = []
		i = 0
		


		for filename in files:
			i+=1
			DiasABP = []
			MAP = []
			SysABP = []
			NIDiasABP = []
			NIMAP = []
			NISysABP = []
			Albumin = []
			ALP = []
			ALT = []
			AST = []
			Bilirubin = []
			BUN = []
			Cholesterol = []
			Creatinine = []
			FiO2 = []
			GCS = []
			Glucose = []
			HCO3 = []
			HCT = []
			HR = []
			K = []
			Lactate = []
			Mg = []
			MechVent = []
			Na = []
			PaCO2 = []
			PaO2 = []
			pH = []
			Platelets = []
			RespRate = []
			SaO2 = []
			Temp = []
			TroponinI = []
			TroponinT = []
			Urine = []
			WBC = []
			readfile = open(mypath+filename,"r")
			
			

			for line in readfile:
				T,P,V = line.split(",")
				V = V.strip()
				if(P == 'RecordID'):
					id = V
				elif(T == 'Time'):
					pass
				elif(P == 'Age'):
					Age = float(V)
				elif(P == 'Gender'):
					Gender = float(V)
				elif(P == 'Height'):
					Height = float(V)
				elif(P == 'ICUType'):
					ICUType[int(V)-1] = ICUType[int(V)-1]+1
				elif(P == 'DiasABP'):
					DiasABP.append(float(V))
				elif(P == 'MAP'):
					MAP.append(float(V))
				elif(P == 'SysABP'):
					SysABP.append(float(V))
				elif(P == 'NIDiasABP'):
					NIDiasABP.append(float(V))
				elif(P == 'NIMAP'):
					NIMAP.append(float(V))
				elif(P == 'NISysABP'):
					NISysABP.append(float(V))
				elif(P == 'Albumin'):
					Albumin.append(float(V))
				elif(P == 'ALP'):
					ALP.append(float(V))
				elif(P == 'ALT'):
					ALT.append(float(V))
				elif(P == 'AST'):
					AST.append(float(V))
				elif(P == 'Bilirubin'):
					Bilirubin.append(float(V))
				elif(P == 'BUN'):
					BUN.append(float(V))
				elif(P == 'Cholesterol'):
					Cholesterol.append(float(V))
				elif(P == 'Creatinine'):
					Creatinine.append(float(V))
				elif(P == 'FiO2'):
					FiO2.append(float(V))
				elif(P == 'GCS'):
					GCS.append(float(V))
				elif(P == 'Glucose'):
					Glucose.append(float(V))
				elif(P == 'HCO3'):
					HCO3.append(float(V))
				elif(P == 'HCT'):
					HCT.append(float(V))
				elif(P == 'HR'):
					HR.append(float(V))
				elif(P == 'K'):
					K.append(float(V))
				elif(P == 'Lactate'):
					Lactate.append(float(V))
				elif(P == 'Mg'):
					Mg.append(float(V))
				elif(P == 'MechVent'):
					MechVent.append(float(V))
				elif(P == 'Na'):
					Na.append(float(V))
				elif(P == 'PaCO2'):
					PaCO2.append(float(V))
				elif(P == 'PaO2'):
					PaO2.append(float(V))
				elif(P == 'pH'):
					pH.append(float(V))
				elif(P == 'Platelets'):
					Platelets.append(float(V))
				elif(P == 'RespRate'):
					RespRate.append(float(V))
				elif(P == 'SaO2'):
					SaO2.append(float(V))
				elif(P == 'Temp'):
					Temp.append(float(V))
				elif(P == 'TroponinI'):
					TroponinI.append(float(V))
				elif(P == 'Troponfloat'):
					Troponfloat.append(float(V))
				elif(P == 'Urine'):
					Urine.append(float(V))
				elif(P == 'WBC'):
					WBC.append(float(V))
		
			if(Height == -1):
				Height = np.nan

			if(len(DiasABP) == 0):
				min_DiasABP = np.nan
				max_DiasABP = np.nan
				median_DiasABP = np.nan
				first_DiasABP = np.nan
				last_DiasABP = np.nan
				number_DiasABP = np.nan
			else:
				min_DiasABP = min(DiasABP)
				max_DiasABP = max(DiasABP)
				median_DiasABP =statistics.median(DiasABP)
				first_DiasABP = DiasABP[0]
				last_DiasABP = DiasABP[-1]
				number_DiasABP = len(DiasABP)

			if(len(MAP) == 0):
				min_MAP = np.nan
				max_MAP= np.nan
				median_MAP= np.nan
				first_MAP= np.nan
				last_MAP = np.nan
				number_MAP = np.nan
			else:
				min_MAP= min(MAP)
				max_MAP= max(MAP)
				median_MAP =statistics.median(MAP)
				first_MAP = MAP[0]
				last_MAP = MAP[-1]
				number_MAP = len(MAP)

			if(len(SysABP) == 0):
				min_SysABP = np.nan
				max_SysABP= np.nan
				median_SysABP= np.nan
				first_SysABP= np.nan
				last_SysABP = np.nan
				number_SysABP = np.nan
			else:
				min_SysABP= min(SysABP)
				max_SysABP= max(SysABP)
				median_SysABP =statistics.median(SysABP)
				first_SysABP = SysABP[0]
				last_SysABP = SysABP[-1]
				number_SysABP = len(SysABP)

			if(len(NIDiasABP) == 0):
				min_NIDiasABP = np.nan
				max_NIDiasABP= np.nan
				median_NIDiasABP= np.nan
				first_NIDiasABP= np.nan
				last_NIDiasABP = np.nan
				number_NIDiasABP = np.nan
			else:
				min_NIDiasABP= min(NIDiasABP)
				max_NIDiasABP= max(NIDiasABP)
				median_NIDiasABP =statistics.median(NIDiasABP)
				first_NIDiasABP = NIDiasABP[0]
				last_NIDiasABP = NIDiasABP[-1]
				number_NIDiasABP = len(NIDiasABP)

			if(len(NIMAP) == 0):
				min_NIMAP = np.nan
				max_NIMAP= np.nan
				median_NIMAP= np.nan
				first_NIMAP= np.nan
				last_NIMAP = np.nan
				number_NIMAP = np.nan
			else:
				min_NIMAP= min(NIMAP)
				max_NIMAP= max(NIMAP)
				median_NIMAP =statistics.median(NIMAP)
				first_NIMAP = NIMAP[0]
				last_NIMAP = NIMAP[-1]
				number_NIMAP = len(NIMAP)

			if(len(NISysABP) == 0):
				min_NISysABP = np.nan
				max_NISysABP= np.nan
				median_NISysABP= np.nan
				first_NISysABP= np.nan
				last_NISysABP = np.nan
				number_NISysABP = np.nan
			else:
				min_NISysABP= min(NISysABP)
				max_NISysABP= max(NISysABP)
				median_NISysABP =statistics.median(NISysABP)
				first_NISysABP = NISysABP[0]
				last_NISysABP = NISysABP[-1]
				number_NISysABP = len(NISysABP)

			if(len(Albumin) == 0):
				min_Albumin = np.nan
				max_Albumin= np.nan
				median_Albumin= np.nan
				first_Albumin= np.nan
				last_Albumin = np.nan
				number_Albumin = np.nan
			else:
				min_Albumin= min(Albumin)
				max_Albumin= max(Albumin)
				median_Albumin =statistics.median(Albumin)
				first_Albumin = Albumin[0]
				last_Albumin = Albumin[-1]
				number_Albumin = len(Albumin)

			if(len(ALP) == 0):
				min_ALP = np.nan
				max_ALP= np.nan
				median_ALP= np.nan
				first_ALP= np.nan
				last_ALP = np.nan
				number_ALP = np.nan
			else:
				min_ALP= min(ALP)
				max_ALP= max(ALP)
				median_ALP =statistics.median(ALP)
				first_ALP = ALP[0]
				last_ALP = ALP[-1]
				number_ALP = len(ALP)

			if(len(ALT) == 0):
				min_ALT = np.nan
				max_ALT= np.nan
				median_ALT= np.nan
				first_ALT= np.nan
				last_ALT = np.nan
				number_ALT = np.nan
			else:
				min_ALT= min(ALT)
				max_ALT= max(ALT)
				median_ALT =statistics.median(ALT)
				first_ALT = ALT[0]
				last_ALT = ALT[-1]
				number_ALT = len(ALT)

			if(len(AST) == 0):
				min_AST = np.nan
				max_AST= np.nan
				median_AST= np.nan
				first_AST= np.nan
				last_AST = np.nan
				number_AST = np.nan
			else:
				min_AST= min(AST)
				max_AST= max(AST)
				median_AST =statistics.median(AST)
				first_AST = AST[0]
				last_AST = AST[-1]
				number_AST = len(AST)

			if(len(Bilirubin) == 0):
				min_Bilirubin = np.nan
				max_Bilirubin= np.nan
				median_Bilirubin= np.nan
				first_Bilirubin= np.nan
				last_Bilirubin = np.nan
				number_Bilirubin = np.nan
			else:
				min_Bilirubin= min(Bilirubin)
				max_Bilirubin= max(Bilirubin)
				median_Bilirubin =statistics.median(Bilirubin)
				first_Bilirubin = Bilirubin[0]
				last_Bilirubin = Bilirubin[-1]
				number_Bilirubin = len(Bilirubin)

			if(len(BUN) == 0):
				min_BUN = np.nan
				max_BUN= np.nan
				median_BUN= np.nan
				first_BUN= np.nan
				last_BUN = np.nan
				number_BUN = np.nan
			else:
				min_BUN= min(BUN)
				max_BUN= max(BUN)
				median_BUN =statistics.median(BUN)
				first_BUN = BUN[0]
				last_BUN = BUN[-1]
				number_BUN = len(BUN)

			if(len(Cholesterol) == 0):
				min_Cholesterol = np.nan
				max_Cholesterol= np.nan
				median_Cholesterol= np.nan
				first_Cholesterol= np.nan
				last_Cholesterol = np.nan
				number_Cholesterol = np.nan
			else:
				min_Cholesterol= min(Cholesterol)
				max_Cholesterol= max(Cholesterol)
				median_Cholesterol =statistics.median(Cholesterol)
				first_Cholesterol = Cholesterol[0]
				last_Cholesterol = Cholesterol[-1]
				number_Cholesterol = len(Cholesterol)

			if(len(Creatinine) == 0):
				min_Creatinine = np.nan
				max_Creatinine= np.nan
				median_Creatinine= np.nan
				first_Creatinine= np.nan
				last_Creatinine = np.nan
				number_Creatinine = np.nan
			else:
				min_Creatinine= min(Creatinine)
				max_Creatinine= max(Creatinine)
				median_Creatinine =statistics.median(Creatinine)
				first_Creatinine = Creatinine[0]
				last_Creatinine = Creatinine[-1]
				number_Creatinine = len(Creatinine)

			if(len(FiO2) == 0):
				min_FiO2 = np.nan
				max_FiO2= np.nan
				median_FiO2= np.nan
				first_FiO2= np.nan
				last_FiO2 = np.nan
				number_FiO2 = np.nan
			else:
				min_FiO2= min(FiO2)
				max_FiO2= max(FiO2)
				median_FiO2 =statistics.median(FiO2)
				first_FiO2 = FiO2[0]
				last_FiO2 = FiO2[-1]
				number_FiO2 = len(FiO2)

			if(len(GCS) == 0):
				min_GCS = np.nan
				max_GCS= np.nan
				median_GCS= np.nan
				first_GCS= np.nan
				last_GCS = np.nan
				number_GCS = np.nan
			else:
				min_GCS= min(GCS)
				max_GCS= max(GCS)
				median_GCS =statistics.median(GCS)
				first_GCS = GCS[0]
				last_GCS = GCS[-1]
				number_GCS = len(GCS)

			if(len(Glucose) == 0):
				min_Glucose = np.nan
				max_Glucose= np.nan
				median_Glucose= np.nan
				first_Glucose= np.nan
				last_Glucose = np.nan
				number_Glucose = np.nan
			else:
				min_Glucose= min(Glucose)
				max_Glucose= max(Glucose)
				median_Glucose =statistics.median(Glucose)
				first_Glucose = Glucose[0]
				last_Glucose = Glucose[-1]
				number_Glucose = len(Glucose)

			if(len(HCO3) == 0):
				min_HCO3 = np.nan
				max_HCO3= np.nan
				median_HCO3= np.nan
				first_HCO3= np.nan
				last_HCO3 = np.nan
				number_HCO3 = np.nan
			else:
				min_HCO3= min(HCO3)
				max_HCO3= max(HCO3)
				median_HCO3 =statistics.median(HCO3)
				first_HCO3 = HCO3[0]
				last_HCO3 = HCO3[-1]
				number_HCO3 = len(HCO3)

			if(len(HCT) == 0):
				min_HCT = np.nan
				max_HCT= np.nan
				median_HCT= np.nan
				first_HCT= np.nan
				last_HCT = np.nan
				number_HCT = np.nan
			else:
				min_HCT= min(HCT)
				max_HCT= max(HCT)
				median_HCT =statistics.median(HCT)
				first_HCT = HCT[0]
				last_HCT = HCT[-1]
				number_HCT = len(HCT)

			if(len(HR) == 0):
				min_HR = np.nan
				max_HR= np.nan
				median_HR= np.nan
				first_HR= np.nan
				last_HR = np.nan
				number_HR = np.nan
			else:
				min_HR= min(HR)
				max_HR= max(HR)
				median_HR =statistics.median(HR)
				first_HR = HR[0]
				last_HR = HR[-1]
				number_HR = len(HR)

			if(len(K) == 0):
				min_K = np.nan
				max_K= np.nan
				median_K= np.nan
				first_K= np.nan
				last_K = np.nan
				number_K = np.nan
			else:
				min_K= min(K)
				max_K= max(K)
				median_K =statistics.median(K)
				first_K = K[0]
				last_K = K[-1]
				number_K = len(K)

			if(len(Lactate) == 0):
				min_Lactate = np.nan
				max_Lactate= np.nan
				median_Lactate= np.nan
				first_Lactate= np.nan
				last_Lactate = np.nan
				number_Lactate = np.nan
			else:
				min_Lactate= min(Lactate)
				max_Lactate= max(Lactate)
				median_Lactate =statistics.median(Lactate)
				first_Lactate = Lactate[0]
				last_Lactate = Lactate[-1]
				number_Lactate = len(Lactate)

			if(len(Mg) == 0):
				min_Mg = np.nan
				max_Mg= np.nan
				median_Mg= np.nan
				first_Mg= np.nan
				last_Mg = np.nan
				number_Mg = np.nan
			else:
				min_Mg= min(Mg)
				max_Mg= max(Mg)
				median_Mg =statistics.median(Mg)
				first_Mg = Mg[0]
				last_Mg = Mg[-1]
				number_Mg = len(Mg)

			if(len(MechVent) == 0):
				min_MechVent = np.nan
				max_MechVent= np.nan
				median_MechVent= np.nan
				first_MechVent= np.nan
				last_MechVent = np.nan
				number_MechVent = np.nan
			else:
				min_MechVent= min(MechVent)
				max_MechVent= max(MechVent)
				median_MechVent =statistics.median(MechVent)
				first_MechVent = MechVent[0]
				last_MechVent = MechVent[-1]
				number_MechVent = len(MechVent)

			if(len(Na) == 0):
				min_Na = np.nan
				max_Na= np.nan
				median_Na= np.nan
				first_Na= np.nan
				last_Na = np.nan
				number_Na = np.nan
			else:
				min_Na= min(Na)
				max_Na= max(Na)
				median_Na =statistics.median(Na)
				first_Na = Na[0]
				last_Na = Na[-1]
				number_Na = len(Na)

			if(len(PaCO2) == 0):
				min_PaCO2 = np.nan
				max_PaCO2= np.nan
				median_PaCO2= np.nan
				first_PaCO2= np.nan
				last_PaCO2 = np.nan
				number_PaCO2 = np.nan
			else:
				min_PaCO2= min(PaCO2)
				max_PaCO2= max(PaCO2)
				median_PaCO2 =statistics.median(PaCO2)
				first_PaCO2 = PaCO2[0]
				last_PaCO2 = PaCO2[-1]
				number_PaCO2 = len(PaCO2)

			if(len(PaO2) == 0):
				min_PaO2 = np.nan
				max_PaO2= np.nan
				median_PaO2= np.nan
				first_PaO2= np.nan
				last_PaO2 = np.nan
				number_PaO2 = np.nan
			else:
				min_PaO2= min(PaO2)
				max_PaO2= max(PaO2)
				median_PaO2 =statistics.median(PaO2)
				first_PaO2 = PaO2[0]
				last_PaO2 = PaO2[-1]
				number_PaO2 = len(PaO2)

			if(len(pH) == 0):
				min_pH = np.nan
				max_pH= np.nan
				median_pH= np.nan
				first_pH= np.nan
				last_pH = np.nan
				number_pH = np.nan
			else:
				min_pH= min(pH)
				max_pH= max(pH)
				median_pH =statistics.median(pH)
				first_pH = pH[0]
				last_pH = pH[-1]
				number_pH = len(pH)

			if(len(Platelets) == 0):
				min_Platelets = np.nan
				max_Platelets= np.nan
				median_Platelets= np.nan
				first_Platelets= np.nan
				last_Platelets = np.nan
				number_Platelets = np.nan
			else:
				min_Platelets= min(Platelets)
				max_Platelets= max(Platelets)
				median_Platelets =statistics.median(Platelets)
				first_Platelets = Platelets[0]
				last_Platelets = Platelets[-1]
				number_Platelets = len(Platelets)


			if(len(RespRate) == 0):
				min_RespRate = np.nan
				max_RespRate= np.nan
				median_RespRate= np.nan
				first_RespRate= np.nan
				last_RespRate = np.nan
				number_RespRate = np.nan
			else:
				min_RespRate= min(RespRate)
				max_RespRate= max(RespRate)
				median_RespRate =statistics.median(RespRate)
				first_RespRate = RespRate[0]
				last_RespRate = RespRate[-1]
				number_RespRate = len(RespRate)

			if(len(SaO2) == 0):
				min_SaO2 = np.nan
				max_SaO2= np.nan
				median_SaO2= np.nan
				first_SaO2= np.nan
				last_SaO2 = np.nan
				number_SaO2 = np.nan
			else:
				min_SaO2= min(SaO2)
				max_SaO2= max(SaO2)
				median_SaO2 =statistics.median(SaO2)
				first_SaO2 = SaO2[0]
				last_SaO2 = SaO2[-1]
				number_SaO2 = len(SaO2)

			if(len(Temp) == 0):
				min_Temp = np.nan
				max_Temp= np.nan
				median_Temp= np.nan
				first_Temp= np.nan
				last_Temp = np.nan
				number_Temp = np.nan
			else:
				min_Temp= min(Temp)
				max_Temp= max(Temp)
				median_Temp =statistics.median(Temp)
				first_Temp = Temp[0]
				last_Temp = Temp[-1]
				number_Temp = len(Temp)

			if(len(TroponinI) == 0):
				min_TroponinI = np.nan
				max_TroponinI= np.nan
				median_TroponinI= np.nan
				first_TroponinI= np.nan
				last_TroponinI = np.nan
				number_TroponinI = np.nan
			else:
				min_TroponinI= min(TroponinI)
				max_TroponinI= max(TroponinI)
				median_TroponinI =statistics.median(TroponinI)
				first_TroponinI = TroponinI[0]
				last_TroponinI = TroponinI[-1]
				number_TroponinI = len(TroponinI)

			if(len(TroponinT) == 0):
				min_TroponinT = np.nan
				max_TroponinT= np.nan
				median_TroponinT= np.nan
				first_TroponinT= np.nan
				last_TroponinT = np.nan
				number_TroponinT = np.nan
			else:
				min_TroponinT= min(TroponinT)
				max_TroponinT= max(TroponinT)
				median_TroponinT =statistics.median(TroponinT)
				first_TroponinT = TroponinT[0]
				last_TroponinT = TroponinT[-1]
				number_TroponinT = len(TroponinT)

			if(len(Urine) == 0):
				min_Urine = np.nan
				max_Urine= np.nan
				median_Urine= np.nan
				first_Urine= np.nan
				last_Urine = np.nan
				number_Urine = np.nan
			else:
				min_Urine= min(Urine)
				max_Urine= max(Urine)
				median_Urine =statistics.median(Urine)
				first_Urine = Urine[0]
				last_Urine = Urine[-1]
				number_Urine = len(Urine)

			if(len(WBC) == 0):
				min_WBC = np.nan
				max_WBC= np.nan
				median_WBC= np.nan
				first_WBC= np.nan
				last_WBC = np.nan
				number_WBC = np.nan
			else:
				min_WBC= min(WBC)
				max_WBC= max(WBC)
				median_WBC =statistics.median(WBC)
				first_WBC = WBC[0]
				last_WBC = WBC[-1]
				number_WBC = len(WBC)

			# with all data
			#if(i in train):
			#	a.append(np.array([Age,Gender,Height,min_DiasABP,max_DiasABP,median_DiasABP,first_DiasABP,last_DiasABP,number_DiasABP,min_MAP,max_MAP,median_MAP,first_MAP,last_MAP,number_MAP,min_SysABP,max_SysABP,median_SysABP,first_SysABP,last_SysABP,number_SysABP,min_NIDiasABP,max_NIDiasABP,median_NIDiasABP,first_NIDiasABP,last_NIDiasABP,number_NIDiasABP,min_NIMAP,max_NIMAP,median_NIMAP,first_NIMAP,last_NIMAP,number_NIMAP,min_NISysABP,max_NISysABP,median_NISysABP,first_NISysABP,last_NISysABP,number_NISysABP,min_Albumin,max_Albumin,median_Albumin,first_Albumin,last_Albumin,number_Albumin,min_ALP,max_ALP,median_ALP,first_ALP,last_ALP,number_ALP,min_ALT,max_ALT,median_ALT,first_ALT,last_ALT,number_ALT,min_AST,max_AST,median_AST,first_AST,last_AST,number_AST,min_Bilirubin,max_Bilirubin,median_Bilirubin,first_Bilirubin,last_Bilirubin,number_Bilirubin,min_BUN,max_BUN,median_BUN,first_BUN,last_BUN,number_BUN,min_Cholesterol,max_Cholesterol,median_Cholesterol,first_Cholesterol,last_Cholesterol,number_Cholesterol,min_Creatinine,max_Creatinine,median_Creatinine,first_Creatinine,last_Creatinine,number_Creatinine,min_FiO2,max_FiO2,median_FiO2,first_FiO2,last_FiO2,number_FiO2,min_GCS,max_GCS,median_GCS,first_GCS,last_GCS,number_GCS,min_Glucose,max_Glucose,median_Glucose,first_Glucose,last_Glucose,number_Glucose,min_HCO3,max_HCO3,median_HCO3,first_HCO3,last_HCO3,number_HCO3,min_HCT,max_HCT,median_HCT,first_HCT,last_HCT,number_HCT,min_HR,max_HR,median_HR,first_HR,last_HR,number_HR,min_K,max_K,median_K,first_K,last_K,number_K,min_Lactate,max_Lactate,median_Lactate,first_Lactate,last_Lactate,number_Lactate,min_Mg,max_Mg,median_Mg,first_Mg,last_Mg,number_Mg,min_MechVent,max_MechVent,median_MechVent,first_MechVent,last_MechVent,number_MechVent,min_Na,max_Na,median_Na,first_Na,last_Na,number_Na,min_PaCO2,max_PaCO2,median_PaCO2,first_PaCO2,last_PaCO2,number_PaCO2,min_PaO2,max_PaO2,median_PaO2,first_PaO2,last_PaO2,number_PaO2,min_pH,max_pH,median_pH,first_pH,last_pH,number_pH,min_Platelets,max_Platelets,median_Platelets,first_Platelets,last_Platelets,number_Platelets,min_RespRate,max_RespRate,median_RespRate,first_RespRate,last_RespRate,number_RespRate,min_SaO2,max_SaO2,median_SaO2,first_SaO2,last_SaO2,number_SaO2,min_Temp,max_Temp,median_Temp,first_Temp,last_Temp,number_Temp,min_TroponinI,max_TroponinI,median_TroponinI,first_TroponinI,last_TroponinI,number_TroponinI,min_TroponinT,max_TroponinT,median_TroponinT,first_TroponinT,last_TroponinT,number_TroponinT,min_Urine,max_Urine,median_Urine,first_Urine,last_Urine,number_Urine,min_WBC,max_WBC,median_WBC,first_WBC,last_WBC,number_WBC]))
			#elif(i in test):
			#	o.append(np.array([Age,Gender,Height,min_DiasABP,max_DiasABP,median_DiasABP,first_DiasABP,last_DiasABP,number_DiasABP,min_MAP,max_MAP,median_MAP,first_MAP,last_MAP,number_MAP,min_SysABP,max_SysABP,median_SysABP,first_SysABP,last_SysABP,number_SysABP,min_NIDiasABP,max_NIDiasABP,median_NIDiasABP,first_NIDiasABP,last_NIDiasABP,number_NIDiasABP,min_NIMAP,max_NIMAP,median_NIMAP,first_NIMAP,last_NIMAP,number_NIMAP,min_NISysABP,max_NISysABP,median_NISysABP,first_NISysABP,last_NISysABP,number_NISysABP,min_Albumin,max_Albumin,median_Albumin,first_Albumin,last_Albumin,number_Albumin,min_ALP,max_ALP,median_ALP,first_ALP,last_ALP,number_ALP,min_ALT,max_ALT,median_ALT,first_ALT,last_ALT,number_ALT,min_AST,max_AST,median_AST,first_AST,last_AST,number_AST,min_Bilirubin,max_Bilirubin,median_Bilirubin,first_Bilirubin,last_Bilirubin,number_Bilirubin,min_BUN,max_BUN,median_BUN,first_BUN,last_BUN,number_BUN,min_Cholesterol,max_Cholesterol,median_Cholesterol,first_Cholesterol,last_Cholesterol,number_Cholesterol,min_Creatinine,max_Creatinine,median_Creatinine,first_Creatinine,last_Creatinine,number_Creatinine,min_FiO2,max_FiO2,median_FiO2,first_FiO2,last_FiO2,number_FiO2,min_GCS,max_GCS,median_GCS,first_GCS,last_GCS,number_GCS,min_Glucose,max_Glucose,median_Glucose,first_Glucose,last_Glucose,number_Glucose,min_HCO3,max_HCO3,median_HCO3,first_HCO3,last_HCO3,number_HCO3,min_HCT,max_HCT,median_HCT,first_HCT,last_HCT,number_HCT,min_HR,max_HR,median_HR,first_HR,last_HR,number_HR,min_K,max_K,median_K,first_K,last_K,number_K,min_Lactate,max_Lactate,median_Lactate,first_Lactate,last_Lactate,number_Lactate,min_Mg,max_Mg,median_Mg,first_Mg,last_Mg,number_Mg,min_MechVent,max_MechVent,median_MechVent,first_MechVent,last_MechVent,number_MechVent,min_Na,max_Na,median_Na,first_Na,last_Na,number_Na,min_PaCO2,max_PaCO2,median_PaCO2,first_PaCO2,last_PaCO2,number_PaCO2,min_PaO2,max_PaO2,median_PaO2,first_PaO2,last_PaO2,number_PaO2,min_pH,max_pH,median_pH,first_pH,last_pH,number_pH,min_Platelets,max_Platelets,median_Platelets,first_Platelets,last_Platelets,number_Platelets,min_RespRate,max_RespRate,median_RespRate,first_RespRate,last_RespRate,number_RespRate,min_SaO2,max_SaO2,median_SaO2,first_SaO2,last_SaO2,number_SaO2,min_Temp,max_Temp,median_Temp,first_Temp,last_Temp,number_Temp,min_TroponinI,max_TroponinI,median_TroponinI,first_TroponinI,last_TroponinI,number_TroponinI,min_TroponinT,max_TroponinT,median_TroponinT,first_TroponinT,last_TroponinT,number_TroponinT,min_Urine,max_Urine,median_Urine,first_Urine,last_Urine,number_Urine,min_WBC,max_WBC,median_WBC,first_WBC,last_WBC,number_WBC]))
			#with gcs
			#if(i in train):
			#	a.append(np.array([Age,Gender,Height,min_GCS,max_GCS,median_GCS,first_GCS,last_GCS,number_GCS]))
			#elif(i in test):
			#	o.append(np.array([Age,Gender,Height,min_GCS,max_GCS,median_GCS,first_GCS,last_GCS,number_GCS]))
			if(i in train):
				a.append(np.array([Age, min_HR,max_HR,median_HR,first_HR,last_HR,number_HR,min_NISysABP,max_NISysABP,median_NISysABP,first_NISysABP,last_NISysABP,number_NISysABP,min_Temp,max_Temp,median_Temp,first_Temp,last_Temp,number_Temp, min_RespRate,max_RespRate,median_RespRate,first_RespRate,last_RespRate,number_RespRate, min_Urine,max_Urine,median_Urine,first_Urine,last_Urine,number_Urine, min_BUN,max_BUN,median_BUN,first_BUN,last_BUN,number_BUN, min_HCT,max_HCT,median_HCT,first_HCT,last_HCT,number_HCT, min_WBC,max_WBC,median_WBC,first_WBC,last_WBC,number_WBC, min_Glucose,max_Glucose,median_Glucose,first_Glucose,last_Glucose,number_Glucose, min_K,max_K,median_K,first_K,last_K,number_K, min_Na,max_Na,median_Na,first_Na,last_Na,number_Na, min_HCO3,max_HCO3,median_HCO3,first_HCO3,last_HCO3,number_HCO3, min_GCS,max_GCS,median_GCS,first_GCS,last_GCS,number_GCS]))
			elif(i in test):
				o.append(np.array([Age, min_HR,max_HR,median_HR,first_HR,last_HR,number_HR,min_NISysABP,max_NISysABP,median_NISysABP,first_NISysABP,last_NISysABP,number_NISysABP,min_Temp,max_Temp,median_Temp,first_Temp,last_Temp,number_Temp, min_RespRate,max_RespRate,median_RespRate,first_RespRate,last_RespRate,number_RespRate, min_Urine,max_Urine,median_Urine,first_Urine,last_Urine,number_Urine, min_BUN,max_BUN,median_BUN,first_BUN,last_BUN,number_BUN, min_HCT,max_HCT,median_HCT,first_HCT,last_HCT,number_HCT, min_WBC,max_WBC,median_WBC,first_WBC,last_WBC,number_WBC, min_Glucose,max_Glucose,median_Glucose,first_Glucose,last_Glucose,number_Glucose, min_K,max_K,median_K,first_K,last_K,number_K, min_Na,max_Na,median_Na,first_Na,last_Na,number_Na, min_HCO3,max_HCO3,median_HCO3,first_HCO3,last_HCO3,number_HCO3, min_GCS,max_GCS,median_GCS,first_GCS,last_GCS,number_GCS]))
			
	
	
		aa = np.array(a)
		oo = np.array(o)

		imp1 = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)
		imp2 = Imputer(missing_values='NaN', strategy='most_frequent', axis=0)

		bb = imp1.fit_transform(aa)
		ii = imp2.fit_transform(oo)
		#print(bb)
		i = 0


		mypath1 ='/Users/Alex/Desktop/ads/Outcomes-a.txt'
		readfile = open(mypath1,"r")
		for line in readfile:
			id, a,b,c,d,m = line.split(",")
			
			if (id == 'RecordID'):
				pass
			else:
				i+=1
				m = m.strip()
				a = a.strip()
				#if(int(a)>=21):
				#	a = 1
				#else:
				#	a = 0
				
				if(i in train):
					#mortal_aa.append(int(m))
					mortal_aa.append(int(m))
					
				elif(i in test):
					#mortal_oo.append(int(m))
					mortal_oo.append(int(m))
		
		fa = np.array(mortal_aa)
		fo = np.array(mortal_oo)
		#print(fa)
		#print(mortal_aa)
		#print(fo)
		#print(len(mortal_aa))
		#print(mortal_oo[0])
		clf = tree.DecisionTreeClassifier()
		clf = clf.fit(bb,fa)
		
		#dot_data = tree.export_graphviz(clf, out_file=None)
		#graph = pydotplus.graph_from_dot_data(dot_data)
		#graph.write_pdf("main.pdf")

		result = clf.predict(ii)
		np.set_printoptions(threshold=np.inf)
		
		#print (result)
	#print(len(fa))
		dead = 0
		alive = 0
		tp = 0
		fp = 0
		tn = 0
		fn = 0
		j = 0
		for i in range(0,3000):
			#if result[i]>=22:
			#	result[i] = 1
			#else:
			#	result[i] = 0
			if mortal_oo[i] == 0:
				alive +=1
			else:
				dead +=1
			
			if(mortal_oo[i] == result[i] and result[i] == 1):
				tp +=1
			elif(mortal_oo[i] != result[i] and mortal_oo[i] == 0):
				fp +=1
			elif(mortal_oo[i] == result[i] and result[i] == 0):
				tn +=1
			elif(mortal_oo[i] != result[i] and mortal_oo[i] == 1):
				fn +=1

		print("TP:"+str(tp))
		print("FP:"+str(fp))
		print("TN:"+str(tn))
		print("FN:"+str(fn))

		Se = float(tp)/float(tp+fn)
		pplus = float(tp)/float(tp+fp)
		#print(Se)
		print("score:"+str(min(Se,pplus)))
		score.append(min(Se,pplus))

	print("final:"+str(sum(score)/float(len(score))))


		
	#print(alive)


	#print(j)
	#print(ICUType)

"""
	mypath1 = '/Users/Alex/Desktop/ads/set-b/'
	files1 = [f for f in listdir(mypath1) if isfile(join(mypath1, f))]
	c = []

	for filename in files1:
		DiasABP = []
		MAP = []
		SysABP = []
		NIDiasABP = []
		NIMAP = []
		NISysABP = []
		Albumin = []
		ALP = []
		ALT = []
		AST = []
		Bilirubin = []
		BUN = []
		Cholesterol = []
		Creatinine = []
		FiO2 = []
		GCS = []
		Glucose = []
		HCO3 = []
		HCT = []
		HR = []
		K = []
		Lactate = []
		Mg = []
		MechVent = []
		Na = []
		PaCO2 = []
		PaO2 = []
		pH = []
		Platelets = []
		RespRate = []
		SaO2 = []
		Temp = []
		TroponinI = []
		TroponinT = []
		Urine = []
		WBC = []
		readfile = open(mypath1+filename,"r")
		for line in readfile:
			T,P,V = line.split(",")
			V = V.strip()
			if(P == 'RecordID'):
				id = V
			elif(T == 'Time'):
				pass
			elif(P == 'Age'):
				Age = float(V)
			elif(P == 'Gender'):
				Gender = float(V)
			elif(P == 'Height'):
				Height = float(V)
			elif(P == 'DiasABP'):
				DiasABP.append(float(V))
			elif(P == 'MAP'):
				MAP.append(float(V))
			elif(P == 'SysABP'):
				SysABP.append(float(V))
			elif(P == 'NIDiasABP'):
				NIDiasABP.append(float(V))
			elif(P == 'NIMAP'):
				NIMAP.append(float(V))
			elif(P == 'NISysABP'):
				NISysABP.append(float(V))
			elif(P == 'Albumin'):
				Albumin.append(float(V))
			elif(P == 'ALP'):
				ALP.append(float(V))
			elif(P == 'ALT'):
				ALT.append(float(V))
			elif(P == 'AST'):
				AST.append(float(V))
			elif(P == 'Bilirubin'):
				Bilirubin.append(float(V))
			elif(P == 'BUN'):
				BUN.append(float(V))
			elif(P == 'Cholesterol'):
				Cholesterol.append(float(V))
			elif(P == 'Creatinine'):
				Creatinine.append(float(V))
			elif(P == 'FiO2'):
				FiO2.append(float(V))
			elif(P == 'GCS'):
				GCS.append(float(V))
			elif(P == 'Glucose'):
				Glucose.append(float(V))
			elif(P == 'HCO3'):
				HCO3.append(float(V))
			elif(P == 'HCT'):
				HCT.append(float(V))
			elif(P == 'HR'):
				HR.append(float(V))
			elif(P == 'K'):
				K.append(float(V))
			elif(P == 'Lactate'):
				Lactate.append(float(V))
			elif(P == 'Mg'):
				Mg.append(float(V))
			elif(P == 'MechVent'):
				MechVent.append(float(V))
			elif(P == 'Na'):
				Na.append(float(V))
			elif(P == 'PaCO2'):
				PaCO2.append(float(V))
			elif(P == 'PaO2'):
				PaO2.append(float(V))
			elif(P == 'pH'):
				pH.append(float(V))
			elif(P == 'Platelets'):
				Platelets.append(float(V))
			elif(P == 'RespRate'):
				RespRate.append(float(V))
			elif(P == 'SaO2'):
				SaO2.append(float(V))
			elif(P == 'Temp'):
				Temp.append(float(V))
			elif(P == 'TroponinI'):
				TroponinI.append(float(V))
			elif(P == 'Troponfloat'):
				Troponfloat.append(float(V))
			elif(P == 'Urine'):
				Urine.append(float(V))
			elif(P == 'WBC'):
				WBC.append(float(V))

		if(Height == -1):
			Height = np.nan
		
		if(len(DiasABP) == 0):
			min_DiasABP = np.nan
			max_DiasABP = np.nan
			median_DiasABP = np.nan
			first_DiasABP = np.nan
			last_DiasABP = np.nan
			number_DiasABP = np.nan
		else:
			min_DiasABP = min(DiasABP)
			max_DiasABP = max(DiasABP)
			median_DiasABP =statistics.median(DiasABP)
			first_DiasABP = DiasABP[0]
			last_DiasABP = DiasABP[-1]
			number_DiasABP = len(DiasABP)
		
		if(len(MAP) == 0):
			min_MAP = np.nan
			max_MAP= np.nan
			median_MAP= np.nan
			first_MAP= np.nan
			last_MAP = np.nan
			number_MAP = np.nan
		else:
			min_MAP= min(MAP)
			max_MAP= max(MAP)
			median_MAP =statistics.median(MAP)
			first_MAP = MAP[0]
			last_MAP = MAP[-1]
			number_MAP = len(MAP)

		if(len(SysABP) == 0):
			min_SysABP = np.nan
			max_SysABP= np.nan
			median_SysABP= np.nan
			first_SysABP= np.nan
			last_SysABP = np.nan
			number_SysABP = np.nan
		else:
			min_SysABP= min(SysABP)
			max_SysABP= max(SysABP)
			median_SysABP =statistics.median(SysABP)
			first_SysABP = SysABP[0]
			last_SysABP = SysABP[-1]
			number_SysABP = len(SysABP)

		if(len(NIDiasABP) == 0):
			min_NIDiasABP = np.nan
			max_NIDiasABP= np.nan
			median_NIDiasABP= np.nan
			first_NIDiasABP= np.nan
			last_NIDiasABP = np.nan
			number_NIDiasABP = np.nan
		else:
			min_NIDiasABP= min(NIDiasABP)
			max_NIDiasABP= max(NIDiasABP)
			median_NIDiasABP =statistics.median(NIDiasABP)
			first_NIDiasABP = NIDiasABP[0]
			last_NIDiasABP = NIDiasABP[-1]
			number_NIDiasABP = len(NIDiasABP)

		if(len(NIMAP) == 0):
			min_NIMAP = np.nan
			max_NIMAP= np.nan
			median_NIMAP= np.nan
			first_NIMAP= np.nan
			last_NIMAP = np.nan
			number_NIMAP = np.nan
		else:
			min_NIMAP= min(NIMAP)
			max_NIMAP= max(NIMAP)
			median_NIMAP =statistics.median(NIMAP)
			first_NIMAP = NIMAP[0]
			last_NIMAP = NIMAP[-1]
			number_NIMAP = len(NIMAP)

		if(len(NISysABP) == 0):
			min_NISysABP = np.nan
			max_NISysABP= np.nan
			median_NISysABP= np.nan
			first_NISysABP= np.nan
			last_NISysABP = np.nan
			number_NISysABP = np.nan
		else:
			min_NISysABP= min(NISysABP)
			max_NISysABP= max(NISysABP)
			median_NISysABP =statistics.median(NISysABP)
			first_NISysABP = NISysABP[0]
			last_NISysABP = NISysABP[-1]
			number_NISysABP = len(NISysABP)

		if(len(Albumin) == 0):
			min_Albumin = np.nan
			max_Albumin= np.nan
			median_Albumin= np.nan
			first_Albumin= np.nan
			last_Albumin = np.nan
			number_Albumin = np.nan
		else:
			min_Albumin= min(Albumin)
			max_Albumin= max(Albumin)
			median_Albumin =statistics.median(Albumin)
			first_Albumin = Albumin[0]
			last_Albumin = Albumin[-1]
			number_Albumin = len(Albumin)

		if(len(ALP) == 0):
			min_ALP = np.nan
			max_ALP= np.nan
			median_ALP= np.nan
			first_ALP= np.nan
			last_ALP = np.nan
			number_ALP = np.nan
		else:
			min_ALP= min(ALP)
			max_ALP= max(ALP)
			median_ALP =statistics.median(ALP)
			first_ALP = ALP[0]
			last_ALP = ALP[-1]
			number_ALP = len(ALP)

		if(len(ALT) == 0):
			min_ALT = np.nan
			max_ALT= np.nan
			median_ALT= np.nan
			first_ALT= np.nan
			last_ALT = np.nan
			number_ALT = np.nan
		else:
			min_ALT= min(ALT)
			max_ALT= max(ALT)
			median_ALT =statistics.median(ALT)
			first_ALT = ALT[0]
			last_ALT = ALT[-1]
			number_ALT = len(ALT)

		if(len(AST) == 0):
			min_AST = np.nan
			max_AST= np.nan
			median_AST= np.nan
			first_AST= np.nan
			last_AST = np.nan
			number_AST = np.nan
		else:
			min_AST= min(AST)
			max_AST= max(AST)
			median_AST =statistics.median(AST)
			first_AST = AST[0]
			last_AST = AST[-1]
			number_AST = len(AST)

		if(len(Bilirubin) == 0):
			min_Bilirubin = np.nan
			max_Bilirubin= np.nan
			median_Bilirubin= np.nan
			first_Bilirubin= np.nan
			last_Bilirubin = np.nan
			number_Bilirubin = np.nan
		else:
			min_Bilirubin= min(Bilirubin)
			max_Bilirubin= max(Bilirubin)
			median_Bilirubin =statistics.median(Bilirubin)
			first_Bilirubin = Bilirubin[0]
			last_Bilirubin = Bilirubin[-1]
			number_Bilirubin = len(Bilirubin)

		if(len(BUN) == 0):
			min_BUN = np.nan
			max_BUN= np.nan
			median_BUN= np.nan
			first_BUN= np.nan
			last_BUN = np.nan
			number_BUN = np.nan
		else:
			min_BUN= min(BUN)
			max_BUN= max(BUN)
			median_BUN =statistics.median(BUN)
			first_BUN = BUN[0]
			last_BUN = BUN[-1]
			number_BUN = len(BUN)

		if(len(Cholesterol) == 0):
			min_Cholesterol = np.nan
			max_Cholesterol= np.nan
			median_Cholesterol= np.nan
			first_Cholesterol= np.nan
			last_Cholesterol = np.nan
			number_Cholesterol = np.nan
		else:
			min_Cholesterol= min(Cholesterol)
			max_Cholesterol= max(Cholesterol)
			median_Cholesterol =statistics.median(Cholesterol)
			first_Cholesterol = Cholesterol[0]
			last_Cholesterol = Cholesterol[-1]
			number_Cholesterol = len(Cholesterol)

		if(len(Creatinine) == 0):
			min_Creatinine = np.nan
			max_Creatinine= np.nan
			median_Creatinine= np.nan
			first_Creatinine= np.nan
			last_Creatinine = np.nan
			number_Creatinine = np.nan
		else:
			min_Creatinine= min(Creatinine)
			max_Creatinine= max(Creatinine)
			median_Creatinine =statistics.median(Creatinine)
			first_Creatinine = Creatinine[0]
			last_Creatinine = Creatinine[-1]
			number_Creatinine = len(Creatinine)

		if(len(FiO2) == 0):
			min_FiO2 = np.nan
			max_FiO2= np.nan
			median_FiO2= np.nan
			first_FiO2= np.nan
			last_FiO2 = np.nan
			number_FiO2 = np.nan
		else:
			min_FiO2= min(FiO2)
			max_FiO2= max(FiO2)
			median_FiO2 =statistics.median(FiO2)
			first_FiO2 = FiO2[0]
			last_FiO2 = FiO2[-1]
			number_FiO2 = len(FiO2)

		if(len(GCS) == 0):
			min_GCS = np.nan
			max_GCS= np.nan
			median_GCS= np.nan
			first_GCS= np.nan
			last_GCS = np.nan
			number_GCS = np.nan
		else:
			min_GCS= min(GCS)
			max_GCS= max(GCS)
			median_GCS =statistics.median(GCS)
			first_GCS = GCS[0]
			last_GCS = GCS[-1]
			number_GCS = len(GCS)

		if(len(Glucose) == 0):
			min_Glucose = np.nan
			max_Glucose= np.nan
			median_Glucose= np.nan
			first_Glucose= np.nan
			last_Glucose = np.nan
			number_Glucose = np.nan
		else:
			min_Glucose= min(Glucose)
			max_Glucose= max(Glucose)
			median_Glucose =statistics.median(Glucose)
			first_Glucose = Glucose[0]
			last_Glucose = Glucose[-1]
			number_Glucose = len(Glucose)

		if(len(HCO3) == 0):
			min_HCO3 = np.nan
			max_HCO3= np.nan
			median_HCO3= np.nan
			first_HCO3= np.nan
			last_HCO3 = np.nan
			number_HCO3 = np.nan
		else:
			min_HCO3= min(HCO3)
			max_HCO3= max(HCO3)
			median_HCO3 =statistics.median(HCO3)
			first_HCO3 = HCO3[0]
			last_HCO3 = HCO3[-1]
			number_HCO3 = len(HCO3)

		if(len(HCT) == 0):
			min_HCT = np.nan
			max_HCT= np.nan
			median_HCT= np.nan
			first_HCT= np.nan
			last_HCT = np.nan
			number_HCT = np.nan
		else:
			min_HCT= min(HCT)
			max_HCT= max(HCT)
			median_HCT =statistics.median(HCT)
			first_HCT = HCT[0]
			last_HCT = HCT[-1]
			number_HCT = len(HCT)

		if(len(HR) == 0):
			min_HR = np.nan
			max_HR= np.nan
			median_HR= np.nan
			first_HR= np.nan
			last_HR = np.nan
			number_HR = np.nan
		else:
			min_HR= min(HR)
			max_HR= max(HR)
			median_HR =statistics.median(HR)
			first_HR = HR[0]
			last_HR = HR[-1]
			number_HR = len(HR)

		if(len(K) == 0):
			min_K = np.nan
			max_K= np.nan
			median_K= np.nan
			first_K= np.nan
			last_K = np.nan
			number_K = np.nan
		else:
			min_K= min(K)
			max_K= max(K)
			median_K =statistics.median(K)
			first_K = K[0]
			last_K = K[-1]
			number_K = len(K)

		if(len(Lactate) == 0):
			min_Lactate = np.nan
			max_Lactate= np.nan
			median_Lactate= np.nan
			first_Lactate= np.nan
			last_Lactate = np.nan
			number_Lactate = np.nan
		else:
			min_Lactate= min(Lactate)
			max_Lactate= max(Lactate)
			median_Lactate =statistics.median(Lactate)
			first_Lactate = Lactate[0]
			last_Lactate = Lactate[-1]
			number_Lactate = len(Lactate)

		if(len(Mg) == 0):
			min_Mg = np.nan
			max_Mg= np.nan
			median_Mg= np.nan
			first_Mg= np.nan
			last_Mg = np.nan
			number_Mg = np.nan
		else:
			min_Mg= min(Mg)
			max_Mg= max(Mg)
			median_Mg =statistics.median(Mg)
			first_Mg = Mg[0]
			last_Mg = Mg[-1]
			number_Mg = len(Mg)

		if(len(MechVent) == 0):
			min_MechVent = np.nan
			max_MechVent= np.nan
			median_MechVent= np.nan
			first_MechVent= np.nan
			last_MechVent = np.nan
			number_MechVent = np.nan
		else:
			min_MechVent= min(MechVent)
			max_MechVent= max(MechVent)
			median_MechVent =statistics.median(MechVent)
			first_MechVent = MechVent[0]
			last_MechVent = MechVent[-1]
			number_MechVent = len(MechVent)

		if(len(Na) == 0):
			min_Na = np.nan
			max_Na= np.nan
			median_Na= np.nan
			first_Na= np.nan
			last_Na = np.nan
			number_Na = np.nan
		else:
			min_Na= min(Na)
			max_Na= max(Na)
			median_Na =statistics.median(Na)
			first_Na = Na[0]
			last_Na = Na[-1]
			number_Na = len(Na)

		if(len(PaCO2) == 0):
			min_PaCO2 = np.nan
			max_PaCO2= np.nan
			median_PaCO2= np.nan
			first_PaCO2= np.nan
			last_PaCO2 = np.nan
			number_PaCO2 = np.nan
		else:
			min_PaCO2= min(PaCO2)
			max_PaCO2= max(PaCO2)
			median_PaCO2 =statistics.median(PaCO2)
			first_PaCO2 = PaCO2[0]
			last_PaCO2 = PaCO2[-1]
			number_PaCO2 = len(PaCO2)

		if(len(PaO2) == 0):
			min_PaO2 = np.nan
			max_PaO2= np.nan
			median_PaO2= np.nan
			first_PaO2= np.nan
			last_PaO2 = np.nan
			number_PaO2 = np.nan
		else:
			min_PaO2= min(PaO2)
			max_PaO2= max(PaO2)
			median_PaO2 =statistics.median(PaO2)
			first_PaO2 = PaO2[0]
			last_PaO2 = PaO2[-1]
			number_PaO2 = len(PaO2)

		if(len(pH) == 0):
			min_pH = np.nan
			max_pH= np.nan
			median_pH= np.nan
			first_pH= np.nan
			last_pH = np.nan
			number_pH = np.nan
		else:
			min_pH= min(pH)
			max_pH= max(pH)
			median_pH =statistics.median(pH)
			first_pH = pH[0]
			last_pH = pH[-1]
			number_pH = len(pH)

		if(len(Platelets) == 0):
			min_Platelets = np.nan
			max_Platelets= np.nan
			median_Platelets= np.nan
			first_Platelets= np.nan
			last_Platelets = np.nan
			number_Platelets = np.nan
		else:
			min_Platelets= min(Platelets)
			max_Platelets= max(Platelets)
			median_Platelets =statistics.median(Platelets)
			first_Platelets = Platelets[0]
			last_Platelets = Platelets[-1]
			number_Platelets = len(Platelets)


		if(len(RespRate) == 0):
			min_RespRate = np.nan
			max_RespRate= np.nan
			median_RespRate= np.nan
			first_RespRate= np.nan
			last_RespRate = np.nan
			number_RespRate = np.nan
		else:
			min_RespRate= min(RespRate)
			max_RespRate= max(RespRate)
			median_RespRate =statistics.median(RespRate)
			first_RespRate = RespRate[0]
			last_RespRate = RespRate[-1]
			number_RespRate = len(RespRate)

		if(len(SaO2) == 0):
			min_SaO2 = np.nan
			max_SaO2= np.nan
			median_SaO2= np.nan
			first_SaO2= np.nan
			last_SaO2 = np.nan
			number_SaO2 = np.nan
		else:
			min_SaO2= min(SaO2)
			max_SaO2= max(SaO2)
			median_SaO2 =statistics.median(SaO2)
			first_SaO2 = SaO2[0]
			last_SaO2 = SaO2[-1]
			number_SaO2 = len(SaO2)

		if(len(Temp) == 0):
			min_Temp = np.nan
			max_Temp= np.nan
			median_Temp= np.nan
			first_Temp= np.nan
			last_Temp = np.nan
			number_Temp = np.nan
		else:
			min_Temp= min(Temp)
			max_Temp= max(Temp)
			median_Temp =statistics.median(Temp)
			first_Temp = Temp[0]
			last_Temp = Temp[-1]
			number_Temp = len(Temp)

		if(len(TroponinI) == 0):
			min_TroponinI = np.nan
			max_TroponinI= np.nan
			median_TroponinI= np.nan
			first_TroponinI= np.nan
			last_TroponinI = np.nan
			number_TroponinI = np.nan
		else:
			min_TroponinI= min(TroponinI)
			max_TroponinI= max(TroponinI)
			median_TroponinI =statistics.median(TroponinI)
			first_TroponinI = TroponinI[0]
			last_TroponinI = TroponinI[-1]
			number_TroponinI = len(TroponinI)

		if(len(TroponinT) == 0):
			min_TroponinT = np.nan
			max_TroponinT= np.nan
			median_TroponinT= np.nan
			first_TroponinT= np.nan
			last_TroponinT = np.nan
			number_TroponinT = np.nan
		else:
			min_TroponinT= min(TroponinT)
			max_TroponinT= max(TroponinT)
			median_TroponinT =statistics.median(TroponinT)
			first_TroponinT = TroponinT[0]
			last_TroponinT = TroponinT[-1]
			number_TroponinT = len(TroponinT)

		if(len(Urine) == 0):
			min_Urine = np.nan
			max_Urine= np.nan
			median_Urine= np.nan
			first_Urine= np.nan
			last_Urine = np.nan
			number_Urine = np.nan
		else:
			min_Urine= min(Urine)
			max_Urine= max(Urine)
			median_Urine =statistics.median(Urine)
			first_Urine = Urine[0]
			last_Urine = Urine[-1]
			number_Urine = len(Urine)

		if(len(WBC) == 0):
			min_WBC = np.nan
			max_WBC= np.nan
			median_WBC= np.nan
			first_WBC= np.nan
			last_WBC = np.nan
			number_WBC = np.nan
		else:
			min_WBC= min(WBC)
			max_WBC= max(WBC)
			median_WBC =statistics.median(WBC)
			first_WBC = WBC[0]
			last_WBC = WBC[-1]
			number_WBC = len(WBC)

		c.append(np.array([Age,Gender,Height,min_DiasABP,max_DiasABP,median_DiasABP,first_DiasABP,last_DiasABP,number_DiasABP,min_MAP,max_MAP,median_MAP,first_MAP,last_MAP,number_MAP,min_SysABP,max_SysABP,median_SysABP,first_SysABP,last_SysABP,number_SysABP,min_NIDiasABP,max_NIDiasABP,median_NIDiasABP,first_NIDiasABP,last_NIDiasABP,number_NIDiasABP,min_NIMAP,max_NIMAP,median_NIMAP,first_NIMAP,last_NIMAP,number_NIMAP,min_NISysABP,max_NISysABP,median_NISysABP,first_NISysABP,last_NISysABP,number_NISysABP,min_Albumin,max_Albumin,median_Albumin,first_Albumin,last_Albumin,number_Albumin,min_ALP,max_ALP,median_ALP,first_ALP,last_ALP,number_ALP,min_ALT,max_ALT,median_ALT,first_ALT,last_ALT,number_ALT,min_AST,max_AST,median_AST,first_AST,last_AST,number_AST,min_Bilirubin,max_Bilirubin,median_Bilirubin,first_Bilirubin,last_Bilirubin,number_Bilirubin,min_BUN,max_BUN,median_BUN,first_BUN,last_BUN,number_BUN,min_Cholesterol,max_Cholesterol,median_Cholesterol,first_Cholesterol,last_Cholesterol,number_Cholesterol,min_Creatinine,max_Creatinine,median_Creatinine,first_Creatinine,last_Creatinine,number_Creatinine,min_FiO2,max_FiO2,median_FiO2,first_FiO2,last_FiO2,number_FiO2,min_GCS,max_GCS,median_GCS,first_GCS,last_GCS,number_GCS,min_Glucose,max_Glucose,median_Glucose,first_Glucose,last_Glucose,number_Glucose,min_HCO3,max_HCO3,median_HCO3,first_HCO3,last_HCO3,number_HCO3,min_HCT,max_HCT,median_HCT,first_HCT,last_HCT,number_HCT,min_HR,max_HR,median_HR,first_HR,last_HR,number_HR,min_K,max_K,median_K,first_K,last_K,number_K,min_Lactate,max_Lactate,median_Lactate,first_Lactate,last_Lactate,number_Lactate,min_Mg,max_Mg,median_Mg,first_Mg,last_Mg,number_Mg,min_MechVent,max_MechVent,median_MechVent,first_MechVent,last_MechVent,number_MechVent,min_Na,max_Na,median_Na,first_Na,last_Na,number_Na,min_PaCO2,max_PaCO2,median_PaCO2,first_PaCO2,last_PaCO2,number_PaCO2,min_PaO2,max_PaO2,median_PaO2,first_PaO2,last_PaO2,number_PaO2,min_pH,max_pH,median_pH,first_pH,last_pH,number_pH,min_Platelets,max_Platelets,median_Platelets,first_Platelets,last_Platelets,number_Platelets,min_RespRate,max_RespRate,median_RespRate,first_RespRate,last_RespRate,number_RespRate,min_SaO2,max_SaO2,median_SaO2,first_SaO2,last_SaO2,number_SaO2,min_Temp,max_Temp,median_Temp,first_Temp,last_Temp,number_Temp,min_TroponinI,max_TroponinI,median_TroponinI,first_TroponinI,last_TroponinI,number_TroponinI,min_TroponinT,max_TroponinT,median_TroponinT,first_TroponinT,last_TroponinT,number_TroponinT,min_Urine,max_Urine,median_Urine,first_Urine,last_Urine,number_Urine,min_WBC,max_WBC,median_WBC,first_WBC,last_WBC,number_WBC]))
		#print(c)

	cc = np.array(c)
	print("111111")

	#print(cc)
	
	imp1 = Imputer(missing_values='NaN', strategy='mean', axis=0)

	dd = imp1.fit_transform(cc)
"""

	#result = clf.predict(dd)
	#np.set_printoptions(threshold=np.inf)
	#print (result[3999])
	#print(len(fa))
	#for i in range(0,3999):
	#	if(fa[i] != result[i]):
	#		print(i)








