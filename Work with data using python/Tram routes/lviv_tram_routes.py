#read file by lines
def read_file():
    with open('all_stations.txt','r', encoding="utf-8") as file:
        lines=file.readlines()
        #print(lines)
        return lines

#write in file is used within methods
def to_file(data, file_name):
    with open(file_name,'a') as file:
        file.writelines(str(data))

#sort stops by alphabet
def sorted_stops(lines):
    sorted_stops = sorted(lines)
    #print(sorted_stops)
    for s in sorted_stops:
        to_file(s, 'sorted_stops.txt')
        
###################### end of working with files of stations ###############
###################### beginning of working with routes ####################

#create set of stations for each tram
def set_of_stations(trams):
    for num,route in trams.items():
        route[2]=set(route[0] + route[1]) #make 1 list of stations in 2 directions, than make set of unique stations
        #print(num, route[0], route[1], route[2], sep='\n')
    return trams

#stop which is in 2 routes
def common_stop(tram_num_first,tram_num_second,trams):
    common_stop_set = trams[tram_num_first][2] & trams[tram_num_second][2]
    res='' #string of all common stops
    for i in common_stop_set:
        res+=str(i) 
    #print('Common stop of tram number',tram_num_first,'and',tram_num_second,'is',res)
    return res

def direction(from_stop,to_stop,tram_num,trams):
    if trams[tram_num][0].index(from_stop) < trams[tram_num][0].index(to_stop) :
        direction = trams[tram_num][0]
    else: direction = trams[tram_num][1]
    #see whole direction
    #res='' #string of all stops
    #for i in direction:
    #    res+=str(i+'|') 
    #print('Direction of tram number',tram_num,':', res)
    #return direction
    res=[]
    for i in direction:
        res.append(i)
    #print('direction "'+res[0],'-',res[-1]+'"')
    return 'direction "'+res[0]+'-'+res[-1]+'"'

def change_tram(from_stop,to_stop,trams):
    res_num_1=0
    res_num_2=0
    c_stop=''
    for num_1,route_1 in trams.items():
        if (from_stop in route_1[2]):
            res_num_1=num_1
        else:
            continue
        for num_2,route_2 in trams.items():
            if (to_stop in route_2[2]):
                c_stop=common_stop(num_1,num_2,trams)
                if c_stop!='':
                    res_num_2=num_2
                    break
            else:
                continue
    dir_1=direction(from_stop,c_stop,res_num_1,trams)
    dir_2=direction(c_stop,to_stop,res_num_2,trams)
    #print('You may sit on tram number',res_num_1,'in',dir_1,', get out of tram on the stop "'+c_stop+'", than sit on tram number',res_num_2,'in',dir_2,'and get out of tram on stop "'+to_stop+'"')
    return 'You may sit on tram number '+str(res_num_1)+' in '+dir_1+', get out of tram on the stop "'+c_stop+'", than sit on tram number '+str(res_num_2),' in '+dir_2+' and get out of tram on stop "'+to_stop+'"'

def how_can_i_get_from_to(from_stop,to_stop,trams):
    res_num=0
    for num,route in trams.items():
        if (from_stop in route[2]) and (to_stop in route[2]):
            #print('You can get from',from_stop,'to',to_stop,'on tram number',num,'in', direction(from_stop,to_stop,num,trams))
            return 'You can get from '+from_stop+' to '+to_stop+' on tram number '+str(num)+' in '+str(direction(from_stop,to_stop,num,trams))
            res_num=num
            break
            #return res_num
        else:
            continue
    if res_num==0:
        #print("You can't get from station",from_stop,'to station',to_stop,'without changing the tram on your way.')
        return "You can't get from station "+from_stop+' to station '+to_stop+' without changing the tram on your way.\n'+str(change_tram(from_stop,to_stop,trams))
        

def get_tram_num(stop,trams):
    res_num=''
    for num,route in trams.items():
        if (stop in route[2]):
            res_num+=' '+str(num)
    #print('You can get to stop "'+stop+'" by tram number'+res_num)
    return 'You can get to stop "'+stop+'" by tram number'+res_num
    if res_num=='':
        #print("You can't get to this station by tram.")
        return "You can't get to this station by tram."
        
#program example
def main():
    #lines = read_file()
    #res=sorted_stops(lines)
    
    #set of trams, two directions of each tram (because of some different stops on the directions)
    trams = {
        1:[['Залізничний вокзал','Приміський вокзал','пл. Кропивницького','вул. Русових','Львівська політехніка','Головна Пошта','вул. Дорошенка','пл. Ринок','вул. Руська','пл. Митна','Війсковий госпіталь','вул. Кармалюка','вул. Мечникова','вул. Котика','вул. Пасічна'],
            ['вул. Пасічна','вул. Котика','вул. Мечникова','Медичний університет','Війсковий госпіталь','пл. Митна','вул. Руська','вул. Дорошенка','Головна Пошта','Львівська політехніка','вул. Карпінського','пл. Кропивницького','Приміський вокзал','Залізничний вокзал'],
           {}],
        2:[['вул. Коновальця (Музей Труша)','вул. Гординських','вул. Залізняка','вул. Мельника','Фабрика Левинського','вул. Київська','Львівська політехніка','Головна Пошта','вул. Дорошенка','пл. Ринок','вул. Руська','пл. Митна','Війсковий госпіталь','вул. Кармалюка','вул. Мечникова','вул. Богдана Котика','вул. Пасічна'],
            ['вул. Пасічна','вул. Котика','вул. Мечникова','Медичний університет','Війсковий госпіталь','пл. Митна','вул. Руська','вул. Дорошенка','Головна Пошта','Львівська політехніка','вул. Київська','Фабрика Левинського','вул. Мельника','вул. Залізняка','вул. Гординських','вул. Коновальця (Музей Труша)'],
           {}],
        3:[['пл. Соборна','вул. Шухевича','вул. Саксаганського','пл. Франка','Парк культури','вул. Сахарова','вул. Горбачевського','вул. Шумського','вул. Аркаса','вул. Бойчука (Кіноцентр)','Аквапарк'],
            ['Аквапарк','вул. Бойчука (Кіноцентр)','вул. Аркаса','вул. Шумського','вул. Горбачевського','вул. Сахарова','Парк культури','пл. Франка','вул. Саксаганського','пл. Соборна'],
           {}],
        4:[['Залізничний вокзал','Приміський вокзал','пл. Кропивницького','вул. Русових','вул. Київська','вул. Сахарова','Парк культури','пл. Франка','Стрийський парк','Академія Мистецтв','Стадіон «Україна»','вул. Угорська','ТРЦ «Шувар»','Дитяча поліклініка','Центр Довженка','Поліклініка №4','вул. Коломийська','вул. Драгана','вул. Вернадського'],
           ['вул. Вернадського','вул. Драгана','вул. Коломийська','Поліклініка №4','Центр Довженка','Дитяча поліклініка','ТРЦ «Шувар»','вул. Угорська','Стадіон «Україна»','Академія Мистецтв','Стрийський парк','Стрийський ринок','Парк культури','вул. Сахарова','вул. Київська','вул. Русових','пл. Кропивницького','Приміський вокзал','Залізничний вокзал'],
           {}],
        6:[['ТРЦ «Скриня»','Привокзальний ринок','пл. Кропивницького','Церква святої Анни','вул. Наливайка','пл. Старий Ринок','вул. Під Дубом','Палац культури ім. Гната Хоткевича','станція Підзамче','вул. Остряниці','вул. Промислова','Трамвайне депо №2','Фабрика «Світанок»','вул. Липинського','вул. Миколайчука'],
           ['вул. Миколайчука','Фабрика «Світанок»','Трамвайне депо №2','вул. Промислова','вул. Остряниці','станція Підзамче','вул. Гайдамацька','Палац культури ім. Гната Хоткевича','пл. Старий Ринок','вул. Театральна','ТЦ «Магнус»','Церква святої Анни','Театр ім. Лесі Українки','пл. Кропивницького','Привокзальний ринок','вул. Кульпарківська'],
           {}],
        7:[['Погулянка','вул. Левицького','Личаківський цвинтар','вул. Мечникова','Медичний університет','Війсковий госпіталь','пл. Митна','вул. Театральна','ТЦ «Магнус»','Церква святої Анни','вул. Турянського','Янівський цвинтар','вул. Татарбунарська'],
           ['вул. Татарбунарська','Крупзавод','Янівський цвинтар','вул. Єрошенка','вул. Турянського','Театр ім. Лесі Українки','Церква святої Анни','вул. Наливайка','Театр ляльок','вул. Підвальна','пл. Митна','Війсковий госпіталь','вул. Кармалюка','вул. Мечникова','Личаківський цвинтар','Обласна інфекційна лікарня','вул. Левицького','Погулянка'],
           {}],
        8:[['пл. Соборна','вул. Шухевича','вул. Саксаганського','пл. Франка','Стрийський парк','Академія Мистецтв','Стадіон «Україна»','вул. Угорська','ТРЦ «Шувар»','Дитяча поліклініка','Центр Довженка','Поліклініка №4','вул. Коломийська','вул. Драгана','вул. Вернадського'],
           ['вул. Вернадського','вул. Драгана','вул. Коломийська','Поліклініка №4','Центр Довженка','Дитяча поліклініка','ТРЦ «Шувар»','вул. Угорська','Стадіон «Україна»','Академія Мистецтв','Стрийський парк','Стрийський ринок','вул. Саксаганського','пл. Соборна'],
           {}],
        9:[['Залізничний вокзал','Приміський вокзал','пл. Кропивницького','вул. Русових','вул. Київська','вул. Сахарова','Парк культури','пл. Франка','вул. Саксаганського','вул. Шухевича','вул. Підвальна','пл. Старий Ринок','вул. Під Дубом','Палац культури ім. Гната Хоткевича','вул. Гайдамацька','вул. Городницька','вул. Торфяна'],
           ['вул. Торфяна','вул. Городницька','вул. Гайдамацька','Палац культури ім. Гната Хоткевича','пл. Старий Ринок','Театр ляльок','вул. Підвальна','вул. Шухевича','вул. Саксаганського','пл. Франка','Парк культури','вул. Сахарова','вул. Київська','вул. Русових','пл. Кропивницького','Приміський вокзал','Залізничний вокзал'],
           {}]
        }
    
    set_of_st = set_of_stations(trams) #fill set of station for each tram

    stop_1='Залізничний вокзал'
    t_n_1=get_tram_num(stop_1,set_of_st)
    to_file('Which tram has a stop Залізничний вокзал?\n','questions and answers.txt')
    to_file(t_n_1,'questions and answers.txt')
    
    stop_2='Брюховичі'
    t_n_2=get_tram_num(stop_2,set_of_st)
    to_file('\n\nWhich tram has a stop Брюховичі?\n','questions and answers.txt')
    to_file(t_n_2,'questions and answers.txt')
    
    cs=common_stop(9,2,set_of_st)
    to_file('What is common stop of tram number 9 and 2?\n','questions and answers.txt')
    to_file(cs,'questions and answers.txt')
    
    from_stop_1 = 'вул. Київська'
    to_stop_1 = 'Парк культури'
    d=direction(from_stop_1,to_stop_1,4,set_of_st)
    to_file('\n\nWhich direction of tram srould I choose to get from вул. Київська to Парк культури?\n','questions and answers.txt')
    to_file(d,'questions and answers.txt')

    from_stop_2 = 'вул. Київська'
    to_stop_2 = 'пл. Митна'
    h=how_can_i_get_from_to(from_stop_2,to_stop_2,set_of_st)
    to_file('\n\nHow can I get from вул. Київська to пл. Митна?\n','questions and answers.txt')
    to_file(h,'questions and answers.txt')

    #коновальця(2) - стрийський парк(4), через київську
    from_stop_3='вул. Коновальця (Музей Труша)'
    to_stop_3='Стрийський парк'
    h1=how_can_i_get_from_to(from_stop_3,to_stop_3,set_of_st)
    to_file('\n\nHow can I get from вул. Коновальця (Музей Труша) to Стрийський парк?\n','questions and answers.txt')
    to_file(h1,'questions and answers.txt')
    
    print('Ready.')
    
#run the program example
main()
