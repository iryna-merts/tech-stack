#read file by lines
def read_file():
    with open('weather_data.txt','r') as file:
        lines=file.readlines()
        return lines
        #print(lines)

#write in file is used within methods
def to_file(data):
    with open('results.txt','a') as file:
        file.writelines(str(data))

#create list of dicts with all data
def file_to_list(lines):
    list_of_dicts=[]
    for l in lines:
        data=l.split('|')
        all_weather = dict(zip(['city','date','time','temperature','pressure','wind'],data)) #assign keys for every line's values 
        list_of_dicts.append(all_weather)
        #print(all_weather)
        #to_file('City:'+all_weather['city']+', date:'+all_weather['date']+', time:'+all_weather['time']+', temperature:'+all_weather['temperature']+', pressure:'+all_weather['pressure']+', wind:'+all_weather['wind']+'\n')
    return list_of_dicts

#show weather of selectes city
def weather_of_1_city(all_weather, city):
    city_data=[] #list of dicts of all selected data lines
    for i in all_weather:
        if i['city']==city:
            city_data.append(i)

    #print('Weather in', city,':\n')
    to_file('Weather in '+city+':\n\n')
    for i in city_data:
        #print(i)
        to_file('Date:'+i['date']+', time:'+i['time']+', temperature:'+i['temperature']+', pressure:'+i['pressure']+', wind:'+i['wind']+'\n')
    return city_data

def max_temp_of_city(all_weather,city):
    list_of_temp = []
    for i in all_weather:
        list_of_temp.append(int(i['temperature']))
        
    #print(list_of_temp)
    res=max(list_of_temp)
    dt='' #date
    for i in all_weather:
        if int(i['temperature'])==int(res):
            dt+=str(i['date']+' ')
    #print(res)
    to_file('Maximum temperature in '+city+' is '+str(res)+'*C in '+dt+'\n\n')
    return res

#show weather of selectes city in ceelcted date
def weather_in_date(all_weather, date):
    day_data=[] #list of dicts of all selected data lines
    for i in all_weather:
        if i['date']==date:
            day_data.append(i)

    to_file('Weather in '+date+':\n\n')
    for i in day_data:
        #print(i)
        to_file('City:'+i['city']+' time:'+i['time']+', temperature:'+i['temperature']+', pressure:'+i['pressure']+', wind:'+i['wind']+'\n')
    return day_data

def max_temp_of_day(all_weather,date):
    list_of_temp = []
    for i in all_weather:
        list_of_temp.append(int(i['temperature']))
        
    #print(list_of_temp)
    res=max(list_of_temp)
    ct='' #city
    for i in all_weather:
        if int(i['temperature'])==int(res):
            ct+=str(i['city']+' ') 
    #print(res)
    to_file('Maximum temperature in '+date+' is '+str(res)+'*C in '+ct+'\n\n')
    return res

def most_common_wind_dir(all_weather,date):
    list_of_wind=[] #all wind types during that days
    for i in all_weather:
        list_of_wind.append(i['wind'])
    dict_of_w_occurance = dict((x,list_of_wind.count(x)) for x in set(list_of_wind))
    max_occurances = max(dict_of_w_occurance.values())
    for w,occr in dict_of_w_occurance.items(): #get key(wind) by value(occurance)
        if int(occr)==int(max_occurances):
            res=w
    #print(res)
    to_file('Most common wind direction is: '+res+'\n\n')
    return res

#program example
def main():
    lines = read_file()
    all_weather = file_to_list(lines)
    
    city='Lviv'
    date='01.10.20'

    max_temp_of_day(all_weather, date)
    most_common_wind_dir(all_weather,date)
    
    w_of_city = weather_of_1_city(all_weather, city)
    max_temp_of_city(w_of_city, city)

    w_of_day = weather_in_date(all_weather, date)
    max_temp_of_day(w_of_day, date)

    print('Ready. Open file results.txt')

#run the program example
main()




