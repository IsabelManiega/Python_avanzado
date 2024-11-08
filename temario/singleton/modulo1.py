import singleton 

print("Antes de modificarlo: ",\
      singleton.shared_variable)
singleton.shared_variable +=\
       "(modificado por samplemodule1)"