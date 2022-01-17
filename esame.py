def funzione1(s):
	sCase = s.lower()
	index = sCase.find("allora")
	if(index < 0): return(0)
	sRes = ""
	for i in range(index,len(s)):
		if (s[i] == 'o'):
			sRes += "0"
		elif(s[i] == 'e'):
			sRes += "1"
		elif(s[i] == 'i'):
			sRes += "2"
		elif(s[i] == 'u'):
			sRes += "3"	
		elif(s[i] == 'y'):
			sRes += "4"
		elif(s[i] == 'm'):
			sRes += "5"
		elif(s[i] == 'n'):
			sRes += "6"
		elif(s[i] == 'b'):
			sRes += "7"
		elif(s[i] == 'v'):
			sRes += "8"
		elif(s[i] == 'c'):
			sRes += "9"
	return(int(sRes))

def funzione2(lista_stud):
	res = set()
	for i in range(len(lista_stud)):
		if(lista_stud[i][1] >= 9 and lista_stud[i][2] >= 9) or ((lista_stud[i][3] <= 3) or (lista_stud[i][4] <= 5)):
			res.add(int(lista_stud[i][0]))

	l = list(res)
	l.sort()
	return l



def funzione3(d1,d2):
	res = dict()
	for k1 in d1:
		for k2 in d2:
			if k1 == k2:
				res[k1] = set(d1[k1].symmetric_difference(d2[k2]))
		if (k1 not in res):
			res[k1] = set(d1[k1])
	
	return res

def funzione4(team,task):
	res = set()
	
	#Se team vuoto oppure team e task vuoti, ritorno set()	
	if len(team) == 0: return set()
	
	#se task vuoto, restituisco i team meno costosi	
	if len(task) == 0:
		bestPrice = team[0]["costo"]
		for x in team:
			if (x["costo"] < bestPrice):
				bestPrice = x["costo"]
		for x in team:
			if (x["costo"] == bestPrice):
				res.add(x["id"])
		return res
	
	#altrimenti, restituisco i team meno costosi in grado di risolvere i task
	bestPrice = 0
	tmp = set()
	for x in team: 	
		if(x["costo"] > bestPrice):
			bestPrice = x["costo"]
	for x in team:
		lTask = 0	
		for s in task:
			if(s["skills"].issubset(x["skills"])):
				lTask+=1
		
		if(lTask == len(task)):
			tmp.add(x["id"])
			if(x["costo"] < bestPrice):
				bestPrice = x["costo"] 	
	for x in team:
		if (x["costo"] == bestPrice and x["id"] in tmp):
			res.add(x["id"])		
	return res			
	



if __name__ == '__main__':
	print(funzione1("allora cavallino"))
	print(funzione1("allora e' stato un caso"))
	print(funzione1("allora? HxH"))
	print(funzione2([[1,9,9,10,5],[1,8,8,4,9]]))
	print(funzione2([[4,9,9,20,15],[5,8,8,4,9]]))
	print(funzione2([]))
	print(funzione2([[4,8,7,1,15],[3,7,8,6,7],[2,8,8,4,2]]))
		
	d1,d2 = {1:set([1,11,111]),2:set([3,11])},{1:set([11,111,1111])}
	print(funzione3(d1,d2))
	print(funzione3({},{}))
	print(funzione4([],[{"id":1,"skills":set([1,2,3])},{"id":1,"skills":set([3])}]))
	print(funzione4([{"id":1,"costo":10, "skills":set([1,2])},{"id":2,"costo":20, "skills":set([1,2,3])},{"id":3,"costo":20, "skills":set([1,2,3,4])}],[{"id":1,"skills":set([1,2,3])},{"id":1,"skills":set([3])}]))
	print(funzione4([{"id":4,"costo":20, "skills":set([4,2])},{"id":2,"costo":10, "skills":set([2,3])}],[]))
	print(funzione4([],[]))




