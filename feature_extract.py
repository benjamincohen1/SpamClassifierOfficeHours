import  os, re
import math, glob
import features
import inspect 


def main():

	 
	 arff = open("spam.arff", "w")
	
	 ben_functions = inspect.getmembers(features, inspect.isfunction)
	 feature_funcitons = []
	 feature_funcitons +=  list([f[1] for f in ben_functions])

	 RELATION_NAME = "spam"									 
	 arff.write("@RELATION " + RELATION_NAME + "\n")
	 for feature in feature_funcitons:
			arff.write("@ATTRIBUTE " +\
						str(feature.__name__) + " REAL\n")  #change this if we
														 	#have non-real number
															#values
		
		###PREDEFINED USER FEATURES#######
	 arff.write("@ATTRIBUTE SPAM {True, False}\n") 
	
	 arff.write("@DATA\n")
	
	 spam_directory = "is-spam"
	 not_spam = "not-spam"
	 os.chdir(spam_directory)
	 for email in glob.glob("*"):#ITERATE THROUGH ALL DATA HERE 
			 extract_features(open(email).read(), feature_funcitons, arff, True)
   
	 os.chdir('../'+not_spam)
	 for email in glob.glob("*"):#ITERATE THROUGH ALL DATA HERE 
			 extract_features(open(email).read(), feature_funcitons, arff, False)



def numwords(emailtext):
    splittext = emailtext.split(" ")
    return len(splittext)
 

    
def extract_features(data, feature_funcitons, arff, spam):
    values = []
    buff = ""

    for feature in feature_funcitons:
		value = feature(data)
		values.append(value)
    if spam:
		  buff += (",".join([str(x) for x in values]) + ', True' + "\n")
    else:
		  buff += (",".join([str(x) for x in values]) + ', False' + "\n")

    arff.write(buff)

  
if __name__ == "__main__":
	main()
