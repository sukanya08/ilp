from os import system,sys
import os


if len(sys.argv) != 3:
    print("Please give database names as arguments. USAGE: python import_studentgroup_data.py ems ilp", file=sys.stderr)
    sys.exit()

basename = "sg"
#Before running this script
#change this to point to the ems database that is used for getting the data
fromdatabase = sys.argv[1]

#change this to ilp db to be populated with
todatabase = sys.argv[2]

inputdatafile = basename+"_getdata.sql"
loaddatafile = basename+"_loaddata.sql"

tables=[
    {
        'name': 'schools_studentgroup',
        'table_name': 'schools_studentgroup',
        'columns': 'id, name, section, group_type_id, institution_id, status_id',
        'query': "COPY(select id, name, section, lower(group_type), institution_id, 'AC' from schools_studentgroup where active=2 and institution_id in (select id from schools_institution where active=2)) TO '$PWD/load/schools_studentgroup.csv' NULL 'null' DELIMITER ',' quote '\\\"' csv;",
    }
]

#Create directory and files
def init():
    if not os.path.exists("load"):
    	os.makedirs("load")
    inputfile = open(inputdatafile,'wb',0)
    loadfile = open(loaddatafile,'wb',0)
    system("psql -U klp -d "+fromdatabase+" -f cleanems.sql")


#Create the getdata.sql and loaddata.sql files
# getdata.sql file has the "Copy to" commands for populating the various csv files
# loaddata.sql file has the "copy from" commands for loading the data into the db
def create_sqlfiles():
  #Loop through the tables
  for table in tables:
      #create the "copy to" file to get data from ems
      system('echo "'+table['query']+'\">>'+inputdatafile)

      #create the "copy from" file to load data into db
      filename = os.getcwd()+'/load/'+table['name']+'.csv'
      open(filename,'wb',0)
      os.chmod(filename,0o666)

      system('echo "COPY '+table['table_name']+"("+table['columns']+") from '"+filename+"' with csv NULL 'null';"+'\">>'+loaddatafile)

#Running the "copy to" commands to populate the csvs.
def getdata():
  system("psql -U klp -d "+fromdatabase+" -f "+inputdatafile)


#Running the "copy from" commands for loading the db.
def loaddata():
  system("psql -U klp -d "+todatabase+" -f "+loaddatafile)


#order in which function should be called.
init()
create_sqlfiles()
getdata()
loaddata()
