import sys
import os
import io
from ipapy import UNICODE_TO_IPA
from ipapy import is_valid_ipa
from ipapy.ipachar import IPAConsonant
from ipapy.ipachar import IPAVowel
from ipapy.ipastring import IPAString
import codecs
import re
import operator
import json
# assume that the reference text's index name is the same as their file names 
# in static file


# generate a JSON FILE: list of file names, and list of text string of display 


reference_path = "./static/mp3s/reference.txt"
simlist_path = "./static/js/stimlist.js"

stimuli_dict={} #key: filepaths; value: the sounds_string
with codecs.open(reference_path,'r','utf-8') as f:
	for line in f.readlines(): 
		index_string, ipa =line.split("\t")
		ipa = re.sub(r"/",'',ipa).strip("\n").rstrip()
		s_ipa = IPAString(unicode_string=ipa) # try to put this into dictionary? 
		stimuli_dict["/static/mp3s/"+index_string+".wav"] =  ipa #the file paths are in the forms of 0.txt
		#stimuli_dict["sound_string"].append(ipa)


with codecs.open(simlist_path, 'w+','utf-8') as f:
	f.write("var stimuli=")
	json.dump(stimuli_dict, f, ensure_ascii=False)



