student = {
    "rahul" : 90, "karthik" : 97, "chotu" : 91
    }
print(type(student))

print( student["karthik"] )

print( student.keys() )

print( student.values() )

#Nested Dictionary

bpie = {
    "cst" : {
        "id" : "Bpiecst01", "no. stud" : 60, "lab" : 1
        },
    "civil" : {
        "id" : "Bpiecivil04", "no. stud" : 180, "lab" : 3
        },   
    "etce" : {
        "id" : "Bpieetce07", "no. stud" : 60, "lab" : 2
        }
    }

print ( bpie.keys())
print ( bpie.values())

print( bpie["etce"]["no. stud"] )

print( bpie["civil"]["lab"] )
