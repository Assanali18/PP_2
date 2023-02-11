movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}]
# 
def good_mov(inp_mov):
    for x in movies:
        if x.get('name').lower() == inp_mov:
            print('Good film') if float(x.get('imdb')) > 5.5 else print ('So-so')
            return  True
    print('We dont have such movie in our list :(')


def list_of_mov():
    for x in movies:
        if float(x.get('imdb')) > 5.5:
            print(x.get('name'), '-', x.get('imdb'))



def categ(category):
    print('List of {} :'.format(category))
    a = True
    for x in movies:
        if x.get('category').lower() == category:
            print(x.get('name'), '-', x.get('imdb'))
            a=False
    if a: print('We dont have such category in our list :(')


def aver():
    sum, cnt =0, 0
    for x in movies:
        sum += float(x.get('imdb'))
        cnt+=1
    print ('Average of out list if movies', '-', "%.2f" % (sum/cnt))


def aver_categ(category):
    sum, cnt, a = 0, 0, True
    for x in movies:
        if x.get('category').lower() == category:
            sum += float(x.get('imdb'))
            cnt+=1
            a = False
    if a: 
        print('We dont have such category in our list :(')
        return False   
    print ('Average of {}'.format(category), '-', "%.2f" % (sum/cnt))


print('Hello, dear User, what do you want today?')
dis =''
while dis != '6':
    dis = input('''
Choose the command:
1 - Define quality of movie
2 - Show list of good films
3 - Suggest a movie of a certain category
4 - Show average of our list of movies
5 - Show average of category of movies
6 - exit
I want: ''')
    print()
    if dis == '1': good_mov(input('Print your movie: ').lower())
    elif dis == '2':  list_of_mov()
    elif dis == '3': categ(input('Print your category: ').lower())
    elif dis == '4': aver()
    elif dis =='5': aver_categ(input('Print your category: ').lower())
    else: exit()


